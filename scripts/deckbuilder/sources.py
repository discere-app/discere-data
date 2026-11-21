# =============================================================================
# sources.py — what every observation source returns
#
# A source answers with the names it knows for the region, each with a
# count: observations (iNaturalist, GBIF), records (OBIS) or sighting
# frequency SF% (REEF). The names are the source's own; the reference DB
# resolves them afterwards. The notes say what the query did, for the report.
# =============================================================================

from dataclasses import dataclass, field


@dataclass
class SourceResult:
    counts: list                       # [(name, count)]
    notes: list = field(default_factory=list)
    taxon_ids: dict = field(default_factory=dict)  # name → the source's taxon id, where it has one
