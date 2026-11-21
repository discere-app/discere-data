# =============================================================================
# findings.py — warnings about deck species, to be decided in the recipe
#
# A deck needs the species a diver meets in the region. The filters cannot
# tell everything; these warnings point at what a person has to decide
# (exclude with a reason, change a level). Nothing here takes a species out.
#
# - dead: most observations annotated alive or dead say dead — empty
#   shells, beach finds, fish on the market. "Cannot be determined" says
#   neither and stays out of the share.
# - few observers: two people made most of the observations, so the count
#   says little about how common the species is.
#
# Both rest on iNaturalist's signals (deckbuilder/signals.py), so a deck
# ordered by another source gets no warnings.
#
# The thresholds come from the recipe's `warnings`, with DEFAULTS.
# =============================================================================

from dataclasses import dataclass

DEAD = "tot beobachtet"
FEW_OBSERVERS = "wenige Beobachter"
KINDS = (DEAD, FEW_OBSERVERS)

DEFAULTS = {"deadShare": 0.8, "deadMinAnnotated": 5, "fewObserversShare": 0.5, "fewObservers": 2}


@dataclass
class Finding:
    species_id: str
    subdeck: str   # the subdeck id
    kind: str      # one of KINDS
    detail: str    # the numbers behind it


def thresholds(recipe):
    return {**DEFAULTS, **recipe.get("warnings", {})}


def percent(part, whole):
    return f"{100 * part / whole:.0f} %"


def dead(signals, species_id, t):
    found = signals.dead.get(species_id, 0)
    annotated = signals.alive.get(species_id, 0) + found
    if annotated >= t["deadMinAnnotated"] and found >= t["deadShare"] * annotated:
        return f"{found} von {annotated} Beobachtungen mit Angabe lebend/tot tot ({percent(found, annotated)})"
    return None


def few_observers(signals, species_id, observations, t):
    if species_id not in signals.observers or not observations:
        return None
    total, top = signals.observers[species_id]
    most = sum(top[:t["fewObservers"]])
    if most >= t["fewObserversShare"] * observations:
        return (f"{most} von {observations:g} Beobachtungen von {min(t['fewObservers'], total)} Personen "
                f"({percent(most, observations)}); {total} Beobachter insgesamt")
    return None


def find(subdeck_of, evidence, signals, t):
    """Findings for the species in `subdeck_of` (id → subdeck id, in deck
    order); `signals` is a signals.Signals, or None if the order source
    has none."""
    if signals is None:
        return []
    found = []
    for species_id, subdeck in subdeck_of.items():
        ev = evidence.get(species_id)
        checks = [
            (DEAD, dead(signals, species_id, t)),
            (FEW_OBSERVERS, few_observers(signals, species_id, ev.order_count if ev else None, t)),
        ]
        found += [Finding(species_id, subdeck, kind, detail) for kind, detail in checks if detail]
    return found
