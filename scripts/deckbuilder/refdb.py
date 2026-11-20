# =============================================================================
# refdb.py — the app's reference database: download, name resolution, facts
#
# A deck names its species by scientific name, and the app resolves each
# name against its reference database (discere_reference.db): it cuts the
# name to genus and epithet, lowercases it and looks it up in
# species_name_lookup, which holds every accepted name and synonym. The
# deckbuilder resolves the same way against the same database, so a name it
# writes is a name the app finds, and two names the app takes for one species
# count as one species here too.
#
# The database is not part of this repository. manifest.json under
# data/reference-db/ lists the newest release per schema version; the
# deckbuilder takes the newest release whose schema it reads
# (SUPPORTED_SCHEMAS), checks its sha256, unpacks it and keeps it under
# ~/.cache/discere-deckbuilder/refdb/v<version>/. A later run downloads only
# when the manifest names a newer version. Without network it falls back to
# the newest copy in the cache. --reference-db uses a given file instead.
#
# What the deckbuilder reads is the same in schema 1 and 2: the tables
# species_name_lookup, species, genera, species_scientific_names, orders and
# taxonomy_distribution_regions and the columns used below. The entity IDs
# differ in shape ("discere:fishbase_species:1161" in schema 1,
# "discere:species:1" in schema 2), so nothing here reads meaning into an ID;
# where the origin matters, external_source says it.
# =============================================================================

import gzip
import hashlib
import json
import os
import shutil
import sqlite3
import sys
import urllib.request
from dataclasses import dataclass

from .fetch import USER_AGENT

MANIFEST_URL = "https://raw.githubusercontent.com/discere-app/discere-data/main/data/reference-db/manifest.json"
SUPPORTED_SCHEMAS = (1, 2)
DB_FILE = "discere_reference.db"

# SQLite allows 999 parameters per statement in older builds.
CHUNK = 500


def normalize_name(name):
    """Genus and epithet in lowercase, as the app looks a name up; "" for a
    name of fewer than two words."""
    parts = name.split()
    if len(parts) < 2:
        return ""
    return f"{parts[0].lower()} {parts[1].lower()}"


def newest_release(manifest):
    """The newest release of a supported schema version, as (schema,
    release); manifests without "schemas" list one schema-1 release at the
    top level."""
    schemas = manifest.get("schemas") or {"1": manifest}
    readable = [(int(s), r) for s, r in schemas.items() if int(s) in SUPPORTED_SCHEMAS]
    if not readable:
        raise RuntimeError(f"das Manifest bietet kein Schema, das das Werkzeug liest ({SUPPORTED_SCHEMAS})")
    return max(readable, key=lambda item: item[0])


def _cached_versions(refdb_dir):
    if not os.path.isdir(refdb_dir):
        return []
    found = []
    for entry in os.listdir(refdb_dir):
        if entry.startswith("v") and entry[1:].isdigit() and os.path.exists(os.path.join(refdb_dir, entry, DB_FILE)):
            found.append(int(entry[1:]))
    return sorted(found)


def _download_release(release, target):
    os.makedirs(os.path.dirname(target), exist_ok=True)
    packed = f"{target}.gz.part"
    unpacked = f"{target}.part"
    digest = hashlib.sha256()
    print(f"Lade Referenz-DB v{release['version']} ({release.get('compressedSizeBytes', 0) // 1_000_000} MB) …")
    request = urllib.request.Request(release["url"], headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=120) as response, open(packed, "wb") as out:
        while chunk := response.read(1 << 20):
            digest.update(chunk)
            out.write(chunk)
    if digest.hexdigest() != release["sha256"]:
        os.remove(packed)
        raise RuntimeError(f"sha256 der Referenz-DB v{release['version']} stimmt nicht mit dem Manifest überein")
    with gzip.open(packed, "rb") as src, open(unpacked, "wb") as dst:
        shutil.copyfileobj(src, dst, 1 << 20)
    os.remove(packed)
    os.replace(unpacked, target)


