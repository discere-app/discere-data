# =============================================================================
# build.py — one run of the deckbuilder: recipe in, deck and report out
#
# Asks the sources the recipe names, resolves every name against the
# reference DB, selects (deckbuilder/selection.py) and writes
# data/decks/<base>.json and recipes/<base>.report.md, the report next to
# the recipe. The deck is checked against schema/deck.schema.json before
# anything is written.
#
# Exit codes:
#   0  deck and report written
#   1  stopped, nothing written: invalid recipe, unreadable input, a source
#      or the reference DB not reachable
#   2  deck and report written, but a highlight stayed out for lack of
#      evidence or of a name the reference DB knows. The deck is written
#      anyway: it holds only species with evidence, and the report, which is
#      what it takes to decide about the highlight, is complete only with
#      the deck it describes. The exit code keeps the run from passing
#      unnoticed.
#
# run() takes the fetcher, the reference DB and the water flags as
# arguments, so the tests hand in recorded answers and a small database.
# =============================================================================

import json
import os
import sys

from jsonschema import Draft202012Validator, FormatChecker

from . import gbif, guide, inat, obis, reef_csv
from .deck import build_deck, deck_name, deck_sources
from .recipe import SCHEMA_DIR, RecipeError
from .recipe import load as load_recipe
from .report import Report
from .selection import Evidence, select

EXIT_OK, EXIT_STOPPED, EXIT_HIGHLIGHT_REJECTED = 0, 1, 2


class BuildError(Exception):
    pass


def order_counts(recipe, fetcher, db):
    """The order source's counts and how two names of one species combine."""
    source = recipe["order"]["source"]
    if source == "inat":
        region = recipe["region"]["inat"] if "region" in recipe else None
        return inat.species_counts(fetcher, region, recipe["taxa"]["inat"]), sum
    if source == "gbif":
        result = gbif.species_counts(
            fetcher, recipe["region"]["gbif"]["countries"], recipe["taxa"]["gbif"]["phylumKey"],
            db.fishbase_order_names(),
        )
        return result, sum
    try:
        return reef_csv.sighting_frequencies(recipe["order"]["csv"]), max
    except (OSError, reef_csv.ReefCsvError) as e:
        raise BuildError(str(e)) from e


def read_guides(recipe):
    guides = []
    for entry in recipe.get("guides", []):
        try:
            guides.append((entry, guide.read_names(entry["path"])))
        except OSError as e:
            raise BuildError(f"Führer '{entry['name']}': {e}") from e
    return guides


def counts_by_id(counts, resolution):
    by_id = {}
    for name, count in counts:
        species_id = resolution.get(name)
        if species_id is not None:
            by_id[species_id] = by_id.get(species_id, 0) + count
    return by_id


def describe_areas(recipe, fetcher):
    """[(source, areas)] for the report, the iNaturalist places by name."""
    region = recipe.get("region")
    if region is None:
        return [("Region", "weltweit (iNaturalist ohne Ort; keine Verbreitungsdaten als Nachweis)")]
    areas = []
    if "inat" in region:
        if "placeIds" in region["inat"]:
            names = inat.place_names(fetcher, region["inat"]["placeIds"])
            text = ", ".join(f"{names.get(i, '?')} ({i})" for i in region["inat"]["placeIds"])
        else:
            r = region["inat"]
            text = f"Rechteck {r['swlat']}/{r['swlng']} bis {r['nelat']}/{r['nelng']} (Breite/Länge)"
        areas.append(("iNaturalist", text))
    if "gbif" in region:
        areas.append(("GBIF", ", ".join(region["gbif"]["countries"])))
    if "obis" in region:
        areas.append(("OBIS", ", ".join(area["name"] for area in region["obis"])))
    if "fishbase" in region:
        areas.append(("FishBase/SeaLifeBase-Verbreitung", ", ".join(region["fishbase"])))
    return areas


def check_deck(deck):
    with open(os.path.join(SCHEMA_DIR, "deck.schema.json"), encoding="utf-8") as f:
        schema = json.load(f)
    errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(deck))
    if errors:
        raise BuildError("das erzeugte Deck passt nicht zu schema/deck.schema.json: "
                         + "; ".join(e.message for e in errors))


