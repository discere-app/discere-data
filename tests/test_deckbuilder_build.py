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
# recipe stops the run without writing anything; the mapping of iNaturalist
# names (recipes/inat_names.json) and the exclusions by hand. No network.
# Also checks every recipe under recipes/ against schema/recipe.schema.json
# and recipes/inat_names.json against its schema.
#
#   python3 -B -m unittest discover -s tests -v
# =============================================================================

import contextlib
import io
import json
import os
import tempfile
import unittest
from urllib.parse import parse_qs, urlsplit

from deckbuilder_support import ROOT, SCHEMA_DIR, FakeFetcher, make_refdb
from jsonschema import Draft202012Validator, FormatChecker
from deckbuilder import build, inat_names, recipe as recipe_module
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
        "inat": {"placeIds": [1, 2]},
        "obis": [{"name": "Testbucht", "wkt": "POLYGON((0 0, 1 0, 1 1, 0 0))"}],
        "fishbase": ["001"],
    },
    "taxa": {"inat": [47178], "obis": [10194]},
    "filters": {"water": "salt", "minCount": 5},
    "levelSizes": [2, 2, 1],
    "highlights": [
        {"name": n, "reason": f"Grund für {n}."}
        for n in ("Beta two", "Delta four", "Kappa ten", "Lambda eleven", "Nu thirteen", "Xi fourteen", "Fictus name")
    ],
    "guides": [{"name": "Testführer", "path": "guides/test.txt"}],
}


TAXON_IDS = {name: 1000 + n for n, (name, _) in enumerate(INAT_RESULTS)}
# Annotation Alive or Dead: (annotated, dead) per iNaturalist name.
ANNOTATIONS = {"Alpha one": (10, 9), "Beta two": (10, 7), "Delta four": (4, 4)}
# Observers: (observers, [observations of the most active]) per taxon id.
OBSERVERS = {TAXON_IDS["Alpha one"]: (3, [60, 20, 20]), TAXON_IDS["Beta two"]: (30, [10, 5, 5])}


def species_counts_body(counts):
    return {"total_results": len(counts),
            "results": [{"count": c, "taxon": {"name": n, "id": TAXON_IDS.get(n, 1)}} for n, c in counts]}


def answer(base, params):
    if base.startswith("https://api.inaturalist.org/v1/places/"):
        ids = base.rsplit("/", 1)[1].split(",")
        return {"results": [{"id": int(i), "display_name": f"Ort {i}"} for i in ids]}
    if base.endswith("/observers"):
        observers, top = OBSERVERS.get(int(str(params["taxon_id"]).split(",")[0]), (1, [1]))
        return {"total_results": observers,
                "results": [{"observation_count": n} for n in top[:params["per_page"]]]}
    if "inaturalist" in base and "term_id" in params:
        column = 1 if "term_value_id" in params else 0
        return species_counts_body([(n, a[column]) for n, a in ANNOTATIONS.items()])
    if "inaturalist" in base:
        return species_counts_body(INAT_RESULTS)
    if "obis" in base and "datasetid" in params:
        return {"total": 1, "results": [{"scientificName": "Alpha one", "taxonRank": "Species", "records": 4}]}
    if "obis" in base:
        return {"total": 2, "results": [{"scientificName": "Kappa ten", "taxonRank": "Species", "records": 2},
                                        {"scientificName": "Alpha one", "taxonRank": "Species", "records": 4}]}
    return None


