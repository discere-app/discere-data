#!/usr/bin/env python3
# =============================================================================
# test_deckbuilder_extra.py — tests for the extra subdecks of a recipe
# (scripts/deckbuilder/extra.py, extraSubdecks in schema/recipe.schema.json)
#
# A made-up reef with fish levels and an invertebrate subdeck, built from
# recorded iNaturalist answers that differ by taxon: the extra subdeck
# follows the levels, the deck's speciesNames is the union, a species on a
# level stays out of the extra subdeck (and cannot be its highlight), the
# subdeck's own filters override the recipe's key by key while the others
# still apply, its highlights count towards its size, its exclusions by
# hand work, and the report has a section of its own. Also the schema
# rules: no level id, inat only, two subdecks with one id stop the run.
# No network.
#
#   python3 -B -m unittest discover -s tests -v
# =============================================================================

import contextlib
import io
import json
import os
import tempfile
import unittest

from deckbuilder_support import FakeFetcher, make_refdb
from deckbuilder import build
from deckbuilder.refdb import ReferenceDb
from deckbuilder.selection import split_extra

FISH_TAXA = "47178,47459"
INVERTEBRATE_TAXA = "47534,47115"

# (id, name, iNat count among the fishes, among the invertebrates, depth_min_m, max_length_cm)
SPECIES = [
    ("s:1", "Alpha one", 100, None, None, 30),
    ("s:2", "Beta two", 90, None, None, 30),
    ("s:3", "Octo pus", 80, 80, None, 50),        # cephalopod: a level species, also a mollusc
    ("s:4", "Coral one", None, 70, None, 20),
    ("s:5", "Crab land", None, 60, None, 10),     # excluded by hand
    ("s:6", "Snail tiny", None, 50, None, 1),     # below the recipe's minimum length
    ("s:7", "Urchin deep", None, 45, 100, 10),    # below the dive depth limit
    ("s:8", "Sponge five", None, 30, None, 20),
    ("s:9", "Star six", None, 20, None, 20),
    ("s:10", "Worm few", None, 3, None, 20),      # too few records
    ("s:11", "Clam giant", None, 2, None, 100),   # highlight of the extra subdeck
]

EXTRA = {
    "id": "invertebrates",
    "name": "Wirbellose & Korallen",
    "translations": {"de": {"name": "Wirbellose & Korallen"}, "en": {"name": "Invertebrates & Corals"}},
    "taxa": {"inat": [47534, 47115], "obis": [1267, 51]},
    "size": 3,
    "filters": {"minLengthCm": 0},
    "highlights": [{"name": "Clam giant", "reason": "Größte Muschel."}],
    "exclude": [{"name": "Crab land", "reason": "Lebt an Land."}],
}

RECIPE = {
    "deck": {
        "name": "Testriff",
        "description": "Tiere des Testriffs.",
        "translations": {"en": {"name": "Test Reef", "description": "Animals of the test reef."}},
        "learningMode": "family",
        "nameType": "commonName",
        "reviewMode": "flip",
    },
    "order": {"source": "inat"},
    "region": {
        "inat": {"placeIds": [1]},
        "obis": [{"name": "Testbucht", "wkt": "POLYGON((0 0, 1 0, 1 1, 0 0))"}],
    },
    "taxa": {"inat": [47178, 47459], "obis": [10194, 11707]},
    "filters": {"water": "salt", "minCount": 5, "diveDepthLimitM": 40, "minLengthCm": 4},
    "levelSizes": [2, 1],
    "extraSubdecks": [EXTRA],
}


def answer(base, params):
    if base.startswith("https://api.inaturalist.org/v1/places/"):
        return {"results": [{"id": 1, "display_name": "Ort 1"}]}
    if base.endswith("/observers"):
        return {"total_results": 5, "results": [{"observation_count": 1}]}
    if "inaturalist" in base and "term_id" in params:
        # (alive, dead) per name
        annotated = {"Coral one": (1, 9), "Snail tiny": (8, 2)} if params["taxon_id"] == INVERTEBRATE_TAXA else {}
        column = {18: 0, 19: 1}[int(params["term_value_id"])]
        return {"total_results": len(annotated),
                "results": [{"count": a[column], "taxon": {"name": n}} for n, a in annotated.items()]}
    if "inaturalist" in base:
        column = {FISH_TAXA: 2, INVERTEBRATE_TAXA: 3}[params["taxon_id"]]
        results = [{"count": row[column], "taxon": {"name": row[1]}} for row in SPECIES if row[column] is not None]
        return {"total_results": len(results), "results": results}
    if "obis" in base:
        return {"total": 0, "results": []}
    return None


class ExtraSubdeckTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        tmp = self._tmp.name
        self.decks_dir = os.path.join(tmp, "decks")
        self.recipe_path = os.path.join(tmp, "testriff.json")
        self.deck_path = os.path.join(self.decks_dir, "testriff.json")
        self.report_path = os.path.join(tmp, "testriff.report.md")
        self.write_recipe(RECIPE)
        db_path = os.path.join(tmp, "ref.db")
        make_refdb(
            db_path,
            species=[(sid, name, "sealifebase", sid[2:], depth, length) for sid, name, _, _, depth, length in SPECIES],
            families={"Coral": "Coralidae", "Snail": "Snailidae"},
            classes={"Coralidae": "Anthozoa", "Snailidae": "Gastropoda"},
        )
        self.db = ReferenceDb(db_path)
        self.addCleanup(self.db.close)
        self.water = {("sealifebase", sid[2:]): (0, 0, 1) for sid, *_ in SPECIES}

    def write_recipe(self, recipe):
        with open(self.recipe_path, "w", encoding="utf-8") as f:
            json.dump(recipe, f)

    def with_extra(self, **changes):
        recipe = json.loads(json.dumps(RECIPE))
        recipe["extraSubdecks"][0].update(changes)
        for key in [k for k, v in changes.items() if v is None]:
            del recipe["extraSubdecks"][0][key]
        return recipe

    def run_build(self):
        with contextlib.redirect_stdout(io.StringIO()) as out, contextlib.redirect_stderr(io.StringIO()) as err:
            code = build.run(self.recipe_path, self.decks_dir, FakeFetcher(answer=answer), self.db, self.water)
        self.stdout, self.stderr = out.getvalue(), err.getvalue()
        return code

    def deck(self):
        with open(self.deck_path, encoding="utf-8") as f:
            return json.load(f)

    def subdeck(self, subdeck_id):
        return next(s for s in self.deck()["subdecks"] if s["id"] == subdeck_id)

    def report(self):
        with open(self.report_path, encoding="utf-8") as f:
            return f.read()

    def test_extra_subdeck_follows_the_levels(self):
        self.assertEqual(self.run_build(), build.EXIT_OK, self.stderr)
        deck = self.deck()
        self.assertEqual([s["id"] for s in deck["subdecks"]], ["level-1", "level-2", "invertebrates"])
        extra = self.subdeck("invertebrates")
        self.assertEqual(extra["name"], "Wirbellose & Korallen")
        self.assertEqual(extra["translations"]["en"], {"name": "Invertebrates & Corals"})
        self.assertEqual(extra["speciesNames"], ["Coral one", "Snail tiny", "Clam giant"])
        self.assertEqual(deck["speciesNames"], [n for s in deck["subdecks"] for n in s["speciesNames"]])

    def test_no_species_is_in_two_subdecks(self):
        self.run_build()
        self.assertEqual(self.subdeck("level-2")["speciesNames"], ["Octo pus"])
        self.assertNotIn("Octo pus", self.subdeck("invertebrates")["speciesNames"])
        names = self.deck()["speciesNames"]
        self.assertEqual(len(names), len(set(names)))
        self.assertIn("| *Octo pus* | 80 | Meer | schon in einem anderen Subdeck (level-2) |", self.report())

    def test_a_level_species_cannot_be_a_highlight_of_the_extra_subdeck(self):
        self.write_recipe(self.with_extra(highlights=[{"name": "Octo pus", "reason": "Klug."}]))
        self.assertEqual(self.run_build(), build.EXIT_HIGHLIGHT_REJECTED)
        self.assertEqual(self.subdeck("level-2")["speciesNames"], ["Octo pus"])
        self.assertNotIn("Octo pus", self.subdeck("invertebrates")["speciesNames"])
        self.assertIn("schon im Subdeck level-2", self.stderr)

    def test_own_filters_override_the_recipe_and_the_rest_still_applies(self):
        self.run_build()
        extra = self.subdeck("invertebrates")["speciesNames"]
        self.assertIn("Snail tiny", extra)
        self.assertNotIn("Urchin deep", extra)
        self.assertIn("| *Urchin deep* | 45 | Meer | nur tiefer als die Tauchgrenze (erst ab 100 m) |", self.report())

    def test_without_own_filters_the_recipe_filters_apply(self):
        self.write_recipe(self.with_extra(filters=None))
        self.run_build()
        self.assertEqual(self.subdeck("invertebrates")["speciesNames"], ["Coral one", "Sponge five", "Clam giant"])
        self.assertIn("| *Snail tiny* | 50 | Meer | zu klein (höchstens 1 cm) |", self.report())

    def test_exclusion_by_hand_and_highlight_count_towards_the_size(self):
        self.run_build()
        extra = self.subdeck("invertebrates")["speciesNames"]
        self.assertNotIn("Crab land", extra)
        self.assertEqual(len(extra), EXTRA["size"])
        section = self.report().split("## Subdeck `invertebrates` (3)")[1]
        self.assertIn("| *Crab land* | 60 | Lebt an Land. |", section)
        self.assertIn("| *Clam giant* | Größte Muschel. |", section)

    def test_warnings_of_the_extra_subdeck_join_the_deck_list(self):
        self.run_build()
        found = self.report().split("## Zu entscheiden")[1].split("## Verworfene Highlights")[0]
        self.assertIn("| *Coral one* | invertebrates | tot beobachtet | 9 von 10", found)
        self.assertNotIn("*Snail tiny*", found)

    def test_report_has_a_section_with_classes_and_boundary(self):
        self.run_build()
        section = self.report().split("## Subdeck `invertebrates` (3)")[1]
        self.assertIn("### Arten", section)
        self.assertIn("| Anthozoa |", section)
        boundary = section.split("### Grenzfälle")[1].split("### Ausgeschlossene")[0]
        self.assertIn("*Sponge five*", boundary.split("**Grenze**")[1])
        self.assertIn("*Snail tiny*", boundary.split("**Grenze**")[0])
        self.assertNotIn("Abgleich", section)

    def test_a_smaller_pool_gives_a_smaller_subdeck(self):
        self.write_recipe(self.with_extra(size=40))
        self.run_build()
        self.assertEqual(self.subdeck("invertebrates")["speciesNames"],
                         ["Coral one", "Snail tiny", "Sponge five", "Star six", "Clam giant"])

    def test_two_subdecks_with_one_id_stop_the_run(self):
        recipe = json.loads(json.dumps(RECIPE))
        recipe["extraSubdecks"].append(dict(EXTRA))
        self.write_recipe(recipe)
        self.assertEqual(self.run_build(), build.EXIT_STOPPED)
        self.assertIn("derselben id", self.stderr)
        self.assertFalse(os.path.exists(self.deck_path))

    def test_schema_rejects_level_id_and_other_order_sources(self):
        self.write_recipe(self.with_extra(id="level-3"))
        self.assertEqual(self.run_build(), build.EXIT_STOPPED)
        self.assertIn("level-3", self.stderr)
        recipe = json.loads(json.dumps(RECIPE))
        recipe["order"] = {"source": "gbif"}
        recipe["region"]["gbif"] = {"countries": ["XX"]}
        recipe["taxa"]["gbif"] = {"phylumKey": 44}
        self.write_recipe(recipe)
        self.assertEqual(self.run_build(), build.EXIT_STOPPED)
        self.assertIn("order/source: 'inat' was expected", self.stderr)


class SplitExtraTest(unittest.TestCase):
    def test_highlights_count_towards_the_size(self):
        levels, sequence, cuts = split_extra(["a", "b", "c", "d"], ["x"], 3)
        self.assertEqual(levels, [["a", "b", "x"]])
        self.assertEqual((sequence, cuts), (["a", "b", "c", "d"], [2]))

    def test_a_highlight_among_the_most_frequent_counts_as_well(self):
        levels, sequence, cuts = split_extra(["a", "b", "c", "d"], ["b", "x"], 3)
        self.assertEqual(levels, [["a", "b", "x"]])
        self.assertEqual((sequence, cuts), (["a", "c", "d"], [1]))

    def test_a_highlight_among_the_ranked_keeps_its_place(self):
        levels, _, _ = split_extra(["a", "b", "c", "d"], ["c"], 2)
        self.assertEqual(levels, [["a", "c"]])


if __name__ == "__main__":
    unittest.main()
