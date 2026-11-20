# =============================================================================
# report.py — the report of a deckbuilder run (recipes/<base>.report.md)
#
# The deck says which species; the report says why, so a reviewer can check
# the deck in its PR without running anything: the evidence for every deck
# species (count per source, FishBase/SeaLifeBase distribution in the recipe
# regions, water type, guide), the highlights that stayed out, the species
# around each level boundary, the comparison with the guides both ways, the
# excluded candidates with their reason and the names nobody resolved.
#
# The report holds no date or path, so a rerun on the same data writes the
# same file and its diff shows only what changed.
# =============================================================================

from collections import Counter

from .selection import BOUNDARY_WIDTH, boundaries, compare_with_guide

ORDER_LABELS = {"inat": "iNat", "gbif": "GBIF", "reef": "REEF SF%"}

# How many guide species missing from the deck the report lists.
MISSING_SHOWN = 30


def water_label(flags):
    if flags is None:
        return "?"
    parts = [label for label, flag in zip(("Süß", "Brack", "Meer"), flags) if flag]
    return "/".join(parts) or "?"


def occurrence_label(occurrences):
    """Distribution entries summarized by status, e.g. "native ×5"; the
    entries that deny occurrence ("absent") come last, struck out."""
    if not occurrences:
        return "–"
    present = Counter((o.establishment_status or "?").lower() for o in occurrences if o.is_evidence)
    absent = Counter((o.establishment_status or "?").lower() for o in occurrences if not o.is_evidence)
    parts = [f"{status} ×{n}" for status, n in sorted(present.items())]
    parts += [f"~~{status} ×{n}~~" for status, n in sorted(absent.items())]
    return ", ".join(parts)


def number(value):
    if value is None:
        return "–"
    return f"{value:g}" if isinstance(value, float) else str(value)


def escape(text):
    return str(text).replace("|", "\\|")


