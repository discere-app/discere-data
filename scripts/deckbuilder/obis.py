# =============================================================================
# obis.py — species checklist from OBIS for a sea area
#
# Records per species in one or more sea areas (GET /v3/checklist), for
# WoRMS taxon IDs (Actinopteri 10194, Elasmobranchii 10193). Only rank
# "Species" counts; the checklist also lists genera and families. Several
# areas go into one MULTIPOLYGON, which OBIS counts as one area: a record
# inside two overlapping areas counts once.
#
# OBIS also holds iNaturalist's research-grade marine observations, the same
# observations the order source counts; in the reef regions they were most
# of the OBIS records. A count that confirms the order source has to be
# independent of it, so their records are taken off: the checklist is asked
# twice, once in full and once for that dataset alone (the API filters by a
# dataset, but cannot leave one out).
#
# OBIS reflects research effort rather than what a diver sees: in the
# Caribbean, monitoring programs and lagoon fisheries put the goliath grouper
# and Colombian lagoon fishes on top. So OBIS only confirms that a species
# occurs in the region and never sets the order.
# =============================================================================

from .sources import SourceResult

API = "https://api.obis.org/v3/checklist"
# "iNaturalist Research-grade Observations Marine Subset"
# (https://api.obis.org/v3/dataset/eaea291a-1e1d-4382-b86f-ac3cc15b8d5a).
INATURALIST_DATASET = "eaea291a-1e1d-4382-b86f-ac3cc15b8d5a"
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


def _species_records(fetcher, params):
    """[(name, records)] of the species in the checklist for `params`."""
    counts, skip = [], 0
    while True:
        body = fetcher.get_json(API, {**params, "skip": skip})
        results = body.get("results") or []
        counts.extend((r["scientificName"], r.get("records", 0)) for r in results if r.get("taxonRank") == "Species")
        skip += len(results)
        if not results or skip >= body.get("total", 0):
            break
    return counts


def checklist(fetcher, wkts, taxon_ids):
    """Records per species in the areas, without those of the iNaturalist
    dataset; a species only iNaturalist records is left out."""
    params = {"geometry": combined_geometry(wkts), "taxonid": ",".join(str(t) for t in taxon_ids), "size": PAGE_SIZE}
    from_inat = dict(_species_records(fetcher, {**params, "datasetid": INATURALIST_DATASET}))
    counts = []
    for name, records in _species_records(fetcher, params):
        independent = records - from_inat.get(name, 0)
        if independent > 0:
            counts.append((name, independent))
    return SourceResult(counts, [f"OBIS: {len(counts)} Arten mit Nachweisen außer iNaturalist"])
