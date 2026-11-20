# =============================================================================
# inat.py — species counts from iNaturalist
#
# The order source for most seas: how often each species was observed in the
# region (GET /v1/observations/species_counts). Only research-grade
# observations count, which also leaves out captive and cultivated ones. The
# region is an iNaturalist place (placeId) or a rectangle
# (swlat/swlng/nelat/nelng), for seas without a fitting place.
#
# The taxa are iNaturalist taxon IDs, e.g. 47178 ray-finned fishes (class
# Actinopterygii), 47273 sharks and rays (subclass Elasmobranchii), 49232
# lampreys (order Petromyzontiformes). 47237 is not the lampreys but the
# angelfish family Pomacanthidae.
# =============================================================================

from .sources import SourceResult

API = "https://api.inaturalist.org/v1/observations/species_counts"
PER_PAGE = 500
# iNaturalist pages no further than this many results.
MAX_RESULTS = 10_000


def region_params(region):
    if "placeId" in region:
        return {"place_id": region["placeId"]}
    return {key: region[key] for key in ("swlat", "swlng", "nelat", "nelng")}


def species_counts(fetcher, region, taxon_ids):
    params = {
        **region_params(region),
        "taxon_id": ",".join(str(t) for t in taxon_ids),
        "quality_grade": "research",
        "per_page": PER_PAGE,
    }
    counts, notes = [], []
    page = 1
    while True:
        body = fetcher.get_json(API, {**params, "page": page})
        results = body.get("results") or []
        counts.extend((r["taxon"]["name"], r["count"]) for r in results)
        total = body.get("total_results", 0)
        if not results or page * PER_PAGE >= min(total, MAX_RESULTS):
            break
        page += 1
    if total > MAX_RESULTS:
        notes.append(f"iNaturalist liefert nur die ersten {MAX_RESULTS} von {total} Taxa")
    notes.append(f"iNaturalist: {len(counts)} Taxa ({page} Seiten)")
    return SourceResult(counts, notes)
