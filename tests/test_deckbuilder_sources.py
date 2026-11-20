#!/usr/bin/env python3
# =============================================================================
# test_deckbuilder_sources.py — tests for the source modules of
# scripts/deckbuilder/ (inat, gbif, obis, reef_csv, guide, refdb)
#
# The sources answer from recorded, trimmed API responses under
# tests/fixtures/deckbuilder/; the reference DB is a few rows the test
# builds itself. No network.
#
#   python3 -B -m unittest discover -s tests -v
# =============================================================================

import os
import tempfile
import unittest
from unittest import mock
from urllib.parse import parse_qs, urlsplit

from deckbuilder_support import FakeFetcher, fixture, make_refdb
from deckbuilder import gbif, guide, inat, obis, reef_csv
from deckbuilder.refdb import ReferenceDb, newest_release


def query(url):
    return parse_qs(urlsplit(url).query)


class INatTest(unittest.TestCase):
    # (h)
    def test_pages_until_all_results_are_read(self):
        pages = {1: fixture("inat_page1.json"), 2: fixture("inat_page2.json")}
        fetcher = FakeFetcher(answer=lambda base, params: pages.get(params["page"]))
        with mock.patch.object(inat, "PER_PAGE", 2):
            result = inat.species_counts(fetcher, {"placeId": 96795}, [47178, 47273])
        self.assertEqual(result.counts, [
            ("Abudefduf saxatilis", 120), ("Thalassoma bifasciatum", 80), ("Hippocampus reidi", 5),
        ])
        self.assertEqual(len(fetcher.requested), 2)
        first = query(fetcher.requested[0])
        self.assertEqual(first["place_id"], ["96795"])
        self.assertEqual(first["taxon_id"], ["47178,47273"])
        self.assertEqual(first["quality_grade"], ["research"])

    def test_rectangle(self):
        fetcher = FakeFetcher(answer=lambda base, params: {"total_results": 0, "results": []})
        inat.species_counts(fetcher, {"swlat": 9.0, "swlng": -88.5, "nelat": 27.5, "nelng": -59.0}, [47178])
        q = query(fetcher.requested[0])
        self.assertEqual((q["swlat"], q["nelng"]), (["9.0"], ["-59.0"]))
        self.assertNotIn("place_id", q)


class GbifTest(unittest.TestCase):
    # (i)
    def test_goes_through_the_fish_orders(self):
        names = fixture("gbif_names.json")

        def answer(base, params):
            if base.startswith("https://api.gbif.org/v1/species/"):
                return names[base.rsplit("/", 1)[1]]
            if params.get("facet") == "orderKey":
                return fixture("gbif_orders.json")
            if params.get("facet") == "speciesKey":
                return fixture("gbif_species_facet.json")
            return None

        fetcher = FakeFetcher(answer=answer)
        result = gbif.species_counts(fetcher, "CH", 44, {"Cypriniformes", "Perciformes"})
        self.assertEqual(result.counts, [("Neogobius melanostomus", 914), ("Telestes souffia", 300)])

        species_query = query(next(u for u in fetcher.requested if "facet=speciesKey" in u))
        self.assertEqual(species_query["orderKey"], ["1153", "549"])   # Passeriformes left out
        self.assertEqual(species_query["country"], ["CH"])
        self.assertNotIn("FOSSIL_SPECIMEN", species_query["basisOfRecord"])
        self.assertNotIn("LIVING_SPECIMEN", species_query["basisOfRecord"])
        self.assertIn("HUMAN_OBSERVATION", species_query["basisOfRecord"])
        order_query = query(next(u for u in fetcher.requested if "facet=orderKey" in u))
        self.assertEqual(order_query["phylumKey"], ["44"])


class ObisTest(unittest.TestCase):
    # (j)
    def test_only_species_over_all_pages(self):
        pages = {0: fixture("obis_page1.json"), 2: fixture("obis_page2.json")}
        fetcher = FakeFetcher(answer=lambda base, params: pages.get(params["skip"]))
        result = obis.checklist(fetcher, "POLYGON((0 0, 1 0, 1 1, 0 0))", [10194, 10193])
        self.assertEqual(result.counts, [("Epinephelus itajara", 324678), ("Elops smithi", 147498)])
        self.assertEqual(query(fetcher.requested[0])["taxonid"], ["10194,10193"])


class TextSourcesTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)

    def write(self, name, text):
        path = os.path.join(self._tmp.name, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return path

    def test_reef_csv(self):
        path = self.write("reef.csv", (
            "REEF Report\nRegion: Test\n"
            "Rank,Species,SF%,DEN\n"
            "1,\"Thalassoma bifasciatum, Bluehead\",85.2%,3.1\n"
            "2,\"Thalassoma bifasciatum, Bluehead\",12,1\n"
            "3,\"Sparisoma viride, Stoplight Parrotfish\",\"61,5\",2\n"
            "4,\"Gobiidae, gobies\",3%,1\n"
        ))
        result = reef_csv.sighting_frequencies(path)
        self.assertEqual(result.counts, [("Sparisoma viride", 61.5), ("Thalassoma bifasciatum", 85.2)])

    def test_reef_csv_without_header(self):
        path = self.write("reef.csv", "Species,SF%\n")
        with self.assertRaises(reef_csv.ReefCsvError):
            reef_csv.sighting_frequencies(path)

    def test_guide_skips_comments_and_blank_lines(self):
        path = self.write("guide.txt", "# Source: somewhere\n\nRhincodon typus\n  Hippocampus   reidi \n")
        self.assertEqual(guide.read_names(path), ["Rhincodon typus", "Hippocampus reidi"])


class ReferenceDbTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        path = os.path.join(self._tmp.name, "ref.db")
        make_refdb(
            path,
            species=[("s:1", "Eques punctatus", "fishbase", "3585", 3, 27)],
            synonyms=[("Equetus punctatus", "s:1")],
            occurrences=[("s:1", "044", "native", "present")],
            orders=[("Perciformes", "fishbase"), ("Decapoda", "sealifebase")],
        )
        self.db = ReferenceDb(path)
        self.addCleanup(self.db.close)

    # (d)
    def test_resolves_like_the_app(self):
        resolution = self.db.resolve(["Equetus punctatus", "equetus  PUNCTATUS Bloch 1787", "Equetus", "Nomen nudum"])
        self.assertEqual(resolution, {
            "Equetus punctatus": "s:1",
            "equetus  PUNCTATUS Bloch 1787": "s:1",
            "Equetus": None,
            "Nomen nudum": None,
        })
        species = self.db.species(["s:1"])["s:1"]
        self.assertEqual(species.preferred_name, "Eques punctatus")
        self.assertTrue(species.preferred_resolves)
        self.assertEqual((species.depth_min_m, species.max_length_cm), (3.0, 27.0))

    def test_occurrences_and_fish_orders(self):
        self.assertEqual([o.region_key for o in self.db.occurrences(["s:1"], ["044", "388"])["s:1"]], ["044"])
        self.assertEqual(self.db.fishbase_order_names(), {"Perciformes"})

    def test_newest_supported_schema(self):
        manifest = {"version": 2, "schemas": {"1": {"version": 2}, "2": {"version": 3}, "9": {"version": 9}}}
        self.assertEqual(newest_release(manifest), (2, {"version": 3}))
        self.assertEqual(newest_release({"version": 1, "url": "u"})[0], 1)


if __name__ == "__main__":
    unittest.main()
