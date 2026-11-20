# =============================================================================
# reef_csv.py — sighting frequencies from a REEF CSV export
#
# Where REEF has survey data, its sighting frequency (SF%: the share of
# surveys that recorded the species) is the best order for a dive region.
# reef.org does not answer automated queries, so the CSV is exported by hand
# and the recipe names its path.
#
# The format is that of the REEF exports scripts/reef/ reads: some lines of
# preamble, then a header starting with "Rank,", with the columns "Species"
# ("<scientific name>, <further text>" — the part before the first comma)
# and "SF%" (e.g. "42.5%" or "42,5"). A species listed twice keeps its
# higher SF%.
# =============================================================================

import csv
import re

from .sources import SourceResult

BINOMIAL = re.compile(r"^[A-Z][A-Za-z-]+ [a-z][A-Za-z-]+$")


class ReefCsvError(Exception):
    pass


def sighting_frequencies(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        lines = f.readlines()
    header = next((i for i, line in enumerate(lines) if line.startswith("Rank,")), None)
    if header is None:
        raise ReefCsvError(f"{path}: keine Kopfzeile, die mit 'Rank,' beginnt")
    reader = csv.DictReader(lines[header:])
    for column in ("Species", "SF%"):
        if column not in reader.fieldnames:
            raise ReefCsvError(f"{path}: Spalte '{column}' fehlt")

    best, skipped = {}, 0
    for row in reader:
        name = re.sub(r"\s+", " ", (row["Species"] or "").split(",")[0]).strip()
        try:
            sf = float((row["SF%"] or "").replace("%", "").replace(",", ".").strip())
        except ValueError:
            skipped += 1
            continue
        if not BINOMIAL.match(name):
            skipped += 1
            continue
        if sf > best.get(name, -1.0):
            best[name] = sf
    notes = [f"REEF: {len(best)} Arten aus {path}"]
    if skipped:
        notes.append(f"REEF: {skipped} Zeilen ohne Artnamen oder SF% übergangen")
    return SourceResult(sorted(best.items()), notes)
