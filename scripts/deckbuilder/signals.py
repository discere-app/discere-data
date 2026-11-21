# =============================================================================
# signals.py — what iNaturalist says beyond the counts, per deck species
#
# The order source counts observations; two more questions decide whether a
# count means "a diver meets this here" (deckbuilder/findings.py judges):
#
# - Annotation Alive or Dead: how many of a species' observations in the
#   region are annotated alive, how many dead. Two species_counts queries
#   per region and taxa, whatever the number of species.
# - Observers: how many people observed the species, and how many
#   observations the most active of them made. One request per species, so
#   only for the species where the answer matters (levels 1 and 2 and the
#   highlights), not for every candidate.
#
# iNaturalist names are mapped (recipes/inat_names.json) and resolved like
# the order source's, so a signal lands on the species the deck holds.
# =============================================================================

from dataclasses import dataclass, field

from . import inat, inat_names
from .selection import counts_by_id


@dataclass
class Signals:
    alive: dict = field(default_factory=dict)      # species id → observations annotated alive
    dead: dict = field(default_factory=dict)       # species id → observations annotated dead
    observers: dict = field(default_factory=dict)  # species id → (observers, [observations of the most active])


def taxon_ids_by_species(taxon_ids, name_map, resolution):
    """species id → the iNaturalist taxon ids counted for it, from the
    order source's name → taxon id."""
    target = {entry["inat"]: entry["referenceDb"] for entry in name_map}
    by_species = {}
    for name, taxon_id in taxon_ids.items():
        species_id = resolution.get(target.get(name, name))
        if species_id is not None:
            by_species.setdefault(species_id, []).append(taxon_id)
    return by_species


def collect(fetcher, region, taxa, source, name_map, resolution, observed_ids, top):
    """The signals for the species counted under `taxa` in `region`
    (recipe region.inat, None for worldwide); `source` is the order
    source's inat.species_counts result, `observed_ids` the species whose
    `top` most active observers are asked for."""
    def by_species(counts):
        return counts_by_id(inat_names.apply(counts, name_map)[0], resolution)

    alive = by_species(inat.annotation_counts(fetcher, region, taxa, inat.ALIVE))
    dead = by_species(inat.annotation_counts(fetcher, region, taxa, inat.DEAD))
    taxon_ids = taxon_ids_by_species(source.taxon_ids, name_map, resolution)
    observers = {
        i: inat.top_observers(fetcher, region, taxon_ids[i], top) for i in observed_ids if i in taxon_ids
    }
    return Signals(alive, dead, observers)
