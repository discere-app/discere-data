#!/usr/bin/env python3
# =============================================================================
# apply_corrections.py — LLM-Korrekturen auf Discere Deck-JSONs anwenden
#
# Usage:
#   python apply_corrections.py <corrections.json> <base_name> [--out-dir DIR] [--dry-run]
#
# Beispiel:
#   python apply_corrections.py kanare_madeira_azoren_corrections.json kanare_madeira_azoren
#   python apply_corrections.py corrections.json kanare_madeira_azoren --out-dir generated
#
# Outputs:
#   <base>_level1_corrected.json
#   <base>_level2_corrected.json
#   <base>_level3_corrected.json
#   <base>_corrections_log.txt
# =============================================================================

import json
import sys
import os
import argparse
from datetime import datetime
from copy import deepcopy

def normalize(name):
    return name.strip().lower()

def find_level(decks, species):
    for level, deck in decks.items():
        if any(normalize(s) == normalize(species) for s in deck["speciesNames"]):
            return level
    return None

def level_key(level_str):
    mapping = {"L1": "level1", "L2": "level2", "L3": "level3"}
    key = mapping.get(level_str.upper() if level_str else "")
    if not key:
        print(f"[ERROR] Ungültiger Level-Wert: {level_str}", file=sys.stderr)
        sys.exit(1)
    return key

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("corrections_file")
    parser.add_argument("base_name")
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--source", default="ChatGPT", help="Name der LLM-Quelle (default: ChatGPT)")
    args = parser.parse_args()

    out_dir = args.out_dir or os.path.dirname(os.path.abspath(args.corrections_file))
    base = args.base_name

    # --- Dateien laden ---
    if not os.path.exists(args.corrections_file):
        print(f"[ERROR] Korrekturen-Datei nicht gefunden: {args.corrections_file}", file=sys.stderr)
        sys.exit(1)

    with open(args.corrections_file) as f:
        corrections = json.load(f)

    decks = {}
    for level in ["level1", "level2", "level3"]:
        path = os.path.join(out_dir, f"{base}_{level}.json")
        if not os.path.exists(path):
            print(f"[ERROR] Deck nicht gefunden: {path}", file=sys.stderr)
            sys.exit(1)
        with open(path) as f:
            decks[level] = json.load(f)

    # Arbeitskopie
    decks = deepcopy(decks)

    additions = corrections.get("additions", [])
    level_corrections = corrections.get("level_corrections", [])
    log = []

    def log_line(line=""):
        print(line)
        log.append(line)

    log_line("=" * 60)
    log_line(f"Korrekturen-Log: {base}")
    log_line(f"Datei: {args.corrections_file}")
    log_line(f"Zeitstempel: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_line("=" * 60)
    log_line()

    # --- Level-Korrekturen ---
    log_line(f"LEVEL-KORREKTUREN ({len(level_corrections)})")
    log_line("-" * 40)

    for c in level_corrections:
        species  = c.get("speciesName", "").strip()
        current  = c.get("current_level")
        suggested = c.get("suggested_level")
        reason   = c.get("reason", "")

        if not current or not suggested or current == "null" or suggested == "null":
            log_line(f"[SKIP] {species} – current_level oder suggested_level ist null, übersprungen")
            continue

        if current.upper() == suggested.upper():
            log_line(f"[SKIP] {species} – current und suggested Level identisch ({current})")
            continue

        actual = find_level(decks, species)
        if not actual:
            log_line(f"[SKIP] {species} – nicht im Deck gefunden, übersprungen")
            continue

        current_key  = level_key(current)
        suggested_key = level_key(suggested)

        if actual != current_key:
            log_line(f"[WARN] {species} – erwartet auf {current}, gefunden auf {actual.replace('level', 'L')} – trotzdem verschoben")

        decks[actual]["speciesNames"] = [
            s for s in decks[actual]["speciesNames"] if normalize(s) != normalize(species)
        ]
        decks[suggested_key]["speciesNames"].append(species)

        log_line(f"[OK]   {species}: {actual.replace('level', 'L')} → {suggested}")
        log_line(f"       Grund: {reason}")
        log_line()

    # --- Additions ---
    log_line()
    log_line(f"ADDITIONS ({len(additions)})")
    log_line("-" * 40)

    for a in additions:
        species  = a.get("speciesName", "").strip()
        level    = a.get("level")
        criteria = ", ".join(a.get("criteria") or [])
        reason   = a.get("reason", "")

        if not level or level == "null":
            log_line(f"[SKIP] {species} – kein Level angegeben")
            continue

        existing = find_level(decks, species)
        if existing:
            log_line(f"[SKIP] {species} – bereits auf {existing.replace('level', 'L')} vorhanden, nicht hinzugefügt")
            continue

        target = level_key(level)
        decks[target]["speciesNames"].append(species)

        log_line(f"[OK]   {species} → {level} hinzugefügt")
        log_line(f"       Kriterien: {criteria}")
        log_line(f"       Grund: {reason}")
        log_line()

    # --- Zusammenfassung ---
    log_line()
    log_line("=" * 60)
    log_line("ZUSAMMENFASSUNG")
    log_line("-" * 40)
    for level, deck in decks.items():
        log_line(f"{level.replace('level', 'Level ')}: {len(deck['speciesNames'])} Arten")
    log_line("=" * 60)

    # --- Source-Eintrag ergänzen ---
    source_urls = {
        "ChatGPT": "https://openai.com/chatgpt",
        "Claude":  "https://claude.ai",
        "Gemini":  "https://gemini.google.com",
    }
    source_entry = {
        "name": args.source,
        "url": source_urls.get(args.source, "")
    }
    for deck in decks.values():
        existing_sources = [s.get("name") for s in deck.get("sources", [])]
        if args.source not in existing_sources:
            deck.setdefault("sources", []).append(source_entry)

    # --- Ausgabe ---
    if args.dry_run:
        print("\n[DRY-RUN] Keine Dateien geschrieben.")
    else:
        for level, deck in decks.items():
            out_file = os.path.join(out_dir, f"{base}_{level}_corrected.json")
            with open(out_file, "w") as f:
                json.dump(deck, f, indent=2, ensure_ascii=False)
            print(f"geschrieben: {out_file}")

        log_file = os.path.join(out_dir, f"{base}_corrections_log.txt")
        with open(log_file, "w") as f:
            f.write("\n".join(log))
        print(f"Log: {log_file}")

if __name__ == "__main__":
    main()