def run(recipe_path, decks_dir, fetcher, db, water, meta=()):
    """Builds the deck of the recipe at `recipe_path`; returns the exit
    code. `water` maps (source, SpecCode) to the flag triple."""
    try:
        recipe = load_recipe(recipe_path)
        base = os.path.splitext(os.path.basename(recipe_path))[0]
        deck_path = os.path.join(decks_dir, f"{base}.json")
        report_path = os.path.join(os.path.dirname(os.path.abspath(recipe_path)), f"{base}.report.md")
        existing = None
        if os.path.exists(deck_path):
            with open(deck_path, encoding="utf-8") as f:
                existing = json.load(f)

        order, combine = order_counts(recipe, fetcher, db)
        notes = list(order.notes)
        obis_counts = []
        region = recipe.get("region", {})
        if "obis" in region:
            result = obis.checklist(fetcher, [area["wkt"] for area in region["obis"]], recipe["taxa"]["obis"])
            obis_counts = result.counts
            notes += result.notes
        guides = read_guides(recipe)

        all_names = {name for name, _ in order.counts} | {name for name, _ in obis_counts}
        all_names |= set(recipe.get("highlights", []))
        for _, names in guides:
            all_names |= set(names)
        resolution = db.resolve(all_names)
        facts = db.species(i for i in resolution.values() if i)
        flags = {i: water.get((f.source, f.external_id)) for i, f in facts.items()}

        order_by_id = counts_by_id(order.counts, resolution)
        obis_by_id = counts_by_id(obis_counts, resolution)
        guide_ids = [{resolution[n] for n in names if resolution[n]} for _, names in guides]
        relevant = set(order_by_id) | {resolution[h] for h in recipe.get("highlights", []) if resolution[h]}
        occurrences = db.occurrences(relevant, region.get("fishbase", []))
        evidence = {
            i: Evidence(
                order_count=order_by_id.get(i),
                obis_records=obis_by_id.get(i),
                occurrences=occurrences.get(i, []),
                guides=[g["name"] for (g, _), ids in zip(guides, guide_ids) if i in ids],
            )
            for i in facts
        }

        selection = select(order.counts, resolution, facts, flags, evidence, recipe, combine)
        source_names = {i: c.names for i, c in selection.candidates.items()}
        for name in recipe.get("highlights", []):
            if resolution[name]:
                source_names.setdefault(resolution[name], [name])
        names = {i: deck_name(f, source_names.get(i, [])) for i, f in facts.items()}

        levels = [[names[i] for i in level] for level in selection.levels]
        used = {facts[i].source for level in selection.levels for i in level}
        deck = build_deck(recipe, levels, deck_sources(recipe, used), existing)
        check_deck(deck)

        guide_reports = [
            (g, ids, [n for n in names_ if not resolution[n]], len(names_))
            for (g, names_), ids in zip(guides, guide_ids)
        ]
        report = Report(
            recipe, base, selection, names, facts, flags, evidence, guide_reports, notes, list(meta),
            existing.get("speciesNames") if existing else None, describe_areas(recipe, fetcher),
        ).render()
    except (RecipeError, BuildError, RuntimeError) as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return EXIT_STOPPED

    os.makedirs(decks_dir, exist_ok=True)
    with open(deck_path, "w", encoding="utf-8") as f:
        json.dump(deck, f, indent=2, ensure_ascii=False)
        f.write("\n")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)

    counts = "/".join(str(len(level)) for level in selection.levels)
    print(f"{deck_path}: {len(deck['speciesNames'])} Arten ({counts})")
    print(f"{report_path}: Bericht")
    if selection.unresolved:
        print(f"[WARN] {len(selection.unresolved)} Namen der Reihenfolge-Quelle nicht aufgelöst (siehe Bericht)")
    if existing is None:
        print(f"[TODO] {base}.json ist neu: Vor dem PR die Grenzfälle im Bericht durchsehen.")
    if selection.rejected_highlights:
        for name, reason in selection.rejected_highlights:
            print(f"[ERROR] Highlight {name} nicht im Deck: {reason}", file=sys.stderr)
        return EXIT_HIGHLIGHT_REJECTED
    return EXIT_OK
