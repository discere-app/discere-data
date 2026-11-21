# Bericht: Karibik & tropischer Westatlantik (`recipes/caribbean.json`)

Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.

- Referenz-DB: v3 (FishBase v26.06, SeaLifeBase v26.06)
- Salz/Süß: FishBase/SeaLifeBase v25.04 (species.parquet)
- iNaturalist: 1456 Taxa (Seiten: 3)
- OBIS: 2963 Arten mit Nachweisen außer iNaturalist
- Bild: https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Snorkeling_Bari_Reef%2C_Bonaire_%2812840799335%29.jpg/330px-Snorkeling_Bari_Reef%2C_Bonaire_%2812840799335%29.jpg — SNORKELINGDIVES.COM, CC BY 2.0, https://commons.wikimedia.org/wiki/File:Snorkeling_Bari_Reef,_Bonaire_(12840799335).jpg

## Gebiete

- iNaturalist: Monroe County, US, FL (1828), Miami-Dade County, US, FL (2345), Broward County, FL, US (1798), Palm Beach County, FL, US (1754), Quintana Roo, MX (7426), Belize (6953), Izabal, GT (10674), Cortés, HN (10725), Atlántida, HN (10720), Colón, HN (10722), Gracias a Dios, HN (13033), Islas de la Bahía, HN (10730), Atlántico Norte, NI (13143), Atlántico Sur, NI (13144), Limón, CR (12776), Bocas del Toro, PA (11521), Colón, PA (13153), Kuna Yala, PA (11525), San Andrés y Providencia, CO (12741), La Guajira, CO (13365), Magdalena, CO (8170), Atlántico, CO (12747), Bolívar, CO (12748), Sucre, CO (12743), Córdoba, CO (12732), Venezuela (1303), Bahamas (7313), Turks and Caicos Islands (7315), Cuba (6944), Cayman Islands (7488), Jamaica (8748), Haiti (7526), Dominican Republic (6931), Puerto Rico (6848), United States Virgin Islands (10319), British Virgin Islands (10318), Anguilla (10281), Saint-Martin (51360), Sint Maarten (10411), Saint-Barthélemy (51356), Antigua and Barbuda (10283), Saint Kitts and Nevis (10297), Montserrat (10304), Guadeloupe (8177), Dominica (9184), Martinique (10305), Saint Lucia (10300), Saint Vincent and the Grenadines (10317), Grenada (9992), Barbados (10285), Trinidad and Tobago (7375), Aruba (8359), Curaçao (10408), Bonaire, Sint Eustatius and Saba (8360), Bermuda (8638)
- OBIS: Florida-Straße, Bahamas, Große Antillen und Yucatán, Karibisches Meer südlich 17,5° N, ohne Pazifikküste, Bermuda
- FishBase/SeaLifeBase-Verbreitung: 028, 044, 052, 084, 092, 136, 192, 212, 214, 308, 312, 332, 388, 474, 500, 531, 533, 534, 535, 630, 652, 659, 660, 662, 663, 670, 780, 796, 850, 862, 840:US-FL, 060

## Übersicht

- Arten der Reihenfolge-Quelle, aufgelöst: 1428; nicht aufgelöst: 21
- ausgeschlossen: 827
  - kein Meeresfisch: 460
  - zu wenige Nachweise: 317
  - zu klein: 39
  - nur tiefer als die Tauchgrenze: 11
- Kandidaten nach den Filtern: 601
- Deck: 157 Arten (Level 1: 47, Level 2: 60, Level 3: 50); Umfang laut Rezept 40/60/50 plus Highlights
- Highlights: 7 im Deck, 0 verworfen

## Zu entscheiden

Hinweise, keine Ausschlüsse: Jede Zeile wird im Rezept entschieden (`exclude` mit Grund, Namenszuordnung, Level) oder bewusst belassen. Schwellen: `warnings` im Rezept.

| Art | Subdeck | Warnung | Zahlen |
|---|---|---|---|
| *Lutjanus griseus* | level-1 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Megalops atlanticus* | level-1 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Gerres cinereus* | level-1 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Caranx latus* | level-2 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Poecilia latipinna* | level-3 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Dajaus monticola* | level-3 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Centropomus undecimalis* | level-3 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Lutjanus jocu* | level-3 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Lagodon rhomboides* | level-3 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Strongylura notata* | level-3 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |

## Verworfene Highlights

Keine.

## iNaturalist-Namen zugeordnet

Laut `recipes/inat_names.json`: iNaturalist nennt die Art anders als die Referenz-DB; die Zählung kommt zu der der Referenz-DB-Art.

| iNaturalist | Referenz-DB | iNat | Art | Beleg |
|---|---|---|---|---|
| *Neoniphon vexillarius* | *Neoniphon vexillarium* | 635 | Umbenennung | https://www.inaturalist.org/taxon_changes/161493 |
| *Neoniphon coruscus* | *Neoniphon coruscum* | 99 | Umbenennung | https://www.inaturalist.org/taxon_changes/161494 |
| *Pinnoctopus macropus* | *Callistoctopus macropus* | 29 | Umbenennung | https://www.inaturalist.org/taxon_changes/172613 |
| *Rhonciscus approximans* | *Rhonciscus pauco* | 7 | Umbenennung | https://www.inaturalist.org/taxon_changes/152389 |
| *Sphoeroides psittacus* | *Colomesus psittacus* | 6 | Umbenennung | https://www.inaturalist.org/taxon_changes/134193 |

## Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Rhincodon typus* | Der Walhai, größter Fisch der Welt, zieht im Frühsommer vor Isla Mujeres und Utila vorbei. | 256 | Reihenfolge-Quelle, OBIS, Verbreitung, Führer | Level 1 |
| *Mobula birostris* | Der Riesenmanta ist selten, aber eine der Begegnungen, auf die Taucher hoffen. | – | OBIS, Verbreitung, Führer | Level 1 |
| *Sphyrna mokarran* | Der Große Hammerhai ist der Großhai, den Taucher auf den Bahamas (Bimini) gezielt suchen. | 247 | Reihenfolge-Quelle, OBIS, Verbreitung, Führer | Level 1 |
| *Hippocampus reidi* | Das Langschnauzen-Seepferdchen ist die Seepferdchen-Art, die man in der Karibik am ehesten findet. | 62 | Reihenfolge-Quelle, OBIS, Verbreitung, Führer | Level 1 |
| *Antennarius multiocellatus* | Der Langstachel-Anglerfisch ist ein Meister der Tarnung und ein Ziel jedes Makrotauchgangs. | 185 | Reihenfolge-Quelle, OBIS, Verbreitung, Führer | Level 1 |
| *Eques punctatus* (Rezept: *Equetus punctatus*) | Der Gefleckte Umberfisch mit seinen langen Flossen gehört zu den Ikonen des karibischen Riffs. | 74 | Reihenfolge-Quelle, OBIS, Verbreitung, Führer | Level 1 |
| *Opistognathus aurifrons* | Der Gelbkopf-Kieferfisch brütet die Eier im Maul aus und ist an jedem Sandgrund zu beobachten. | 131 | Reihenfolge-Quelle, OBIS, Verbreitung, Führer | Level 1 |

## Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS ohne iNaturalist oder Verbreitung): 156/157 (99 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 0
- Arten ohne Volksnamen `de` in der Referenz-DB: 97/157 (62 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 0/157 (0 %)
- Familien ohne Volksnamen `de`: 9/64 (14 %): *Aetobatidae*, *Cheloniidae*, *Dermochelyidae*, *Epinephelidae*, *Grammistidae*, *Loliginidae*, *Mobulidae*, *Octopodidae*, *Urotrygonidae*
- Familien ohne Volksnamen `en`: 0/64 (0 %)

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

- *Mobula birostris*: OBIS, Verbreitung, Führer

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

- gleicher Volksname `de` „Frauenfisch“: *Megalops atlanticus*, *Albula vulpes*
- gleicher Volksname `de` „Schnapper“: *Lutjanus apodus*, *Lutjanus analis*, *Lutjanus mahogoni*, *Lutjanus synagris*, *Lutjanus jocu*

## Deck

Spalten: Rang unter den Kandidaten, Zählung der Reihenfolge-Quelle (iNat), OBIS-Nachweise ohne den iNaturalist-Datensatz, Einträge der FishBase/SeaLifeBase-Verbreitung in den Rezept-Regionen (~~durchgestrichen~~: Eintrag sagt „nicht vorhanden“), Wasser laut FishBase/SeaLifeBase, Nummer des Führers, der die Art listet.

### Level 1 (47)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer |
|---|---|---|---|---|---|---|
| 1 | *Abudefduf saxatilis* (4046 Beobachter) | 9598 | 20797 | native ×28 | Meer | 1 |
| 2 | *Acanthurus coeruleus* (2505 Beobachter) | 7879 | 71817 | native ×28 | Meer | 1 |
| 3 | *Thalassoma bifasciatum* (1952 Beobachter) | 6796 | 116888 | native ×28 | Meer | 1 |
| 4 | *Chelonia mydas* (3339 Beobachter) | 6768 | 22917 | native ×23 | Meer | – |
| 5 | *Sparisoma viride* (1998 Beobachter) | 6280 | 60235 | native ×28 | Meer | 1 |
| 6 | *Sphyraena barracuda* (3073 Beobachter) | 5884 | 7032 | native ×28 | Brack/Meer | 1 |
| 7 | *Haemulon flavolineatum* (1868 Beobachter) | 5568 | 37782 | native ×28 | Meer | 1 |
| 8 | *Lutjanus apodus* (2183 Beobachter) | 5425 | 16512 | native ×28 | Brack/Meer | 1 |
| 9 | *Halichoeres bivittatus* (1426 Beobachter) | 4332 | 71766 | native ×27 | Meer | 1 |
| 10 | *Pomacanthus paru* (1789 Beobachter) | 4317 | 6884 | native ×28, ~~not established ×1~~ | Meer | 1 |
| 11 | *Haemulon sciurus* (1803 Beobachter) | 4248 | 28071 | native ×28 | Meer | 1 |
| 12 | *Acanthurus tractus* (1391 Beobachter) | 4059 | 3789 | native ×28, stray ×1 | Meer | 1 |
| 13 | *Lutjanus griseus* (1747 Beobachter) | 4013 | 24687 | native ×28 | Süß/Brack/Meer | 1 |
| 14 | *Ginglymostoma cirratum* (2347 Beobachter) | 3854 | 1051 | native ×26 | Brack/Meer | 1 |
| 15 | *Hypanus americanus* (2084 Beobachter) | 3728 | 4293 | native ×21 | Brack/Meer | 1 |
| 16 | *Aulostomus maculatus* (1339 Beobachter) | 3550 | 5235 | native ×27 | Meer | 1 |
| 17 | *Scarus iseri* (1144 Beobachter) | 3505 | 107826 | native ×28 | Meer | 1 |
| 18 | *Pterois volitans* (1504 Beobachter) | 3434 | 2620 | introduced ×15 | Meer | 1 |
| 19 | *Chaetodon capistratus* (1364 Beobachter) | 3406 | 25488 | native ×16 | Meer | 1 |
| 20 | *Lactophrys triqueter* (1481 Beobachter) | 3379 | 3176 | native ×27 | Meer | 1 |
| 21 | *Caranx ruber* (1357 Beobachter) | 3313 | 26262 | native ×28 | Meer | 1 |
| 22 | *Megalops atlanticus* (2214 Beobachter) | 3251 | 56727 | native ×28 | Süß/Brack/Meer | 1 |
| 23 | *Ocyurus chrysurus* (1485 Beobachter) | 3150 | 71830 | native ×28 | Meer | 1 |
| 24 | *Microspathodon chrysurus* (1167 Beobachter) | 3040 | 14059 | native ×28 | Meer | 1 |
| 25 | *Sparisoma aurofrenatum* (907 Beobachter) | 2783 | 102645 | native ×28 | Meer | 1 |
| 26 | *Gerres cinereus* (1310 Beobachter) | 2671 | 1737 | native ×28 | Süß/Brack/Meer | 1 |
| 27 | *Diodon hystrix* (1255 Beobachter) | 2396 | 724 | native ×27 | Meer | 1 |
| 28 | *Urobatis jamaicensis* (1300 Beobachter) | 2395 | 1252 | native ×26 | Meer | 1 |
| 29 | *Holacanthus ciliaris* (Quelle: *Holacanthus ciliaris × bermudensis*; 993 Beobachter) | 2383 | 10113 | native ×28 | Meer | 1 |
| 30 | *Scarus vetula* (816 Beobachter) | 2304 | 7400 | native ×28 | Meer | 1 |
| 31 | *Halichoeres garnoti* (673 Beobachter) | 2249 | 72443 | native ×28 | Meer | 1 |
| 32 | *Chaetodon striatus* (966 Beobachter) | 2229 | 6055 | native ×28 | Meer | 1 |
| 33 | *Pomacanthus arcuatus* (1087 Beobachter) | 2205 | 19425 | introduced ×1, native ×25 | Meer | 1 |
| 34 | *Sparisoma rubripinne* (960 Beobachter) | 2188 | 12674 | native ×22 | Meer | 1 |
| 35 | *Anisotremus virginicus* (1062 Beobachter) | 2147 | 18218 | introduced ×1, native ×27 | Meer | 1 |
| 36 | *Gymnothorax moringa* (918 Beobachter) | 2145 | 1723 | native ×23 | Meer | 1 |
| 37 | *Canthigaster rostrata* (855 Beobachter) | 2114 | 20731 | native ×28 | Meer | 1 |
| 38 | *Aetobatus narinari* (1382 Beobachter) | 2111 | 7847 | native ×28 | Brack/Meer | 1 |
| 39 | *Haemulon plumierii* (864 Beobachter) | 2085 | 64915 | introduced ×1, native ×26 | Meer | 1 |
| 40 | *Holocentrus rufus* (922 Beobachter) | 2053 | 7794 | native ×26 | Meer | 1 |
| 256 | *Rhincodon typus* (Highlight; 78 Beobachter) | 104 | 748 | native ×28 | Meer | 1 |
| – | *Mobula birostris* (Highlight) | – | 76 | native ×10 | Meer | 1 |
| 247 | *Sphyrna mokarran* (Highlight; 78 Beobachter) | 112 | 2156 | native ×26 | Brack/Meer | 1 |
| 62 | *Hippocampus reidi* (Highlight; 424 Beobachter) | 1403 | 102 | native ×18 | Brack/Meer | 1 |
| 185 | *Antennarius multiocellatus* (Highlight; 100 Beobachter) | 249 | 145 | native ×27 | Meer | 1 |
| 74 | *Eques punctatus* (Highlight; 529 Beobachter) | 1231 | 777 | native ×27 | Meer | 1 |
| 131 | *Opistognathus aurifrons* (Highlight; 251 Beobachter) | 544 | 9773 | native ×27 | Meer | 1 |

### Level 2 (60)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer |
|---|---|---|---|---|---|---|
| 41 | *Cephalopholis cruentata* (744 Beobachter) | 2035 | 21465 | native ×28 | Meer | 1 |
| 42 | *Sepioteuthis sepioidea* (1087 Beobachter) | 2022 | 91 | native ×22 | Meer | – |
| 43 | *Scorpaena plumieri* (868 Beobachter) | 2014 | 848 | native ×22 | Meer | 1 |
| 44 | *Eretmochelys imbricata* (994 Beobachter) | 1956 | 4119 | native ×22 | Brack/Meer | – |
| 45 | *Synodus intermedius* (934 Beobachter) | 1944 | 1601 | native ×25 | Meer | 1 |
| 46 | *Sphoeroides testudineus* (1383 Beobachter) | 1929 | 733 | native ×27 | Brack/Meer | 1 |
| 47 | *Mulloidichthys martinicus* (692 Beobachter) | 1833 | 6727 | native ×28 | Meer | 1 |
| 48 | *Bodianus rufus* (780 Beobachter) | 1802 | 13752 | native ×28 | Meer | 1 |
| 49 | *Azurina cyanea* (729 Beobachter) | 1782 | 23191 | native ×28 | Meer | 1 |
| 50 | *Halichoeres radiatus* (738 Beobachter) | 1759 | 9553 | native ×28 | Brack/Meer | 1 |
| 51 | *Scarus guacamaia* (963 Beobachter) | 1661 | 3820 | native ×28 | Meer | 1 |
| 52 | *Stegastes planifrons* (579 Beobachter) | 1635 | 20052 | native ×28 | Meer | 1 |
| 53 | *Acanthurus chirurgus* (803 Beobachter) | 1626 | 30515 | native ×28 | Meer | 1 |
| 54 | *Bothus lunatus* (856 Beobachter) | 1545 | 446 | native ×28 | Meer | 1 |
| 55 | *Stegastes partitus* (542 Beobachter) | 1540 | 85186 | native ×28 | Meer | 1 |
| 56 | *Aluterus scriptus* (880 Beobachter) | 1519 | 1743 | native ×25 | Meer | 1 |
| 57 | *Stegastes leucostictus* (715 Beobachter) | 1480 | 13555 | native ×28 | Meer | 1 |
| 58 | *Gymnothorax funebris* (806 Beobachter) | 1478 | 583 | native ×22 | Meer | 1 |
| 59 | *Azurina multilineata* (457 Beobachter) | 1447 | 14305 | native ×28 | Meer | 1 |
| 60 | *Scarus taeniopterus* (497 Beobachter) | 1425 | 21944 | native ×28 | Meer | 1 |
| 61 | *Chaetodon ocellatus* (686 Beobachter) | 1410 | 14639 | native ×29 | Meer | 1 |
| 63 | *Brachygenys chrysargyrea* (557 Beobachter) | 1362 | 4897 | native ×28 | Meer | 1 |
| 64 | *Lutjanus analis* (744 Beobachter) | 1336 | 20652 | introduced ×1, native ×27 | Brack/Meer | 1 |
| 65 | *Haemulon aurolineatum* (479 Beobachter) | 1318 | 19783 | native ×28 | Meer | 1 |
| 66 | *Cephalopholis fulva* (436 Beobachter) | 1315 | 7104 | native ×28 | Meer | 1 |
| 67 | *Caranx latus* (677 Beobachter) | 1308 | 1039 | native ×29 | Süß/Brack/Meer | 1 |
| 68 | *Diodon holocanthus* (699 Beobachter) | 1294 | 911 | native ×12 | Meer | 1 |
| 69 | *Tylosurus crocodilus* (842 Beobachter) | 1277 | 450 | native ×27 | Meer | 1 |
| 70 | *Lutjanus mahogoni* (536 Beobachter) | 1267 | 4972 | native ×26 | Meer | 1 |
| 71 | *Haemulon parra* (550 Beobachter) | 1243 | 3014 | native ×27 | Meer | 1 |
| 72 | *Holacanthus tricolor* (549 Beobachter) | 1242 | 12747 | native ×29 | Meer | 1 |
| 73 | *Acanthostracion polygonium* (620 Beobachter) | 1232 | 616 | native ×26 | Meer | 1 |
| 75 | *Acanthostracion quadricornis* (748 Beobachter) | 1211 | 1349 | native ×22 | Meer | 1 |
| 76 | *Myripristis jacobus* (454 Beobachter) | 1196 | 2905 | native ×30 | Meer | 1 |
| 77 | *Cantherhines macrocerus* (563 Beobachter) | 1184 | 539 | native ×27 | Meer | 1 |
| 78 | *Epinephelus striatus* (501 Beobachter) | 1156 | 1011 | native ×28 | Meer | 1 |
| 79 | *Serranus tigrinus* (492 Beobachter) | 1148 | 12628 | native ×28 | Meer | 1 |
| 80 | *Lutjanus synagris* (570 Beobachter) | 1131 | 6101 | native ×27 | Meer | 1 |
| 81 | *Stegastes diencaeus* (432 Beobachter) | 1131 | 3745 | native ×27 | Meer | 1 |
| 82 | *Lactophrys bicaudalis* (615 Beobachter) | 1095 | 668 | native ×28 | Meer | 1 |
| 83 | *Sparisoma chrysopterum* (509 Beobachter) | 1082 | 11822 | native ×27 | Meer | 1 |
| 84 | *Bodianus parrae* (436 Beobachter) | 1079 | 13005 | native ×28 | Meer | 1 |
| 85 | *Lachnolaimus maximus* (577 Beobachter) | 1077 | 23624 | native ×27 | Meer | 1 |
| 86 | *Cantherhines pullus* (531 Beobachter) | 1072 | 1667 | native ×27 | Meer | 1 |
| 87 | *Pseudupeneus maculatus* (506 Beobachter) | 1071 | 18000 | native ×27 | Meer | 1 |
| 88 | *Holocentrus adscensionis* (573 Beobachter) | 1052 | 7395 | native ×26 | Meer | 1 |
| 89 | *Octopus insularis* (542 Beobachter) | 1037 | 87 | native ×5 | Meer | – |
| 90 | *Melichthys niger* (528 Beobachter) | 1014 | 3039 | native ×27 | Meer | 1 |
| 91 | *Ophioblennius macclurei* (360 Beobachter) | 1014 | 1117 | native ×7, questionable ×1 | Meer | 1 |
| 92 | *Stegastes adustus* (484 Beobachter) | 1002 | 12212 | native ×27, stray ×1 | Meer | 1 |
| 93 | *Caranx crysos* (548 Beobachter) | 1001 | 2951 | native ×28 | Brack/Meer | 1 |
| 94 | *Gymnothorax miliaris* (452 Beobachter) | 975 | 473 | native ×28 | Meer | 1 |
| 95 | *Styracura schmardae* (768 Beobachter) | 966 | 92 | native ×17 | Meer | 1 |
| 96 | *Echidna catenata* (659 Beobachter) | 950 | 351 | native ×28 | Meer | 1 |
| 97 | *Carcharhinus perezii* (422 Beobachter) | 936 | 415 | native ×27 | Meer | 1 |
| 98 | *Gramma loreto* (336 Beobachter) | 935 | 3127 | native ×27 | Meer | 1 |
| 99 | *Myrichthys breviceps* (550 Beobachter) | 915 | 287 | native ×13 | Meer | 1 |
| 100 | *Caranx bartholomaei* (493 Beobachter) | 910 | 4204 | native ×28 | Meer | 1 |
| 101 | *Sphoeroides spengleri* (482 Beobachter) | 907 | 1592 | native ×23 | Brack/Meer | 1 |
| 102 | *Haemulon carbonarium* (420 Beobachter) | 892 | 4429 | native ×28 | Meer | 1 |

### Level 3 (50)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer |
|---|---|---|---|---|---|---|
| 103 | *Hypoplectrus puella* | 886 | 5807 | native ×28 | Meer | 1 |
| 104 | *Kyphosus sectatrix* | 862 | 9672 | native ×28 | Meer | 1 |
| 105 | *Pareques acuminatus* | 821 | 2418 | native ×16, ~~error ×1~~ | Meer | 1 |
| 106 | *Trachinotus falcatus* | 804 | 465 | native ×27 | Brack/Meer | 1 |
| 107 | *Malacoctenus triangulatus* | 777 | 7793 | native ×27 | Meer | 1 |
| 108 | *Dermochelys coriacea* | 765 | 462 | native ×21 | Meer | – |
| 109 | *Caretta caretta* | 757 | 7810 | native ×21 | Meer | – |
| 110 | *Kyphosus vaigiensis* | 727 | 45 | – | Meer | 1 |
| 111 | *Trachinotus goodei* | 718 | 341 | native ×28 | Meer | 1 |
| 112 | *Balistes vetula* | 702 | 2364 | native ×27 | Meer | 1 |
| 113 | *Stegastes xanthurus* | 686 | 8 | native ×26 | Meer | 1 |
| 114 | *Canthidermis sufflamen* | 684 | 1353 | native ×26 | Meer | 1 |
| 115 | *Heteropriacanthus cruentatus* | 683 | 987 | native ×30 | Meer | 1 |
| 116 | *Poecilia latipinna* | 658 | 882 | introduced ×1, native ×1 | Süß/Brack/Meer | 1 |
| 117 | *Epinephelus guttatus* | 655 | 3603 | native ×27 | Meer | 1 |
| 118 | *Dajaus monticola* | 640 | 444 | native ×19 | Süß/Brack/Meer | 1 |
| 119 | *Neoniphon vexillarium* | 635 | 1080 | native ×26 | Meer | 1 |
| 120 | *Octopus briareus* | 628 | 101 | native ×19 | Meer | – |
| 121 | *Halichoeres maculipinna* | 624 | 43411 | native ×27 | Meer | 1 |
| 122 | *Caranx hippos* | 620 | 39512 | native ×18 | Brack/Meer | 1 |
| 123 | *Chaetodipterus faber* | 616 | 1311 | introduced ×1, native ×19 | Brack/Meer | 1 |
| 124 | *Abudefduf taurus* | 604 | 115 | native ×27 | Meer | 1 |
| 125 | *Negaprion brevirostris* | 604 | 653 | native ×27 | Brack/Meer | 1 |
| 126 | *Centropomus undecimalis* | 603 | 27027 | native ×27 | Süß/Brack/Meer | 1 |
| 127 | *Lutjanus jocu* | 602 | 1330 | introduced ×1, native ×26 | Süß/Brack/Meer | 1 |
| 128 | *Lactophrys trigonus* | 582 | 541 | native ×25, questionable ×1 | Meer | 1 |
| 129 | *Parablennius marmoreus* | 571 | 3099 | native ×27 | Meer | 1 |
| 130 | *Anisotremus surinamensis* | 569 | 1274 | native ×27 | Meer | 1 |
| 132 | *Hypoplectrus unicolor* | 530 | 15870 | native ×27 | Meer | 1 |
| 133 | *Rypticus saponaceus* | 528 | 674 | native ×28 | Meer | 1 |
| 134 | *Gnatholepis thompsoni* | 524 | 5375 | native ×28 | Meer | 1 |
| 135 | *Hemiramphus brasiliensis* | 509 | 620 | native ×21 | Meer | 1 |
| 136 | *Malacanthus plumieri* | 503 | 1878 | native ×19 | Meer | 1 |
| 137 | *Echeneis naucrates* | 489 | 616 | native ×27 | Brack/Meer | 1 |
| 138 | *Elacatinus evelynae* | 478 | 2119 | native ×25, questionable ×1 | Meer | 1 |
| 139 | *Holacanthus bermudensis* | 451 | 10703 | native ×6 | Meer | 1 |
| 140 | *Hypoplectrus indigo* | 440 | 344 | native ×10, questionable ×3 | Meer | 1 |
| 141 | *Pempheris schomburgkii* | 433 | 546 | native ×28 | Meer | 1 |
| 142 | *Balistes capriscus* | 432 | 1463 | native ×19 | Meer | 1 |
| 143 | *Malacoctenus macropus* | 419 | 2016 | native ×28 | Meer | 1 |
| 144 | *Scarus coeruleus* | 412 | 5002 | native ×27 | Meer | 1 |
| 145 | *Apogon maculatus* | 410 | 1321 | native ×27 | Meer | 1 |
| 146 | *Lagodon rhomboides* | 405 | 1589 | native ×4 | Süß/Brack/Meer | 1 |
| 147 | *Dactylopterus volitans* | 400 | 259 | native ×21 | Brack/Meer | 1 |
| 148 | *Monacanthus tuckeri* | 393 | 1150 | native ×26 | Meer | 1 |
| 149 | *Labrisomus nuchipinnis* | 390 | 750 | native ×28 | Meer | 1 |
| 150 | *Strongylura notata* | 390 | 869 | native ×7, questionable ×1 | Süß/Brack/Meer | 1 |
| 151 | *Albula vulpes* | 375 | 1216 | native ×29 | Brack/Meer | 1 |
| 152 | *Mycteroperca tigris* | 372 | 481 | native ×28 | Meer | 1 |
| 153 | *Acanthemblemaria aspera* | 356 | 452 | native ×26 | Meer | 1 |

## Grenzfälle

Je 10 Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels sie nehmen (Highlights ab Level 2 übersprungen).

### Level 1/2

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer | Level |
|---|---|---|---|---|---|---|---|
| 31 | *Halichoeres garnoti* (673 Beobachter) | 2249 | 72443 | native ×28 | Meer | 1 | 1 |
| 32 | *Chaetodon striatus* (966 Beobachter) | 2229 | 6055 | native ×28 | Meer | 1 | 1 |
| 33 | *Pomacanthus arcuatus* (1087 Beobachter) | 2205 | 19425 | introduced ×1, native ×25 | Meer | 1 | 1 |
| 34 | *Sparisoma rubripinne* (960 Beobachter) | 2188 | 12674 | native ×22 | Meer | 1 | 1 |
| 35 | *Anisotremus virginicus* (1062 Beobachter) | 2147 | 18218 | introduced ×1, native ×27 | Meer | 1 | 1 |
| 36 | *Gymnothorax moringa* (918 Beobachter) | 2145 | 1723 | native ×23 | Meer | 1 | 1 |
| 37 | *Canthigaster rostrata* (855 Beobachter) | 2114 | 20731 | native ×28 | Meer | 1 | 1 |
| 38 | *Aetobatus narinari* (1382 Beobachter) | 2111 | 7847 | native ×28 | Brack/Meer | 1 | 1 |
| 39 | *Haemulon plumierii* (864 Beobachter) | 2085 | 64915 | introduced ×1, native ×26 | Meer | 1 | 1 |
| 40 | *Holocentrus rufus* (922 Beobachter) | 2053 | 7794 | native ×26 | Meer | 1 | 1 |
| | **Grenze** | | | | | | |
| 41 | *Cephalopholis cruentata* (744 Beobachter) | 2035 | 21465 | native ×28 | Meer | 1 | 2 |
| 42 | *Sepioteuthis sepioidea* (1087 Beobachter) | 2022 | 91 | native ×22 | Meer | – | 2 |
| 43 | *Scorpaena plumieri* (868 Beobachter) | 2014 | 848 | native ×22 | Meer | 1 | 2 |
| 44 | *Eretmochelys imbricata* (994 Beobachter) | 1956 | 4119 | native ×22 | Brack/Meer | – | 2 |
| 45 | *Synodus intermedius* (934 Beobachter) | 1944 | 1601 | native ×25 | Meer | 1 | 2 |
| 46 | *Sphoeroides testudineus* (1383 Beobachter) | 1929 | 733 | native ×27 | Brack/Meer | 1 | 2 |
| 47 | *Mulloidichthys martinicus* (692 Beobachter) | 1833 | 6727 | native ×28 | Meer | 1 | 2 |
| 48 | *Bodianus rufus* (780 Beobachter) | 1802 | 13752 | native ×28 | Meer | 1 | 2 |
| 49 | *Azurina cyanea* (729 Beobachter) | 1782 | 23191 | native ×28 | Meer | 1 | 2 |
| 50 | *Halichoeres radiatus* (738 Beobachter) | 1759 | 9553 | native ×28 | Brack/Meer | 1 | 2 |

### Level 2/3

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer | Level |
|---|---|---|---|---|---|---|---|
| 93 | *Caranx crysos* (548 Beobachter) | 1001 | 2951 | native ×28 | Brack/Meer | 1 | 2 |
| 94 | *Gymnothorax miliaris* (452 Beobachter) | 975 | 473 | native ×28 | Meer | 1 | 2 |
| 95 | *Styracura schmardae* (768 Beobachter) | 966 | 92 | native ×17 | Meer | 1 | 2 |
| 96 | *Echidna catenata* (659 Beobachter) | 950 | 351 | native ×28 | Meer | 1 | 2 |
| 97 | *Carcharhinus perezii* (422 Beobachter) | 936 | 415 | native ×27 | Meer | 1 | 2 |
| 98 | *Gramma loreto* (336 Beobachter) | 935 | 3127 | native ×27 | Meer | 1 | 2 |
| 99 | *Myrichthys breviceps* (550 Beobachter) | 915 | 287 | native ×13 | Meer | 1 | 2 |
| 100 | *Caranx bartholomaei* (493 Beobachter) | 910 | 4204 | native ×28 | Meer | 1 | 2 |
| 101 | *Sphoeroides spengleri* (482 Beobachter) | 907 | 1592 | native ×23 | Brack/Meer | 1 | 2 |
| 102 | *Haemulon carbonarium* (420 Beobachter) | 892 | 4429 | native ×28 | Meer | 1 | 2 |
| | **Grenze** | | | | | | |
| 103 | *Hypoplectrus puella* | 886 | 5807 | native ×28 | Meer | 1 | 3 |
| 104 | *Kyphosus sectatrix* | 862 | 9672 | native ×28 | Meer | 1 | 3 |
| 105 | *Pareques acuminatus* | 821 | 2418 | native ×16, ~~error ×1~~ | Meer | 1 | 3 |
| 106 | *Trachinotus falcatus* | 804 | 465 | native ×27 | Brack/Meer | 1 | 3 |
| 107 | *Malacoctenus triangulatus* | 777 | 7793 | native ×27 | Meer | 1 | 3 |
| 108 | *Dermochelys coriacea* | 765 | 462 | native ×21 | Meer | – | 3 |
| 109 | *Caretta caretta* | 757 | 7810 | native ×21 | Meer | – | 3 |
| 110 | *Kyphosus vaigiensis* | 727 | 45 | – | Meer | 1 | 3 |
| 111 | *Trachinotus goodei* | 718 | 341 | native ×28 | Meer | 1 | 3 |
| 112 | *Balistes vetula* | 702 | 2364 | native ×27 | Meer | 1 | 3 |

### Level 3/nicht im Deck

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer | Level |
|---|---|---|---|---|---|---|---|
| 144 | *Scarus coeruleus* | 412 | 5002 | native ×27 | Meer | 1 | 3 |
| 145 | *Apogon maculatus* | 410 | 1321 | native ×27 | Meer | 1 | 3 |
| 146 | *Lagodon rhomboides* | 405 | 1589 | native ×4 | Süß/Brack/Meer | 1 | 3 |
| 147 | *Dactylopterus volitans* | 400 | 259 | native ×21 | Brack/Meer | 1 | 3 |
| 148 | *Monacanthus tuckeri* | 393 | 1150 | native ×26 | Meer | 1 | 3 |
| 149 | *Labrisomus nuchipinnis* | 390 | 750 | native ×28 | Meer | 1 | 3 |
| 150 | *Strongylura notata* | 390 | 869 | native ×7, questionable ×1 | Süß/Brack/Meer | 1 | 3 |
| 151 | *Albula vulpes* | 375 | 1216 | native ×29 | Brack/Meer | 1 | 3 |
| 152 | *Mycteroperca tigris* | 372 | 481 | native ×28 | Meer | 1 | 3 |
| 153 | *Acanthemblemaria aspera* | 356 | 452 | native ×26 | Meer | 1 | 3 |
| | **Grenze** | | | | | | |
| 154 | *Lophogobius cyprinoides* | 356 | 296 | native ×15 | Süß/Brack/Meer | 1 | – |
| 155 | *Emblemaria pandionis* | 352 | 138 | native ×27 | Meer | 1 | – |
| 156 | *Scarus coelestinus* | 350 | 3187 | native ×27, questionable ×1 | Meer | 1 | – |
| 157 | *Scomberomorus regalis* | 346 | 3989 | native ×27 | Meer | 1 | – |
| 158 | *Xyrichtys splendens* | 343 | 4796 | native ×9 | Meer | 1 | – |
| 159 | *Halichoeres poeyi* | 341 | 5930 | native ×27 | Meer | 1 | – |
| 160 | *Serranus tabacarius* | 338 | 3463 | native ×28 | Meer | 1 | – |
| 161 | *Archosargus probatocephalus* | 331 | 346 | native ×6 | Brack/Meer | 1 | – |
| 162 | *Strongylura marina* | 330 | 976 | native ×7 | Süß/Brack/Meer | 1 | – |
| 163 | *Labrisomus conditus* | 328 | – | – | Meer | 1 | – |

## Abgleich mit Führern

### 1. Smithsonian: Shorefishes of the Greater Caribbean

- 1896 Namen, 1878 Arten aufgelöst, 15 Namen nicht aufgelöst
- Deck-Arten im Führer: 150/157
  - Level 1: 46/47
  - Level 2: 57/60
  - Level 3: 47/50
- Kandidaten im Führer, aber nicht im Deck: 427

**Im Deck, nicht im Führer** (Verdacht: Fehlbestimmung, falsch verortet oder Süßwasser):

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer | Level |
|---|---|---|---|---|---|---|---|
| 4 | *Chelonia mydas* (3339 Beobachter) | 6768 | 22917 | native ×23 | Meer | – | 1 |
| 42 | *Sepioteuthis sepioidea* (1087 Beobachter) | 2022 | 91 | native ×22 | Meer | – | 2 |
| 44 | *Eretmochelys imbricata* (994 Beobachter) | 1956 | 4119 | native ×22 | Brack/Meer | – | 2 |
| 89 | *Octopus insularis* (542 Beobachter) | 1037 | 87 | native ×5 | Meer | – | 2 |
| 108 | *Dermochelys coriacea* | 765 | 462 | native ×21 | Meer | – | 3 |
| 109 | *Caretta caretta* | 757 | 7810 | native ×21 | Meer | – | 3 |
| 120 | *Octopus briareus* | 628 | 101 | native ×19 | Meer | – | 3 |

**Im Führer und häufig, aber nicht im Deck** (Kandidaten; die 30 häufigsten):

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer |
|---|---|---|---|---|---|---|
| 154 | *Lophogobius cyprinoides* | 356 | 296 | native ×15 | Süß/Brack/Meer | 1 |
| 155 | *Emblemaria pandionis* | 352 | 138 | native ×27 | Meer | 1 |
| 156 | *Scarus coelestinus* | 350 | 3187 | native ×27, questionable ×1 | Meer | 1 |
| 157 | *Scomberomorus regalis* | 346 | 3989 | native ×27 | Meer | 1 |
| 158 | *Xyrichtys splendens* | 343 | 4796 | native ×9 | Meer | 1 |
| 159 | *Halichoeres poeyi* | 341 | 5930 | native ×27 | Meer | 1 |
| 160 | *Serranus tabacarius* | 338 | 3463 | native ×28 | Meer | 1 |
| 161 | *Archosargus probatocephalus* | 331 | 346 | native ×6 | Brack/Meer | 1 |
| 162 | *Strongylura marina* | 330 | 976 | native ×7 | Süß/Brack/Meer | 1 |
| 163 | *Labrisomus conditus* | 328 | – | – | Meer | 1 |
| 164 | *Harengula humeralis* | 319 | 990 | native ×28 | Meer | 1 |
| 165 | *Epinephelus itajara* | 317 | 325049 | native ×27, questionable ×1 | Brack/Meer | 1 |
| 166 | *Flammeo marianus* | 316 | 1061 | native ×24 | Meer | 1 |
| 167 | *Carcharhinus leucas* | 314 | 2473 | native ×27 | Süß/Brack/Meer | 1 |
| 168 | *Heteroconger longissimus* | 312 | 200 | native ×25 | Meer | 1 |
| 169 | *Atherinomorus stipes* | 306 | 717 | native ×12 | Süß/Brack/Meer | 1 |
| 170 | *Scartella cristata* | 296 | 463 | native ×28 | Meer | 1 |
| 171 | *Narcine bancroftii* | 294 | 27 | native ×3 | Meer | 1 |
| 172 | *Amblycirrhitus pinos* | 287 | 925 | native ×27 | Meer | 1 |
| 173 | *Coryphopterus glaucofraenum* | 281 | 29910 | native ×27 | Meer | 1 |
| 174 | *Hippocampus erectus* | 280 | 495 | native ×28 | Meer | 1 |
| 175 | *Stephanolepis hispida* | 280 | 808 | native ×27 | Meer | 1 |
| 176 | *Lutjanus cyanopterus* | 271 | 377 | native ×26 | Brack/Meer | 1 |
| 177 | *Bothus ocellatus* | 270 | 661 | native ×27 | Meer | 1 |
| 178 | *Haemulon album* | 270 | 1073 | native ×28 | Meer | 1 |
| 179 | *Xyrichtys martinicensis* | 267 | 1406 | native ×10 | Meer | 1 |
| 180 | *Myrichthys ocellatus* | 264 | 183 | native ×26 | Meer | 1 |
| 181 | *Bothus maculiferus* | 262 | 72 | native ×8 | Meer | 1 |
| 182 | *Haemulon macrostoma* | 260 | 2493 | native ×27, ~~misidentification ×1~~ | Meer | 1 |
| 183 | *Hypoplectrus chlorurus* | 256 | 1333 | native ×13 | Meer | 1 |

<details><summary>Nicht aufgelöste Namen des Führers</summary>

*Polymixia hollisterae*, *Pteraclis carolinum*, *Syngnathus texanus*, *Psilotris vantasselli*, *Varicus benthonis*, *Varicus vespa*, *Hiatirhaphis cascajalensis*, *Acyrtus nudus*, *Omobranchus sewalli*, *Anthias hensleyi*, *Bathyanthias atlanticus*, *Hyporthodus drummondhayi*, *Serranus fuscula*, *Orthopristis scapularis*, *Menticirrhus cuiaranensis*

</details>

## Änderungen gegenüber dem bestehenden Deck

- neu: 0
- entfallen: 0

## Ausgeschlossene Kandidaten

<details><summary>827 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Mayaheros urophthalmus* | 2962 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lepisosteus platyrhincus* | 2182 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Micropterus salmoides* | 1255 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cichla ocellaris* | 1251 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acanthemblemaria spinosa* | 989 | Meer | zu klein (höchstens 3.1 cm) |
| *Pelmatolapia mariae* | 944 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gambusia holbrooki* | 845 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lepomis macrochirus* | 798 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mycteroperca bonaci* | 691 | Meer | nur tiefer als die Tauchgrenze (erst ab 60 m) |
| *Astronotus ocellatus* | 472 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parachromis managuensis* | 397 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oreochromis aureus* | 383 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Clarias batrachus* | 295 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Spirula spirula* | 283 | Meer | nur tiefer als die Tauchgrenze (erst ab 100 m) |
| *Channa aurolineata* | 280 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Vieja melanurus* | 277 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Coryphopterus lipernes* | 248 | Meer | zu klein (höchstens 3 cm) |
| *Lepomis punctatus* | 236 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Belonesox belizanus* | 231 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia reticulata* | 216 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gymnothorax vicinus* | 213 | Meer | nur tiefer als die Tauchgrenze (erst ab 50 m) |
| *Oreochromis mossambicus* | 213 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amphilophus citrinellus* | 203 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Elacatinus lobeli* | 195 | Meer | zu klein (höchstens 3.1 cm) |
| *Gambusia rhizophorae* | 180 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trichromis salvini* | 172 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Synbranchus marmoratus* | 171 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Fundulus chrysotus* | 170 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rhamdia guatemalensis* | 170 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rubricatochromis guttatus* | 168 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lepomis gulosus* | 162 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oreochromis niloticus* | 162 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lepomis microlophus* | 161 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anablepsoides hartii* | 155 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rocio octofasciata* | 148 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Heterotilapia buettikoferi* | 146 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia velifera* | 131 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lucania goodei* | 126 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ctenopharyngodon idella* | 121 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gambusia yucatana* | 121 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cichlasoma bimaculatum* | 114 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinus rubrofuscus* | 91 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Andinoacara pulcher* | 89 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia orri* | 87 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Andinoacara coeruleopunctatus* | 86 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Jordanella floridae* | 83 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Elacatinus cayman* | 82 | Meer | zu klein (höchstens 2.33 cm) |
| *Amia calva* | 78 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Typhlias pearsei* | 78 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Vieja maculicauda* | 77 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Tigrigobius dilepis* | 76 | Meer | zu klein (höchstens 2.5 cm) |
| *Astyanax bacalarensis* | 75 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amatitlania nigrofasciata* | 74 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Heterandria formosa* | 73 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Petenia splendida* | 71 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Xiphophorus hellerii* | 70 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Awaous banana* | 67 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hoplosternum littorale* | 66 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gambusia puncticulata* | 62 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hoplias malabaricus* | 62 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Coryphopterus hyalinus* | 60 | Brack/Meer | zu klein (höchstens 2.5 cm) |
| *Fundulus grandis* | 59 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Emblemariopsis bottomei* | 58 | Meer | zu klein (höchstens 2.96 cm) |
| *Fundulus seminolis* | 57 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ophisternon infernale* | 57 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lepomis marginatus* | 56 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Chitala ornata* | 54 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Astyanax bimaculatus* | 52 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amphilophus labiatus* | 51 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ginsburgellus novemlineatus* | 51 | Meer | zu klein (höchstens 2.5 cm) |
| *Labidesthes vanhyningi* | 51 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sicydium punctatum* | 51 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Astatotilapia calliptera* | 48 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Tigrigobius harveyi* | 48 | Meer | zu klein (höchstens 2.11 cm) |
| *Rhamdia quelen* | 46 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hypostomus robinii* | 45 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ictalurus punctatus* | 44 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cryptoheros cutteri* | 43 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Alectis ciliaris* | 42 | Meer | nur tiefer als die Tauchgrenze (erst ab 60 m) |
| *Floridichthys polyommus* | 42 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acyrtops beryllinus* | 41 | Meer | zu klein (höchstens 2.5 cm) |
| *Enneanectes deloachorum* | 41 | Meer | zu klein (höchstens 2.16 cm) |
| *Malacoctenus erdmani* | 41 | Meer | zu klein (höchstens 3.8 cm) |
| *Piaractus brachypomus* | 41 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ariopsis assimilis* | 38 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nomeus gronovii* | 38 | Meer | nur tiefer als die Tauchgrenze (erst ab 200 m) |
| *Pseudoxiphophorus bimaculatus* | 37 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Risor ruber* | 37 | Meer | zu klein (höchstens 2.5 cm) |
| *Enneacanthus gloriosus* | 36 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Heros severus* | 36 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cribroheros alfari* | 35 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cribroheros robertsoni* | 34 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Phallichthys amates* | 34 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Priapichthys annectens* | 34 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ameiurus nebulosus* | 33 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Caquetaia kraussii* | 33 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrognathus siamensis* | 33 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acanthemblemaria rivasi* | 32 | Meer | zu klein (höchstens 3 cm) |
| *Pomoxis nigromaculatus* | 32 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Etheostoma fusiforme* | 31 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acyrtus rubiginosus* | 30 | Meer | zu klein (höchstens 3.5 cm) |
| *Enneanectes matador* | 30 | Meer | zu klein (höchstens 2.1 cm) |
| *Gambusia wrayi* | 30 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sicydium plumieri* | 30 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anableps anableps* | 29 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynodonichthys isthmensis* | 28 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia vandepolli* | 28 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia vivipara* | 28 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Thorichthys meeki* | 28 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cichlasoma taenia* | 27 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nandopsis haitiensis* | 27 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Andinoacara latifrons* | 26 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Enneanectes atrorus* | 26 | Meer | zu klein (höchstens 3.3 cm) |
| *Notemigonus crysoleucas* | 26 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia mexicana* | 26 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ancistrus trinitatis* | 25 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Elacatinus louisae* | 25 | Meer | zu klein (höchstens 3.8 cm) |
| *Poecilia picta* | 24 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trichopsis vittata* | 24 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ameiurus natalis* | 23 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lutjanus vivanus* | 23 | Meer | nur tiefer als die Tauchgrenze (erst ab 90 m) |
| *Alfaro cultratus* | 22 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anableps microlepis* | 22 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gambusia sexradiata* | 22 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gymnotus carapo* | 22 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osteogaster aenea* | 22 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parachromis dovii* | 22 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Elacatinus centralis* | 20 | Meer | zu klein (höchstens 3.79 cm) |
| *Poecilia perugiae* | 20 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pimelodella chagresi* | 20 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia gillii* | 20 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brycon costaricensis* | 19 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Coptodon rendalli* | 19 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Chuco intermedium* | 18 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Tigrigobius pallens* | 18 | Meer | zu klein (höchstens 1.9 cm) |
| *Tigrigobius saucrus* | 18 | Meer | zu klein (höchstens 1.6 cm) |
| *Erimyzon sucetta* | 17 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gambusia punctata* | 17 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia caucana* | 17 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Tomicodon rupestris* | 17 | Meer | zu klein (höchstens 2.73 cm) |
| *Bathygobius geminatus* | 16 | Meer | zu klein (höchstens 3.8 cm) |
| *Cryptoheros chetumalensis* | 16 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Emblemariopsis leptocirris* | 16 | Meer | zu klein (höchstens 2.2 cm) |
| *Rineloricaria uracantha* | 16 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Geophagus crassilabris* | 16 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hoplias microlepis* | 16 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nandopsis tetracanthus* | 16 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amatitlania myrnae* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ancistrus chagresi* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinodon riverendi* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Elassoma evergladei* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Etelis oculatus* | 15 | Meer | nur tiefer als die Tauchgrenze (erst ab 100 m) |
| *Lebiasina panamensis* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Clarias gariepinus* | 14 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyphocharax magdalenae* | 14 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gambusia manni* | 14 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemibrycon taeniurus* | 14 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Alburnops petersoni* | 13 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amatitlania siquia* | 13 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ameiurus catus* | 13 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Atractosteus tristoechus* | 13 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ctenolucius hujeta* | 13 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Emblemariopsis bahamensis* | 13 | Meer | zu klein (höchstens 2.6 cm) |
| *Lythrypnus elasson* | 13 | Meer | zu klein (höchstens 1.58 cm) |
| *Astyanax panamensis* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Atractosteus tropicus* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Coryphopterus kuna* | 12 | Meer | zu klein (höchstens 1.71 cm) |
| *Eleotris perniger* | 12 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Prochilodus reticulatus* | 12 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pygocentrus cariba* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Alfaro huberi* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinodon dearborni* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Panamius panamensis* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parachromis friedrichsthalii* | 11 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Roeboides dientonito* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Callichthys callichthys* | 10 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Emblemariopsis pricei* | 10 | Meer | zu klein (höchstens 2.86 cm) |
| *Emblemariopsis ruetzleri* | 10 | Meer | zu klein (höchstens 2 cm) |
| *Esox niger* | 10 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gambusia hispaniolae* | 10 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemigrammus unilineatus* | 10 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neetroplus nematopus* | 10 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia sphenops* | 10 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Carassius auratus* | 9 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cryptoheros spilurus* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Esox americanus* | 9 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Jordanella pulchra* | 9 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemichromis fasciatus* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia elegans* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Polycentrus schomburgkii* | 9 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Prochilodus magdalenae* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trichopodus pectoralis* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Astyanax belizianus* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Caulolatilus cyanops* | 8 | Meer | nur tiefer als die Tauchgrenze (erst ab 45 m) |
| *Corynopoma riisei* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Emblemariopsis tayrona* | 8 | Meer | zu klein (höchstens 3.1 cm) |
| *Gambusia xanthosoma* | 8 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gephyrocharax atracaudatus* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lepisosteus osseus* | 8 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Phractocephalus hemioliopterus* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rhamdia nicaraguensis* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Xiphophorus maculatus* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amatitlania kanna* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cichla monoculus* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinodon nichollsi* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Geophagus steindachneri* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Helicolenus dactylopterus* | 7 | Meer | nur tiefer als die Tauchgrenze (erst ab 50 m) |
| *Herotilapia multispinosa* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Kryptolebias marmoratus* | 7 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia vittata* | 7 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lythrypnus spilus* | 7 | Meer | zu klein (höchstens 2.5 cm) |
| *Ophisternon aenigmaticum* | 7 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Seriola fasciata* | 7 | Meer | nur tiefer als die Tauchgrenze (erst ab 55 m) |
| *Sternopygus aequilabiatus* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Tomicodon cryptus* | 7 | Meer | zu klein (höchstens 1.9 cm) |
| *Vieja bifasciata* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acanthemblemaria greenfieldi* | 6 | Meer | zu klein (höchstens 3.6 cm) |
| *Amatitlania septemfasciata* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brycon guatemalensis* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Crenicichla geayi* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinus carpio* | 6 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Elacatinus colini* | 6 | Meer | zu klein (höchstens 3.2 cm) |
| *Lepomis auritus* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Megaleporinus muyscorum* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Noturus gyrinus* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Odontostilbe pulchra* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trachelyopterus insignis* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Astronotus mikoljii* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Astyanax nicaraguensis* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brachyhypopomus occidentalis* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brachyrhaphis episcopi* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brachyrhaphis holdridgei* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cribroheros bussingi* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cryptopsilotris batrachodes* | 5 | Meer | zu klein (höchstens 1.9 cm) |
| *Cubanichthys cubensis* | 5 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinodon brontotheroides* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Emblemariopsis lancea* | 5 | Meer | zu klein (höchstens 2.43 cm) |
| *Emblemariopsis occidentalis* | 5 | Meer | zu klein (höchstens 1.92 cm) |
| *Fundulus lineolatus* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gambusia luma* | 5 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gambusia nicaraguensis* | 5 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hyphessobrycon panamensis* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hypostomus hondae* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia nigrofasciata* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia sulphurophila* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lythrypnus heterochroma* | 5 | Meer | zu klein (höchstens 2.5 cm) |
| *Maylandia zebra* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pethia conchonius* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pontinus longispinis* | 5 | Meer | nur tiefer als die Tauchgrenze (erst ab 75 m) |
| *Rachovia maculipinnis* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rineloricaria magdalenae* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Roeboides bouchellei* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Serrasalmus rhombeus* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Tomicodon reitzae* | 5 | Meer | zu klein (höchstens 3.5 cm) |
| *Tomocichla tuba* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Antigonia capros* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Apogon pillionatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Bairdiella chrysoura* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Bathypterois bigelowi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Chaetostoma fischeri* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Colossoma macropomum* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cribroheros longimanus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cypselurus comatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Decapterus tabl* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Emblemaria vitta* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gobiesox cephalus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gobiosoma grosvenori* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gymnothorax ocellatus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Gymnothorax saxicola* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gymnura lessae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hemicaranx amblyrhynchus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hexanchus griseus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hollardia hollardi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hoplosternum magdalenae* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hoplostethus occidentalis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hypostomus wilsoni* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Jenkinsia lamprotaenia* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Poecilia caymanensis* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Liopropoma carmabi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lipogramma trilineata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lonchopisthus micrognathus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lopholatilus chamaeleonticeps* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Microphis brachyurus* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Micropterus chattahoochae* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mobula tarapacana* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Mustelus canis* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Notropis maculatus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oligoplites palometa* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Ophichthus gomesii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Parachromis motaguensis* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Phaeoptyx xenus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Plagioscion magdalenae* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia hispaniolana* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia hondurensis* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Potamotrygon orbignyi* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Prochilodus mariae* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudoplatystoma magdaleniatum* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Quassiremus ascensionis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Remora osteochir* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scorpaena calcarata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scorpaenodes tredecimspinosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Symphurus caribbeanus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Syngnathus fuscus* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Trichomycterus striatus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Vieja zonata* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acyrtus lanthanum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Anablepsoides cryptocallus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anarchopterus criniger* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Anchoa mitchilli* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Anthias asperilinguis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Argyropelecus aculeatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ariosoma balearicum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Astyanax mexicanus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Atherinella brasiliensis* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Atherinella milleri* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Auxis thazard* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bathygobius curacao* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bathytoshia centroura* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Brotula barbata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Carapus bermudensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Carcharhinus isodon* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Carcharodon carcharias* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Cerdale floridana* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chilomycterus spinosus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Cichla orinocensis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Citharichthys spilopterus* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Copella arnoldi* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Coptodon zillii* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Coryphopterus alloides* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cribroheros rhytisma* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cribroheros rostratus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ctenobrycon magdalenae* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ctenogobius smaragdus* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Cynodonichthys rubripunctatus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynopotamus magdalenae* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyttopsis rosea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Echiophis intertinctus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Emblemariopsis diaphana* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Emmelichthyops atlanticus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Enneanectes wilki* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Evorthodus lyricus* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Gambusia pseudopunctata* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gasteropelecus maculatus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gillellus greyae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gobiesox nigripinnis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gobioides broussonnetii* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Gonioplectrus hispanus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Grammicolepis brachiusculus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Guavina guavina* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Gymnothorax nigromarginatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hyporhamphus unifasciatus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Hyporthodus nigritus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hypostomus aspidolepis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lagocephalus lagocephalus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Leucoraja erinaceus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Malacoctenus delalandii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Micropogonias furnieri* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Morone chrysops × saxatilis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mugil trichodon* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Opisthoteuthis agassizii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Opistognathus gilberti* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Opistognathus lonchurus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Oxydoras sifontesi* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paraclinus barbatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paraclinus infrons* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Parexocoetus hillianus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Peprilus paru* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Poecilia wingei* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Polydactylus octonemus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Polydactylus oligodon* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Priapichthys puetzi* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Prionotus carolinus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Prionotus roseus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Pseudocaranx dentex* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Regalecus glesne* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rhamdia laticauda* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rhaphiodon vulpinus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rivulus cylindraceus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Roeboides dayi* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Roeboides guatemalensis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sanopus greenfieldorum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Schedophilus ovalis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Semaprochilodus kneri* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Seriola zonata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Serrasalmus elongatus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Serrasalmus manueli* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sorubim cuspicaudus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sphyrna alleni* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Squalus cubensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Starksia ocellata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Starksia smithvanizi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Starksia splendens* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Stathmonotus hemphillii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Stathmonotus stahli* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Steindachnerina argentea* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sthenoteuthis pteropus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tigrigobius zebrellus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Trichopodus trichopterus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Triportheus magdalenae* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Vomerogobius flavus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Zu cristatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Abralia veranyi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acyrtus artius* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anablepsoides deltaphilus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Apogon robbyi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Archocentrus centrarchus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Argonauta hians* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Astrapogon alutus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Astyanax macal* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Astyanax orstedii* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Barbulifer ceuthoecus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Batrachoides gilberti* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Beryx decadactylus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bollmannia boqueronensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Brachyplatystoma filamentosum* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brachyrhaphis hessfeldi* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bryx dunckeri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bunocephalus colombianus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Callechelys bilinearis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Carcharhinus porosus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Centropomus mexicanus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Centropristis philadelphica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chaunax suttkusi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cheilopogon cyanopterus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cichla intermedia* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Citharichthys macrops* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cookeolus japonicus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Creagrutus bolivari* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Crenuchus spilurus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynodonichthys brunneus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynodonichthys monikae* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynodonichthys tenuis* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynoscion jamaicensis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Cynoscion virescens* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Cyprinodon desquamator* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinodon higuey* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Dactyloscopus tridigitatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Diapterus rhombeus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Dicrossus filamentosus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ekemblemaria nigra* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Elacatinus serranilla* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Emblemaria caldwelli* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Enneanectes flavus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epinnula magistralis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Erythrinus erythrinus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Etmopterus schultzi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gambusia affinis* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gambusia beebei* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gephyrocharax valencia* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gillellus uranidea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Girardinus microdactylus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Girardinus uninotatus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gymnotus cylindricus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemanthias leptus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Heteroconger camelopardalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hexanchus vitulus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hyperoglyphe perciformis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hyporthodus flavolimbatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hyporthodus mystacinus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Illex coindetii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Isurus oxyrinchus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Isurus paucus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lebiasina erythrinoides* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Leporinus ortomaculatus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia melanogaster* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lythrypnus crocodilus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Menticirrhus saxatilis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Mesoheros atromaculatus* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mola mola* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Monocirrhus polyacanthus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Monopterus javanensis* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mugil liza* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Muusoctopus januarii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nannostomus eques* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nanocheirodon insignis* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neoheterandria tridentiger* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nezumia aequalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Octopus maya* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Odontaspis ferox* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Odontognathus compressus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Pangasianodon hypophthalmus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paracanthurus hepatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Paracheirodon axelrodi* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parodon alfonsoi* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parophidion schmidti* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Penetopteryx nanus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Peristedion brevirostre* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Phallichthys quadripunctatus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Piaractus orinoquensis* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pimelodus blochii* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia salvatoris* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Potamotrygon magdalenae* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Potamotrygon schroederi* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Prionace glauca* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Pristipomoides macrophthalmus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Prognichthys occidentalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudophallus mindii* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudoplatystoma orinocoense* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Puntigrus tetrazona* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Remora remora* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rhizoprionodon lalandii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rivulus roloffi* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rypticus randalli* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sarda sarda* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Sargocentron bullisi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scyliorhinus hesperius* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Serrasalmus neveriensis* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sicydium gymnogaster* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sphyrna tudes* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Starksia culebrae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Starksia lepicoelia* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Starksia springeri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Starksia weigti* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Starksia williamsi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Stellifer colonensis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Sternopygus macrurus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sturisomatichthys aureus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Thalassophryne maculosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Thorichthys aureus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Thunnus obesus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Thunnus thynnus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Tigrigobius rubrigenis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tremoctopus violaceus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Uraspis helvola* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Urophycis cirrata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Abramites hypselonotus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acaronia nassa* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acipenser ruthenus* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acyrtops amplicirrus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Adontosternarchus devenanzii* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ageneiosus inermis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ageneiosus lineatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ageneiosus magoi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ageneiosus pardalis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ageneiosus polystictus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Albula nemoptera* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Alepisaurus ferox* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alopias superciliosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amatitlania nanolutea* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ambloplites rupestris* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anarchopterus tectus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anchoa lamprotaenia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anchoa lyolepis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ancistrocheirus lesueurii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ancistrus brevifilis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ancistrus triradiatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ancylopsetta quadrocellata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anduzedoras oxyrhynchus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anisotremus taeniatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anodus orinocensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anthias nicholsi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aphredoderus gibbosus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Apistogramma diplotaenia* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Apistogramma lineata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Apristurus laurussonii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Arothron meleagris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Astroscopus guttatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Astyanax anai* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Astyanax bransfordii* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Astyanax orthodus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Atherinella chagresi* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Aulopus filamentosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Austrofundulus limnaeus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Austrofundulus transilis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Baryancistrus beggini* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bathophilus vaillanti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Batrachoides surinamensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Bellator militaris* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Bothus mancus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Boulengerella lateristriga* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Boulengerella lucius* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brachyplatystoma rousseauxii* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brachyplatystoma vaillantii* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brycon chagrensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brycon falcatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brycon pesu* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brycon whitei* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bryconops colaroja* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Calophysus macropterus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Carcharhinus signatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carcharias taurus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carnegiella strigata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cathorops mapale* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cathorops spixii* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Catoprion mento* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Centrophorus uyato* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cetopsis coecutiens* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cetorhinus maximus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaetostoma anomalum* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Chalceus macrolepidotus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Characidium longum* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cheilopogon furcatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheilopogon heterurus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chlorophthalmus agassizi* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Chortiheros wesseli* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cichla pleiozona* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cichlasoma dimerus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cincelichthys bocourti* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cirrhigaleus asper* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Citharichthys arenaceus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Citharichthys dinoceros* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Compsura gorgonae* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Conger esculentus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cordylancistrus tayrona* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Corvula batabana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ctenogobius shufeldti* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Curimata mivartii* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynodonichthys weberi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynoponticus savanna* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Cynopotamus bipunctatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynoscion acoupa* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Cynoscion arenarius* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Cyphocharax aspilos* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyphotilapia frontosa* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinodon beltrani* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinodon bondi* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Dactyloscopus poeyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dascyllus aruanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Decapterus kurroides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dekeyseria picta* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Diodon eydouxii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diplectrum radiale* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Distocyclus conirostris* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ditropichthys storeri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dormitator latifrons* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Duopalatinus peruanus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eigenmannia macrops* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Elacatinus atronasus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Elachocharax junki* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Electrophorus electricus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eleotris picta* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Emblemaria hyltoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Entomocorus gameroi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Epinephelus ongus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Erotelis smaragdus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Etrumeus sadina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eugerres brasilianus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Exallodontus aguanai* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Exastilithoxus fimbriatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Farlowella odontotumulus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Synchiropus agassizii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fundulus persimilis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gelanoglanis nanonocticolus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Genyatremus luteus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Gilbertolus maracaiboensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gillellus healae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Girardinus creolus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Glanapteryx anguilla* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gymnachirus texae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnocorymbus ternetzi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gymnothorax castaneus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax conspersus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax maderensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Haemulon maculicauda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halieutichthys aculeatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Helogenes marmoratus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemiancistrus subviridis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemiodus gracilis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemiodus unimaculatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemiramphus balao* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Hemisorubim platyrhynchos* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hirundichthys affinis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hirundichthys volador* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hoplias aimara* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hoplias teres* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hyaloteuthis pelagica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hydrolycus armatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hydrolycus wallacei* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hyphessobrycon axelrodi* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hypoplectrus liberte* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hyporhamphus meeki* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Hypostomus plecostomus* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hypsophrys nicaraguensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ichthyapus ophioneus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ichthyoelephas longirostris* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Isorineloricaria acuarius* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Jenkinsia stolifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Kronoheros umbrifer* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Kryptolebias ocellatus* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Labeotropheus fuelleborni* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Laemolyta taeniata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Laetacara fulvipinnis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Laimosemion lyricauda* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Laimosemion tecminae* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lasiancistrus guacharote* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lasiancistrus schomburgkii* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lates niloticus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lebiasina uruyensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lepidocybium flavobrunneum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leporinus brunneus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia immaculata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia miragoanensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia pauciradiata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia yaguajali* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Liopropoma aberrans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Liopropoma eukrines* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Llanolebias stellifer* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lonchopisthus higmani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lophius gastrophysus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lucifuga dentata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lupinoblennius vinctus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Lycengraulis grossidens* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Makunaima pittieri* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Masturus lanceolatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Maurolicus weitzmani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Melanorhinus microps* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Menidia menidia* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Menidia peninsulae* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Mesonauta egregius* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Metynnis fasciatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Microgobius meeki* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Micromoema xiphophora* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mugil brevirostris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mullus auratus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Muraena retifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mustelus higmani* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Myleus setiger* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mylossoma duriventre* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nannostomus nigrotaeniatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Naucrates ductor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neobathyclupea argentea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Odonus niger* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ogcocephalus pantostictus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ommastrephes caroli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophichthus puncticeps* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophisternon berlini* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Opsanus dichrostomus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ostichthys trachypoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxynotus caribbaeus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Panaqolus maccus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Panaque nigrolineatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paraclinus naeorhegmis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paragoniates alburnus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paralichthys lethostigma* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Paralonchurus brasiliensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Paratrygon parvaspina* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pellona harroweri* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pimelodus coprophagus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Platygillellus rubrocinctus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Platynematichthys notatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Platyurosternarchus macrostoma* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia kykesis* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Polyipnus laternatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polylepion gilmorei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polymixia lowei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomacanthus semicirculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pontinus castor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Porichthys plectrodon* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Potamorhina altamazonica* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Potamotrygon motoro* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Potamotrygon yepezi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Prognathodes guyanensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Protemblemaria punctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Psalidodon anisitsi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Psalidodon fasciatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Psenes cyanophrys* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Psenes maculatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pseudanos winterbottomi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudolithoxus anthrax* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudoplatystoma metaense* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudoplatystoma tigrinum* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudoxiphophorus anzuetoi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Psilotris alepis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pterodoras granulosus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pterophyllum scalare* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pterygoplichthys multiradiatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rachovia brevis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rachovia hummelincki* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rachovia pyropunctata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Remora albescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Callionymus calcaratus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhinodoras gallagheri* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rhinoptera brasiliensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rineloricaria melini* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rocio spinosissima* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rostroraja eglanteria* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Rostroraja texana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Salminus affinis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Satanoperca leucosticta* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Saurida normani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scarus ghobban* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Sciades proops* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Scomber colias* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Scorpaena bergii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sepioteuthis lessoniana* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Serranus atrobranchus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Serranus notospilus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Serranus scriba* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Serrasalmus irritans* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Serrasalmus medinai* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sicydium adelum* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sicydium altum* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sicydium buscki* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sicydium salvini* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sparisoma frondosum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sphoeroides dorsalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sphoeroides pachygaster* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Starksia fasciata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Starksia sluiteri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stathmonotus gymnodermis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sternarchorhynchus roseni* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Symphurus ommaspilus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Syngnathus caribbaeus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synodontis eupterus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Synodus poeyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Taractichthys longipinnis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tatia brunnea* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Tetragonopterus argenteus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Thalassophryne nattereri* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Thorichthys affinis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Thunnus alalunga* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tigrigobius gemmatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tomicodon rhabdotus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trachelyopterus galeatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trachurus lathami* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trichomycterus mondolfi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trinectes paulistanus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Triportheus venezuelensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Vladichthys gloverensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xenophallus umbratilis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Xiphophorus mayae* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Xiphophorus variatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Zebrasoma flavescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Zebrasoma scopas* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Zebrasoma velifer* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Zoarces americanus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Zungaro zungaro* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |

</details>

## Subdeck `invertebrates` (40)

Eigene Taxa, Größe und Filter, Reihenfolge-Quelle und Region des Rezepts. Arten, die schon in einem Level oder einem früheren Subdeck stehen, bleiben draußen; die Führer werden nicht abgeglichen.

- iNaturalist: 2682 Taxa (Seiten: 6)
- OBIS: 13421 Arten mit Nachweisen außer iNaturalist

### iNaturalist-Namen zugeordnet

Laut `recipes/inat_names.json`: iNaturalist nennt die Art anders als die Referenz-DB; die Zählung kommt zu der der Referenz-DB-Art.

| iNaturalist | Referenz-DB | iNat | Art | Beleg |
|---|---|---|---|---|
| *Pinnoctopus macropus* | *Callistoctopus macropus* | 29 | Umbenennung | https://www.inaturalist.org/taxon_changes/172613 |

### Von Hand ausgeschlossen

| Art | iNat | Grund |
|---|---|---|
| *Coenobita clypeatus* | 11456 | Landeinsiedlerkrebs, lebt an Land und geht nur zur Eiablage ans Meer. |
| *Cardisoma guanhumi* | 6656 | Landkrabbe, lebt an Land und geht nur zum Laichen ans Meer. |
| *Grapsus grapsus* | 4819 | Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen. |
| *Ocypode quadrata* | 4499 | Geisterkrabbe, lebt am trockenen Sandstrand. |
| *Acanthopleura granulata* | 3708 | Käferschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Nerita versicolor* | 2363 | Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Cenchritis muricatus* | 2149 | Strandschnecke der Spritzwasserzone, sitzt über dem Wasser auf den Uferfelsen. |
| *Nerita tessellata* | 1987 | Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Cittarium pica* | 1919 | Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Aratus pisonii* | 1703 | Mangrovenbaumkrabbe, klettert über dem Wasser in den Mangroven. |
| *Glycymeris spectralis* | 1443 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 358 von 358 Beobachtungen mit Angabe „tot“). |
| *Nerita peloronta* | 1044 | Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Arca zebra* | 939 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 314 von 320 Beobachtungen mit Angabe „tot“). |
| *Chione elevata* | 824 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 438 von 442 Beobachtungen mit Angabe „tot“). |
| *Bulla occidentalis* | 806 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 179 von 191 Beobachtungen mit Angabe „tot“). |
| *Gecarcinus ruricola* | 804 | Landkrabbe, lebt an Land und geht nur zum Laichen ans Meer. |
| *Codakia orbicularis* | 775 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 262 von 266 Beobachtungen mit Angabe „tot“). |
| *Columbella mercatoria* | 751 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 137 von 144 Beobachtungen mit Angabe „tot“). |
| *Barbatia cancellaria* | 665 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 261 von 261 Beobachtungen mit Angabe „tot“). |

### Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Acropora cervicornis* | Die Hirschgeweihkoralle baute einst die Flachriffe der Karibik und ist heute vom Aussterben bedroht; sie wird in Riffgärten nachgezüchtet. | 40 | Reihenfolge-Quelle, OBIS, Verbreitung | invertebrates |
| *Ancylomenes pedersoni* | Die Pederson-Putzergarnele betreibt in Anemonen Putzerstationen, an denen Fische Schlange stehen. | 37 | Reihenfolge-Quelle, OBIS, Verbreitung | invertebrates |
| *Astrophyton muricatum* | Das Gorgonenhaupt entfaltet nachts seine verzweigten Arme auf Gorgonien, ein Höhepunkt jedes Nachttauchgangs. | 79 | Reihenfolge-Quelle, OBIS, Verbreitung | invertebrates |

### Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS ohne iNaturalist oder Verbreitung): 40/40 (100 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 0
- Arten ohne Volksnamen `de` in der Referenz-DB: 34/40 (85 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 0/40 (0 %)
- Familien ohne Volksnamen `de`: 31/31 (100 %): *Acroporidae*, *Actiniidae*, *Agariciidae*, *Amphinomidae*, *Aplysiidae*, *Aplysinidae*, *Callyspongiidae*, *Diadematidae*, *Diogenidae*, *Echinometridae*, *Faviidae*, *Gorgoniidae*, *Gorgonocephalidae*, *Inachidae*, *Merulinidae*, *Milleporidae*, *Oreasteridae*, *Ovulidae*, *Palaemonidae*, *Palinuridae*, *Petrosiidae*, *Physaliidae*, *Plakobranchidae*, *Poritidae*, *Rhizangiidae*, *Sabellidae*, *Serpulidae*, *Stenopodidae*, *Strombidae*, *Toxopneustidae*, *Zoanthidae*
- Familien ohne Volksnamen `en`: 22/31 (71 %): *Acroporidae*, *Actiniidae*, *Agariciidae*, *Amphinomidae*, *Aplysinidae*, *Callyspongiidae*, *Diadematidae*, *Echinometridae*, *Faviidae*, *Gorgoniidae*, *Gorgonocephalidae*, *Inachidae*, *Merulinidae*, *Oreasteridae*, *Petrosiidae*, *Physaliidae*, *Plakobranchidae*, *Poritidae*, *Rhizangiidae*, *Serpulidae*, *Toxopneustidae*, *Zoanthidae*

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

Keine.

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

Keine.

### Arten

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Klasse |
|---|---|---|---|---|---|---|
| 1 | *Gorgonia ventalina* | 4533 | 1253 | native ×1 | Meer | Octocorallia |
| 2 | *Aliger gigas* | 3857 | 1266 | native ×29 | Meer | Gastropoda |
| 3 | *Panulirus argus* | 3856 | 634 | native ×22 | Meer | Malacostraca |
| 4 | *Oreaster reticulatus* | 3650 | 172 | native ×3 | Meer | Asteroidea |
| 5 | *Physalia physalis* (Quelle: *Physalia utriculus*) | 3596 | 40 | – | Meer | Hydrozoa |
| 6 | *Condylactis gigantea* | 3145 | 87 | native ×2 | Meer | Hexacorallia |
| 7 | *Diadema antillarum* | 3094 | 1944 | native ×8 | Meer | Echinoidea |
| 8 | *Echinometra lucunter* | 2826 | 815 | native ×5 | Meer | Echinoidea |
| 9 | *Porites astreoides* | 2511 | 32603 | native ×5 | Meer | Hexacorallia |
| 10 | *Cyphoma gibbosum* | 2442 | 580 | native ×6 | Meer | Gastropoda |
| 11 | *Acropora palmata* | 2440 | 9331 | native ×28 | Meer | Hexacorallia |
| 12 | *Pseudodiploria strigosa* | 2334 | 18912 | native ×7 | Meer | Hexacorallia |
| 13 | *Spirobranchus giganteus* | 2324 | 72 | native ×2 | Meer | Polychaeta |
| 14 | *Elysia crispata* | 2285 | 197 | native ×5 | Meer | Gastropoda |
| 15 | *Hermodice carunculata* | 2244 | 232 | native ×3 | Meer | Polychaeta |
| 16 | *Montastraea cavernosa* | 2026 | 22791 | native ×7 | Meer | Hexacorallia |
| 17 | *Stenorhynchus seticornis* | 1901 | 620 | native ×26 | Meer | Malacostraca |
| 18 | *Xestospongia muta* | 1760 | 966 | native ×5 | Brack/Meer | Demospongiae |
| 19 | *Tripneustes ventricosus* | 1681 | 622 | native ×3 | Meer | Echinoidea |
| 20 | *Diploria labyrinthiformis* | 1597 | 7723 | native ×5 | Meer | Hexacorallia |
| 21 | *Stenopus hispidus* | 1564 | 248 | native ×4 | Meer | Malacostraca |
| 22 | *Siderastrea siderea* | 1529 | 28065 | native ×26 | Meer | Hexacorallia |
| 23 | *Orbicella faveolata* | 1492 | 29530 | native ×3 | Meer | Hexacorallia |
| 24 | *Orbicella annularis* | 1421 | 26957 | native ×7 | Meer | Hexacorallia |
| 25 | *Sabellastarte magnifica* | 1357 | 51 | native ×3 | Meer | Polychaeta |
| 26 | *Agaricia agaricites* | 1291 | 19334 | native ×22 | Meer | Hexacorallia |
| 27 | *Aplysina fistularis* | 1280 | 137 | native ×6 | Brack/Meer | Demospongiae |
| 28 | *Palythoa caribaeorum* | 1269 | 1523 | native ×1 | Meer | Hexacorallia |
| 29 | *Aplysia dactylomela* | 1239 | 68 | native ×5 | Meer | Gastropoda |
| 30 | *Millepora alcicornis* | 1189 | 9704 | native ×4 | Brack/Meer | Hydrozoa |
| 31 | *Porites porites* | 1179 | 13329 | native ×20 | Meer | Hexacorallia |
| 32 | *Aiolochroia crassa* | 1068 | 114 | native ×6 | Brack/Meer | Demospongiae |
| 33 | *Colpophyllia natans* | 1005 | 11954 | native ×5 | Meer | Hexacorallia |
| 34 | *Clibanarius tricolor* | 990 | 86 | native ×4 | Meer | Malacostraca |
| 35 | *Callyspongia plicifera* | 964 | – | native ×4 | Meer | Demospongiae |
| 36 | *Millepora complanata* | 952 | 7558 | native ×3 | Brack/Meer | Hydrozoa |
| 37 | *Ancylomenes pedersoni* (Highlight; 335 Beobachter) | 907 | 136 | native ×2 | Meer | Malacostraca |
| 38 | *Aplysina archeri* | 906 | 69 | native ×2 | Brack/Meer | Demospongiae |
| 40 | *Acropora cervicornis* (Highlight; 382 Beobachter) | 875 | 2516 | native ×28 | Meer | Hexacorallia |
| 79 | *Astrophyton muricatum* (Highlight; 187 Beobachter) | 497 | 260 | native ×2 | Meer | Ophiuroidea |

### Grenzfälle

Je 10 Arten vor und nach der Grenze (Highlights übersprungen).

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Klasse | Im Subdeck |
|---|---|---|---|---|---|---|---|
| 28 | *Palythoa caribaeorum* | 1269 | 1523 | native ×1 | Meer | Hexacorallia | ja |
| 29 | *Aplysia dactylomela* | 1239 | 68 | native ×5 | Meer | Gastropoda | ja |
| 30 | *Millepora alcicornis* | 1189 | 9704 | native ×4 | Brack/Meer | Hydrozoa | ja |
| 31 | *Porites porites* | 1179 | 13329 | native ×20 | Meer | Hexacorallia | ja |
| 32 | *Aiolochroia crassa* | 1068 | 114 | native ×6 | Brack/Meer | Demospongiae | ja |
| 33 | *Colpophyllia natans* | 1005 | 11954 | native ×5 | Meer | Hexacorallia | ja |
| 34 | *Clibanarius tricolor* | 990 | 86 | native ×4 | Meer | Malacostraca | ja |
| 35 | *Callyspongia plicifera* | 964 | – | native ×4 | Meer | Demospongiae | ja |
| 36 | *Millepora complanata* | 952 | 7558 | native ×3 | Brack/Meer | Hydrozoa | ja |
| 38 | *Aplysina archeri* | 906 | 69 | native ×2 | Brack/Meer | Demospongiae | ja |
| | **Grenze** | | | | | | |
| 39 | *Isostichopus badionotus* | 886 | 188 | native ×8 | Meer | ? | nein |
| 41 | *Pseudodiploria clivosa* | 874 | 2787 | native ×6 | Meer | ? | nein |
| 42 | *Cassiopea andromeda* | 861 | 1 | – | Meer | ? | nein |
| 43 | *Ircinia felix* | 850 | 196 | native ×7 | Brack/Meer | ? | nein |
| 44 | *Fasciolaria tulipa* | 831 | 721 | native ×21 | Meer | ? | nein |
| 45 | *Bartholomea annulata* | 826 | 118 | native ×2 | Meer | ? | nein |
| 46 | *Niphates digitalis* | 804 | 52 | native ×4 | Brack/Meer | ? | nein |
| 47 | *Petrochirus diogenes* | 794 | 185 | native ×1 | Meer | ? | nein |
| 48 | *Anamobaea orstedii* | 791 | 4 | native ×2 | Meer | ? | nein |
| 49 | *Stichodactyla helianthus* | 782 | 52 | native ×2 | Meer | ? | nein |

### Ausgeschlossene Kandidaten

<details><summary>705 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Coenobita clypeatus* | 11456 | Brack/Meer | von Hand ausgeschlossen (Landeinsiedlerkrebs, lebt an Land und geht nur zur Eiablage ans Meer.) |
| *Cardisoma guanhumi* | 6656 | Meer | von Hand ausgeschlossen (Landkrabbe, lebt an Land und geht nur zum Laichen ans Meer.) |
| *Grapsus grapsus* | 4819 | Meer | von Hand ausgeschlossen (Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen.) |
| *Ocypode quadrata* | 4499 | Brack/Meer | von Hand ausgeschlossen (Geisterkrabbe, lebt am trockenen Sandstrand.) |
| *Acanthopleura granulata* | 3708 | Meer | von Hand ausgeschlossen (Käferschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Nerita versicolor* | 2363 | Süß/Meer | von Hand ausgeschlossen (Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Cenchritis muricatus* | 2149 | Meer | von Hand ausgeschlossen (Strandschnecke der Spritzwasserzone, sitzt über dem Wasser auf den Uferfelsen.) |
| *Sepioteuthis sepioidea* | 2022 | Meer | schon in einem anderen Subdeck (level-2) |
| *Nerita tessellata* | 1987 | Meer | von Hand ausgeschlossen (Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Cittarium pica* | 1919 | Meer | von Hand ausgeschlossen (Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Aratus pisonii* | 1703 | Brack/Meer | von Hand ausgeschlossen (Mangrovenbaumkrabbe, klettert über dem Wasser in den Mangroven.) |
| *Glycymeris spectralis* | 1443 | Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 358 von 358 Beobachtungen mit Angabe „tot“).) |
| *Nerita peloronta* | 1044 | Meer | von Hand ausgeschlossen (Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Octopus insularis* | 1038 | Meer | schon in einem anderen Subdeck (level-2) |
| *Arca zebra* | 939 | Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 314 von 320 Beobachtungen mit Angabe „tot“).) |
| *Chione elevata* | 824 | Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 438 von 442 Beobachtungen mit Angabe „tot“).) |
| *Bulla occidentalis* | 806 | Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 179 von 191 Beobachtungen mit Angabe „tot“).) |
| *Gecarcinus ruricola* | 804 | Meer | von Hand ausgeschlossen (Landkrabbe, lebt an Land und geht nur zum Laichen ans Meer.) |
| *Codakia orbicularis* | 775 | Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 262 von 266 Beobachtungen mit Angabe „tot“).) |
| *Columbella mercatoria* | 751 | Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 137 von 144 Beobachtungen mit Angabe „tot“).) |
| *Barbatia cancellaria* | 665 | Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 261 von 261 Beobachtungen mit Angabe „tot“).) |
| *Octopus briareus* | 628 | Meer | schon in einem anderen Subdeck (level-3) |
| *Marisa cornuarietis* | 426 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Spirula spirula* | 283 | Meer | nur tiefer als die Tauchgrenze (erst ab 100 m) |
| *Elliptio jayensis* | 278 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Melanoides tuberculata* | 179 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Corbicula fluminea* | 151 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Verongula reiswigi* | 147 | Meer | nur tiefer als die Tauchgrenze (erst ab 76 m) |
| *Clavelina puertosecensis* | 140 | Meer | nur tiefer als die Tauchgrenze (erst ab 60 m) |
| *Pomacea canaliculata* | 70 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cherax quadricarinatus* | 43 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Alatina alata* | 39 | Meer | nur tiefer als die Tauchgrenze (erst ab 55 m) |
| *Siphonodictyon brevitubulatum* | 39 | Meer | nur tiefer als die Tauchgrenze (erst ab 67 m) |
| *Diplastrella megastellata* | 36 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Papyridea lata* | 28 | Meer | nur tiefer als die Tauchgrenze (erst ab 73 m) |
| *Utterbackia imbecillis* | 25 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neopetrosia proxima* | 16 | Brack/Meer | nur tiefer als die Tauchgrenze (erst ab 53 m) |
| *Planorbella trivolvis* | 16 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Plakina jamaicensis* | 13 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Batzella rubra* | 12 | Meer | nur tiefer als die Tauchgrenze (erst ab 90 m) |
| *Micratya poeyi* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Procambarus clarkii* | 8 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mycale angulosa* | 7 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pomacea bridgesii* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eumunida picta* | 6 | Meer | nur tiefer als die Tauchgrenze (erst ab 200 m) |
| *Gastroptychus spinifer* | 6 | Meer | nur tiefer als die Tauchgrenze (erst ab 225 m) |
| *Uniomerus carolinianus* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Physella acuta* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acanthacaris caeca* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Acanthilia intermedia* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Acanthochitona astrigera* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Alpheus angulosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Alpheus paraformosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Acanthochitona andersoni* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Antalis antillarum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Antipathes atlantica* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Aplysia cervina* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Astrangia poculata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Atrina serrata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Bathynomus giganteus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Berghia stephanieae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Busycon carica* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Caliphylla mediterranea* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Calliostoma adelae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Chiridota rotifera* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Choristodon robustus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cinetorhynchus rigens* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Clathrina clathrus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Clypeasterophilus rugatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Conasprella delessertii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Coralliophila salebrosa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pyrgospira tampaensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cyerce nicholasi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cyphoma christahemmenae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Desmanthus incrustans* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Dibaphimitra florida* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Diodora meta* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Diplosoma spongiforme* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Donax vellicatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Doto chica* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Encope emarginata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Eupolyodontes batabanoensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Flabellina dana* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Forskalia edwardsii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Globivenus rigida* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Haliclona manglaris* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Hemipolygona mcgintyi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Holothuria arenicola* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Holothuria impatiens* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ischnochiton kaasi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Janthina umbilicata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Jaspidella jaspidea* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Laevicardium angmagsalikense* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Latitriphora albida* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ligia platycephala* | 4 | ? | zu wenige Nachweise (4 < 5) |
| *Lissodendoryx sigmata* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Lucina roquesana* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lysmata wurdemanni* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Macrobrachium olfersii* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Macrobrachium rosenbergii* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Madracis carmabi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Malmgreniella variegata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Monoplex vespaceus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Muricopsis deformis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Mycale magnirhaphidifera* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Nassarius consensus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Neverita delessertiana* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Niphates alba* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Notarchus punctatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Olivella floralia* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Olivella lactea* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ophioderma squamosissimum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ophiolepis impressa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pagurus longicarpus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pedipes mirabilis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Perophora viridis* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Petricolaria pholadiformis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Petrolisthes caribensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Plesiothyreus hamillei* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Plexaurella nutans* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pontonides unciger* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pseudoplexaura flagellosa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Rhizopsammia bermudensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scaphella junonia* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sclerodactyla briareus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Thylacodes riisei* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sesarma curacaoense* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Spongia graminea* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Tamoya haplonema* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Tegula gruneri* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Thecacera pennigera* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Truncatella clathrus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Tylos wegeneri* | 4 | ? | zu wenige Nachweise (4 < 5) |
| *Tyrinna evelinae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Vermicularia spirata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Acteocina canaliculata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Aequorea floridana* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Alima neptuni* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Amphibalanus improvisus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sclerodoris worki* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Anisopagurus asteriscus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Anisopagurus pygmaeus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Aplidium stellatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Aplysilla sulfurea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ascobulla ulla* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Berthella agassizii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bhawania goodei* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Botruanthus mexicanus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bulla solida* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Calliostoma pulchrum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Doriopsilla pharpa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chelonaplysilla betinensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cladopsammia manuelensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Clathria foliacea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Clathria prolifera* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Clathrina coriacea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus anabathrum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus bahamensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus burryae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Coralliophila erosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Corbula dietziana* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Corolla spectabilis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Costoanachis scutulata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Diplosoma listerianum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Diaulula phoca* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ellisella elongata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ellisella schmitti* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Elysia patina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Epialtus bituberculatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Epitonium angulatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Eunephrops cadenasi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Eunicea laxispica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Eurytellina angulosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Felimare nyalya* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Goniaster tessellatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Haliclona curacaoensis* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Hepatus pudibundus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Holothuria cubana* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Holothuria glaberrima* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Homola vigil* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hypoconcha parasitica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Isostichopus macroparentheses* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Leukoma granulata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lioberus castanea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lithophaga nigra* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Longchaeus suturalis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lysmata ankeri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Macrobrachium panamense* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Madracis senaria* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mitrella dichroa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Moira atropos* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Myosotella myosotis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Nassarius paucicostatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Niveria nix* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Oculina arbuscula* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ophiolepis paucispina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ophiomyxa flaccida* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Opisthoteuthis agassizii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ovalipes stephensoni* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pachycheles monilifer* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pachycheles riisei* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pachygrapsus corrugatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Panopeus lacustris* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Panopeus occidentalis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Parvanachis obesa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Perophora regina* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Persephona aquilonaris* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Persicula interruptolineata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Petrolisthes jugosus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Petrolisthes politus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Phronima sedentaria* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Placida cremoniana* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Planorbella scalaris* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Platylambrus granulatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pleurobranchaea inconspicua* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Polygona angulata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Polymesoda arctata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Poraniella echinulata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Porcellio scaber* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Porites colonensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Prunum amabile* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Prunum leonardhilli* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Prunum marginatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Prunum pruinosum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Radiolucina amianta* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sabellastarte spectabilis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sanguinolaria sanguinolenta* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Scyllarides nodifer* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sesarma rectum* | 3 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sicyonia brevirostris* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sinum maculatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Solanderia gracilis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Steironepion moniliferum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sthenoteuthis pteropus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Stomozoa roseola* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Streptocephalus texanus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Strigilla surinamensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Styela canopus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Suturoglypta iontha* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tellidora cristata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Truncatella caribaeensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Turbo canaliculatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ventridens demissus* | 3 | ? | zu wenige Nachweise (3 < 5) |
| *Volvarina maya* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Zyzzyzus warreni* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Abralia veranyi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acanthochitona pygmaea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acteocina lepta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Aesopus stearnsii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Alaba incerta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Alpheus heterochaelis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Alpheus paracrinitus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Alpheus websteri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anachis veleda* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anilocra abudefdufi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Antillophos candeanus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Argonauta hians* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Armases rubripes* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ascidia interrupta* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Asterias forbesi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Asterinides folium* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Athorybia rosacea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Atys riiseanus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Aurelia aurita* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Aurelia coerulea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Axinella polycapella* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bailya intricata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bailya parva* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bayerotrochus midas* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Branchiomma bairdi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Caecum plicatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Caecum tornatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Callyspongia tenerrima* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cassidulus caribaearum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cestoplana rubrocincta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chaceon quinquedens* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chaetacanthus magnificus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chaetopleura apiculata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cirsotrema dalli* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cliona schmidtii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus brianoi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus ceruttii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus cingulatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Costoanachis sertulariarum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Crassinella lunulata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Creseis acicula* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cyphoma intermedium* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dendrodoris warta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Desmophyllum pertusum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dichotomia cannoides* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Didemnum conchyliatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dissodactylus crinitichelis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dissodactylus mellitae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Donax fossor* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dulichiella appendiculata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ebalia cariosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eburna balteata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ericthonius brasiliensis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Eugonatonotus crassus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eulithidium affine* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eunicea clavigera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eunicea succinea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eurypanopeus depressus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eutiara mayeri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fargoa bushiana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Felimare marci* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Felimida regalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fiona pinnata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Geitodoris pusae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Glossobius hemiramphi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Glyphocrangon longleyi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gouldia cerina* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Halichondria melanadocia* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Haliclona mucifibrosa* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Heliacus cylindricus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Herdmania pallida* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hermenia verruculosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hippolyte nicholsoni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hymeniacidon heliophila* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Illex coindetii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ischnochiton hartmeyeri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Jorunna spazzola* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Laciolina magna* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lapinura divae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lepidopa richmondi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lightiella incisa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lindapecten exasperatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lithotrya dorsalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lumbrineris perkinsi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Macrobrachium americanum* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrocoeloma subparallelum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Martesia striata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mazatlania cosentini* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Millepora striata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mitrella nycteis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Moinodaphnia macleayi* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Musculus lateralis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Muusoctopus januarii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nanomia bijuga* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Octopus maya* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Oliva tisiphona* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ophidiaster guildingi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ophiocomella ophiactoides* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ophioderma phoenia* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ophiolepis elegans* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ostrea equestris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pagurus pollicaris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Parastarte triquetra* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Diaulula greeleyi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Penaeus notialis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Penaeus setiferus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Phylliroe bucephala* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Physophora hydrostatica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pitho anisodon* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pitho laevigata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pitho lherminieri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Planorbella duryi* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pleurolucina hendersoni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Polyophthalmus pictus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Potimirim potimirim* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudoplexaura porosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Muricopsis withrowi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rocellaria stimpsonii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Saccostrea cuccullata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scleropactes zeteki* | 2 | ? | zu wenige Nachweise (2 < 5) |
| *Semelina nuculoides* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sicyonia typica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Simnialena uniplicata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Squilla empusa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Strongylacidon griseum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Swiftia exserta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Symethis variolosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Synalpheus dominicensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tremoctopus violaceus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tropiometra carinata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Truncatella scalaris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Turritella exoleta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Turritellinella tricarinata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tylos marcuzzii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Urosalpinx cinerea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vokesimurex chrysostoma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vokesimurex donmoorei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Voluta virescens* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acanthochitona roseojugum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Achelous spinicarpus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Achelous tumidulus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cylichnella bidentata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Agelas dilatata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Siphonodictyon siphonum* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Albunea gibbesii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alitta succinea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alpheus glaber* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alpheus nuttingi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alpheus thomasi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alpheus viridari* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alvania auberiana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amblyosyllis rhombeata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Americonuphis magna* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ancistrocheirus lesueurii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anodontites trapesialis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anomoeomunida caribensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Antipathes lenta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Araeosoma fenestratum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Arenicola marina* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Armases miersii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Artemia salina* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Artemisina melana* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Atrina seminuda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Axinella waltonsmithi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Balanus crenatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Basterotia quadrata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Berghia columbina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Biemna cribaria* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Biomphalaria havanensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Boonea impressa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Botryllus schlosseri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bractechlamys vexillum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Brissopsis atlantica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bursa grayana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Busycotypus canaliculatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Calappa sulcata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Callinectes rathbunae* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Calliostoma euglyptum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Callistochiton shuttleworthianus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calyx maya* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Camposcia retusa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cardisoma crassum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carpilius convexus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Casmaria atlantica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cassidinidea ovalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ceraesignum maximum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cerithiopsis flava* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cerithiopsis gemmulosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cerodrillia perryae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cerodrillia thea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chama inezae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chasmocarcinus cylindricus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheilea striata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chelonibia caretta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chicoreus dunni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cidaris blakei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cladonema radiatum* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Clathrina hondurensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clathrodrillia solida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conasprella bajanensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conasprella centurio* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conasprella mazei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conchoderma auritum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conopea galeata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus amphiurgus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus bayeri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus cardinalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus duffyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus ebraeus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus explorator* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus glenni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus kirkandersi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus sahlbergi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coronula diadema* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Crangonyx floridanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Crassispira cubana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Crassispira pellisphocae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cratena pilata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Crepidula depressa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cribrochalina dura* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cubaia aphrodite* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Cumingia sinuosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cyclosalpa affinis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cyclostrema cancellatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cylindrobulla beauii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cymatium raderi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cyphoma rhomba* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Daphnella lymneiformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dendropoma nebulosum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dentalium laqueatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dentimargo aureocincta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dermomurex pauperculus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Deutella incerta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diacavolinia longirostris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diaulula farmersi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Didemnum granulatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Didemnum psammatodes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Didiscus oxeatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diodogorgia nodulifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diodora arcuata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diodora sayi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diodora variegata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dolabrifera dolabrifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Doriopsilla nigrolineata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dosima fascicularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Doto cabecar* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Doto caramella* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dysidea avara* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ebalia stimpsonii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ecteinascidia conklini* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Elachisina floridana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Elysia diomedea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Elysia evelinae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Elysia nisbeti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Enoplobranchus sanguineus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ensis leei* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Entemnotrochus adansonianus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epactophanes richardi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Epialtus dilatatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epialtus longirostris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epitonium albidum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epitonium humphreysii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epitonium nautlae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epitonium tollini* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eualetes tulipa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eudendrium carneum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eulima fulvocincta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eulithidium bellum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eulithidium pterocladicum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eulithidium thalassicola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eunicea tourneforti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eupleura sulcidentata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eupolymnia crassicornis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eurypanopeus abbreviatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eurytellina punicea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eutriphora bermudensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Favia gravida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fissurella barbouri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Folinia mottezi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gari circe* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gelagna succincta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Geukensia granosissima* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gnesioceros sargassicola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Godiva rubrolineata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gonodactylus chiragra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichondria panicea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Harmothoe aculeata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Heliacus bisulcatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hexapanopeus angustifrons* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hippolyte obliquimanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hipponix costellatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hippospongia lachne* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hourstonius laguna* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hyaloteuthis pelagica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hypoconcha arcuata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hypoconcha spinosissima* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Iasis cylindrica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Iphione ovata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ischadium recurvum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ischioscia panamensis* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Isocheles wurdemanni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Jaspidella blanesi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Jonga serrei* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Kirchenpaueria halecioides* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Kurtziella limonitella* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Laciolina laevigata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Laemodonta cubensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Larsonia pterophylla* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leucaltis clathria* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Liriope tetraphylla* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Littoraria tessellata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lottia cubensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Loxothylacus texanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lucidella tantilla* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Macrobrachium amazonicum* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrocoeloma intermedium* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mactrellona exoleta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Malleus candeanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Megabalanus stultus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Megalobrachium soriatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Melanella conoidea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Melanella hypsela* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Melanella polita* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Metapenaeopsis smithi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Metaxia prompta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Metoporhaphis calcarata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Microcosmus squamiger* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mithrax tortugae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Monocorophium tuberculatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Monoplex parthenopeus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Morum lindae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Munidopsis erinacea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Muricea elongata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Musculium partumeium* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nanobalcis worsfoldi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Natica menkeana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Naushonia draconis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Naushonia portoricensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nemausa acuticornis* | 1 | Süß/Meer | zu wenige Nachweise (1 < 5) |
| *Neogonodactylus torus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neopetrosia dendrocrevacea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neothyonidium parvum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nerita funiculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nerita scabricosta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Newmanella radiata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Niambia squamata* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Nidorellia armata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Obelia geniculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oculina patagonica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Olindias muelleri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oliva nivosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Olivella watermani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ommastrephes caroli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiocoma aethiops* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophioderma longicaudum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Orchistoma pileus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxynoe azuropunctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pagurus curacaoensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Palaemon floridanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Palaemon vulgaris* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Parhyale hawaiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parvilucina crenella* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pectinaria gouldii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pelia rotunda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Penaeus aztecus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Periclimenaeus caraibicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Periclimenes meyeri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Periphyllopsis braueri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Perotrochus quoyanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Petrolisthes tonsorius* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllangia pequegnatae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllaplysia padinae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllidiella molaensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pilsbryspira albinodata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pilsbryspira monilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pitho aculeata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pitho quadridentata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Platorchestia platensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plexaurella grisea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plocamopherus tilesii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Podochela grossipes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pododesmus rudis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polyandrocarpa anguinea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polycarpa cartilaginea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polycarpa insulsa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polyclinum constellatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polymesoda caroliniana* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Polyonyx gibbesi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polystira florencae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Porcellionides saussurei* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Portoricoscia richmondi* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Probopyrinella latreuticola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Propustularia surinamensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Prosuberites laughlini* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Prunum roscidum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Psalidopus barbouri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudarcopagia disculus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudevadne tergestina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudocoutierea antillensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pustulatirus virginensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pyrgocythara hemphilli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pyrgophorus parvulus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pyrosoma atlanticum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pyrostremma spinosum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rangia flexuosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rapana rapiformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Retilaskeya bicolor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhithropanopeus harrisii* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Rhizophysa filiformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhizopsammia goesi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhopilema verrilli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rissoina dyscrita* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rostanga byga* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sabaco elongatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Salpa fusiformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scaphella gouldiana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sclerodoris prea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sconsia grayi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Selva rubra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Semele bellastriata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sepioteuthis lessoniana* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Sertularella diaphana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sesarma reticulatum* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Sigatica semisulcata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Solena obliqua* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Solenosteira cancellaria* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Solmissus incisa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Spathochlamys benedicti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sphaeroma quadridentatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Spondylus varius* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Spongiobranchaea australis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Staurocladia vallentini* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stegopontonia commensalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stenocionops furcatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stephanomia amphytridis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Strigilla mirabilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Striostrea prismatica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Styela clava* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stygiomysis major* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sycon ciliatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synalpheus bituberculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synalpheus fritzmuelleri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tamoya ohboya* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tenaturris bartlettii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Teredothyra dominicensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thetys vagina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thylacodes adamsii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thyonella gemmata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Transennella conradina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trapania maringa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tremaster mirabilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trididemnum cyanophorum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Triphora turtlebayensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Triptychus niveus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tryonia aequicostata* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Typhlatya monae* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Upogebia affinis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Upogebia omissa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Volvarina abbreviata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xiphopenaeus kroyeri* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |

</details>

### Nicht aufgelöste Namen

<details><summary>870 Namen</summary>

*Zachrysia provisoria* (3787), *Liguus fasciatus* (3005), *Caracolus caracolla* (2754), *Bulimulus guadalupensis* (2588), *Hartnollius lateralis* (2098), *Lissachatina fulica* (1795), *Caracolus marginella* (1590), *Mesembrinus multilineatus* (1208), *Amphimedon nodosa* (1036), *Granodomus lima* (1033), *Leidyula floridana* (856), *Callyspongia aculeata* (847), *Orthalicus floridensis* (744), *Chionopsis intapurpurea* (620), *Parthena acutangula* (613), *Pomacea maculata* (571), *Lamarcka imbricata* (504), *Cerion incanum* (488), *Gaeotis nigrolineata* (479), *Naria turdus* (446), *Nenia tridens* (439), *Cliothosa delitrix* (429), *Cubaris murina* (414), *Volutella muricata* (372), *Minuca rapax* (356), *Siphonaria naufragum* (355), *Neopupina crocea* (339), *Subulina octona* (333), *Cerion uva* (324), *Polygyra cereolus* (322), *Dallocardia muricata* (305), *Bradybaena similaris* (301), *Megalobulimus oblongus* (276), *Bulimulus bonariensis* (275), *Otala lactea* (263), *Venezillo parvus* (255), *Stylocheilus polyomma* (251), *Neoterebra dislocata* (249), *Mesembrinus dominicus* (248), *Orthalicus undatus* (245), *Agathistoma fasciatum* (241), *Edmundsella dushia* (220), *Mesembrinus elongatus* (218), *Johnsonella fausta* (199), *Cerion striatellum* (187), *Hysteroconcha dione* (170), *Armadillidium vulgare* (166), *Hemitrochus varians* (152), *Plekocheilus glaber* (148), *Veronicella sloanii* (147), *Euglandina rosea* (143), *Epilobocera sinuatifrons* (142), *Liguus virgineus* (136), *Omalacantha bicornuta* (131), *Navanax gemmatus* (130), *Leptuca pugilator* (129), *Cinctura hunteria* (119), *Nereina punctulata* (117), *Parachondria dentata* (116), *Armases americanum* (111), *Orthalicus princeps* (109), *Calcinus verrillii* (102), *Alcadia alta* (100), *Beckianum beckianum* (98), *Mexorchestia carpenteri* (97), *Polymita picta* (96), *Felimare zebra* (93), *Creaseria morleyi* (92), *Palythoa grandiflora* (91), *Sarasinula plebeia* (91), *Orthalicus reses* (89), *Thelidomus aspera* (89), *Caracolus excellens* (88), *Prostheceraeus crozieri* (88), *Vermicularia lumbricalis* (86), *Mesembrinus liliaceus* (85), *Felimida clenchi* (83), *Helicina dysoni* (83), *Caviturritella variegata* (81), *Camachoaglaja berolina* (80), *Cerithideopsis scalariformis* (78), *Chromolaichma hemera* (78), *Caracolus sagemon* (76), *Orienthella verta* (76), *Epilobocera haytensis* (73), *Neptunazurea kempfi* (72), *Dentellaria formosa* (69), *Microceramus pontificus* (69), *Rumina decollata* (69), *Antidrymaeus sulphureus* (68), *Dondice arianeae* (67), *Elysia ellenae* (67), *Elysia jibacoaensis* (65), *Elysia pratensis* (65), *Fulguropsis pyruloides* (61), *Learchis evelinae* (61), *Camachoaglaja mariagordae* (60), *Helicina striata* (59), *Tanychlamys indica* (59), *Leptinaria unilamellata* (58), *Coelocarteria bartschi* (57), *Globivasum capitellum* (57), *Poppiana dentata* (56), *Claremontiella nodulosa* (55), *Agelas schmidtii* (54), *Kalolophus speciosus* (54), *Felimare juliae* (53), *Helicina orbiculata* (53), *Dondice freddiemercuryi* (52), *Drymonema larsoni* (52), *Helicina fasciata* (52), *Lirophora varicosa* (52), *Procambarus alleni* (52), *Actinopyga agassizii* (51), *Dondice juansanchezi* (51), *Ovachlamys fulgens* (51), *Pomacea flagellata* (51), *Cornu aspersum* (50), *Polymita muscarum* (50), *Anadara hemidesmos* (49), *Cerion tridentatum* (49), *Pleurodonte orbiculata* (49), *Dolabrifera ascifera* (48), *Pugilina tupiniquim* (48), *Pleurodonte isabella* (47), *Helicina nemoralis* (46), *Gyroscala commutata* (45), *Allopeas gracile* (44), *Neotiara nodulosa* (44), *Parachondria riisei* (44), *Bergia puertoricense* (43), *Doto curere* (42), *Cyphoma cassidyae* (40), *Nanuca leali* (40), *Callinina georgiana* (39), *Gulella bicolor* (39), *Paguristes karenae* (39), *Phallusia fragilis* (39), *Pseudochama cristella* (39), *Platysuccinea portoricensis* (37), *Poecilozonites bermudensis* (37), *Polydontes luquillensis* (37), *Pseudobiceros pardalis* (36), *Ranularia cynocephala* (36), *Tudora megacheilos* (36), *Clathria opalina* (35), *Dondice jupiteriensis* (35), *Neocyclotus dysoni* (35), *Anamobaea phyllisae* (34), *Bulbaeolidia oasis* (34), *Tayuva branneri* (34), *Antromysis cenotensis* (33), *Pomacea urceus* (33), *Fulguropsis keysensis* (32), *Haliclona zeae* (32), *Prostheceraeus floridanus* (32), *Thylacodes bermudensis* (32), *Hispaniolana crispata* (31), *Ischnoplax pectinata* (31), *Leidyula moreleti* (31), *Leptuca thayeri* (31), *Polymesoda floridana* (31), *Amphithrax verrucosus* (30), *Atya scabra* (30), *Bellactis caeruleus* (30), *Biemna trisigmata* (30), *Coryda ovumreguli* (30), *Leptuca leptodactyla* (30), *Ophiomastix wendtii* (30), *Vitta usnea* (30), *Macroceramus microdon* (29), *Archachatina marginata* (28), *Elysia zemi* (28), *Mesembrinus mossi* (28), *Conus dominicanus* (27), *Helicina platychila* (27), *Pomacea glauca* (27), *Agelas repens* (26), *Amphithrax aculeatus* (26), *Chelonaplysilla americana* (26), *Elysia pawliki* (26), *Helicina amoena* (26), *Americhiton zebra* (25), *Amphimedon caribica* (25), *Boriquena playa* (25), *Chioneryx pygmaea* (25), *Pleurehdera vialactea* (25), *Pseudoceros rawlinsonae* (25), *Villosa amygdalum* (25), *Atya lanipes* (24), *Coryda alauda* (24), *Montfortia emarginata* (24), *Plekocheilus coloratus* (24), *Minuca burgersi* (23), *Tytthosoceros mopsus* (23), *Vansoestia caribensis* (23), *Xibalbanus tulumensis* (23), *Eurycratera jamaicensis* (22), *Hydrozoanthus tunicans* (22), *Orthalicus maracaibensis* (22), *Praticolella mexicana* (22), *Tudora aurantia* (22), *Agathistoma viridulum* (21), *Diplosolenodes occidentalis* (21), *Mesembrinus emeus* (21), *Panderevela* (21), *Viana regina* (21), *Choanopomops largillierti* (20), *Dulcerana cubaniana* (20), *Ligia simoni* (20), *Phyllamphion gundlachi* (20), *Cepolella definita* (19), *Dercitus luteus* (19), *Euconulus fulvus* (19), *Halotudora kuesteri* (19), *Hyrtios caracasensis* (19), *Lamelliconcha circinata* (19), *Praticolella griseola* (19), *Echinolittorina jamaicensis* (18), *Forcepia colonensis* (18), *Macroceramus signatus* (18), *Mesembrinus vincentinus* (18), *Neocyclotus rugatus* (18), *Omalonyx unguis* (18), *Pseudoceros bicolor* (18), *Teleophrys ruber* (18), *Thuridilla malaquita* (18), *Cochlicella barbara* (17), *Dragmacidon lunaecharta* (17), *Hydrozoanthus antumbrosus* (17), *Palaemonella americana* (17), *Pleurodonte incerta* (17), *Polybranchia schmekelae* (17), *Polymita venusta* (17), *Antillogorgia americana* (16), *Helicina convexa* (16), *Helicina phasianella* (16), *Lucidella vinosa* (16), *Metopaulias depressus* (16), *Pellicula depressa* (16), *Pleurodonte josephinae* (16), *Polygyra plana* (16), *Porcellio lamellatus* (16), *Procambarus fallax* (16), *Prosuberites carriebowensis* (16), *Amphibulima patula* (15), *Antidrymaeus stramineus* (15), *Antillipecten antillarum* (15), *Haplosyllis gula* (15), *Laevicaulis alte* (15), *Melibe arianeae* (15), *Pleurodonte parilis* (15), *Taenioraphe leucorhaphe* (15), *Antidrymaeus multifasciatus* (14), *Cerberilla potiguara* (14), *Clathrolucina costata* (14), *Lithopoma brevispina* (14), *Phrontis alba* (14), *Plekocheilus aurissileni* (14), *Rhodonyx rubescens* (14), *Voluta bonay* (14), *Zophos concolor* (14), *Antillogorgia bipinnata* (13), *Cepolis squamosa* (13), *Diplopoma crenulatum* (13), *Diplopoma decussatum* (13), *Doto fluctifraga* (13), *Helicina viridis* (13), *Hoplometopus antillensis* (13), *Limicolaria aurora* (13), *Palaemon paludosus* (13), *Rudmania grahami* (13), *Spinoaglaja petra* (13), *Unomia stolonifera* (13), *Agathistoma lividomaculatum* (12), *Americardia guppyi* (12), *Aperostoma translucidum* (12), *Armases roberti* (12), *Atya innocous* (12), *Brachypodella riisei* (12), *Crella brasiliensis* (12), *Dentellaria sloaneana* (12), *Filellum bouvetensis* (12), *Helicina rhodostoma* (12), *Isostichopus maculatus* (12), *Jasypitar fulminatus* (12), *Marsupina bufo* (12), *Pleurodonte discolor* (12), *Pyura torpida* (12), *Streptartemon glaber* (12), *Venezillo culebrae* (12), *Xestospongia caminata* (12), *Fulguropsis spirata* (11), *Halotudora aripensis* (11), *Levicepolis nemoralina* (11), *Notaulax nudicollis* (11), *Typhlatya pearsei* (11), *Anilocra brillae* (10), *Bulimulus unicolor* (10), *Coloniconcha prima* (10), *Conasprella bermudensis* (10), *Deroceras laeve* (10), *Discosoma neglecta* (10), *Felimare alaini* (10), *Hispaniolana dominicensis* (10), *Neoernsta rocasensis* (10), *Oxynoe ilani* (10), *Stenoniscus nestori* (10), *Zachrysia guanensis* (10), *Acanthochitona lata* (9), *Aegires corrugatus* (9), *Axinella digitiformis* (9), *Clathrina lutea* (9), *Mesembrinus sallei* (9), *Microceramus concisus* (9), *Plakortis symbiotica* (9), *Pusia dermestina* (9), *Veronicella tenax* (9), *Zachrysia auricoma* (9), *Bergia catenularis* (8), *Brachypodella portoricensis* (8), *Brachypodella speluncae* (8), *Clathria bulbotoxa* (8), *Clibanarius symmetricus* (8), *Forcepia trilabis* (8), *Helicina foveata* (8), *Iridonida pusilla* (8), *Lacteoluna selenina* (8), *Lucerna mora* (8), *Mcleania darlingtoni* (8), *Mesembrinus aureolus* (8), *Minuca vocator* (8), *Notocomplana ferruginea* (8), *Parmarion martensi* (8), *Patera appressa* (8), *Potamocarcinus roatensis* (8), *Pseudopapyridea semisulcata* (8), *Sinanodonta pacifica* (8), *Achelous anceps* (7), *Antillogorgia acerosa* (7), *Austromacoma constricta* (7), *Bulimulus lherminieri* (7), *Carminodoris hansrosaorum* (7), *Cerion pannosum* (7), *Daedalochila uvulifera* (7), *Doto cangas* (7), *Echinaster paucispinus* (7), *Glyphepithema floridana* (7), *Laevaricella glabra* (7), *Leptuca speciosa* (7), *Leukoma pectorina* (7), *Moreiradromia antillensis* (7), *Odontodactylus havanensis* (7), *Oscarella minka* (7), *Plagioptycha musicola* (7), *Pleurehdera nebula* (7), *Polymita versicolor* (7), *Reductoniscus costulatus* (7), *Succinea bermudensis* (7), *Telmatactis vernonia* (7), *Teralatirus festivus* (7), *Typhlatya mitchelli* (7), *Angustassiminea succinea* (6), *Armadilloniscus luisi* (6), *Aspiculortis garifuna* (6), *Cepolis boriquenae* (6), *Ctenorillo tuberosus* (6), *Delphinonaias largillierti* (6), *Diplopoma candeanum* (6), *Drymaeus serperastrum* (6), *Epilobocera wetherbeei* (6), *Guppya gundlachii* (6), *Isocheles sawayai* (6), *Labyrinthus otis* (6), *Lucerna lamarckii* (6), *Mesembrinus broadwayi* (6), *Mesochaetopterus stinapa* (6), *Naticarius cayennensis* (6), *Pegophysema schrammi* (6), *Plakina nathaliae* (6), *Pleurodonte pachygastra* (6), *Tudora rupis* (6), *Venezillo clausus* (6), *Venezillo pisum* (6), *Zophos alticola* (6), *Acanthoniscus richardsonae* (5), *Aplysia ghanimii* (5), *Averellia coactiliata* (5), *Belocaulus angustipes* (5), *Brachypodella dubia* (5), *Brachypodella subtilis* (5), *Cerion watlingense* (5), *Chondropoma schaliei* (5), *Decoradrillia pulchella* (5), *Dentimargo eburneola* (5), *Epilobocera cubensis* (5), *Euglandina ghiesbreghti* (5), *Helicina flavida* (5), *Helicina oweniana* (5), *Helicina umbonata* (5), *Laevaricella interrupta* (5), *Mastoniaeforis turristhomae* (5), *Mayaweckelia cenoticola* (5), *Monoplex krebsii* (5), *Parhippolyte antiguensis* (5), *Pomacea diffusa* (5), *Pseudobiceros caribbensis* (5), *Rudmania fentoni* (5), *Stenogyra terebraster* (5), *Stramonita brasiliensis* (5), *Succinea floridana* (5), *Tamayoa decolorata* (5), *Trichodiscina hinkleyi* (5), *Tudorisca rosenbergiana* (5), *Vagavarix portoricensis* (5), *Areopaguristes hummi* (4), *Atlantilux puella* (4), *Autocoptis argpihrix* (4), *Brachypodella trinitaria* (4), *Caracolus carinatus* (4), *Cerion casablancae* (4), *Chrysaora chesapeakei* (4), *Cochlodinella poeyana* (4), *Conus maya* (4), *Doris acerico* (4), *Elumoides* (4), *Ercolania selva* (4), *Hermaea cubana* (4), *Hispaniolana obliterata* (4), *Jeanneretia bicincta* (4), *Limacus flavus* (4), *Lucerna lucerna* (4), *Lygdamis wirtzi* (4), *Nanuca alboviridis* (4), *Parachondria lineolata* (4), *Parachondria trachyderma* (4), *Pleurodonte dentiens* (4), *Pseudobalea dominicensis* (4), *Pusia histrio* (4), *Sagittalia pulcherrima* (4), *Stygiomysis cokei* (4), *Tayloria kibweziensis* (4), *Trichodactylus quinquedentatus* (4), *Typhlopseudothelphusa acanthochela* (4), *Utterbackiana couperiana* (4), *Venezillo ramsdeni* (4), *Vokesula limatula* (4), *Abbottella moreletiana* (3), *Achelous forceps* (3), *Agathistoma hotessierianum* (3), *Alcadia hjalmarsoni* (3), *Allopeas micra* (3), *Amphicyclotulus beauianus* (3), *Anthopleura pallida* (3), *Antillogorgia rigida* (3), *Arenabbottella urbana* (3), *Armatoplana divae* (3), *Caracolus insititia* (3), *Carminodoris madibenthos* (3), *Cerion pillsburyi* (3), *Chioneryx grus* (3), *Chondropoma pictum* (3), *Coelotrochus viridis* (3), *Copidaster cavernicola* (3), *Costasiella arenaria* (3), *Costasiella patricki* (3), *Cubaris flavobrunnea* (3), *Dentellaria peracutissima* (3), *Dentellaria perplexa* (3), *Deroceras reticulatum* (3), *Dryptus moritzianus* (3), *Dulcerana granularis* (3), *Elysia corinneae* (3), *Elysia orientalis* (3), *Emoda sagraiana* (3), *Epilobocera gilmanii* (3), *Euglandina fosteri* (3), *Eulimnadia cylindrova* (3), *Felimare fortunensis* (3), *Gibberula dosmosquises* (3), *Haliclona plakophila* (3), *Helicina adspersa* (3), *Helicina rostrata* (3), *Hemitrochus graminicola* (3), *Hyalella cenotensis* (3), *Hyalella maya* (3), *Hyalella wakulla* (3), *Hydra viridissima* (3), *Idioplana atlantica* (3), *Lepidochitona pseudoliozonis* (3), *Leptarionta trigonostoma* (3), *Lucerna chemnitziana* (3), *Lucidella caldwelli* (3), *Lysmata jundalini* (3), *Macrobrachium lucifugum* (3), *Macroceramus parallelus* (3), *Melaniella gracillima* (3), *Mellita tenuis* (3), *Mieniplotia scabra* (3), *Myrianida pachycera* (3), *Neopupina curta* (3), *Niphates arenata* (3), *Oithona* (3), *Olivella esther* (3), *Petricolaria serrata* (3), *Plakinastrella microspiculifera* (3), *Poecilozonites circumfirmatus* (3), *Polygyra septemvolva* (3), *Polymita brocheri* (3), *Proceraea janetae* (3), *Psammotella cruenta* (3), *Sertularella speciosa* (3), *Stenogyra salleanus* (3), *Strengeriana taironae* (3), *Streptostyla* (3), *Succinea campestris* (3), *Triops longicaudatus* (3), *Venezillo pearsei* (3), *Venezillo venustus* (3), *Voluta caquetio* (3), *Volvarina beyerleana* (3), *Zachrysia bayamensis* (3), *Zachrysia trinitaria* (3), *Zoanthus solanderi* (3), *Alcadia aurantia* (2), *Alcadia schrammi* (2), *Amphiatlantica sulensoni* (2), *Amphicyclotus* (2), *Anodontites leotaudi* (2), *Antidrymaeus immaculatus* (2), *Archierato maugeriae* (2), *Arenabbottella sosuaensis* (2), *Bivetopsia rugosa* (2), *Boninia antillarum* (2), *Brachypodella dominicensis* (2), *Brachypodella pallida* (2), *Cerion glans* (2), *Cerion martinianum* (2), *Cerithideopsis costata* (2), *Chatziplana grubei* (2), *Chondropomella magnifica* (2), *Circulus angulatus* (2), *Clypeaster luetkeni* (2), *Colobostylus albus* (2), *Colobostylus bronnii* (2), *Conasprella allamandi* (2), *Conus alainallaryi* (2), *Conus guanahacabibensis* (2), *Conus tranthami* (2), *Cuboleacina solidula* (2), *Darwinella muelleri* (2), *Dentellaria valida* (2), *Diplopoma rigidulum* (2), *Distorsio mcgintyi* (2), *Enchiridium periommatum* (2), *Epilobocera gertraudae* (2), *Euthyonidiella occidentalis* (2), *Eutrochatella costata* (2), *Gastrocopta pellucida* (2), *Gastrocopta servilis* (2), *Glyptemoda torrei* (2), *Helicina funcki* (2), *Helicina gabbi* (2), *Helicina neritella* (2), *Hemisinus lineolatus* (2), *Hemitrochus constatior* (2), *Hemitrochus riveroi* (2), *Hojeda inaguensis* (2), *Hypolobocera bouvieri* (2), *Hysteroconcha lupanaria* (2), *Labyrinthus uncigerus* (2), *Leidyula portoricensis* (2), *Leptotrichus panzerii* (2), *Lucidella ignicoma* (2), *Lucidella striatula* (2), *Marsenia perspicua* (2), *Mastigias* (2), *Microceramus bonairensis* (2), *Microceramus guanicanus* (2), *Microthelphusa odaelkae* (2), *Milax gagates* (2), *Neopupina hjalmarsoni* (2), *Neoterebra glossema* (2), *Nephronaias ravistella* (2), *Notobryon caribbaeum* (2), *Notopygos caribea* (2), *Octomarginula ostheimerae* (2), *Olea hensoni* (2), *Opisthosiphon simpsoni* (2), *Pachychilus lacustris* (2), *Pallifera fosteri* (2), *Parachondria blauneri* (2), *Parachondria columna* (2), *Phrontis polygonata* (2), *Phyllognathopus* (2), *Plekocheilus aurissciuri* (2), *Pleurodonte guadeloupensis* (2), *Pleurodonte hippocastanum* (2), *Pleurodonte lychnuchus* (2), *Plexaurella rastrera* (2), *Procambarus niveus* (2), *Procambarus pilosimanus* (2), *Proserpina depressa* (2), *Pseudarmadillo vansicklei* (2), *Pseudoceros bolool* (2), *Pupoides modicus* (2), *Pyrgodomus microdinus* (2), *Rectoleacina cubaniana* (2), *Septa occidentalis* (2), *Simpulopsis corrugata* (2), *Succinea guatemalensis* (2), *Talitroides alluaudi* (2), *Tellinella mexicana* (2), *Thelidomus cognata* (2), *Thysanozoon raphaeli* (2), *Trochomodulus carchedonius* (2), *Tulumella unidens* (2), *Typhlatya dzilamensis* (2), *Varicella burringtonbakeri* (2), *Varicella leucozonias* (2), *Venezillo booneae* (2), *Vertigo bermudensis* (2), *Xenopoma aguayoi* (2), *Alanbeuella corrugata* (1), *Alcadia hollandi* (1), *Alcadia nitida* (1), *Alcadia spectabilis* (1), *Allopeas clavulinum* (1), *Alpheus richardsoni* (1), *Ambigolimax valentianus* (1), *Americardia columbella* (1), *Ameritella versicolor* (1), *Amphiatlantica marcuzzi* (1), *Amphibulima pardalina* (1), *Amphicyclotulus amethystinus* (1), *Amphicyclotulus martinicensis* (1), *Amphicyclotulus rufescens* (1), *Amphithrax hemphilli* (1), *Anamathia hystrix* (1), *Annularia fimbriatula* (1), *Annularia lincina* (1), *Anodontites tortilis* (1), *Anoma levis* (1), *Antidrymaeus inusitatus* (1), *Antidrymaeus pinchoti* (1), *Apoma chemnitzianum* (1), *Arenabbottella rosaliae* (1), *Armadillidium nasatum* (1), *Armases angustipes* (1), *Atlantilux albocincta* (1), *Atlantilux sykesi* (1), *Babelomurex scalariformis* (1), *Bathynomus yucatanensis* (1), *Brachypodella costata* (1), *Buchnerillo neotropicalis* (1), *Bulimulus dysoni* (1), *Bulimulus fraterculus* (1), *Bulimulus tenuissimus* (1), *Busycoarctum coarctatum* (1), *Canthocamptinae* (1), *Caracolus lowei* (1), *Caribodillo martinicensis* (1), *Caviturritella leucostoma* (1), *Cepaea nemoralis* (1), *Cepolis chocolata* (1), *Cerion nana* (1), *Chaceus guajiraensis* (1), *Cheilea americana* (1), *Chloeia amphora* (1), *Chondropoma rufilabre* (1), *Chondropometes vignalense* (1), *Chondropomium sardonyx* (1), *Chondropomium weinlandi* (1), *Chondrothyra pudica* (1), *Clathrina aphrodita* (1), *Clydonopoma pumilum* (1), *Clypeolum latissimum* (1), *Coelocentrum fistulare* (1), *Coenobita compressus* (1), *Colobostylus humphreysianus* (1), *Conasprella arawak* (1), *Conasprella verrucosa* (1), *Conasprella wendrosi* (1), *Conus belizeanus* (1), *Conus colombi* (1), *Corbicula largillierti* (1), *Crocidopoma orbellum* (1), *Cuzcodinella oryx* (1), *Cyclestheria hislopi* (1), *Cysticopsis pemphigodes* (1), *Dendrodoris karukeraensis* (1), *Dentellaria bronni* (1), *Dentellaria obesa* (1), *Deroceras invadens* (1), *Diploexochus echinatus* (1), *Diplopoma aguadillense* (1), *Diplopoma sulculosum* (1), *Drepanotrema surinamense* (1), *Dryptus marmoratus* (1), *Echinaster guyanensis* (1), *Edenttellina caribbea* (1), *Endoxocrinus parrae* (1), *Epialtus elongatus* (1), *Euglandina cylindracea* (1), *Euglandina striata* (1), *Eunice* (1), *Eutrochatella nobilis* (1), *Eutrochatella tankervillii* (1), *Excorallana antillensis* (1), *Farcimen guanense* (1), *Felimare samueli* (1), *Ferrissia californica* (1), *Fulguropsis plagosa* (1), *Gastrocopta rupicola* (1), *Geodia tylastra* (1), *Glyptograpsus jamaicensis* (1), *Goniodoridella picoensis* (1), *Gyraxis sericata* (1), *Gyroscala rupicola* (1), *Halotudora gruneri* (1), *Harpacticus* (1), *Helicina antillarum* (1), *Helicina gemma* (1), *Helicina prasinata* (1), *Hemiliostraca auricincta* (1), *Hemitrochus gallopavonis* (1), *Hemitrochus hendersoni* (1), *Hesione praetexta* (1), *Hispaniolana angustata* (1), *Hojeda boothiana* (1), *Insularorchestia monodi* (1), *Ischioscia variegata* (1), *Isoaulactinia hespervolita* (1), *Janolus costacubensis* (1), *Jeanneretia parraiana* (1), *Jorunna davidbowieii* (1), *Kankelibranchus alhenae* (1), *Latirus* (1), *Leidyula trichroma* (1), *Lepidopa dexterae* (1), *Leptuca cumulanta* (1), *Leptuca panacea* (1), *Leucozonia cerata* (1), *Leukoma grata* (1), *Levicepolis dermatina* (1), *Lipkemenes lanipes* (1), *Lissembryon dilatatus* (1), *Lucerna bainbridgii* (1), *Lucidella lirata* (1), *Luidia lawrencei* (1), *Marevalvata tricarinata* (1), *Megalomastoma antillarum* (1), *Megalomastoma verruculosum* (1), *Melanella amblytera* (1), *Mesembrinus binominis* (1), *Microeuraphia rhizophorae* (1), *Microprosthema dimitrisorum* (1), *Minuca mordax* (1), *Minyorhyncha crassa* (1), *Modulus honkerorum* (1), *Monoplex tranquebaricus* (1), *Mycetopoda siliquosa* (1), *Mytella strigata* (1), *Nenisca bartschi* (1), *Neosubulina harterti* (1), *Neoterebra concava* (1), *Neoterebra protexta* (1), *Neoterebra vinosa* (1), *Novodinia antillensis* (1), *Octopus taganga* (1), *Oleacina cyanozoaria* (1), *Oleacina subulata* (1), *Opalia moerchiana* (1), *Oudardia iris* (1), *Pachychilus glaphyrus* (1), *Pachychilus indiorum* (1), *Pachychilus largillierti* (1), *Palaemon pandaliformis* (1), *Pallifera dorsalis* (1), *Parachondria gnota* (1), *Parachondria graminosa* (1), *Parachondria maritima* (1), *Parachondria santacruzensis* (1), *Parhippolyte sterreri* (1), *Paroctopus mercatoris* (1), *Petromica ciocalyptoides* (1), *Pfeiffericoptis sinistra* (1), *Phaenocelis peleca* (1), *Phylliroe lichtensteinii* (1), *Plagioptycha strumosa* (1), *Plakina cyanorosea* (1), *Planorbarius corneus* (1), *Plekocheilus argenteus* (1), *Plekocheilus aulacostylus* (1), *Plekocheilus distortus* (1), *Plekocheilus euryomphalus* (1), *Plekocheilus quadricolor* (1), *Plekocheilus sinuatus* (1), *Polymita sulphurosa* (1), *Pomacea cumingii* (1), *Potamocarcinus hartmanni* (1), *Potamocarcinus lobulatus* (1), *Potamocarcinus richmondi* (1), *Procambarus cubensis* (1), *Procaris mexicana* (1), *Prosthiostomum utarum* (1), *Protiaropsis anonyma* (1), *Protoglyptus luciae* (1), *Prunum succineum* (1), *Pseudarmadillo bidentatus* (1), *Pseudarmadillo maiteae* (1), *Pseudobiceros splendidus* (1), *Pseudomadrepora carolina* (1), *Pseudopusula antillarum* (1), *Ptychopatula dioscoricola* (1), *Pupisoma macneilli* (1), *Pusia epiphanea* (1), *Pusia exigua* (1), *Pusia monilifera* (1), *Pusia variata* (1), *Pylopaguridium markhami* (1), *Racekiela andina* (1), *Raillietiella orientalis* (1), *Retusa* (1), *Rhizophysa eysenhardtii* (1), *Rolleia oberi* (1), *Saccella acuta* (1), *Sagda grandis* (1), *Sagittalia catenata* (1), *Scolanthus curacaoensis* (1), *Serratina aequistriata* (1), *Sesarma bidentatum* (1), *Sesarma cookei* (1), *Sheldonella bisulcata* (1), *Sinistrofulgur perversum* (1), *Speleonectes gironensis* (1), *Sphaerium incurvum* (1), *Spinoaglaja aeci* (1), *Spongia anclotea* (1), *Streptartemon deformis* (1), *Strophina laterradii* (1), *Stylochoplana sisalensis* (1), *Succinea approximans* (1), *Succinea unicolor* (1), *Sylviocarcinus piriformis* (1), *Synarmadillo ruthveni* (1), *Tampaella mera* (1), *Teinostoma brankovitsi* (1), *Teralatirus roboreus* (1), *Tetrentodon philippianus* (1), *Tomostele musaecola* (1), *Trichorhina biocellata* (1), *Trochomodulus calusa* (1), *Tudora fossor* (1), *Tuluweckelia cernua* (1), *Turbo sazae* (1), *Turritella attenuata* (1), *Ustronia acuminata* (1), *Venezillo brevispinis* (1), *Venezillo grenadensis* (1), *Venezillo soyatlanensis* (1), *Ventrilia tenera* (1), *Vermetus irregularis* (1), *Vitta clenchi* (1), *Vitta meleagris* (1), *Volvidens tichostoma* (1), *Yagerocaris cozumel* (1), *Zachrysia microstoma* (1), *Zancleopsis cabela* (1), *Zophos baudoni* (1)

</details>

## Nicht aufgelöste Namen der Reihenfolge-Quelle

Die Referenz-DB der App kennt diese Namen nicht; die App fände sie auch nicht.

| Name | iNat |
|---|---|
| *Parachromis multifasciatus* | 21 |
| *Saxatilia frenata* | 20 |
| *Micropterus nigricans* | 16 |
| *Hiatirhaphis cascajalensis* | 13 |
| *Saxatilia saxatilis* | 11 |
| *Eretmobrycon scleroparius* | 7 |
| *Poecilia zonata* | 5 |
| *Acyrtus nudus* | 4 |
| *Eretmobrycon emperador* | 4 |
| *Brevidens striatus* | 3 |
| *Poecilia dominicensis* | 3 |
| *Cynodonichthys pivijay* | 2 |
| *Lophiosilurus apurensis* | 2 |
| *Arapaima* | 1 |
| *Hiatirhaphis parismina* | 1 |
| *Lasiancistrus wiwa* | 1 |
| *Octopus taganga* | 1 |
| *Paroctopus mercatoris* | 1 |
| *Pimelodus yuma* | 1 |
| *Saxatilia alta* | 1 |
| *Squatina* | 1 |
