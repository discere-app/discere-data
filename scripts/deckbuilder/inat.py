# =============================================================================
# inat.py — species counts from iNaturalist
#
# The order source for most seas: how often each species was observed in the
# region (GET /v1/observations/species_counts). Only research-grade
# observations count, which also leaves out captive and cultivated ones. The
# region is one or more iNaturalist places (placeIds, asked as one
# comma-separated place_id, which iNaturalist counts together without
# counting an observation twice) or a rectangle (swlat/swlng/nelat/nelng).
# Without a region the counts are worldwide, the order for a deck about a
# group of animals rather than a region.
#
# The taxa are iNaturalist taxon IDs, e.g. 47178 ray-finned fishes (class
# Actinopterygii), 47273 sharks and rays (subclass Elasmobranchii), 49232
# lampreys (order Petromyzontiformes). 47237 is not the lampreys but the
# angelfish family Pomacanthidae.
#
# Besides the counts, two signals for the report (deckbuilder/findings.py):
# how many observations are annotated alive and how many dead (an empty
# shell, a fish on the market) — the value Cannot Be Determined says
# neither and does not count — and who observed a
# species: if two people account for most observations, the count says
# little about how common it is.
# =============================================================================

from .sources import SourceResult

API = "https://api.inaturalist.org/v1/observations/species_counts"
OBSERVERS = "https://api.inaturalist.org/v1/observations/observers"
# The controlled term "Alive or Dead" and its values "Alive" and "Dead".
ALIVE_OR_DEAD = 17
ALIVE = 18
DEAD = 19
PLACES = "https://api.inaturalist.org/v1/places/{ids}"
PER_PAGE = 500
# iNaturalist pages no further than this many results.
MAX_RESULTS = 10_000
# Places per request to /v1/places/{ids}.
PER_PLACES_REQUEST = 50


def region_params(region):
    """Query parameters of a recipe's region.inat; None means worldwide."""
    if region is None:
        return {}
    if "placeIds" in region:
        return {"place_id": ",".join(str(i) for i in region["placeIds"])}
    return {key: region[key] for key in ("swlat", "swlng", "nelat", "nelng")}


def place_names(fetcher, place_ids):
    """place id → display name, for the report."""
    names = {}
    ids = list(place_ids)
    for i in range(0, len(ids), PER_PLACES_REQUEST):
        chunk = ids[i:i + PER_PLACES_REQUEST]
        body = fetcher.get_json(PLACES.format(ids=",".join(str(p) for p in chunk)))
        names.update((p["id"], p["display_name"]) for p in body.get("results") or [])
    return names


def _species_count_pages(fetcher, params):
    """All results of /v1/observations/species_counts for `params`, and the
    notes on paging."""
    results, page = [], 1
    while True:
        body = fetcher.get_json(API, {**params, "per_page": PER_PAGE, "page": page})
        found = body.get("results") or []
        results.extend(found)
        total = body.get("total_results", 0)
        if not found or page * PER_PAGE >= min(total, MAX_RESULTS):
            break
        page += 1
    notes = [f"iNaturalist liefert nur die ersten {MAX_RESULTS} von {total} Taxa"] if total > MAX_RESULTS else []
    return results, notes, page


def _query(region, taxon_ids):
    return {**region_params(region), "taxon_id": ",".join(str(t) for t in taxon_ids), "quality_grade": "research"}


def species_counts(fetcher, region, taxon_ids):
    results, notes, pages = _species_count_pages(fetcher, _query(region, taxon_ids))
    counts = [(r["taxon"]["name"], r["count"]) for r in results]
    notes.append(f"iNaturalist: {len(counts)} Taxa (Seiten: {pages})")
    return SourceResult(counts, notes, {r["taxon"]["name"]: r["taxon"]["id"] for r in results if "id" in r["taxon"]})


def annotation_counts(fetcher, region, taxon_ids, value_id):
    """[(name, count)] of the observations annotated Alive or Dead with the
    value `value_id` (ALIVE or DEAD)."""
    params = {**_query(region, taxon_ids), "term_id": ALIVE_OR_DEAD, "term_value_id": value_id}
    results, _, _ = _species_count_pages(fetcher, params)
    return [(r["taxon"]["name"], r["count"]) for r in results]


def top_observers(fetcher, region, taxon_ids, top):
    """(number of observers, [observation counts of the `top` most active])
    of the taxa, among the research-grade observations in the region."""
    body = fetcher.get_json(OBSERVERS, {
        **_query(region, taxon_ids), "order_by": "observation_count", "per_page": top,
    })
    return body.get("total_results", 0), [r["observation_count"] for r in (body.get("results") or [])[:top]]
