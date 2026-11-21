# =============================================================================
# findings.py — warnings about deck species, to be decided in the recipe
#
# A deck needs the species a diver meets in the region, each under the name
# that is right there. The filters cannot tell everything; these warnings
# point at what a person has to decide (exclude with a reason, map a name,
# change a level). Nothing here takes a species out.
#
# - dead: most annotated observations say dead — empty shells, beach finds,
#   fish on the market.
# - name of the region: the deck carries the iNaturalist name, which the
#   reference DB knows only as a synonym of the species it lists; often a
#   species complex the reference DB has not split (Halichoeres annularis
#   under H. marginatus). The app resolves the name through its synonyms all
#   the same, and the deck is right once the reference DB splits.
# - few observers: two people made most of the observations, so the count
#   says little about how common the species is.
# - freshwater: FishBase/SeaLifeBase set Fresh. Many reef species rightly
#   carry it (tarpon, bull shark), a few are river or pond fishes.
#
# The thresholds come from the recipe's `warnings`, with DEFAULTS.
# =============================================================================

from dataclasses import dataclass

DEAD = "tot beobachtet"
REGION_NAME = "Name der Region"
FEW_OBSERVERS = "wenige Beobachter"
FRESHWATER = "Süßwasser-Kennzeichen"
KINDS = (DEAD, REGION_NAME, FEW_OBSERVERS, FRESHWATER)

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
    annotated = signals.annotated.get(species_id, 0)
    found = signals.dead.get(species_id, 0)
    if annotated >= t["deadMinAnnotated"] and found >= t["deadShare"] * annotated:
        return f"{found} von {annotated} annotierten Beobachtungen tot ({percent(found, annotated)})"
    return None


def region_name(written, preferred):
    if written != preferred:
        return f"Deck: *{written}*; die Referenz-DB führt die Art als *{preferred}*"
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


def freshwater(flags):
    if flags and flags[0]:
        return "FishBase/SeaLifeBase: Fresh gesetzt (" + "/".join(
            label for label, flag in zip(("Süß", "Brack", "Meer"), flags) if flag) + ")"
    return None


def find(subdeck_of, written, facts, flags, evidence, signals, t):
    """Findings for the species in `subdeck_of` (id → subdeck id, in deck
    order); `written` is the deck name per id, `signals` a
    signals.Signals or None if there are none for this order source."""
    found = []
    for species_id, subdeck in subdeck_of.items():
        ev = evidence.get(species_id)
        checks = [
            (DEAD, dead(signals, species_id, t) if signals else None),
            (REGION_NAME, region_name(written[species_id], facts[species_id].preferred_name)),
            (FEW_OBSERVERS, few_observers(signals, species_id, ev.order_count if ev else None, t) if signals else None),
            (FRESHWATER, freshwater(flags.get(species_id))),
        ]
        found += [Finding(species_id, subdeck, kind, detail) for kind, detail in checks if detail]
    return found
