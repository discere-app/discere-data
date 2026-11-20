# =============================================================================
# levels.py — the level subdecks of a catalog deck
#
# Every catalog deck with levels names them the same way: id "level-<n>",
# which an update must keep (the app recognizes a subdeck by it), and the
# name "Level <n>" in every app language. Both scripts that write such decks
# (scripts/merge_level_decks.py and the deckbuilder) build their subdecks
# here, so a deck merged from level files and a deck built from a recipe
# cannot drift apart.
# =============================================================================

# Subdeck name per language; "de" is also the base name, since the base
# fields of the catalog decks are German.
LEVEL_NAMES = {"de": "Level {n}", "en": "Level {n}", "fr": "Niveau {n}", "es": "Nivel {n}"}


def level_subdeck(level, species_names):
    """The subdeck of level `level` (1-based) holding `species_names`."""
    return {
        "id": f"level-{level}",
        "name": LEVEL_NAMES["de"].format(n=level),
        "translations": {lang: {"name": text.format(n=level)} for lang, text in LEVEL_NAMES.items()},
        "speciesNames": list(species_names),
    }
