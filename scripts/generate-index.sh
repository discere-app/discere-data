#!/usr/bin/env bash
# Generates data/decks/index.json from all individual deck JSON files.
# Usage: ./scripts/generate-index.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DECKS_DIR="$SCRIPT_DIR/../data/decks"

cd "$DECKS_DIR"
jq -s '.' $(ls -1 *.json | grep -v '^index\.json$' | sort) > index.json
echo "Generated index.json with $(jq length index.json) decks"