def query(url):
    return parse_qs(urlsplit(url).query)


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
            synonyms=[
                ("Gammaold three", "s:3"), ("Delta old", "s:4"), ("Delta old", "s:5"),
                ("Alpha one", "s:2", "misapplied name"), ("Beta vague", "s:1", "ambiguous synonym"),
                ("Beta vague", "s:2", "ambiguous synonym"),
            ],
            occurrences=[
                ("s:13", "001", "native", "present"), ("s:14", "001", "extirpated", "absent"),
                ("s:1", "001", "native", "present"), ("s:3", "001", "endemic", "present"),
            ],
            families={"Alpha": "Alphidae", "Beta": "Alphidae", "Gamma": "Gammidae"},
            common_names=[
                ("s:1", "de", "Alphafisch", None, 1, 1), ("s:1", "en", "Alpha fish", None, 1, 1),
                ("s:1", "en", "Regional alpha", "001", 1, 1),
                ("s:2", "en", "alpha fish", None, 1, 1),
                ("s:4", "de", "Deltafisch", None, 0, 2), ("s:4", "de", "Bester Deltafisch", None, 1, 1),
                ("f:Alphidae", "en", "Alpha fishes", None, 1, 1),
                ("f:Gammidae", "de", "Gammafische", None, 1, 1), ("f:Gammidae", "en", "Gamma fishes", None, 1, 1),
            ],
        )
        self.db = ReferenceDb(db_path)
        self.addCleanup(self.db.close)
        self.water = {("fishbase", code): flags for _, _, code, _, flags in SPECIES}

    def write_recipe(self, recipe):
        with open(self.recipe_path, "w", encoding="utf-8") as f:
            json.dump(recipe, f)

    def run_build(self, name_map=()):
        self.fetcher = FakeFetcher(answer=answer)
        with contextlib.redirect_stdout(io.StringIO()) as out, contextlib.redirect_stderr(io.StringIO()) as err:
            code = build.run(self.recipe_path, self.decks_dir, self.fetcher, self.db, self.water, (), name_map)
        self.stdout = out.getvalue()
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
            ["Gammaold three", "Epsilon five"],
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
        recipe["highlights"] = [{"name": "Kappa ten", "reason": "Nur bei OBIS."}]
        self.write_recipe(recipe)
        self.assertEqual(self.run_build(), build.EXIT_OK)

    # (d)
    def test_regional_name_is_written_and_unknown_name_reported(self):
        # iNaturalist counts s:3 as "Gammaold three", which the reference DB
        # knows as a synonym of Gamma three: the deck keeps the region's name.
        self.run_build()
        names = self.deck()["speciesNames"]
        self.assertIn("Gammaold three", names)
        self.assertNotIn("Gamma three", names)
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

    def test_highlights_are_listed_with_their_reason(self):
        self.run_build()
        section = self.report().split("## Highlights")[1].split("## Prüfung")[0]
        self.assertIn("| *Kappa ten* | Grund für Kappa ten. | – | OBIS, Führer | Level 1 |", section)
        self.assertIn("| *Lambda eleven* | Grund für Lambda eleven. | – | keine | verworfen: kein Nachweis", section)
        self.assertIn("| *Fictus name* | Grund für Fictus name. | – | – | verworfen: Name in der Referenz-DB", section)

    def checks(self):
        self.run_build()
        return self.report().split("## Prüfung")[1].split("## Deck")[0]

    def test_two_independent_sources(self):
        section = self.checks()
        # Deck: Alpha Beta Delta Kappa Nu | Gamma Epsilon | Theta; only Alpha
        # and Gamma have iNaturalist and the distribution.
        self.assertIn("(Reihenfolge-Quelle und OBIS ohne iNaturalist oder Verbreitung): 2/8 (25 %)", section)
        single = section.split("**Arten ohne zweite, unabhängige Quelle:**")[1].split("**Eine Art")[0]
        self.assertIn("- *Beta two*: Reihenfolge-Quelle\n", single)
        self.assertIn("- *Kappa ten*: OBIS, Führer\n", single)
        self.assertIn("- *Nu thirteen*: Verbreitung\n", single)
        self.assertNotIn("*Alpha one*", single)
        self.assertNotIn("*Gammaold three*", single)

    def test_endemics(self):
        self.assertIn("laut FishBase/SeaLifeBase: 1: *Gammaold three*", self.checks())

    def test_common_names_as_the_app_picks_them(self):
        section = self.checks()
        self.assertIn("Arten ohne Volksnamen `de` in der Referenz-DB: 6/8 (75 %)", section)
        self.assertIn("Arten ohne Volksnamen `en` in der Referenz-DB: 6/8 (75 %)", section)
        self.assertIn("Familien ohne Volksnamen `de`: 1/2 (50 %): *Alphidae*", section)
        self.assertIn("Familien ohne Volksnamen `en`: 0/2 (0 %)", section)

    def test_one_species_under_two_entries(self):
        section = self.checks().split("**Eine Art unter zwei Einträgen?**")[1]
        self.assertIn("gleicher Volksname `en` „Alpha fish“: *Alpha one*, *Beta two*", section)
        self.assertIn("gemeinsamer wissenschaftlicher Name *delta old*: *Delta four*, *Epsilon five*", section)
        self.assertNotIn("Regional alpha", section)
        # A name misapplied to a species, or a synonym of several, does not
        # make two species one.
        self.assertNotIn("*alpha one*", section)
        self.assertNotIn("*beta vague*", section)

    def test_image_credit_in_the_report(self):
        recipe = json.loads(json.dumps(RECIPE))
        recipe["deck"]["imageUrl"] = "https://upload.wikimedia.org/x/330px-Reef.jpg"
        recipe["imageCredit"] = {"author": "Jemand", "license": "CC BY-SA 4.0",
                                 "page": "https://commons.wikimedia.org/wiki/File:Reef.jpg"}
        self.write_recipe(recipe)
        self.run_build()
        self.assertIn("- Bild: https://upload.wikimedia.org/x/330px-Reef.jpg — Jemand, CC BY-SA 4.0, "
                      "https://commons.wikimedia.org/wiki/File:Reef.jpg", self.report())
        self.assertEqual(self.deck()["imageUrl"], "https://upload.wikimedia.org/x/330px-Reef.jpg")

    def levels(self):
        return [s["speciesNames"] for s in self.deck()["subdecks"]]

    MAPPING = [{"inat": "Nomen nudum", "referenceDb": "Mu twelve", "change": "swap",
                "reason": "Neuer Name derselben Art.", "evidence": "https://www.inaturalist.org/taxon_changes/1"}]

    def test_inat_name_mapping_adds_the_counts(self):
        self.run_build(self.MAPPING)
        # Mu twelve: 20 under its own name and 15 as "Nomen nudum"; 35 puts
        # it ahead of Theta eight (30) onto level 3.
        self.assertEqual(self.levels()[2], ["Mu twelve"])
        report = self.report()
        self.assertIn("| *Nomen nudum* | *Mu twelve* | 15 | Umbenennung | "
                      "https://www.inaturalist.org/taxon_changes/1 |", report)
        self.assertNotIn("*Nomen nudum* | 15 |", report.split("## Nicht aufgelöste Namen")[1])

    def test_without_mapping_the_name_stays_unresolved(self):
        self.run_build()
        self.assertEqual(self.levels()[2], ["Theta eight"])
        self.assertIn("| *Nomen nudum* | 15 |", self.report().split("## Nicht aufgelöste Namen")[1])
        self.assertIn("## iNaturalist-Namen zugeordnet\n\nKeine", self.report())

    def test_exclusion_by_hand(self):
        recipe = json.loads(json.dumps(RECIPE))
        recipe["exclude"] = [
            {"name": "Theta eight", "reason": "Lebt nur im Mangrovenschlamm."},
            {"name": "Zeta six", "reason": "Süßwasser."},
            {"name": "Fictus name", "reason": "Gibt es nicht."},
        ]
        self.write_recipe(recipe)
        self.run_build()
        self.assertEqual(self.levels()[2], ["Mu twelve"])
        section = self.report().split("## Von Hand ausgeschlossen")[1].split("\n## ")[0]
        self.assertIn("| *Theta eight* | 30 | Lebt nur im Mangrovenschlamm. |", section)
        self.assertIn("- *Zeta six*: schon ausgeschlossen: kein Meeresfisch", section)
        self.assertIn("- *Fictus name*: Name in der Referenz-DB nicht gefunden", section)
        self.assertIn("  - von Hand ausgeschlossen: 1", self.report())
        self.assertIn("[WARN] Ausschluss Zeta six wirkt nicht", self.stdout)

    def test_a_highlight_cannot_be_excluded(self):
        recipe = json.loads(json.dumps(RECIPE))
        recipe["exclude"] = [{"name": "Gammaold three", "reason": "x"}]
        recipe["highlights"] = [{"name": "Gamma three", "reason": "y"}]
        self.write_recipe(recipe)
        self.assertEqual(self.run_build(), build.EXIT_STOPPED)
        self.assertIn("Highlight und von Hand ausgeschlossen zugleich: Gamma three", self.stderr)
        self.assertFalse(os.path.exists(self.deck_path))

    def test_report_names_the_areas(self):
        self.run_build()
        areas = self.report().split("## Gebiete")[1].split("## Übersicht")[0]
        self.assertIn("- iNaturalist: Ort 1 (1), Ort 2 (2)", areas)
        self.assertIn("- OBIS: Testbucht", areas)
        self.assertIn("- FishBase/SeaLifeBase-Verbreitung: 001", areas)

    def test_without_region_the_deck_is_worldwide(self):
        recipe = json.loads(json.dumps(RECIPE))
        del recipe["region"]
        del recipe["taxa"]["obis"]
        self.write_recipe(recipe)
        self.run_build()
        inat_queries = [u for u in self.fetcher.requested if "species_counts" in u and "term_id" not in u]
        self.assertEqual(len(inat_queries), 1)
        self.assertNotIn("place_id", inat_queries[0])
        self.assertNotIn("swlat", inat_queries[0])
        self.assertFalse([u for u in self.fetcher.requested if "obis" in u])
        self.assertIn("- Region: weltweit", self.report())
        # Without OBIS and distribution data, only iNaturalist and the guide
        # confirm a highlight: Kappa ten (guide) stays, Nu thirteen
        # (distribution only) goes.
        names = self.deck()["speciesNames"]
        self.assertIn("Kappa ten", names)
        self.assertNotIn("Nu thirteen", names)
        self.assertNotIn("OBIS", [s["name"] for s in self.deck()["sources"]])

    # (g)
    def test_guide_comparison_both_ways(self):
        self.run_build()
        section = self.report().split("## Abgleich mit Führern")[1].split("## Ausgeschlossene")[0]
        suspects = section.split("**Im Deck, nicht im Führer**")[1].split("**Im Führer und häufig")[0]
        candidates = section.split("**Im Führer und häufig")[1]
        for name in ("Beta two", "Delta four", "Nu thirteen", "Theta eight"):
            self.assertIn(f"*{name}*", suspects)
        for name in ("Alpha one", "Gammaold three", "Epsilon five", "Kappa ten"):
            self.assertNotIn(f"*{name}*", suspects)
        self.assertIn("*Mu twelve*", candidates)
        self.assertNotIn("*Alpha one*", candidates)
        self.assertIn("6 Namen, 5 Arten aufgelöst, 1 Namen nicht aufgelöst", section)
        self.assertIn("*Omega unknown*", section)


    # Warnings to decide (deckbuilder/findings.py)
    def found(self):
        return self.report().split("## Zu entscheiden")[1].split("## Verworfene Highlights")[0]

    def test_mostly_dead_observations_are_reported(self):
        self.run_build()
        found = self.found()
        self.assertIn("| *Alpha one* | level-1 | tot beobachtet | 9 von 10 annotierten Beobachtungen tot (90 %) |",
                      found)
        self.assertNotIn("| *Beta two* | level-1 | tot beobachtet", found)     # 7 of 10
        self.assertNotIn("| *Delta four* | level-1 | tot beobachtet", found)   # 4 of 4, too few annotated
        self.assertIn("Alpha one", self.deck()["speciesNames"])

    def test_warning_thresholds_come_from_the_recipe(self):
        recipe = json.loads(json.dumps(RECIPE))
        recipe["warnings"] = {"deadShare": 0.7, "deadMinAnnotated": 4, "fewObserversShare": 0.9}
        self.write_recipe(recipe)
        self.run_build()
        found = self.found()
        self.assertIn("| *Beta two* | level-1 | tot beobachtet | 7 von 10", found)
        self.assertIn("| *Delta four* | level-1 | tot beobachtet | 4 von 4", found)
        self.assertNotIn("wenige Beobachter", found)

    def test_regional_name_is_reported_and_every_written_name_resolves(self):
        self.run_build()
        self.assertIn("| *Gammaold three* | level-2 | Name der Region | Deck: *Gammaold three*; "
                      "die Referenz-DB führt die Art als *Gamma three* |", self.found())
        names = self.deck()["speciesNames"]
        self.assertTrue(all(self.db.resolve(names).values()))
        with self.assertRaises(build.BuildError):
            build.check_names(self.db, {"Gammaold three": "s:3", "Delta old": "s:5"})

    def test_few_observers_are_reported_for_levels_1_and_2_only(self):
        self.run_build()
        found = self.found()
        self.assertIn("| *Alpha one* | level-1 | wenige Beobachter | 80 von 100 Beobachtungen von 2 Personen (80 %); "
                      "3 Beobachter insgesamt |", found)
        self.assertNotIn("| *Beta two* | level-1 | wenige Beobachter", found)
        asked = {int(query(u)["taxon_id"][0]) for u in self.fetcher.requested if "/observers" in u}
        self.assertIn(TAXON_IDS["Gammaold three"], asked)
        self.assertNotIn(TAXON_IDS["Theta eight"], asked)
        self.assertIn("| 1 | *Alpha one* (3 Beobachter) | 100 |", self.report())

    def test_freshwater_flag_is_reported_without_excluding(self):
        self.run_build()
        self.assertIn("| *Epsilon five* | level-2 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt "
                      "(Süß/Brack/Meer) |", self.found())
        self.assertIn("Epsilon five", self.deck()["speciesNames"])

    def test_warnings_are_summed_up_on_stdout(self):
        self.assertEqual(self.run_build(), build.EXIT_HIGHLIGHT_REJECTED)
        self.assertIn("[WARN] Zu entscheiden: 4 Warnungen (tot beobachtet 1, Name der Region 1, "
                      "wenige Beobachter 1, Süßwasser-Kennzeichen 1)", self.stdout)

    def test_a_level_below_its_minimum_count_stays_smaller(self):
        recipe = json.loads(json.dumps(RECIPE))
        recipe["levelMinCounts"] = [0, 75]
        self.write_recipe(recipe)
        self.run_build()
        levels = [s["speciesNames"] for s in self.deck()["subdecks"]]
        # Epsilon five (60) misses level 2 and moves on to level 3.
        self.assertEqual(levels[1:], [["Gammaold three"], ["Epsilon five"]])
        self.assertIn("Mindestzählung je Level 0/75", self.report())


