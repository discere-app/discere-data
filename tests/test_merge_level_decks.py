#!/usr/bin/env python3
# =============================================================================
# test_merge_level_decks.py — tests for scripts/merge_level_decks.py
#
# Checks the merged deck the script writes from synthetic level files: the
# learning settings and the key order, the subdecks, supersedes, validity
# against schema/deck.schema.json, and that the script stops without writing
# a file when an argument is missing or invalid, a level has no sourceId or
# the output exists. The level files are built in a temporary directory, so
# the tests do not depend on the decks in data/decks/.
#
# Runs in CI (.github/workflows/test-scripts.yml) and locally:
#   pip install "jsonschema[format]"
#   python3 -B -m unittest discover -s tests -v
# (-B: the repository ignores no __pycache__, so the tests write none.)
# =============================================================================

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest

from jsonschema import Draft202012Validator, FormatChecker

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SCRIPT = os.path.join(ROOT, "scripts", "merge_level_decks.py")
SCHEMA_FILE = os.path.join(ROOT, "schema", "deck.schema.json")

# The script imports deckbuilder.levels from its own directory, which is on
# the path when it runs as a script, but not when a test loads it.
sys.path.insert(0, os.path.dirname(SCRIPT))
_spec = importlib.util.spec_from_file_location("merge_level_decks", SCRIPT)
merge_level_decks = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(merge_level_decks)

BASE = "testmeer"
SETTINGS_ARGS = {
    "--learning-mode": "family",
    "--name-type": "scientificName",
    "--review-mode": "multipleChoice",
}
SOURCE_IDS = [
    "11111111-1111-4111-8111-111111111111",
    "22222222-2222-4222-8222-222222222222",
    "33333333-3333-4333-8333-333333333333",
]
# "Beta beta" stands in levels 1 and 2 and belongs to level 1.
LEVEL_SPECIES = [
    ["Alpha alpha", "Beta beta"],
    ["Beta beta", "Gamma gamma"],
    ["Delta delta"],
]


def level_deck(n):
    return {
        "name": f"Testmeer - Level {n}",
        "description": f"Beschreibung {n}",
        "speciesNames": LEVEL_SPECIES[n - 1],
        "imageUrl": "https://example.org/cover.jpg",
        "sources": [{"name": "REEF", "url": "https://www.reef.org/"}],
        "sourceId": SOURCE_IDS[n - 1],
    }


class MergeLevelDecksTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.decks_dir = self._tmp.name
        self.out = os.path.join(self.decks_dir, f"{BASE}.json")
        for n in range(1, len(LEVEL_SPECIES) + 1):
            self.write_level(n, level_deck(n))

    def write_level(self, n, deck):
        with open(os.path.join(self.decks_dir, f"{BASE}_level{n}.json"), "w", encoding="utf-8") as f:
            json.dump(deck, f)

    def run_script(self, settings=SETTINGS_ARGS):
        args = [sys.executable, SCRIPT, BASE, "--decks-dir", self.decks_dir]
        for option, value in settings.items():
            args += [option, value]
        return subprocess.run(args, capture_output=True, text=True)

    def merged(self):
        result = self.run_script()
        self.assertEqual(result.returncode, 0, result.stderr)
        with open(self.out, encoding="utf-8") as f:
            return json.load(f)

    def assert_fails_without_output(self, result):
        self.assertNotEqual(result.returncode, 0, "script exited with 0")
        self.assertFalse(os.path.exists(self.out), "script wrote the output file")

    # (a)
    def test_writes_learning_settings_in_key_order(self):
        deck = self.merged()
        self.assertEqual(
            {field: deck.get(field) for field in ("learningMode", "nameType", "reviewMode")},
            {"learningMode": "family", "nameType": "scientificName", "reviewMode": "multipleChoice"},
        )
        self.assertEqual(list(deck), [
            "formatVersion", "name", "description", "imageUrl", "sources",
            "learningMode", "nameType", "reviewMode",
            "speciesNames", "subdecks", "supersedes",
        ])

    # (b)
    def test_missing_setting_stops_without_output(self):
        for option in SETTINGS_ARGS:
            with self.subTest(missing=option):
                # A run of an earlier subtest that wrongly wrote the file
                # must not make this one stop for an existing output.
                if os.path.exists(self.out):
                    os.remove(self.out)
                settings = {k: v for k, v in SETTINGS_ARGS.items() if k != option}
                result = self.run_script(settings)
                self.assert_fails_without_output(result)
                self.assertIn(option, result.stderr)

    # (c)
    def test_invalid_setting_stops_without_output(self):
        result = self.run_script({**SETTINGS_ARGS, "--learning-mode": "order"})
        self.assert_fails_without_output(result)
        self.assertIn("invalid choice: 'order'", result.stderr)

    # (d)
    def test_allowed_values_are_the_schema_enums(self):
        with open(SCHEMA_FILE, encoding="utf-8") as f:
            properties = json.load(f)["properties"]
        for field in ("learningMode", "nameType", "reviewMode"):
            with self.subTest(field=field):
                self.assertEqual(merge_level_decks.allowed_values(field), properties[field]["enum"])

    # (e)
    def test_subdecks_per_level_with_species_in_first_level(self):
        deck = self.merged()
        self.assertEqual(deck["speciesNames"], ["Alpha alpha", "Beta beta", "Gamma gamma", "Delta delta"])
        expected_species = [["Alpha alpha", "Beta beta"], ["Gamma gamma"], ["Delta delta"]]
        self.assertEqual(len(deck["subdecks"]), 3)
        for n, (subdeck, species) in enumerate(zip(deck["subdecks"], expected_species), 1):
            with self.subTest(level=n):
                self.assertEqual(subdeck["id"], f"level-{n}")
                self.assertEqual(subdeck["name"], f"Level {n}")
                self.assertEqual(subdeck.get("translations"), {
                    "de": {"name": f"Level {n}"},
                    "en": {"name": f"Level {n}"},
                    "fr": {"name": f"Niveau {n}"},
                    "es": {"name": f"Nivel {n}"},
                })
                self.assertEqual(subdeck["speciesNames"], species)

    # (f)
    def test_supersedes_the_level_decks(self):
        self.assertEqual(self.merged()["supersedes"], SOURCE_IDS)

    # (g)
    def test_level_without_source_id_stops_without_output(self):
        deck = level_deck(2)
        del deck["sourceId"]
        self.write_level(2, deck)
        result = self.run_script()
        self.assert_fails_without_output(result)
        self.assertIn("ohne sourceId", result.stderr)

    # (h)
    def test_existing_output_stays_unchanged(self):
        with open(self.out, "w", encoding="utf-8") as f:
            f.write("existing\n")
        result = self.run_script()
        self.assertNotEqual(result.returncode, 0, "script exited with 0")
        with open(self.out, encoding="utf-8") as f:
            self.assertEqual(f.read(), "existing\n")

    # (i)
    def test_output_is_valid_against_schema(self):
        with open(SCHEMA_FILE, encoding="utf-8") as f:
            schema = json.load(f)
        errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(self.merged()))
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()
