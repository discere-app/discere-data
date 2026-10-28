#!/usr/bin/env bash
# =============================================================================
# list_deck_files.sh — the deck files of the catalog, one path per line
#
# The one rule for which files under data/decks/ are decks: every *.json
# directly in it except the generated index.json (the v<N>/ indexes sit in
# subdirectories). scripts/sync_index.sh and the index dry run in
# .github/workflows/validate-decks.yml both read the decks through it, so
# the dry run checks exactly the decks the sync publishes.
#
# Paths are newline-separated, sorted, and absolute. A deck file name holds
# no newline.
#
# Usage:
#   ./scripts/list_deck_files.sh
# =============================================================================

set -euo pipefail

DECKS_DIR="$(cd "$(dirname "$0")/.." && pwd)/data/decks"

find "$DECKS_DIR" -maxdepth 1 -name '*.json' ! -name 'index.json' | sort
