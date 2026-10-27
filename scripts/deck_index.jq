# =============================================================================
# deck_index.jq — the decks of the catalog index for one format version
#
# Input: the array of all decks. Argument: $version (--argjson version N).
# Output: the decks an app reading format $version gets — every deck of
# format $version or lower, minus those a deck in that same index
# supersedes. A superseded deck thus stays in the indexes of versions below
# its superseding deck's and leaves the rest, and a deck without
# formatVersion (format 1) is in every index.
#
# Used by scripts/sync_index.sh; scripts/validate_decks.py has already
# checked formatVersion, so anything but a whole number is an error here
# rather than read as format 1.
# =============================================================================

def format_version:
  if has("formatVersion") | not then 1
  elif (.formatVersion | type) == "number" and (.formatVersion | floor) == .formatVersion
  then .formatVersion
  else error("\(.name): formatVersion \(.formatVersion | tojson) is not a whole number")
  end;

map(select(format_version <= $version))
| [.[].supersedes // [] | .[]] as $superseded
| map(select(.sourceId | IN($superseded[]) | not))
