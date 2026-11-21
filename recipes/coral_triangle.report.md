# Bericht: Korallendreieck (`recipes/coral_triangle.json`)

Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.

- Referenz-DB: v3 (FishBase v26.06, SeaLifeBase v26.06)
- Salz/Süß: FishBase/SeaLifeBase v25.04 (species.parquet)
- iNaturalist: 3082 Taxa (Seiten: 7)
- OBIS: 6028 Arten mit Nachweisen außer iNaturalist
- Bild: https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Coral_in_Raja_Ampat.jpg/330px-Coral_in_Raja_Ampat.jpg — Akbar raf, CC BY-SA 4.0, https://commons.wikimedia.org/wiki/File:Coral_in_Raja_Ampat.jpg

## Gebiete

- iNaturalist: Indonesia (6966), Philippines (6873), Sabah, MY (13134), Papua New Guinea (7013), East Timor (10314), Solomon Islands (7081)
- OBIS: Indonesien und Osttimor (Rechteck; schließt Malakkastraße und Nordborneo ein), Philippinen und Sabah nördlich 6° N, Papua-Neuguinea und Salomonen (Rechteck; schließt die Torres-Straße ein)
- FishBase/SeaLifeBase-Verbreitung: 360, 608, 458, 598, 598A, 626, 090

## Übersicht

- Arten der Reihenfolge-Quelle, aufgelöst: 3021; nicht aufgelöst: 41
- ausgeschlossen: 1486
  - zu wenige Nachweise: 841
  - kein Meeresfisch: 516
  - zu klein: 121
  - nur tiefer als die Tauchgrenze: 8
- Kandidaten nach den Filtern: 1535
- Deck: 158 Arten (Level 1: 48, Level 2: 60, Level 3: 50); Umfang laut Rezept 40/60/50 plus Highlights
- Highlights: 8 im Deck, 0 verworfen

## Zu entscheiden

Hinweise, keine Ausschlüsse: Jede Zeile wird im Rezept entschieden (`exclude` mit Grund, Namenszuordnung, Level) oder bewusst belassen. Schwellen: `warnings` im Rezept.

| Art | Subdeck | Warnung | Zahlen |
|---|---|---|---|
| *Concholabrus fasciatus* | level-2 | Name der Region | Deck: *Concholabrus fasciatus*; die Referenz-DB führt die Art als *Cheilinus fasciatus* |
| *Pteraeolidia semperi* | invertebrates | Name der Region | Deck: *Pteraeolidia semperi*; die Referenz-DB führt die Art als *Pteraeolidia ianthina* |
| *Acanthaster solaris* | invertebrates | Name der Region | Deck: *Acanthaster solaris*; die Referenz-DB führt die Art als *Acanthaster planci* |
| *Mobula alfredi* | level-2 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Meer) |
| *Caranx sexfasciatus* | level-3 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |

## Verworfene Highlights

Keine.

## iNaturalist-Namen zugeordnet

Laut `recipes/inat_names.json`: iNaturalist nennt die Art anders als die Referenz-DB; die Zählung kommt zu der der Referenz-DB-Art.

| iNaturalist | Referenz-DB | iNat | Art | Beleg |
|---|---|---|---|---|
| *Ascarosepion pfefferi* | *Metasepia pfefferi* | 638 | Umbenennung | https://www.inaturalist.org/taxon_changes/131489 |
| *Pseudanthias cheirospilos* | *Pseudanthias squamipinnis* | 564 | Abspaltung | https://www.inaturalist.org/taxon_changes/147467 |
| *Coris schroederii* | *Coris batuensis* | 375 | Abspaltung | https://www.inaturalist.org/taxon_changes/157302 |
| *Eviotops atriventris* | *Eviota atriventris* | 328 | Umbenennung | https://www.inaturalist.org/taxon_changes/178886 |
| *Ascarosepion bandense* | *Sepia bandensis* | 253 | Umbenennung | https://www.inaturalist.org/taxon_changes/131481 |
| *Eviotops sebreei* | *Eviota sebreei* | 227 | Umbenennung | https://www.inaturalist.org/taxon_changes/178922 |
| *Ascarosepion papuense* | *Sepia papuensis* | 187 | Umbenennung | https://www.inaturalist.org/taxon_changes/131455 |
| *Eviotops bifasciatus* | *Eviota bifasciata* | 96 | Umbenennung | https://www.inaturalist.org/taxon_changes/178889 |
| *Pinnoctopus luteus* | *Callistoctopus luteus* | 69 | Umbenennung | https://www.inaturalist.org/taxon_changes/172616 |
| *Eviotops prasites* | *Eviota prasites* | 63 | Umbenennung | https://www.inaturalist.org/taxon_changes/178916 |
| *Eviotops ancora* | *Eviota ancora* | 51 | Umbenennung | https://www.inaturalist.org/taxon_changes/178883 |
| *Eviotops nigriventris* | *Eviota nigriventris* | 49 | Umbenennung | https://www.inaturalist.org/taxon_changes/178908 |
| *Eviotops sigillatus* | *Eviota sigillata* | 44 | Umbenennung | https://www.inaturalist.org/taxon_changes/178924 |
| *Eviotops longirostris* | *Eviota longirostris* | 16 | Umbenennung | https://www.inaturalist.org/taxon_changes/178903 |
| *Pinnoctopus aspilosomatis* | *Callistoctopus aspilosomatis* | 12 | Umbenennung | https://www.inaturalist.org/taxon_changes/172611 |
| *Eviotops raja* | *Eviota raja* | 12 | Umbenennung | https://www.inaturalist.org/taxon_changes/178919 |
| *Eviota bryozophila* | *Sueviota bryozophila* | 12 | Umbenennung | https://www.inaturalist.org/taxon_changes/178948 |
| *Eviotops shimadai* | *Eviota shimadai* | 11 | Umbenennung | https://www.inaturalist.org/taxon_changes/178923 |
| *Eviotops brahmi* | *Eviota brahmi* | 8 | Umbenennung | https://www.inaturalist.org/taxon_changes/178891 |
| *Eviotops rubriceps* | *Eviota rubriceps* | 8 | Umbenennung | https://www.inaturalist.org/taxon_changes/178920 |
| *Eviota lachneri* | *Sueviota lachneri* | 7 | Umbenennung | https://www.inaturalist.org/taxon_changes/178945 |
| *Acanthosepion recurvirostrum* | *Sepia recurvirostra* | 6 | Umbenennung | https://www.inaturalist.org/taxon_changes/131450 |
| *Eviotops bellus* | *Eviota bella* | 6 | Umbenennung | https://www.inaturalist.org/taxon_changes/178888 |
| *Eviotops imitatus* | *Eviota imitata* | 5 | Umbenennung | https://www.inaturalist.org/taxon_changes/178898 |
| *Eviotops punyit* | *Eviota punyit* | 4 | Umbenennung | https://www.inaturalist.org/taxon_changes/178918 |
| *Eviotops oculineatus* | *Eviota oculineata* | 2 | Umbenennung | https://www.inaturalist.org/taxon_changes/178909 |
| *Pinnoctopus ornatus* | *Callistoctopus ornatus* | 1 | Umbenennung | https://www.inaturalist.org/taxon_changes/172615 |
| *Eviotops spilotus* | *Eviota spilota* | 1 | Umbenennung | https://www.inaturalist.org/taxon_changes/178925 |

## Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Rhincodon typus* | Der Walhai, größter Fisch der Welt, lässt sich in der Cenderawasih-Bucht und vor Oslob verlässlich beobachten. | 220 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Mobula birostris* | Der Riesenmanta ist in Raja Ampat und Komodo eine der Begegnungen, für die Taucher anreisen. | 681 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Mola alexandrini* | Der Mondfisch steigt vor Nusa Penida aus der Tiefe zu den Putzerstationen auf, ein Grund für viele Bali-Reisen. | 611 | Reihenfolge-Quelle, OBIS | Level 1 |
| *Hippocampus bargibanti* | Das Zwergseepferdchen lebt getarnt auf Gorgonien und ist das Sinnbild des Makrotauchens in der Region. | – | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Synchiropus splendidus* | Der Mandarinfisch balzt in der Dämmerung, ein Pflichttauchgang in Lembeh und Anilao. | 218 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Hemiscyllium freycineti* | Der Raja-Ampat-Epaulettenhai läuft nachts mit den Flossen über den Riffboden und kommt nur in Westpapua vor. | 420 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Metasepia pfefferi* | Die Prachtsepia wandert in Warnfarben über den Sand und ist ein Ziel jedes Muck-Dive. | 95 | Reihenfolge-Quelle, Verbreitung | Level 1 |
| *Wunderpus photogenicus* | Der Wunderpus ist der gestreifte Krake, wegen dem viele Taucher nach Lembeh kommen. | 253 | Reihenfolge-Quelle, Verbreitung | Level 1 |

## Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS ohne iNaturalist oder Verbreitung): 158/158 (100 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 0
- Arten ohne Volksnamen `de` in der Referenz-DB: 85/158 (54 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 0/158 (0 %)
- Familien ohne Volksnamen `de`: 7/46 (15 %): *Anthiadidae*, *Cheloniidae*, *Epinephelidae*, *Loliginidae*, *Mobulidae*, *Octopodidae*, *Sepiidae*
- Familien ohne Volksnamen `en`: 0/46 (0 %)

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

Keine.

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

- gleicher Volksname `de` „krake“: *Octopus cyanea*, *Amphioctopus marginatus*
- gleicher Volksname `de` „Lippfisch“: *Coris gaimard*, *Choerodon anchorago*
- gleicher Volksname `de` „Schnapper“: *Macolor macularis*, *Lutjanus decussatus*

## Deck

Spalten: Rang unter den Kandidaten, Zählung der Reihenfolge-Quelle (iNat), OBIS-Nachweise ohne den iNaturalist-Datensatz, Einträge der FishBase/SeaLifeBase-Verbreitung in den Rezept-Regionen (~~durchgestrichen~~: Eintrag sagt „nicht vorhanden“), Wasser laut FishBase/SeaLifeBase.

### Level 1 (48)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 1 | *Amphiprion clarkii* (835 Beobachter) | 2925 | 398 | native ×6 | Meer |
| 2 | *Chelonia mydas* (1223 Beobachter) | 2830 | 2972 | native ×6 | Meer |
| 3 | *Amphiprion ocellaris* (920 Beobachter) | 2358 | 153 | native ×6 | Meer |
| 4 | *Arothron nigropunctatus* (766 Beobachter) | 2244 | 227 | native ×4 | Meer |
| 5 | *Zanclus cornutus* (850 Beobachter) | 2148 | 737 | native ×4 | Meer |
| 6 | *Eretmochelys imbricata* (918 Beobachter) | 1896 | 598 | native ×6 | Brack/Meer |
| 7 | *Pteropterus antennatus* (509 Beobachter) | 1599 | 353 | native ×4 | Meer |
| 8 | *Solenostomus paradoxus* (415 Beobachter) | 1595 | 39 | native ×6 | Meer |
| 9 | *Aulostomus chinensis* (626 Beobachter) | 1593 | 115 | native ×4 | Meer |
| 10 | *Pterois volitans* (570 Beobachter) | 1564 | 277 | native ×5 | Meer |
| 11 | *Dascyllus trimaculatus* (573 Beobachter) | 1538 | 634 | native ×6 | Meer |
| 12 | *Chaetodon kleinii* (532 Beobachter) | 1502 | 826 | native ×6 | Meer |
| 13 | *Ascarosepion latimanus* (509 Beobachter) | 1446 | 19 | native ×5 | Meer |
| 14 | *Canthigaster valentini* (466 Beobachter) | 1403 | 288 | native ×4 | Meer |
| 15 | *Amphiprion perideraion* (477 Beobachter) | 1349 | 264 | native ×6 | Brack/Meer |
| 16 | *Amphiprion biaculeatus* (506 Beobachter) | 1344 | 81 | native ×6 | Meer |
| 17 | *Thalassoma lunare* (449 Beobachter) | 1270 | 1004 | native ×5 | Meer |
| 18 | *Abudefduf vaigiensis* (Quelle: *Abudefduf caudobimaculatus*; 614 Beobachter) | 1239 | 368 | native ×6 | Meer |
| 19 | *Balistapus undulatus* (507 Beobachter) | 1236 | 1596 | native ×5 | Meer |
| 20 | *Pygoplites diacanthus* (473 Beobachter) | 1201 | 567 | native ×5 | Meer |
| 21 | *Taenianotus triacanthus* (418 Beobachter) | 1197 | 12 | native ×5 | Meer |
| 22 | *Plotosus lineatus* (470 Beobachter) | 1190 | 253 | native ×5 | Brack/Meer |
| 23 | *Plectorhinchus chaetodonoides* (493 Beobachter) | 1174 | 101 | native ×4 | Brack/Meer |
| 24 | *Hippocampus histrix* (348 Beobachter) | 1123 | – | native ×4 | Meer |
| 25 | *Gymnothorax thyrsoideus* (384 Beobachter) | 1116 | 44 | native ×5 | Meer |
| 26 | *Arothron mappa* (499 Beobachter) | 1112 | 10 | native ×4 | Meer |
| 27 | *Rhinomuraena quaesita* (407 Beobachter) | 1107 | – | native ×4 | Meer |
| 28 | *Balistoides viridescens* (535 Beobachter) | 1098 | 153 | native ×4 | Meer |
| 29 | *Dascyllus reticulatus* (419 Beobachter) | 1095 | 684 | native ×5 | Meer |
| 30 | *Halichoeres hortulanus* (391 Beobachter) | 1071 | 703 | native ×4 | Meer |
| 31 | *Chaetodon lunulatus* (432 Beobachter) | 1065 | 504 | native ×4 | Meer |
| 32 | *Chaetodon baronessa* (429 Beobachter) | 1063 | 597 | native ×5 | Meer |
| 33 | *Echidna nebulosa* (511 Beobachter) | 1059 | 147 | native ×5 | Meer |
| 34 | *Thalassoma hardwicke* (429 Beobachter) | 1057 | 698 | native ×5 | Meer |
| 35 | *Odonus niger* (436 Beobachter) | 1044 | 238 | native ×5 | Meer |
| 36 | *Heniochus varius* (430 Beobachter) | 1043 | 399 | native ×5 | Meer |
| 37 | *Scolopsis bilineata* (418 Beobachter) | 1035 | 585 | native ×6 | Meer |
| 38 | *Dendrochirus zebra* (381 Beobachter) | 1031 | 194 | native ×4 | Meer |
| 39 | *Ostracion cubicum* (409 Beobachter) | 999 | 107 | native ×5 | Meer |
| 40 | *Amblyglyphidodon curacao* (397 Beobachter) | 995 | 315 | native ×6 | Meer |
| 220 | *Rhincodon typus* (Highlight; 291 Beobachter) | 381 | 2892 | native ×7 | Meer |
| 681 | *Mobula birostris* (Highlight; 50 Beobachter) | 73 | 38 | native ×4 | Meer |
| 611 | *Mola alexandrini* (Highlight; 73 Beobachter) | 92 | 1 | – | Meer |
| – | *Hippocampus bargibanti* (Highlight; 426 Beobachter) | 1139 | 10 | native ×5 | Meer |
| 218 | *Synchiropus splendidus* (Highlight; 204 Beobachter) | 385 | 30 | native ×5 | Meer |
| 420 | *Hemiscyllium freycineti* (Highlight; 111 Beobachter) | 168 | 14 | native ×2 | Meer |
| 95 | *Metasepia pfefferi* (Highlight; 248 Beobachter) | 638 | – | native ×2 | Meer |
| 253 | *Wunderpus photogenicus* (Highlight; 161 Beobachter) | 335 | – | native ×6 | Meer |

### Level 2 (60)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 41 | *Gymnothorax javanicus* (394 Beobachter) | 993 | 49 | native ×5 | Meer |
| 42 | *Chaetodon vagabundus* (366 Beobachter) | 988 | 708 | native ×4 | Meer |
| 43 | *Pomacentrus moluccensis* (387 Beobachter) | 968 | 478 | native ×6 | Meer |
| 44 | *Labroides dimidiatus* (396 Beobachter) | 957 | 990 | native ×5 | Meer |
| 45 | *Macolor macularis* (339 Beobachter) | 950 | 226 | native ×7 | Meer |
| 46 | *Pomacanthus imperator* (344 Beobachter) | 928 | 94 | native ×5 | Meer |
| 47 | *Amblyglyphidodon aureus* (347 Beobachter) | 924 | 203 | native ×6 | Meer |
| 48 | *Pseudanthias huchtii* (296 Beobachter) | 924 | 442 | native ×5 | Meer |
| 49 | *Paracirrhites forsteri* (338 Beobachter) | 923 | 230 | native ×4 | Meer |
| 50 | *Acanthurus lineatus* (420 Beobachter) | 896 | 1278 | native ×6 | Meer |
| 51 | *Amphiprion frenatus* (340 Beobachter) | 887 | 46 | native ×3 | Meer |
| 52 | *Mobula alfredi* (540 Beobachter) | 880 | 17 | native ×2 | Süß/Meer |
| 53 | *Octopus cyanea* (394 Beobachter) | 866 | 31 | native ×6 | Meer |
| 54 | *Arothron hispidus* (439 Beobachter) | 862 | 242 | native ×5 | Brack/Meer |
| 55 | *Antennarius pictus* (237 Beobachter) | 849 | 5 | native ×3 | Meer |
| 56 | *Chlorurus bleekeri* (295 Beobachter) | 842 | 542 | native ×5 | Meer |
| 57 | *Antennarius maculatus* (286 Beobachter) | 838 | 3 | native ×4 | Meer |
| 58 | *Ostracion meleagris* (385 Beobachter) | 835 | 96 | native ×4 | Meer |
| 59 | *Ctenochaetus striatus* (305 Beobachter) | 821 | 2158 | native ×5 | Meer |
| 60 | *Zebrasoma scopas* (328 Beobachter) | 819 | 1053 | native ×5 | Meer |
| 61 | *Neochirus brachyptera* (262 Beobachter) | 818 | 103 | native ×5 | Meer |
| 62 | *Hemigymnus melapterus* (354 Beobachter) | 803 | 384 | native ×5 | Meer |
| 63 | *Arothron manilensis* (360 Beobachter) | 784 | 202 | native ×5 | Brack/Meer |
| 64 | *Fistularia commersonii* (405 Beobachter) | 784 | 143 | native ×5 | Meer |
| 65 | *Cephalopholis miniata* (292 Beobachter) | 780 | 178 | native ×6 | Meer |
| 66 | *Acanthurus pyroferus* (293 Beobachter) | 777 | 847 | native ×4 | Meer |
| 67 | *Coris gaimard* (275 Beobachter) | 777 | 151 | native ×6 | Meer |
| 68 | *Concholabrus fasciatus* (354 Beobachter) | 771 | 405 | native ×5 | Meer |
| 69 | *Centropyge bicolor* (314 Beobachter) | 768 | 479 | native ×6 | Meer |
| 70 | *Antennarius commerson* (282 Beobachter) | 760 | 3 | native ×3 | Meer |
| 71 | *Carcharhinus melanopterus* (410 Beobachter) | 757 | 157 | native ×6 | Brack/Meer |
| 72 | *Chaetodon rafflesii* (340 Beobachter) | 753 | 376 | native ×4 | Brack/Meer |
| 73 | *Melichthys vidua* (Quelle: *Melichthys vidua × indicus*; 354 Beobachter) | 752 | 449 | native ×5 | Meer |
| 74 | *Dunckerocampus dactyliophorus* (284 Beobachter) | 751 | 177 | native ×3 | Meer |
| 75 | *Taeniura lymma* (403 Beobachter) | 742 | 94 | native ×6 | Meer |
| 76 | *Amphiprion polymnus* (Quelle: *Amphiprion annamensis*; 281 Beobachter) | 741 | 55 | native ×6 | Meer |
| 77 | *Gymnothorax flavimarginatus* (341 Beobachter) | 741 | 97 | native ×3 | Meer |
| 78 | *Caranx melampygus* (352 Beobachter) | 730 | 230 | native ×7 | Brack/Meer |
| 79 | *Pomacentrus coelestis* (279 Beobachter) | 714 | 486 | native ×4 | Meer |
| 80 | *Halichoeres scapularis* (272 Beobachter) | 689 | 225 | native ×6 | Meer |
| 81 | *Naso vlamingii* (294 Beobachter) | 689 | 152 | native ×5 | Meer |
| 82 | *Triaenodon obesus* (347 Beobachter) | 688 | 82 | native ×6 | Meer |
| 83 | *Abudefduf sexfasciatus* (338 Beobachter) | 682 | 94 | native ×6 | Meer |
| 84 | *Neoglyphidodon nigroris* (220 Beobachter) | 680 | 324 | native ×5 | Meer |
| 85 | *Chlorurus spilurus* (238 Beobachter) | 675 | 62 | native ×4 | Meer |
| 86 | *Lutjanus decussatus* (291 Beobachter) | 672 | 182 | native ×5 | Meer |
| 87 | *Plectorhinchus vittatus* (340 Beobachter) | 670 | 94 | native ×6 | Meer |
| 88 | *Rhinecanthus verrucosus* (381 Beobachter) | 670 | 152 | native ×6 | Meer |
| 89 | *Amphiprion sandaracinos* (317 Beobachter) | 665 | 41 | native ×6 | Meer |
| 90 | *Dascyllus aruanus* (335 Beobachter) | 662 | 305 | native ×5 | Meer |
| 91 | *Canthigaster papua* (270 Beobachter) | 651 | – | native ×5 | Meer |
| 92 | *Cirrhitichthys falco* (294 Beobachter) | 646 | 161 | native ×5 | Meer |
| 93 | *Hippocampus kuda* (263 Beobachter) | 643 | 84 | native ×6 | Brack/Meer |
| 94 | *Oxycheilinus bimaculatus* (170 Beobachter) | 643 | 357 | native ×5 | Meer |
| 96 | *Amphioctopus marginatus* (195 Beobachter) | 637 | 51 | native ×4 | Meer |
| 97 | *Cheilinus undulatus* (292 Beobachter) | 635 | 123 | native ×5 | Meer |
| 98 | *Helcogramma striata* (209 Beobachter) | 629 | 188 | native ×5 | Meer |
| 99 | *Scolopsis lineata* (312 Beobachter) | 629 | 138 | native ×6 | Meer |
| 100 | *Balistoides conspicillum* (330 Beobachter) | 627 | 46 | native ×4 | Brack/Meer |
| 101 | *Chaetodon adiergastos* (271 Beobachter) | 626 | 60 | native ×4 | Meer |

### Level 3 (50)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 102 | *Hemitaurichthys polylepis* | 623 | 99 | native ×4 | Meer |
| 103 | *Parupeneus barberinus* | 623 | 444 | native ×6 | Meer |
| 104 | *Aluterus scriptus* | 622 | 81 | native ×5 | Meer |
| 105 | *Chaetodon speculum* | 613 | 40 | native ×5 | Meer |
| 106 | *Gymnothorax fimbriatus* | 612 | 121 | native ×4 | Brack/Meer |
| 107 | *Scarus dimidiatus* | 607 | 373 | native ×6 | Brack/Meer |
| 108 | *Solenostomus cyanopterus* | 603 | 5 | native ×4 | Meer |
| 109 | *Chaetodon octofasciatus* | 602 | 143 | native ×5 | Meer |
| 110 | *Cephalopholis argus* | 601 | 368 | native ×6 | Meer |
| 111 | *Pomacanthus navarchus* | 594 | 46 | native ×5 | Meer |
| 112 | *Chaetodon melannotus* | 591 | 180 | native ×5 | Meer |
| 113 | *Chaetodontoplus mesoleucus* | 591 | 115 | native ×5 | Meer |
| 114 | *Oxycheilinus digramma* | 591 | 380 | native ×5 | Brack/Meer |
| 115 | *Scolopsis margaritifera* | 591 | 275 | native ×6 | Meer |
| 116 | *Siganus vulpinus* | 585 | 220 | native ×5 | Meer |
| 117 | *Platax pinnatus* | 584 | 87 | native ×6 | Meer |
| 118 | *Plectorhinchus lineatus* | 580 | 86 | native ×6 | Meer |
| 119 | *Forcipiger flavissimus* | 577 | 190 | native ×4 | Meer |
| 120 | *Acanthurus nigricans* (Quelle: *Acanthurus nigricans × leucosternon*) | 573 | 238 | native ×5 | Meer |
| 121 | *Bodianus mesothorax* | 573 | 276 | native ×6 | Meer |
| 122 | *Pseudanthias squamipinnis* | 572 | 256 | native ×5 | Meer |
| 123 | *Dischistodus perspicillatus* | 569 | 80 | native ×6 | Brack/Meer |
| 124 | *Platax teira* | 566 | 145 | native ×5 | Meer |
| 125 | *Chaetodon trifascialis* | 565 | 255 | native ×5 | Meer |
| 126 | *Choerodon anchorago* | 556 | 259 | native ×5 | Meer |
| 127 | *Heniochus chrysostomus* | 556 | 240 | native ×4 | Meer |
| 128 | *Parupeneus multifasciatus* | 551 | 756 | native ×5 | Meer |
| 129 | *Centropyge vrolikii* | 550 | 723 | native ×5 | Meer |
| 130 | *Lactoria fornasini* | 550 | 13 | native ×2 | Meer |
| 131 | *Synodus variegatus* | 549 | 502 | native ×4 | Meer |
| 132 | *Nemateleotris magnifica* | 548 | 71 | native ×5 | Meer |
| 133 | *Caranx sexfasciatus* | 547 | 351 | native ×7 | Süß/Brack/Meer |
| 134 | *Sepioteuthis lessoniana* | 540 | 53 | native ×6 | Brack/Meer |
| 135 | *Plectorhinchus polytaenia* | 539 | 7 | native ×5 | Meer |
| 136 | *Bodianus dictynna* | 533 | 7 | native ×6 | Meer |
| 137 | *Cheilinus chlorourus* | 529 | 277 | native ×6 | Meer |
| 138 | *Cephalopholis cyanostigma* | 520 | 247 | native ×6 | Meer |
| 139 | *Caesio caerulaurea* | 514 | 401 | native ×6 | Meer |
| 140 | *Pentapodus trivittatus* | 512 | 58 | native ×6 | Meer |
| 141 | *Pomacentrus amboinensis* | 512 | 466 | native ×5 | Meer |
| 142 | *Amblyglyphidodon leucogaster* | 511 | 215 | native ×4 | Meer |
| 143 | *Dischistodus melanotus* | 506 | 55 | native ×6 | Meer |
| 144 | *Amphiprion melanopus* | 503 | 78 | native ×5 | Meer |
| 145 | *Mirolabrichthys tuka* | 503 | 161 | native ×5 | Meer |
| 146 | *Diodon hystrix* | 500 | 44 | native ×5 | Meer |
| 147 | *Plagiotremus rhinorhynchos* | 500 | 174 | native ×5 | Meer |
| 148 | *Epinephelus merra* | 499 | 536 | native ×6 | Meer |
| 149 | *Valenciennea puellaris* | 498 | 80 | native ×5 | Meer |
| 150 | *Cymbacephalus beauforti* | 495 | – | native ×4 | Meer |
| 151 | *Sufflamen chrysopterum* | 495 | 269 | native ×4 | Meer |

## Grenzfälle

Je 10 Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels sie nehmen (Highlights ab Level 2 übersprungen).

### Level 1/2

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 31 | *Chaetodon lunulatus* (432 Beobachter) | 1065 | 504 | native ×4 | Meer | 1 |
| 32 | *Chaetodon baronessa* (429 Beobachter) | 1063 | 597 | native ×5 | Meer | 1 |
| 33 | *Echidna nebulosa* (511 Beobachter) | 1059 | 147 | native ×5 | Meer | 1 |
| 34 | *Thalassoma hardwicke* (429 Beobachter) | 1057 | 698 | native ×5 | Meer | 1 |
| 35 | *Odonus niger* (436 Beobachter) | 1044 | 238 | native ×5 | Meer | 1 |
| 36 | *Heniochus varius* (430 Beobachter) | 1043 | 399 | native ×5 | Meer | 1 |
| 37 | *Scolopsis bilineata* (418 Beobachter) | 1035 | 585 | native ×6 | Meer | 1 |
| 38 | *Dendrochirus zebra* (381 Beobachter) | 1031 | 194 | native ×4 | Meer | 1 |
| 39 | *Ostracion cubicum* (409 Beobachter) | 999 | 107 | native ×5 | Meer | 1 |
| 40 | *Amblyglyphidodon curacao* (397 Beobachter) | 995 | 315 | native ×6 | Meer | 1 |
| | **Grenze** | | | | | |
| 41 | *Gymnothorax javanicus* (394 Beobachter) | 993 | 49 | native ×5 | Meer | 2 |
| 42 | *Chaetodon vagabundus* (366 Beobachter) | 988 | 708 | native ×4 | Meer | 2 |
| 43 | *Pomacentrus moluccensis* (387 Beobachter) | 968 | 478 | native ×6 | Meer | 2 |
| 44 | *Labroides dimidiatus* (396 Beobachter) | 957 | 990 | native ×5 | Meer | 2 |
| 45 | *Macolor macularis* (339 Beobachter) | 950 | 226 | native ×7 | Meer | 2 |
| 46 | *Pomacanthus imperator* (344 Beobachter) | 928 | 94 | native ×5 | Meer | 2 |
| 47 | *Amblyglyphidodon aureus* (347 Beobachter) | 924 | 203 | native ×6 | Meer | 2 |
| 48 | *Pseudanthias huchtii* (296 Beobachter) | 924 | 442 | native ×5 | Meer | 2 |
| 49 | *Paracirrhites forsteri* (338 Beobachter) | 923 | 230 | native ×4 | Meer | 2 |
| 50 | *Acanthurus lineatus* (420 Beobachter) | 896 | 1278 | native ×6 | Meer | 2 |

### Level 2/3

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 91 | *Canthigaster papua* (270 Beobachter) | 651 | – | native ×5 | Meer | 2 |
| 92 | *Cirrhitichthys falco* (294 Beobachter) | 646 | 161 | native ×5 | Meer | 2 |
| 93 | *Hippocampus kuda* (263 Beobachter) | 643 | 84 | native ×6 | Brack/Meer | 2 |
| 94 | *Oxycheilinus bimaculatus* (170 Beobachter) | 643 | 357 | native ×5 | Meer | 2 |
| 96 | *Amphioctopus marginatus* (195 Beobachter) | 637 | 51 | native ×4 | Meer | 2 |
| 97 | *Cheilinus undulatus* (292 Beobachter) | 635 | 123 | native ×5 | Meer | 2 |
| 98 | *Helcogramma striata* (209 Beobachter) | 629 | 188 | native ×5 | Meer | 2 |
| 99 | *Scolopsis lineata* (312 Beobachter) | 629 | 138 | native ×6 | Meer | 2 |
| 100 | *Balistoides conspicillum* (330 Beobachter) | 627 | 46 | native ×4 | Brack/Meer | 2 |
| 101 | *Chaetodon adiergastos* (271 Beobachter) | 626 | 60 | native ×4 | Meer | 2 |
| | **Grenze** | | | | | |
| 102 | *Hemitaurichthys polylepis* | 623 | 99 | native ×4 | Meer | 3 |
| 103 | *Parupeneus barberinus* | 623 | 444 | native ×6 | Meer | 3 |
| 104 | *Aluterus scriptus* | 622 | 81 | native ×5 | Meer | 3 |
| 105 | *Chaetodon speculum* | 613 | 40 | native ×5 | Meer | 3 |
| 106 | *Gymnothorax fimbriatus* | 612 | 121 | native ×4 | Brack/Meer | 3 |
| 107 | *Scarus dimidiatus* | 607 | 373 | native ×6 | Brack/Meer | 3 |
| 108 | *Solenostomus cyanopterus* | 603 | 5 | native ×4 | Meer | 3 |
| 109 | *Chaetodon octofasciatus* | 602 | 143 | native ×5 | Meer | 3 |
| 110 | *Cephalopholis argus* | 601 | 368 | native ×6 | Meer | 3 |
| 111 | *Pomacanthus navarchus* | 594 | 46 | native ×5 | Meer | 3 |

### Level 3/nicht im Deck

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 142 | *Amblyglyphidodon leucogaster* | 511 | 215 | native ×4 | Meer | 3 |
| 143 | *Dischistodus melanotus* | 506 | 55 | native ×6 | Meer | 3 |
| 144 | *Amphiprion melanopus* | 503 | 78 | native ×5 | Meer | 3 |
| 145 | *Mirolabrichthys tuka* | 503 | 161 | native ×5 | Meer | 3 |
| 146 | *Diodon hystrix* | 500 | 44 | native ×5 | Meer | 3 |
| 147 | *Plagiotremus rhinorhynchos* | 500 | 174 | native ×5 | Meer | 3 |
| 148 | *Epinephelus merra* | 499 | 536 | native ×6 | Meer | 3 |
| 149 | *Valenciennea puellaris* | 498 | 80 | native ×5 | Meer | 3 |
| 150 | *Cymbacephalus beauforti* | 495 | – | native ×4 | Meer | 3 |
| 151 | *Sufflamen chrysopterum* | 495 | 269 | native ×4 | Meer | 3 |
| | **Grenze** | | | | | |
| 152 | *Thalassoma amblycephalum* | 488 | 561 | native ×5 | Meer | – |
| 153 | *Lutjanus biguttatus* | 485 | 193 | native ×7 | Meer | – |
| 154 | *Epinephelus fasciatus* | 483 | 251 | native ×6 | Brack/Meer | – |
| 155 | *Chaetodon ornatissimus* | 481 | 220 | native ×4 | Meer | – |
| 156 | *Chaetodon lunula* | 475 | 169 | native ×4 | Meer | – |
| 157 | *Cyclichthys orbicularis* | 475 | 79 | native ×4 | Meer | – |
| 158 | *Cetoscarus ocellatus* | 471 | 92 | native ×6 | Meer | – |
| 159 | *Ostracion solorense* | 471 | 12 | native ×4 | Meer | – |
| 160 | *Pomacentrus bankanensis* | 471 | 377 | native ×5 | Meer | – |
| 161 | *Sargocentron caudimaculatum* | 470 | 307 | native ×5 | Meer | – |

## Abgleich mit Führern

Das Rezept nennt keinen Führer.
## Änderungen gegenüber dem bestehenden Deck

- neu: 0
- entfallen: 0

## Ausgeschlossene Kandidaten

<details><summary>1486 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Hippocampus bargibanti* | 1139 | Meer | zu klein (höchstens 2.4 cm) |
| *Hippocampus denise* | 451 | Meer | zu klein (höchstens 2.15 cm) |
| *Hippocampus pontohi* | 367 | Meer | zu klein (höchstens 1.69 cm) |
| *Euprymna berryi* | 352 | Meer | zu klein (höchstens 3 cm) |
| *Eviota atriventris* | 328 | Meer | zu klein (höchstens 1.71 cm) |
| *Asterropteryx striata* | 249 | Meer | zu klein (höchstens 2.32 cm) |
| *Channa striata* | 245 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia reticulata* | 239 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota sebreei* | 227 | Meer | zu klein (höchstens 2.5 cm) |
| *Toxotes jaculatrix* | 227 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma benjamini* | 221 | Meer | zu klein (höchstens 3 cm) |
| *Bryaninops yongei* | 220 | Meer | zu klein (höchstens 3.5 cm) |
| *Barbodes binotatus* | 191 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oreochromis niloticus* | 168 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma halonevum* | 168 | Meer | zu klein (höchstens 3 cm) |
| *Trichopodus trichopterus* | 166 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bryaninops natans* | 161 | Meer | zu klein (höchstens 2.5 cm) |
| *Trimma cana* | 159 | Meer | zu klein (höchstens 2.45 cm) |
| *Pleurosicya mossambica* | 141 | Meer | zu klein (höchstens 3 cm) |
| *Fusigobius melacron* | 135 | Meer | zu klein (höchstens 3.52 cm) |
| *Channa limbata* | 129 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anabas testudineus* | 125 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hazeus profusus* | 111 | Meer | zu klein (höchstens 2.86 cm) |
| *Eviota teresae* | 107 | Meer | zu klein (höchstens 2.11 cm) |
| *Eviota bifasciata* | 96 | Meer | zu klein (höchstens 3.5 cm) |
| *Eviota fallax* | 96 | Meer | zu klein (höchstens 1.81 cm) |
| *Ecsenius bandanus* | 94 | Meer | zu klein (höchstens 3.4 cm) |
| *Trimma yanoi* | 93 | Meer | zu klein (höchstens 2.18 cm) |
| *Xiphophorus hellerii* | 90 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ecsenius trilineatus* | 83 | Meer | zu klein (höchstens 3 cm) |
| *Oreochromis mossambicus* | 81 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota pictifacies* | 80 | Meer | zu klein (höchstens 1.56 cm) |
| *Monopterus javanensis* | 80 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudorhombus dupliciocellatus* | 80 | Meer | nur tiefer als die Tauchgrenze (erst ab 50 m) |
| *Trimma anaima* | 73 | Meer | zu klein (höchstens 3 cm) |
| *Trimma striatum* | 72 | Meer | zu klein (höchstens 3 cm) |
| *Eviota rubrisparsa* | 68 | Meer | zu klein (höchstens 1.95 cm) |
| *Oxyeleotris marmorata* | 68 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Foa fo* | 67 | Meer | zu klein (höchstens 3.5 cm) |
| *Gambusia affinis* | 65 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinus rubrofuscus* | 63 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota prasites* | 63 | Meer | zu klein (höchstens 3 cm) |
| *Clarias gariepinus* | 62 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osteochilus vittatus* | 62 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma hollemani* | 60 | Meer | zu klein (höchstens 2.76 cm) |
| *Trimma stobbsi* | 57 | Meer | zu klein (höchstens 2.5 cm) |
| *Ecsenius dilemma* | 54 | Meer | zu klein (höchstens 3.1 cm) |
| *Hampala macrolepidota* | 54 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora argyrotaenia* | 54 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma rubromaculatum* | 54 | Meer | zu klein (höchstens 3.5 cm) |
| *Trimma nasa* | 53 | Meer | zu klein (höchstens 2.25 cm) |
| *Oryzias javanicus* | 52 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trichopsis vittata* | 52 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ecsenius prooculis* | 51 | Meer | zu klein (höchstens 3.95 cm) |
| *Eviota ancora* | 51 | Meer | zu klein (höchstens 1.4 cm) |
| *Pleurosicya micheli* | 51 | Meer | zu klein (höchstens 2.5 cm) |
| *Rasbora einthovenii* | 51 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sepiadarium kochii* | 51 | Meer | nur tiefer als die Tauchgrenze (erst ab 60 m) |
| *Eviota nigriventris* | 49 | Meer | zu klein (höchstens 3 cm) |
| *Discotrema monogrammum* | 48 | Meer | zu klein (höchstens 2.32 cm) |
| *Trimma taylori* | 48 | Meer | zu klein (höchstens 3.5 cm) |
| *Channa lucius* | 47 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Idiosepius pygmaeus* | 47 | Brack/Meer | zu klein (höchstens 1.517 cm) |
| *Trimma haimassum* | 47 | Meer | zu klein (höchstens 3.09 cm) |
| *Tomiyamichthys alleni* | 45 | Meer | zu klein (höchstens 3.8 cm) |
| *Amphilophus labiatus* | 44 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota sigillata* | 44 | Meer | zu klein (höchstens 3 cm) |
| *Lotilia klausewitzi* | 44 | Meer | zu klein (höchstens 2.71 cm) |
| *Barbodes sealei* | 43 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma macrophthalmus* | 43 | Meer | zu klein (höchstens 2.5 cm) |
| *Belontia hasselti* | 42 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta edithae* | 41 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma naudei* | 41 | Meer | zu klein (höchstens 3.5 cm) |
| *Trimma lantana* | 39 | Meer | zu klein (höchstens 2.94 cm) |
| *Chrysiptera cymatilis* | 38 | Meer | zu klein (höchstens 3.62 cm) |
| *Dichotomyctere nigroviridis* | 38 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ecsenius shirleyae* | 38 | Meer | zu klein (höchstens 2.84 cm) |
| *Nemacheilus chrysolaimos* | 38 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Asterropteryx bipunctata* | 37 | Meer | zu klein (höchstens 3.11 cm) |
| *Clarias leiacanthus* | 37 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acanthosphex leurynnis* | 36 | Meer | zu klein (höchstens 3.1 cm) |
| *Luciocephalus pulcher* | 36 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora cephalotaenia* | 36 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Channa micropeltes* | 35 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinus carpio* | 35 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Fusigobius aureus* | 35 | Meer | zu klein (höchstens 3.48 cm) |
| *Barbonymus gonionotus* | 34 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Clarias batrachus* | 34 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Tomiyamichthys nudus* | 33 | Meer | zu klein (höchstens 3.34 cm) |
| *Cyclocheilichthys apogon* | 32 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osphronemus goramy* | 31 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pleurosicya labiata* | 31 | Meer | zu klein (höchstens 3.5 cm) |
| *Puntigrus tetrazona* | 31 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gastromyzon lepidogaster* | 30 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora elegans* | 30 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Striuntius lateristriga* | 30 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Helostoma temminckii* | 29 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Systomus rubripinnis* | 29 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hazeus maculipinna* | 28 | Meer | zu klein (höchstens 3.73 cm) |
| *Trigonopoma gracile* | 28 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nandus nebulosus* | 27 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Barbonymus balleroides* | 26 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemirhamphodon pogonognathus* | 26 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Abdopus abaculus* | 25 | Meer | zu klein (höchstens 3.3 cm) |
| *Glyptothorax platypogon* | 25 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mystus singaringan* | 25 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora baliensis* | 25 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Tomiyamichthys emilyae* | 25 | Meer | zu klein (höchstens 3.24 cm) |
| *Trichopodus leerii* | 25 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrognathus maculatus* | 24 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nematabramis everetti* | 24 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rudarius excelsus* | 24 | Meer | zu klein (höchstens 2.5 cm) |
| *Gnatholepis yoshinoi* | 23 | Meer | zu klein (höchstens 3.13 cm) |
| *Rasbora aprotaenia* | 23 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sphaerichthys osphromenoides* | 22 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma fangi* | 22 | Meer | zu klein (höchstens 2.05 cm) |
| *Hazeus atrispinalis* | 21 | ? | zu klein (höchstens 3.18 cm) |
| *Trigonopoma pauciperforatum* | 21 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Barbonymus schwanefeldii* | 20 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Desmopuntius johorensis* | 20 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota latifasciata* | 20 | Meer | zu klein (höchstens 1.5 cm) |
| *Hampala sabana* | 20 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Desmopuntius gemellus* | 19 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ecsenius caeruliventris* | 19 | Meer | zu klein (höchstens 2.43 cm) |
| *Hemibagrus capitulum* | 19 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nemacheilus fasciatus* | 19 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Periophthalmodon septemradiatus* | 19 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Spirula spirula* | 19 | Meer | nur tiefer als die Tauchgrenze (erst ab 100 m) |
| *Hemibagrus planiceps* | 18 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lepidocephalichthys hasselti* | 18 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pristolepis grootii* | 18 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Toxotes chatareus* | 18 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Channa bankanensis* | 17 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mene maculata* | 17 | Brack/Meer | nur tiefer als die Tauchgrenze (erst ab 50 m) |
| *Pteropsaron springeri* | 17 | Meer | zu klein (höchstens 2.75 cm) |
| *Alectis ciliaris* | 16 | Meer | nur tiefer als die Tauchgrenze (erst ab 60 m) |
| *Bryaninops tigris* | 16 | Meer | zu klein (höchstens 2.45 cm) |
| *Eviota longirostris* | 16 | Meer | zu klein (höchstens 1.78 cm) |
| *Melanochromis auratus* | 16 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pangio semicincta* | 16 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Piaractus brachypomus* | 16 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Protomyzon whiteheadi* | 16 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora trilineata* | 16 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Stiphodon semoni* | 16 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amatitlania nigrofasciata* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta raja* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Desmopuntius hexazona* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Glaniopsis hanitschi* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parachromis managuensis* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora kalochroma* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora tornieri* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trichopodus pectoralis* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma flavatrum* | 15 | Meer | zu klein (höchstens 2.3 cm) |
| *Channa pleurophthalma* | 14 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Chrysiptera arnazae* | 14 | Meer | zu klein (höchstens 3.91 cm) |
| *Eviotops storthynx* | 14 | Meer | zu klein (höchstens 2.5 cm) |
| *Grallenia baliensis* | 14 | Meer | zu klein (höchstens 1.48 cm) |
| *Lentipes palawanirufus* | 14 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora lateristriata* | 14 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Wallagonia leerii* | 14 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta anabatoides* | 13 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gobiodon okinawae* | 13 | Meer | zu klein (höchstens 3.5 cm) |
| *Labiobarbus leptocheilus* | 13 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora dusonensis* | 13 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rhinolepadichthys geminus* | 13 | Meer | zu klein (höchstens 2.7 cm) |
| *Betta ocellata* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta picta* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Carassius auratus* | 12 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ecsenius taeniatus* | 12 | Meer | zu klein (höchstens 3.2 cm) |
| *Eviota raja* | 12 | Meer | zu klein (höchstens 2.38 cm) |
| *Gobiodon prolixus* | 12 | Meer | zu klein (höchstens 3.21 cm) |
| *Hemibagrus nemurus* | 12 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Kuhlia marginata* | 12 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mayaheros urophthalmus* | 12 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osteochilus spilurus* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parachela hypophthalmus* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sueviota bryozophila* | 12 | Meer | zu klein (höchstens 1.32 cm) |
| *Trimma annosum* | 12 | Meer | zu klein (höchstens 2.8 cm) |
| *Aseraggodes albidus* | 11 | Meer | zu klein (höchstens 2.93 cm) |
| *Betta cracens* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta pugnax* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Clarias nieuhofii* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota shimadai* | 11 | Meer | zu klein (höchstens 1.56 cm) |
| *Hazeus ammophilus* | 11 | Meer | zu klein (höchstens 3.34 cm) |
| *Kryptopterus macrocephalus* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paragobiodon modestus* | 11 | Meer | zu klein (höchstens 3.5 cm) |
| *Syncrossus hymenophysa* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Grallenia ornata* | 10 | ? | zu klein (höchstens 1.35 cm) |
| *Mystus castaneus* | 10 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mystus nigriceps* | 10 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osteochilus melanopleura* | 10 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pao palembangensis* | 10 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Puntioplites bulu* | 10 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Puntius brevis* | 10 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Asterropteryx atripes* | 9 | Meer | zu klein (höchstens 2.19 cm) |
| *Bathygobius mero* | 9 | Meer | zu klein (höchstens 3.6 cm) |
| *Betta coccina* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta spilotogena* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brevibora cheeya* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Chaca bankanensis* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Festucalex rufus* | 9 | Meer | zu klein (höchstens 3.63 cm) |
| *Luposicya lupus* | 9 | Meer | zu klein (höchstens 3.5 cm) |
| *Mystus bimaculatus* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nemacheilus selangoricus* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nomorhamphus celebensis* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ompok fumidus* | 9 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora myersi* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rhinogobius similis* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Silurichthys indragiriensis* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma erdmanni* | 9 | Meer | zu klein (höchstens 2.62 cm) |
| *Amphilophus citrinellus* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Asterropteryx ensifera* | 8 | Brack/Meer | zu klein (höchstens 3 cm) |
| *Bagarius lica* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bagroides melapterus* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Belobranchus segura* | 8 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta falx* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Esomus metallicus* | 8 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota brahmi* | 8 | Meer | zu klein (höchstens 1.68 cm) |
| *Eviota queenslandica* | 8 | Meer | zu klein (höchstens 2.4 cm) |
| *Eviota rubriceps* | 8 | Meer | zu klein (höchstens 1.35 cm) |
| *Garra borneensis* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Grallenia rubrilineata* | 8 | Meer | zu klein (höchstens 1.52 cm) |
| *Iniistius bakunawa* | 8 | Meer | nur tiefer als die Tauchgrenze (erst ab 54 m) |
| *Leptobarbus hoevenii* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Luciosoma setigerum* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Melanotaenia fredericki* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mugilogobius sarasinorum* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Notopterus notopterus* | 8 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osteochilus waandersii* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ostorhinchus neotes* | 8 | Meer | zu klein (höchstens 2.7 cm) |
| *Pangasianodon hypophthalmus* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paragobiodon melanosoma* | 8 | Meer | zu klein (höchstens 3.5 cm) |
| *Puntioplites waandersi* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Stiphodon pulchellus* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trigonostigma heteromorpha* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma caudomaculatum* | 8 | Meer | zu klein (höchstens 2.69 cm) |
| *Upeneus guttatus* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Xiphophorus maculatus* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amblygobius cheraphilus* | 7 | Meer | zu klein (höchstens 2.74 cm) |
| *Apterygocampus epinnulatus* | 7 | Meer | zu klein (höchstens 3 cm) |
| *Channa marulioides* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Chonerhinos naritus* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota maculosa* | 7 | Meer | zu klein (höchstens 1.79 cm) |
| *Lentipes ikeae* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Luciosoma pellegrinii* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mastacembelus erythrotaenia* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mastacembelus unicolor* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Meiacanthus limbatus* | 7 | Meer | zu klein (höchstens 3.7 cm) |
| *Mystus gulio* | 7 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pristolepis fasciata* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora caudimaculata* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Solenostomus snuffleupagus* | 7 | ? | zu klein (höchstens 3.51 cm) |
| *Stiphodon aureofuscus* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sueviota lachneri* | 7 | Meer | zu klein (höchstens 2.1 cm) |
| *Telmatherina antoniae* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Vanderhorstia cyanolineata* | 7 | Meer | zu klein (höchstens 2.41 cm) |
| *Auxis thazard* | 6 | Meer | nur tiefer als die Tauchgrenze (erst ab 50 m) |
| *Belobranchus belobranchus* | 6 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta hipposideros* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bryaninops earlei* | 6 | Meer | zu klein (höchstens 1.4 cm) |
| *Chitala ornata* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Dermogenys bispina* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Dermogenys orientalis* | 6 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Discordipinna vibrissa* | 6 | ? | zu klein (höchstens 1.1 cm) |
| *Eviota bella* | 6 | ? | zu klein (höchstens 1.91 cm) |
| *Favonigobius opalescens* | 6 | Brack/Meer | zu klein (höchstens 2.5 cm) |
| *Hipposcorpaena filamentosa* | 6 | Meer | zu klein (höchstens 3.52 cm) |
| *Lentipes mindanaoensis* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neohomaloptera johorensis* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oryzias orthognathus* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osphronemus laticlavius* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oxygaster anomalura* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parioglossus philippinus* | 6 | Brack/Meer | zu klein (höchstens 3.5 cm) |
| *Priolepis vexilla* | 6 | Meer | zu klein (höchstens 1.94 cm) |
| *Pseudapocryptes elongatus* | 6 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora bankanensis* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rhinogobius estrellae* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sicyopus rubicundus* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Stigmatogobius pleurostigma* | 6 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Stiphodon palawanensis* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Stiphodon rutilaureus* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Thynnichthys thynnoides* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma marinae* | 6 | Meer | zu klein (höchstens 2 cm) |
| *Adrianichthys oophorus* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Aioliops novaeguineae* | 5 | Meer | zu klein (höchstens 2.3 cm) |
| *Ancistrogobius yanoi* | 5 | Meer | zu klein (höchstens 3.68 cm) |
| *Aphareus rutilans* | 5 | Meer | nur tiefer als die Tauchgrenze (erst ab 100 m) |
| *Betta pinguis* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta simorum* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bryaninops annella* | 5 | Meer | zu klein (höchstens 2.66 cm) |
| *Chitala hypselonotus* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Chitala lopis* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Dermogenys palawanensis* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Desmopuntius rhomboocellatus* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Etroplus suratensis* | 5 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota algida* | 5 | Meer | zu klein (höchstens 1.65 cm) |
| *Eviota imitata* | 5 | Meer | zu klein (höchstens 1.39 cm) |
| *Eviota melasma* | 5 | Meer | zu klein (höchstens 3 cm) |
| *Fluvitrygon signifer* | 5 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemirhamphodon phaiosoma* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hippocampus satomiae* | 5 | Meer | zu klein (höchstens 1.38 cm) |
| *Kottelatlimia pristes* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Leptobarbus melanotaenia* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lobulogobius morrigu* | 5 | Meer | zu klein (höchstens 3.1 cm) |
| *Luciocephalus aura* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Luciosoma trinema* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrognathus aculeatus* | 5 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ompok siluroides* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osteochilus bleekeri* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parachela oxygastroides* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parosphromenus gunawani* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia sphenops* | 5 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Psammogobius pisinnus* | 5 | Meer | zu klein (höchstens 1.79 cm) |
| *Pseudomystus heokhuii* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Redigobius oyensi* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sicyopus auxilimentus* | 5 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sphaerichthys selatanensis* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sundadanio goblinus* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Telmatherina sarasinorum* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Tor tambroides* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma hoesei* | 5 | Meer | zu klein (höchstens 2.4 cm) |
| *Trimmatom sagma* | 5 | Meer | zu klein (höchstens 2.1 cm) |
| *Xenanthias longimanus* | 5 | Meer | zu klein (höchstens 3.5 cm) |
| *Xenentodon canciloides* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acantopsis dialuzona* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acentrogobius cenderawasih* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Adelotremus deloachi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Aioliops megastigma* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Alepes kleinii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Amblycirrhitus bimacula* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Amblygaster sirm* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Anampses lineatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Andamia heteroptera* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Andinoacara rivulatus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Antennarius biocellatus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Apogonichthyoides timorensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ariosoma anagoides* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Atherinomorus endrachtensis* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Aurigequula fasciata* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Aurigequula longispinis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Auxis rochei* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Awaous grammepomus* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Barbichthys laevis* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Belodontichthys dinema* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta balunga* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta splendens* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bodianus diana* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Boraras maculatus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brevibora dorsiocellata* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Callionymus superbus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Channa melasoma* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Chlorurus strongylocephalus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Chromobotia macracanthus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cirrhilabrus walindi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cirripectes filamentosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Corythoichthys conspicillatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Crossocheilus oblongus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ctenochaetus truncatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Dawkinsia filamentosa* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Dermogenys sumatrana* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Doryrhamphus melanopleura* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Eleutheronema tetradactylum* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Entomacrodus striatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Epinephelus bleekeri* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Epinephelus miliaris* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Etelis radiosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Eumegistus illustris* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Eviotops infulatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Eviota korechika* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Eviota prasina* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Eviota punyit* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Festucalex kulbickii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Glossogobius giuris* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Gobiopterus chuno* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gymnocranius griseus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gymnothorax breedeni* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gymnothorax castlei* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gymnothorax margaritophorus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gymnothorax nudivomer* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gymnothorax paucivertebralis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gymnura poecilura* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Halicampus mataafae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Halichoeres kneri* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Halichoeres leucoxanthus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Halichoeres zeylonicus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Halophryne hutchinsi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hemiscyllium hallstromi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lentipes whittenorum* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lethrinus amboinensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lutjanus fuscescens* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lutjanus papuensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Macrochirichthys macrochirus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Maculabatis macrura* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Manonichthys paranox* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Mastacembelus notophthalmus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Micrognathus andersonii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Micrognathus pygmaeus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Microphis arrakisae* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Microphis manadensis* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mugilogobius rexi* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nemacheilus pfeifferae* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nemanthias ignitus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Nemipterus bathybius* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Neolissochilus soroides* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neopomacentrus australicus* | 4 | ? | zu wenige Nachweise (4 < 5) |
| *Nomorhamphus kolonodalensis* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oliotius oligolepis* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oreochromis aureus* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osteochilus kahajanensis* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osteochilus microcephalus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Otolithes ruber* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Pao leiurus* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parambassis wolffii* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parioglossus nudus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Parioglossus rainfordi* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Pelates quadrilineatus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Pentapodus paradiseus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Planiliza subviridis* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Platycephalus indicus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Plectroglyphidodon obreptus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Poecilia latipinna* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Pomacentrus albimaculus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pomacentrus melanochir* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pomacentrus opisthostigma* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pomacentrus taeniometopon* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Pristigenys meyeri* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pseudochromis flavopunctatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pteragogus guttatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Puntigrus anchisporus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora jacobsoni* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora paucisqualis* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora sarawakensis* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rastrelliger faughni* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Redigobius bikolanus* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Redigobius tambujon* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Rhizoprionodon oligolinx* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Rhynchobatus palpebratus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sardinella lemuru* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scomber australasicus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Siganus randalli* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sillago sihama* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Silurichthys phaiosoma* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Siphamia corallicola* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sphyrna mokarran* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Spratelloides delicatulus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Stenogobius genivittatus* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Stiphodon surrufus* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Strongylura urvillii* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Synchiropus bartelsi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Takifugu oblongus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Tetraroge nigra* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Thyrsitoides marleyi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Tomiyamichthys gomezi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Trimma cheni* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Trimma xanthochrum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Trimmatom pharus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Upeneus heterospinus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Urogymnus polylepis* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Uropterygius macrocephalus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Uropterygius mactanensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Valenciennea limicola* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Verulux solmaculata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Wetmorella albofasciata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Zebrasoma desjardinii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Zebrias zebra* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Zoramia perlita* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Acanthopagrus berda* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Acanthopagrus pacificus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Acentrogobius viridipunctatus* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Aetomylaeus vespertilio* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Alopias superciliosus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ambassis buruensis* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amblyglyphidodon silolona* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Amphilophus trimaculatus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anacanthus barbatus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Anaora tentaculata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ancistrocheirus lesueurii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cyclocheilichthys repasson* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anomalops katoptron* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Apogon doryssa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Atelomycterus baliensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Atropus hedlandensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Barbodes banksi* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bathygobius petrophilus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Benthosema fibulatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Betta obscura* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Blenniella bilitonensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Brachygobius doriae* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bryaninops erythrops* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bulbonaricus brucei* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Butis amboinensis* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Callionymus enneactis* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Canthigaster leoparda* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Caracanthus unipinna* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Carcharhinus brevipinna* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Carcharhinus macloti* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chaetodon madagaskariensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chaetodon triangulum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chaetodon xanthocephalus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chanda siamensis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cheilodipterus zonatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chelmon marginalis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chrysiptera ellenae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cookeolus japonicus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cryptocentrus altipinna* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dactyloptena macracantha* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Datnioides microlepis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Datnioides polota* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Decapterus kurroides* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dentex hypselosomus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Desmopuntius trifasciatus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Echinogobius hayashii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ecsenius kurti* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ecsenius similis* | 3 | ? | zu wenige Nachweise (3 < 5) |
| *Eirmotus furvus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Encheloclarias velatus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Enchelycore bayeri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Epinephelus erythrurus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Fibramia amboinensis* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Fowleria flammea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Fowleria variegata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gastromyzon monticola* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Giuris margaritaceus* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Glossamia timika* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Glossogobius aureus* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Glossogobius celebius* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Glossogobius matanensis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gobiodon ceramensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gobiodon histrio* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gyrinocheilus pustulosus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Halichoeres chrysotaenia* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hampala bimaculata* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Helcogramma atauroensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Himantura undulata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hippocampus waleananus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hoplolatilus fourmanoiri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hoplolatilus marcosi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hoplolatilus randalli* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Istigobius spence* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Kelloggella cardinalis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Labeo chrysophekadion* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Labiobarbus ocellatus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Labropsis australis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lagocephalus spadiceus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Lagusia micracanthus* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lentipes armatus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Liopropoma multilineatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lobocheilos falcifer* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lubbockichthys multisquamatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lutjanus goldiei* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Lutjanus indicus* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Mimoblennius atrocinctus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mirolabrichthys pascalus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Muraenesox bagio* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Myrichthys paleracio* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mystus abbreviatus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nemipterus isacanthus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Nemipterus japonicus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Nemipterus nematophorus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Nemipterus tambuloides* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Nemipterus zysron* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Neoglyphidodon bonang* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Neoniphon aurolineatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Neopomacentrus filamentosus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Netuma bilineata* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Netuma thalassina* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Nibea soldado* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Nomorhamphus rex* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ophiocara gigas* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Oryzias hubbsi* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oryzias kalimpaaensis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oryzias matanensis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oryzias sarasinorum* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osteoglossum bicirrhosum* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ostorhinchus cavitensis* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Ostorhinchus selas* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Oxyeleotris fimbriata* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oxymetopon cyanoctenosum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paedocypris carbunculus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pampus argenteus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pandaka rouxi* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pangasius kunyit* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pangasius polyuranodon* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pangio muraeniformis* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pao hilgendorfii* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parablennius thysanius* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paracentropogon zonatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paracheilinus rennyae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paragobiodon lacunicola* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paramonacanthus pusillus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Parapercis multiplicata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Parascorpaena poseidon* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Parosphromenus sumatranus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parupeneus spilurus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Pectenocypris micromysticetus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pentapodus numberii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Photopectoralis bindus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Pictichromis caitlinae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Platybelone platyura* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Platycaranx chrysophrys* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Plectroglyphidodon johnstonianus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pomacentrus littoralis* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Priacanthus tayenus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Priolepis semidoliata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pristipomoides multidens* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pseudojuloides severnsi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ptereleotris monoptera* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pycnochromis fieldi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pycnochromis vanderbilti* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rasbora everetti* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora hubbsi* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora vulcanus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Remora remora* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rhinecanthus lunula* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rhinoptera jayakari* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rogadius pristiger* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sardinella tawilis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Scarus fuscocaudalis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Scarus globiceps* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Schizothorax richardsonii* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Scoliodon macrorhynchos* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Scolopsis vosmeri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Scomberoides tala* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Scorpaenodes guamensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Scorpaenopsis possi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sicyopterus microcephalus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sicyopterus ocellaris* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Siphamia fuscolineata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Siphamia jebbi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sphyraena helleri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Spratelloides gracilis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Stalix histrio* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Stenogobius gymnopomus* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Stiphodon maculidorsalis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Stiphodon ornatus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Stonogobiops yasha* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Strongylura leiurus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Sunagocia arenicola* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Thryssa samam* | 3 | ? | zu wenige Nachweise (3 < 5) |
| *Tor tambra* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Triacanthus nieuhofii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Trimma okinawae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Trimma papayum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Trimma trioculatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Upeneus moluccensis* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Upeneus sulphureus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Uraspis helvola* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Uropterygius hades* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Zebrias quagga* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Abantennarius dorehensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ablennes hians* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Acentrogobius janthinopterus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Acrochordonichthys rugosus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Adrianichthys poptae* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Albulichthys albuloides* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Alepes djedaba* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Allonautilus scrobiculatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ambassis dussumieri* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Ambassis miops* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Ambassis urotaenia* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Amblyeleotris aurora* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Amblyeleotris macronema* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Amblyglyphidodon indicus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ancistrogobius dipus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anguilla bicolor* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Antennatus linearis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Apogonichthyoides umbratilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Apolemichthys xanthurus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Asterorhombus filifer* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Astronotus ocellatus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Atherinomorus lacunosus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Atractosteus spatula* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Atropus atropos* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Auriglobus modestus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Barbodes bunau* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bathygobius meggitti* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Betta dimidiata* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta schalleri* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta unimaculata* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Blenniella leopardus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bostrychus expatria* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brachygobius xanthomelas* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brachysomophis umbonis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Callionymus neptunius* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Callionymus pleurostictus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Callionymus tethys* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Callogobius stellatus* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Canthidermis macrolepis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Canthigaster cyanospilota* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Canthigaster petersii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Carangoides praeustus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Caranx heberi* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Carcharhinus limbatus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Carcharhinus plumbeus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Carcharodon carcharias* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Centropyge multispinis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cephalopholis igarashiensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chaetodon andamanensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chaetodon interruptus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Channa baramensis* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Channa cyanospilos* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cheilopogon dorsomacula* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chiloscyllium griseum* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Chitala borneensis* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Choerodon jordani* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Choeroichthys brachysoma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Choeroichthys cinctus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Choeroichthys sculptus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chromis pura* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chrysiptera flavipinnis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chrysiptera giti* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cirrhilabrus cenderawasih* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Clarias macrocephalus* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Clarias meladerma* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cociella punctata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Coptodon zillii* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cristatogobius lophius* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Cryptarius truncatus* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cryptocentroides insignis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Cryptocentrus epakros* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cyclichthys spilostylus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dascyllus abudafur* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dermogenys collettei* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Dichotomyctere erythrotaenia* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Microphis boaja* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Echidna rhodochilus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Echinorhinus cookei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eirmotus octozona* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Elops hawaiensis* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Encheloclarias kelioides* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Enneapterygius mirabilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Entomacrodus caudofasciatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epalzeorhynchos kalopterum* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Epinephelus cyanopodus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epinephelus polystigma* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Epinephelus tauvina* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Etelis boweni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Etelis coruscans* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eubleekeria jonesi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eviota oculineata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Exyrias ferrarisi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fowleria amblyuroptera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gastromyzon ingeri* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gastromyzon ocellatus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gazza achlamys* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Gazza dentex* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Giuris charpini* | 2 | ? | zu wenige Nachweise (2 < 5) |
| *Glaucosoma magnificum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Glossamia aprion* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Glossolepis incisa* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Glyptothorax amnestus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Glyptothorax platypogonides* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gobiodon acicularis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gobiodon heterospilos* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Grallenia arenicola* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnocranius elongatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnothorax pindae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnothorax polyuranodon* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Gymnothorax sagmacephalus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Halichoeres chlorocephalus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Halichoeres pardaleocephalus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Halichoeres rubricephalus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Halichoeres timorensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Helcogramma albimacula* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Helcogramma chica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Helcogramma randalli* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hemibagrus wyckii* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemichromis elongatus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemigobius hoevenii* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Hemirhamphodon chrysopunctatus* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemiscyllium strahani* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hemitrygon parvonigra* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Heteroconger cobra* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Heteroconger fugax* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Heteroconger guttatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Heterodontus zebra* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hypseleotris everetti* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ichthyapus vulturis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Isurus oxyrinchus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Johnius borneensis* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Kalyptatherina helodes* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Labiobarbus fasciatus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Labiobarbus festivus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lagocephalus lunaris* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Lagocephalus sceleratus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Laiphognathus multimaculatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lamiopsis tephrodes* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Leiocassis bekantan* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Leiopotherapon plumbeus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lentipes kijimuna* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lepidocephalichthys tomaculum* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Leptojulis polylepis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Liocranchia reinhardtii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Litobranchus fowleri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lophodiodon calori* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lubricogobius dinah* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Macrognathus circumcinctus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrognathus tapirus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Maculabatis pastinacoides* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mahidolia paucipora* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Masturus lanceolatus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Meiacanthus anema* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Melanotaenia batanta* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mesopristes argenteus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Microphis brachyurus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Microphis leiaspis* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mirolabrichthys evansi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mobula tarapacana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mugilogobius chulae* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Mugilogobius mertoni* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Mustelus griseus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Myersina nigrivirgata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Myersina yangii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Myliobatis hamlyni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mystacoleucus padangensis* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mystus wolffii* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neamia octospina* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nemacheilus olivaceus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nematabramis borneensis* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nemipterus balinensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nemipterus nematopus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Neovespicula depressifrons* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Nomorhamphus megarrhamphus* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nomorhamphus towoetii* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Novaculops halsteadi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Odontaspis ferox* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Omobranchus obliquus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Ompok rhadinurus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ophiocara porocephalum* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Oryzias nebulosus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oryzias nigrimas* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oryzias profundicola* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osteogeneiosus militaris* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Ostorhinchus endekataenia* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ostorhinchus komodoensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ostorhinchus microspilos* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ostorhinchus properuptus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Oxymetopon compressus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Oxyurichthys auchenolepis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pangasius mahakamensis* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pangio oblonga* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paracheilinus mccoskeri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Paragobiodon kasaii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Paratherina striata* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parioglossus interruptus* | 2 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parioglossus palustris* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Parosphromenus bintan* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parosphromenus phoenicurus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pectenocypris korthausae* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pempheris schwenkii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Periophthalmus kalolo* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Periophthalmus malaccensis* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Phalacronotus apogon* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Photolateralis stercorarius* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pinjalo pinjalo* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pisodonophis cancrivorus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Plectorhinchus multivittatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plesiobatis daviesi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plesiops corallicola* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pogonoperca ocellata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pomacentrus andamanensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pomacentrus geminospilus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pomadasys furcatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Praealticus oortii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Priolepis profunda* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Priolepis sticta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Prionace glauca* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Pseudeutropius brachypopterus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudochromis aurulentus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudochromis eichleri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudochromis pylei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudochromis tapeinosoma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudocoris petila* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudogobiopsis lumbantobing* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudogobiopsis oligactis* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudorhombus javanicus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Psilogobius prolatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pteroplatytrygon violacea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pycnochromis iomelas* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pyronotanthias bimarginatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rasbora meinkeni* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora semilineata* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora tawarensis* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rhabdoblennius nitidus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rhinobatos jimbaranensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rhinolepadichthys lineatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rhynchobatus cooki* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rogadius serratus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ruvettus pretiosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Salarias alboguttatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Salarias sibogai* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sardinops sagax* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sargocentron ittodai* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Saurida undosquamis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scomberomorus semifasciatus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Scorpaenodes varipinnis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scuticaria okinawae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Selenotoca multifasciata* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Seriola rivoliana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sicyopterus cynocephalus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sicyopterus micrurus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Sicyopterus squamosissimus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Silurichthys hasseltii* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Smilosicyopus fehlmanni* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Sphaerichthys vaillanti* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Springeratus xanthosoma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Squalus altipinnis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Stiphodon hadiatyae* | 2 | ? | zu wenige Nachweise (2 < 5) |
| *Sundadanio axelrodi* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Callionymus corallinus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tominanga sanguicauda* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Tomiyamichthys russus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tomiyamichthys zonatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trachurus novaezelandiae* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Trimma capostriatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trimma flammeum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trimma putrai* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trimma sanguinellum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tryssogobius colini* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Upeneus elongatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Upeneus taeniopterus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Uropterygius oligospondylus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Uropterygius xanthopterus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Uroteuthis bartschi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vanderhorstia dawnarnallae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vanderhorstia flavilineata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vanderhorstia nannai* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Velifer hypselopterus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Zoramia fragilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Zoramia gilberti* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Abudefduf abdominalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acanthocepola abbreviata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acanthogobius flavimanus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Acentrogobius suluensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Acentrogobius vanderloosi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aetomylaeus nichofii* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Alticus saliens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Altrichthys curatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amblyeleotris rhyax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amblygobius calvatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amblygobius semicinctus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Amblypomacentrus kuiteri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amblyrhynchichthys truncatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ammolabrus dicrus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amphiprion thiellei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ancistrogobius squamiceps* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anguilla borneensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anguilla celebesensis* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Anodontostoma chacunda* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Apogon ceramensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Apogon crassiceps* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Apogon seminigracaudus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Apogonichthyoides sialis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Arius maculatus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Arius manillensis* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Assessor flavissimus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Asterropteryx ovata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Asterropteryx profunda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Asterropteryx senoui* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Asterropteryx spinosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bagrichthys macracanthus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bagrichthys macropterus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Balitoropsis ophiolepis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Barbodes everetti* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Barbodes kuchingensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Barbodes palavanensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bathytoshia lata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Batrachocephalus mino* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Betta albimarginata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta antoni* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta burdigala* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta chini* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta chloropharynx* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta compuncta* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta foerschi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta gladiator* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta krataios* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta mandor* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta nuluhon* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta pallifina* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta patoti* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta renata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta rubra* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bihunichthys monopteroides* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bleekeriella leptaspis* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Blenniella caudolineata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Blenniella periophthalmus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Boleophthalmus dussumieri* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Boleophthalmus poti* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Boraras brigittae* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bostrychus sinensis* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Breitensteinia insignis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brevibora exilis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Butis gymnopomus* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Butis humeralis* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Butis koilomatodon* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Callionymus japonicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Callistoctopus ornatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Callogobius centrolepis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Callogobius maculipinnis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Canthigaster punctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Canthigaster smithae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Caracanthus madagascariensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Caragobius urolepis* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Carapus bermudensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carcharhinus amblyrhynchoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carcharhinus dussumieri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Centrophorus granulosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Centrophorus longipinnis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Centropyge abei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Centropyge flavipectoralis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Centropyge flavissima × vrolikii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cephaloscyllium pictum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cercamia melanogaster* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaenogaleus macrostoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaetodon argentatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaetodontoplus duboulayi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaetodontoplus vanderloosi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chanda ranga* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Channomuraena vittata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chauliodus sloani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheilopogon atrisignis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheilopogon nigricans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheilopogon spilopterus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chiloscyllium burmense* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chiloscyllium hasseltii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chiloscyllium indicum* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Choerodon robustus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chromis xouthos* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chrysiptera niger* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chrysiptera sinclairi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirrhilabrus katherinae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirrhilabrus melanomarginatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirrhilabrus punctatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirrhimuraena playfairii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clarias pseudoleiacanthus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Clupeichthys goniognathus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Congresox talabon* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Conidens laticephalus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coryphaena equiselis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Corythoichthys flavofasciatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Corythoichthys nigripectus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cosmocampus maxweberi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Craterocephalus lacustris* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Crossocheilus cobitis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Crossocheilus langei* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Crossocheilus nigriloba* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cryptocentrus cebuanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cryptocentrus nanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cryptocentrus pavoninoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cyclocheilichthys heteronema* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyclocheilichthys janthochir* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynoglossus kopsii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cypselurus hexazona* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cypselurus oligolepis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Danio albolineatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Decapterus akaadsi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Decapterus tabl* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dentex spariformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dermogenys robertsi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Deveximentum indicium* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Diagramma labiosum* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Diaphenchelys dalmatian* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Drepane longimana* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Drombus globiceps* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Dussumieria elopsoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echidna delicatula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echidna xanthospilos* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ecsenius collettei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ecsenius oculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ecsenius paroculus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ecsenius polystictus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eleutheronema tridactylum* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Ellopostoma megalomycter* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Encheliophis gracilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Encheliophis homei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Enchelycore pardalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Enneapterygius flavoccipitis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Enneapterygius pusillus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Enneapterygius erythrosoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Entomacrodus epalzeocheilos* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Entomacrodus thalassinus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ephippus orbis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus epistictus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus faveatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus insularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus morrhua* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus radiatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus rivulatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Equulites leuciscus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Erythrocles schlegelii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eviota bipunctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eviota santanai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eviota spilota* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Evoxymetopon poeyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Filimanus perplexa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fistularia petimba* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Flabellicauda bolini* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Foa hyalina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gargariscus prionocephalus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gastromyzon danumensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gastromyzon punctulatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gazza rhombea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Genicanthus caudovittatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gerres limbatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Gerres macracanthus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Gerres oblongus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gladiogobius brevispinis* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gladiogobius rex* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Glaniopsis denudata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Glossogobius flavipinnis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Glossogobius illimis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Glossogobius intermedius* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Glyptothorax decussatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Glyptothorax nieuwenhuisi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gobiodon fuscoruber* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gobiopsis quinquecincta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Grallenia cinnamea* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Grammonus thielei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gulaphallus mirabilis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gymnapogon philippinus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnapogon urospilotus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnochanda filamentosa* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gymnocranius frenatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnocranius satoi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnocranius superciliosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax eurostus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax gracilicauda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax herrei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax longinquus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax minor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax neglectus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax pseudoherrei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax pseudokidako* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax robinsi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax shaoi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax taiwanensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax tile* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Gyrinocheilus aymonieri* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Halaelurus maculosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halicampus brocki* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halicampus grayi* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres bicolor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres cosmetus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres kallochroma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres pallidus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres trispilus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halieutaea stellata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hampala ampalong* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Helcogramma desa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hemiarius stormii* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Hemibagrus hoevenii* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemiramphus archipelagicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hemiramphus lutkei* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Hemiscyllium henryi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hemisilurus heterorhynchus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemitriakis indroyonoi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hephaestus trimaculatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hilsa kelee* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Hippichthys heptagonus* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hippichthys spicifer* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Hipposcarus harid* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hologymnosus rhodonotus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Homaloptera ocellata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Homalopteroides nebulosus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Homalopteroides stephensoni* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Homalopteroides tweediei* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Homalopterula gymnogaster* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hyporhamphus limbatus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Hyporhamphus quoyi* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Hyporthodus octofasciatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hypseleotris compressa* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Idiosepius paradoxus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ilisha melastoma* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Inegocia japonica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Iniistius evides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Inimicus caledonicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Inimicus cuvieri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Isistius brasiliensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Istiblennius colei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Istigobius diadema* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Isurus paucus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Johnius belangerii* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Karalla daura* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Kryptopterus bicirrhis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Kryptopterus minor* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Kurtus gulliveri* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Labeo erythropterus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Labracinus atrofasciatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lactarius lactarius* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Laiphognathus albifrons* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Lampris megalopsis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lentipes kaaea* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lentipes mekonggaensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lentipes niasensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lepidamia kalosoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lepidotrigla argus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leptobarbus melanopterus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Leptobarbus rubripinna* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Leptomelanosoma indicum* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Leptosynanceia asteroblepa* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Lethrinus conchyliatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lethrinus miniatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Liocranium pleurostigma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Liopropoma susumi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lobocheilos ixocheilos* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lobocheilos kajanensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lophiocharon hutchinsi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lubricogobius ornatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lutjanus maxweberi* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Manonichthys scintilla* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Marilyna meraukensis* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Marosatherina ladigesi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Megatrygon microps* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Meiacanthus abditus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Meiacanthus lineatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Meiacanthus vittatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Melanotaenia kokasensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Melanotaenia rubrostriata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mesopristes cancellatus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Micronema hexapterus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Microphis brevidorsalis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Microphis deokhatoides* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Microphis retzii* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Minous groeneveldi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mitsukurina owstoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mola mola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Monodactylus kottelati* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Mugil cephalus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Mugil curvidens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mugilogobius adeia* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mugilogobius hitam* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mugilogobius latifrons* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mugilogobius platynotus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Mugilogobius rambaiae* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mugilogobius tigrinus* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mustelus stevensi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mustelus widodoi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Myripristis chryseres* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Naso tergus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Naucrates ductor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nedystoma dayi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Negaprion acutidens* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Nemacheilus elegantissimus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nemacheilus saravacensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nematabramis alestes* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nemipterus gracilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nemipterus nemurus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nemipterus sugillatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nemipterus virgatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neoaploactis tridorsalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neolissochilus soro* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neolissochilus sumatranus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neopomacentrus taeniurus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Neosebastes entaxis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neotrygon annotata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neotrygon malaccensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nesogobius pulchellus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nomorhamphus ebrardtii* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nomorhamphus liemi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nomorhamphus pectoralis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nomorhamphus weberi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nototodarus hawaiiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nuchequula gerreoides* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Ompok bimaculatus* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ompok miostoma* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Onuxodon fowleri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophichthus lithinus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiocara cantoris* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Ophisternon bengalense* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Opistognathus castelnaui* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Opistognathus cyanospilotus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Opistognathus punctatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Orbiraja jensenae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Orectolobus reticulatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ornithoteuthis volatilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oryzias bonneorum* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oryzias celebensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oryzias loxolepis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osphronemus septemfasciatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osteochilus flavicauda* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osteochilus schlegelii* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ostorhinchus capricornis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ostorhinchus kiensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Ostorhinchus luteus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ostorhinchus pleuron* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ostorhinchus septemstriatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxyeleotris aruensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oxyeleotris urophthalmus* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oxymetopon filamentosum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxyurichthys lonchotus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pachyula crassilabris* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paedocypris progenetica* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pagrus major* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pampus cinereus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pandaka pusilla* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pandaka pygmaea* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pangasius macronema* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pangio cuneovirgata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pangio kuhlii* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pangio piperata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pangio shelfordii* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Panna microdon* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Paracaesio kusakarii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paracheilinus rubricaudalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paracheilinus togeanensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paracheilinus xanthocirritus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paracrossochilus acerus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parakysis hystriculus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parambassis gulliveri* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paramonacanthus japonicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paramonacanthus oblongus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parapriacanthus dispar* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parascolopsis eriomma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parascorpaena aurita* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Parascorpaena mcadamsi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parascorpaena picta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parexocoetus brachypterus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parioglossus aporos* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parioglossus senoui* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parkraemeria rhinoceros* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parosphromenus filamentosus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parupeneus biaculeatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parupeneus margaritatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pastinachus solocirostris* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pempheris malabarica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pentapodus nagasakiensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Periophthalmus walailakae* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Phalacronotus micronemus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Photoblepharon palpebratum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phoxacromion kaneharai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phoxocampus kampeni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phractocephalus hemioliopterus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pictichromis aurifrons* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plagiotremus phenax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plectorhinchus unicolor* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pleurosicya bilobata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pleurosicya fringilla* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plicofollis argyropleuron* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Polypterus senegalus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pomacentrus javanicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomacentrus komodoensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomacentrus nigriradiatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomacentrus similis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomacentrus umbratilus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomacentrus xanthosternus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomadasys andamanensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomadasys argyreus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomadasys unimaculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Potamosilurus velutinus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Priacanthus fitchi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Priolepis compita* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Priolepis fallacincta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Priolepis kappa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Priolepis nocturna* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Prionobutis microps* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pristiapogon taeniopterus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pristipomoides auricilla* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pristipomoides typus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Proteracanthus sarissophorus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Protomyzon borneensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Protomyzon griswoldi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Psenes cyanophrys* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudamia amblyuroptera* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pseudamia hayashii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudamiops gracilicauda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudanthias hutomoi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudochromis andamanensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudochromis cyanotaenia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudochromis jace* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudochromis litus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudochromis pictus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudogobius hoesei* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudogobius verticalis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pseudojuloides mesostigma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudomystus flavipinnis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudomystus funebris* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudomystus leiacanthus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudomystus stenomus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudotriacanthus strigilifer* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pseudotropheus crabro* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ptereleotris grammica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ptereleotris uroditaenia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pteropterus mombasae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pterotolithus maculatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Puntigrus partipentazona* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Puntigrus pulcher* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pycnochromis acares* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pycnochromis flavipectoralis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pycnochromis howsoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pycnochromis pacifica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pyronotanthias flavoguttatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pyronotanthias parvirostris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rainfordia opercularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rasbora api* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora ennealepis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora kalbarensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rastrelliger brachysoma* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Redigobius balteatus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Rhabdosargus sarba* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Rhinobatos penggali* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhinobatos whitei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhinogobius philippinus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rhinogobius tandikan* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rhinoptera javanica* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Rogadius patriciae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rogadius welanderi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sacura speciosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sardinella gibbosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sargocentron tiere* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Satyrichthys welchi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Saurida tumbil* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scartelaos histophorus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Scarus maculipinna* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Schismatogobius bruynisi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Schismatogobius marmoratus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Schismatogobius saurii* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Scleropages formosus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Scolopsis frenata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scorpaenodes corallinus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sepia brevimana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sepiella inermis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Seriolina nigrofasciata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Setipinna breviceps* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Sicyopterus parvei* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sicyopus discordipinnis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Siganus laqueus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sillago aeolus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Silurichthys marmoratus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Siphamia cyanophthalma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Siphamia majimai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Squalus japonicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Squalus montalbani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Squalus nasutus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Squatina legnota* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stethojulis albovittata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stiphodon carisa* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Stiphodon percnopterygionus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Stonogobiops larsonae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Strophidon dorsalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sunagocia otaitensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sundadanio margarition* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Synchiropus circularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Desmopuntius endecanalis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Taenioides cirratus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Taenioides purpurascens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Takifugu alboplumbeus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Takifugu flavipterus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Telmatherina bonti* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Telmatherina celebensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Terapon puta* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Tetraroge barbata* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Tetrosomus concatenatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thalassoma lutescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thryssa setirostris* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Tomiyamichthys smithi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Torquigener flavimaculosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Torquigener pleurogramma* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Torquigener tuberculiferus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trachicephalus uranoscopus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Triacanthus biaculeatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Trigonostigma hengeli* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma emeryi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trimma nomurai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trimma pajama* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trimma preclarum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trimma readerae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trimma xanthum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tripodichthys blochii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tryssogobius sarah* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Upeneus asymmetricus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Urolophus mitosis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Uropterygius marmoratus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Uropterygius nagoensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Uroteuthis chinensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vanderhorstia attenuata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vanderhorstia vandersteene* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vincentia novaehollandiae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Wattsia mossambica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Wetmorella tanakai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xanthichthys lineopunctatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xenanthias nanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xenentodon cancila* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Xenojulis margaritacea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xestochilus nebulosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xiphias gladius* | 1 | Meer | zu wenige Nachweise (1 < 5) |

</details>

## Subdeck `invertebrates` (40)

Eigene Taxa, Größe und Filter, Reihenfolge-Quelle und Region des Rezepts. Arten, die schon in einem Level oder einem früheren Subdeck stehen, bleiben draußen; die Führer werden nicht abgeglichen.

- iNaturalist: 4211 Taxa (Seiten: 9)
- OBIS: 18394 Arten mit Nachweisen außer iNaturalist

### iNaturalist-Namen zugeordnet

Laut `recipes/inat_names.json`: iNaturalist nennt die Art anders als die Referenz-DB; die Zählung kommt zu der der Referenz-DB-Art.

| iNaturalist | Referenz-DB | iNat | Art | Beleg |
|---|---|---|---|---|
| *Ascarosepion pfefferi* | *Metasepia pfefferi* | 638 | Umbenennung | https://www.inaturalist.org/taxon_changes/131489 |
| *Ascarosepion bandense* | *Sepia bandensis* | 253 | Umbenennung | https://www.inaturalist.org/taxon_changes/131481 |
| *Ascarosepion papuense* | *Sepia papuensis* | 187 | Umbenennung | https://www.inaturalist.org/taxon_changes/131455 |
| *Pinnoctopus luteus* | *Callistoctopus luteus* | 69 | Umbenennung | https://www.inaturalist.org/taxon_changes/172616 |
| *Pinnoctopus aspilosomatis* | *Callistoctopus aspilosomatis* | 12 | Umbenennung | https://www.inaturalist.org/taxon_changes/172611 |
| *Acanthosepion recurvirostrum* | *Sepia recurvirostra* | 6 | Umbenennung | https://www.inaturalist.org/taxon_changes/131450 |
| *Pinnoctopus ornatus* | *Callistoctopus ornatus* | 1 | Umbenennung | https://www.inaturalist.org/taxon_changes/172615 |

### Von Hand ausgeschlossen

| Art | iNat | Grund |
|---|---|---|
| *Coenobita rugosus* | 867 | Landeinsiedlerkrebs, lebt an Land und geht nur zur Eiablage ans Meer. |

### Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Hexabranchus sanguineus* | Die Spanische Tänzerin ist die größte Nacktschnecke des Riffs und schwimmt bei Nacht mit wehendem Mantel. | 415 | Reihenfolge-Quelle, OBIS, Verbreitung | invertebrates |
| *Hymenocera picta* | Die Harlekingarnele frisst nur Seesterne und ist einer der begehrtesten Funde für Unterwasserfotografen. | 68 | Reihenfolge-Quelle | invertebrates |
| *Acanthaster solaris* (Rezept: *Acanthaster planci*) | Die Dornenkrone frisst Korallen; ihre Massenvermehrungen zerstören ganze Riffe, und ihre Stacheln sind giftig. | 77 | Reihenfolge-Quelle, OBIS, Verbreitung | invertebrates |

### Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS ohne iNaturalist oder Verbreitung): 39/40 (98 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 0
- Arten ohne Volksnamen `de` in der Referenz-DB: 20/40 (50 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 2/40 (5 %)
- Familien ohne Volksnamen `de`: 24/24 (100 %): *Acanthasteridae*, *Cardiidae*, *Chromodorididae*, *Cypraeidae*, *Diadematidae*, *Didemnidae*, *Diogenidae*, *Discodorididae*, *Dorididae*, *Echinasteridae*, *Facelinidae*, *Hexabranchidae*, *Holothuriidae*, *Odontodactylidae*, *Ophidiasteridae*, *Oreasteridae*, *Palaemonidae*, *Palinuridae*, *Phyllidiidae*, *Polyceridae*, *Porcellanidae*, *Stenopodidae*, *Styelidae*, *Thoridae*
- Familien ohne Volksnamen `en`: 14/24 (58 %): *Chromodorididae*, *Diadematidae*, *Didemnidae*, *Discodorididae*, *Dorididae*, *Echinasteridae*, *Facelinidae*, *Hexabranchidae*, *Ophidiasteridae*, *Oreasteridae*, *Phyllidiidae*, *Polyceridae*, *Styelidae*, *Thoridae*

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

- *Hymenocera picta*: Reihenfolge-Quelle

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

- gleicher Volksname `de` „Nacktschnecke“: *Pteraeolidia semperi*, *Phyllidia elegans*, *Caloria indica*
- gleicher Volksname `de` „Prachtsternschnecke“: *Chromodoris annae*, *Chromodoris willani*, *Doriprismatica atromarginata*, *Chromodoris lochi*, *Chromodoris magnifica*

### Arten

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Klasse |
|---|---|---|---|---|---|---|
| 1 | *Linckia laevigata* | 2328 | 1924 | native ×2 | Meer | Asteroidea |
| 2 | *Chromodoris annae* | 2286 | 552 | native ×4 | Meer | Gastropoda |
| 3 | *Pteraeolidia semperi* | 1841 | 446 | native ×3 | Meer | Gastropoda |
| 4 | *Odontodactylus scyllarus* | 1647 | 1 | native ×5 | Meer | Malacostraca |
| 5 | *Protoreaster nodosus* | 1636 | 560 | native ×3 | Meer | Asteroidea |
| 6 | *Phyllidia varicosa* | 1537 | 388 | native ×5 | Meer | Gastropoda |
| 7 | *Hypselodoris tryoni* | 1398 | 460 | native ×2 | Meer | Gastropoda |
| 8 | *Nembrotha kubaryana* | 1332 | 472 | native ×2 | Meer | Gastropoda |
| 9 | *Chromodoris willani* | 1223 | 350 | native ×3 | Meer | Gastropoda |
| 10 | *Stenopus hispidus* | 1215 | 38 | native ×1 | Meer | Malacostraca |
| 11 | *Neopetrolisthes maculatus* | 1211 | 27 | native ×1 | Meer | Malacostraca |
| 12 | *Thor amboinensis* | 1172 | 150 | native ×1 | Meer | Malacostraca |
| 13 | *Phyllidia ocellata* | 1166 | 402 | native ×4 | Meer | Gastropoda |
| 14 | *Polycarpa aurata* | 1101 | 33 | native ×2 | Meer | Ascidiacea |
| 15 | *Doriprismatica atromarginata* | 1077 | 322 | native ×4 | Meer | Gastropoda |
| 16 | *Culcita novaeguineae* | 1064 | 577 | native ×2 | Meer | Asteroidea |
| 17 | *Chromodoris lochi* | 1060 | 294 | native ×1 | Meer | Gastropoda |
| 18 | *Goniobranchus geometricus* | 993 | 331 | native ×2 | Meer | Gastropoda |
| 19 | *Echinaster luzonicus* | 928 | 161 | native ×2 | Meer | Asteroidea |
| 20 | *Echinothrix calamaris* | 918 | 139 | native ×2 | Meer | Echinoidea |
| 21 | *Tridacna squamosa* | 897 | 498 | native ×6 | Meer | Bivalvia |
| 22 | *Didemnum molle* | 893 | 63 | native ×2 | Meer | Ascidiacea |
| 23 | *Chromodoris magnifica* | 870 | 436 | native ×4 | Meer | Gastropoda |
| 24 | *Halgerda batangas* | 866 | 319 | native ×2 | Meer | Gastropoda |
| 25 | *Cypraea tigris* | 854 | 411 | native ×6 | Meer | Gastropoda |
| 26 | *Phyllidia elegans* | 843 | 295 | native ×3 | Meer | Gastropoda |
| 27 | *Caloria indica* | 842 | 256 | native ×2 | Meer | Gastropoda |
| 28 | *Nembrotha cristata* | 842 | 381 | native ×5 | Meer | Gastropoda |
| 29 | *Pearsonothuria graeffei* | 840 | 220 | native ×5 | Meer | Holothuroidea |
| 30 | *Nembrotha chamberlaini* | 831 | 250 | native ×1 | Meer | Gastropoda |
| 31 | *Tridacna crocea* | 818 | 1555 | native ×6 | Meer | Bivalvia |
| 32 | *Phyllidia coelestis* | 815 | 227 | native ×3 | Meer | Gastropoda |
| 33 | *Panulirus versicolor* | 806 | 103 | native ×5 | Meer | Malacostraca |
| 34 | *Diadema setosum* | 756 | 44 | native ×2 | Meer | Echinoidea |
| 35 | *Jorunna funebris* | 726 | 284 | native ×3 | Meer | Gastropoda |
| 36 | *Choriaster granulatus* | 715 | 91 | native ×4 | Meer | Asteroidea |
| 37 | *Dardanus pedunculatus* | 688 | 37 | native ×3 | Meer | Malacostraca |
| 68 | *Hymenocera picta* (Highlight; 192 Beobachter) | 454 | – | – | Meer | Malacostraca |
| 77 | *Acanthaster solaris* (Highlight; Quelle: *Acanthaster planci*; 235 Beobachter) | 420 | 299 | native ×2 | Meer | Asteroidea |
| 415 | *Hexabranchus sanguineus* (Highlight; 53 Beobachter) | 74 | 143 | native ×5 | Meer | Gastropoda |

### Grenzfälle

Je 10 Arten vor und nach der Grenze (Highlights übersprungen).

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Klasse | Im Subdeck |
|---|---|---|---|---|---|---|---|
| 28 | *Nembrotha cristata* | 842 | 381 | native ×5 | Meer | Gastropoda | ja |
| 29 | *Pearsonothuria graeffei* | 840 | 220 | native ×5 | Meer | Holothuroidea | ja |
| 30 | *Nembrotha chamberlaini* | 831 | 250 | native ×1 | Meer | Gastropoda | ja |
| 31 | *Tridacna crocea* | 818 | 1555 | native ×6 | Meer | Bivalvia | ja |
| 32 | *Phyllidia coelestis* | 815 | 227 | native ×3 | Meer | Gastropoda | ja |
| 33 | *Panulirus versicolor* | 806 | 103 | native ×5 | Meer | Malacostraca | ja |
| 34 | *Diadema setosum* | 756 | 44 | native ×2 | Meer | Echinoidea | ja |
| 35 | *Jorunna funebris* | 726 | 284 | native ×3 | Meer | Gastropoda | ja |
| 36 | *Choriaster granulatus* | 715 | 91 | native ×4 | Meer | Asteroidea | ja |
| 37 | *Dardanus pedunculatus* | 688 | 37 | native ×3 | Meer | Malacostraca | ja |
| | **Grenze** | | | | | | |
| 38 | *Goniobranchus hintuanensis* | 671 | 238 | native ×4 | Meer | ? | nein |
| 39 | *Xestospongia testudinaria* | 656 | 85 | native ×2 | Meer | ? | nein |
| 40 | *Zenopontonia rex* | 637 | 12 | – | Meer | ? | nein |
| 41 | *Goniobranchus kuniei* | 627 | 254 | native ×3 | Meer | ? | nein |
| 42 | *Hypselodoris zephyra* | 625 | 146 | native ×1 | Meer | ? | nein |
| 43 | *Achaeus japonicus* | 618 | 1 | – | Meer | ? | nein |
| 44 | *Elysia marginata* | 602 | 19 | – | Meer | ? | nein |
| 45 | *Tridacna maxima* | 597 | 1533 | native ×6 | Brack/Meer | ? | nein |
| 46 | *Pleurobranchus forskalii* | 594 | 156 | native ×1 | Meer | ? | nein |
| 47 | *Phyllidiella pustulosa* | 588 | 509 | native ×3 | Meer | ? | nein |

### Ausgeschlossene Kandidaten

<details><summary>1261 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Ascarosepion latimanus* | 1446 | Meer | schon in einem anderen Subdeck (level-1) |
| *Coenobita rugosus* | 867 | Meer | von Hand ausgeschlossen (Landeinsiedlerkrebs, lebt an Land und geht nur zur Eiablage ans Meer.) |
| *Octopus cyanea* | 866 | Meer | schon in einem anderen Subdeck (level-2) |
| *Metasepia pfefferi* | 638 | Meer | schon in einem anderen Subdeck (level-1) |
| *Amphioctopus marginatus* | 637 | Meer | schon in einem anderen Subdeck (level-2) |
| *Sepioteuthis lessoniana* | 540 | Brack/Meer | schon in einem anderen Subdeck (level-3) |
| *Wunderpus photogenicus* | 335 | Meer | schon in einem anderen Subdeck (level-1) |
| *Metasesarma aubryi* | 60 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sepiadarium kochii* | 51 | Meer | nur tiefer als die Tauchgrenze (erst ab 60 m) |
| *Harpa major* | 50 | Meer | nur tiefer als die Tauchgrenze (erst ab 62 m) |
| *Melanoides tuberculata* | 35 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Aliculastrum cylindricum* | 34 | Brack/Meer | nur tiefer als die Tauchgrenze (erst ab 45 m) |
| *Jacksonaster depressum* | 29 | Meer | nur tiefer als die Tauchgrenze (erst ab 50 m) |
| *Macrobrachium lar* | 28 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pylopaguropsis zebra* | 28 | Meer | nur tiefer als die Tauchgrenze (erst ab 50 m) |
| *Epizoanthus illoricatus* | 27 | Meer | nur tiefer als die Tauchgrenze (erst ab 90 m) |
| *Faunus ater* | 26 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cherax quadricarinatus* | 25 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Spirula spirula* | 19 | Meer | nur tiefer als die Tauchgrenze (erst ab 100 m) |
| *Ancylomenes tenuirostris* | 14 | Meer | nur tiefer als die Tauchgrenze (erst ab 73 m) |
| *Myra grandis* | 14 | Meer | nur tiefer als die Tauchgrenze (erst ab 49 m) |
| *Conus ammiralis* | 12 | Meer | nur tiefer als die Tauchgrenze (erst ab 42 m) |
| *Quadrella boopsis* | 10 | Meer | nur tiefer als die Tauchgrenze (erst ab 100 m) |
| *Pomacea canaliculata* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Atyoida pilipes* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Halgerda okinawa* | 7 | Meer | nur tiefer als die Tauchgrenze (erst ab 53 m) |
| *Macrobrachium sintangense* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Corbicula manilensis* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrobrachium latimanus* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Conus andremenezi* | 5 | Meer | nur tiefer als die Tauchgrenze (erst ab 150 m) |
| *Sanderia malayensis* | 5 | Meer | nur tiefer als die Tauchgrenze (erst ab 102 m) |
| *Acropora samoensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Acropora spicifera* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Acropora subglabra* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Actinocyclus verrucosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Actinopyga varians* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Aldisa fragaria* | 4 | ? | zu wenige Nachweise (4 < 5) |
| *Alectryonella plicatula* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Alertigorgia orientalis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Alpheus thompsoni* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Anomalorhiza shawi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Anthenea regalis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Anthopleura dixoniana* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Arete indicus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Armina semperi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ashtoret picta* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Astralium rhodostomum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Atergatis dilatatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Atrina vexillum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Babylonia spirata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Berthellina citrina* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Brachidontes crebristriatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Bursatella leachii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Burtonulla sibogae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Calappa clypeata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Caridina weberi* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cephalopyge trematoides* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Chama lazarus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Charybdis anisodon* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Chelidonura livida* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Clarkcomanthus alternans* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Clypeomorus petrosa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Conus australis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Conus consors* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Conus litoglyphus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Conus muriculatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Conus nobilis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Conus spectrum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Conus striolatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Coryphellina pannae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cratena lineata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Crenavolva striatula* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cuapetes grandis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cycloachelous granulatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cycloseris vaughani* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cyerce bourbonica* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Dendrodoris arborescens* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Diazona tenera* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Latona cuneata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Echinophyllia echinoporoides* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ecteinascidia nexa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ectopleura viridis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Engina lineata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Engina spica* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Episesarma singaporense* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Episesarma versicolor* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Eudistoma fluorescens* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Goniopora fruticosa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gutturnium muricinum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gymnangium hians* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Halgerda mango* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Haliotis diversicolor* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Halomitra clavator* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Holothuria flavomaculata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Holothuria pervicax* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Homalocantha zamboi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hydromyles globulosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Isopora togianensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Julia zebra* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lambis crocata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lambis truncata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Liloa porcellana* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lithophyllon repanda* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lunella cinerea* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lyrocardium lyratum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lysiosquilla tredecimdentata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Macrobrachium lanchesteri* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrobrachium latidactylus* | 4 | Süß/Meer | zu wenige Nachweise (4 < 5) |
| *Maculotriton serriale* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Metopograpsus thukuhar* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Mexichromis macropus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Micippa philyra* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Micropagurus devaneyi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Strigatella retusa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Monodonta labio* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Myomenippe hardwickii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Myra eudactylus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Nassarius albescens* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Nassarius gaudiosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Neocancilla clathrus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Nerita insculpta* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ophiothrix exigua* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ozius tuberculosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Parasesarma sanguimanus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Paratapes undulatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Parthenope longimanus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pegea confoederata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Phanerophthalmus cylindricus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Phronima sedentaria* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Platydoris inornata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Polybranchia orientalis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pontoniopsis comanthi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pseudodistoma megalarva* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Quadrella serenei* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sabellastarte magnifica* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sacoproteus nishae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Salmacis belli* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scutellastra flexuosa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Selatium elongatum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sermyla riquetii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sicyonia bispinosa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Solmundella bitentaculata* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Stichopus monotuberculatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Stichopus pseudohorrens* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Stichopus rubermaculosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Stiliger aureomarginatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Stiliger ornatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Strigatella paupercula* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Symplegma brakenhielmi* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Tapes literatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Tectus fenestratus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Terpios granulosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Tetralia rubridactyla* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Tiaramedon spinosum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Tibia fusus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Tritonoharpa antiquata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Trochus maculatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Tuleariocaris neglecta* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Vexillum acupictum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Acropora desalwii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Acropora granulosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Acropora loripes* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Acropora plumosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Acropora selago* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Actinoporus elongatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Amphipholis squamata* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Ancistrocheirus lesueurii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Exaiptasia diaphana* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Aniculus ursus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Anthopleura anjunae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Antigona magnifica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Aquilonastra coronata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Araiopontonia odontorhyncha* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Arcania septemspinosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ardeadoris electra* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Atriolum robustum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Australaugeneria rutilans* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Batissa violacea* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bernardpora stutchburyi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bistolida ursellus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bufonaria rana* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bursa lamarckii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bursina ignobilis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cadlinella subornatissima* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Calcinus guamensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Callyspongia diffusa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cassidula nucleus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Catostylus townsendi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ceraesignum maximum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cerithium citrinum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Charybdis callianassa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chicoreus capucinus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chirostylus dolichopus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chlorodiella nigra* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chondrosia corticata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chrysaora chinensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cinachyrella tenuiviolacea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Circe scripta* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cirsotrema amamiense* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Clathria hirsuta* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Comanthus parvicirrus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus armadillo* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus aureus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus blanfordianus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus coccineus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus crocatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus ferrugineus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus figulinus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus furvus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus hyaena* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus nussatella* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus radiatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus solomonensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus stramineus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus sugillatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Corolla spectabilis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Craspedochiton laqueatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Crella papillata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Crenatula picta* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Crenavolva tinctura* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cryptoplax larvaeformis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ctenocella pectinata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cymbiola nobilis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cymo andreossyi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cypraecassis rufa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dactylonia ascidicola* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dendrodoris albopurpura* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Diminovula alabaster* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Diogenes biramus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dipsastraea matthaii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dipsastraea rosaria* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Disasterina abnormalis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Distichopora violacea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Diversidoris aurantionodulosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dolomena pulchella* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Donax spiniferus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Drupella margariticola* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Drupina grossularia* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Echineulima robusta* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Echinophyllia bulbosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ellobium aurisjudae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Elysia obtusa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Eoacmaea profunda* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Epidendrium sordidum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Epixanthus dentatus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Erronea pallida* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Eudistoma amplum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Euxanthus exsculptus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gafrarium divaricatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Goniobranchus reticulatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Goniopora lobata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Goniopora tenuidens* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Grapsus intermedius* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gymnodoris citrina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gymnodoris striata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Halgerda scripta* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Haliclona baeri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Haliclona caerulea* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Haliotis ovina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hastula strigilata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hippa adactyla* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Hippolyte ventricosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Holothuria lineata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Holothuria nigralutea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hydatina amplustre* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hyotissa sinensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Imbricaria conularis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Indomodulus tectum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Julia exquisita* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Junceella juncea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lachnopodus ponapensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Leucosia punctata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Liomera monticulosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lissodiadema lorioli* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lithophyllon concinna* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lobophyllia hataii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lysmata malagasy* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Macrophthalmus tomentosus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Madrella ferruginosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Madrella sanguinea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mammilla melanostoma* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mancinella alouina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mauritia depressa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mauritia maculifera* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Melo broderipii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Menippe rumphii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Montipora altasepta* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Montipora foliosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Montipora hodgsoni* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Morula spinosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mycale cecilia* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Nassarius globosus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Neosarmatium integrum* | 3 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neotroglocarcinus dawydoffi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Neoxanthops lineatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Notocochlis gualteriana* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Oligometra serripinna* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Olindias singularis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Oliva parkinsoni* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Oliva tigridella* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Opheodesoma spectabilis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ophiothrix trilineata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Oxymeris felina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pagurixus haigae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pagurixus patiae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Palmadusta saulae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paradoris erythraeensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Parhippolyte uveae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pavona maldivensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Peltodoris murrea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Peltodoris rubra* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Penaeus merguiensis* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Pennaria disticha* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Peronia verruculata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Petrolisthes hastatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Phanerophthalmus luteus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Phenacovolva parvita* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Phylliroe bucephala* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Phyllodesmium hyalinum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Physella acuta* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pinna saccata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Placuna ephippium* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Placuna placenta* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Plagusia squamosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Platydoris ellioti* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Polinices aurantius* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Porites lobata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Portunus convexus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Primovula formosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Procalpurnus lacteus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pseudopaguristes monoporus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Psilaxis oxytropis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Purpura persica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Purpuradusta hammondae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pylopaguropsis fimbriata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rapa rapa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sabia conica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Saccostrea cuccullata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sclerodoris apiculata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Scutarcopagia scobinata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sebadoris nubilosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Septaria lineata* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Siphonodictyon maldiviense* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Spondylus regius* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Stenomelania plicaria* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Stichopathes maldivensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Stylophora subseriata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Synaptula spinifera* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tanea lineata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Terebra amanda* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tetraloides heterodactylus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Thalassianthus aster* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Thorectaxia papuensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Thorunna punicea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tonna tessellata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Trapezia bidentata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Trochus radiatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tubipora musica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Turbo setosus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tylocarcinus styx* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Urnalana elata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Valvaster striatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Velella velella* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Vexillum coccineum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Stellaria solaris* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Acropora aspera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora awi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora carduus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora derawanensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora donei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora indonesia* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora latistella* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora multiacuta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora palmerae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora suharsonoi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acrosterigma simplex* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Actaeodes hirsutissimus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acteon virgatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Actinopyga miliaris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Adinda lamellata* | 2 | ? | zu wenige Nachweise (2 < 5) |
| *Aesopus cumingii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Aethra scruposa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Aglaura hemistoma* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Allonautilus scrobiculatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Alpheus cyanoteles* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Alveopora catalai* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anacropora puertogalerae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anacropora spinosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anilocra longicauda* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Aplidium protectans* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Aplysia juliana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Aquilonastra corallicola* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Architectonica maculata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Armina comta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Barbatia obliquata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bornella hermanni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bruciana pediger* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Brunneifusus ternatanus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cassiopea ornata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cellana grata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cellana toreuma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cerithidea obtusa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cerithium columna* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cerithium coralium* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chaetodiadema granulatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Charybdis truncata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chelidonura punctata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Siratus alabaster* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chironex fleckeri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chironex yamaguchii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chirostylus ortmanni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chirostylus stellaris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chloeia conspicua* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chromodoris mandapamensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cinetorhynchus hendersoni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cirrhipathes anguina* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cirrhipathes rumphii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Clavelina polycitorella* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Clibanarius snelliusi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Clytia linearis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Colubraria muricata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Colubraria nitidula* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Colubraria obscura* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus abbas* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus auricomus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus balteatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus barbieri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus capitanellus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus caracteristicus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus chiangi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus emaciatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus episcopatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus glaucus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus nimbosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus nocturnus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus striatellus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Copula sivickisi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Coryphellina pseudolotos* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Crenavolva traillii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Crithe cossinea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cryptodromia coronata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cycloscala revoluta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cymo deplanatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lyncina leviathan* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Diacarnus levii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Didemnum conchyliatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Didemnum psammatodes* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dipsastraea favus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dipsastraea lizardensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dipsastraea pallida* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Distorsio reticularis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Domiporta filaris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Latona incarnata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Echinolittorina malaccana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Echinolittorina sundaica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Echinolittorina wallaceana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Echinometra oblonga* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Echinoneus cyclostomus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eirene hexanemalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ellisella plexauroides* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ellobium aurismidae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Elysia mercieri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Engina alveolata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Enigmonia aenigmatica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epimenia australis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epitonium replicatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epitonium scalare* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Etisus anaglyptus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Euplica turturina* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Euprotomus vomer* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fimbria fimbriata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fusinus colus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fusinus forceps* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Galathea subsquamata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Galaxea paucisepta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gari elongata* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Gari maculosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gari squamosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Glaucus atlanticus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Glossodoris pallida* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gomophia egyptiaca* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Goniobranchus roboi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Goniopora pedunculata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Goniopora stokesi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gonodactylaceus glabrous* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gonodactylus smithii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Grapsus longitarsis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Guildfordia triumphans* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Guildfordia yoka* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Halgerda albocristata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Haliotis discus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hallaxa cryptica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hamodactylus noumeae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Harpiosquilla raphidea* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Harrovia elegans* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Heliacus implexus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Heterolithadia fallax* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Holothuria notabilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Holothuria pardalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Holothuria whitmaei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Homola ikedai* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hyastenus uncifer* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hydatina zonata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hypselodoris babai* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Icelopagurus undulatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ilyoplax delsmani* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Iphione muricata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Isognomon perna* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Jorunna daoulasi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lauriea punctata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lepidonotus cristatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Leptastrea purpurea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Leptoseris incrustans* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Leucetta sulcata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Leucosia rubripalma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Limaria basilanica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Limaria fragilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Liocranchia reinhardtii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lissoporcellana nakasonei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lithophyllon scabra* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Luffariella geometrica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lupocyclus quinquedentatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lysiosquilloides siamensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lysmata kuekenthali* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lysmata vittata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Macrobrachium equidens* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Macrobrachium pilimanus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macroschisma sinense* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Malleus albus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Manokia stiasnyi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Marcia hiantina* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Margovula bimaculata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mauritia histrio* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Menaethius monoceros* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mexichromis lemniscata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Millepora exaesa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Montipora caliculata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Montipora carinata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Montipora tuberculosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Montipora verrucosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Murichorda fiscellum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Myra tumidospina* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Naquetia cumingii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nassarius olivaceus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nassarius pullus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nemalecium lighti* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Nematopagurus gardineri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Neonaesa rugosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nerita maxima* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Neritodryas dubia* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Notocochlis dillwynii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Oncinopus araneus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ophiocoma cynthiae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ophiolepis cincta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ophiomaza cacaotica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ophiopeza spinosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ophiothrix foveolata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Palaemon concinnus* | 2 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Panulirus penicillatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Panulirus polyphagus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Paractaea rufopunctata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Parasesarma eumolpe* | 2 | ? | zu wenige Nachweise (2 < 5) |
| *Patelloida lentiginosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Periclimenes patae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Petrolisthes coccineus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Petrolisthes lamarckii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Phanogenia gracilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Phidiana anulifera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Phos senticosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Phyllaplysia lafonti* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Phyllidiella cooraburrama* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Phyllidiella granulata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pinna muricata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pipestela candelabra* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plagusia immaculata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Platygyra pini* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plicatula australis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plocamopherus maculatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Podospongia colini* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Polybranchia jensenae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Procambarus clarkii* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudocirrhipathes mapia* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudograpsus albus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudoliomera speciosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pterygia crenulata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pterynotus bipinnatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pustularia bistrinotata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pyramidella dolabrata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rhinoclavis fasciata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rimellopsis powisii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rochia conus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Roxaniella multistriata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sclerobelemnon burgeri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scyllarides squammosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sicyonia japonica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sicyonia ocellata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Solenocera pectinata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Stomatella auricula* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Strigatella assimilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Strigatella pica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Synalpheus carinatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Synaptula reticulata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tectarius coronatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Terebralia sulcata* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Tesseropora wireni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Testudovolva nebula* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Thalamita admete* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Thalamita chaptalii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Thalamophyllia tenuescens* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Theonella mirabilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tmethypocoelis ceratophora* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tonna sulcosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Topsentia dura* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tritonoturris amabilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trochus hanleyanus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Turbo marmoratus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Turricula javana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Turris spectabilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Uroptychus joloensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Uroteuthis bartschi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vasticardium flavum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vepricardium coronatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Verconia decussata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Verconia varians* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vexilla vexillum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vexillum angustissimum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vexillum citrinum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vexillum discolorium* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vexillum michaui* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vexillum rubrocostatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vexillum spicatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Volegalea cochlidium* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Volvatella vigourouxi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acanthephyra carinata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acanthodromia margarita* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acromitus maculosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora glauca* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora globiceps* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora halmaherae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora horrida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora jacquelineae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora kenti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora lokani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora microphthalma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora nana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora solitaryensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora squamata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora sukarnoi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora verweyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora willisae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acrosterigma maculosum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acrosterigma transcendens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Actinopyga albonigra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Actinopyga palauensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Actumnus setifer* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Adinda malaccensis* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Aequorea pensilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Agelas ceylonica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Albunea symmysta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aldisa pikokai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aliculastrum parallelum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alitropus typus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Alloeocomatella pectinifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alpheopsis yaldwyni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alpheus djeddensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alpheus frontalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alpheus lobidens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amphibalanus variegatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amphimetra tessellata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amphinome rostrata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anacropora forbesi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anacropora pillai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anacropora reticulata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anadara crebricostata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tegillarca nodifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anapagurus bonnieri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Angaria melanacantha* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anteaeolidiella indica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anthelia glauca* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anthopleura nigrescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Antigona chemnitzii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aplidium conicum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aplysia extraordinaria* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aplysia parvula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aplysilla sulfurea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aquilonastra anomala* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aquilonastra colemani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Arcania gracilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Arcania heptacantha* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Arcania undecimspinosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Architectonica maxima* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aretopsis amabilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Armina babai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Armina papillata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Astichopus multifidus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Astralium lapillus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Astreopora expansa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Astreopora randalli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Astropecten indicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Astropecten minadensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Astropecten monacanthus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Atergatopsis signata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aurelia coerulea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Baeolidia australis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Balanus trigonus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Barbatia cometa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Barbatia trapezina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Barbatia virescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Benthodytes lingua* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Biarctus sordidus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bittium glareosum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Blastomussa wellsi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bohadschia maculisparsa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bufonaria echinata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bulla orientalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bullina lineata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Caducifer truncatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calappa bilineata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calappa lophos* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calappa torulosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calcinus fuscus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calcinus rosaceus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calcinus seurati* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Callistoctopus ornatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Callyspongia fructicosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Canarium wilsonorum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cantharellus doederleini* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Caphyra rotundifrons* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carcinus maenas* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Caridina typus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Carinaria cristata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carinomitra typha* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carupa tenuipes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Caudoeuraphia caudata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cavolinia uncinata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cellana enneagona* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ceratosoma palliolatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cerithidea decollata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cerithium echinatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cerithium punctatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cerithium zonatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chelarctus cultrifer* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chelonibia caretta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chicoreus aculeatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chicoreus axicornis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chicoreus bundharmai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chicoreus microphyllus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chicoreus rossiteri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chondrocidaris gigantea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chromodoris quadricolor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cinetorhynchus fasciatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirsotrema rugosum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cladacanthella scabra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clanculus corallinus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clathria venosa* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Clavus canalicularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clibanarius laevimanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clithon faba* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Clivipollia pulchra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Codakia paytenorum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Colubraria tortuosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Comaster audax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conasprella aculeiformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conasprella articulata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conasprella viminea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conchoderma hunteri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conchodytes meleagrinae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus artoptus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus asiaticus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus biliosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus coelinae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus floridulus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus kinoshitai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus legatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus lynceus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus magnificus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus moluccensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus monachus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus moreleti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus mucronatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus nanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus ochroleucus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus pertusus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus suratensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus thalassiarchus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus tulipa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus ventricosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus viola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus wittigi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Corallianassa borradailei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coralliophila amirantium* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coralliophila bulbiformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coralliophila radula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coralliophila squamosissima* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Corbicula fluminea* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Corella minuta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coronaster pauciporis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Corymorpha bigelowi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Crella cyathophora* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Creseis acicula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Crosslandia viridis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Crossotonotus spinipes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cyclodius obscurus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cyclosalpa affinis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cyllometra manca* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cymbulia peronii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cymbulia sibogae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cyphastrea serailia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Annepona mariae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Purpuradusta microdon* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cyrtomaia bicornis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dactylospongia metachromia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Daldorfia investigatoris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Daldorfia rathbuni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Daphnia magna* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Dardanus hessii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dendostrea folium* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dendrodoris albobrunnea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dentalium aprinum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dentalium elephantinum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diphyes dispar* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diplulmaris malayensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dipsastraea helianthoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dipsastraea laddi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dipsastraea laxa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Distichopora vervoorti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Distorsio kurzi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Doclea armata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dolicholatirus lancea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Latona faba* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dorippoides facchino* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Doris raripilosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Doris viridis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dosima fascicularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dosinia japonica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Duncanopsammia axifuga* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Duplicaria duplicata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Duplicaria spectabilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dynomene praedator* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dysidea granulosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echinolittorina melanacme* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echinolittorina vidua* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echinometra viridis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echinostrephus molaris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ecteinascidia turbinata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Edwardsia mammillata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Elimia virginica* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Elysia nigropunctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Elysia ornata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Elysia rufescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Elysia trisinuata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Enoplolambrus echinatus* | 1 | Süß/Meer | zu wenige Nachweise (1 < 5) |
| *Enoplometopus debelius* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epifungium ulu* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epitonium aureomaculatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epitonium clementinum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epitonium fucatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epitonium profundum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epitonium pyramidale* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epitonium stigmaticum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eratoena sulcifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ercolania kencolesi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eriphia ferox* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Erronea pyriformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Erugosquilla woodmasoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Etisus laboutei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eubranchus inabai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Euchelus atratus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Euplectella aspergillum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Euplica deshayesii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Euterpina acutifrons* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Ficus gracilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fragum sueziense* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fulvia boholensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Galathea balssi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Galearctus aurora* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Galeropsis monodonta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gari pulcherrima* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gelliodes obtusa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Geloina expansa* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Glycymeris reevei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gonatonotus nasutus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Goniastrea retiformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Goniobranchus decorus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gonodactylaceus falcatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gonodactylellus viridis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Granata maculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnodoris alba* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnodoris bicolor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gyrineum perca* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halgerda mesophotica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halgerda profunda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halgerda takipsilim* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Haliotis fatui* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Haliotis varia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halitiara rigida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Haloa cobbi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hamigera strongylata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hanabira yukibana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hastula lanceata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hemilienardia goubini* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Heteranthus verruculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Heteronucia venusta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Heteropia glomerosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hicksonella princeps* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hirsutodynomene spinosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria difficilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria enalia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria lessoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria nobilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria turriscelsa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria verrucosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Homalocantha anatomica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Homalocantha scorpio* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Homola orientalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Huenia pacifica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hyastenus elatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hydatina albocincta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hypocolpus abbotti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hypselodoris nigrostriata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Idiosepius paradoxus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xenuroturris cingulifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Isactinernus quadrilobatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Isaurus maculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Isognomon isognomum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Janicella spinicauda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Janthina janthina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Jocaste lucina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lamoha inflata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lamoha murotoensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lampasopsis rhodostoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Latirus belcheri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Latirus gibbulus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Latreutes fucorum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Latreutes pymoeus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lauridromia intermedia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leiaster glaber* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leptastrea gibbosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leptastrea transversa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leptoclinides madara* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leptodius nudipes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leptodius sanguineus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leptoseris fragilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leptoseris striata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leucetta pyriformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leuckartiara zacae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lienardia rubida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lioconcha fastigiata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lioconcha sowerbyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Liomera loevis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Liomera rugata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lissoclinum timorense* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Littoraria nebulosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lobonemoides robustus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lophozozymus incisus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Luidia penangensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lyphira heterograna* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Macrobrachium gracilirostre* | 1 | Süß/Meer | zu wenige Nachweise (1 < 5) |
| *Macrobrachium jaroense* | 1 | Süß/Meer | zu wenige Nachweise (1 < 5) |
| *Macrophiothrix hybrida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Macrophiothrix longipeda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Macrophiothrix striolata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Macrophthalmus convexus* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrophthalmus milloti* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macropodia rostrata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mactra grandis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mactra luzonica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Magallana gigas* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Magilus antiquus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mancinella armigera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Marivagia stellata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Matuta planipes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mauritia scurra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Melibe japonica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Melo amphora* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Menathais tuberosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mesactinia ganensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Metadynomene devaneyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Metalia angustus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Metapeachia tropica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Metaprotella sandalensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Metopograpsus oceanicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Micippa platipes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Micromussa pacifica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Micropagurus polynesiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Microprosthema validum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mikadotrochus anseeuwi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Millepora intricata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mimatys fukuokaensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Minnivola pyxidata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Miyakella nepa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Modiolus philippinarum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Monomia lucida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Monoplex mundus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Monoplex vespaceus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Montipora danae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Montipora delicatula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Montipora foveolata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Montipora spongodes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Montipora verruculosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Morbakka virulenta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mycale parishii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mycedium steeni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Myra curtimana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Myra fugax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Myurella affinis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nanosesarma minutum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nassa serta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nassarius acuticostus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nassarius arcularia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nassarius gruneri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nassarius livescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nassarius nodiferus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nassarius reeveanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Natatolana albicaudata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Natica arachnoidea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Natica buriasiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Natica kawamurai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Natica vitellus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Naxioides taurus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neocancilla papilio* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neodorippe callida* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Neofibularia hartmani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neoliomera insularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neopalicus contractus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neopetrosia carbonaria* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Neosarmatium fourmanoiri* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neoxanthias impressus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nerita signata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neritina pulligera* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Neritopsis radula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Netrostoma nuda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Netrostoma setouchianum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neverita didyma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nikoides sibogae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Notopus dorsipes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nototodarus hawaiiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dichelaspis orthogonia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Octotiara russelli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Odontodactylus japonicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oliva chrysoplecta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oliva concavospira* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oliva hirasei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Onithochiton lyellii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Opheodesoma grisea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiarachna delicata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiarachnella macracantha* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophidiaster duncani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophidiaster hemprichi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiocoma echinata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiomastix corallicola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiomastix mixta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiomastix variabilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiomyxa australis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiothrix proteus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ornithoteuthis volatilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Otopleura auriscati* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Otopleura nodicincta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oulophyllia levis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxymeris chlorata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pachygrapsus planifrons* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paguristes longirostris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paguritta corallicola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pagurixus anceps* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pagurixus ruber* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Palaemon debilis* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Palaemon pacificus* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Palinustus waguensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paracondylactis sinensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paradynomene tuberculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paradyte crinoidicola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paralemnalia thyrsoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paraplanocera oligoglena* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paratapes textile* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paraxanthias notatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Patelloida saccharinoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pavona danai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Penaeus latisulcatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Penaeus semisulcatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Penaeus vannamei* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Percnon affine* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pericelis byerleyana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Periclimenes albolineatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Peristernia ustulata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Petrolisthes asiaticus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Petrolisthes pubescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Petrosia strongylata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phalangipus filiformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phalangipus hystrix* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phallusia nigra* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Phanerophthalmus batangas* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Phanerophthalmus perpallidus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phasianella solida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phenacovolva brevirostris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phenacovolva subreflexa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phos blainvillei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phos hirasei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phos sculptilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phronimella elongata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllidia larryi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllocoma convoluta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Physophora hydrostatica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pilumnus scabriusculus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pisania tritonoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Platygyra lamellina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Platymaia bartschi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pleraplysilla flabellum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plesionika narval* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pleuractis taiwanensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pleurehdera haraldi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pleurobranchella nicobarica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polinices albumen* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mammilla simiae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polycarpa contecta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polycyathus fuscomarginatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polydectus cupulifer* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polyphyllia novaehiberniae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polyplectana kefersteinii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Poraster superbus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Porites annae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Porites lichen* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Porites napopora* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Porites rugosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Psammocora digitata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Psammocora exesa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Psammocora stellata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Psaumis cavipes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudograpsus elongatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudohelice subquadrata* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudolambrus tarpeius* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudoporcellanella manoliensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudorhaphitoma alticostata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pterotrachea coronata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pterygia dactylus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pterynotus martinetanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pterynotus tripterus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Puerulus angulatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pupa tessellata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Purpura bufo* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pylopaguropsis keijii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pylopaguropsis lewinsohni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Racilius compressus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rapana rapiformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Remiarctus bertholdii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Renocila loriae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Renocila richardsonae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhinoclavis longicaudata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhinolambrus rudis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhynchocinetes brucei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhynchocinetes conspiciocellus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Salpa fusiformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sandalolitha dentata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sarcophyton glaucum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sarmatium germaini* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Scabricola desetangsii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scabricola variegata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sclerodoris faninozi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scopimera inflata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scyllarides haanii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sepia brevimana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sepiella inermis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sicyonia robusta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Siliqua radiata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Smaragdia pulcherrima* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hiatula diphos* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Soliella flava* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Solmaris flavofinis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sphaerocoryne bedoti* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Sphenopus marsupialis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Spiropagurus fimbriatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Spondylus echinatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Spondylus linguafelis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Spongia agaricina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stenasellus javanicus* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Stenopus cyanoscelis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stenorhynchus seticornis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stichopus naso* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stomatolina rubra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Strigatella zebra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Suberea laboutei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Surrepifungium costulatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Svenzea devoogdae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Swainsonia ocellata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Symplegma rubra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synaptula media* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synaptula reciprocans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synaptula recta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Takedromia longispina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tectus triserialis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Isactinia citrina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cyclotellina discus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phylloda foliacea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tellinella virgata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Terebra laevigata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Terebra quoygaimardi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Testudovolva nipponensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mancinella echinata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thalamita integra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thalamita picta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thenus unimaculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thetys vagina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thordisa sanguinea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thuridilla indopacifica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thuridilla neona* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thylacodes variabilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thyraplax crosnieri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thysanostoma flagellatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thysanozoon nigrum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Timoclea marica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tonna ampullacea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tonna chinensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tonna luteostoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tozeuma serratum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trapania brunnea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trapania japonica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trapania tatsulok* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trapania undulata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trapezia plana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trididemnum polyorchis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trigonostoma thysthlon* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tripedalia cystophora* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trivirostra scabriuscula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tropiometra afra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tropiometra carinata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tubuca capricornis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tucetona auriflua* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tuleariocaris holthuisi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Turbo heterocheilus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Turris garnonsii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Turritopsis dohrnii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ulmaris snelliusi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Urnalana pulchella* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Uroteuthis chinensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Utinomiella dimorpha* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Varicospira crispata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Varuna yui* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Vasticardium elongatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vasticardium papuanum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Venus verrucosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Veronicella cubensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum caffrum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum cookorum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum costatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum deshayesii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum diutenerum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum formosense* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum lyratum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum militare* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum mirabile* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum obeliscus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum radius* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum stainforthii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum unifasciale* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum virgo* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum zebuense* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Viaderiana quadrispinosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Villogorgia nozzolea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Viriola cancellata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Volvarina philippinarum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xenophora cerea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xenophora pallidula* | 1 | Meer | zu wenige Nachweise (1 < 5) |

</details>

### Nicht aufgelöste Namen

<details><summary>1299 Namen</summary>

*Lissachatina fulica* (4471), *Ancylocaris brevicarpalis* (825), *Coryphellina exoptata* (717), *Ancylomenes sarasvati* (555), *Radianthus magnifica* (543), *Amphidromus perversus* (509), *Samla bicolor* (492), *Hypselodoris roo* (478), *Lysiosquilla lisa* (401), *Zenopontonia soror* (397), *Hypselodoris apolegma* (385), *Unidentia sandramillenae* (378), *Hexabranchus lacer* (338), *Longibranchus putnami* (313), *Phycocaris simulans* (299), *Hypselodoris paradisa* (291), *Thecacera pikachu* (283), *Laevicaulis alte* (282), *Goniobranchus leopardus* (260), *Costasiella usagi* (256), *Dardanus sanguinolentus* (248), *Glossodoris buko* (238), *Hypselodoris variobranchia* (236), *Parathelphusa convexa* (233), *Doto ussi* (230), *Plakobranchus papua* (224), *Pseudoceros lindae* (218), *Bermudella brunneomaculata* (213), *Nembrotha purpureolineata* (203), *Parmarion martensi* (202), *Doto greenamyeri* (194), *Haliclona nematifera* (192), *Melibe colemani* (187), *Gelastocaris paronai* (184), *Samla riwo* (181), *Cyclocoeloma tuberculatum* (173), *Amplexidiscus fenestrafer* (168), *Samla bilas* (163), *Hamopontonia fungicola* (152), *Nembrotha lorosae* (151), *Produnga rubropunctata* (143), *Cabangus regius* (139), *Hypselodoris iba* (138), *Trapania palmula* (138), *Cyerce blackburnae* (137), *Asperitas sparsa* (132), *Radianthus doreensis* (132), *Palaemonella colemani* (130), *Fromia heffernani* (125), *Radianthus crispa* (125), *Tenellia puti* (125), *Dendrodoris krusensternii* (119), *Pseudoceros laingensis* (119), *Armina scotti* (118), *Phyllodesmium jakobsenae* (109), *Sarasinula plebeia* (109), *Pseudoceros scintillatus* (108), *Tenellia nakapila* (107), *Austruca perplexa* (106), *Chloeia amphora* (101), *Phyllodesmium iriomotense* (98), *Tomoberthella martensi* (96), *Amphidromus furcillatus* (95), *Ibycus rachelae* (94), *Chloeia bemisae* (93), *Thecacera melkyi* (93), *Doriprismatica balut* (92), *Pachyrhynchia cuppressina* (90), *Ancylomenes luteomaculatus* (88), *Ophiomastix pictum* (88), *Bradybaena similaris* (87), *Cycloporus venetus* (87), *Tenellia bughaw* (87), *Baeolidia moebii* (86), *Tuerkayana hirtipes* (86), *Armina occulta* (84), *Austruca annulipes* (84), *Hypselodoris violacea* (84), *Dermatobranchus funiculus* (83), *Paracorynactis hoplites* (83), *Tyrannodoris luteolineata* (82), *Fromia hemiopla* (81), *Pseudoceros dimidiatus* (81), *Trapezionida olivarae* (80), *Cyerce katiae* (79), *Parathelphusa valida* (79), *Pseudobiceros gloriosus* (79), *Lysmatella prima* (78), *Miamira alleni* (78), *Phyllodesmium tuberculatum* (78), *Gelasimus tetragonon* (75), *Gymnodoris crocea* (72), *Cyerce basi* (71), *Noumeaella rehderi* (71), *Thranita crenata* (70), *Tubuca dussumieri* (70), *Naria labrolineata* (68), *Thylacodes grandis* (68), *Geosesarma noduliferum* (67), *Heteropia minor* (67), *Doriprismatica stellata* (66), *Hypselodoris lacuna* (65), *Janolus savinkini* (64), *Paraleptuca crassipes* (63), *Phyllodesmium pinnatum* (63), *Limenandra confusa* (62), *Marioniopsis arborescens* (62), *Ricordea yuma* (62), *Cuapetes ischiospinosus* (61), *Hypselodoris melanesica* (61), *Austruca triangularis* (59), *Urocaridella degravei* (59), *Exrhysota brookei* (58), *Plesiastrea peroni* (58), *Melibe digitata* (57), *Dermatobranchus caeruleomaculatus* (56), *Acrozoanthus australiae* (55), *Eubranchopsis virginalis* (53), *Massinium magnum* (53), *Pleurobranchus weberi* (50), *Tenellia goniophaga* (49), *Tubuca forcipata* (48), *Naria helvola* (47), *Pelagella longicornis* (47), *Siphopteron tigrinum* (47), *Thuridilla ratna* (47), *Laomenes pardus* (46), *Amphidromus palaceus* (45), *Amphimedon queenslandica* (45), *Mexichromis aurora* (45), *Pseudoceros paralaticlavus* (45), *Pteroeides argenteum* (45), *Ardeadoris averni* (44), *Coryphellina delicata* (44), *Sulcospira testudinaria* (44), *Tubuca coarctata* (44), *Amphidromus poecilochroa* (43), *Cubaris murina* (43), *Paradoris liturata* (43), *Verconia romeri* (43), *Phyllodesmium lizardense* (42), *Rhyssoplax baliensis* (42), *Asteronotus mimeticus* (41), *Conglomeratusclera coerulea* (41), *Acrossota amboinensis* (40), *Dardanus jacquesi* (40), *Kaloplocamus peludo* (40), *Pycnoclavella flava* (40), *Tubuca paradussumieri* (40), *Nymphozoon orsaki* (39), *Rhinocochlis chlorosoma* (39), *Verconia alboannulata* (39), *Discosoma nummiforme* (38), *Leptopoma undatum* (38), *Dardanus longior* (37), *Geosesarma danumense* (37), *Mycale humilis* (37), *Naria miliaris* (37), *Tanychlamys indica* (37), *Aclyvolva coarctata* (36), *Fimbriaphyllia yaeyamensis* (36), *Polybranchia jannae* (36), *Tenellia yamasui* (36), *Hippolyte commensalis* (35), *Naisdoris vitiligata* (35), *Neoferdina insolita* (35), *Plocamopherus pecoso* (35), *Ardeadoris cruenta* (34), *Phyllognathia simplex* (34), *Annulorhina mandapamensis* (33), *Cyerce kikutarobabai* (32), *Hippolyte dossena* (32), *Lipkemenes lanipes* (32), *Naria boivinii* (32), *Pseudobiceros fulgor* (32), *Pseudobiceros kryptos* (32), *Pseudoceros scriptus* (32), *Subulina octona* (32), *Turrilatirus turritus* (32), *Amphidromus martensi* (31), *Cystiscus minutissimus* (31), *Phyllidia haegeli* (31), *Phyllodesmium parangatum* (31), *Pruvotfolia rhodopos* (31), *Pseudoceros concinnus* (31), *Radix rubiginosa* (31), *Tergiposacca longicerata* (31), *Thranita prymna* (31), *Videna metcalfii* (31), *Favites valenciennesi* (30), *Ischnochiton caliginosus* (30), *Geosesarma sabanum* (29), *Ercolania endophytophaga* (28), *Kabeiro rubroreticulata* (28), *Melibe coralophilia* (28), *Pseudoceros gravieri* (28), *Pseudopaguristes kuekenthali* (28), *Testudovolva ericae* (28), *Trapania tora* (28), *Asperitas colorata* (27), *Chirostylus sandyi* (27), *Goniodoridella geminae* (27), *Pseudoceros imitatus* (27), *Rhodactis inchoata* (27), *Arestorides argus* (26), *Hydrozoanthus gracilis* (26), *Lamarcka ventricosa* (26), *Limenandra barnosii* (26), *Palaemonella smiti* (26), *Pellasimnia annabelae* (26), *Sesarmops imperator* (26), *Pseudobiceros splendidus* (25), *Sclerophytum flexibilis* (25), *Trionectes tenuipes* (25), *Micromelo barbarae* (24), *Palaemonella euphyllius* (24), *Siphopteron flavolineatum* (24), *Haliclona acoroides* (23), *Lysiosquilla sulcata* (23), *Microparmarion simrothi* (23), *Palmadusta clandestina* (23), *Phyllidia marindica* (23), *Pseudobiceros hymanae* (23), *Abronica payaso* (22), *Crenavolva aureola* (22), *Diminovula concinna* (22), *Habuprionovolva basilia* (22), *Izucaris masudai* (22), *Pseudobiceros gratus* (22), *Pseudoceros susanae* (22), *Sinanodonta pacifica* (22), *Eubranchus ocellatus* (21), *Pelagella albopunctata* (21), *Pelagella joubini* (21), *Pseudoceros contrarius* (21), *Siphopteron nakakatuwa* (21), *Amphimedon sulcata* (20), *Hamopontonia physogyra* (20), *Hemiplecta humphreysiana* (20), *Maculastrombus mutabilis* (20), *Pinnigorgia flava* (20), *Pseudoceros agattiensis* (20), *Pseudoceros meenae* (20), *Pseudoceros rubronanus* (20), *Ransoniella punctata* (20), *Tenellia viei* (20), *Thranita danae* (20), *Amphidromus porcellanus* (19), *Ceratodoris nakamotoensis* (19), *Costasiella formicaria* (19), *Dermatobranchus pustulosus* (19), *Haliclona hooperi* (19), *Knopia octocontacanalis* (19), *Maritigrella fuscopunctata* (19), *Phyllodesmium undulatum* (19), *Sistrum ricinus* (19), *Coenobita lila* (18), *Elysia aowthai* (18), *Marioniopsis elongoreticulata* (18), *Rhodactis bryoides* (18), *Tanea undulata* (18), *Amphimedon paraviridis* (17), *Clathria mima* (17), *Doto racemosa* (17), *Filopaludina javanica* (17), *Gomophia egeriae* (17), *Janolus tricellariodes* (17), *Mariaella dussumieri* (17), *Pilsbryoconcha exilis* (17), *Pseudoceros prudhoei* (17), *Strepsichordaia lendenfeldi* (17), *Thranita pseudopelsarti* (17), *Amphidromus contrarius* (16), *Bursatella ocelligera* (16), *Caementabunda simplex* (16), *Ceratodoris kendi* (16), *Dermatobranchus tuberculatus* (16), *Edwardsianthus sapphirus* (16), *Leucetta avocada* (16), *Maritigrella virgulata* (16), *Sagaminopteron pohnpei* (16), *Tubuca demani* (16), *Tuerkayana magnum* (16), *Tytthosoceros lizardensis* (16), *Actinimenes ornatellus* (15), *Armina rubida* (15), *Cryptopodia dorsalis* (15), *Dermatobranchus kalyptos* (15), *Dermatobranchus phyllodes* (15), *Everettia subconsul* (15), *Hallaxa hileenae* (15), *Hayashidonus japonicus* (15), *Phyllidiella hageni* (15), *Thranita coeruleipes* (15), *Thranita spinimana* (15), *Trapania euryeia* (15), *Tubuca bellator* (15), *Unomia stolonifera* (15), *Anentome helena* (14), *Astropecten sumbawanus* (14), *Dulcerana granularis* (14), *Edwardsianthus gilbertensis* (14), *Gymnodoris feyae* (14), *Marionia distincta* (14), *Paguritta morgani* (14), *Platyzoanthus mussoides* (14), *Pseudoceros microcelis* (14), *Rhinocochlis nasuta* (14), *Sarika siamensis* (14), *Semperula wallacei* (14), *Stephanogorgia diomedea* (14), *Tambja kava* (14), *Asterophilia carlae* (13), *Hiatavolva depressa* (13), *Kabeiro christianae* (13), *Leptopoma lowi* (13), *Leptopoma perlucidum* (13), *Leptopoma sericatum* (13), *Myurellopsis undulata* (13), *Percnon sinense* (13), *Phanerophthalmus anettae* (13), *Pseudoceros duplicinctus* (13), *Pseudoceros goslineri* (13), *Ryssota otaheitana* (13), *Trapania caerulea* (13), *Tuerkayana rotundum* (13), *Zosimus maculatus* (13), *Amonovula piriei* (12), *Gastropteron bicornutum* (12), *Haliclona milnei* (12), *Heliopora hiberniana* (12), *Miamira flavicostata* (12), *Miamira moloch* (12), *Mycale regularis* (12), *Neoferdina oni* (12), *Neozoanthus uchina* (12), *Ophiopsila polyacantha* (12), *Oxynoe jordani* (12), *Pardalinops testudinarius* (12), *Pseudoceros leptostictus* (12), *Ptilocaulis spiculifer* (12), *Thordisa villosa* (12), *Zoanthus vietnamensis* (12), *Ceratodoris kondoi* (11), *Coenobita longitarsis* (11), *Conus epistomium* (11), *Dermatobranchus striatus* (11), *Doriprismatica paladentata* (11), *Episesarma lafondii* (11), *Eurypatagus ovalis* (11), *Geosesarma aedituens* (11), *Halgerda indotessellata* (11), *Isarachnanthus bandanensis* (11), *Kabeiro phasmida* (11), *Mexichromis katalexis* (11), *Neosarmatium asiaticum* (11), *Noalda* (11), *Oliva keenii* (11), *Parasesarma indiarum* (11), *Philinopsis ctenophoraphaga* (11), *Platydoris sabulosa* (11), *Quantula striata* (11), *Aegires flores* (10), *Chloraea fibula* (10), *Cyclophorus perdix* (10), *Dermatobranchus rodmani* (10), *Eclogavena quadrimaculata* (10), *Gelasimus jocelynae* (10), *Geosesarma aurantium* (10), *Latreutes bicornis* (10), *Leptopoma lamellatum* (10), *Lupocyclus rotundatus* (10), *Mariaglaja alexisi* (10), *Pseudoceros rubrotentaculatus* (10), *Sundathelphusa longipes* (10), *Testudovolva orientis* (10), *Thranita pelsarti* (10), *Trapania reticulata* (10), *Baeolidia variabilis* (9), *Baptozius vinosus* (9), *Bistolida hirundo* (9), *Caloria militaris* (9), *Cyrtulus undatus* (9), *Dendronephthya* (9), *Dermatobranchus fasciatus* (9), *Echineulima asthenosomae* (9), *Edwardsianthus pudicus* (9), *Goniobranchus conchyliatus* (9), *Haliclona vanderlandi* (9), *Hermania orca* (9), *Hydrozoanthus sils* (9), *Latona bicolor* (9), *Lissocarcinus polybioides* (9), *Litophyton* (9), *Nerita balteata* (9), *Parasesarma peninsulare* (9), *Parathelphusa pardus* (9), *Pseudobiceros damawan* (9), *Ricinella rubusidaeus* (9), *Shinobium trapezoideum* (9), *Stereosoma celebense* (9), *Tubuca rosea* (9), *Valiguna flava* (9), *Aeolidiopsis ransoni* (8), *Anachis fasciata* (8), *Avaldesia tahala* (8), *Clavularia viridis* (8), *Coralliocaris sandyi* (8), *Dermatobranchus semilunus* (8), *Dolomena turturella* (8), *Episesarma chentongense* (8), *Goniosupradens obtusifrons* (8), *Hermaea* (8), *Leptopoma moussoni* (8), *Lissocarcinus arkati* (8), *Mieniplotia scabra* (8), *Ministrombus variabilis* (8), *Novaeolidiella janae* (8), *Obba rota* (8), *Parathelphusa bogorensis* (8), *Phyllodesmium pecten* (8), *Platydoris ocellata* (8), *Pylopaguropsis speciosa* (8), *Alcyonosyllis phili* (7), *Caridina brevicarpalis* (7), *Cerberilla annulata* (7), *Clarkcomanthus mirabilis* (7), *Corbicula javanica* (7), *Cryptoplax oculata* (7), *Dermatobranchus gonatophorus* (7), *Dolomena epidromis* (7), *Elaphroconcha javacensis* (7), *Eupatagus rubellus* (7), *Filicaulis bleekeri* (7), *Filifusus filamentosus* (7), *Godiva* (7), *Hecuba reticulata* (7), *Hyastenus bispinosus* (7), *Hypselodoris perii* (7), *Hypselodoris sagamiensis* (7), *Latirolagena smaragdulus* (7), *Meghimatium striatum* (7), *Melo aethiopicus* (7), *Ministrombus minimus* (7), *Myurella pertusa* (7), *Neostylodactylus litoralis* (7), *Okenia rhinorma* (7), *Oliva mantichora* (7), *Pleurobranchus mamillatus* (7), *Pseudoceros vishnui* (7), *Pteria heteroptera* (7), *Ranularia gutturnia* (7), *Scopalina hapalia* (7), *Scyllaea fulva* (7), *Terrathelphusa chilensis* (7), *Terrathelphusa kuhlii* (7), *Trapania squama* (7), *Tubulophilinopsis lineolata* (7), *Xenia* (7), *Actinimenes ornatus* (6), *Aliculastrum debile* (6), *Annulobalcis maculata* (6), *Asperitas nemorensis* (6), *Caridina caerulea* (6), *Caridina longidigita* (6), *Charybdis lucifer* (6), *Conus alexandrei* (6), *Conus amplus* (6), *Corymorpha tropica* (6), *Cubaris insularis* (6), *Cyerce goodheartae* (6), *Elysia asbecki* (6), *Heteronucia perlata* (6), *Hexabranchus giganteus* (6), *Iciligorgia brunnea* (6), *Labuanium politum* (6), *Limenandra fusiformis* (6), *Malayopotamon brevimarginatum* (6), *Marioniopsis elongoviridis* (6), *Melicerona listeri* (6), *Miersarma granosimanum* (6), *Monoplex comptus* (6), *Moridilla jobeli* (6), *Naviculavolva deflexa* (6), *Nerita trifasciata* (6), *Ocypode sinensis* (6), *Parmunculus philippinensis* (6), *Phrikoceros katoi* (6), *Phyllidia fontjei* (6), *Phyllodesmium karenae* (6), *Scandarma splendidum* (6), *Siphopteron ladrones* (6), *Thorunna africana* (6), *Acanthozoon alderi* (5), *Agaronia lutaria* (5), *Allopeas gracile* (5), *Alpheus rubromaculatus* (5), *Anachis terpsichore* (5), *Anthopleura buddemeieri* (5), *Arcania tropicalis* (5), *Bermudella japonica* (5), *Caridina ensifera* (5), *Chloeia incerta* (5), *Clathrina purpurea* (5), *Conus balabacensis* (5), *Deroceras laeve* (5), *Discosoma dawydoffi* (5), *Doris nucleola* (5), *Dragmacidon australe* (5), *Dyakia rumphii* (5), *Emerita emeritus* (5), *Entacmaea medusivora* (5), *Grapsodes notatus* (5), *Haliclona peixinhoae* (5), *Helicostyla rufogaster* (5), *Helicostyla smaragdina* (5), *Indoplanorbis exustus* (5), *Lamarcka avellana* (5), *Longibrachium arariensis* (5), *Macrophthalmus pacificus* (5), *Marosina serratirostris* (5), *Martadoris limaciformis* (5), *Matuta purnama* (5), *Meghimatium pictum* (5), *Monomia petrea* (5), *Naisdoris liklik* (5), *Nebularia eremitarum* (5), *Nebularia ferruginea* (5), *Nerita grossa* (5), *Optediceros breviculum* (5), *Oxymetra finschii* (5), *Pagurixus vicinus* (5), *Pharodoris philippinensis* (5), *Pherecardia distincta* (5), *Philinopsis buntot* (5), *Phyllidiella albonigra* (5), *Pila ampullacea* (5), *Pliopontonia harazakii* (5), *Pseudoceros imperatus* (5), *Siphopteron nigromarginatum* (5), *Stenoplax alata* (5), *Tenellia minor* (5), *Vercoia interrupta* (5), *Acanthosepion aculeatum* (4), *Aegires malinus* (4), *Aldisa williamsi* (4), *Amphidromus filozonatus* (4), *Amphidromus latestrigatus* (4), *Archivolva clava* (4), *Asperitas bimaensis* (4), *Asperitas trochus* (4), *Asterophilia culcitae* (4), *Atagema ornata* (4), *Basilometra boschmai* (4), *Callioplana marginata* (4), *Caridina dennerli* (4), *Caridina endehensis* (4), *Celetaia persculpta* (4), *Cellana cylindrica* (4), *Clypidina notata* (4), *Corymorpha balssi* (4), *Cyclophorus linguiferus* (4), *Diminovula whitworthi* (4), *Dolomena vittata* (4), *Doris immonda* (4), *Gastropteron multo* (4), *Geosesarma batak* (4), *Geosesarma cikaniki* (4), *Geosesarma hagen* (4), *Goniosupradens hawaiensis* (4), *Gyroscala commutata* (4), *Hastula acumen* (4), *Hastula raphanula* (4), *Hemiplecta densa* (4), *Herviella claror* (4), *Hypselodoris rositoi* (4), *Iotrochota sinki* (4), *Limenandra rosanae* (4), *Lobodillo flavus* (4), *Luidia sibogae* (4), *Maritigrella eschara* (4), *Melibe tuberculata* (4), *Myurella pygmaea* (4), *Naria eburnea* (4), *Naria gangranosa* (4), *Neosarmatium rotundifrons* (4), *Pagurus fungiformis* (4), *Parasesarma lanchesteri* (4), *Parathelphusa linduensis* (4), *Parathelphusa pantherina* (4), *Parazoanthus aruensis* (4), *Philine orientalis* (4), *Plakobranchus noctisstellatus* (4), *Platydoris inframaculata* (4), *Pleurolidia juliae* (4), *Protodendron repens* (4), *Pseudoceros jebborum* (4), *Pseudonebularia fraga* (4), *Roxaniella pittmani* (4), *Sagaminopteron multimaculatum* (4), *Saidjahus guttatus* (4), *Sakuraeolis kirembosa* (4), *Samla macassarana* (4), *Scleronephthya* (4), *Sclerophytum pocilloporaeformis* (4), *Syntripsa matannensis* (4), *Tegulaplax hululensis* (4), *Tenellia acinosa* (4), *Terpios hoshinota* (4), *Thuridilla moebii* (4), *Vexillum mccauslandi* (4), *Vittina variegata* (4), *Vojmirophthalmus minabensis* (4), *Acanthozoon fuscobulbosum* (3), *Aegires lemoncello* (3), *Alaerato palawanica* (3), *Aldisa erwinkoehleri* (3), *Amphidromus adamsii* (3), *Amphidromus enganoensis* (3), *Amphidromus inversus* (3), *Amphidromus javanicus* (3), *Amphidromus pictus* (3), *Anapagurus japonicus* (3), *Annulobalcis vinaria* (3), *Anteaeolidiella cacaotica* (3), *Arachnothelphusa terrapes* (3), *Arakawania marginalba* (3), *Arcania sagamiensis* (3), *Asterospicularia randalli* (3), *Astropecten javanicus* (3), *Atergatopsis germainii* (3), *Atyopsis moluccensis* (3), *Bermudella purpureolineata* (3), *Bornella dotoides* (3), *Bradybaena fodiens* (3), *Breviturma pica* (3), *Breviturma securis* (3), *Calappa quadrimaculata* (3), *Caridina acutirostris* (3), *Caridina fusca* (3), *Caridina laoagensis* (3), *Caridina loehae* (3), *Caridina siamensis* (3), *Casmaria turgida* (3), *Chaenostoma crassimanus* (3), *Charybdis padangensis* (3), *Clibanarius antennatus* (3), *Coenobita pseudorugosus* (3), *Conus beatrix* (3), *Conus blatteus* (3), *Conus bocki* (3), *Corticium niger* (3), *Crella erecta* (3), *Crenavolva matsumiyai* (3), *Cyclophorus woodianus* (3), *Cycloscala peaseana* (3), *Demania splendida* (3), *Diacarnus tubifera* (3), *Doratosepion andreanum* (3), *Drachiella angulata* (3), *Eclogavena coxeni* (3), *Elysia thompsoni* (3), *Elysia trilobata* (3), *Erronea adusta* (3), *Galathea senta* (3), *Gelliodes wilsoni* (3), *Geosesarma confertum* (3), *Geosesarma lebak* (3), *Gymnodoris brunnea* (3), *Imbricaria rufogyrata* (3), *Insulamon palawanense* (3), *Isolapotamon ingeri* (3), *Jagora asperata* (3), *Kalamantania whiteheadi* (3), *Kaloplocamus dokte* (3), *Kaloplocamus maru* (3), *Landouria menorehensis* (3), *Lepidonotus oculatus* (3), *Leptopoma multilabre* (3), *Madrella amphora* (3), *Mariaglaja mandroroa* (3), *Meghimatium bilineatum* (3), *Mourgona* (3), *Nebularia contracta* (3), *Ocypode urvillii* (3), *Oliva multiplicata* (3), *Palio gaeli* (3), *Parasphaerasclera grayi* (3), *Parathelphusa celebensis* (3), *Parathelphusa sarasinorum* (3), *Patelloida garuda* (3), *Phenacovolva rehderi* (3), *Phrikoceros baibaiye* (3), *Phyllodesmium lembehense* (3), *Physalia mikazuki* (3), *Placida barackobamai* (3), *Plakortis badabaluensis* (3), *Prostheceraeus fuscolineatus* (3), *Pseudoceros bolool* (3), *Pseudoceros gamblei* (3), *Pseudoceros monostichos* (3), *Punctacteon flammeus* (3), *Quasimitra cardinalis* (3), *Rapipontonia paragalene* (3), *Rhinolambrus turriger* (3), *Rhynchotrochus taylorianus* (3), *Sabellastarte australiensis* (3), *Sapphirina* (3), *Saron rectirostris* (3), *Sclerodoris rubicunda* (3), *Siphopteron dumbo* (3), *Siphopteron leah* (3), *Syntripsa flavichela* (3), *Tayuva coerulescens* (3), *Tenellia fuscostriata* (3), *Tenellia poritophages* (3), *Thor leptochelus* (3), *Trichomya hirsuta* (3), *Tylomelania robusta* (3), *Tylomelania scalariopsis* (3), *Verconia laboutei* (3), *Weinkauffia reliqua* (3), *Actinimenes inornatus* (2), *Aegires incusus* (2), *Aegires petalis* (2), *Aldisa albatrossae* (2), *Alpheus richardsoni* (2), *Amphidromus atricallosus* (2), *Amphidromus djajasasmitai* (2), *Amphidromus sinistralis* (2), *Anadara fultoni* (2), *Arakawania granulata* (2), *Ariophanta exilis* (2), *Aspastus miltocheilus* (2), *Asteronotus spongicolus* (2), *Astroboa ernae* (2), *Avaldesia albomacula* (2), *Breviturma dentata* (2), *Bufonaria elegans* (2), *Calappa liaoi* (2), *Calycia isseliana* (2), *Caridina peninsularis* (2), *Caridina spinata* (2), *Caridina sulawesi* (2), *Carminodoris nodulosa* (2), *Ceratodoris plana* (2), *Ceratodoris virginiae* (2), *Cherax boesemani* (2), *Cladocoryne spongicola* (2), *Clathrina luteoculcitella* (2), *Clivipollia incarnata* (2), *Contradusta bregeriana* (2), *Conus nicobaricus* (2), *Cornu aspersum* (2), *Coryphellina iurmanovi* (2), *Costacallista erycina* (2), *Cryptopodia laevimana* (2), *Cucullaearca foliata* (2), *Dendrodoris atromaculata* (2), *Dermatobranchus cymatilis* (2), *Dermatobranchus dendronephthyphagus* (2), *Diogenes holthuisi* (2), *Discomya radulosa* (2), *Discoplax gracilipes* (2), *Doto gaeli* (2), *Dyakia hugonis* (2), *Epitonium grayi* (2), *Epitonium yangi* (2), *Facelina bourailli* (2), *Forcepia vansoesti* (2), *Fromia nodosa* (2), *Geosesarma dennerle* (2), *Geosesarma hednon* (2), *Geosesarma riani* (2), *Geotrochus bicolor* (2), *Goniodoridella unidonta* (2), *Goodingia capillastericola* (2), *Gulella bicolor* (2), *Gymnodoris pseudobrunnea* (2), *Gyraulus convexiusculus* (2), *Habuprionovolva umbilicata* (2), *Hamineobulla kawamurai* (2), *Hantazuia kimotoi* (2), *Haptosquilla nefanda* (2), *Helicobulinus sarcinosa* (2), *Hemiplecta weberi* (2), *Hesione uchidai* (2), *Ilyella gigas* (2), *Isolapotamon seowi* (2), *Kuroshiovolva lacanientae* (2), *Laomenes cornutus* (2), *Latirus philberti* (2), *Latona solida* (2), *Lens contradens* (2), *Lepidothelphusa padawan* (2), *Leptopoma atricapillum* (2), *Loimia tuberculata* (2), *Lotoria triangularis* (2), *Lysmata rauli* (2), *Lytocarpia phyteuma* (2), *Macrobrachium leucodactylus* (2), *Macrobrachium spinipes* (2), *Macrophiothrix rhabdota* (2), *Mactra dissimilis* (2), *Maritigrella makranica* (2), *Microparmarion exquadratus* (2), *Mnestia villica* (2), *Naisdoris aurornata* (2), *Naria poraria* (2), *Nautilothelphusa zimmeri* (2), *Neozoanthus caleyi* (2), *Nerita incerta* (2), *Niparaya* (2), *Obba listeri* (2), *Odontozona ensifera* (2), *Oliva guttata* (2), *Oliva vicweei* (2), *Pagurus decimbranchiae* (2), *Palmadusta humphreyii* (2), *Palola viridis* (2), *Panderevela* (2), *Papustyla pulcherrima* (2), *Paraferdina laccadivensis* (2), *Parasesarma exquisitum* (2), *Parathelphusa ferruginea* (2), *Phanerophthalmus albotriangulatus* (2), *Phanerophthalmus lentigines* (2), *Phenacovolva barbieri* (2), *Phrikoceros fritillus* (2), *Phyllaplysia viridis* (2), *Phyllidia alyta* (2), *Phyllidia ovata* (2), *Pirenella cingulata* (2), *Platydoris pulchra* (2), *Pleurehdera postrema* (2), *Plocamopherus margaretae* (2), *Primovula tadashigei* (2), *Pseudobiceros stellae* (2), *Pseudoceros intermittus* (2), *Pseudoceros mossambicus* (2), *Pterocyclos tenuilabiatus* (2), *Quasimitra nubila* (2), *Rachis zonulata* (2), *Rectidens orientalis* (2), *Rhinolambrus lippus* (2), *Rhynchotrochus jucundus* (2), *Rhytisma fulvum* (2), *Roboastra tentaculata* (2), *Scalptia obliquata* (2), *Sculpsitechinus tenuissimus* (2), *Septaria cumingiana* (2), *Sesarmops mora* (2), *Siphonaria viridis* (2), *Siphopteron vermiculum* (2), *Spinophallus coronatus* (2), *Stenomelania torulosa* (2), *Synaptula rosea* (2), *Talitroides topitotum* (2), *Tanychlamys hippocastaneum* (2), *Terebra tricolor* (2), *Terestrombus fragilis* (2), *Thuridilla kathae* (2), *Tokoyo eburnea* (2), *Tortulosa sumatrana* (2), *Verconia verconiforma* (2), *Vexillum amentare* (2), *Vexillum obtusispinosum* (2), *Vittina semiconica* (2), *Xesta citrina* (2), *Abronica turon* (1), *Acanthocyclops* (1), *Acanthogorgia* (1), *Acanthosepion esculentum* (1), *Acochlidium* (1), *Acrosterigma attenuatum* (1), *Acrosterigma biradiatum* (1), *Actiomera erythra* (1), *Acusta despecta* (1), *Aegiochus vigilans* (1), *Aeolidiopsis harrietae* (1), *Agnara* (1), *Alcomaja nagashimaensis* (1), *Alcyonosyllis hinterkircheri* (1), *Alertigorgia hoeksemai* (1), *Allopeas clavulinum* (1), *Amarinus pumilus* (1), *Amphidromus alicetandiasae* (1), *Amphidromus columellaris* (1), *Amphidromus laevus* (1), *Amphidromus maculiferus* (1), *Amphidromus quadrasi* (1), *Amphidromus reflexilabris* (1), *Amphidromus stevenliei* (1), *Amphidromus sumatranus* (1), *Anadara hankeyana* (1), *Anadara setigericosta* (1), *Anadara subrubra* (1), *Anapagrides facetus* (1), *Ancylomenes aesopius* (1), *Angaria exasperata* (1), *Angaria javanica* (1), *Anilocra boucheti* (1), *Annulobalcis wareni* (1), *Antennellopsis integerrima* (1), *Anthogorgia caerulea* (1), *Antipathozoanthus remengesaui* (1), *Aplysia atromarginata* (1), *Arachnothelphusa kadamaiana* (1), *Architectonica taylori* (1), *Arion ater* (1), *Armina major* (1), *Ascidiophilus caphyraeformis* (1), *Asperitas everetti* (1), *Astropecten alatus* (1), *Atergatis ocyroe* (1), *Atopos smithi* (1), *Avaldesia tamatoa* (1), *Baeolidia gracilis* (1), *Baeolidia japonica* (1), *Bakawan fusca* (1), *Bermudella pellucida* (1), *Berndtia purpurea* (1), *Borneosa* (1), *Bouchetitrochus gotoi* (1), *Breviturma krohi* (1), *Bulaceros porcellanus* (1), *Bunga payung* (1), *Callistocypraea leucodon* (1), *Callochiton subsulcatus* (1), *Calocochlea festiva* (1), *Calocochlea harfordii* (1), *Canarium elegans* (1), *Canarium incisum* (1), *Canarium orrae* (1), *Caphyra yookadai* (1), *Carcinoplax haswelli* (1), *Carcinoplax nana* (1), *Caridina appendiculata* (1), *Caridina gracilipes* (1), *Caridina marlenae* (1), *Caridina mayamareenae* (1), *Caridina poso* (1), *Caridina sarasinorum* (1), *Caridina schenkeli* (1), *Caridina spongicola* (1), *Caridina tenuirostris* (1), *Caridina woltereckae* (1), *Carijoa* (1), *Carinomitra peculiaris* (1), *Carpiscula procera* (1), *Carupa ohashii* (1), *Ceratodoris lambat* (1), *Ceratodoris pilosa* (1), *Ceratophyllidia* (1), *Ceratosoma bicolor* (1), *Cerianthus filiformis* (1), *Cerithidea quoyii* (1), *Chalaroachaeus curvipes* (1), *Cherax lorentzi* (1), *Cherax peknyi* (1), *Cherusius triunguiculatus* (1), *Chicoreus miyokoae* (1), *Chicoreus paini* (1), *Chloraea dryope* (1), *Chloraea psittacina* (1), *Chloritis dentrecasteauxi* (1), *Cirolana willeyi* (1), *Clathrina stipitata* (1), *Clibanarius harisi* (1), *Clistocoeloma villosum* (1), *Clithon bicolor* (1), *Clithon sowerbianum* (1), *Coccogranula prillwitzi* (1), *Coenobita spinosus* (1), *Condylomitra bernhardina* (1), *Coneuplecta calculosa* (1), *Contusarma bocourti* (1), *Contusarma cheirogonum* (1), *Conus brettinghami* (1), *Conus buxeus* (1), *Conus cebuensis* (1), *Conus leobottonii* (1), *Coralastele pulcherrima* (1), *Costasiella paweli* (1), *Crambionella helmbiru* (1), *Crassispira cerithina* (1), *Cratena affinis* (1), *Crimora lutea* (1), *Cristimenes commensalis* (1), *Cryptaegis pilsbryi* (1), *Crystallopsis aphrodite* (1), *Crystallopsis hunteri* (1), *Cuspivolva pulcherrima* (1), *Cycloachelous orbicularis* (1), *Cyclophorus tigrinus* (1), *Cyclophorus validus* (1), *Cycloscala armata* (1), *Cyclotus discoideus* (1), *Daldorfia triangularis* (1), *Damayantia carinata* (1), *Dendrotrochus helicinoides* (1), *Dentarene loculosa* (1), *Dermatobranchus diagonalis* (1), *Dermatobranchus kokonas* (1), *Desmaulus extinctorium* (1), *Dicranodromia robusta* (1), *Dictyodendrilla dendyi* (1), *Diodora sieboldii* (1), *Diogenes moosai* (1), *Diplosoma gumavirens* (1), *Ditropopsis biroi* (1), *Dolomena plicata* (1), *Dolomena succincta* (1), *Dominamaria kowaldi* (1), *Domiporta praestantissima* (1), *Doriprismatica sibogae* (1), *Dyakia clypeus* (1), *Eclogavena dayritiana* (1), *Eclogavena interrupta* (1), *Ecmanis ignea* (1), *Elysia expansa* (1), *Elysia yaeyamana* (1), *Emarginella incisura* (1), *Engina cronuchorda* (1), *Epitonium eximium* (1), *Epitonium sakuraii* (1), *Epitonium schoedei* (1), *Ercolania annelyleorum* (1), *Erronea melanesiae* (1), *Euclosiana scitula* (1), *Eudistoma diasterum* (1), *Euryxanthops flexidentatus* (1), *Euthymella kosugei* (1), *Everettia jucundior* (1), *Everettia paulbasintali* (1), *Farrea* (1), *Fasciarma fasciatum* (1), *Favorinus pacificus* (1), *Ficus variegata* (1), *Filopaludina sumatrensis* (1), *Fragum whitleyi* (1), *Galilia petricola* (1), *Gelasimus vomeris* (1), *Geosesarma ambawang* (1), *Geosesarma nigripes* (1), *Geosesarma rathbunae* (1), *Gomophia sphenisci* (1), *Goniobranchus bimaensis* (1), *Halgerda aurantiomaculata* (1), *Halgerda bacalusia* (1), *Halgerda diaphana* (1), *Haliclona cnidata* (1), *Haliclona osiris* (1), *Hallaxa translucens* (1), *Hancockia* (1), *Haplosyllis anthogorgicola* (1), *Helicostyla fasciata* (1), *Hesione paulayi* (1), *Hippolyte catagrapha* (1), *Holthuisana festiva* (1), *Hoplodoris desmoparypha* (1), *Hypselodoris jacksoni* (1), *Idiomysis japonica* (1), *Imbricaria bacillum* (1), *Indianastra sarasini* (1), *Inozonites retardatus* (1), *Isolapotamon anomalum* (1), *Isolapotamon mahakkamense* (1), *Japonia ciliocincta* (1), *Karstarma ardea* (1), *Karstarma jacobsoni* (1), *Karstarma sulu* (1), *Karstarma waigeo* (1), *Laevistrombus liveranii* (1), *Lambis indomaris* (1), *Lamprotula leaii* (1), *Latona ticaonica* (1), *Launsina tanyae* (1), *Lemnalia* (1), *Leporicypraea valentia* (1), *Leptodius affinis* (1), *Leptodius australis* (1), *Leptopoma crenilabre* (1), *Leptopoma diplochilus* (1), *Leptopoma leucorhaphe* (1), *Leptopoma pileus* (1), *Limicolaria flammea* (1), *Limnasterias oinops* (1), *Lobophytum patulum* (1), *Lucilina sowerbyi* (1), *Lucilina variegata* (1), *Macridiscus donacinus* (1), *Macrorhynchia balei* (1), *Mactrinula plicataria* (1), *Maculastrombus microurceus* (1), *Malayopotamon granulatum* (1), *Margovula anulata* (1), *Margovula marginata* (1), *Margovula somaliensis* (1), *Marionia olivacea* (1), *Marmaronchis vaigiensis* (1), *Marmorofusus nicobaricus* (1), *Medioantenna variopinta* (1), *Megalacron admiralitatis* (1), *Meghimatium uniforme* (1), *Melo georginae* (1), *Merguia oligodon* (1), *Mesanella monochroa* (1), *Metaplax crenulata* (1), *Microparmarion basifixus* (1), *Microparmarion pollonerai* (1), *Mictyris brevidactylus* (1), *Mimachlamys punctata* (1), *Miratesta celebensis* (1), *Moridilla hermanita* (1), *Munidopsis plumatisetigera* (1), *Mursia danigoi* (1), *Myja longicornis* (1), *Myra biconica* (1), *Mytella strigata* (1), *Myurella bilineata* (1), *Myurellopsis parkinsoni* (1), *Myurellopsis paucistriata* (1), *Nakamigawaia spiralis* (1), *Nassarius graphiterus* (1), *Naviculavolva kurziana* (1), *Nemalecium caeruleus* (1), *Neocancilla rufescens* (1), *Neocaridina davidi* (1), *Neoernsta citrea* (1), *Neoernsta klautauae* (1), *Neparilia tuberculata* (1), *Nerita ocellata* (1), *Nodolatirus nodatus* (1), *Nodolatirus recurvirostrus* (1), *Noumeaella isa* (1), *Ocypode nobilii* (1), *Odontonia rufopunctata* (1), *Odontosyllis marombibooral* (1), *Odontozona crinoidicola* (1), *Ogeramua ogeramuensis* (1), *Oliva buelowi* (1), *Oliva dactyliola* (1), *Ophioplocus giganteus* (1), *Opisthoporus biciliatus* (1), *Oscarella ochreacea* (1), *Oxynoe jacksoni* (1), *Pachycerianthus maua* (1), *Pacifilux rubra* (1), *Paguritta kroppi* (1), *Papustyla chancei* (1), *Papustyla hindei* (1), *Paraleonnates bolus* (1), *Paraplanocera marginata* (1), *Parasesarma kuekenthali* (1), *Parasesarma lividum* (1), *Parathelphusa pallida* (1), *Parathelphusa pareparensis* (1), *Parathelphusa possoensis* (1), *Parathelphusa torta* (1), *Parilia major* (1), *Partula grisea* (1), *Partula micans* (1), *Paryphantopsis abstrusa* (1), *Paryphantopsis bradleyi* (1), *Paryphantopsis fragilicosta* (1), *Paryphantopsis koragae* (1), *Paryphantopsis lebasii* (1), *Paryphantopsis louisiadarum* (1), *Paryphantopsis misimensis* (1), *Paryphantopsis nucella* (1), *Paryphantopsis ubwamensis* (1), *Paryphantopsis vanatinensis* (1), *Paryphantopsis yawii* (1), *Paryphantopsis yelensis* (1), *Pelagella balanoyensis* (1), *Pellasimnia angasi* (1), *Periclimenes dardanicola* (1), *Perisserosa guttata* (1), *Peristernia castanoleuca* (1), *Petasometra clarae* (1), *Phalium fimbria* (1), *Phanerophthalmus cerverai* (1), *Phanerophthalmus purpura* (1), *Phenacovolva nectarea* (1), *Phidiana semidecora* (1), *Philine dentiphallus* (1), *Philine elegans* (1), *Philine verdensis* (1), *Philinopsis aliciae* (1), *Phyllacanthus longispinus* (1), *Phyllamphion elegans* (1), *Phyllidia goslineri* (1), *Phyllidia multituberculata* (1), *Phyllidia rueppelii* (1), *Phymanthus* (1), *Physunio superbus* (1), *Pilsbryoconcha expressa* (1), *Platevindex martensi* (1), *Plaxiphora tricolor* (1), *Plicopurpura columellaris* (1), *Polyodontes kuroshio* (1), *Pomacea maculata* (1), *Prodotia lannumi* (1), *Protaeolidiella atra* (1), *Protoelongata corallina* (1), *Protoreaster nodulosus* (1), *Pseudobiceros flavocanthus* (1), *Pseudobiceros mikros* (1), *Pseudobiceros periculosus* (1), *Pseudobiceros sharroni* (1), *Pseudoceros auranticrinis* (1), *Pseudoceros confusus* (1), *Pseudoceros cruentus* (1), *Pseudoceros josei* (1), *Pseudoceros velutinus* (1), *Pseudocorynactis tuberculata* (1), *Pseudodon vondembuschianus* (1), *Pseudolambrus longispinosus* (1), *Pseudonebularia cucumerina* (1), *Pseudophiline hayashii* (1), *Pterygia conus* (1), *Quasimitra puncticulata* (1), *Ralpharia parasitica* (1), *Ranularia sarcostoma* (1), *Raybaudia porteri* (1), *Reductoniscus* (1), *Renocila bijui* (1), *Reticulidia suzanneae* (1), *Reticunassa poppeorum* (1), *Reticutriton pfeifferianus* (1), *Rhizophysa eysenhardtii* (1), *Rhyssoplax densilirata* (1), *Rhyssoplax pulcherrima* (1), *Saidjahus creper* (1), *Satsuma batanica* (1), *Scabricola olivaeformis* (1), *Scabricola vicdani* (1), *Scandarma gracilipes* (1), *Sciurella indivisa* (1), *Septa flaveola* (1), *Septa occidentalis* (1), *Septaria sanguisuga* (1), *Seulocia vittata* (1), *Simpsonella gracilis* (1), *Siphonaria alba* (1), *Siphopteron flavum* (1), *Spondylus lamarckii* (1), *Stelgistra stormi* (1), *Stephanogorgia wainwrighti* (1), *Strigilla grasi* (1), *Stylaster* (1), *Sundathelphusa molluscivora* (1), *Sundathelphusa waray* (1), *Sunetta meroe* (1), *Syrinx aruana* (1), *Taheitia bifurca* (1), *Tambja pulcherrima* (1), *Taxella longicornis* (1), *Tenuitibia martinii* (1), *Terebra cumingii* (1), *Terrathelphusa secula* (1), *Tetralia brengelae* (1), *Thalamita kagosimensis* (1), *Thelphusula dicerophilus* (1), *Thelphusula tawauensis* (1), *Thorunna horologia* (1), *Thyca nardoafrianti* (1), *Tornatellides subperforatus* (1), *Trachystyla cryptica* (1), *Trapania armilla* (1), *Trapania nebula* (1), *Tricheulota bulbulus* (1), *Tricheulota zodiacus* (1), *Tridentata trigonostoma* (1), *Trinchesia* (1), *Tritonia* (1), *Tuerkayana celeste* (1), *Turbinella fusus* (1), *Turbo laminiferus* (1), *Turleania rubriguttatus* (1), *Tylomelania gemmifera* (1), *Tylomelania insulaesacrae* (1), *Tylomelania marwotoae* (1), *Tylomelania patriarchalis* (1), *Urnalana cristata* (1), *Vasticardium mindanense* (1), *Vellicolla amphorella* (1), *Verconia subnivalis* (1), *Vexillum honestum* (1), *Vexillum nivale* (1), *Vitrinula thisbe* (1), *Weinkauffia ukulele* (1), *Xenophora regularis* (1), *Xesta banggaiensis* (1), *Xesta obiana* (1), *Xesta semipartita* (1), *Xiphonectes longispinosus* (1), *Xiphonectes macrophthalmus* (1)

</details>

## Nicht aufgelöste Namen der Reihenfolge-Quelle

Die Referenz-DB der App kennt diese Namen nicht; die App fände sie auch nicht.

| Name | iNat |
|---|---|
| *Aplocheilus armatus* | 183 |
| *Pterygoplichthys* | 106 |
| *Priacanthus starnesi* | 67 |
| *Mystacoleucus obtusirostris* | 24 |
| *Barbodes sellifer* | 19 |
| *Ecsenius markalleni* | 14 |
| *Rasbora pycnopeza* | 13 |
| *Neotrygon vali* | 5 |
| *Acanthosepion aculeatum* | 4 |
| *Eviotops dorsopurpureus* | 4 |
| *Eviotops mikiae* | 4 |
| *Giuris tolsoni* | 4 |
| *Nomorhamphus versicolor* | 4 |
| *Awaous maculatus* | 3 |
| *Doratosepion andreanum* | 3 |
| *Eviotops lachdeberei* | 3 |
| *Eviotops nigrispinus* | 3 |
| *Helcogramma melanolancea* | 3 |
| *Micropterus nigricans* | 3 |
| *Ancistrus* | 2 |
| *Microphis martensii* | 2 |
| *Scomberoides pelagicus* | 2 |
| *Acanthosepion esculentum* | 1 |
| *Barbonymus strigatus* | 1 |
| *Coelorinchus* | 1 |
| *Cyclocheilos enoplos* | 1 |
| *Doboatherina yoshinoi* | 1 |
| *Enneapterygius rubrimarginatus* | 1 |
| *Eviotops pamae* | 1 |
| *Hypoatherina* | 1 |
| *Lobocheilos aurolineatus* | 1 |
| *Melanostomias* | 1 |
| *Microphis ocellatus* | 1 |
| *Oxuderces nexipinnis* | 1 |
| *Parachela johorensis* | 1 |
| *Pectenocypris rubra* | 1 |
| *Sebastiscus vibrantus* | 1 |
| *Strophidon tetraporus* | 1 |
| *Trichosomus trachinoides* | 1 |
| *Valenciennea schlieweni* | 1 |
| *Valenciennea zaboae* | 1 |