class Report:
    def __init__(self, recipe, base, selection, names, facts, flags, evidence, guides, notes, meta, existing_names):
        self.recipe = recipe
        self.base = base
        self.s = selection
        self.names = names
        self.facts = facts
        self.flags = flags
        self.evidence = evidence
        self.guides = guides          # [(guide, set of ids, [unresolved names], number of names)]
        self.notes = notes
        self.meta = meta              # [(label, value)] for the header
        self.existing_names = existing_names
        self.order_label = ORDER_LABELS[recipe["order"]["source"]]
        self.level_of = {i: n for n, level in enumerate(selection.levels, 1) for i in level}
        self.rank_of = {i: n for n, i in enumerate(selection.ranked, 1)}
        self.lines = []

    def out(self, line=""):
        self.lines.append(line)

    def table_header(self, extra=()):
        columns = ["Rang", "Art", self.order_label, "OBIS", "FishBase/SLB im Gebiet", "Wasser"]
        if self.guides:
            columns.append("Führer")
        columns += list(extra)
        self.out("| " + " | ".join(columns) + " |")
        self.out("|" + "---|" * len(columns))

    def row(self, species_id, extra=()):
        ev = self.evidence.get(species_id)
        name = self.names[species_id]
        note = []
        if species_id in self.s.highlights:
            note.append("Highlight")
        source_names = [n for n in getattr(self.s.candidates.get(species_id), "names", []) if n != name]
        if source_names:
            note.append("Quelle: " + ", ".join(f"*{escape(n)}*" for n in source_names))
        if not self.facts[species_id].preferred_resolves:
            note.append(f"bevorzugter Name *{escape(self.facts[species_id].preferred_name)}* löst anders auf")
        cells = [
            number(self.rank_of.get(species_id)),
            f"*{escape(name)}*" + (f" ({'; '.join(note)})" if note else ""),
            number(ev.order_count if ev else None),
            number(ev.obis_records if ev else None),
            occurrence_label(ev.occurrences if ev else []),
            water_label(self.flags.get(species_id)),
        ]
        if self.guides:
            cells.append(", ".join(str(n) for n, (_, ids, _, _) in enumerate(self.guides, 1) if species_id in ids) or "–")
        cells += [str(c) for c in extra]
        self.out("| " + " | ".join(cells) + " |")

    def render(self):
        s = self.s
        deck_ids = [i for level in s.levels for i in level]
        self.out(f"# Bericht: {self.recipe['deck']['name']} (`recipes/{self.base}.json`)")
        self.out()
        self.out("Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und "
                 "Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.")
        self.out()
        for label, value in self.meta:
            self.out(f"- {label}: {value}")
        for note in self.notes:
            self.out(f"- {note}")
        self.out()

        self.out("## Übersicht")
        self.out()
        self.out(f"- Arten der Reihenfolge-Quelle, aufgelöst: {len(s.candidates)}; nicht aufgelöst: {len(s.unresolved)}")
        self.out(f"- ausgeschlossen: {len(s.excluded)}")
        for reason, n in Counter(reason for _, reason, _ in s.excluded).most_common():
            self.out(f"  - {reason}: {n}")
        self.out(f"- Kandidaten nach den Filtern: {len(s.ranked)}")
        sizes = ", ".join(f"Level {n}: {len(level)}" for n, level in enumerate(s.levels, 1))
        self.out(f"- Deck: {len(deck_ids)} Arten ({sizes}); Umfang laut Rezept "
                 f"{'/'.join(map(str, self.recipe['levelSizes']))} plus Highlights")
        self.out(f"- Highlights: {len(s.highlights)} im Deck, {len(s.rejected_highlights)} verworfen")
        self.out()

        self.out("## Verworfene Highlights")
        self.out()
        if s.rejected_highlights:
            self.out("**Diese Highlights stehen nicht im Deck.** Ohne Nachweis in der Region (Reihenfolge-Quelle, "
                     "OBIS, Verbreitungsdaten oder Führer) kommt keine Art ins Deck; der Lauf endet mit Fehler.")
            self.out()
            for name, reason in s.rejected_highlights:
                self.out(f"- *{escape(name)}*: {reason}")
        else:
            self.out("Keine.")
        self.out()

        self.out("## Deck")
        self.out()
        self.out(f"Spalten: Rang unter den Kandidaten, Zählung der Reihenfolge-Quelle ({self.order_label}), "
                 "OBIS-Nachweise, Einträge der FishBase/SeaLifeBase-Verbreitung in den Rezept-Regionen "
                 "(~~durchgestrichen~~: Eintrag sagt „nicht vorhanden“), Wasser laut FishBase/SeaLifeBase"
                 + (", Nummer des Führers, der die Art listet." if self.guides else "."))
        for n, level in enumerate(s.levels, 1):
            self.out()
            self.out(f"### Level {n} ({len(level)})")
            self.out()
            self.table_header()
            for species_id in level:
                self.row(species_id)
        self.out()

        self.out("## Grenzfälle")
        self.out()
        self.out(f"Je {BOUNDARY_WIDTH} Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels "
                 "sie nehmen (Highlights ab Level 2 übersprungen).")
        for level, before, after in boundaries(s):
            self.out()
            label = f"Level {level}/{level + 1}" if level < len(s.levels) else f"Level {level}/nicht im Deck"
            self.out(f"### {label}")
            self.out()
            self.table_header(["Level"])
            for species_id in before:
                self.row(species_id, [self.level_of.get(species_id, "–")])
            self.out("| | **Grenze** | | | | |" + (" |" if self.guides else "") + " |")
            for species_id in after:
                self.row(species_id, [self.level_of.get(species_id, "–")])
        self.out()

        self.out("## Abgleich mit Führern")
        self.out()
        if not self.guides:
            self.out("Das Rezept nennt keinen Führer.")
        for n, (guide, ids, unresolved, total) in enumerate(self.guides, 1):
            suspects, missing = compare_with_guide(deck_ids, ids, s.ranked)
            self.out(f"### {n}. {escape(guide['name'])}")
            self.out()
            self.out(f"- {total} Namen, {len(ids)} Arten aufgelöst, {len(unresolved)} Namen nicht aufgelöst")
            self.out(f"- Deck-Arten im Führer: {len(deck_ids) - len(suspects)}/{len(deck_ids)}")
            for level_n, level in enumerate(s.levels, 1):
                self.out(f"  - Level {level_n}: {sum(1 for i in level if i in ids)}/{len(level)}")
            self.out(f"- Kandidaten im Führer, aber nicht im Deck: {len(missing)}")
            self.out()
            self.out("**Im Deck, nicht im Führer** (Verdacht: Fehlbestimmung, falsch verortet oder Süßwasser):")
            self.out()
            if suspects:
                self.table_header(["Level"])
                for species_id in suspects:
                    self.row(species_id, [self.level_of[species_id]])
            else:
                self.out("Keine.")
            self.out()
            self.out(f"**Im Führer und häufig, aber nicht im Deck** (Kandidaten; die {MISSING_SHOWN} häufigsten):")
            self.out()
            if missing:
                self.table_header()
                for species_id in missing[:MISSING_SHOWN]:
                    self.row(species_id)
            else:
                self.out("Keine.")
            if unresolved:
                self.out()
                self.out("<details><summary>Nicht aufgelöste Namen des Führers</summary>")
                self.out()
                self.out(", ".join(f"*{escape(name)}*" for name in unresolved))
                self.out()
                self.out("</details>")
            self.out()

        if self.existing_names is not None:
            new_names = {self.names[i] for i in deck_ids}
            old_names = set(self.existing_names)
            self.out("## Änderungen gegenüber dem bestehenden Deck")
            self.out()
            added = sorted(new_names - old_names)
            removed = sorted(old_names - new_names)
            self.out(f"- neu: {len(added)}" + (": " + ", ".join(f"*{escape(n)}*" for n in added) if added else ""))
            self.out(f"- entfallen: {len(removed)}"
                     + (": " + ", ".join(f"*{escape(n)}*" for n in removed) if removed else ""))
            self.out()

        self.out("## Ausgeschlossene Kandidaten")
        self.out()
        if s.excluded:
            self.out("<details><summary>" + f"{len(s.excluded)} Arten" + "</summary>")
            self.out()
            self.out(f"| Art | {self.order_label} | Wasser | Grund |")
            self.out("|---|---|---|---|")
            for species_id, reason, detail in s.excluded:
                self.out(f"| *{escape(self.names[species_id])}* | {number(s.candidates[species_id].count)} | "
                         f"{water_label(self.flags.get(species_id))} | {reason} ({detail}) |")
            self.out()
            self.out("</details>")
        else:
            self.out("Keine.")
        self.out()

        self.out("## Nicht aufgelöste Namen der Reihenfolge-Quelle")
        self.out()
        if s.unresolved:
            self.out("Die Referenz-DB der App kennt diese Namen nicht; die App fände sie auch nicht.")
            self.out()
            self.out(f"| Name | {self.order_label} |")
            self.out("|---|---|")
            for name, count in s.unresolved:
                self.out(f"| *{escape(name)}* | {number(count)} |")
        else:
            self.out("Keine.")
        return "\n".join(self.lines) + "\n"