class RecipeSchemaTest(unittest.TestCase):
    def errors(self, change):
        recipe = json.loads(json.dumps(RECIPE))
        change(recipe)
        return [e.message for e in recipe_module.validator().iter_errors(recipe)]

    def test_example_recipe_is_valid(self):
        self.assertEqual(self.errors(lambda r: None), [])

    def test_empty_place_list_is_rejected(self):
        def change(recipe):
            recipe["region"]["inat"] = {"placeIds": []}
        self.assertTrue(self.errors(change))

    def test_inat_order_needs_taxa(self):
        self.assertIn("'taxa' is a required property", self.errors(lambda r: r.pop("taxa")))

    def test_region_with_inat_order_needs_inat_area(self):
        def change(recipe):
            del recipe["region"]["inat"]
        self.assertIn("'inat' is a required property", self.errors(change))

    def test_gbif_order_needs_countries(self):
        def without_region(recipe):
            recipe["order"] = {"source": "gbif"}
            recipe["taxa"] = {"gbif": {"phylumKey": 44}}
            del recipe["region"]
        self.assertIn("'region' is a required property", self.errors(without_region))

        def with_countries(recipe):
            without_region(recipe)
            recipe["region"] = {"gbif": {"countries": ["CH", "AT"]}}
        self.assertEqual(self.errors(with_countries), [])

    def test_reef_order_needs_no_region(self):
        def change(recipe):
            recipe["order"] = {"source": "reef", "csv": "reef.csv"}
            del recipe["taxa"]
            del recipe["region"]
        self.assertEqual(self.errors(change), [])

    def test_warning_thresholds_and_level_minimums(self):
        def valid(recipe):
            recipe["levelMinCounts"] = [20, 10]
            recipe["warnings"] = {"deadShare": 0.8, "deadMinAnnotated": 5, "fewObserversShare": 0.5, "fewObservers": 2}
        self.assertEqual(self.errors(valid), [])
        self.assertTrue(self.errors(lambda r: r.update(warnings={"deadShare": 80})))
        self.assertTrue(self.errors(lambda r: r.update(warnings={"deadRatio": 0.8})))

    def test_more_level_minimums_than_levels_stop_the_load(self):
        recipe = json.loads(json.dumps(RECIPE))
        recipe["levelMinCounts"] = [1, 1, 1, 1]
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "r.json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump(recipe, f)
            with self.assertRaisesRegex(recipe_module.RecipeError, "levelMinCounts"):
                recipe_module.load(path)


