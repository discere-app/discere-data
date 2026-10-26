#!/usr/bin/env python3
# =============================================================================
# validate_decks.py — alle Deck-Dateien gegen schema/deck.schema.json prüfen
#
# Läuft in CI bei jedem PR (.github/workflows/validate-decks.yml) und lokal:
#   pip install "jsonschema[format]"
#   python3 scripts/validate_decks.py
#
# Zusätzlich zum Schema prüft es, was JSON Schema nicht ausdrücken kann:
#   - Subdecks enthalten nur Arten aus speciesNames,
#   - jede Art steht in höchstens einem Subdeck,
#   - Subdeck-ids sind innerhalb eines Decks eindeutig,
#   - sourceIds sind über alle Decks eindeutig, und kein Deck löst sich
#     selbst oder ein Deck ab, das noch im Katalog steht.
# Exit-Code 1, wenn etwas nicht stimmt.
# =============================================================================

import glob
import json
import os
import sys

from jsonschema import Draft202012Validator, FormatChecker

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
DECKS_DIR = os.path.join(ROOT, "data", "decks")
SCHEMA_FILE = os.path.join(ROOT, "schema", "deck.schema.json")


def deck_files():
    return sorted(
        p for p in glob.glob(os.path.join(DECKS_DIR, "*.json"))
        if os.path.basename(p) != "index.json"
    )


def check_subdecks(deck):
    errors = []
    subdecks = deck.get("subdecks") or []
    all_names = set(deck.get("speciesNames") or [])
    ids, placed = set(), {}
    for subdeck in subdecks:
        if subdeck["id"] in ids:
            errors.append(f"Subdeck-id '{subdeck['id']}' kommt mehrfach vor")
        ids.add(subdeck["id"])
        for name in subdeck["speciesNames"]:
            if name not in all_names:
                errors.append(f"'{name}' steht in Subdeck '{subdeck['id']}', aber nicht in speciesNames")
            if name in placed:
                errors.append(f"'{name}' steht in Subdeck '{placed[name]}' und '{subdeck['id']}'")
            placed.setdefault(name, subdeck["id"])
    return errors


def main():
    with open(SCHEMA_FILE, encoding="utf-8") as f:
        validator = Draft202012Validator(json.load(f), format_checker=FormatChecker())

    problems = {}
    decks = {}
    for path in deck_files():
        name = os.path.basename(path)
        try:
            with open(path, encoding="utf-8") as f:
                deck = json.load(f)
        except json.JSONDecodeError as e:
            problems[name] = [f"kein gültiges JSON: {e}"]
            continue
        errors = [
            f"{'/'.join(map(str, e.absolute_path)) or '(Wurzel)'}: {e.message}"
            for e in sorted(validator.iter_errors(deck), key=lambda e: list(e.absolute_path))
        ]
        if not errors:
            errors = check_subdecks(deck)
            decks[name] = deck
        if errors:
            problems[name] = errors

    owners = {}
    for name, deck in decks.items():
        if "sourceId" in deck:
            owners.setdefault(deck["sourceId"], []).append(name)
    for source_id, names in owners.items():
        if len(names) > 1:
            for name in names:
                problems.setdefault(name, []).append(f"sourceId {source_id} teilen sich {', '.join(names)}")
    for name, deck in decks.items():
        for source_id in deck.get("supersedes") or []:
            if source_id == deck.get("sourceId"):
                problems.setdefault(name, []).append("supersedes nennt die eigene sourceId")
            elif source_id in owners:
                problems.setdefault(name, []).append(
                    f"supersedes nennt {source_id}, das noch als {', '.join(owners[source_id])} im Katalog steht"
                )

    for name, errors in sorted(problems.items()):
        print(f"✗ {name}")
        for error in errors:
            print(f"    {error}")
    print(f"{len(deck_files())} Decks geprüft, {len(problems)} mit Fehlern")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
