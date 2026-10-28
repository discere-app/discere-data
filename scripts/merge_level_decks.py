#!/usr/bin/env python3
# =============================================================================
# merge_level_decks.py — merge level decks into one deck with subdecks
#
# The generators under scripts/reef/ produce three level files per region
# (<base>_level1.json … <base>_level3.json). The app keeps one deck with
# subdecks: one deck per region, each level a subdeck the user can switch
# off on its own. This script turns the level files into that one deck of
# format 2. The level files stay: they are format 1, so they stay in
# data/decks/index.json for app versions without subdecks, and leave the
# indexes from format 2 on, where the merged deck supersedes them. They go
# once the format-1 index is retired.
#
# Format of the result (see docs/architecture-overview.md §7.5 in the
# app repo):
#   formatVersion 2 — subdecks and supersedes need it.
#   speciesNames  union of all levels — app versions without subdecks
#                 import the deck from it as a flat list.
#   subdecks      [{id, name, speciesNames}] per level; the id is stable
#                 ("level-1" …), an update recognizes the subdeck by it.
#   supersedes    the sourceIds of the level decks: whoever imported them
#                 is offered to merge them in the app and keeps their
#                 learning progress.
# scripts/sync_index.sh assigns a new sourceId after the merge into main.
#
# Usage:
#   python scripts/merge_level_decks.py <base> [<base> …] [--decks-dir DIR]
#
# Example:
#   python scripts/merge_level_decks.py mittelmeer rotesmeer
# =============================================================================

import argparse
import glob
import json
import os
import re
import sys

LEVEL_SUFFIX = re.compile(r"\s*-\s*Level\s*\d+\s*$")


def load_levels(decks_dir, base):
    paths = sorted(
        glob.glob(os.path.join(decks_dir, f"{base}_level*.json")),
        key=lambda p: int(re.search(r"_level(\d+)\.json$", p).group(1)),
    )
    if not paths:
        sys.exit(f"[ERROR] keine Level-Dateien für '{base}' in {decks_dir}")
    levels = []
    for path in paths:
        with open(path, encoding="utf-8") as f:
            levels.append(json.load(f))
    return levels


def merged_description(decks):
    descriptions = [d["description"] for d in decks]
    if len(set(descriptions)) == 1:
        return descriptions[0]
    return " · ".join(f"Level {i}: {text}" for i, text in enumerate(descriptions, 1))


def merge(decks, base):
    first = decks[0]
    for key in ("imageUrl", "sources", "createdBy"):
        if any(d.get(key) != first.get(key) for d in decks):
            sys.exit(f"[ERROR] '{base}': Feld '{key}' unterscheidet sich zwischen den Levels")
    missing = [i for i, d in enumerate(decks, 1) if not d.get("sourceId")]
    if missing:
        sys.exit(f"[ERROR] '{base}': Level {missing} ohne sourceId — erst sync_index.sh laufen lassen")

    union, seen, subdecks = [], set(), []
    for level, deck in enumerate(decks, 1):
        names = []
        for name in deck["speciesNames"]:
            if name in seen:
                print(f"[WARN] '{base}': {name} steht in mehreren Levels, bleibt im ersten")
                continue
            seen.add(name)
            names.append(name)
        union.extend(names)
        subdecks.append({"id": f"level-{level}", "name": f"Level {level}", "speciesNames": names})

    merged = {
        "formatVersion": 2,
        "name": LEVEL_SUFFIX.sub("", first["name"]),
        "description": merged_description(decks),
        "imageUrl": first.get("imageUrl", ""),
        "sources": first.get("sources", []),
    }
    if first.get("createdBy"):
        merged["createdBy"] = first["createdBy"]
    merged["speciesNames"] = union
    merged["subdecks"] = subdecks
    merged["supersedes"] = [d["sourceId"] for d in decks]
    return merged


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("bases", nargs="+", help="Dateiname ohne _levelN.json")
    parser.add_argument("--decks-dir", default=os.path.join(os.path.dirname(__file__), "..", "data", "decks"))
    args = parser.parse_args()

    for base in args.bases:
        merged = merge(load_levels(args.decks_dir, base), base)
        out = os.path.join(args.decks_dir, f"{base}.json")
        if os.path.exists(out):
            sys.exit(f"[ERROR] {out} existiert bereits")
        with open(out, "w", encoding="utf-8") as f:
            json.dump(merged, f, indent=2, ensure_ascii=False)
            f.write("\n")
        counts = "/".join(str(len(s["speciesNames"])) for s in merged["subdecks"])
        print(f"{base}.json: {merged['name']} — {len(merged['speciesNames'])} Arten ({counts})")


if __name__ == "__main__":
    main()