def ensure_reference_db(cache_dir):
    """Path to the newest supported reference DB, downloaded if needed."""
    refdb_dir = os.path.join(cache_dir, "refdb")
    try:
        request = urllib.request.Request(MANIFEST_URL, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(request, timeout=30) as response:
            manifest = json.load(response)
    except OSError as e:
        cached = _cached_versions(refdb_dir)
        if not cached:
            raise RuntimeError(f"Manifest der Referenz-DB nicht erreichbar ({e}) und keine Kopie im Cache") from e
        print(f"[WARN] Manifest der Referenz-DB nicht erreichbar ({e}); nehme die Kopie v{cached[-1]} aus dem Cache",
              file=sys.stderr)
        return os.path.join(refdb_dir, f"v{cached[-1]}", DB_FILE)
    schema, release = newest_release(manifest)
    target = os.path.join(refdb_dir, f"v{release['version']}", DB_FILE)
    if not os.path.exists(target):
        _download_release(release, target)
    print(f"Referenz-DB: v{release['version']} (Schema {schema}), {target}")
    return target


@dataclass(frozen=True)
class SpeciesFacts:
    id: str
    # The species' preferred scientific name, and whether the app resolves
    # it back to this species; only then can a deck name the species by it.
    preferred_name: str
    preferred_resolves: bool
    source: str           # "fishbase" or "sealifebase"
    external_id: str      # SpecCode in that source
    status: str
    depth_min_m: float
    max_length_cm: float


@dataclass(frozen=True)
class Occurrence:
    source: str
    region_key: str
    establishment_status: str
    presence_status: str

    @property
    def is_evidence(self):
        """Whether this entry says the species occurs there. An entry with
        presence "absent" records the opposite: extirpated, a
        misidentification, an error or a failed introduction."""
        return (self.presence_status or "").lower() != "absent"


# The preferred scientific name as the app shows it: genus and epithet, or
# for a species without a genus the preferred name of its own source first.
_PREFERRED_NAME_SQL = """
COALESCE(
  g.name || ' ' || s.name,
  (SELECT n.name FROM species_scientific_names n
   WHERE n.species_id = s.id AND n.is_preferred = 1 AND n.source = s.external_source LIMIT 1),
  (SELECT n.name FROM species_scientific_names n
   WHERE n.species_id = s.id AND n.is_preferred = 1 ORDER BY n.source, n.name LIMIT 1),
  s.name)
"""


def _chunks(items):
    items = list(items)
    for i in range(0, len(items), CHUNK):
        yield items[i:i + CHUNK]


class ReferenceDb:
    def __init__(self, path):
        self.path = path
        self._db = sqlite3.connect(f"file:{path}?mode=ro", uri=True)

    def close(self):
        self._db.close()

    def lookup(self, normalized_names):
        """normalized name → species id, for the names the DB knows."""
        found = {}
        for chunk in _chunks(set(normalized_names)):
            marks = ",".join("?" * len(chunk))
            rows = self._db.execute(
                f"SELECT normalized_name, species_id FROM species_name_lookup WHERE normalized_name IN ({marks})",
                chunk,
            )
            found.update(rows)
        return found

    def resolve(self, names):
        """name → species id or None, resolved as the app does."""
        normalized = {name: normalize_name(name) for name in names}
        found = self.lookup(n for n in normalized.values() if n)
        return {name: found.get(n) for name, n in normalized.items()}

    def species(self, ids):
        """species id → SpeciesFacts."""
        facts = {}
        for chunk in _chunks(set(ids)):
            marks = ",".join("?" * len(chunk))
            rows = self._db.execute(
                f"""SELECT s.id, {_PREFERRED_NAME_SQL}, s.external_source, s.external_id, s.status,
                           s.depth_min_m, s.max_length_cm
                    FROM species s LEFT JOIN genera g ON g.id = s.genus
                    WHERE s.id IN ({marks})""",
                chunk,
            ).fetchall()
            back = self.lookup(normalize_name(row[1]) for row in rows)
            for sid, name, source, external_id, status, depth_min, length in rows:
                facts[sid] = SpeciesFacts(
                    id=sid,
                    preferred_name=name,
                    preferred_resolves=back.get(normalize_name(name)) == sid,
                    source=source,
                    external_id=str(external_id),
                    status=status,
                    depth_min_m=float(depth_min) if depth_min is not None else None,
                    max_length_cm=float(length) if length is not None else None,
                )
        return facts

    def occurrences(self, ids, region_keys):
        """species id → [Occurrence] in the given FishBase/SeaLifeBase
        region keys (country or subregion, e.g. "756" or "840:US-FL")."""
        result = {}
        keys = list(region_keys)
        if not keys:
            return result
        key_marks = ",".join("?" * len(keys))
        for chunk in _chunks(set(ids)):
            marks = ",".join("?" * len(chunk))
            rows = self._db.execute(
                f"""SELECT entity_id, source, region_key, establishment_status, presence_status
                    FROM taxonomy_distribution_regions
                    WHERE entity_id IN ({marks}) AND region_key IN ({key_marks})
                    ORDER BY entity_id, region_key, source""",
                chunk + keys,
            )
            for sid, source, key, establishment, presence in rows:
                result.setdefault(sid, []).append(Occurrence(source, key, establishment, presence))
        return result

    def fishbase_order_names(self):
        """Names of the orders FishBase describes, i.e. the fish orders."""
        rows = self._db.execute("SELECT name FROM orders WHERE external_source = 'fishbase'")
        return {name for (name,) in rows}
