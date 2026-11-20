# =============================================================================
# water_flags.py — freshwater, brackish and saltwater per species
#
# FishBase and SeaLifeBase mark each species with Fresh, Brack and Saltwater
# (0/1) in species.parquet. The reference DB's habitat label cannot stand in
# for them (the tarpon's reads "freshwater stream"). The parquets are read
# remotely with DuckDB, as scripts/reef/ does, joined to the reference DB by
# SpecCode (species.external_id), and the flags of both sources are kept as
# JSON under ~/.cache/discere-deckbuilder/water_flags/, so later runs need
# neither the network nor DuckDB.
#
# DuckDB is imported only when the flags are fetched, so the rest of the
# deckbuilder and its tests run without it.
#
# How a flag triple counts (see selection.water_verdict): SeaLifeBase leaves
# all three at 0 for thousands of species, which means unknown, not "lives
# nowhere".
# =============================================================================

import json
import os

PARQUET = "https://huggingface.co/datasets/cboettig/fishbase/resolve/main/data/{db}/{version}/parquet/species.parquet"
SOURCES = {"fishbase": "fb", "sealifebase": "slb"}
DEFAULT_VERSION = "v25.04"


def _fetch(version):
    try:
        import duckdb
    except ImportError as e:
        raise RuntimeError("duckdb fehlt (pip install duckdb); es liest die Salz/Süß-Angaben aus den Parquets") from e
    con = duckdb.connect()
    flags = {}
    for source, db in SOURCES.items():
        url = PARQUET.format(db=db, version=version)
        rows = con.execute(
            "SELECT CAST(SpecCode AS VARCHAR), COALESCE(Fresh, 0), COALESCE(Brack, 0), COALESCE(Saltwater, 0) "
            f"FROM read_parquet('{url}')"
        ).fetchall()
        flags[source] = {code: [int(fresh), int(brack), int(salt)] for code, fresh, brack, salt in rows}
    con.close()
    return flags


def load(cache_dir, version=DEFAULT_VERSION, refresh=False):
    """{(source, SpecCode): (fresh, brack, salt)} for every species of
    FishBase and SeaLifeBase."""
    path = os.path.join(cache_dir, "water_flags", f"{version}.json")
    if refresh or not os.path.exists(path):
        print(f"Lade Salz/Süß-Angaben aus FishBase/SeaLifeBase {version} …")
        flags = _fetch(version)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(f"{path}.tmp", "w", encoding="utf-8") as f:
            json.dump(flags, f)
        os.replace(f"{path}.tmp", path)
    with open(path, encoding="utf-8") as f:
        flags = json.load(f)
    return {(source, code): tuple(value) for source, by_code in flags.items() for code, value in by_code.items()}
