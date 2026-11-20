# =============================================================================
# obis.py — species checklist from OBIS for a sea area
#
# Records per species in a WKT polygon (GET /v3/checklist), for WoRMS taxon
# IDs (Actinopteri 10194, Elasmobranchii 10193). Only rank "Species" counts;
# the checklist also lists genera and families.
#
# OBIS reflects research effort rather than what a diver sees: in the
# Caribbean, monitoring programs and lagoon fisheries put the goliath grouper
# and Colombian lagoon fishes on top. So OBIS only confirms that a species
# occurs in the region and never sets the order.
# =============================================================================

from .sources import SourceResult

API = "https://api.obis.org/v3/checklist"
PAGE_SIZE = 1000


def checklist(fetcher, wkt, taxon_ids):
    params = {"geometry": wkt, "taxonid": ",".join(str(t) for t in taxon_ids), "size": PAGE_SIZE}
    counts, skip = [], 0
    while True:
        body = fetcher.get_json(API, {**params, "skip": skip})
        results = body.get("results") or []
        counts.extend((r["scientificName"], r.get("records", 0)) for r in results if r.get("taxonRank") == "Species")
        skip += len(results)
        if not results or skip >= body.get("total", 0):
            break
    return SourceResult(counts, [f"OBIS: {len(counts)} Arten"])