class InatNamesFileTest(unittest.TestCase):
    ENTRY = {"inat": "Ascarosepion pfefferi", "referenceDb": "Metasepia pfefferi", "change": "swap",
             "reason": "Neue Gattung.", "evidence": "https://www.inaturalist.org/taxon_changes/131489"}

    def load(self, names):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "inat_names.json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump({"names": names}, f)
            return inat_names.load(path)

    def test_valid_entry(self):
        self.assertEqual(self.load([self.ENTRY]), [self.ENTRY])

    def test_entry_without_reason_or_evidence_is_rejected(self):
        for key in ("reason", "evidence"):
            with self.subTest(missing=key):
                entry = {k: v for k, v in self.ENTRY.items() if k != key}
                with self.assertRaisesRegex(recipe_module.RecipeError, f"'{key}' is a required property"):
                    self.load([entry])
        with self.assertRaises(recipe_module.RecipeError):
            self.load([{**self.ENTRY, "reason": ""}])
        with self.assertRaises(recipe_module.RecipeError):
            self.load([{**self.ENTRY, "evidence": "https://www.inaturalist.org/taxa/1"}])

    def test_a_name_twice_is_rejected(self):
        with self.assertRaisesRegex(recipe_module.RecipeError, "zweimal"):
            self.load([self.ENTRY, {**self.ENTRY, "referenceDb": "Sepia pfefferi"}])

    def test_missing_file_means_no_mapping(self):
        self.assertEqual(inat_names.load(os.path.join(ROOT, "no", "such.json")), [])

    def test_apply_sums_and_keeps_the_order(self):
        counts, applied = inat_names.apply([("A b", 5), ("Ascarosepion pfefferi", 7), ("Metasepia pfefferi", 3)],
                                           [self.ENTRY])
        self.assertEqual(counts, [("A b", 5), ("Metasepia pfefferi", 10)])
        self.assertEqual([(a.entry["inat"], a.count) for a in applied], [("Ascarosepion pfefferi", 7)])

    def test_the_repository_file_is_valid(self):
        self.assertTrue(inat_names.load(os.path.join(ROOT, "recipes", "inat_names.json")))


class RecipesTest(unittest.TestCase):
    def test_every_recipe_is_valid_and_its_files_exist(self):
        recipes_dir = os.path.join(ROOT, "recipes")
        # inat_names.json is no recipe; InatNamesFileTest checks it.
        paths = sorted(p for p in os.listdir(recipes_dir) if p.endswith(".json") and p != "inat_names.json")
        self.assertTrue(paths, "no recipe found")
        for name in paths:
            with self.subTest(recipe=name):
                loaded = recipe_module.load(os.path.join(recipes_dir, name))
                for guide in loaded.get("guides", []):
                    self.assertTrue(os.path.exists(guide["path"]), guide["path"])


if __name__ == "__main__":
    unittest.main()
