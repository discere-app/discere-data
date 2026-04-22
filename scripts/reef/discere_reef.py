#!/usr/bin/env python3
# =============================================================================
# discere_reef.py — REEF CSV -> Discere deck JSONs (Wizard)
#
# Abhängigkeiten:
#   pip install duckdb
#
# Usage:
#   python discere_reef.py reef.csv
#   python discere_reef.py reef.csv --out-dir generated
#   python discere_reef.py reef.csv --region-name "Mittelmeer"
#   python discere_reef.py reef.csv --version v25.04
#   python discere_reef.py reef.csv --fishbase-dir ./fb/parquet --slb-dir ./slb/parquet
#
# Ablauf:
#   1. REEF CSV einlesen & gegen FishBase/SeaLifeBase auflösen
#   2. Prompt B anzeigen → in ChatGPT einfügen
#   3. ChatGPT-Output hier einfügen
#   4. Korrekturen anwenden & alle JSONs schreiben
# =============================================================================

import argparse
import csv
import json
import math
import os
import re
import sys
import tempfile
from copy import deepcopy
from datetime import datetime

try:
    import duckdb
except ImportError:
    print("[ERROR] duckdb nicht gefunden. Installation: pip install duckdb", file=sys.stderr)
    sys.exit(1)


SOURCES = [
    {"name": "REEF",        "url": "https://www.reef.org/"},
    {"name": "FishBase",    "url": "https://www.fishbase.org/"},
    {"name": "SeaLifeBase", "url": "https://www.sealifebase.org/"},
]

BINOMIAL_RE = re.compile(r"^[A-Z][A-Za-z-]+ [a-z][A-Za-z-]+$")


# =============================================================================
# SCHRITT 1 — CSV parsen
# =============================================================================

def parse_reef_csv(csv_file):
    with open(csv_file, newline="", encoding="utf-8-sig") as f:
        lines = f.readlines()

    header_idx = next(
        (i for i, line in enumerate(lines) if line.startswith("Rank,")), None
    )
    if header_idx is None:
        print("[ERROR] Header-Zeile mit 'Rank,...' nicht gefunden", file=sys.stderr)
        sys.exit(1)

    reader = csv.DictReader(lines[header_idx:])
    if "Species" not in reader.fieldnames or "SF%" not in reader.fieldnames:
        print("[ERROR] Spalten 'Species' oder 'SF%' nicht gefunden", file=sys.stderr)
        sys.exit(1)

    rows = {}
    for row in reader:
        species_raw = row["Species"].strip()
        sf_raw = row["SF%"].strip()
        if not species_raw or not sf_raw:
            continue
        scientific_name = re.sub(r"\s+", " ", species_raw.split(",")[0].strip())
        if not scientific_name or not BINOMIAL_RE.match(scientific_name):
            continue
        sf_clean = sf_raw.replace("%", "").replace(",", ".").strip()
        try:
            sf = float(sf_clean)
        except ValueError:
            continue
        normalized = scientific_name.strip().lower()
        if normalized not in rows or sf > rows[normalized]["sf"]:
            rows[normalized] = {"original_name": scientific_name, "normalized_name": normalized, "sf": sf}

    return sorted(rows.values(), key=lambda r: r["original_name"])


# =============================================================================
# SCHRITT 2 — DuckDB-Lookup
# =============================================================================

