#!/usr/bin/env bash
# =============================================================================
# sync_index.sh — regenerate and publish data/decks/index.json
#
# Runs automatically via .github/workflows/sync-deck-index.yml on every push
# to main that touches data/decks/*.json (i.e. after a deck PR is merged),
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
#   4. Combines all deck files into data/decks/index.json (the app fetches
#      this instead of listing + fetching every deck file individually).
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
INDEX_FILE="$DECKS_DIR/index.json"
SYNC_COMMIT_MESSAGE="chore: regenerate deck index"

cd "$REPO_ROOT"

if [ -n "${GITHUB_ACTIONS:-}" ]; then
  git config user.name "github-actions[bot]"
  git config user.email "github-actions[bot]@users.noreply.github.com"
fi

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

echo "Generating index.json..."
while IFS= read -r deck_file; do
  updated_at="$(git log --invert-grep --grep="^${SYNC_COMMIT_MESSAGE}" -1 --format=%cI -- "$deck_file")"
  [ -z "$updated_at" ] && updated_at="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  jq --arg u "$updated_at" '. + {updatedAt: $u}' "$deck_file"
done < <(list_deck_files) | jq -s '.' > "$INDEX_FILE"

echo "Wrote $(jq length "$INDEX_FILE") decks to data/decks/index.json"

if [ -z "$(git status --porcelain -- "$DECKS_DIR")" ]; then
  echo "Nothing changed."
  exit 0
fi

git add "$DECKS_DIR"
git commit -m "$SYNC_COMMIT_MESSAGE [skip ci]"

echo "Pushing to main..."
git push origin main
echo "Done."
