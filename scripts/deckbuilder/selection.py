# =============================================================================
# selection.py — which species go into the deck, and on which level
#
# Pure functions over what the sources and the reference DB said; no
# network, no files. The rules:
#
# 1. Candidates are the species of the order source, resolved against the
#    reference DB (names that resolve to one species count together) and
#    filtered: water type, minimum count, not only deeper than the dive
#    limit, not smaller than the minimum length. Every exclusion keeps its
#    reason for the report; an unknown value never excludes.
# 2. The candidates are ranked by their count, descending; a tie goes by
#    name, so a run gives the same order every time.
# 3. Level 1 holds the first N1 candidates plus every highlight not already
#    among them. Levels 2, 3, … take the next N2, N3, … candidates, skipping
#    the highlights, which are on level 1.
# 4. A highlight is picked by hand for being worth knowing, not for being
#    common. It needs evidence in the region all the same: a record in the
#    order source or OBIS, an entry in the FishBase/SeaLifeBase distribution
#    of a recipe region that does not say "absent", or a line in a guide.
#    Without one (or without a name the reference DB resolves) it stays out
#    of the deck. Highlights picked automatically by "rare here, common
#    elsewhere" turned out to be mostly misidentifications, such as
#    Indo-Pacific species reported from the Caribbean — so no highlight goes
#    in on a person's word alone either.
# 5. A guide never filters; the comparison with it is a report, both ways.
# =============================================================================

from dataclasses import dataclass, field

# Water types of a recipe, and the flag that has to be set for each; a
# species whose three flags are all 0 counts as unknown and stays in.
WATER_FLAG = {"salt": 2, "fresh": 0}

# How many species on each side of a level boundary the report shows.
BOUNDARY_WIDTH = 10


@dataclass
class Candidate:
    id: str
    count: float
    names: list = field(default_factory=list)   # the source's names for it


@dataclass
class Evidence:
    """What says a species occurs in the region."""
    order_count: float = None      # count in the order source, None if not listed
    obis_records: int = None       # OBIS records, None if not listed
    occurrences: list = field(default_factory=list)  # refdb.Occurrence in the recipe regions
    guides: list = field(default_factory=list)       # names of the guides that list it

    def found(self):
        return bool(
            self.order_count
            or self.obis_records
            or any(o.is_evidence for o in self.occurrences)
            or self.guides
        )


@dataclass
class Selection:
    candidates: dict           # id → Candidate, every resolved species of the order source
    unresolved: list           # [(name, count)] the reference DB does not know
    excluded: list             # [(id, reason, detail)]
    ranked: list               # ids of the candidates that passed, best first
    levels: list               # [[id]] per level
    sequence: list             # the ranked ids as the levels take them, highlights out of order
    cuts: list                 # index into sequence where each level ends
    highlights: list           # ids of the accepted highlights, in recipe order
    rejected_highlights: list  # [(name, reason)]


def aggregate(counts, resolution, combine=sum):
    """Counts per resolved species, and the names that did not resolve.
    `combine` merges the counts of two names of one species: sum for
    observations, max for a frequency."""
    by_id, unresolved = {}, []
    for name, count in counts:
        species_id = resolution.get(name)
        if species_id is None:
            unresolved.append((name, count))
            continue
        candidate = by_id.setdefault(species_id, Candidate(species_id, None))
        candidate.count = count if candidate.count is None else combine([candidate.count, count])
        candidate.names.append(name)
    unresolved.sort(key=lambda item: (-item[1], item[0]))
    return by_id, unresolved


def water_verdict(flags, water):
    """Whether a species with FishBase/SeaLifeBase flags (fresh, brack,
    salt) fits the recipe's water type. Missing flags or all three 0 mean
    unknown, which fits. Brackish alone does not make a sea fish: a
    rectangle over Florida would bring in mosquitofish and peacock bass."""
    if water == "any" or flags is None or not any(flags):
        return True
    return bool(flags[WATER_FLAG[water]])