SQL_TEMPLATE = """
COPY (
    WITH
    input_names AS (
        SELECT original_name, normalized_name, CAST(sf AS DOUBLE) AS sf
        FROM read_csv('{candidates}', HEADER = true, ALL_VARCHAR = true)
    ),
    name_rows AS (
        SELECT 'fishbase' AS source, CAST(s.SpecCode AS VARCHAR) AS source_species_id,
            LOWER(TRIM(g.GenName) || ' ' || TRIM(s.Species)) AS normalized_name,
            TRIM(g.GenName) || ' ' || TRIM(s.Species) AS matched_name,
            TRIM(g.GenName) || ' ' || TRIM(s.Species) AS canonical_name,
            'valid' AS name_status, CAST(NULL AS VARCHAR) AS synonymy,
            CAST(NULL AS VARCHAR) AS combination, 0 AS misspelling, 1 AS is_preferred
        FROM read_parquet('{fb}/species.parquet') s
        JOIN read_parquet('{fb}/genera.parquet') g ON g.GenCode = s.GenCode
        UNION ALL
        SELECT 'fishbase' AS source, CAST(s.SpecCode AS VARCHAR) AS source_species_id,
            LOWER(TRIM(syn.SynGenus) || ' ' || TRIM(syn.SynSpecies)) AS normalized_name,
            TRIM(syn.SynGenus) || ' ' || TRIM(syn.SynSpecies) AS matched_name,
            TRIM(g.GenName) || ' ' || TRIM(s.Species) AS canonical_name,
            LOWER(TRIM(syn.Status)) AS name_status, NULLIF(TRIM(syn.Synonymy), '') AS synonymy,
            NULLIF(TRIM(syn.Combination), '') AS combination,
            CAST(COALESCE(syn.Misspelling, 0) AS INTEGER) AS misspelling, 0 AS is_preferred
        FROM read_parquet('{fb}/synonyms.parquet') syn
        JOIN read_parquet('{fb}/species.parquet') s ON s.SpecCode = syn.SpecCode
        JOIN read_parquet('{fb}/genera.parquet') g ON g.GenCode = s.GenCode
        WHERE syn.TaxonLevel = 'Species' AND syn.SpecCode IS NOT NULL
          AND NULLIF(TRIM(syn.SynGenus), '') IS NOT NULL
          AND NULLIF(TRIM(syn.SynSpecies), '') IS NOT NULL
          AND LOWER(COALESCE(TRIM(syn.Status), '')) NOT IN ('accepted name', 'provisionally accepted name')
        UNION ALL
        SELECT 'sealifebase' AS source, CAST(s.SpecCode AS VARCHAR) AS source_species_id,
            LOWER(TRIM(g.GenName) || ' ' || TRIM(s.Species)) AS normalized_name,
            TRIM(g.GenName) || ' ' || TRIM(s.Species) AS matched_name,
            TRIM(g.GenName) || ' ' || TRIM(s.Species) AS canonical_name,
            'valid' AS name_status, CAST(NULL AS VARCHAR) AS synonymy,
            CAST(NULL AS VARCHAR) AS combination, 0 AS misspelling, 1 AS is_preferred
        FROM read_parquet('{slb}/species.parquet') s
        JOIN read_parquet('{slb}/genera.parquet') g ON g.GenCode = s.GenCode
        UNION ALL
        SELECT 'sealifebase' AS source, CAST(s.SpecCode AS VARCHAR) AS source_species_id,
            LOWER(TRIM(syn.SynGenus) || ' ' || TRIM(syn.SynSpecies)) AS normalized_name,
            TRIM(syn.SynGenus) || ' ' || TRIM(syn.SynSpecies) AS matched_name,
            TRIM(g.GenName) || ' ' || TRIM(s.Species) AS canonical_name,
            LOWER(TRIM(syn.Status)) AS name_status, NULLIF(TRIM(syn.Synonymy), '') AS synonymy,
            NULLIF(TRIM(syn.Combination), '') AS combination,
            CAST(COALESCE(syn.Misspelling, 0) AS INTEGER) AS misspelling, 0 AS is_preferred
        FROM read_parquet('{slb}/synonyms.parquet') syn
        JOIN read_parquet('{slb}/species.parquet') s ON s.SpecCode = syn.SpecCode
        JOIN read_parquet('{slb}/genera.parquet') g ON g.GenCode = s.GenCode
        WHERE syn.TaxonLevel = 'Species' AND syn.SpecCode IS NOT NULL
          AND NULLIF(TRIM(syn.SynGenus), '') IS NOT NULL
          AND NULLIF(TRIM(syn.SynSpecies), '') IS NOT NULL
          AND LOWER(COALESCE(TRIM(syn.Status), '')) NOT IN ('accepted name', 'provisionally accepted name')
    ),
    ranked AS (
        SELECT i.original_name, i.normalized_name AS requested_normalized_name, i.sf,
            n.source, n.source_species_id, n.matched_name, n.canonical_name,
            n.name_status, n.synonymy, n.combination, n.misspelling, n.is_preferred,
            ROW_NUMBER() OVER (
                PARTITION BY i.normalized_name
                ORDER BY n.is_preferred DESC,
                    CASE n.source WHEN 'fishbase' THEN 0 WHEN 'sealifebase' THEN 1 ELSE 2 END,
                    n.source_species_id
            ) AS rn
        FROM input_names i
        LEFT JOIN name_rows n ON n.normalized_name = i.normalized_name
    )
    SELECT original_name,
        COALESCE(canonical_name, '') AS resolved_name,
        COALESCE(matched_name, '') AS matched_name,
        COALESCE(source, '') AS source,
        COALESCE(source_species_id, '') AS source_species_id,
        COALESCE(name_status, '') AS name_status,
        CASE WHEN source IS NULL THEN 'none'
             WHEN is_preferred = 1 THEN 'canonical'
             WHEN misspelling = 1 THEN 'misspelling'
             ELSE 'synonym' END AS match_type,
        COALESCE(synonymy, '') AS synonymy,
        COALESCE(combination, '') AS combination,
        sf,
        CASE WHEN source IS NULL THEN 'invalid' ELSE 'resolved' END AS status
    FROM ranked
    WHERE rn = 1 OR rn IS NULL
    ORDER BY CASE WHEN source IS NULL THEN 1 ELSE 0 END, original_name
) TO '{resolution}' (FORMAT csv, HEADER true);
"""

