# =============================================================================
# extra.py — subdecks beside the levels, each for a group of animals
#
# A recipe's levels hold its main taxa (fishes, say) by frequency. An extra
# subdeck holds another group — the invertebrates and corals of a reef deck
# — from the same order source and region, with its own taxa, size and,
# where they differ, filters that override the recipe's one by one. It gets
# the same treatment as the levels: the iNaturalist name mapping, the
# resolution against the reference DB, the evidence a highlight needs, the
# exclusions by hand. A species already on a level (or in an earlier extra
# subdeck) stays out of it, so every species is in one subdeck only; the
# taxa may overlap (molluscs include the cephalopods of the levels).
#
# Only the order source inat is supported: it is the one that asks for
# taxa. The guides are fish guides and are not compared here.
# =============================================================================

from dataclasses import dataclass

from . import inat, inat_names, obis
from .checks import LANGUAGES, run_checks
from .recipe import RecipeError
from .deck import deck_name
from .selection import Evidence, counts_by_id, select, split_extra


@dataclass
class ExtraResult:
    spec: dict          # the recipe's entry in extraSubdecks
    selection: object   # selection.Selection, one level
    resolution: dict
    facts: dict
    flags: dict
    evidence: dict
    names: dict         # species id → deck name
    mapped: list        # [inat_names.Applied]
    notes: list
    checks: object      # checks.Checks of the subdeck's species
    classes: dict       # species id → class name

    @property
    def ids(self):
        return self.selection.levels[0]


def filters_of(recipe, spec):
    """The recipe's filters with the subdeck's on top, key by key."""
    return {**recipe.get("filters", {}), **spec.get("filters", {})}


def build_extra(recipe, spec, fetcher, db, water, name_map, taken):
    """The selection of the extra subdeck `spec`; `taken` maps the ids
    already in a subdeck to that subdeck's id."""
    region = recipe.get("region", {})
    result = inat.species_counts(fetcher, region.get("inat"), spec["taxa"]["inat"])
    counts, mapped = inat_names.apply(result.counts, name_map)
    notes = list(result.notes)
    obis_counts = []
    if "obis" in region and "obis" in spec["taxa"]:
        checklist = obis.checklist(fetcher, [area["wkt"] for area in region["obis"]], spec["taxa"]["obis"])
        obis_counts = checklist.counts
        notes += checklist.notes

    highlights = [h["name"] for h in spec.get("highlights", [])]
    excludes = [e["name"] for e in spec.get("exclude", [])]
    resolution = db.resolve({n for n, _ in counts} | {n for n, _ in obis_counts} | set(highlights) | set(excludes))
    both = {resolution[n] for n in highlights if resolution[n]} & {resolution[n] for n in excludes if resolution[n]}
    if both:
        raise RecipeError(f"Subdeck {spec['id']}: Highlight und von Hand ausgeschlossen zugleich: "
                          + ", ".join(sorted(n for n in highlights if resolution[n] in both)))
    facts = db.species(i for i in resolution.values() if i)
    flags = {i: water.get((f.source, f.external_id)) for i, f in facts.items()}
    order_by_id = counts_by_id(counts, resolution)
    obis_by_id = counts_by_id(obis_counts, resolution)
    relevant = set(order_by_id) | {resolution[h] for h in highlights if resolution[h]}
    occurrences = db.occurrences(relevant, region.get("fishbase", []))
    evidence = {
        i: Evidence(order_count=order_by_id.get(i), obis_records=obis_by_id.get(i), occurrences=occurrences.get(i, []))
        for i in facts
    }

    sub_recipe = {"filters": filters_of(recipe, spec), "highlights": spec.get("highlights", []),
                  "exclude": spec.get("exclude", [])}
    selection = select(counts, resolution, facts, flags, evidence, sub_recipe, sum, taken=taken,
                       split=lambda ranked, highlights: split_extra(ranked, highlights, spec["size"]))
    source_names = {i: c.names for i, c in selection.candidates.items()}
    for name in highlights:
        if resolution[name]:
            source_names.setdefault(resolution[name], [name])
    names = {i: deck_name(f, source_names.get(i, [])) for i, f in facts.items()}

    ids = selection.levels[0]
    family_of = db.families(ids)
    checks = run_checks(
        ids, evidence, db.common_names(ids, LANGUAGES), family_of,
        db.common_names({f for f, _ in family_of.values()}, LANGUAGES), db.shared_scientific_names(ids),
    )
    return ExtraResult(spec, selection, resolution, facts, flags, evidence, names, mapped, notes, checks,
                       db.classes(ids))
