# =============================================================================
# obis.py — species checklist from OBIS for a sea area
#
# Records per species in one or more sea areas (GET /v3/checklist), for
# WoRMS taxon IDs (Actinopteri 10194, Elasmobranchii 10193). Only rank
# "Species" counts; the checklist also lists genera and families. Several
# areas go into one MULTIPOLYGON, which OBIS counts as one area: a record
# inside two overlapping areas counts once.
#
# OBIS reflects research effort rather than what a diver sees: in the
# Caribbean, monitoring programs and lagoon fisheries put the goliath grouper
# and Colombian lagoon fishes on top. So OBIS only confirms that a species
# occurs in the region and never sets the order.
# =============================================================================

from .sources import SourceResult

API = "https://api.obis.org/v3/checklist"
PAGE_SIZE = 1000


def _polygons(wkt):
    """The polygon bodies of a POLYGON or MULTIPOLYGON, e.g. "((0 0, …))"."""
    text = wkt.strip()
    body = text[text.index("("):]
    if text.upper().startswith("MULTIPOLYGON"):
        return body[1:-1].strip()
    return body


def combined_geometry(wkts):
    """One geometry for several areas: a single one as given, more as one
    MULTIPOLYGON."""
    if len(wkts) == 1:
        return wkts[0]
    return "MULTIPOLYGON(" + ",".join(_polygons(w) for w in wkts) + ")"


def checklist(fetcher, wkts, taxon_ids):
    params = {"geometry": combined_geometry(wkts), "taxonid": ",".join(str(t) for t in taxon_ids), "size": PAGE_SIZE}
    counts, skip = [], 0
    while True:
        body = fetcher.get_json(API, {**params, "skip": skip})
        results = body.get("results") or []
        counts.extend((r["scientificName"], r.get("records", 0)) for r in results if r.get("taxonRank") == "Species")
        skip += len(results)
        if not results or skip >= body.get("total", 0):
            break
    return SourceResult(counts, [f"OBIS: {len(counts)} Arten"])
