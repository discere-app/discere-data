# =============================================================================
# deckbuilder_support.py — shared test fixtures for scripts/deckbuilder/
#
# Not a test module itself: a fetcher that answers from recorded JSON
# instead of the network, and a reference DB built from a few rows with
# just the tables and columns the deckbuilder reads. The tests stay
# offline.
#
# Importing it puts scripts/ on the path. Run the tests with python3 -B: the
# repository ignores no __pycache__.
# =============================================================================

import json
import os
import sqlite3
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
FIXTURES = os.path.join(ROOT, "tests", "fixtures", "deckbuilder")
SCHEMA_DIR = os.path.join(ROOT, "schema")
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from deckbuilder.fetch import build_url  # noqa: E402


def fixture(name):
    with open(os.path.join(FIXTURES, name), encoding="utf-8") as f:
        return json.load(f)


class FakeFetcher:
    """Answers get_json from a dict URL → body (URLs built like the real
    fetcher builds them), or from `answer(base, params)`; records the
    requested URLs and fails on one it has no answer for."""

    def __init__(self, answers=None, answer=None):
        self.answers = answers or {}
        self.answer = answer
        self.requested = []

    def get_json(self, base, params=None):
        url = build_url(base, params or {})
        self.requested.append(url)
        if url in self.answers:
            return self.answers[url]
        if self.answer:
            body = self.answer(base, params or {})
            if body is not None:
                return body
        raise AssertionError(f"no recorded answer for {url}")


SCHEMA = """
CREATE TABLE classes (id TEXT PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE families (id TEXT PRIMARY KEY, name TEXT NOT NULL, "order" TEXT);
CREATE TABLE genera (id TEXT PRIMARY KEY, name TEXT NOT NULL, family TEXT);
CREATE TABLE common_names (
    entity_id TEXT NOT NULL, language TEXT NOT NULL, country TEXT, name TEXT NOT NULL,
    rank INTEGER, is_preferred INTEGER NOT NULL DEFAULT 0);
CREATE TABLE species (
    id TEXT PRIMARY KEY, external_id TEXT NOT NULL, external_source TEXT NOT NULL, name TEXT NOT NULL,
    max_length_cm NUMERIC, depth_min_m NUMERIC, genus TEXT, status TEXT NOT NULL DEFAULT 'active');
CREATE TABLE species_scientific_names (
    species_id TEXT NOT NULL, name TEXT NOT NULL, normalized_name TEXT NOT NULL, source TEXT NOT NULL,
    is_preferred INTEGER NOT NULL DEFAULT 0, name_status TEXT NOT NULL);
CREATE TABLE species_name_lookup (normalized_name TEXT PRIMARY KEY, species_id TEXT NOT NULL);
CREATE TABLE taxonomy_distribution_regions (
    entity_id TEXT NOT NULL, source TEXT NOT NULL, region_scope TEXT NOT NULL, region_key TEXT NOT NULL,
    establishment_status TEXT, presence_status TEXT);
CREATE TABLE orders (id TEXT PRIMARY KEY, external_source TEXT NOT NULL, name TEXT NOT NULL, class TEXT);
"""


def make_refdb(path, species, synonyms=(), occurrences=(), orders=(), families=None, common_names=(), classes=None):
    """A reference DB at `path`.
    species:      (id, "Genus epithet", source, SpecCode, depth_min_m, max_length_cm)
    synonyms:     ("Other name", species id[, name_status]) — also findable by
                  name; the status defaults to "synonym"
    occurrences:  (species id, region_key, establishment_status, presence_status)
    orders:       (order name, external_source)
    families:     {genus name: family name}; the family id is "f:<name>"
    classes:      {family name: class name}, each through an order of its own
    common_names: (entity id, language, name, country, is_preferred, rank)"""
    db = sqlite3.connect(path)
    db.executescript(SCHEMA)
    for sid, name, source, code, depth, length in species:
        genus, epithet = name.split()
        family = (families or {}).get(genus)
        if family:
            class_name = (classes or {}).get(family)
            if class_name:
                db.execute("INSERT OR IGNORE INTO classes VALUES (?, ?)", (f"c:{class_name}", class_name))
                db.execute("INSERT OR IGNORE INTO orders VALUES (?, 'test', ?, ?)",
                           (f"o:{family}", f"{family}ales", f"c:{class_name}"))
            db.execute("INSERT OR IGNORE INTO families VALUES (?, ?, ?)",
                       (f"f:{family}", family, class_name and f"o:{family}"))
        db.execute("INSERT OR IGNORE INTO genera VALUES (?, ?, ?)", (f"g:{genus}", genus, family and f"f:{family}"))
        db.execute("INSERT INTO species VALUES (?, ?, ?, ?, ?, ?, ?, 'active')",
                   (sid, code, source, epithet, length, depth, f"g:{genus}"))
        db.execute("INSERT INTO species_scientific_names VALUES (?, ?, ?, ?, 1, 'valid')", (sid, name, name.lower(), source))
        db.execute("INSERT INTO species_name_lookup VALUES (?, ?)", (name.lower(), sid))
    for name, sid, *status in synonyms:
        db.execute("INSERT INTO species_scientific_names VALUES (?, ?, ?, 'fishbase', 0, ?)",
                   (sid, name, name.lower(), status[0] if status else "synonym"))
        # The first species to carry a name gets it in the lookup, as one
        # name resolves to one species in the app.
        db.execute("INSERT OR IGNORE INTO species_name_lookup VALUES (?, ?)", (name.lower(), sid))
    for sid, key, establishment, presence in occurrences:
        db.execute("INSERT INTO taxonomy_distribution_regions VALUES (?, 'fishbase', 'country', ?, ?, ?)",
                   (sid, key, establishment, presence))
    for row in common_names:
        db.execute("INSERT INTO common_names VALUES (?, ?, ?, ?, ?, ?)",
                   (row[0], row[1], row[3], row[2], row[5], row[4]))
    for n, (name, source) in enumerate(orders):
        db.execute("INSERT INTO orders VALUES (?, ?, ?, NULL)", (f"o:{n}", source, name))
    db.commit()
    db.close()
