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
#   2  deck and report written, but a highlight (of a level or an extra
#      subdeck) stayed out for lack of
#      evidence or of a name the reference DB knows. The deck is written
#      anyway: it holds only species with evidence, and the report, which is
#      what it takes to decide about the highlight, is complete only with
#      the deck it describes. The exit code keeps the run from passing
#      unnoticed.
#
# run() takes the fetcher, the reference DB, the water flags and the
# entries of recipes/inat_names.json as arguments, so the tests hand in
# recorded answers and a small database.
# =============================================================================

import json
import os
import sys

from jsonschema import Draft202012Validator, FormatChecker

from . import findings, gbif, guide, inat, inat_names, obis, reef_csv, signals
from .checks import LANGUAGES, run_checks
from .deck import build_deck, deck_names, deck_sources
from .recipe import SCHEMA_DIR, RecipeError
from .recipe import exclude_names, highlight_names
from .recipe import load as load_recipe
from .report import Report
from .extra import build_extra
from .selection import Evidence, counts_by_id, select
from .sources import SourceResult

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


def check_names(db, written):
    """Every written name (name → species id) resolves to its species
    through the reference DB's species_name_lookup, as the app resolves it."""
    resolved = db.resolve(written)
    wrong = sorted(name for name, species_id in written.items() if resolved[name] != species_id)
    if wrong:
        raise BuildError("diese Namen löst die App nicht zu ihrer Art auf: " + ", ".join(wrong))


def check_deck(deck):
    with open(os.path.join(SCHEMA_DIR, "deck.schema.json"), encoding="utf-8") as f:
        schema = json.load(f)
    errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(deck))
    if errors:
        raise BuildError("das erzeugte Deck passt nicht zu schema/deck.schema.json: "
                         + "; ".join(e.message for e in errors))


