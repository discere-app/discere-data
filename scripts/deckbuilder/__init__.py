# =============================================================================
# deckbuilder — build a deck with level subdecks from observation data
#
# Turns a recipe (recipes/<base>.json, schema/recipe.schema.json) into a deck
# (data/decks/<base>.json) and a report of the evidence behind it
# (recipes/<base>.report.md). Data set the order, distribution data and a
# field guide confirm that a species occurs in the region, and a person picks
# only the highlights.
#
# One module per source (inat, gbif, obis, reef_csv, water_flags, refdb,
# guide), the selection as pure functions without network or files
# (selection), the deck and the report on their own (deck, report), and the
# run that ties them together (build). Entry point: scripts/build_deck.py.
#
# This file stays empty on purpose: scripts/merge_level_decks.py imports
# deckbuilder.levels, and must not pull in the rest of the package with it.
# =============================================================================
