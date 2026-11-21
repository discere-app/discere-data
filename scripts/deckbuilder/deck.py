# =============================================================================
# deck.py — the deck file a recipe produces
#
# Format 2 with one subdeck per level (deckbuilder/levels.py: ids level-1 …,
# names in every app language). What the recipe sets is written anew on
# every run: name, description, translations, learning settings, sources,
# speciesNames and subdecks, and imageUrl/createdBy if the recipe has them.
# Everything else an existing deck file holds stays as it is — above all its
# sourceId (assigned by scripts/sync_index.sh, the deck's identity in the
# app) and supersedes.
#
# A species is named by its preferred scientific name in the reference DB,
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
    """The name the deck writes for a species (see the file comment)."""
    if facts.preferred_resolves or not source_names:
        return facts.preferred_name
    return source_names[0]


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


def build_deck(recipe, levels, sources, existing=None):
    """The deck for `levels` ([[name]] from level 1), on top of the existing
    deck file's content if there is one. A level left empty gets no
    subdeck."""
    deck = dict(existing or {})
    deck["formatVersion"] = 2
    for field in RECIPE_FIELDS:
        if field in recipe["deck"]:
            deck[field] = recipe["deck"][field]
    deck.setdefault("imageUrl", "")
    deck["sources"] = sources
    deck["speciesNames"] = [name for level in levels for name in level]
    deck["subdecks"] = [level_subdeck(n, names) for n, names in enumerate(levels, 1) if names]
    ordered = {key: deck[key] for key in KEY_ORDER if key in deck}
    ordered.update((key, value) for key, value in deck.items() if key not in ordered)
    return ordered