def run(recipe_path, decks_dir, fetcher, db, water, meta=(), name_map=()):
    """Builds the deck of the recipe at `recipe_path`; returns the exit
    code. `water` maps (source, SpecCode) to the flag triple, `name_map`
    holds the entries of recipes/inat_names.json."""
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
        source = order  # before the name mapping: its taxon ids are iNaturalist's
        notes = list(order.notes)
        mapped = None
        regional = recipe["order"]["source"] == "inat"
        if regional:
            counts, mapped = inat_names.apply(order.counts, name_map)
            order = SourceResult(counts, order.notes)
        obis_counts = []
        region = recipe.get("region", {})
        if "obis" in region:
            result = obis.checklist(fetcher, [area["wkt"] for area in region["obis"]], recipe["taxa"]["obis"])
            obis_counts = result.counts
            notes += result.notes
        guides = read_guides(recipe)

        all_names = {name for name, _ in order.counts} | {name for name, _ in obis_counts}
        all_names |= set(highlight_names(recipe)) | set(exclude_names(recipe))
        for _, names in guides:
            all_names |= set(names)
        resolution = db.resolve(all_names)
        both = {resolution[n] for n in highlight_names(recipe) if resolution[n]} \
            & {resolution[n] for n in exclude_names(recipe) if resolution[n]}
        if both:
            raise BuildError("Highlight und von Hand ausgeschlossen zugleich: "
                             + ", ".join(sorted(n for n in highlight_names(recipe) if resolution[n] in both)))
        facts = db.species(i for i in resolution.values() if i)
        flags = {i: water.get((f.source, f.external_id)) for i, f in facts.items()}

        order_by_id = counts_by_id(order.counts, resolution)
        obis_by_id = counts_by_id(obis_counts, resolution)
        guide_ids = [{resolution[n] for n in names if resolution[n]} for _, names in guides]
        relevant = set(order_by_id) | {resolution[h] for h in highlight_names(recipe) if resolution[h]}
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
        names = deck_names(facts, selection.candidates, highlight_names(recipe), resolution, regional)
        t = findings.thresholds(recipe)
        found_signals = None
        if regional:
            observed = [i for level in selection.levels[:2] for i in level] + selection.highlights
            found_signals = signals.collect(fetcher, region.get("inat"), recipe["taxa"]["inat"], source, name_map,
                                            resolution, observed, t["fewObservers"])
        subdeck_of = {i: f"level-{n}" for n, level in enumerate(selection.levels, 1) for i in level}
        found = findings.find(subdeck_of, evidence, found_signals, t)

        taken = dict(subdeck_of)
        extras = []
        extra_ids = [spec["id"] for spec in recipe.get("extraSubdecks", [])]
        if len(set(extra_ids)) < len(extra_ids):
            raise BuildError("zwei zusätzliche Subdecks mit derselben id: " + ", ".join(extra_ids))
        for spec in recipe.get("extraSubdecks", []):
            extra = build_extra(recipe, spec, fetcher, db, water, name_map, taken)
            taken.update((i, spec["id"]) for i in extra.ids)
            extras.append(extra)
            found += extra.findings

        check_names(db, {names[i]: i for level in selection.levels for i in level}
                    | {e.names[i]: i for e in extras for i in e.ids})
        levels = [[names[i] for i in level] for level in selection.levels]
        used = {facts[i].source for level in selection.levels for i in level}
        used |= {e.facts[i].source for e in extras for i in e.ids}
        deck = build_deck(recipe, levels, deck_sources(recipe, used), existing,
                          [(e.spec, [e.names[i] for i in e.ids]) for e in extras])
        check_deck(deck)

        deck_ids = [i for level in selection.levels for i in level]
        family_of = db.families(deck_ids)
        checks = run_checks(
            deck_ids, evidence, db.common_names(deck_ids, LANGUAGES), family_of,
            db.common_names({f for f, _ in family_of.values()}, LANGUAGES), db.shared_scientific_names(deck_ids),
        )

        guide_reports = [
            (g, ids, [n for n in names_ if not resolution[n]], len(names_))
            for (g, names_), ids in zip(guides, guide_ids)
        ]
        report = Report(
            recipe, base, selection, names, facts, flags, evidence, guide_reports, notes, list(meta),
            existing.get("speciesNames") if existing else None, describe_areas(recipe, fetcher),
            resolution, checks, mapped, extras, found,
            found_signals.observers if found_signals else {},
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
    counts += "".join(f" + {e.spec['id']} {len(e.ids)}" for e in extras)
    print(f"{deck_path}: {len(deck['speciesNames'])} Arten ({counts})")
    print(f"{report_path}: Bericht")
    for name, why in selection.unused_excludes:
        print(f"[WARN] Ausschluss {name} wirkt nicht: {why}")
    for e in extras:
        for name, why in e.selection.unused_excludes:
            print(f"[WARN] Subdeck {e.spec['id']}: Ausschluss {name} wirkt nicht: {why}")
    if found:
        by_kind = ", ".join(f"{kind} {n}" for kind in findings.KINDS if (n := sum(f.kind == kind for f in found)))
        print(f"[WARN] Zu entscheiden: {len(found)} Warnungen ({by_kind}), siehe Bericht")
    if selection.unresolved:
        print(f"[WARN] {len(selection.unresolved)} Namen der Reihenfolge-Quelle nicht aufgelöst (siehe Bericht)")
    if existing is None:
        print(f"[TODO] {base}.json ist neu: Vor dem PR die Grenzfälle im Bericht durchsehen.")
    rejected = list(selection.rejected_highlights)
    rejected += [(f"{name} (Subdeck {e.spec['id']})", reason) for e in extras for name, reason in e.selection.rejected_highlights]
    if rejected:
        for name, reason in rejected:
            print(f"[ERROR] Highlight {name} nicht im Deck: {reason}", file=sys.stderr)
        return EXIT_HIGHLIGHT_REJECTED
    return EXIT_OK
