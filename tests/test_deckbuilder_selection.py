#!/usr/bin/env python3
# =============================================================================
# test_deckbuilder_selection.py — tests for scripts/deckbuilder/selection.py
#
# The selection rules as pure functions: level split with highlights, the
# evidence a highlight needs, the water filter, the other filters and the
# comparison with a guide. No network, no files.
#
#   python3 -B -m unittest discover -s tests -v
# =============================================================================

import unittest

import deckbuilder_support  # noqa: F401  (puts scripts/ on the path)
from deckbuilder.refdb import Occurrence, SpeciesFacts
from deckbuilder.selection import (
    Candidate, Evidence, check_highlights, compare_with_guide, exclusion_reason, split_levels, water_verdict,
)


def facts(depth=None, length=None):
    return SpeciesFacts("x", "Xus xus", True, "fishbase", "1", "active", depth, length)


class SplitLevelsTest(unittest.TestCase):
    RANKED = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

    # (a)
    def test_levels_take_their_size_in_rank_order(self):
        levels, _, _ = split_levels(self.RANKED, [], [2, 3, 2])
        self.assertEqual(levels, [["a", "b"], ["c", "d", "e"], ["f", "g"]])

    # (a)
    def test_highlight_in_the_top_is_not_counted_twice(self):
        levels, _, _ = split_levels(self.RANKED, ["b"], [2, 3, 2])
        self.assertEqual(levels, [["a", "b"], ["c", "d", "e"], ["f", "g"]])

    # (a)
    def test_highlight_from_the_rest_moves_to_level_1_and_leaves_the_others(self):
        levels, sequence, cuts = split_levels(self.RANKED, ["d", "z"], [2, 3, 2])
        self.assertEqual(levels, [["a", "b", "d", "z"], ["c", "e", "f"], ["g", "h"]])
        self.assertEqual(sequence, ["a", "b", "c", "e", "f", "g", "h", "i"])
        self.assertEqual(cuts, [2, 5, 7])

    def test_short_list_leaves_later_levels_short(self):
        levels, _, cuts = split_levels(["a", "b", "c"], [], [2, 3, 2])
        self.assertEqual(levels, [["a", "b"], ["c"], []])
        self.assertEqual(cuts, [2, 3, 3])


    COUNTS = {"a": 50, "b": 40, "c": 30, "d": 20, "e": 9, "f": 8, "g": 6, "h": 5, "i": 4}

    def test_a_level_ends_at_its_minimum_and_leaves_the_rest_to_the_next(self):
        levels, sequence, cuts = split_levels(self.RANKED, [], [2, 3, 2], [0, 25, 5], self.COUNTS)
        self.assertEqual(levels, [["a", "b"], ["c"], ["d", "e"]])
        self.assertEqual(cuts, [2, 3, 5])
        self.assertEqual(sequence, self.RANKED)

    def test_a_level_below_its_minimum_stays_empty_and_highlights_need_none(self):
        levels, _, _ = split_levels(self.RANKED, ["i"], [2, 3, 2], [45, 100], self.COUNTS)
        self.assertEqual(levels, [["a", "i"], [], ["b", "c"]])


class HighlightTest(unittest.TestCase):
    RESOLUTION = {"Seen": "s1", "Listed": "s2", "Distributed": "s3", "Gone": "s4", "Nowhere": "s5",
                  "Synonym of seen": "s1", "Unknown": None}

    def evidence(self):
        return {
            "s1": Evidence(order_count=12),
            "s2": Evidence(guides=["Guide"]),
            "s3": Evidence(occurrences=[Occurrence("fishbase", "001", "native", "present")]),
            "s4": Evidence(occurrences=[Occurrence("fishbase", "001", "extirpated", "absent")]),
            "s5": Evidence(),
        }

    # (b)
    def test_highlight_needs_evidence_in_the_region(self):
        accepted, rejected = check_highlights(
            ["Seen", "Listed", "Distributed", "Gone", "Nowhere", "Unknown", "Synonym of seen"],
            self.RESOLUTION, self.evidence(),
        )
        self.assertEqual(accepted, ["s1", "s2", "s3"])
        self.assertEqual(rejected, [
            ("Gone", "kein Nachweis in der Region"),
            ("Nowhere", "kein Nachweis in der Region"),
            ("Unknown", "Name in der Referenz-DB nicht gefunden"),
        ])

    def test_obis_record_is_evidence(self):
        self.assertTrue(Evidence(obis_records=3).found())
        self.assertFalse(Evidence(order_count=0, obis_records=0).found())


class WaterTest(unittest.TestCase):
    # (c) flags are (fresh, brack, salt)
    def test_sea_deck(self):
        cases = {
            (0, 0, 1): True,     # saltwater
            (1, 1, 1): True,     # all three
            (0, 1, 1): True,
            (1, 0, 0): False,    # freshwater only
            (0, 1, 0): False,    # brackish alone is not a sea fish
            (1, 1, 0): False,
            (0, 0, 0): True,     # unknown stays in
            None: True,          # not in the parquets: unknown
        }
        for flags, expected in cases.items():
            with self.subTest(flags=flags):
                self.assertEqual(water_verdict(flags, "salt"), expected)

    # (c)
    def test_freshwater_deck(self):
        self.assertTrue(water_verdict((1, 0, 0), "fresh"))
        self.assertFalse(water_verdict((0, 1, 1), "fresh"))
        self.assertTrue(water_verdict((0, 0, 0), "fresh"))

    def test_any_takes_everything(self):
        self.assertTrue(water_verdict((1, 0, 0), "any"))

    # (c)
    def test_exclusion_reason_for_water(self):
        self.assertEqual(exclusion_reason(Candidate("x", 50), facts(), (0, 1, 0), {"water": "salt"}),
                         ("kein Meeresfisch", "Saltwater nicht gesetzt"))
        self.assertIsNone(exclusion_reason(Candidate("x", 50), facts(), (0, 0, 0), {"water": "salt"}))


class FilterTest(unittest.TestCase):
    FILTERS = {"minCount": 5, "diveDepthLimitM": 40, "minLengthCm": 4}

    def reason(self, count=10, depth=None, length=None):
        result = exclusion_reason(Candidate("x", count), facts(depth, length), None, self.FILTERS)
        return result and result[0]

    def test_filters(self):
        self.assertIsNone(self.reason())
        self.assertEqual(self.reason(count=4), "zu wenige Nachweise")
        self.assertIsNone(self.reason(count=5))
        self.assertEqual(self.reason(depth=41), "nur tiefer als die Tauchgrenze")
        self.assertIsNone(self.reason(depth=40))
        self.assertEqual(self.reason(length=3.5), "zu klein")
        self.assertIsNone(self.reason(length=4))


class GuideComparisonTest(unittest.TestCase):
    # (g)
    def test_both_directions(self):
        deck = ["a", "b", "c"]
        guide = {"a", "c", "d", "e", "z"}
        ranked = ["a", "b", "c", "e", "x", "d"]
        suspects, candidates = compare_with_guide(deck, guide, ranked)
        self.assertEqual(suspects, ["b"])
        self.assertEqual(candidates, ["e", "d"])


if __name__ == "__main__":
    unittest.main()