def exclusion_reason(candidate, facts, flags, filters):
    """Why a candidate stays out, as (reason, detail), or None if it passes
    every filter. The reason is one of a few fixed texts, so the report can
    count by it; the detail gives the species' own value."""
    water = filters.get("water", "any")
    if not water_verdict(flags, water):
        return ("kein Meeresfisch", "Saltwater nicht gesetzt") if water == "salt" \
            else ("kein Süßwasserfisch", "Fresh nicht gesetzt")
    min_count = filters.get("minCount")
    if min_count is not None and candidate.count < min_count:
        return "zu wenige Nachweise", f"{candidate.count:g} < {min_count:g}"
    depth_limit = filters.get("diveDepthLimitM")
    if depth_limit is not None and facts.depth_min_m is not None and facts.depth_min_m > depth_limit:
        return "nur tiefer als die Tauchgrenze", f"erst ab {facts.depth_min_m:g} m"
    min_length = filters.get("minLengthCm")
    if min_length is not None and facts.max_length_cm is not None and facts.max_length_cm < min_length:
        return "zu klein", f"höchstens {facts.max_length_cm:g} cm"
    return None


def rank(candidates, names):
    """Candidate ids by count, descending; ties by deck name."""
    return [c.id for c in sorted(candidates, key=lambda c: (-c.count, names[c.id]))]


def split_levels(ranked, highlights, sizes):
    """The levels, the sequence they are cut from and the cut indices.
    Level 1 is the first sizes[0] of `ranked` plus every highlight not
    among them; the later levels follow in `ranked` order, highlights left
    out."""
    top = ranked[:sizes[0]]
    picked = set(highlights)
    rest = [i for i in ranked[sizes[0]:] if i not in picked]
    levels = [top + [h for h in highlights if h not in top]]
    sequence = top + rest
    cuts, end = [sizes[0]], 0
    for size in sizes[1:]:
        levels.append(rest[end:end + size])
        end += size
        cuts.append(sizes[0] + end)
    return levels, sequence, [min(c, len(sequence)) for c in cuts]


def check_highlights(names, resolution, evidence):
    """Accepted highlight ids in recipe order, and the rejected names with
    their reason."""
    accepted, rejected = [], []
    for name in names:
        species_id = resolution.get(name)
        if species_id is None:
            rejected.append((name, "Name in der Referenz-DB nicht gefunden"))
        elif not evidence.get(species_id, Evidence()).found():
            rejected.append((name, "kein Nachweis in der Region"))
        elif species_id not in accepted:
            accepted.append(species_id)
    return accepted, rejected


def select(order_counts, resolution, facts, flags, evidence, recipe, combine=sum):
    """The whole selection of a recipe. `resolution` maps every name (order
    source and highlights) to a species id or None; `facts`, `flags` and
    `evidence` are per species id (refdb.SpeciesFacts, the water flag
    triple if known, Evidence)."""
    candidates, unresolved = aggregate(order_counts, resolution, combine)
    filters = recipe.get("filters", {})
    passed, excluded = [], []
    for candidate in candidates.values():
        reason = exclusion_reason(candidate, facts[candidate.id], flags.get(candidate.id), filters)
        if reason:
            excluded.append((candidate.id, *reason))
        else:
            passed.append(candidate)
    names = {i: f.preferred_name for i, f in facts.items()}
    excluded.sort(key=lambda item: (-candidates[item[0]].count, names[item[0]]))
    ranked = rank(passed, names)
    highlights, rejected = check_highlights(recipe.get("highlights", []), resolution, evidence)
    levels, sequence, cuts = split_levels(ranked, highlights, recipe["levelSizes"])
    return Selection(candidates, unresolved, excluded, ranked, levels, sequence, cuts, highlights, rejected)


def boundaries(selection, width=BOUNDARY_WIDTH):
    """Per level boundary: (level number, the last `width` ids before it,
    the first `width` after it)."""
    result = []
    for level, cut in enumerate(selection.cuts, 1):
        before = selection.sequence[max(0, cut - width):cut]
        after = selection.sequence[cut:cut + width]
        if before or after:
            result.append((level, before, after))
    return result


def compare_with_guide(deck_ids, guide_ids, ranked):
    """Deck species the guide lacks (suspects), and ranked candidates in the
    guide but not in the deck (candidates), each in deck or rank order."""
    in_deck = set(deck_ids)
    suspects = [i for i in deck_ids if i not in guide_ids]
    missing = [i for i in ranked if i in guide_ids and i not in in_deck]
    return suspects, missing
