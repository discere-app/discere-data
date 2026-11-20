#!/usr/bin/env python3
# =============================================================================
# test_deckbuilder_build.py — tests for a whole deckbuilder run
# (scripts/deckbuilder/build.py)
#
# Runs a recipe for a made-up sea against recorded source answers and a
# reference DB of a few rows, in a temporary directory: the deck it writes
# (levels, highlights, names, validity against schema/deck.schema.json, what
# an existing deck keeps), the report (rejected highlights, unresolved
# names, the guide comparison) and the exit code, and that an invalid
# recipe stops the run without writing anything. No network. Also checks
# every recipe under recipes/ against schema/recipe.schema.json.
#
#   python3 -B -m unittest discover -s tests -v
# =============================================================================

import contextlib
import io
import json
import os
import tempfile
import unittest

from deckbuilder_support import ROOT, SCHEMA_DIR, FakeFetcher, make_refdb
from jsonschema import Draft202012Validator, FormatChecker
from deckbuilder import build, recipe as recipe_module
from deckbuilder.refdb import ReferenceDb

# (id, name, SpecCode, iNat count or None, water flags (fresh, brack, salt))
SPECIES = [
    ("s:1", "Alpha one", "1", 100, (0, 0, 1)),
    ("s:2", "Beta two", "2", 90, (0, 1, 1)),
    ("s:3", "Gamma three", "3", None, (0, 0, 1)),     # iNat knows it as "Gammaold three"
    ("s:4", "Delta four", "4", 70, (0, 0, 1)),
    ("s:5", "Epsilon five", "5", 60, (1, 1, 1)),
    ("s:6", "Zeta six", "6", 50, (1, 0, 0)),          # freshwater only
    ("s:7", "Eta seven", "7", 40, (0, 1, 0)),         # brackish only
    ("s:8", "Theta eight", "8", 30, (0, 0, 0)),       # unknown
    ("s:9", "Iota nine", "9", 3, (0, 0, 1)),          # too few records
    ("s:12", "Mu twelve", "12", 20, (0, 0, 1)),
    ("s:10", "Kappa ten", "10", None, (0, 0, 1)),     # highlight, OBIS only
    ("s:11", "Lambda eleven", "11", None, (0, 0, 1)),  # highlight without evidence
    ("s:13", "Nu thirteen", "13", None, (0, 0, 1)),   # highlight, FishBase distribution
    ("s:14", "Xi fourteen", "14", None, (0, 0, 1)),   # highlight, extirpated there
]
INAT_RESULTS = [(name, count) for _, name, _, count, _ in SPECIES if count is not None]
INAT_RESULTS += [("Gammaold three", 80), ("Nomen nudum", 15)]
GUIDE = ["Alpha one", "Gammaold three", "Epsilon five", "Kappa ten", "Mu twelve", "Omega unknown"]

RECIPE = {
    "deck": {
        "name": "Testmeer",
        "description": "Fische des Testmeers.",
        "translations": {
            "de": {"name": "Testmeer", "description": "Fische des Testmeers."},
            "en": {"name": "Test Sea", "description": "Fishes of the test sea."},
        },
        "learningMode": "family",
        "nameType": "commonName",
        "reviewMode": "flip",
    },
    "order": {"source": "inat"},
    "region": {
        "inat": {"placeId": 1},
        "obis": {"wkt": "POLYGON((0 0, 1 0, 1 1, 0 0))"},
        "fishbase": ["001"],
    },
    "taxa": {"inat": [47178], "obis": [10194]},
    "filters": {"water": "salt", "minCount": 5},
    "levelSizes": [2, 2, 1],
    "highlights": ["Beta two", "Delta four", "Kappa ten", "Lambda eleven", "Nu thirteen", "Xi fourteen",
                   "Fictus name"],
    "guides": [{"name": "Testführer", "path": "guides/test.txt"}],
}


def answer(base, params):
    if "inaturalist" in base:
        return {"total_results": len(INAT_RESULTS),
                "results": [{"count": c, "taxon": {"name": n}} for n, c in INAT_RESULTS]}
    if "obis" in base:
        return {"total": 1, "results": [{"scientificName": "Kappa ten", "taxonRank": "Species", "records": 2}]}
    return None


class BuildTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        tmp = self._tmp.name
        self.decks_dir = os.path.join(tmp, "decks")
        self.recipes_dir = os.path.join(tmp, "recipes")
        os.makedirs(os.path.join(self.recipes_dir, "guides"))
        self.recipe_path = os.path.join(self.recipes_dir, "testmeer.json")
        self.deck_path = os.path.join(self.decks_dir, "testmeer.json")
        self.report_path = os.path.join(self.recipes_dir, "testmeer.report.md")
        self.write_recipe(RECIPE)
        with open(os.path.join(self.recipes_dir, "guides", "test.txt"), "w", encoding="utf-8") as f:
            f.write("# Testführer\n" + "\n".join(GUIDE) + "\n")

        db_path = os.path.join(tmp, "ref.db")
        make_refdb(
            db_path,
            species=[(sid, name, "fishbase", code, None, None) for sid, name, code, _, _ in SPECIES],
            synonyms=[("Gammaold three", "s:3")],
            occurrences=[("s:13", "001", "native", "present"), ("s:14", "001", "extirpated", "absent")],
        )
        self.db = ReferenceDb(db_path)
        self.addCleanup(self.db.close)
        self.water = {("fishbase", code): flags for _, _, code, _, flags in SPECIES}

    def write_recipe(self, recipe):
        with open(self.recipe_path, "w", encoding="utf-8") as f:
            json.dump(recipe, f)

    def run_build(self):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()) as err:
            code = build.run(self.recipe_path, self.decks_dir, FakeFetcher(answer=answer), self.db, self.water)
        self.stderr = err.getvalue()
        return code

    def deck(self):
        with open(self.deck_path, encoding="utf-8") as f:
            return json.load(f)

    def report(self):
        with open(self.report_path, encoding="utf-8") as f:
            return f.read()

    # (a) (c)
    def test_levels(self):
        self.run_build()
        levels = [s["speciesNames"] for s in self.deck()["subdecks"]]
        self.assertEqual(levels, [
            ["Alpha one", "Beta two", "Delta four", "Kappa ten", "Nu thirteen"],
            ["Gamma three", "Epsilon five"],
            ["Theta eight"],
        ])
        self.assertEqual([s["id"] for s in self.deck()["subdecks"]], ["level-1", "level-2", "level-3"])
        self.assertEqual(self.deck()["speciesNames"], [n for level in levels for n in level])

    # (c)
    def test_excluded_candidates_are_reported_with_reason(self):
        self.run_build()
        report = self.report()
        self.assertIn("| *Zeta six* | 50 | Süß | kein Meeresfisch", report)
        self.assertIn("| *Eta seven* | 40 | Brack | kein Meeresfisch", report)
        self.assertIn("| *Iota nine* | 3 | Meer | zu wenige Nachweise", report)

    # (b)
    def test_highlight_without_evidence_stays_out_and_fails_the_run(self):
        code = self.run_build()
        self.assertEqual(code, build.EXIT_HIGHLIGHT_REJECTED)
        names = self.deck()["speciesNames"]
        for name in ("Lambda eleven", "Xi fourteen", "Fictus name"):
            self.assertNotIn(name, names)
        section = self.report().split("## Verworfene Highlights")[1].split("## Deck")[0]
        self.assertIn("*Lambda eleven*: kein Nachweis in der Region", section)
        self.assertIn("*Xi fourteen*: kein Nachweis in der Region", section)
        self.assertIn("*Fictus name*: Name in der Referenz-DB nicht gefunden", section)
        self.assertIn("Lambda eleven", self.stderr)

    def test_without_rejected_highlights_the_run_succeeds(self):
        recipe = json.loads(json.dumps(RECIPE))
        recipe["highlights"] = ["Kappa ten"]
        self.write_recipe(recipe)
        self.assertEqual(self.run_build(), build.EXIT_OK)

    # (d)
    def test_synonym_is_written_as_preferred_name_and_unknown_name_reported(self):
        self.run_build()
        names = self.deck()["speciesNames"]
        self.assertIn("Gamma three", names)
        self.assertNotIn("Gammaold three", names)
        unresolved = self.report().split("## Nicht aufgelöste Namen der Reihenfolge-Quelle")[1]
        self.assertIn("| *Nomen nudum* | 15 |", unresolved)

    # (e)
    def test_existing_deck_keeps_what_the_recipe_does_not_set(self):
        os.makedirs(self.decks_dir)
        existing = {
            "formatVersion": 2,
            "name": "Alter Name",
            "description": "alt",
            "imageUrl": "https://example.org/cover.jpg",
            "createdBy": "Jemand",
            "speciesNames": ["Alpha one", "Old species"],
            "supersedes": ["11111111-1111-4111-8111-111111111111"],
            "sourceId": "22222222-2222-4222-8222-222222222222",
        }
        with open(self.deck_path, "w", encoding="utf-8") as f:
            json.dump(existing, f)
        self.run_build()
        deck = self.deck()
        self.assertEqual(deck["sourceId"], existing["sourceId"])
        self.assertEqual(deck["supersedes"], existing["supersedes"])
        self.assertEqual(deck["imageUrl"], existing["imageUrl"])
        self.assertEqual(deck["createdBy"], existing["createdBy"])
        self.assertEqual(deck["name"], "Testmeer")
        self.assertNotIn("Old species", deck["speciesNames"])
        self.assertIn("- entfallen: 1: *Old species*", self.report())

    # (f)
    def test_deck_is_valid_against_the_schema(self):
        self.run_build()
        with open(os.path.join(SCHEMA_DIR, "deck.schema.json"), encoding="utf-8") as f:
            schema = json.load(f)
        errors = list(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(self.deck()))
        self.assertEqual(errors, [])
        deck = self.deck()
        self.assertEqual(deck["formatVersion"], 2)
        self.assertEqual((deck["learningMode"], deck["nameType"], deck["reviewMode"]),
                         ("family", "commonName", "flip"))
        self.assertEqual([s["name"] for s in deck["sources"]], ["iNaturalist", "OBIS", "FishBase"])

    # (f)
    def test_invalid_recipe_stops_without_writing(self):
        recipe = json.loads(json.dumps(RECIPE))
        del recipe["levelSizes"]
        recipe["filters"]["water"] = "brackish"
        self.write_recipe(recipe)
        code = self.run_build()
        self.assertEqual(code, build.EXIT_STOPPED)
        self.assertIn("levelSizes", self.stderr)
        self.assertIn("brackish", self.stderr)
        self.assertFalse(os.path.exists(self.deck_path))
        self.assertFalse(os.path.exists(self.report_path))

    # (g)
    def test_guide_comparison_both_ways(self):
        self.run_build()
        section = self.report().split("## Abgleich mit Führern")[1].split("## Ausgeschlossene")[0]
        suspects = section.split("**Im Deck, nicht im Führer**")[1].split("**Im Führer und häufig")[0]
        candidates = section.split("**Im Führer und häufig")[1]
        for name in ("Beta two", "Delta four", "Nu thirteen", "Theta eight"):
            self.assertIn(f"*{name}*", suspects)
        for name in ("Alpha one", "Gamma three", "Epsilon five", "Kappa ten"):
            self.assertNotIn(f"*{name}*", suspects)
        self.assertIn("*Mu twelve*", candidates)
        self.assertNotIn("*Alpha one*", candidates)
        self.assertIn("6 Namen, 5 Arten aufgelöst, 1 Namen nicht aufgelöst", section)
        self.assertIn("*Omega unknown*", section)


class RecipesTest(unittest.TestCase):
    def test_every_recipe_is_valid_and_its_files_exist(self):
        recipes_dir = os.path.join(ROOT, "recipes")
        paths = sorted(p for p in os.listdir(recipes_dir) if p.endswith(".json"))
        self.assertTrue(paths, "no recipe found")
        for name in paths:
            with self.subTest(recipe=name):
                loaded = recipe_module.load(os.path.join(recipes_dir, name))
                for guide in loaded.get("guides", []):
                    self.assertTrue(os.path.exists(guide["path"]), guide["path"])


if __name__ == "__main__":
    unittest.main()
