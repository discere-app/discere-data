#!/usr/bin/env python3
# =============================================================================
# build_deck.py — build a catalog deck from a recipe and observation data
#
# Reads recipes/<base>.json (schema/recipe.schema.json) and writes
# data/decks/<base>.json, a deck of format 2 with one subdeck per level, and
# recipes/<base>.report.md, the evidence behind it. The order of the species
# comes from observation data (iNaturalist, GBIF or a REEF CSV), occurrence
# is confirmed by OBIS, the FishBase/SeaLifeBase distribution and field
# guides, and only the highlights are picked by hand. How: the package
# scripts/deckbuilder/, starting at deckbuilder/build.py.
#
# A plain script rather than `python3 -m`: it runs from anywhere without
# installing anything, and it can switch off bytecode before the package is
# imported — the repository ignores no __pycache__.
#
# Caches live outside the repository, under ~/.cache/discere-deckbuilder/
# (--cache-dir): HTTP answers, the reference DB, the water flags.
#
# Dependencies: pip install "jsonschema[format]" duckdb
# (duckdb only for the first run per FishBase version; see water_flags.py)
#
# Usage:
#   python3 scripts/build_deck.py recipes/<base>.json
#       [--decks-dir DIR] [--cache-dir DIR] [--refresh]
#       [--reference-db FILE] [--fishbase-version VERSION]
#
# Exit code 0 on success, 1 if it stopped without writing, 2 if it wrote the
# deck but a highlight stayed out for lack of evidence (see the report).
# =============================================================================

import argparse
import os
import sys
import time

sys.dont_write_bytecode = True

from deckbuilder import build, inat_names, recipe, refdb, water_flags  # noqa: E402
from deckbuilder.fetch import CachedFetcher  # noqa: E402

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DEFAULT_CACHE = os.path.join(os.path.expanduser("~"), ".cache", "discere-deckbuilder")


def main():
    parser = argparse.ArgumentParser(description="Deck aus einem Rezept und Beobachtungsdaten bauen")
    parser.add_argument("recipe", help="Rezept, z. B. recipes/karibik.json")
    parser.add_argument("--decks-dir", default=os.path.join(ROOT, "data", "decks"))
    parser.add_argument("--cache-dir", default=DEFAULT_CACHE, help="Caches außerhalb des Repos")
    parser.add_argument("--refresh", action="store_true",
                        help="Quellen und Salz/Süß-Angaben neu abfragen statt aus dem Cache lesen")
    parser.add_argument("--reference-db", help="diese Referenz-DB nehmen statt der neuesten laut Manifest")
    parser.add_argument("--inat-names", default=os.path.join(ROOT, "recipes", "inat_names.json"),
                        help="Zuordnung von iNaturalist-Namen zu Namen der Referenz-DB")
    parser.add_argument("--fishbase-version", default=water_flags.DEFAULT_VERSION,
                        help="Version der FishBase/SeaLifeBase-Parquets für Salz/Süß")
    args = parser.parse_args()

    started = time.monotonic()
    try:
        # Checked here already, so a broken recipe stops before the reference
        # DB is downloaded; build.run checks it again for its own callers.
        recipe.load(args.recipe)
        name_map = inat_names.load(args.inat_names)
        db_path = args.reference_db or refdb.ensure_reference_db(args.cache_dir)
        water = water_flags.load(args.cache_dir, args.fishbase_version, args.refresh)
    except (OSError, RuntimeError, recipe.RecipeError) as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(build.EXIT_STOPPED)
    db = refdb.ReferenceDb(db_path)
    fetcher = CachedFetcher(os.path.join(args.cache_dir, "http"), refresh=args.refresh)
    meta = [
        ("Referenz-DB", db.describe()),
        ("Salz/Süß", f"FishBase/SeaLifeBase {args.fishbase_version} (species.parquet)"),
    ]
    code = build.run(args.recipe, args.decks_dir, fetcher, db, water, meta, name_map)
    db.close()
    print(f"HTTP: {fetcher.network_requests} Requests ans Netz, {fetcher.cache_hits} aus dem Cache; "
          f"{time.monotonic() - started:.0f} s")
    sys.exit(code)


if __name__ == "__main__":
    main()
