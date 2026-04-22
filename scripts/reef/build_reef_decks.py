#!/usr/bin/env python3
# =============================================================================
# build_reef_decks.py — Standalone REEF CSV -> Discere deck JSONs
#
# Erstellt Level-Decks aus einem REEF-CSV und löst wissenschaftliche Namen
# direkt gegen FishBase-/SeaLifeBase-Parquets auf. Das Script ist unabhängig
# vom Discere-ETL-Build und nutzt weder discere_reference.db noch ETL-Tabellen.
#
# Standardmäßig werden die Parquets remote von Hugging Face per DuckDB gelesen.
# Optional können lokale Parquet-Verzeichnisse übergeben werden.
#
# Abhängigkeiten:
#   pip install duckdb
#
# Usage:
#   python build_reef_decks.py reef.csv
#   python build_reef_decks.py reef.csv --out-dir generated
#   python build_reef_decks.py reef.csv --region-name "Mittelmeer"
#   python build_reef_decks.py reef.csv --version v25.04
#   python build_reef_decks.py reef.csv --fishbase-dir ./fb/parquet --slb-dir ./slb/parquet
#
# Outputs:
#   <base>_level1.json
#   <base>_level2.json
#   <base>_level3.json
#   <base>_invalid_species.csv
#   <base>_species_resolution.csv
#   <base>_prompt_b.txt
# =============================================================================

import argparse
import csv
import json
import math
import os
import re
import sys
import tempfile

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
# CSV-Parsing
# =============================================================================

def parse_reef_csv(csv_file):
    """Liest REEF-CSV und gibt deduplizierte Kandidatenliste zurück."""
    with open(csv_file, newline="", encoding="utf-8-sig") as f:
        lines = f.readlines()

    header_idx = next(
        (i for i, line in enumerate(lines) if line.startswith("Rank,")),
        None
    )
    if header_idx is None:
        print("[ERROR] Header-Zeile mit 'Rank,...' nicht gefunden", file=sys.stderr)
        sys.exit(1)

    reader = csv.DictReader(lines[header_idx:])
    if "Species" not in reader.fieldnames:
        print("[ERROR] Spalte 'Species' nicht gefunden", file=sys.stderr)
        sys.exit(1)
    if "SF%" not in reader.fieldnames:
        print("[ERROR] Spalte 'SF%' nicht gefunden", file=sys.stderr)
        sys.exit(1)

    rows = {}
    for row in reader:
        species_raw = row["Species"].strip()
        sf_raw = row["SF%"].strip()
        if not species_raw or not sf_raw:
            continue

        scientific_name = species_raw.split(",")[0].strip()
        scientific_name = re.sub(r"\s+", " ", scientific_name)
        if not scientific_name or not BINOMIAL_RE.match(scientific_name):
            continue

        sf_clean = sf_raw.replace("%", "").replace(",", ".").strip()
        try:
            sf = float(sf_clean)
        except ValueError:
            continue

        normalized = scientific_name.strip().lower()
        if normalized not in rows or sf > rows[normalized]["sf"]:
            rows[normalized] = {
                "original_name": scientific_name,
                "normalized_name": normalized,
                "sf": sf,
            }

    candidates = sorted(rows.values(), key=lambda r: r["original_name"])
    print(f"Kandidaten vor Parquet-Lookup: {len(candidates)}")
    return candidates


# =============================================================================
# DuckDB-Lookup
# =============================================================================

