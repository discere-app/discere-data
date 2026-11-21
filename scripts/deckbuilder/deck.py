# =============================================================================
# deck.py — the deck file a recipe produces
#
# Format 2 with one subdeck per level (deckbuilder/levels.py: ids level-1 …,
# names in every app language), then the recipe's extra subdecks
# (deckbuilder/extra.py) with the id and names the recipe gives them. What
# the recipe sets is written anew on every run: name, description,
# translations, learning settings, sources, speciesNames and subdecks, and
# imageUrl/createdBy if the recipe has them.
# Everything else an existing deck file holds stays as it is — above all its
# sourceId (assigned by scripts/sync_index.sh, the deck's identity in the
# app) and supersedes.
#
# With iNaturalist as the order source, a species is named as iNaturalist
# names it in the region (its most observed name there): iNaturalist often
# splits a species complex the reference DB still holds as one species with
# the regional names as synonyms (Halichoeres annularis in the Andaman Sea,
# H. marginatus in the reference DB). The app resolves the name through
# those synonyms all the same, and the deck is right once the reference DB
# splits. Every name counted for a species resolves to it by construction;
# deckbuilder/build.py checks the written names once more.
#
# Otherwise (another order source, a highlight iNaturalist does not count)
# a species is named by its preferred scientific name in the reference DB,
# so the app resolves it for sure — unless the app would resolve that name
# to another species (a homonym); then the name from the source stays.
# =============================================================================

from .levels import level_subdeck

# Key order of a written deck; keys the deckbuilder does not know follow.
KEY_ORDER = [
    "$schema", "formatVersion", "name", "description", "translations", "imageUrl", "sources",
    "createdBy", "learningMode", "nameType", "reviewMode", "speciesNames", "subdecks",
    "supersedes", "sourceId",
]

RECIPE_FIELDS = ["name", "description", "translations", "imageUrl", "createdBy", "learningMode", "nameType", "reviewMode"]

ORDER_SOURCES = {
    "inat": {"name": "iNaturalist", "url": "https://www.inaturalist.org/"},
    "gbif": {"name": "GBIF", "url": "https://www.gbif.org/"},
    "reef": {"name": "REEF", "url": "https://www.reef.org/"},
}
OBIS = {"name": "OBIS", "url": "https://obis.org/"}
FISHBASE = {"name": "FishBase", "url": "https://www.fishbase.org/"}
SEALIFEBASE = {"name": "SeaLifeBase", "url": "https://www.sealifebase.org/"}


def deck_name(facts, source_names):
    """The name the deck writes for a species without a regional name."""
    if facts.preferred_resolves or not source_names:
        return facts.preferred_name
    return source_names[0]


def deck_names(facts, candidates, highlights, resolution, regional):
    """species id → the name the deck writes (see the file comment).
    `candidates` are the order source's (selection.Candidate, names most
    counted first), `highlights` the recipe's highlight names, `regional`
    whether the order source's names are the region's (iNaturalist)."""
    names = {}
    for species_id, facts_ in facts.items():
        candidate = candidates.get(species_id)
        if candidate and regional:
            names[species_id] = candidate.names[0]
        else:
            source = candidate.names if candidate else [h for h in highlights if resolution.get(h) == species_id]
            names[species_id] = deck_name(facts_, source)
    return names


def deck_sources(recipe, species_sources):
    """The sources the deck was built from: the order source, OBIS if
    asked, FishBase/SeaLifeBase for the species they hold, and every guide
    with a URL."""
    sources = [ORDER_SOURCES[recipe["order"]["source"]]]
    if "obis" in recipe.get("region", {}):
        sources.append(OBIS)
    if "fishbase" in species_sources:
        sources.append(FISHBASE)
    if "sealifebase" in species_sources:
        sources.append(SEALIFEBASE)
    for guide in recipe.get("guides", []):
        if guide.get("url"):
            sources.append({"name": guide["name"], "url": guide["url"]})
    return sources


def extra_subdeck(spec, species_names):
    subdeck = {"id": spec["id"], "name": spec["name"]}
    if "translations" in spec:
        subdeck["translations"] = spec["translations"]
    subdeck["speciesNames"] = list(species_names)
    return subdeck


def build_deck(recipe, levels, sources, existing=None, extras=()):
    """The deck for `levels` ([[name]] from level 1) and `extras` ([(spec,
    [name])], one per extra subdeck), on top of the existing deck file's
    content if there is one. A level or extra subdeck left empty gets no
    subdeck."""
    deck = dict(existing or {})
    deck["formatVersion"] = 2
    for field in RECIPE_FIELDS:
        if field in recipe["deck"]:
            deck[field] = recipe["deck"][field]
    deck.setdefault("imageUrl", "")
    deck["sources"] = sources
    deck["speciesNames"] = [name for level in levels for name in level] + [n for _, names in extras for n in names]
    deck["subdecks"] = [level_subdeck(n, names) for n, names in enumerate(levels, 1) if names]
    deck["subdecks"] += [extra_subdeck(spec, names) for spec, names in extras if names]
    ordered = {key: deck[key] for key in KEY_ORDER if key in deck}
    ordered.update((key, value) for key, value in deck.items() if key not in ordered)
    return ordered
