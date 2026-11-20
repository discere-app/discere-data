# =============================================================================
# checks.py — checks on a finished selection, for the report
#
# Pure functions; the run collects their inputs from the reference DB.
#
# - Evidence from two independent sources: the order source (observations)
#   and OBIS or the FishBase/SeaLifeBase distribution (records and
#   literature). A species seen only by the order source may be a
#   misidentification that many observers repeat; the report lists those.
# - Endemics: species whose distribution entry in a recipe region says
#   "endemic".
# - Common names: with nameType commonName the app asks for the common name
#   of what the learning mode asks for (the species, or its genus or
#   family), in the app language, falling back to English, then to the
#   scientific name. The report counts the deck species and families
#   without a German or English name in the reference DB.
# - One species under two entries: two deck species with the same common
#   name, or sharing a scientific name (as Pterois cincta and Pteropterus
#   cinctus once did), are listed for a person to look at.
# =============================================================================

from dataclasses import dataclass, field

LANGUAGES = ("de", "en")


@dataclass
class Checks:
    two_sources: list                 # ids with order source and an independent source
    single_source: list               # [(id, source label)] the others
    endemic: list                     # ids endemic in a recipe region
    species_without_name: dict        # language → [ids]
    families: dict                    # family id → (family name, [ids])
    families_without_name: dict       # language → [family ids]
    same_common_name: list = field(default_factory=list)   # [(language, name, [ids])]
    shared_scientific: list = field(default_factory=list)  # [(id a, id b, normalized name)]


def evidence_sources(ev):
    """Labels of the sources that say a species occurs in the region."""
    labels = []
    if ev.order_count:
        labels.append("Reihenfolge-Quelle")
    if ev.obis_records:
        labels.append("OBIS")
    if any(o.is_evidence for o in ev.occurrences):
        labels.append("Verbreitung")
    if ev.guides:
        labels.append("Führer")
    return labels


def run_checks(deck_ids, evidence, species_names, family_of, family_names, shared_names):
    """`species_names`/`family_names`: entity id → {language: name};
    `family_of`: species id → (family id, family name); `shared_names`:
    refdb.shared_scientific_names of the deck species."""
    two, single, endemic = [], [], []
    for i in deck_ids:
        ev = evidence[i]
        independent = ev.obis_records or any(o.is_evidence for o in ev.occurrences)
        if ev.order_count and independent:
            two.append(i)
        else:
            single.append((i, ", ".join(evidence_sources(ev)) or "keine"))
        if any(o.is_evidence and (o.establishment_status or "").lower() == "endemic" for o in ev.occurrences):
            endemic.append(i)

    species_without = {lang: [i for i in deck_ids if lang not in species_names.get(i, {})] for lang in LANGUAGES}

    families = {}
    for i in deck_ids:
        if i in family_of:
            family_id, family_name = family_of[i]
            families.setdefault(family_id, (family_name, []))[1].append(i)
    families_without = {
        lang: sorted((f for f in families if lang not in family_names.get(f, {})), key=lambda f: families[f][0])
        for lang in LANGUAGES
    }

    same = []
    for lang in LANGUAGES:
        by_name = {}
        for i in deck_ids:
            name = species_names.get(i, {}).get(lang)
            if name:
                by_name.setdefault(name.casefold(), []).append(i)
        same += [(lang, species_names[ids[0]][lang], ids) for _, ids in sorted(by_name.items()) if len(ids) > 1]

    return Checks(two, single, endemic, species_without, families, families_without, same, list(shared_names))
