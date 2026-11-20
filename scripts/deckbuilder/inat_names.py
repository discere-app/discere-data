# =============================================================================
# inat_names.py — iNaturalist names the reference DB knows under another name
#
# iNaturalist follows renames and splits (Catalog of Fishes, new genera of
# cuttlefish and gobies) before FishBase and SeaLifeBase do. An observation
# under the new name resolves to nothing in the reference DB, and the
# species drops out of a deck without a word: the Hawaiian convict tang,
# Acanthurus sandvicensis for iNaturalist, is Acanthurus triostegus in the
# reference DB and the most observed fish of Hawaii.
#
# recipes/inat_names.json maps such names, each entry with its reason and
# the iNaturalist taxon change as evidence (schema/inat_names.schema.json).
# The mapping applies to the counts of the order source inat before they
# are resolved, so the counts of both names add up.
# =============================================================================

import json
import os
from dataclasses import dataclass

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

from .recipe import SCHEMA_DIR, RecipeError


@dataclass
class Applied:
    entry: dict    # the entry of the mapping file
    count: float   # the count iNaturalist gave under entry["inat"]


def _validator():
    schemas = []
    for name in ("inat_names.schema.json", "deck.schema.json"):
        with open(os.path.join(SCHEMA_DIR, name), encoding="utf-8") as f:
            schemas.append(json.load(f))
    registry = Registry().with_resources([(s["$id"], Resource.from_contents(s)) for s in schemas])
    return Draft202012Validator(schemas[0], registry=registry, format_checker=FormatChecker())


def load(path):
    """The entries of the mapping file at `path`, checked against the schema;
    a missing file means no entries."""
    if not os.path.exists(path):
        return []
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        raise RecipeError(f"{path}: {e}") from e
    errors = sorted(_validator().iter_errors(data), key=lambda e: list(e.absolute_path))
    if errors:
        lines = [f"  {'/'.join(map(str, e.absolute_path)) or '(Wurzel)'}: {e.message}" for e in errors]
        raise RecipeError(f"{path} passt nicht zu schema/inat_names.schema.json:\n" + "\n".join(lines))
    seen = set()
    for entry in data["names"]:
        if entry["inat"] in seen:
            raise RecipeError(f"{path}: {entry['inat']} steht zweimal")
        seen.add(entry["inat"])
    return data["names"]


def apply(counts, entries):
    """The counts [(name, count)] with every mapped name replaced by its
    reference-DB name, and the entries that applied with their count. The
    order of the names is kept; a mapped name adds to its target's count."""
    by_name = {entry["inat"]: entry for entry in entries}
    merged, applied = {}, []
    for name, count in counts:
        entry = by_name.get(name)
        if entry:
            applied.append(Applied(entry, count))
            name = entry["referenceDb"]
        merged[name] = merged.get(name, 0) + count
    return list(merged.items()), applied
