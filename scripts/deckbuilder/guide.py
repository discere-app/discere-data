# =============================================================================
# guide.py — the species list of a field guide
#
# A guide confirms that a species occurs in the region, but says nothing
# about how often a diver meets it (scientific guides list deep-sea species
# and vagrants too). The deckbuilder therefore never filters by it: it
# counts as evidence for a highlight and is compared with the deck in the
# report, both ways.
#
# Format: a text file, one scientific name per line; blank lines and lines
# starting with "#" are ignored, so the file can say where it comes from.
# Lists live under recipes/guides/.
# =============================================================================


def read_names(path):
    names = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                names.append(" ".join(line.split()))
    return names
