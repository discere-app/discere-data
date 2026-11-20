# =============================================================================
# gbif.py — species counts from GBIF for a country
#
# The order source for inland waters, where iNaturalist is too sparse:
# occurrences per species in one or more countries (GET
# /v1/occurrence/search with facet=speciesKey; country repeated, which GBIF
# reads as "any of them").
#
# In the current GBIF backbone the ray-finned fishes have no class, so a
# class key finds nothing. The way that works goes through the orders: facet
# the occurrences of the phylum (44, Chordata) by order, keep the orders the
# reference DB knows as FishBase orders (the fish orders), then facet those
# orders by species. Names come from GET /v1/species/{key} (canonicalName).
#
# Fossils (the Glarus slate yields Lepidopus glarisianus in Switzerland) and
# zoo or aquarium animals are left out by naming the kinds of record that
# count: GBIF's basisOfRecord takes no negation ("!FOSSIL_SPECIMEN" is
# rejected), only a list. Names the reference DB does not resolve drop out
# later, which takes care of the remaining fossil taxa.
# =============================================================================

from .sources import SourceResult

SEARCH = "https://api.gbif.org/v1/occurrence/search"
SPECIES = "https://api.gbif.org/v1/species/{key}"
FACET_LIMIT = 1000

# Every basisOfRecord except FOSSIL_SPECIMEN and LIVING_SPECIMEN.
BASIS_OF_RECORD = [
    "HUMAN_OBSERVATION",
    "MACHINE_OBSERVATION",
    "OBSERVATION",
    "OCCURRENCE",
    "PRESERVED_SPECIMEN",
    "MATERIAL_SAMPLE",
    "MATERIAL_CITATION",
]


def facet_counts(fetcher, params, facet):
    """[(key, count)] of the facet over all its pages."""
    counts, offset = [], 0
    while True:
        body = fetcher.get_json(SEARCH, {
            **params, "limit": 0, "facet": facet, "facetLimit": FACET_LIMIT, "facetOffset": offset,
        })
        facets = body.get("facets") or []
        page = facets[0]["counts"] if facets else []
        counts.extend((int(c["name"]), c["count"]) for c in page)
        if len(page) < FACET_LIMIT:
            return counts
        offset += FACET_LIMIT


def canonical_name(fetcher, key):
    return fetcher.get_json(SPECIES.format(key=key)).get("canonicalName")


def species_counts(fetcher, countries, phylum_key, fish_orders):
    base = {"country": list(countries), "occurrenceStatus": "PRESENT", "basisOfRecord": BASIS_OF_RECORD}
    orders = facet_counts(fetcher, {**base, "phylumKey": phylum_key}, "orderKey")
    kept = [key for key, _ in orders if canonical_name(fetcher, key) in fish_orders]
    notes = [f"GBIF: {len(kept)} von {len(orders)} Ordnungen als Fischordnungen behalten"]
    if not kept:
        return SourceResult([], notes)
    species = facet_counts(fetcher, {**base, "orderKey": kept}, "speciesKey")
    counts = [(canonical_name(fetcher, key), count) for key, count in species]
    notes.append(f"GBIF: {len(counts)} Arten")
    return SourceResult([(name, count) for name, count in counts if name], notes)