SQL_TEMPLATE = """
COPY (
    WITH
    input_names AS (
        SELECT original_name, normalized_name, CAST(sf AS DOUBLE) AS sf
        FROM read_csv('{candidates}', HEADER = true, ALL_VARCHAR = true)
    ),
    name_rows AS (
        SELECT
            'fishbase' AS source,
            CAST(s.SpecCode AS VARCHAR) AS source_species_id,
            LOWER(TRIM(g.GenName) || ' ' || TRIM(s.Species)) AS normalized_name,
            TRIM(g.GenName) || ' ' || TRIM(s.Species) AS matched_name,
            TRIM(g.GenName) || ' ' || TRIM(s.Species) AS canonical_name,
            'valid' AS name_status,
            CAST(NULL AS VARCHAR) AS synonymy,
            CAST(NULL AS VARCHAR) AS combination,
            0 AS misspelling,
            1 AS is_preferred
        FROM read_parquet('{fb}/species.parquet') s
        JOIN read_parquet('{fb}/genera.parquet') g ON g.GenCode = s.GenCode

        UNION ALL

        SELECT
            'fishbase' AS source,
            CAST(s.SpecCode AS VARCHAR) AS source_species_id,
            LOWER(TRIM(syn.SynGenus) || ' ' || TRIM(syn.SynSpecies)) AS normalized_name,
            TRIM(syn.SynGenus) || ' ' || TRIM(syn.SynSpecies) AS matched_name,
            TRIM(g.GenName) || ' ' || TRIM(s.Species) AS canonical_name,
            LOWER(TRIM(syn.Status)) AS name_status,
            NULLIF(TRIM(syn.Synonymy), '') AS synonymy,
            NULLIF(TRIM(syn.Combination), '') AS combination,
            CAST(COALESCE(syn.Misspelling, 0) AS INTEGER) AS misspelling,
            0 AS is_preferred
        FROM read_parquet('{fb}/synonyms.parquet') syn
        JOIN read_parquet('{fb}/species.parquet') s ON s.SpecCode = syn.SpecCode
        JOIN read_parquet('{fb}/genera.parquet') g ON g.GenCode = s.GenCode
        WHERE syn.TaxonLevel = 'Species'
          AND syn.SpecCode IS NOT NULL
          AND NULLIF(TRIM(syn.SynGenus), '') IS NOT NULL
          AND NULLIF(TRIM(syn.SynSpecies), '') IS NOT NULL
          AND LOWER(COALESCE(TRIM(syn.Status), '')) NOT IN (
              'accepted name', 'provisionally accepted name'
          )

        UNION ALL

        SELECT
            'sealifebase' AS source,
            CAST(s.SpecCode AS VARCHAR) AS source_species_id,
            LOWER(TRIM(g.GenName) || ' ' || TRIM(s.Species)) AS normalized_name,
            TRIM(g.GenName) || ' ' || TRIM(s.Species) AS matched_name,
            TRIM(g.GenName) || ' ' || TRIM(s.Species) AS canonical_name,
            'valid' AS name_status,
            CAST(NULL AS VARCHAR) AS synonymy,
            CAST(NULL AS VARCHAR) AS combination,
            0 AS misspelling,
            1 AS is_preferred
        FROM read_parquet('{slb}/species.parquet') s
        JOIN read_parquet('{slb}/genera.parquet') g ON g.GenCode = s.GenCode

        UNION ALL

        SELECT
            'sealifebase' AS source,
            CAST(s.SpecCode AS VARCHAR) AS source_species_id,
            LOWER(TRIM(syn.SynGenus) || ' ' || TRIM(syn.SynSpecies)) AS normalized_name,
            TRIM(syn.SynGenus) || ' ' || TRIM(syn.SynSpecies) AS matched_name,
            TRIM(g.GenName) || ' ' || TRIM(s.Species) AS canonical_name,
            LOWER(TRIM(syn.Status)) AS name_status,
            NULLIF(TRIM(syn.Synonymy), '') AS synonymy,
            NULLIF(TRIM(syn.Combination), '') AS combination,
            CAST(COALESCE(syn.Misspelling, 0) AS INTEGER) AS misspelling,
            0 AS is_preferred
        FROM read_parquet('{slb}/synonyms.parquet') syn
        JOIN read_parquet('{slb}/species.parquet') s ON s.SpecCode = syn.SpecCode
        JOIN read_parquet('{slb}/genera.parquet') g ON g.GenCode = s.GenCode
        WHERE syn.TaxonLevel = 'Species'
          AND syn.SpecCode IS NOT NULL
          AND NULLIF(TRIM(syn.SynGenus), '') IS NOT NULL
          AND NULLIF(TRIM(syn.SynSpecies), '') IS NOT NULL
          AND LOWER(COALESCE(TRIM(syn.Status), '')) NOT IN (
              'accepted name', 'provisionally accepted name'
          )
    ),
    ranked AS (
        SELECT
            i.original_name,
            i.normalized_name AS requested_normalized_name,
            i.sf,
            n.source,
            n.source_species_id,
            n.matched_name,
            n.canonical_name,
            n.name_status,
            n.synonymy,
            n.combination,
            n.misspelling,
            n.is_preferred,
            ROW_NUMBER() OVER (
                PARTITION BY i.normalized_name
                ORDER BY
                    n.is_preferred DESC,
                    CASE n.source
                        WHEN 'fishbase' THEN 0
                        WHEN 'sealifebase' THEN 1
                        ELSE 2
                    END,
                    n.source_species_id
            ) AS rn
        FROM input_names i
        LEFT JOIN name_rows n ON n.normalized_name = i.normalized_name
    )
    SELECT
        original_name,
        COALESCE(canonical_name, '') AS resolved_name,
        COALESCE(matched_name, '') AS matched_name,
        COALESCE(source, '') AS source,
        COALESCE(source_species_id, '') AS source_species_id,
        COALESCE(name_status, '') AS name_status,
        CASE
            WHEN source IS NULL THEN 'none'
            WHEN is_preferred = 1 THEN 'canonical'
            WHEN misspelling = 1 THEN 'misspelling'
            ELSE 'synonym'
        END AS match_type,
        COALESCE(synonymy, '') AS synonymy,
        COALESCE(combination, '') AS combination,
        sf,
        CASE WHEN source IS NULL THEN 'invalid' ELSE 'resolved' END AS status
    FROM ranked
    WHERE rn = 1 OR rn IS NULL
    ORDER BY
        CASE WHEN source IS NULL THEN 1 ELSE 0 END,
        original_name
) TO '{resolution}' (FORMAT csv, HEADER true);
"""

