#!/usr/bin/env bash
# =============================================================================
# sync_index.sh — regenerate and publish the deck catalog indexes
#
# Runs automatically via .github/workflows/sync-deck-index.yml on every push
# to main that touches data/decks/*.json (i.e. after a deck PR is merged)
# or schema/deck.schema.json (which names the newest format version),
# and can also be triggered manually (Actions tab -> "Run workflow") or run
# locally by a maintainer. Contributors never touch this - they only add a
# deck JSON file and open a PR. This script:
#   1. Pulls the latest main.
#   2. Assigns a stable `sourceId` (a UUID, not derived from the filename) to
#      any deck file that doesn't have one yet, and persists it back into
#      that file - so renaming a deck file later never changes its identity,
#      and there is no collision risk.
#   3. Adds `updatedAt` (ISO 8601, from the deck file's last git commit) to
#      every deck in the generated index. This script's own housekeeping
#      commits (sourceId assignment, index regeneration) are excluded when
#      looking up that date, so `updatedAt` reflects the last real content
#      edit, not the last time this script happened to touch the file.
#   4. Combines the deck files into one index per format version (the app
#      fetches its index instead of listing + fetching every deck file
#      individually): data/decks/index.json for format 1, whose path app
#      versions without format versions read, and data/decks/v<N>/index.json
#      for every N from 2 up to the schema's formatVersion maximum, so
#      raising that maximum is all a new format needs. Which decks an index
#      holds is scripts/deck_index.jq's rule.
#   5. Commits and pushes to main if anything changed.
#
# Usage:
#   ./scripts/sync_index.sh
#
# Requires: git, jq, uuidgen
# =============================================================================

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DECKS_DIR="$REPO_ROOT/data/decks"
SCHEMA_FILE="$REPO_ROOT/schema/deck.schema.json"
INDEX_FILTER="$SCRIPT_DIR/deck_index.jq"
SYNC_COMMIT_MESSAGE="chore: regenerate deck index"

cd "$REPO_ROOT"

branch="$(git rev-parse --abbrev-ref HEAD)"
if [ "$branch" != "main" ]; then
  echo "error: expected to be on 'main', currently on '$branch'" >&2
  exit 1
fi

if ! git diff --quiet -- "$DECKS_DIR" || ! git diff --cached --quiet -- "$DECKS_DIR"; then
  echo "error: data/decks has uncommitted changes, commit or stash first" >&2
  exit 1
fi

echo "Pulling latest main..."
git pull --ff-only origin main

list_deck_files() {
  find "$DECKS_DIR" -maxdepth 1 -name '*.json' ! -name 'index.json' | sort
}

if [ -z "$(list_deck_files)" ]; then
  echo "error: no deck files found in $DECKS_DIR" >&2
  exit 1
fi

echo "Assigning sourceId to new decks..."
while IFS= read -r deck_file; do
  if [ "$(jq 'has("sourceId")' "$deck_file")" = "false" ]; then
    new_id="$(uuidgen | tr '[:upper:]' '[:lower:]')"
    tmp="$(mktemp)"
    jq --arg id "$new_id" '. + {sourceId: $id}' "$deck_file" > "$tmp"
    mv "$tmp" "$deck_file"
    echo "  $(basename "$deck_file") -> $new_id"
  fi
done < <(list_deck_files)

index_file_for() {
  if [ "$1" -eq 1 ]; then
    echo "$DECKS_DIR/index.json"
  else
    echo "$DECKS_DIR/v$1/index.json"
  fi
}

newest_format_version="$(jq -e '.properties.formatVersion.maximum' "$SCHEMA_FILE")"

echo "Generating indexes up to format $newest_format_version..."
all_decks="$(mktemp)"
while IFS= read -r deck_file; do
  updated_at="$(git log --invert-grep --grep="^${SYNC_COMMIT_MESSAGE}" -1 --format=%cI -- "$deck_file")"
  [ -z "$updated_at" ] && updated_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  jq --arg u "$updated_at" '. + {updatedAt: $u}' "$deck_file"
done < <(list_deck_files) | jq -s '.' > "$all_decks"

for version in $(seq 1 "$newest_format_version"); do
  index_file="$(index_file_for "$version")"
  mkdir -p "$(dirname "$index_file")"
  jq --argjson version "$version" -f "$INDEX_FILTER" "$all_decks" > "$index_file"
  echo "Wrote $(jq length "$index_file") decks to ${index_file#"$REPO_ROOT/"}"
done
rm "$all_decks"

if [ -z "$(git status --porcelain -- "$DECKS_DIR")" ]; then
  echo "Nothing changed."
  exit 0
fi

git add "$DECKS_DIR"
git commit -m "$SYNC_COMMIT_MESSAGE [skip ci]"

echo "Pushing to main..."
git push origin main
echo "Done."