def run_lookup(candidates_csv, resolution_csv, fb_base, slb_base, work_dir):
    sql = SQL_TEMPLATE.format(
        candidates=candidates_csv.replace("'", "''"),
        fb=fb_base.replace("'", "''"),
        slb=slb_base.replace("'", "''"),
        resolution=resolution_csv.replace("'", "''"),
    )
    con = duckdb.connect(os.path.join(work_dir, "lookup.duckdb"))
    con.execute(sql)
    con.close()


# =============================================================================
# SCHRITT 3 — Level-Berechnung
# =============================================================================

def compute_levels(resolution_csv):
    resolved, invalid = [], []
    with open(resolution_csv, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            (resolved if row["status"] == "resolved" else invalid).append(row)

    by_name = {}
    for row in resolved:
        name = row["resolved_name"]
        if name not in by_name or float(row["sf"]) > float(by_name[name]["sf"]):
            by_name[name] = row

    rows = sorted(by_name.values(), key=lambda r: (-float(r["sf"]), r["resolved_name"]))
    n = len(rows)
    if n == 0:
        print("[ERROR] Keine validen Arten gefunden", file=sys.stderr)
        sys.exit(1)

    if n >= 40:
        l1 = max(math.ceil(n * 0.2), 15)
        l2 = min(max(math.ceil(n * 0.3), 15), n - l1)
    else:
        l1 = min(10, n)
        l2 = min(10, n - l1)

    return rows[:l1], rows[l1:l1+l2], rows[l1+l2:], resolved, invalid


# =============================================================================
# SCHRITT 4 — Prompt B generieren & anzeigen
# =============================================================================

PROMPT_B_TEMPLATE = """\
Du bist ein erfahrener Meeresbiologieexperte und Tauchführer-Autor mit umfassendem
Wissen über marine Artengemeinschaften weltweit.

Dir werden drei Deck-JSONs für die Region {region} übergeben. Diese Decks basieren
auf REEF-Sichtungsdaten. Das Level-System der Decks spiegelt Sichtungshäufigkeit wider:
  - L1 = sehr häufig gesichtet
  - L2 = häufig gesichtet
  - L3 = selten gesichtet

Deine Aufgabe ist es, diese Decks aus der Perspektive eines Tauchführer-Autors zu
ergänzen und zu korrigieren – nicht aus Häufigkeitsperspektive.

---

TEIL 1 – FEHLENDE IKONISCHE ARTEN ERGÄNZEN

Prüfe ob ikonische Arten fehlen. Eine Art gilt als ikonisch wenn mindestens zwei
der folgenden Kriterien zutreffen:
  a) Hoher Wiedererkennungswert (unverwechselbare Form, Farbe, Verhalten)
  b) Präsenz in mindestens einem Standardtauchführer für die Region
  c) Touristische oder taucherische Bedeutung (Bucket-List, Zielart für Reisen)
  d) Einziger oder seltener Vertreter einer Familie/Gattung in der Region
  e) Ökologische Schlüsselrolle (Apex-Predator, Strukturbildner, etc.)

Berücksichtige neben Tieren auch markante Makroalgen, Seegräser und sessile
Wirbellose (z.B. Schwämme, Korallen, Seegras) wenn sie einen hohen
Wiedererkennungswert haben und in Tauchführern der Region präsent sind.

Für Additions gilt ein eigenes Level-System basierend auf Bekanntheit und
Lernrelevanz für Taucher – unabhängig von Sichtungshäufigkeit:
  - L1 = Muss jeder Taucher dieser Region kennen (absolutes Basiswissen)
  - L2 = Wichtig für interessierte / fortgeschrittene Taucher
  - L3 = Für Spezialisten oder besondere Begegnungen relevant

Schlage maximal 10 fehlende Arten vor, priorisiert nach Relevanz.
Verwende ausschliesslich Binomialnamen die in FishBase oder SeaLifeBase gültig sind.

---

TEIL 2 – LEVEL-KORREKTUREN BESTEHENDER ARTEN

Prüfe ob bestehende Arten falsch eingestuft sind. Dabei gilt:
  - Ist eine Art im Deck bereits vorhanden (egal auf welchem Level) → nur
    Level-Korrektur vorschlagen, keine Addition
  - Ist eine Art nicht im Deck → Addition vorschlagen (TEIL 1), keine
    Level-Korrektur

Bewertungsgrundlage für Korrekturen: Würde ein Tauchführer-Autor diese Art auf
einem anderen Level einordnen als die REEF-Häufigkeit suggeriert?

Wichtig: Für Level-Korrekturen gilt weiterhin die ursprüngliche Deck-Logik
(L1 = sehr häufig, L2 = häufig, L3 = selten) als Referenzrahmen – nicht die
Lernrelevanz-Logik aus Teil 1.

Upgrade-Regel: Upgrades über mehrere Stufen (z.B. L3→L1) sind erlaubt wenn
die taucherische Relevanz die Sichtungshäufigkeit klar übersteuert.
Downgrade-Regel: Downgrades erfolgen maximal um eine Stufe (L1→L2 oder
L2→L3). Ein direkter Sprung von L1→L3 ist nicht zulässig.

Schlage maximal 10 Level-Korrekturen vor, priorisiert nach Dringlichkeit.

---

AUSGABEFORMAT – antworte ausschliesslich als valides JSON:

{{
  "additions": [
    {{
      "speciesName": "...",
      "level": "L1|L2|L3",
      "criteria": ["a", "b", ...],
      "reason": "..."
    }}
  ],
  "level_corrections": [
    {{
      "speciesName": "...",
      "current_level": "L1|L2|L3",
      "suggested_level": "L1|L2|L3",
      "reason": "..."
    }}
  ]
}}

---

Region: {region}

Deck L1:
{l1}

Deck L2:
{l2}

Deck L3:
{l3}
"""

def build_deck_dict(pretty_name, level_label, description, rows):
    return {
        "name": f"{pretty_name} - {level_label}",
        "description": description,
        "speciesNames": [r["resolved_name"] for r in rows],
        "imageUrl": "",
        "sources": SOURCES,
    }

def generate_prompt_b(region, decks):
    return PROMPT_B_TEMPLATE.format(
        region=region,
        l1=json.dumps(decks["level1"], indent=2, ensure_ascii=False),
        l2=json.dumps(decks["level2"], indent=2, ensure_ascii=False),
        l3=json.dumps(decks["level3"], indent=2, ensure_ascii=False),
    )


# =============================================================================
# SCHRITT 5 — Korrekturen einlesen & anwenden
# =============================================================================

def normalize(name):
    return name.strip().lower()

def find_level(decks, species):
    for level, deck in decks.items():
        if any(normalize(s) == normalize(species) for s in deck["speciesNames"]):
            return level
    return None

def level_key(level_str):
    mapping = {"L1": "level1", "L2": "level2", "L3": "level3"}
    key = mapping.get((level_str or "").upper())
    if not key:
        print(f"[ERROR] Ungültiger Level-Wert: {level_str}", file=sys.stderr)
        sys.exit(1)
    return key

def apply_corrections(decks, corrections, source_name):
    decks = deepcopy(decks)
    log = []

    def log_line(line=""):
        print(line)
        log.append(line)

    log_line("=" * 60)
    log_line(f"Korrekturen-Log")
    log_line(f"Zeitstempel: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_line("=" * 60)
    log_line()

    level_corrections = corrections.get("level_corrections", [])
    log_line(f"LEVEL-KORREKTUREN ({len(level_corrections)})")
    log_line("-" * 40)

    for c in level_corrections:
        species  = c.get("speciesName", "").strip()
        current  = c.get("current_level")
        suggested = c.get("suggested_level")
        reason   = c.get("reason", "")

        if not current or not suggested or current == "null" or suggested == "null":
            log_line(f"[SKIP] {species} – current_level oder suggested_level ist null")
            continue
        if current.upper() == suggested.upper():
            log_line(f"[SKIP] {species} – Level identisch ({current})")
            continue

        actual = find_level(decks, species)
        if not actual:
            log_line(f"[SKIP] {species} – nicht im Deck gefunden")
            continue

        suggested_key = level_key(suggested)
        if actual != level_key(current):
            log_line(f"[WARN] {species} – erwartet auf {current}, gefunden auf {actual.replace('level','L')} – trotzdem verschoben")

        decks[actual]["speciesNames"] = [
            s for s in decks[actual]["speciesNames"] if normalize(s) != normalize(species)
        ]
        decks[suggested_key]["speciesNames"].append(species)
        log_line(f"[OK]   {species}: {actual.replace('level','L')} → {suggested}")
        log_line(f"       Grund: {reason}")
        log_line()

    additions = corrections.get("additions", [])
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
            log_line(f"[SKIP] {species} – bereits auf {existing.replace('level','L')} vorhanden")
            continue

        decks[level_key(level)]["speciesNames"].append(species)
        log_line(f"[OK]   {species} → {level} hinzugefügt")
        log_line(f"       Kriterien: {criteria}")
        log_line(f"       Grund: {reason}")
        log_line()

    log_line()
    log_line("=" * 60)
    log_line("ZUSAMMENFASSUNG")
    log_line("-" * 40)
    for level, deck in decks.items():
        log_line(f"{level.replace('level','Level ')}: {len(deck['speciesNames'])} Arten")
    log_line("=" * 60)

    # Source-Eintrag ergänzen
    if source_name:
        if isinstance(source_name, dict):
            source_entry = source_name
        else:
            source_urls = {
                "ChatGPT": "https://openai.com/chatgpt",
                "Claude":  "https://claude.ai",
                "Gemini":  "https://gemini.google.com",
            }
            source_entry = {"name": source_name, "url": source_urls.get(source_name, "")}
        for deck in decks.values():
            if source_entry["name"] not in [s.get("name") for s in deck.get("sources", [])]:
                deck.setdefault("sources", []).append(source_entry)

    return decks, log


# =============================================================================
# SCHRITT 6 — Dateien schreiben
# =============================================================================

def write_outputs(decks, base_name, out_dir, log, invalid_rows, metadata):
    os.makedirs(out_dir, exist_ok=True)

    for level, deck in decks.items():
        # Metadaten überschreiben
        level_label = level.replace("level", "Level ")
        deck["name"]        = f"{metadata['name']} - {level_label}"
        deck["description"] = metadata["description"]
        deck["imageUrl"]    = metadata["image_url"]
        deck["createdBy"]   = metadata["created_by"]

        path = os.path.join(out_dir, f"{base_name}_{level}.json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(deck, f, indent=2, ensure_ascii=False)
        print(f"  geschrieben: {path}")

    log_path = os.path.join(out_dir, f"{base_name}_corrections_log.txt")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write("\n".join(log))
    print(f"  geschrieben: {log_path}")


# =============================================================================
# SOURCE-AUSWAHL — Arrow-Key Selector
# =============================================================================

def arrow_select(prompt, options):
    """Interaktive Auswahl mit Pfeiltasten. Gibt gewählte Option zurück."""
    import tty
    import termios

    idx = 0

    def render(current):
        # Cursor nach oben bewegen um neu zu zeichnen
        sys.stdout.write(f"\033[{len(options)}A")
        for i, opt in enumerate(options):
            prefix = "  \033[1;36m›\033[0m " if i == current else "    "
            sys.stdout.write(f"\r{prefix}{opt}\033[K\n")
        sys.stdout.flush()

    print(f"\n{prompt}")
    for opt in options:
        print(f"    {opt}")

    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        render(idx)
        while True:
            ch = sys.stdin.read(1)
            if ch == "\r" or ch == "\n":
                break
            elif ch == "\x1b":
                ch2 = sys.stdin.read(1)
                ch3 = sys.stdin.read(1)
                if ch2 == "[":
                    if ch3 == "A":  # Hoch
                        idx = (idx - 1) % len(options)
                    elif ch3 == "B":  # Runter
                        idx = (idx + 1) % len(options)
                render(idx)
            elif ch == "\x03":  # Ctrl+C
                raise KeyboardInterrupt
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

    sys.stdout.write(f"\r\033[K")
    return options[idx]


def ask_source():
    """Fragt ob Source-Enrichment gewünscht, dann welches System."""
    answer = input("\nSource-Eintrag in JSONs schreiben? (j/N): ").strip().lower()
    if answer not in ("j", "ja", "y", "yes"):
        print("  → Übersprungen.")
        return None

    known = [
        ("ChatGPT", "https://openai.com/chatgpt"),
        ("Claude",  "https://claude.ai"),
        ("Gemini",  "https://gemini.google.com"),
        ("Anderes System...", ""),
    ]
    options = [name for name, _ in known]
    chosen = arrow_select("Verwendetes System (↑↓ wählen, Enter bestätigen):", options)

    if chosen == "Anderes System...":
        name = input("  Name: ").strip()
        url  = input("  URL (optional): ").strip()
        print(f"  → {name}")
        return {"name": name, "url": url} if name else None
    else:
        url = dict(known)[chosen]
        print(f"  → {chosen}")
        return {"name": chosen, "url": url}


# =============================================================================
# MAIN
# =============================================================================

def write_invalid_csv(invalid_rows, base_name, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    if not invalid_rows:
        return
    path = os.path.join(out_dir, f"{base_name}_invalid_species.csv")
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["original_name", "sf"])
        writer.writeheader()
        for row in invalid_rows:
            writer.writerow({"original_name": row["original_name"], "sf": row["sf"]})
    print(f"  geschrieben: {path}")


def ask_metadata(region_name):
    """Fragt die Deck-Attribute interaktiv ab."""
    print(f"\n{'─'*60}")
    print("  Deck-Attribute")
    print(f"{'─'*60}")
    name        = input(f"  Name [{region_name}]: ").strip() or region_name
    description = input(f"  Beschreibung []: ").strip()
    image_url   = input(f"  imageUrl []: ").strip()
    created_by  = input(f"  createdBy []: ").strip()
    return {
        "name":        name,
        "description": description,
        "image_url":   image_url,
        "created_by":  created_by,
    }


# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description="REEF CSV -> Discere deck JSONs (Wizard)")
    parser.add_argument("csv_file")
    parser.add_argument("--base-name", default=None)
    parser.add_argument("--version", default="v25.04")
    parser.add_argument("--fishbase-dir", default=None)
    parser.add_argument("--slb-dir", default=None)
    args = parser.parse_args()

    if not os.path.exists(args.csv_file):
        print(f"[ERROR] CSV nicht gefunden: {args.csv_file}", file=sys.stderr)
        sys.exit(1)

    base_name = args.base_name or os.path.splitext(os.path.basename(args.csv_file))[0]
    out_dir   = "generated"

    fb_base  = args.fishbase_dir or f"https://huggingface.co/datasets/cboettig/fishbase/resolve/main/data/fb/{args.version}/parquet"
    slb_base = args.slb_dir      or f"https://huggingface.co/datasets/cboettig/fishbase/resolve/main/data/slb/{args.version}/parquet"

    print(f"\n{'='*60}")
    print(f"  Discere REEF Wizard")
    print(f"{'='*60}\n")

    region_name = input("Regionsname (z.B. 'Mittelmeer'): ").strip()
    if not region_name:
        region_name = " ".join(w.capitalize() for w in base_name.split("_"))
        print(f"  → Kein Name eingegeben, verwende: {region_name}")

    # --- [1] CSV einlesen & Lookup ---
    print(f"\n[1/3] CSV einlesen & gegen FishBase/SeaLifeBase auflösen...")

    with tempfile.TemporaryDirectory() as work_dir:
        candidates_csv = os.path.join(work_dir, "candidates.csv")
        resolution_csv = os.path.join(work_dir, "resolution.csv")

        candidates = parse_reef_csv(args.csv_file)
        print(f"      {len(candidates)} Kandidaten gefunden")

        with open(candidates_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["original_name", "normalized_name", "sf"])
            writer.writeheader()
            writer.writerows(candidates)

        print("      Parquet-Lookup läuft (kann einen Moment dauern)...")
        run_lookup(candidates_csv, resolution_csv, fb_base, slb_base, work_dir)

        level1_rows, level2_rows, level3_rows, resolved, invalid = compute_levels(resolution_csv)
        n = len(level1_rows) + len(level2_rows) + len(level3_rows)
        synonym_count = sum(1 for r in resolved if r["match_type"] != "canonical")

        print(f"\n      {n} Arten aufgelöst | {len(invalid)} ungültig | {synonym_count} Synonym-Korrekturen")

        # Ungültige Arten sofort schreiben
        if invalid:
            print(f"\n      Ungültige Arten (nicht in FishBase/SeaLifeBase):")
            for row in invalid:
                print(f"        - {row['original_name']}")
            print(f"\n      Schreibe invalid_species.csv...")
            write_invalid_csv(invalid, base_name, out_dir)

        # --- [2] AI-Anreicherung ---
        pretty = " ".join(w.capitalize() for w in base_name.split("_"))
        decks = {
            "level1": build_deck_dict(pretty, "Level 1", "Sehr häufige Arten", level1_rows),
            "level2": build_deck_dict(pretty, "Level 2", "Häufige Arten",      level2_rows),
            "level3": build_deck_dict(pretty, "Level 3", "Seltene Arten",      level3_rows),
        }

        log = []
        print(f"\n[2/3] KI-Anreicherung")
        enrich = input("      Ikonische Arten via KI ergänzen? (j/N): ").strip().lower()

        if enrich in ("j", "ja", "y", "yes"):
            prompt_b = generate_prompt_b(region_name, decks)
            print(f"\n      Prompt:\n")
            print("=" * 60)
            print(prompt_b)
            print("=" * 60)

            print(f"\n      LLM-Output hier einfügen, dann Enter + Ctrl+D:")
            raw = sys.stdin.read().strip()

            if not raw:
                print("      [WARN] Kein Input – keine Korrekturen angewendet.")
            else:
                try:
                    corrections = json.loads(raw)
                except json.JSONDecodeError as e:
                    print(f"[ERROR] Ungültiges JSON: {e}", file=sys.stderr)
                    sys.exit(1)

                source_name = ask_source()
                print()
                decks, log = apply_corrections(decks, corrections, source_name)
        else:
            print("      → Übersprungen.")

        # --- [3] Deck-Attribute & Schreiben ---
        print(f"\n[3/3] Deck-Attribute & Ausgabe")
        metadata = ask_metadata(region_name)

        print(f"\n  Schreibe Dateien nach '{out_dir}'...")
        write_outputs(decks, base_name, out_dir, log, invalid, metadata)
        print("\nFertig.")

if __name__ == "__main__":
    main()