def run_lookup(candidates_csv, resolution_csv, fb_base, slb_base, work_dir):
    sql = SQL_TEMPLATE.format(
        candidates=candidates_csv.replace("'", "''"),
        fb=fb_base.replace("'", "''"),
        slb=slb_base.replace("'", "''"),
        resolution=resolution_csv.replace("'", "''"),
    )
    db_path = os.path.join(work_dir, "lookup.duckdb")
    con = duckdb.connect(db_path)
    con.execute(sql)
    con.close()


# =============================================================================
# Level-Berechnung & JSON-Ausgabe
# =============================================================================

def compute_levels(resolution_csv):
    resolved = []
    invalid = []

    with open(resolution_csv, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["status"] == "resolved":
                resolved.append(row)
            else:
                invalid.append(row)

    # Deduplizieren nach resolved_name, höchste SF behalten
    by_name = {}
    for row in resolved:
        name = row["resolved_name"]
        if name not in by_name or float(row["sf"]) > float(by_name[name]["sf"]):
            by_name[name] = row

    rows = sorted(by_name.values(), key=lambda r: (-float(r["sf"]), r["resolved_name"]))
    n = len(rows)

    if n == 0:
        print("[ERROR] Keine gegen FishBase/SeaLifeBase-Parquets validen Arten gefunden", file=sys.stderr)
        sys.exit(1)

    if n >= 40:
        l1_size = max(math.ceil(n * 0.2), 15)
        l2_size = max(math.ceil(n * 0.3), 15)
        l1_size = min(l1_size, n)
        l2_size = min(l2_size, n - l1_size)
    else:
        l1_size = min(10, n)
        l2_size = min(10, n - l1_size)

    level1 = rows[:l1_size]
    level2 = rows[l1_size:l1_size + l2_size]
    level3 = rows[l1_size + l2_size:]

    return level1, level2, level3, resolved, invalid


def write_deck_json(path, name, description, rows):
    payload = {
        "name": name,
        "description": description,
        "speciesNames": [r["resolved_name"] for r in rows],
        "imageUrl": "",
        "sources": SOURCES,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"geschrieben: {path}")


# =============================================================================
# Prompt-Generierung
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

def write_prompt_b(path, region, l1_path, l2_path, l3_path):
    with open(l1_path) as f: l1 = f.read()
    with open(l2_path) as f: l2 = f.read()
    with open(l3_path) as f: l3 = f.read()

    content = PROMPT_B_TEMPLATE.format(region=region, l1=l1, l2=l2, l3=l3)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Prompt B geschrieben: {path}")


# =============================================================================
# Main
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="REEF CSV -> Discere deck JSONs"
    )
    parser.add_argument("csv_file", help="REEF CSV-Datei")
    parser.add_argument("--out-dir", default=".", help="Ausgabeverzeichnis (default: .)")
    parser.add_argument("--base-name", default=None, help="Basis-Dateiname (default: CSV-Dateiname)")
    parser.add_argument("--region-name", default=None, help="Lesbarer Regionsname für den Prompt")
    parser.add_argument("--version", default="v25.04", help="FishBase/SLB Version (default: v25.04)")
    parser.add_argument("--fishbase-dir", default=None, help="Lokales FishBase Parquet-Verzeichnis")
    parser.add_argument("--slb-dir", default=None, help="Lokales SeaLifeBase Parquet-Verzeichnis")
    args = parser.parse_args()

    if not os.path.exists(args.csv_file):
        print(f"[ERROR] CSV-Datei nicht gefunden: {args.csv_file}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(args.out_dir, exist_ok=True)

    base_name = args.base_name or os.path.splitext(os.path.basename(args.csv_file))[0]
    region_name = args.region_name or " ".join(w.capitalize() for w in base_name.split("_"))

    if args.fishbase_dir:
        for f in ["species.parquet", "genera.parquet", "synonyms.parquet"]:
            if not os.path.exists(os.path.join(args.fishbase_dir, f)):
                print(f"[ERROR] FishBase {f} fehlt in: {args.fishbase_dir}", file=sys.stderr)
                sys.exit(1)
        fb_base = args.fishbase_dir
    else:
        fb_base = f"https://huggingface.co/datasets/cboettig/fishbase/resolve/main/data/fb/{args.version}/parquet"

    if args.slb_dir:
        for f in ["species.parquet", "genera.parquet", "synonyms.parquet"]:
            if not os.path.exists(os.path.join(args.slb_dir, f)):
                print(f"[ERROR] SeaLifeBase {f} fehlt in: {args.slb_dir}", file=sys.stderr)
                sys.exit(1)
        slb_base = args.slb_dir
    else:
        slb_base = f"https://huggingface.co/datasets/cboettig/fishbase/resolve/main/data/slb/{args.version}/parquet"

    with tempfile.TemporaryDirectory() as work_dir:
        candidates_csv = os.path.join(work_dir, "candidates.csv")
        resolution_csv = os.path.join(work_dir, "species_resolution.csv")

        # 1. CSV parsen
        candidates = parse_reef_csv(args.csv_file)
        with open(candidates_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["original_name", "normalized_name", "sf"])
            writer.writeheader()
            writer.writerows(candidates)

        # 2. DuckDB-Lookup
        run_lookup(candidates_csv, resolution_csv, fb_base, slb_base, work_dir)

        # 3. Level-Berechnung
        level1, level2, level3, resolved, invalid = compute_levels(resolution_csv)

        # 4. Resolution-CSV schreiben
        resolution_out = os.path.join(args.out_dir, f"{base_name}_species_resolution.csv")
        with open(resolution_csv, newline="", encoding="utf-8") as src, \
             open(resolution_out, "w", newline="", encoding="utf-8") as dst:
            dst.write(src.read())

        # 5. Invalid-CSV schreiben
        invalid_out = os.path.join(args.out_dir, f"{base_name}_invalid_species.csv")
        with open(invalid_out, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["original_name", "sf"])
            writer.writeheader()
            for row in invalid:
                writer.writerow({"original_name": row["original_name"], "sf": row["sf"]})

        # 6. Deck-JSONs schreiben
        pretty = " ".join(w.capitalize() for w in base_name.split("_"))
        l1_path = os.path.join(args.out_dir, f"{base_name}_level1.json")
        l2_path = os.path.join(args.out_dir, f"{base_name}_level2.json")
        l3_path = os.path.join(args.out_dir, f"{base_name}_level3.json")

        write_deck_json(l1_path, f"{pretty} - Level 1", "Sehr häufige Arten", level1)
        write_deck_json(l2_path, f"{pretty} - Level 2", "Häufige Arten",      level2)
        write_deck_json(l3_path, f"{pretty} - Level 3", "Seltene Arten",      level3)

        # 7. Prompt B schreiben
        prompt_b_path = os.path.join(args.out_dir, f"{base_name}_prompt_b.txt")
        write_prompt_b(prompt_b_path, region_name, l1_path, l2_path, l3_path)

    # 8. Zusammenfassung
    n = len(level1) + len(level2) + len(level3)
    synonym_count = sum(1 for r in resolved if r["match_type"] != "canonical")
    print()
    print(f"Gesamtarten nach Parquet-Lookup: {n}")
    print(f"Invalid / ungelöst:              {len(invalid)}")
    print(f"Synonym/Misspelling-Korrekturen: {synonym_count}")
    print(f"Resolution-Datei:                {resolution_out}")
    print(f"Invalid-Datei:                   {invalid_out}")
    print(f"Level 1: {len(level1)}")
    print(f"Level 2: {len(level2)}")
    print(f"Level 3: {len(level3)}")


if __name__ == "__main__":
    main()