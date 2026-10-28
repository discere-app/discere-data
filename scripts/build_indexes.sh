#!/usr/bin/env bash
# =============================================================================
# build_indexes.sh — write the deck catalog indexes from a list of decks
#
# Used by scripts/sync_index.sh to write the published indexes, and by
# .github/workflows/validate-decks.yml for a dry run on every PR, so a
# broken index is caught before the merge. Given a JSON array of decks, it
# writes one index per format version into the target directory:
# index.json for format 1, whose path app versions without format versions
# read, and v<N>/index.json for every N from 2 up to the schema's
# formatVersion maximum, so raising that maximum is all a new format needs.
# Which decks an index holds is scripts/deck_index.jq's rule.
#
# Usage:
#   ./scripts/build_indexes.sh <decks.json> <target-dir>
#
# Requires: jq
# =============================================================================

set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "usage: $0 <decks.json> <target-dir>" >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SCHEMA_FILE="$SCRIPT_DIR/../schema/deck.schema.json"
INDEX_FILTER="$SCRIPT_DIR/deck_index.jq"
ALL_DECKS="$1"
TARGET_DIR="$2"

index_file_for() {
  if [ "$1" -eq 1 ]; then
    echo "$TARGET_DIR/index.json"
  else
    echo "$TARGET_DIR/v$1/index.json"
  fi
}

newest_format_version="$(jq -e '.properties.formatVersion.maximum' "$SCHEMA_FILE")"

echo "Generating indexes up to format $newest_format_version..."
for version in $(seq 1 "$newest_format_version"); do
  index_file="$(index_file_for "$version")"
  mkdir -p "$(dirname "$index_file")"
  jq --argjson version "$version" -f "$INDEX_FILTER" "$ALL_DECKS" > "$index_file"
  echo "Wrote $(jq length "$index_file") decks to $index_file"
done
