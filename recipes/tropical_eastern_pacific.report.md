# Bericht: Tropischer Ostpazifik (`recipes/tropical_eastern_pacific.json`)

Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.

- Referenz-DB: v3 (FishBase v26.06, SeaLifeBase v26.06)
- Salz/Süß: FishBase/SeaLifeBase v25.04 (species.parquet)
- iNaturalist: 978 Taxa (Seiten: 2)
- OBIS: 2028 Arten mit Nachweisen außer iNaturalist
- Bild: https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Bogenstirn-Hammerhaie_Sphyrna_lewini_Schule_in_Galapagos.jpg/330px-Bogenstirn-Hammerhaie_Sphyrna_lewini_Schule_in_Galapagos.jpg — kdaniel20816, CC0 1.0, https://commons.wikimedia.org/wiki/File:Bogenstirn-Hammerhaie_Sphyrna_lewini_Schule_in_Galapagos.jpg

## Gebiete

- iNaturalist: Galápagos, EC (12990), Reserva Marina Galápagos, GA, EC (141232), Isla del Coco (Cocos Island), PU, CR (68646), Malpelo, VC, CO (162711), Archipiélago de Revillagigedo (Revillagigedo Islands) (55202), Baja California Sur, MX (7403), Sonora, MX (6794), Sinaloa, MX (7187), Guanacaste, CR (12774), Puntarenas, CR (8579), Chiriquí, PA (13152), Veraguas, PA (13158), Los Santos, PA (11526), Herrera, PA (11524), Coclé, PA (11522), Panamá, PA (13157), Panamá Oeste, PA (97127), Darién, PA (13154)
- OBIS: Galápagos, Isla del Coco, Malpelo, Revillagigedo-Inseln, Golf von Kalifornien und Pazifikküste von Baja California Sur, Pazifikküste von Costa Rica und Panama, ohne Karibikküste
- FishBase/SeaLifeBase-Verbreitung: 218A, I188

## Übersicht

- Arten der Reihenfolge-Quelle, aufgelöst: 962; nicht aufgelöst: 10
- ausgeschlossen: 513
  - zu wenige Nachweise: 319
  - kein Meeresfisch: 173
  - zu klein: 11
  - nur tiefer als die Tauchgrenze: 10
- Kandidaten nach den Filtern: 449
- Deck: 159 Arten (Level 1: 49, Level 2: 60, Level 3: 50); Umfang laut Rezept 40/60/50 plus Highlights
- Highlights: 9 im Deck, 0 verworfen

## Zu entscheiden

Hinweise, keine Ausschlüsse: Jede Zeile wird im Rezept entschieden (`exclude` mit Grund, Namenszuordnung, Level) oder bewusst belassen. Schwellen: `warnings` im Rezept.

| Art | Subdeck | Warnung | Zahlen |
|---|---|---|---|
| *Diodon hystrix* | level-1 | tot beobachtet | 41 von 49 Beobachtungen mit Angabe lebend/tot tot (84 %) |
| *Strombus gracilior* | invertebrates | tot beobachtet | 7 von 8 Beobachtungen mit Angabe lebend/tot tot (88 %) |
| *Chama coralloides* | invertebrates | tot beobachtet | 11 von 12 Beobachtungen mit Angabe lebend/tot tot (92 %) |
| *Neoniphon suborbitalis* | level-2 | Name der Region | Deck: *Neoniphon suborbitalis*; die Referenz-DB führt die Art als *Sargocentron suborbitale* |
| *Eucidaris galapagensis* | invertebrates | Name der Region | Deck: *Eucidaris galapagensis*; die Referenz-DB führt die Art als *Eucidaris thouarsii* |
| *Physalia utriculus* | invertebrates | Name der Region | Deck: *Physalia utriculus*; die Referenz-DB führt die Art als *Physalia physalis* |
| *Acanthaster ellisii* | invertebrates | Name der Region | Deck: *Acanthaster ellisii*; die Referenz-DB führt die Art als *Acanthaster planci* |
| *Phyllonotus erythrostomus* | invertebrates | Name der Region | Deck: *Phyllonotus erythrostomus*; die Referenz-DB führt die Art als *Hexaplex erythrostomus* |
| *Chama coralloides* | invertebrates | Name der Region | Deck: *Chama coralloides*; die Referenz-DB führt die Art als *Chama echinata* |
| *Mola mola* | level-1 | wenige Beobachter | 2 von 4 Beobachtungen von 2 Personen (50 %); 4 Beobachter insgesamt |
| *Holacanthus clarionensis* | level-2 | wenige Beobachter | 189 von 274 Beobachtungen von 2 Personen (69 %); 59 Beobachter insgesamt |
| *Lepidonectes corallicola* | level-2 | wenige Beobachter | 155 von 215 Beobachtungen von 2 Personen (72 %); 41 Beobachter insgesamt |
| *Caranx sexfasciatus* | level-2 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Mugil cephalus* | level-2 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Carcharhinus leucas* | level-2 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Dajaus monticola* | level-3 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Dormitator latifrons* | level-3 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |

## Verworfene Highlights

Keine.

## iNaturalist-Namen zugeordnet

Laut `recipes/inat_names.json`: iNaturalist nennt die Art anders als die Referenz-DB; die Zählung kommt zu der der Referenz-DB-Art.

| iNaturalist | Referenz-DB | iNat | Art | Beleg |
|---|---|---|---|---|
| *Haemulopsis elongata* | *Haemulopsis elongatus* | 12 | Umbenennung | https://www.inaturalist.org/taxon_changes/119848 |

## Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Sphyrna lewini* | Schulen von Bogenstirn-Hammerhaien stehen an den Felsen von Kokosinsel, Malpelo und Darwin. | 44 | Reihenfolge-Quelle, OBIS, Verbreitung, Führer | Level 1 |
| *Rhincodon typus* | Der Walhai zieht an Darwin Island vorbei und sammelt sich in der Bahía de La Paz. | 66 | Reihenfolge-Quelle, OBIS, Verbreitung, Führer | Level 1 |
| *Mobula birostris* | Riesenmantas suchen bei San Benedicto und Socorro die Nähe von Tauchern. | 64 | Reihenfolge-Quelle, OBIS, Verbreitung, Führer | Level 1 |
| *Carcharhinus galapagensis* | Der Galápagoshai ist der typische Hai der ozeanischen Inseln des Ostpazifiks. | 74 | Reihenfolge-Quelle, OBIS, Verbreitung, Führer | Level 1 |
| *Mobula munkiana* | Munks Teufelsrochen springen im Golf von Kalifornien in riesigen Schwärmen aus dem Wasser. | 88 | Reihenfolge-Quelle, OBIS, Verbreitung, Führer | Level 1 |
| *Mola mola* | Der Mondfisch lässt sich an den kalten Auftriebsstellen westlich von Isabela putzen. | – | Reihenfolge-Quelle, OBIS, Verbreitung, Führer | Level 1 |
| *Odontaspis ferox* | Der Kleinzahn-Sandtigerhai ist an kaum einem Ort so verlässlich zu sehen wie in Malpelo. | – | OBIS, Verbreitung, Führer | Level 1 |
| *Amblyrhynchus cristatus* | Die Meerechse, einzige Echse, die im Meer frisst, weidet vor Galápagos Algen unter Wasser. | – | Verbreitung | Level 1 |
| *Zalophus wollebaeki* | Der Galápagos-Seelöwe spielt mit Schnorchlern und Tauchern. | – | Verbreitung | Level 1 |

## Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS ohne iNaturalist oder Verbreitung): 154/159 (97 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 7: *Amblyrhynchus cristatus*, *Brachygenys jessiae*, *Gobioclinus dendriticus*, *Apogon atradorsatus*, *Lepidonectes corallicola*, *Girella freminvillii*, *Archosargus pourtalesii*
- Arten ohne Volksnamen `de` in der Referenz-DB: 115/159 (72 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 6/159 (4 %)
- Familien ohne Volksnamen `de`: 10/58 (17 %): *Aetobatidae*, *Cheloniidae*, *Epinephelidae*, *Girellidae*, *Iguanidae*, *Mobulidae*, *Octopodidae*, *Otariidae*, *Rhinopteridae*, *Urotrygonidae*
- Familien ohne Volksnamen `en`: 2/58 (3 %): *Iguanidae*, *Otariidae*

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

- *Aetobatus ocellatus*: Reihenfolge-Quelle, Führer
- *Odontaspis ferox*: OBIS, Verbreitung, Führer
- *Amblyrhynchus cristatus*: Verbreitung
- *Zalophus wollebaeki*: Verbreitung
- *Urobatis pardalis*: Reihenfolge-Quelle, Führer

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

- gleicher Volksname `de` „krake“: *Octopus oculifer*, *Octopus hubbsorum*
- gleicher Volksname `de` „Schnapper“: *Lutjanus argentiventris*, *Lutjanus novemfasciatus*, *Lutjanus guttatus*, *Lutjanus colorado*

## Deck

Spalten: Rang unter den Kandidaten, Zählung der Reihenfolge-Quelle (iNat), OBIS-Nachweise ohne den iNaturalist-Datensatz, Einträge der FishBase/SeaLifeBase-Verbreitung in den Rezept-Regionen (~~durchgestrichen~~: Eintrag sagt „nicht vorhanden“), Wasser laut FishBase/SeaLifeBase, Nummer des Führers, der die Art listet.

### Level 1 (49)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer |
|---|---|---|---|---|---|---|
| 1 | *Chelonia mydas* (1818 Beobachter) | 4242 | 2248 | native ×1 | Meer | – |
| 2 | *Abudefduf troschelii* (1160 Beobachter) | 2559 | 921 | native ×2 | Meer | 1 |
| 3 | *Holacanthus passer* (1020 Beobachter) | 2507 | 2745 | native ×2 | Meer | 1 |
| 4 | *Prionurus laticlavius* (985 Beobachter) | 2454 | 122 | native ×2 | Meer | 1 |
| 5 | *Bodianus diplotaenia* (712 Beobachter) | 2419 | 2846 | native ×2 | Meer | 1 |
| 6 | *Thalassoma lucasanum* (848 Beobachter) | 2376 | 2668 | native ×2 | Meer | 1 |
| 7 | *Arothron meleagris* (1007 Beobachter) | 2315 | 1053 | native ×1 | Meer | 1 |
| 8 | *Diodon holocanthus* (1146 Beobachter) | 1999 | 527 | native ×1 | Meer | 1 |
| 9 | *Triaenodon obesus* (893 Beobachter) | 1999 | 813 | native ×2 | Meer | 1 |
| 10 | *Scarus ghobban* (640 Beobachter) | 1954 | 1654 | native ×1 | Brack/Meer | 1 |
| 11 | *Lepidochelys olivacea* (1148 Beobachter) | 1555 | 559 | native ×1 | Meer | – |
| 12 | *Ophioblennius steindachneri* (563 Beobachter) | 1289 | 2162 | native ×1 | Meer | 1 |
| 13 | *Microspathodon dorsalis* (550 Beobachter) | 1281 | 763 | native ×2 | Meer | 1 |
| 14 | *Sphoeroides annulatus* (721 Beobachter) | 1240 | 908 | native ×1 | Brack/Meer | 1 |
| 15 | *Johnrandallia nigrirostris* (468 Beobachter) | 1109 | 2089 | native ×2 | Meer | 1 |
| 16 | *Epinephelus labriformis* (475 Beobachter) | 1067 | 2802 | native ×1 | Meer | 1 |
| 17 | *Cephalopholis colonus* (363 Beobachter) | 1034 | 1279 | native ×2 | Meer | 1 |
| 18 | *Cirrhitus rivulatus* (538 Beobachter) | 1005 | 1143 | native ×1 | Meer | 1 |
| 19 | *Stegastes arcifrons* (336 Beobachter) | 994 | 1300 | native ×2 | Meer | 1 |
| 20 | *Scarus rubroviolaceus* (352 Beobachter) | 958 | 913 | native ×2 | Meer | 1 |
| 21 | *Fistularia commersonii* (444 Beobachter) | 873 | 575 | native ×1 | Meer | 1 |
| 22 | *Sufflamen verres* (384 Beobachter) | 859 | 1799 | native ×2 | Meer | 1 |
| 23 | *Balistes polylepis* (542 Beobachter) | 836 | 566 | native ×1 | Meer | 1 |
| 24 | *Carcharhinus limbatus* (537 Beobachter) | 833 | 112 | native ×1 | Brack/Meer | 1 |
| 25 | *Acanthurus xanthopterus* (401 Beobachter) | 821 | 575 | native ×1 | Meer | 1 |
| 26 | *Zanclus cornutus* (396 Beobachter) | 808 | 915 | native ×2 | Meer | 1 |
| 27 | *Lutjanus argentiventris* (396 Beobachter) | 807 | 1048 | native ×2 | Brack/Meer | 1 |
| 28 | *Cirrhitichthys oxycephalus* (296 Beobachter) | 770 | 1677 | native ×1 | Meer | 1 |
| 29 | *Stegastes beebei* (243 Beobachter) | 762 | 2133 | native ×2 | Meer | 1 |
| 30 | *Stegastes acapulcoensis* (362 Beobachter) | 757 | 107 | native ×2 | Meer | 1 |
| 31 | *Canthigaster punctatissima* (307 Beobachter) | 732 | 658 | native ×1 | Meer | 1 |
| 32 | *Eretmochelys imbricata* (418 Beobachter) | 724 | 85 | native ×1 | Brack/Meer | – |
| 33 | *Chaetodon humeralis* (356 Beobachter) | 694 | 596 | native ×1 | Meer | 1 |
| 34 | *Aetobatus ocellatus* (460 Beobachter) | 691 | – | – | Brack/Meer | 1 |
| 35 | *Halichoeres nicholsi* (241 Beobachter) | 673 | 1213 | native ×1 | Meer | 1 |
| 36 | *Lutjanus viridis* (284 Beobachter) | 663 | 1270 | native ×2 | Meer | 1 |
| 37 | *Hypanus dipterurus* (397 Beobachter) | 655 | 365 | native ×1 | Meer | 1 |
| 38 | *Diodon hystrix* (456 Beobachter) | 624 | 228 | native ×1 | Meer | 1 |
| 39 | *Azurina atrilobata* (299 Beobachter) | 599 | 1024 | native ×2 | Meer | 1 |
| 40 | *Halichoeres dispilus* (196 Beobachter) | 580 | 2139 | native ×1 | Meer | 1 |
| 44 | *Sphyrna lewini* (Highlight; 298 Beobachter) | 557 | 678 | native ×1 | Brack/Meer | 1 |
| 66 | *Rhincodon typus* (Highlight; 280 Beobachter) | 349 | 570 | native ×2 | Meer | 1 |
| 64 | *Mobula birostris* (Highlight; 183 Beobachter) | 351 | 164 | native ×2 | Meer | 1 |
| 74 | *Carcharhinus galapagensis* (Highlight; 160 Beobachter) | 323 | 334 | native ×2 | Meer | 1 |
| 88 | *Mobula munkiana* (Highlight; 166 Beobachter) | 249 | 35 | native ×1 | Meer | 1 |
| – | *Mola mola* (Highlight; 4 Beobachter) | 4 | 29 | native ×1 | Meer | 1 |
| – | *Odontaspis ferox* (Highlight) | – | 8 | native ×2 | Meer | 1 |
| – | *Amblyrhynchus cristatus* (Highlight) | – | – | endemic ×1 | Meer | – |
| – | *Zalophus wollebaeki* (Highlight) | – | – | native ×1, stray ×1 | Meer | – |

### Level 2 (60)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer |
|---|---|---|---|---|---|---|
| 41 | *Cephalopholis panamensis* (282 Beobachter) | 572 | 904 | native ×1 | Meer | 1 |
| 42 | *Mulloidichthys dentatus* (252 Beobachter) | 563 | 532 | native ×1 | Meer | 1 |
| 43 | *Scorpaena mystes* (298 Beobachter) | 563 | 742 | native ×2 | Meer | 1 |
| 45 | *Caranx sexfasciatus* (231 Beobachter) | 553 | 219 | native ×1 | Süß/Brack/Meer | 1 |
| 46 | *Arothron hispidus* (335 Beobachter) | 548 | 295 | native ×1 | Brack/Meer | 1 |
| 47 | *Muraena lentiginosa* (315 Beobachter) | 526 | 576 | native ×1 | Meer | 1 |
| 48 | *Brachygenys jessiae* (264 Beobachter) | 506 | 53 | endemic ×1 | Meer | 1 |
| 49 | *Thalassoma grammaticum* (159 Beobachter) | 503 | 292 | native ×2 | Meer | 1 |
| 50 | *Haemulon sexfasciatum* (224 Beobachter) | 499 | 148 | native ×1 | Meer | 1 |
| 51 | *Serranus psittacinus* (233 Beobachter) | 493 | 1132 | native ×1 | Meer | 1 |
| 52 | *Acanthurus nigricans* (160 Beobachter) | 492 | 443 | native ×2 | Meer | 1 |
| 53 | *Gymnothorax castaneus* (265 Beobachter) | 464 | 177 | native ×2 | Meer | 1 |
| 54 | *Gobioclinus dendriticus* (135 Beobachter) | 455 | 100 | endemic ×1 | Meer | 1 |
| 55 | *Caranx melampygus* (159 Beobachter) | 454 | 535 | native ×1 | Brack/Meer | 1 |
| 56 | *Acanthurus triostegus* (186 Beobachter) | 448 | 254 | native ×2 | Meer | 1 |
| 57 | *Stegastes flavilatus* (203 Beobachter) | 443 | 247 | native ×2 | Meer | 1 |
| 58 | *Rhinoptera steindachneri* (372 Beobachter) | 435 | 58 | native ×1 | Meer | 1 |
| 59 | *Pomacanthus zonipectus* (231 Beobachter) | 420 | 213 | native ×1 | Meer | 1 |
| 60 | *Hippocampus ingens* (310 Beobachter) | 409 | 172 | native ×2 | Meer | 1 |
| 61 | *Abudefduf concolor* (278 Beobachter) | 397 | 48 | native ×2 | Meer | 1 |
| 62 | *Bathygobius ramosus* (252 Beobachter) | 395 | 273 | – | Meer | 1 |
| 63 | *Haemulon maculicauda* (198 Beobachter) | 378 | 210 | native ×1 | Meer | 1 |
| 65 | *Ostracion meleagris* (153 Beobachter) | 350 | 152 | native ×1 | Meer | 1 |
| 67 | *Scarus perrico* (213 Beobachter) | 349 | 377 | native ×1 | Meer | 1 |
| 68 | *Pseudobalistes naufragium* (186 Beobachter) | 342 | 113 | native ×1 | Meer | 1 |
| 69 | *Apogon atradorsatus* (129 Beobachter) | 339 | 1266 | endemic ×1, native ×1 | Meer | 1 |
| 70 | *Lutjanus novemfasciatus* (226 Beobachter) | 339 | 491 | native ×1 | Brack/Meer | 1 |
| 71 | *Trachinotus rhodopus* (253 Beobachter) | 339 | 181 | native ×1 | Meer | 1 |
| 72 | *Mycteroperca rosacea* (124 Beobachter) | 337 | 137 | – | Meer | 1 |
| 73 | *Halichoeres notospilus* (139 Beobachter) | 325 | 277 | native ×1 | Meer | 1 |
| 75 | *Caranx caninus* (236 Beobachter) | 322 | 96 | native ×1 | Brack/Meer | 1 |
| 76 | *Chilomycterus reticulatus* (205 Beobachter) | 318 | 241 | native ×1 | Meer | 1 |
| 77 | *Gymnothorax dovii* (111 Beobachter) | 299 | 643 | native ×2 | Meer | 1 |
| 78 | *Hoplopagrus guentherii* (211 Beobachter) | 298 | 391 | native ×1 | Meer | 1 |
| 79 | *Myrichthys xysturus* (231 Beobachter) | 293 | 58 | native ×1 | Meer | 1 |
| 80 | *Aulostomus chinensis* (85 Beobachter) | 292 | 582 | native ×2 | Meer | 1 |
| 81 | *Bathygobius lineatus* (135 Beobachter) | 289 | 527 | native ×1 | Meer | 1 |
| 82 | *Echidna nebulosa* (164 Beobachter) | 289 | 98 | native ×1 | Meer | 1 |
| 83 | *Holacanthus clarionensis* (59 Beobachter) | 274 | 119 | – | Meer | 1 |
| 84 | *Hypanus longus* (164 Beobachter) | 271 | 68 | native ×1 | Meer | 1 |
| 85 | *Taeniurops meyeni* (166 Beobachter) | 269 | 146 | native ×2 | Meer | 1 |
| 86 | *Octopus oculifer* (141 Beobachter) | 257 | 209 | native ×1 | Meer | – |
| 87 | *Bodianus eclancheri* (111 Beobachter) | 249 | 734 | native ×1 | Meer | 1 |
| 89 | *Neoniphon suborbitalis* (129 Beobachter) | 245 | 399 | native ×2 | Meer | 1 |
| 90 | *Caranx caballus* (134 Beobachter) | 241 | 464 | native ×1 | Brack/Meer | 1 |
| 91 | *Microspathodon bairdii* (125 Beobachter) | 232 | 409 | native ×2 | Meer | 1 |
| 92 | *Dermatolepis dermatolepis* (98 Beobachter) | 231 | 1429 | native ×2 | Meer | 1 |
| 93 | *Aetobatus laticeps* (177 Beobachter) | 227 | 46 | native ×1 | Meer | 1 |
| 94 | *Mycteroperca olfax* (85 Beobachter) | 218 | 3070 | native ×2 | Meer | 1 |
| 95 | *Kyphosus elegans* (124 Beobachter) | 216 | 546 | native ×1 | Meer | 1 |
| 96 | *Lepidonectes corallicola* (41 Beobachter) | 215 | 768 | endemic ×1 | Meer | 1 |
| 97 | *Stegastes rectifraenum* (114 Beobachter) | 213 | 251 | – | Meer | 1 |
| 98 | *Mugil cephalus* (158 Beobachter) | 210 | 367 | native ×1 | Süß/Brack/Meer | 1 |
| 99 | *Alphestes immaculatus* (114 Beobachter) | 206 | 462 | native ×1 | Meer | 1 |
| 100 | *Malacoctenus sudensis* (150 Beobachter) | 205 | 44 | – | Meer | 1 |
| 101 | *Anisotremus taeniatus* (123 Beobachter) | 200 | 37 | – | Meer | 1 |
| 102 | *Haemulon scudderii* (106 Beobachter) | 195 | 388 | native ×1 | Meer | 1 |
| 103 | *Plagiotremus azaleus* (91 Beobachter) | 192 | 1566 | native ×1 | Meer | 1 |
| 104 | *Carcharhinus leucas* (62 Beobachter) | 189 | 34 | – | Süß/Brack/Meer | 1 |
| 105 | *Melichthys niger* (93 Beobachter) | 188 | 890 | native ×2 | Meer | 1 |

### Level 3 (50)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer |
|---|---|---|---|---|---|---|
| 106 | *Urobatis pardalis* | 184 | – | – | Meer | 1 |
| 107 | *Kyphosus vaigiensis* | 181 | 287 | native ×1 | Meer | 1 |
| 108 | *Anisotremus espinozai* | 179 | – | native ×2 | Meer | 1 |
| 109 | *Novaculichthys taeniourus* | 175 | 211 | native ×1 | Meer | 1 |
| 110 | *Halichoeres chierchiae* | 173 | 107 | native ×1 | Meer | 1 |
| 111 | *Urobatis maculatus* | 169 | 150 | – | Meer | 1 |
| 112 | *Myripristis leiognathus* | 168 | 410 | native ×2 | Meer | 1 |
| 113 | *Forcipiger flavissimus* | 162 | 58 | native ×1 | Meer | 1 |
| 114 | *Acanthemblemaria hancocki* | 157 | 95 | – | Meer | 1 |
| 115 | *Echidna nocturna* | 156 | 127 | native ×2 | Meer | 1 |
| 116 | *Abudefduf declivifrons* | 155 | 78 | – | Meer | 1 |
| 117 | *Dialommus macrocephalus* | 152 | 90 | – | Meer | 1 |
| 118 | *Labrisomus xanti* | 150 | 333 | – | Meer | 1 |
| 119 | *Nematistius pectoralis* | 150 | 99 | native ×1 | Meer | 1 |
| 120 | *Sphoeroides lobatus* | 148 | 129 | native ×1 | Brack/Meer | 1 |
| 121 | *Paralabrax maculatofasciatus* | 146 | 400 | – | Meer | 1 |
| 122 | *Gymnomuraena zebra* | 142 | 136 | native ×1 | Meer | 1 |
| 123 | *Scomberomorus sierra* | 140 | 514 | native ×1 | Meer | 1 |
| 124 | *Synodus lacertinus* | 140 | 382 | native ×1 | Meer | 1 |
| 125 | *Gnathanodon speciosus* | 139 | 74 | native ×1 | Meer | 1 |
| 126 | *Urobatis halleri* | 133 | 215 | – | Meer | 1 |
| 127 | *Caranx lugubris* | 132 | 224 | native ×1 | Meer | 1 |
| 128 | *Lutjanus guttatus* | 132 | 223 | native ×1 | Meer | 1 |
| 129 | *Nicholsina denticulata* | 131 | 335 | native ×1 | Meer | 1 |
| 130 | *Scarus compressus* | 131 | 360 | native ×1 | Meer | 1 |
| 131 | *Lutjanus colorado* | 130 | 91 | – | Brack/Meer | 1 |
| 132 | *Oxycirrhites typus* | 128 | 118 | native ×1 | Meer | 1 |
| 133 | *Aluterus scriptus* | 126 | 132 | native ×1 | Meer | 1 |
| 134 | *Dajaus monticola* | 123 | 100 | native ×1 | Süß/Brack/Meer | 1 |
| 135 | *Kyphosus ocyurus* | 121 | 175 | native ×1 | Meer | 1 |
| 136 | *Urobatis concentricus* | 121 | 35 | – | Meer | 1 |
| 137 | *Dormitator latifrons* | 120 | 112 | native ×1 | Süß/Brack/Meer | 1 |
| 138 | *Anisotremus interruptus* | 118 | 333 | native ×1 | Meer | 1 |
| 139 | *Ctenochaetus marginatus* | 117 | 53 | native ×1 | Meer | 1 |
| 140 | *Heterodontus quoyi* | 116 | 165 | native ×1 | Meer | 1 |
| 141 | *Euthynnus lineatus* | 115 | 274 | native ×1 | Meer | 1 |
| 142 | *Octopus hubbsorum* | 115 | 40 | – | Meer | – |
| 143 | *Gymnothorax flavimarginatus* | 114 | 44 | native ×1 | Meer | 1 |
| 144 | *Stegastes redemptus* | 114 | 71 | – | Meer | 1 |
| 145 | *Girella freminvillii* | 113 | 674 | endemic ×1 | Meer | 1 |
| 146 | *Sphyraena idiastes* | 113 | 276 | native ×2 | Meer | 1 |
| 147 | *Bothus mancus* | 112 | 51 | native ×2 | Meer | 1 |
| 148 | *Coryphopterus urospilus* | 112 | 634 | native ×1 | Meer | 1 |
| 149 | *Elops affinis* | 109 | 60 | native ×1 | Brack/Meer | 1 |
| 150 | *Gerres simillimus* | 104 | 3 | native ×1 | Brack/Meer | 1 |
| 151 | *Myripristis berndti* | 104 | 103 | native ×2 | Meer | 1 |
| 152 | *Archosargus pourtalesii* | 103 | 117 | endemic ×1 | Meer | 1 |
| 153 | *Chromis alta* | 99 | 224 | native ×2 | Meer | 1 |
| 154 | *Elacatinus puncticulatus* | 97 | 164 | – | Meer | 1 |
| 155 | *Thunnus albacares* | 97 | 87 | native ×1 | Brack/Meer | 1 |

## Grenzfälle

Je 10 Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels sie nehmen (Highlights ab Level 2 übersprungen).

### Level 1/2

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer | Level |
|---|---|---|---|---|---|---|---|
| 31 | *Canthigaster punctatissima* (307 Beobachter) | 732 | 658 | native ×1 | Meer | 1 | 1 |
| 32 | *Eretmochelys imbricata* (418 Beobachter) | 724 | 85 | native ×1 | Brack/Meer | – | 1 |
| 33 | *Chaetodon humeralis* (356 Beobachter) | 694 | 596 | native ×1 | Meer | 1 | 1 |
| 34 | *Aetobatus ocellatus* (460 Beobachter) | 691 | – | – | Brack/Meer | 1 | 1 |
| 35 | *Halichoeres nicholsi* (241 Beobachter) | 673 | 1213 | native ×1 | Meer | 1 | 1 |
| 36 | *Lutjanus viridis* (284 Beobachter) | 663 | 1270 | native ×2 | Meer | 1 | 1 |
| 37 | *Hypanus dipterurus* (397 Beobachter) | 655 | 365 | native ×1 | Meer | 1 | 1 |
| 38 | *Diodon hystrix* (456 Beobachter) | 624 | 228 | native ×1 | Meer | 1 | 1 |
| 39 | *Azurina atrilobata* (299 Beobachter) | 599 | 1024 | native ×2 | Meer | 1 | 1 |
| 40 | *Halichoeres dispilus* (196 Beobachter) | 580 | 2139 | native ×1 | Meer | 1 | 1 |
| | **Grenze** | | | | | | |
| 41 | *Cephalopholis panamensis* (282 Beobachter) | 572 | 904 | native ×1 | Meer | 1 | 2 |
| 42 | *Mulloidichthys dentatus* (252 Beobachter) | 563 | 532 | native ×1 | Meer | 1 | 2 |
| 43 | *Scorpaena mystes* (298 Beobachter) | 563 | 742 | native ×2 | Meer | 1 | 2 |
| 45 | *Caranx sexfasciatus* (231 Beobachter) | 553 | 219 | native ×1 | Süß/Brack/Meer | 1 | 2 |
| 46 | *Arothron hispidus* (335 Beobachter) | 548 | 295 | native ×1 | Brack/Meer | 1 | 2 |
| 47 | *Muraena lentiginosa* (315 Beobachter) | 526 | 576 | native ×1 | Meer | 1 | 2 |
| 48 | *Brachygenys jessiae* (264 Beobachter) | 506 | 53 | endemic ×1 | Meer | 1 | 2 |
| 49 | *Thalassoma grammaticum* (159 Beobachter) | 503 | 292 | native ×2 | Meer | 1 | 2 |
| 50 | *Haemulon sexfasciatum* (224 Beobachter) | 499 | 148 | native ×1 | Meer | 1 | 2 |
| 51 | *Serranus psittacinus* (233 Beobachter) | 493 | 1132 | native ×1 | Meer | 1 | 2 |

### Level 2/3

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer | Level |
|---|---|---|---|---|---|---|---|
| 96 | *Lepidonectes corallicola* (41 Beobachter) | 215 | 768 | endemic ×1 | Meer | 1 | 2 |
| 97 | *Stegastes rectifraenum* (114 Beobachter) | 213 | 251 | – | Meer | 1 | 2 |
| 98 | *Mugil cephalus* (158 Beobachter) | 210 | 367 | native ×1 | Süß/Brack/Meer | 1 | 2 |
| 99 | *Alphestes immaculatus* (114 Beobachter) | 206 | 462 | native ×1 | Meer | 1 | 2 |
| 100 | *Malacoctenus sudensis* (150 Beobachter) | 205 | 44 | – | Meer | 1 | 2 |
| 101 | *Anisotremus taeniatus* (123 Beobachter) | 200 | 37 | – | Meer | 1 | 2 |
| 102 | *Haemulon scudderii* (106 Beobachter) | 195 | 388 | native ×1 | Meer | 1 | 2 |
| 103 | *Plagiotremus azaleus* (91 Beobachter) | 192 | 1566 | native ×1 | Meer | 1 | 2 |
| 104 | *Carcharhinus leucas* (62 Beobachter) | 189 | 34 | – | Süß/Brack/Meer | 1 | 2 |
| 105 | *Melichthys niger* (93 Beobachter) | 188 | 890 | native ×2 | Meer | 1 | 2 |
| | **Grenze** | | | | | | |
| 106 | *Urobatis pardalis* | 184 | – | – | Meer | 1 | 3 |
| 107 | *Kyphosus vaigiensis* | 181 | 287 | native ×1 | Meer | 1 | 3 |
| 108 | *Anisotremus espinozai* | 179 | – | native ×2 | Meer | 1 | 3 |
| 109 | *Novaculichthys taeniourus* | 175 | 211 | native ×1 | Meer | 1 | 3 |
| 110 | *Halichoeres chierchiae* | 173 | 107 | native ×1 | Meer | 1 | 3 |
| 111 | *Urobatis maculatus* | 169 | 150 | – | Meer | 1 | 3 |
| 112 | *Myripristis leiognathus* | 168 | 410 | native ×2 | Meer | 1 | 3 |
| 113 | *Forcipiger flavissimus* | 162 | 58 | native ×1 | Meer | 1 | 3 |
| 114 | *Acanthemblemaria hancocki* | 157 | 95 | – | Meer | 1 | 3 |
| 115 | *Echidna nocturna* | 156 | 127 | native ×2 | Meer | 1 | 3 |

### Level 3/nicht im Deck

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer | Level |
|---|---|---|---|---|---|---|---|
| 146 | *Sphyraena idiastes* | 113 | 276 | native ×2 | Meer | 1 | 3 |
| 147 | *Bothus mancus* | 112 | 51 | native ×2 | Meer | 1 | 3 |
| 148 | *Coryphopterus urospilus* | 112 | 634 | native ×1 | Meer | 1 | 3 |
| 149 | *Elops affinis* | 109 | 60 | native ×1 | Brack/Meer | 1 | 3 |
| 150 | *Gerres simillimus* | 104 | 3 | native ×1 | Brack/Meer | 1 | 3 |
| 151 | *Myripristis berndti* | 104 | 103 | native ×2 | Meer | 1 | 3 |
| 152 | *Archosargus pourtalesii* | 103 | 117 | endemic ×1 | Meer | 1 | 3 |
| 153 | *Chromis alta* | 99 | 224 | native ×2 | Meer | 1 | 3 |
| 154 | *Elacatinus puncticulatus* | 97 | 164 | – | Meer | 1 | 3 |
| 155 | *Thunnus albacares* | 97 | 87 | native ×1 | Brack/Meer | 1 | 3 |
| | **Grenze** | | | | | | |
| 156 | *Chaetodipterus zonatus* | 94 | 142 | native ×1 | Meer | 1 | – |
| 157 | *Coryphaena hippurus* | 94 | 303 | native ×1 | Brack/Meer | 1 | – |
| 158 | *Narcine entemedor* | 94 | 81 | – | Meer | 1 | – |
| 159 | *Chanos chanos* | 90 | 396 | native ×1 | Süß/Brack/Meer | 1 | – |
| 160 | *Lythrypnus gilberti* | 89 | 606 | endemic ×1 | Meer | 1 | – |
| 161 | *Zapteryx exasperata* | 89 | 47 | – | Meer | 1 | – |
| 162 | *Sphoeroides rosenblatti* | 88 | 38 | – | Brack/Meer | 1 | – |
| 163 | *Styracura pacifica* | 88 | 4 | native ×1 | Meer | 1 | – |
| 164 | *Paralabrax albomaculatus* | 86 | 755 | endemic ×1 | Meer | 1 | – |
| 165 | *Seriola rivoliana* | 84 | 1078 | native ×1 | Meer | 1 | – |

## Abgleich mit Führern

### 1. Smithsonian: Shorefishes of the Tropical Eastern Pacific

- 1480 Namen, 1462 Arten aufgelöst, 17 Namen nicht aufgelöst
- Deck-Arten im Führer: 152/159
  - Level 1: 44/49
  - Level 2: 59/60
  - Level 3: 49/50
- Kandidaten im Führer, aber nicht im Deck: 278

**Im Deck, nicht im Führer** (Verdacht: Fehlbestimmung, falsch verortet oder Süßwasser):

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer | Level |
|---|---|---|---|---|---|---|---|
| 1 | *Chelonia mydas* (1818 Beobachter) | 4242 | 2248 | native ×1 | Meer | – | 1 |
| 11 | *Lepidochelys olivacea* (1148 Beobachter) | 1555 | 559 | native ×1 | Meer | – | 1 |
| 32 | *Eretmochelys imbricata* (418 Beobachter) | 724 | 85 | native ×1 | Brack/Meer | – | 1 |
| – | *Amblyrhynchus cristatus* (Highlight) | – | – | endemic ×1 | Meer | – | 1 |
| – | *Zalophus wollebaeki* (Highlight) | – | – | native ×1, stray ×1 | Meer | – | 1 |
| 86 | *Octopus oculifer* (141 Beobachter) | 257 | 209 | native ×1 | Meer | – | 2 |
| 142 | *Octopus hubbsorum* | 115 | 40 | – | Meer | – | 3 |

**Im Führer und häufig, aber nicht im Deck** (Kandidaten; die 30 häufigsten):

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Führer |
|---|---|---|---|---|---|---|
| 156 | *Chaetodipterus zonatus* | 94 | 142 | native ×1 | Meer | 1 |
| 157 | *Coryphaena hippurus* | 94 | 303 | native ×1 | Brack/Meer | 1 |
| 158 | *Narcine entemedor* | 94 | 81 | – | Meer | 1 |
| 159 | *Chanos chanos* | 90 | 396 | native ×1 | Süß/Brack/Meer | 1 |
| 160 | *Lythrypnus gilberti* | 89 | 606 | endemic ×1 | Meer | 1 |
| 161 | *Zapteryx exasperata* | 89 | 47 | – | Meer | 1 |
| 162 | *Sphoeroides rosenblatti* | 88 | 38 | – | Brack/Meer | 1 |
| 163 | *Styracura pacifica* | 88 | 4 | native ×1 | Meer | 1 |
| 164 | *Paralabrax albomaculatus* | 86 | 755 | endemic ×1 | Meer | 1 |
| 165 | *Seriola rivoliana* | 84 | 1078 | native ×1 | Meer | 1 |
| 166 | *Trachinotus stilbe* | 84 | 112 | native ×1 | Meer | 1 |
| 167 | *Malacanthus brevirostris* | 83 | 33 | native ×1 | Meer | 1 |
| 168 | *Elagatis bipinnulata* | 81 | 609 | native ×1 | Meer | 1 |
| 169 | *Heteroconger klausewitzi* | 81 | 90 | endemic ×1 | Meer | 1 |
| 170 | *Anisotremus scapularis* | 80 | 627 | native ×1 | Meer | 1 |
| 171 | *Halichoeres discolor* | 80 | 23 | native ×1 | Meer | 1 |
| 172 | *Kuhlia mugil* | 80 | 237 | native ×2 | Brack/Meer | 1 |
| 173 | *Malacoctenus tetranemus* | 78 | 264 | native ×1 | Meer | 1 |
| 174 | *Malacoctenus zonogaster* | 78 | 152 | endemic ×1 | Meer | 1 |
| 175 | *Apogon pacificus* | 76 | 89 | native ×1 | Meer | 1 |
| 176 | *Carcharhinus albimarginatus* | 76 | 52 | native ×2 | Meer | 1 |
| 177 | *Stegastes leucorus* | 75 | 159 | – | Meer | 1 |
| 178 | *Heteropriacanthus carolinus* | 74 | – | native ×1 | Meer | 1 |
| 179 | *Nexilosus latifrons* | 74 | 102 | native ×1 | Meer | 1 |
| 180 | *Muraena clepsydra* | 73 | 93 | native ×1 | Meer | 1 |
| 181 | *Oplegnathus insignis* | 72 | 381 | native ×1 | Meer | 1 |
| 182 | *Xanthichthys mento* | 72 | 445 | native ×2 | Meer | 1 |
| 183 | *Calamus brachysomus* | 70 | 269 | native ×1 | Meer | 1 |
| 184 | *Iniistius pavo* | 70 | 42 | native ×1 | Meer | 1 |
| 185 | *Carcharhinus falciformis* | 68 | 212 | native ×2 | Meer | 1 |

<details><summary>Nicht aufgelöste Namen des Führers</summary>

*Alepocephalus convexifrons*, *Asquamiceps pacificus*, *Elacatinus rubrifrons*, *Pinnichthys atrimelum*, *Acyrtus arturo*, *Gobiesox lanceolatus*, *Gobiesox varius*, *Paraclinus asper*, *Coralliozetus clausus*, *Omobranchus sewalli*, *Baldwinella eos*, *Stellifer imiceps*, *Stellifer scierus*, *Stellifer simulus*, *Stellifer strabo*, *Stellifer typicus*, *Stellifer vermicularis*

</details>

## Änderungen gegenüber dem bestehenden Deck

- neu: 0
- entfallen: 0

## Ausgeschlossene Kandidaten

<details><summary>513 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Oxyzygonectes dovii* | 181 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oreochromis mossambicus* | 176 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia butleri* | 122 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Andinoacara coeruleopunctatus* | 110 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oreochromis niloticus* | 101 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sicydium salvini* | 86 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia mexicana* | 82 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gobiomorus maculatus* | 78 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brachyrhaphis rhabdophora* | 69 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinus carpio* | 59 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Astyanax orstedii* | 58 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mayaheros beani* | 57 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acanthemblemaria atrata* | 53 | Meer | zu klein (höchstens 3.2 cm) |
| *Ictalurus punctatus* | 53 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eleotris picta* | 52 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brachyrhaphis olomina* | 51 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Synbranchus marmoratus* | 47 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Awaous transandeanus* | 45 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinus rubrofuscus* | 44 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia reticulata* | 44 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poeciliopsis turrubarensis* | 44 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amatitlania sajica* | 40 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Uraspis helvola* | 39 | Meer | nur tiefer als die Tauchgrenze (erst ab 50 m) |
| *Gambusia affinis* | 36 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Alectis ciliaris* | 35 | Meer | nur tiefer als die Tauchgrenze (erst ab 60 m) |
| *Herotilapia multispinosa* | 35 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gambusia yucatana* | 33 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cribroheros diquis* | 32 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parachromis dovii* | 32 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynodonichthys hildebrandi* | 29 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rhamdia guatemalensis* | 29 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amatitlania siquia* | 28 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brachyrhaphis terrabensis* | 28 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bothus leopardinus* | 27 | Meer | nur tiefer als die Tauchgrenze (erst ab 55 m) |
| *Hoplias microlepis* | 27 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parachromis managuensis* | 26 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Axoclinus cocoensis* | 25 | Meer | zu klein (höchstens 3.5 cm) |
| *Lythrypnus cobalus* | 25 | Meer | zu klein (höchstens 1.9 cm) |
| *Pimelodella chagresi* | 25 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Euprepocaranx dorsalis* | 24 | Meer | nur tiefer als die Tauchgrenze (erst ab 60 m) |
| *Poeciliopsis viriosa* | 23 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brachyrhaphis roseni* | 22 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pontinus clemensi* | 22 | Meer | nur tiefer als die Tauchgrenze (erst ab 91 m) |
| *Brycon behreae* | 21 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sturisomatichthys panamensis* | 21 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Opistognathus punctatus* | 19 | Meer | nur tiefer als die Tauchgrenze (erst ab 50 m) |
| *Parachromis friedrichsthalii* | 19 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Priapichthys annectens* | 19 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Heteroconger digueti* | 18 | Meer | nur tiefer als die Tauchgrenze (erst ab 230 m) |
| *Poeciliopsis retropinna* | 18 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Talamancaheros sieboldii* | 18 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Tomicodon petersii* | 18 | Meer | zu klein (höchstens 3.5 cm) |
| *Poeciliopsis prolifica* | 16 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Coralliozetus angelicus* | 15 | Meer | zu klein (höchstens 3.5 cm) |
| *Lepomis macrochirus* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poeciliopsis sonoriensis* | 15 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acanthemblemaria mangognatha* | 14 | Meer | zu klein (höchstens 3.09 cm) |
| *Brachyrhaphis episcopi* | 14 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Epinephelus analogus* | 14 | Meer | nur tiefer als die Tauchgrenze (erst ab 50 m) |
| *Oreochromis aureus* | 13 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amatitlania nigrofasciata* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rineloricaria uracantha* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gobiesox potamius* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lebiasina boruca* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lythrypnus rhizophora* | 12 | Meer | zu klein (höchstens 3.4 cm) |
| *Talamancaheros underwoodi* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trichomycterus striatus* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Astronotus ocellatus* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemieleotris latifasciata* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lepomis cyanellus* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia caucana* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Priapichthys panamensis* | 11 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Axoclinus storeyae* | 10 | Meer | zu klein (höchstens 2.28 cm) |
| *Brycon costaricensis* | 10 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Fundulus lima* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hyporthodus acanthistius* | 9 | Meer | nur tiefer als die Tauchgrenze (erst ab 46 m) |
| *Amphilophus lyonsi* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinodon macularius* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nomeus gronovii* | 8 | Meer | nur tiefer als die Tauchgrenze (erst ab 200 m) |
| *Poeciliopsis paucimaculata* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Roeboides bouchellei* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Astyanax panamensis* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Campostoma ornatum* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Chaetostoma fischeri* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Chriolepis dialepta* | 7 | Meer | zu klein (höchstens 3.05 cm) |
| *Hypostomus aspidolepis* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia gillii* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Tigrigobius limbaughi* | 7 | Meer | zu klein (höchstens 3.33 cm) |
| *Axoclinus multicinctus* | 6 | Meer | zu klein (höchstens 3 cm) |
| *Catostomus bernardini* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gobioides peruanus* | 6 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hypsophrys nicaraguensis* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Roeboides bussingi* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Vieja maculicauda* | 6 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Agosia chrysogaster* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amphilophus citrinellus* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brachyrhaphis holdridgei* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Carassius auratus* | 5 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cribroheros alfari* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinodon eremus* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Geophagus crassilabris* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gila purpurea* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gobionellus microdon* | 5 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hyphessobrycon savagei* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Xiphophorus hellerii* | 5 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acanthemblemaria balanorum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Achirus mazatlanus* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Ancistrus chagresi* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Arcos poecilophthalmos* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ariopsis guatemalensis* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Axoclinus lucillae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Azurina hirundo* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Bagre pinnimaculatus* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Bairdiella ensifera* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Batrachoides pacifici* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Brachygenys californiensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Carcharodon carcharias* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Chloroscombrus orqueta* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Cichla monoculus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Coralliozetus rosenblatti* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cribroheros altifrons* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cribroheros longimanus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ctenolucius beani* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynodonichthys brunneus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynodonichthys frommi* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynodonichthys isthmensis* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynoscion xanthulus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Emblemaria hypacanthus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Emblemaria nivipes* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Eucinostomus entomelas* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Eugerres lineatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Euleptorhamphus viridis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gephyrocharax atracaudatus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gila minacae* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Haemulopsis axillaris* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hemanthias peruanus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hemibrycon dariensis* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemicaranx leucurus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Neetroplus nematopus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Labrisomus jenkinsi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Labrisomus multiporosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Malacoctenus zonifer* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Menticirrhus elongatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Microdesmus suttkusi* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Mola mola* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Mustelus californicus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Octopus fitchi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pliosteostoma lutipinnis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pontinus furcirhinus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Remora australis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Roeboides ilseae* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sciades dowii* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Scorpaena guttata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Synodus lucioceps* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Tomicodon boehlkei* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Urotrygon rogersi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Xanthichthys caeruleolineatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Xenichthys xanti* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Xenophallus umbratilis* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Xiphias gladius* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Antennatus strigatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Atherinella eriarcha* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Atractoscion nobilis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bagre panamensis* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Chaetodon meyeri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Characidium marshi* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cheilopogon xenopterus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Colossoma macropomum* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ctenogobius sagittula* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Cynodonichthys fuscolineatus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynodonichthys siegfriedi* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynoscion othonopterus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Decapterus macrosoma* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Decapterus muroadsi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gasteropelecus maculatus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gillellus semicinctus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gillichthys mirabilis* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Gobiesox adustus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gobiesox cephalus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gymnothorax mordax* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hemanthias signifer* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Herpetoichthys fossatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hypsoblennius jenkinsi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hypsoblennius striatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ictalurus furcatus* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ictalurus pricei* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Isthmoheros tuyrensis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Katsuwonus pelamis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Larimus effulgens* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lebiasina panamensis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Leptoancistrus canensis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lile stolifera* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mobula tarapacana* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mustelus henlei* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Naso brevirostris* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Negaprion brevirostris* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Neoheterandria tridentiger* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Octopus mimus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Odontoscion xanthops* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Ogcocephalus porrectus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Oligoplites inornatus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Opistognathus rhomaleus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paraclinus sini* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paraletharchus opercularis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paralichthys aestuarius* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Phallichthys amates* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gobiesox funebris* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Platyrhinoidis triseriata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Poecilia latipinna* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Poeciliopsis lucida* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poeciliopsis occidentalis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudophallus starksii* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rhamdia nicaraguensis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Roeboides occidentalis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sarda chiliensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Scorpaena sonorae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tigrigobius inornatus* | 3 | ? | zu wenige Nachweise (3 < 5) |
| *Tomicodon absitus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tomicodon myersi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Totoaba macdonaldi* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Triakis maculata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Trichiurus lepturus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Umbrina galapagorum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Zalieutes elater* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Abantennarius coccineus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Alfaro cultratus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ameiurus melas* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anchoa nasus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Arcos erythrops* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Atherinella hubbsi* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Atherinops affinis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Auxis brachydorax* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bairdiella armata* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Callechelys cliffi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Caranx ignobilis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Carcharhinus melanopterus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Carpiodes carpio* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Catostomus wigginsi* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Centropomus armatus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Centropomus undecimalis* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Cephaloscyllium ventriosum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cheilopogon atrisignis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cichla ocellaris* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cratinus agassizii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cynodonichthys chucunaque* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynodonichthys uroflammeus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Daector reticulata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Darienheros calobrensis* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Desmodema polystictum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dorosoma petenense* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Etrumeus acuminatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eucinostomus gracilis* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Gephyrocharax intermedius* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gymnothorax pictus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Gymnothorax porphyreus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnothorax verrilli* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnotus maculosus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Haemulopsis nitida* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Halichoeres aestuaricola* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Hyporthodus niphobles* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Istiompax indica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Labrisomus socorroensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lasiancistrus mayoloi* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lolliguncula panamensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Luvarus imperialis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Megachasma pelagios* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Megalops atlanticus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Melanorhinus cyanellus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Naso hexacanthus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Nebris occidentalis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Neoheterandria cana* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Octopus veligero* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Odontostilbe dialeptura* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oligoplites refulgens* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Oncorhynchus mykiss* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Pangasianodon hypophthalmus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paraclinus beebei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Phenagoniates macrolepis* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Piaractus brachypomus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Platax teira* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Poeciliopsis elongata* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poeciliopsis presidionis* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Porichthys mimeticus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Prionotus albirostris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Prionotus horrens* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Prionotus ruscarius* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pterobrycon myrnae* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Quassiremus nothochir* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Quietula guaymasiae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rhamdia laticauda* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Saccodon dariensis* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Scartichthys gigas* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scomberomorus concolor* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Serranus socorroensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sphyraena argentea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sphyraena stellata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Thalassoma bifasciatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tigrigobius digueti* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tomicodon zebra* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tomocichla tuba* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Triakis semifasciata* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Trinectes fonsecensis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Umbrina dorsalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Umbrina roncador* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Urobatis jamaicensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Urotrygon aspidura* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Urotrygon cimar* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Xyrichtys victori* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Abraliopsis falco* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Abudefduf saxatilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acanthurus leucocheilus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acanthurus mata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acanthurus olivaceus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Achirus klunzingeri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Achirus scutum* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Alloclinus holderi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amatitlania septemfasciata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ameiurus natalis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ameiurus nebulosus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ammodytoides gilli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amphilophus labiatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anarchias galapagensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anchoa helleri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anchoa mundeola* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Ancistrocheirus lesueurii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ancistrus centrolepis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anguilla marmorata* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Anisotremus surinamensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aplatophis zorro* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ariopsis jimenezi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Astyanax bransfordii* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Atherinella chagresi* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Atherinella crystallina* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Atherinopsis californiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Auxis eudorax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Auxis thazard* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Azurina intercrusma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Barbulifer pantherinus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bothus constellatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Brachyhypopomus occidentalis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Brachyrhaphis roswithae* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bregmaceros bathymaster* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Brockius striatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Brotula ordwayi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Caliraja inornata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carapus dubius* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Centropomus unionensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Cerdale ionthas* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaenopsis deltarrhis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaetodipterus faber* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Cheilopogon abei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheilopogon dorsomacula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheilopogon papilio* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chriolepis zebra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chromis punctipinnis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cichla temensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Citharichthys gilberti* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Citharichthys mariajorisae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clarkichthys bilineatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cochleoceps orientalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conodon serrifer* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cookeolus japonicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coralliozetus boehlkei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coralliozetus springeri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cosmocampus arctus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cribroheros rostratus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyclopsetta panamensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Cyclopsetta querna* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Cynodonichthys monikae* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynodonichthys weberi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cynoponticus coniceps* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cyphocharax magdalenae* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinella lutrensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Dactylagnus mundus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dactylagnus parvus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diodon eydouxii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diplectrum eumelum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diplectrum labarum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diplectrum maximum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diplectrum sciurus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dormitator maculatus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Dorosoma smithi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Doryteuthis opalescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eleotris tubularis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Embiotoca jacksoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Engraulis mordax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eques punctatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Erotelis armiger* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Etropus ciadi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eucinostomus melanopterus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Eugerres plumieri* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Evermannia zosterura* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gila eremica* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gobiesox canidens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gobiesox daedaleus* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gobiosoma paradoxum* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Gobiosoma seminudum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gobulus crescentalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gonatopsis borealis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gonatus californiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gorgasia punctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gramma loreto* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Grimalditeuthis bonplandii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Guentheridia formosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax buroensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax meleagris* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax moringa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Haemulon flavolineatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Haemulon plumierii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres californicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres inornatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Helicocranchia pfefferi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Heterostichus rostratus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hirundichthys marginatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hoplosternum punctatum* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hypanus americanus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Hypanus guttatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hyphessobrycon panamensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hyporthodus cifuentesi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hypsoblennius paytensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hypsoblennius proteus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ilisha fuerthii* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Isistius brasiliensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Isopisthus altipinnis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Japetella diaphana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Kathetostoma averruncus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Kronoheros umbrifer* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Labrisomus nuchipinnis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lactoria diaphana* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Lagocephalus lagocephalus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lamna ditropis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Larimus acclivis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leachia danae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leachia dislocata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lebiasina festae* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lepophidium prorates* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lolliguncula diomedeae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lonchopisthus sinuscalifornicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lycengraulis poeyi* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Malacoctenus costaricanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Malacoctenus margaritae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Masturus lanceolatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Maurolicus breviculus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Medialuna californiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mesonauta festivus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Microgobius brevispinis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Microphis lineatus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Naso vlamingii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Notarius kessleri* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Notarius planiceps* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Notarius troschelii* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Occidentarius platypogon* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Odontognathus panamensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Oncorhynchus keta* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Oncorhynchus kisutch* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Ophichthus rugifer* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophidion galapagensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophidion imitator* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiodon elongatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Opisthonema bulleri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Opistognathus fenmutis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Opistognathus scops* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Opsanus beta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxyporhamphus micropterus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Panamius panamensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paraclinus mexicanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paraconger californiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paraletharchus pacificus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paraselene orstedii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pareques fuscovittatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pisodonophis daspilotus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pleuronichthys ocellatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Poeciliopsis jackschultzi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poeciliopsis santaelena* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Porichthys analis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Porichthys greenei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Priapichthys darienensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Prionotus miles* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Prognathodes falcifer* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Psalidodon fasciatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Psenes cyanophrys* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudocheirodon terrabae* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pygocentrus cariba* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Remora brachyptera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Remora osteochir* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhinogobiops nicholsii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhynchoconger nitens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scorpaena afuerae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scorpaena wellingtoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sebastes macdonaldi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sebastes semicinctus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Selene setapinnis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Seriola peruana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sphoeroides kendalli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sphoeroides trichocephalus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sphyrna media* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sphyrna vespertina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Starksia galapagensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stellifer chrysoleuca* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sternopygus dariensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sternopygus macrurus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Stigmatoteuthis hoylei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Symphurus chabanaudi* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Syngnathus auliscus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Syngnathus carinatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synodus sechurae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thysanoteuthis rhombus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trinectes fluviatilis* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Tylosurus crocodilus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Umbrina analis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Umbrina wintersteeni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Urotrygon nana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Zu cristatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |

</details>

## Subdeck `invertebrates` (40)

Eigene Taxa, Größe und Filter, Reihenfolge-Quelle und Region des Rezepts. Arten, die schon in einem Level oder einem früheren Subdeck stehen, bleiben draußen; die Führer werden nicht abgeglichen.

- iNaturalist: 1730 Taxa (Seiten: 4)
- OBIS: 6287 Arten mit Nachweisen außer iNaturalist

### iNaturalist-Namen zugeordnet

Keine (`recipes/inat_names.json`).

### Von Hand ausgeschlossen

| Art | iNat | Grund |
|---|---|---|
| *Grapsus grapsus* | 7707 | Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen. |
| *Cardisoma crassum* | 2104 | Landkrabbe, lebt an Land und geht nur zum Laichen ans Meer. |
| *Ocypode gaudichaudii* | 1482 | Geisterkrabbe, lebt am trockenen Sandstrand. |
| *Nerita scabricosta* | 1259 | Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Goniopsis pulchra* | 824 | Mangrovenkrabbe, lebt im Wurzelwerk und Schlick über dem Wasser. |
| *Pachygrapsus socius* | 534 | Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen. |
| *Siphonaria gigas* | 453 | Napfschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Chiton stokesii* | 449 | Käferschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Vasula melones* | 311 | Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Nerita funiculata* | 282 | Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Crucibulum spinosum* | 229 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 24 von 25 Beobachtungen mit Angabe „tot“). |
| *Callinectes arcuatus* | 224 | Schwimmkrabbe der Lagunen und Flussmündungen, vor allem als Fang auf Märkten beobachtet. |
| *Ucides occidentalis* | 212 | Mangrovenkrabbe, lebt im Wurzelwerk und Schlick über dem Wasser. |
| *Arca pacifica* | 186 | Archenmuschel der Mangroven, lebt im Schlick zwischen den Wurzeln. |
| *Cerithium stercusmuscarum* | 178 | Schnecke des Schlickwatts und der Mangroven, bei Ebbe über dem Wasser. |
| *Emerita rathbunae* | 161 | Maulwurfskrebs, gräbt sich in der Brandung des Sandstrands ein. |
| *Tivela byronensis* | 159 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 11 von 12 Beobachtungen mit Angabe „tot“). |
| *Argopecten ventricosus* | 153 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 11 von 11 Beobachtungen mit Angabe „tot“). |
| *Arenaeus mexicanus* | 138 | Schwimmkrabbe der Lagunen und Flussmündungen, vor allem als Fang auf Märkten beobachtet. |
| *Geograpsus lividus* | 136 | Landkrabbe, lebt an Land und geht nur zum Laichen ans Meer. |
| *Chiton virgulatus* | 132 | Käferschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Porcellio laevis* | 132 | Landassel, kein Meerestier. |

### Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Hymenocera picta* | Die Harlekingarnele frisst nur Seesterne und ist einer der begehrtesten Funde für Unterwasserfotografen. | 149 | Reihenfolge-Quelle, OBIS, Verbreitung | invertebrates |
| *Pocillopora damicornis* | Die Blumenkohlkoralle baut die meisten der wenigen Korallenriffe des Ostpazifiks, etwa vor Panama und der Kokosinsel. | 236 | Reihenfolge-Quelle, OBIS | invertebrates |
| *Pavona gigantea* | Die Riesen-Pavona bildet im Ostpazifik meterhohe Korallenstöcke, die Taucher an Panamas und Costa Ricas Riffen sehen. | 36 | Reihenfolge-Quelle, OBIS, Verbreitung | invertebrates |

### Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS ohne iNaturalist oder Verbreitung): 40/40 (100 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 1: *Tambja mullineri*
- Arten ohne Volksnamen `de` in der Referenz-DB: 33/40 (82 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 12/40 (30 %)
- Familien ohne Volksnamen `de`: 32/32 (100 %): *Acanthasteridae*, *Aeolidiidae*, *Agariciidae*, *Aplysiidae*, *Chamidae*, *Cidaridae*, *Conidae*, *Cypraeidae*, *Dendrophylliidae*, *Diadematidae*, *Diogenidae*, *Echinometridae*, *Fasciolariidae*, *Holothuriidae*, *Inachidae*, *Margaritidae*, *Muricidae*, *Ophidiasteridae*, *Ophiocomidae*, *Oreasteridae*, *Palaemonidae*, *Palinuridae*, *Physaliidae*, *Plakobranchidae*, *Pocilloporidae*, *Polyceridae*, *Porpitidae*, *Stichopodidae*, *Strombidae*, *Toxopneustidae*, *Turbinidae*, *Veneridae*
- Familien ohne Volksnamen `en`: 18/32 (56 %): *Aeolidiidae*, *Agariciidae*, *Cidaridae*, *Dendrophylliidae*, *Diadematidae*, *Echinometridae*, *Inachidae*, *Margaritidae*, *Ophidiasteridae*, *Ophiocomidae*, *Oreasteridae*, *Physaliidae*, *Plakobranchidae*, *Pocilloporidae*, *Polyceridae*, *Porpitidae*, *Stichopodidae*, *Toxopneustidae*

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

Keine.

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

Keine.

### Arten

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Klasse |
|---|---|---|---|---|---|---|
| 1 | *Pentaceraster cumingi* | 1247 | 800 | native ×1 | Meer | Asteroidea |
| 2 | *Eucidaris galapagensis* (Quelle: *Eucidaris thouarsii*) | 1244 | 1611 | native ×1 | Meer | Echinoidea |
| 3 | *Phataria unifascialis* | 895 | 713 | native ×1 | Meer | Asteroidea |
| 4 | *Nidorellia armata* | 885 | 1028 | native ×1 | Meer | Asteroidea |
| 5 | *Tripneustes depressus* | 829 | 350 | native ×1 | Meer | Echinoidea |
| 6 | *Elysia diomedea* | 796 | 88 | – | Meer | Gastropoda |
| 7 | *Physalia utriculus* | 682 | 6 | native ×1 | Meer | Hydrozoa |
| 8 | *Echinometra vanbrunti* | 662 | 297 | native ×1 | Meer | Echinoidea |
| 9 | *Pharia pyramidata* | 618 | 446 | native ×1 | Meer | Asteroidea |
| 10 | *Diadema mexicanum* | 516 | 735 | native ×1 | Meer | Echinoidea |
| 11 | *Isostichopus fuscus* | 398 | 11909 | native ×1 | Meer | Holothuroidea |
| 12 | *Tubastraea coccinea* | 393 | 600 | native ×1 | Meer | Hexacorallia |
| 13 | *Panulirus inflatus* | 358 | 5 | – | Meer | Malacostraca |
| 14 | *Aplysia californica* | 305 | 29 | native ×1 | Meer | Gastropoda |
| 15 | *Acanthaster ellisii* (Quelle: *Acanthaster solaris*) | 291 | 57 | native ×1 | Meer | Asteroidea |
| 16 | *Toxopneustes roseus* | 284 | 142 | native ×1 | Meer | Echinoidea |
| 17 | *Hexaplex princeps* | 277 | 1124 | native ×1 | Meer | Gastropoda |
| 18 | *Holothuria lubrica* | 266 | – | native ×1 | Meer | Holothuroidea |
| 19 | *Titanostrombus galeatus* | 260 | 43 | native ×1 | Meer | Gastropoda |
| 20 | *Panulirus penicillatus* | 245 | 10978 | native ×2 | Meer | Malacostraca |
| 21 | *Panulirus gracilis* | 231 | 6986 | native ×1 | Meer | Malacostraca |
| 22 | *Porpita porpita* | 218 | 15 | – | Meer | Hydrozoa |
| 23 | *Ophiocoma aethiops* | 216 | 130 | native ×1 | Meer | Ophiuroidea |
| 24 | *Macrocypraea cervinetta* | 215 | 99 | – | Meer | Gastropoda |
| 25 | *Tambja mullineri* | 203 | 221 | endemic ×1 | Meer | Gastropoda |
| 26 | *Spurilla braziliana* | 188 | 5 | – | Meer | Gastropoda |
| 27 | *Triplofusus princeps* | 170 | 244 | – | Meer | Gastropoda |
| 28 | *Megapitaria squalida* | 169 | 148 | native ×1 | Meer | Bivalvia |
| 29 | *Pinctada mazatlanica* | 169 | 58 | native ×1 | Meer | Bivalvia |
| 30 | *Stenorhynchus debilis* | 165 | 201 | native ×1 | Meer | Malacostraca |
| 31 | *Strombus gracilior* | 153 | 93 | – | Meer | Gastropoda |
| 32 | *Calcinus explorator* | 151 | 41 | native ×1 | Meer | Malacostraca |
| 33 | *Turbo fluctuosus* | 148 | 87 | – | Meer | Gastropoda |
| 34 | *Conus purpurascens* | 146 | 146 | native ×1 | Meer | Gastropoda |
| 35 | *Conus nux* | 141 | 110 | native ×1 | Meer | Gastropoda |
| 36 | *Pavona gigantea* (Highlight; 71 Beobachter) | 139 | 592 | native ×2 | Meer | Hexacorallia |
| 37 | *Phyllonotus erythrostomus* | 137 | 59 | – | Meer | Gastropoda |
| 38 | *Chama coralloides* (Quelle: *Chama echinata*) | 134 | 49 | native ×1 | Meer | Bivalvia |
| 149 | *Hymenocera picta* (Highlight; 30 Beobachter) | 33 | 4 | native ×1 | Meer | Malacostraca |
| 236 | *Pocillopora damicornis* (Highlight; 14 Beobachter) | 18 | 93 | – | Meer | Hexacorallia |

### Grenzfälle

Je 10 Arten vor und nach der Grenze (Highlights übersprungen).

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Klasse | Im Subdeck |
|---|---|---|---|---|---|---|---|
| 28 | *Megapitaria squalida* | 169 | 148 | native ×1 | Meer | Bivalvia | ja |
| 29 | *Pinctada mazatlanica* | 169 | 58 | native ×1 | Meer | Bivalvia | ja |
| 30 | *Stenorhynchus debilis* | 165 | 201 | native ×1 | Meer | Malacostraca | ja |
| 31 | *Strombus gracilior* | 153 | 93 | – | Meer | Gastropoda | ja |
| 32 | *Calcinus explorator* | 151 | 41 | native ×1 | Meer | Malacostraca | ja |
| 33 | *Turbo fluctuosus* | 148 | 87 | – | Meer | Gastropoda | ja |
| 34 | *Conus purpurascens* | 146 | 146 | native ×1 | Meer | Gastropoda | ja |
| 35 | *Conus nux* | 141 | 110 | native ×1 | Meer | Gastropoda | ja |
| 37 | *Phyllonotus erythrostomus* | 137 | 59 | – | Meer | Gastropoda | ja |
| 38 | *Chama coralloides* (Quelle: *Chama echinata*) | 134 | 49 | native ×1 | Meer | Bivalvia | ja |
| | **Grenze** | | | | | | |
| 39 | *Persististrombus granulatus* | 133 | 24 | native ×1 | Meer | ? | nein |
| 40 | *Holothuria atra* | 132 | 124 | native ×1 | Meer | ? | nein |
| 41 | *Chiton articulatus* | 128 | 31 | – | Meer | ? | nein |
| 42 | *Clibanarius digueti* | 122 | 31 | – | Meer | ? | nein |
| 43 | *Pilosabia trigona* | 120 | 57 | native ×1 | Meer | ? | nein |
| 44 | *Lepas anserifera* | 119 | – | – | Meer | ? | nein |
| 45 | *Spirobranchus incrassatus* | 119 | – | native ×1 | Meer | ? | nein |
| 46 | *Holothuria inornata* | 116 | – | – | Meer | ? | nein |
| 47 | *Glycymeris gigantea* | 114 | 51 | – | Meer | ? | nein |
| 48 | *Ozius verreauxii* | 114 | 27 | native ×1 | Meer | ? | nein |

### Ausgeschlossene Kandidaten

<details><summary>500 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Grapsus grapsus* | 7707 | Meer | von Hand ausgeschlossen (Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen.) |
| *Cardisoma crassum* | 2104 | Meer | von Hand ausgeschlossen (Landkrabbe, lebt an Land und geht nur zum Laichen ans Meer.) |
| *Ocypode gaudichaudii* | 1482 | Meer | von Hand ausgeschlossen (Geisterkrabbe, lebt am trockenen Sandstrand.) |
| *Nerita scabricosta* | 1259 | Meer | von Hand ausgeschlossen (Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Goniopsis pulchra* | 824 | Meer | von Hand ausgeschlossen (Mangrovenkrabbe, lebt im Wurzelwerk und Schlick über dem Wasser.) |
| *Pachygrapsus socius* | 534 | Meer | von Hand ausgeschlossen (Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen.) |
| *Siphonaria gigas* | 453 | Meer | von Hand ausgeschlossen (Napfschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Chiton stokesii* | 449 | Meer | von Hand ausgeschlossen (Käferschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Vasula melones* | 311 | Meer | von Hand ausgeschlossen (Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Nerita funiculata* | 282 | Meer | von Hand ausgeschlossen (Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Octopus oculifer* | 257 | Meer | schon in einem anderen Subdeck (level-2) |
| *Crucibulum spinosum* | 229 | Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 24 von 25 Beobachtungen mit Angabe „tot“).) |
| *Callinectes arcuatus* | 224 | Brack/Meer | von Hand ausgeschlossen (Schwimmkrabbe der Lagunen und Flussmündungen, vor allem als Fang auf Märkten beobachtet.) |
| *Ucides occidentalis* | 212 | Meer | von Hand ausgeschlossen (Mangrovenkrabbe, lebt im Wurzelwerk und Schlick über dem Wasser.) |
| *Arca pacifica* | 186 | Meer | von Hand ausgeschlossen (Archenmuschel der Mangroven, lebt im Schlick zwischen den Wurzeln.) |
| *Macrobrachium hancocki* | 185 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cerithium stercusmuscarum* | 178 | Meer | von Hand ausgeschlossen (Schnecke des Schlickwatts und der Mangroven, bei Ebbe über dem Wasser.) |
| *Melanoides tuberculata* | 165 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Emerita rathbunae* | 161 | Meer | von Hand ausgeschlossen (Maulwurfskrebs, gräbt sich in der Brandung des Sandstrands ein.) |
| *Tivela byronensis* | 159 | Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 11 von 12 Beobachtungen mit Angabe „tot“).) |
| *Argopecten ventricosus* | 153 | Brack/Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 11 von 11 Beobachtungen mit Angabe „tot“).) |
| *Arenaeus mexicanus* | 138 | Meer | von Hand ausgeschlossen (Schwimmkrabbe der Lagunen und Flussmündungen, vor allem als Fang auf Märkten beobachtet.) |
| *Geograpsus lividus* | 136 | Meer | von Hand ausgeschlossen (Landkrabbe, lebt an Land und geht nur zum Laichen ans Meer.) |
| *Chiton virgulatus* | 132 | Meer | von Hand ausgeschlossen (Käferschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Porcellio laevis* | 132 | ? | von Hand ausgeschlossen (Landassel, kein Meerestier.) |
| *Octopus hubbsorum* | 115 | Meer | schon in einem anderen Subdeck (level-3) |
| *Corbicula fluminea* | 79 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrobrachium americanum* | 72 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Narcissia gracilis* | 42 | Meer | nur tiefer als die Tauchgrenze (erst ab 57 m) |
| *Procambarus clarkii* | 41 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Grimothea planipes* | 28 | Meer | nur tiefer als die Tauchgrenze (erst ab 101 m) |
| *Macrobrachium digueti* | 21 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrobrachium tenellum* | 18 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cherax quadricarinatus* | 15 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Physella acuta* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Coronaster marchenus* | 8 | Meer | nur tiefer als die Tauchgrenze (erst ab 52 m) |
| *Pomacea canaliculata* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anodontites trapesialis* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Planorbella trivolvis* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrobrachium panamense* | 5 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pyura haustor* | 5 | Meer | nur tiefer als die Tauchgrenze (erst ab 75 m) |
| *Rostanga pulchra* | 5 | Meer | nur tiefer als die Tauchgrenze (erst ab 102 m) |
| *Acar gradata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Amphibalanus improvisus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Anachis lyrata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Caliphylla mediterranea* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cardisoma guanhumi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cinetorhynchus hiatti* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cladopsammia gracilis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Conus scalaris* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cycloxanthops vittatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cymothoa exigua* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Dendraster excentricus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Donax gracilis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Doriopsilla rowena* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Echinometra oblonga* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Evibacus princeps* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Haliclona roslynae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hemimycale nathani* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hirsutodynomene ursula* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lobiger souverbii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Menippe frontalis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Navanax polyalphos* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Neogonodactylus zacae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Notopygos ornata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ochetostoma baronii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Octopus fitchi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Opalia funiculata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Phyllaplysia padinae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sabellastarte spectabilis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Salpa fusiformis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Anachis varia* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Strongylocentrotus purpuratus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Teleophrys cristulipes* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Tucetona strigilata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Turritella nodulosa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Actinoporus elongatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Alicia beebei* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Aplysilla polyraphis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Astrangia dentata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Astrometis sertulifera* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Berthella agassizii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bursa calcipicta* | 3 | ? | zu wenige Nachweise (3 < 5) |
| *Chaetopleura lanuginosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conasprella tornata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conchoderma auritum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Coralliophila violacea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Crepidula incurva* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Crucibulum personatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dendrodoris carbunculosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Enaeta cumingii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Enchiridium punctatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Eupleura nitida* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Forskalia tholoides* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Granolaria salmo* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Haliotis dalli* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Harpiliopsis depressa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hermosita hakunamatata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Higginsia johannae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Holothuria imitans* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Holothuria kefersteinii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Holothuria paraprinceps* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Holothuria pardalis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Isognomon janus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Antiopella barbarensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Labidodemas americanum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Leptopecten latiauratus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lucapinella milleri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Luidia columbia* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Modulus disculus* | 3 | ? | zu wenige Nachweise (3 < 5) |
| *Mycale parishii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mytilopsis adamsi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Nagurus nanus* | 3 | ? | zu wenige Nachweise (3 < 5) |
| *Nassarius gallegosi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Neotrypaea californiensis* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Nerocila californica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Octopus mimus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Olivella zanoeta* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pacifigorgia stenobrochis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paraconcavus mexicanus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pelagia flaveola* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Platypodiella rotundata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Renilla amethystina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rissoina stricta* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rocinela signata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Scopalina ruetzleri* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Solenosteira gatesi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Spondylus gloriosus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Squilla aculeata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Stellamedusa ventana* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Stenocionops ovatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Suberites aurantiacus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tagelus affinis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Taliepus nuttallii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tegula funebralis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tegula gallina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tivela stultorum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Trapania goslineri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tylos wegeneri* | 3 | ? | zu wenige Nachweise (3 < 5) |
| *Acarnus erithacus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Agabiformius lentus* | 2 | ? | zu wenige Nachweise (2 < 5) |
| *Aglaophenia diegensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Amphibalanus eburneus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anachis coronata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anthopleura artemisia* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Aplidium californicum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Atrina rigida* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Balanus calidus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bispira monroi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Calliactis polypus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cavernulina darwini* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cheilea cepacea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chione compta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Clavelina oblonga* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Clytia linearis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Columbella castanea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus archon* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus bartschi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus ebraeus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus orion* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cosmioconcha modesta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Craspedacusta sowerbii* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Crassispira incrassata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Crassostrea corteziensis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Crucibulum umbrella* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cryptosoma bairdii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cyclosalpa bakeri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Darwinella pronzatoi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dendrodoris nigromaculata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Diodora saturnalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Diaulula aurila* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dragmacidon raeae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Echinolittorina atrata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Echinolittorina lemniscata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ectopleura crocea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Elysia hedgpethi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eubranchus cucullus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Forskalia edwardsii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gari helenae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gari maxima* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gyractis sesere* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Halocynthia dumosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hiatella arctica* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Hymeniacidon perlevis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Isocheles pilosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Knefastia dalli* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lepidopa deamae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Leptoseris explanata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Leptoseris mycetoseroides* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ligia exotica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Liomera cinctimanus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lolliguncula panamensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lovenia cordiformis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Macrobrachium hobbsi* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrobrachium olfersii* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Megabalanus galapaganus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Megabalanus peninsularis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Megalobrachium poeyi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Metacarcinus anthonyi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Modulus cerodes* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Octopus veligero* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ophiocoma echinata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ophioderma teres* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ophionereis albomaculata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Oreaster reticulatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pacifigorgia curta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Paradoris lopezi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Patiria miniata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pavona clavus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pavona maldivensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pedipes angulatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pegea confoederata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Periploma planiusculum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Persephona orbicularis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Petrolisthes glasselli* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pilsbryspira aterrima* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pinnaxodes gigas* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plagusia immaculata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pocillopora inflata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudocnus californicus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pyrgulopsis bernardina* | 2 | ? | zu wenige Nachweise (2 < 5) |
| *Pyura lignosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Raeta undulata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Semele pulchra* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sicyonia penicillata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sinum debile* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Solena obliqua* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Spirobranchus spinosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Stiliger fuscovittatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Subcancilla sulcata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Symplegma brakenhielmi* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Tamaria obstipa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tegula rubroflammulata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tethyaster canaliculatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tetrabalanus polygenus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tivela mactroides* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trapezia rufopunctata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Turbo squamiger* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Turritella lentiginosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vitta virginea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Volvarina taeniolata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Xanthodius cooksoni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Xenobalanus globicipitis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Zoanthus sansibaricus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Zonitoides arboreus* | 2 | ? | zu wenige Nachweise (2 < 5) |
| *Zonulispira zonulata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Abraliopsis falco* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acar bailyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acteocina inculta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Actinopyga varians* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Albunea lucasia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alpheus bellimanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alpheus panamensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alpheus paracrinitus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ambidexter panamensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amiantis callosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amphibalanus inexpectatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amphibalanus reticulatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amphinome rostrata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amphiodia occidentalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anadara reinharti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ancistrocheirus lesueurii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ancula lentiginosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aphantolana costaricensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aplysilla glacialis* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Artemia franciscana* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Artemia salina* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Ascidia sydneiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Astrangia equatorialis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Astrocaneum spinosum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aurelia coerulea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Balanus poecilus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Boloceroides mcmurrichi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Brachidontes semilaevis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Branchiomma bairdi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Branchiomma nigromaculatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bunodeopsis medusoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cadlina limbaughorum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Caecum californicum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calappa hepatica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calliostoma eximium* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carditamera gracilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carinodrillia alboangulata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Casmaria erinaceus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cerithium menkei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cestoplana rubrocincta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chama venosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chiropsalmus alipes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chiton marmoratus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chloeia flava* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ciona intestinalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirolana harfordi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cliopsis krohnii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clivipollia fragaria* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cloridopsis dubia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clypeaster europacificus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clypeaster rotundus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Colidotea findleyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Compsodrillia haliplexa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conasprella baccata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conasprella emarginata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conchoderma virgatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus gradatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus miliaris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus sponsalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coralliophila nux* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coronula diadema* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Corymorpha palma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Crassispira kluthi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Crassispira nigerrima* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Crassispira rudis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Crepidula arenata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Crossata californica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cucumaria salma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cumingia lamellosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cuthona lizae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cuthona phoenix* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cycloseris cyclolites* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cyphoma emarginatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cystodytes dellechiajei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Daphnella mazatlanica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dendrodoris nigra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diadumene lineata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Didemnum cineraceum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Didemnum vexillum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diplosoma listerianum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Distaplia stylifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Distorsio constricta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dolabrifera dolabrifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Doriopsis pecten* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Doryteuthis opalescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dosima fascicularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dosinia concentrica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echinolittorina porcata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eoacmaea pustulata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Euapta lappa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eucheilota bakeri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eugorgia daniana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eunice macrobranchia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Euphausia pacifica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Excirolana braziliensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Felimida ruzafai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fiona pinnata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fistulobalanus dentivarians* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Galeropsis monodonta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gonatopsis borealis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gonatus californiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Grimalditeuthis bonplandii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Haliclona clairae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Haliclona dianae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Haliotis cracherodii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hancockia californica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Helicocranchia pfefferi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hemitoma octoradiata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hepatus kossmanni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hermodice carunculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Heteractaea lunata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria mexicana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria theeli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria zacae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Iphigenia brasiliensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Isognomon recognitus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Isostichopus badionotus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Janaria mirabilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Japetella diaphana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Karolus consobrinus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Kelletia kelletii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Kurtzia ephaedra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leachia danae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leachia dislocata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leiosolenus plumula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lepas hillii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leptogorgia exigua* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Liriope tetraphylla* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Lissoclinum fragile* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lolliguncula diomedeae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lottia gigantea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lucapinella callomarginata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Luidia senegalensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Luidia tessellata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lyncina schilderorum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Macrobrachium crebrum* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrobrachium crenulatum* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Macrobrachium heterochirus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Macrobrachium occidentale* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrobrachium rathbunae* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrorhynchia nuttingi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Macrostrombus costatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mactrellona alata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mactrotoma nasuta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mactrotoma velata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Maguimithrax spinosissimus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Maiopsis panamensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Marisa cornuarietis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mauritia scurra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Melampus coffea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Melongena melongena* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Menesiniella regalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mesocentrotus franciscanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Metandrocarpa taylori* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Microcassiope xantusii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mitra papalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mitrella ocellata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mitromorpha carpenteri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Monetaria annulus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mytilus californianus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nanomia bijuga* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nassarius iodes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neogonodactylus bahiahondensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nerita versicolor* | 1 | Süß/Meer | zu wenige Nachweise (1 < 5) |
| *Olivella anazora* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Olivella gracilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Olivella sphoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiocomina nigra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophioderma variegatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ostrea lurida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxymeris crenulata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pachycheles biocellatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pacifigorgia adamsii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pacifigorgia firma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pacifigorgia irene* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pagurus nesiotes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Panopea globosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Panopeus americanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paracerceis sculpta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paracondylactis hertwigi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parvanachis nigricans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pavona frondifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Penares angeli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Percnon abbreviatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Percnon planissimum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Persephona subovata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Petricola californiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phacellophora camtschatica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phragmatopoma attenuata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phylliroe bucephala* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllorhiza punctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Physophora hydrostatica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Piloslambrus triangulus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pilsbryspira aureonodosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pinna saccata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Placida dendritica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Placospongia intermedia* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Plagusia depressa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plakobranchus ocellatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Platydoris carolynae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Platymera gaudichaudii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Platyodon cancellatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plesiothyreus osculans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pododesmus macrochisma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polinices otis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polycera atra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polyclinum constellatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polycyathus isabela* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polymesoda inflata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polyophthalmus pictus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polystira picta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pontonia margarita* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Porites astreoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Porites sverdrupi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Praestheceraeus bellostriatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Praya dubia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudosquillisma adiastalta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pyrosoma atlanticum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rangia mendica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sabellastarte magnifica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Saccostrea glomerata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Semele purpurascens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sicyonia aliaffinis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sicyonia disparri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Spathochlamys vestalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Spheciospongia confoederata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Squilla mantoidea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stenoplax heathiana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stenoplax rugulata* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Stenopus hispidus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stephanolepas muricata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stichopus monotuberculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stigmatoteuthis hoylei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stramonita rustica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stylaster californicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stylocheilus striatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synalpheus lockingtoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tagelus peruvianus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Talostolida pellucens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tenaturris concinna* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tethya californiana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thalia democratica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thamnocephalus mexicanus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Thelecythara floridana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thor algicola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thyrolambrus verrucibrachium* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thysanoteuthis rhombus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tivela lessonii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trachypollia lugubris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trapania goddardi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trapezia formosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Turritella anactor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xiphopenaeus riveti* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Zonulispira chrysochildosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |

</details>

### Nicht aufgelöste Namen

<details><summary>815 Namen</summary>

*Coenobita compressus* (5773), *Hartnollius quadratus* (2063), *Ocypode occidentalis* (788), *Dolabrifera nicaraguana* (768), *Heliaster kubiniji* (498), *Eriphia squamata* (496), *Heliaster cumingi* (379), *Uca princeps* (362), *Lytechinus semituberculatus* (341), *Caviturritella leucostoma* (288), *Mithrodia bradleyi* (284), *Stramonita biserialis* (280), *Acanthais brevidentata* (266), *Chromolaichma sedna* (266), *Mexicardia procera* (261), *Carditamera affinis* (259), *Plicopurpura columellaris* (256), *Hysteroconcha lupanaria* (250), *Jenneria pustulata* (247), *Cardites tricolor* (239), *Calcinus californiensis* (233), *Felimare californiensis* (203), *Aratus pacificus* (199), *Bunodosoma californicum* (199), *Stylocheilus rickettsi* (190), *Calcinus obscurus* (186), *Cubaris murina* (169), *Bunodosoma grande* (168), *Minuca galapagensis* (167), *Columbella fuscata* (165), *Felimare agassizii* (155), *Pseudozonaria arabicula* (154), *Armases angustum* (153), *Johngarthia oceanica* (149), *Vitta luteofasciata* (139), *Muricanthus nigritus* (126), *Ophiocomella alexandri* (126), *Leucozonia cerata* (124), *Iliochione subrugosa* (122), *Opeatostoma pseudodon* (115), *Notocochlis chemnitzii* (109), *Cerithium adustum* (108), *Cerithideopsis californica* (104), *Eriphides hispida* (102), *Vasula speciosa* (102), *Chromolaichma dalli* (100), *Morum tuberculosum* (99), *Felimida norrisi* (98), *Leptuca crenulata* (98), *Leukoma grata* (96), *Cronius edwardsii* (94), *Venezillo stuckchensis* (93), *Armadillidium vulgare* (91), *Leptuca musica* (90), *Oliva spicata* (90), *Supplanaxis planicostatus* (88), *Calyptraea mamillaris* (82), *Pseudozonaria nigropunctata* (82), *Sarasinula plebeia* (82), *Columbella major* (80), *Ischnochiton muscarius* (80), *Mulinia pallida* (76), *Phyllodoce tuberculosa* (75), *Chiton sulcatus* (74), *Cypraecassis coarctata* (69), *Volutella caestus* (69), *Oliva incrassata* (65), *Orthalicus princeps* (65), *Agaronia testacea* (64), *Actinostella bradleyi* (60), *Echinaster tenuispina* (59), *Columbella strombiformis* (58), *Felimida sphoni* (58), *Aniculus elegans* (55), *Pseudozonaria annettae* (55), *Chionopsis gnidia* (54), *Encope galapagensis* (54), *Antidrymaeus sulphureus* (53), *Caviturritella gonostoma* (53), *Littoraria zebra* (53), *Strophocardia megastropha* (53), *Naria albuginosa* (52), *Oxynoe aliciae* (52), *Ophioderma panamense* (50), *Caviturritella banksii* (49), *Dallocardia radula* (49), *Cypraecassis tenuis* (47), *Noetia reversa* (47), *Pleurobranchus digueti* (47), *Cryptolepas rhachianecti* (46), *Larkinia grandis* (46), *Carditamera bajaensis* (45), *Felimida baumanni* (45), *Anthopleura mariscali* (44), *Clypeolum latissimum* (44), *Cucullaearca reeveana* (43), *Strigilla chroma* (43), *Tetraclita panamensis* (43), *Sanguinolaria tellinoides* (42), *Strigatella tristis* (42), *Glossaulax reclusiana* (41), *Leptuca latimanus* (41), *Muricanthus radix* (41), *Pusula radians* (40), *Tribulus planospira* (40), *Trizopagurus magnificus* (40), *Leptuca terpsichores* (39), *Rumina decollata* (38), *Edmundsella bertschi* (37), *Chione tumens* (36), *Chthamalus anisopoma* (36), *Donax assimilis* (36), *Ventrificus ventricosa* (35), *Aplysia hooveri* (34), *Luidia phragma* (34), *Neorapana tuberculata* (34), *Ovachlamys fulgens* (34), *Semicassis centiquadrata* (34), *Alanbeuella corrugata* (33), *Anteaeolidiella chromosoma* (33), *Sultana sultana* (33), *Antisabia panamensis* (32), *Crambe panamensis* (32), *Gemophos sanguinolentus* (32), *Euglandina gigantea* (31), *Pusio elegans* (31), *Leidyula moreleti* (30), *Paulia horrida* (30), *Americardia planicostata* (29), *Chiton goodallii* (29), *Isoaulactinia hespervolita* (29), *Jorunna osae* (29), *Pachyoliva semistriata* (29), *Cornu aspersum* (28), *Flabellinopsis iodinea* (28), *Glyptograpsus impressus* (28), *Neotiara lens* (28), *Polybranchia mexicana* (28), *Potimirim glabra* (28), *Subulina octona* (28), *Lottia fascicularis* (27), *Olivella volutella* (27), *Tyrannodoris leonis* (27), *Baeolidia moebii* (26), *Columbella haemastoma* (26), *Lamelliconcha concinna* (26), *Leptuca helleri* (26), *Monoplex vestitus* (26), *Muricea plantaginea* (26), *Thaisella kiosquiformis* (26), *Tikoconus costaricanus* (26), *Vokesimurex ruthae* (26), *Agathistoma verrucosum* (25), *Lamarcka mutabilis* (25), *Anadara obesa* (24), *Conus edaphus* (24), *Ischnochiton dispar* (24), *Goniofusus dupetitthouarsi* (23), *Mitrella delicata* (23), *Favorinus elenalexiae* (22), *Leucozonia tuberculata* (22), *Muricea purpurea* (22), *Uca stylifera* (22), *Fissurella gemmata* (21), *Limaria pacifica* (21), *Liocerithium judithae* (21), *Oliva polpasta* (21), *Pseudopusula sanguinea* (21), *Armases occidentale* (20), *Axinactis delessertii* (20), *Cubaris flavobrunnea* (20), *Geitodoris mavis* (20), *Gemophos gemmatus* (20), *Hybolophus gibbosus* (20), *Neorapana muricata* (20), *Oxymeris strigata* (20), *Phrontis luteostoma* (20), *Bostrycapulus latebrus* (19), *Bradybaena similaris* (19), *Bulbaeolidia sulphurea* (19), *Corbicula largillierti* (19), *Echinolittorina dubiosa* (19), *Lunarca brevifrons* (19), *Apiocardia obovalis* (18), *Cerithideopsis montagnei* (18), *Epidendrium billeeanum* (18), *Lamelliconcha unicolor* (18), *Leiaster teres* (18), *Acanthochitona exquisita* (17), *Anachis fluctuata* (17), *Anteaeolidiella ireneae* (17), *Columbella labiosa* (17), *Ellobium stagnale* (17), *Ischnochiton tridentatus* (17), *Onchidella steindachneri* (17), *Samla telja* (17), *Tegula rugosa* (17), *Terrazoanthus patagonichus* (17), *Chaetopleura lurida* (16), *Hypterita helicoides* (16), *Hysteroconcha rosea* (16), *Penethais triangularis* (16), *Zenopontonia soror* (16), *Cuthona destinyae* (15), *Lissachatina fulica* (15), *Phataria mionactis* (15), *Terebra robusta* (15), *Bostrycapulus calyptraeiformis* (14), *Calyptraea conica* (14), *Naesiotus amastroides* (14), *Oliva truncata* (14), *Pseudobiceros deliae* (14), *Turritriton gibbosus* (14), *Uca ornata* (14), *Agaronia griseoalba* (13), *Echinolittorina conspersa* (13), *Lamelliconcha vinacea* (13), *Linisa texasiana* (13), *Naesiotus tortuganus* (13), *Neoterebra variegata* (13), *Petruca panamensis* (13), *Psammotella bertini* (13), *Scurria stipulata* (13), *Stigmaulax broderipiana* (13), *Vitularia salebrosa* (13), *Xanthodius sternberghii* (13), *Harvella elegans* (12), *Labyrinthus uncigerus* (12), *Lanthonia grantii* (12), *Leptuca stenodactylus* (12), *Mithraculus nodosus* (12), *Monoplex macrodon* (12), *Phyllocoma scalariformis* (12), *Stenoplax mariposa* (12), *Terebra ornata* (12), *Alpheus richardsoni* (11), *Anachis rugosa* (11), *Axinactis inaequalis* (11), *Diplosolenodes occidentalis* (11), *Harpa crenata* (11), *Lirophora mariae* (11), *Lysmata argentopunctata* (11), *Mytella strigata* (11), *Rhinocoryne humboldti* (11), *Siphonaria costata* (11), *Solenosteira macrospira* (11), *Uvanilla olivacea* (11), *Venezillo parvus* (11), *Vullietoliva splendidula* (11), *Acrosterigma pristipleura* (10), *Amphiaster insignis* (10), *Callyspongia californica* (10), *Carditamera radiata* (10), *Ctena galapagana* (10), *Felimida marislae* (10), *Hermissenda opalescens* (10), *Homalocantha oxyacantha* (10), *Northia northiae* (10), *Pacifigorgia darwinii* (10), *Parametaria dupontii* (10), *Parametaria macrostoma* (10), *Petrolisthes sanfelipensis* (10), *Phrontis tiarula* (10), *Temnoconcha cognata* (10), *Uvanilla unguis* (10), *Acanthochitona hirudiniformis* (9), *Engina tabogaensis* (9), *Fissurella obscura* (9), *Fissurella spongiosa* (9), *Fugleria illota* (9), *Johngarthia cocoensis* (9), *Littoraria variegata* (9), *Manucomplanus varians* (9), *Mellita notabilis* (9), *Mexacanthina angelica* (9), *Monoplex wiegmanni* (9), *Naesiotus basiplicatus* (9), *Pagurus benedicti* (9), *Papyridea aspersa* (9), *Petricolaria cognata* (9), *Rabdotus sufflatus* (9), *Triops longicaudatus* (9), *Agaronia propatula* (8), *Aplysina chiriquiensis* (8), *Bostrycapulus urraca* (8), *Callyspongia acapulcaensis* (8), *Cardites crassicostatus* (8), *Eurytellina regia* (8), *Fissurella deroyae* (8), *Labyrinthus otis* (8), *Minuca osa* (8), *Oliva undatella* (8), *Pacifigorgia symbiotica* (8), *Pagurus lepidus* (8), *Petrolisthes hirtipes* (8), *Pseudogaetice americanus* (8), *Sheldonella olssoni* (8), *Thylacodes oryzatus* (8), *Tritonicula pickensi* (8), *Tyrannodoris tigris* (8), *Uca monilifera* (8), *Xerarionta areolata* (8), *Antipathozoanthus hickmani* (7), *Enaeta barnesii* (7), *Gulella bicolor* (7), *Laevicardium elenense* (7), *Lottia atrata* (7), *Lottia stanfordiana* (7), *Mactrellona clisia* (7), *Monoplex lignarius* (7), *Neptunazurea porterae* (7), *Niveria pacifica* (7), *Phrontis nassiformis* (7), *Pseudoceros josei* (7), *Sapphirina* (7), *Sheldonella delgada* (7), *Sinanodonta pacifica* (7), *Terebra formosa* (7), *Uca heteropleura* (7), *Venezillo gigas* (7), *Zetecopsis zeteki* (7), *Anachis scalarina* (6), *Aplysina revillagigedi* (6), *Atrimitra effusa* (6), *Bulimulus* (6), *Chloeia pseudeuglochis* (6), *Cymia tectum* (6), *Drymaeus serperastrum* (6), *Felimare lapislazuli* (6), *Lamelliconcha paytensis* (6), *Lottia discors* (6), *Lottia mitella* (6), *Naesiotus rimatus* (6), *Naesiotus ustulatus* (6), *Neoterebra aspera* (6), *Onchidella hansi* (6), *Paguristes sanguinimanus* (6), *Pagurus nanodes* (6), *Parazoanthus darwini* (6), *Parvanachis pygmaea* (6), *Petrolisthes edwardsii* (6), *Pustulatirus sanguineus* (6), *Tucetona multicostata* (6), *Acar rostae* (5), *Allopeas gracile* (5), *Anadara aequatorialis* (5), *Anadara emarginata* (5), *Aplysina encarnacionae* (5), *Brissus obesus* (5), *Calloarca alternata* (5), *Chionopsis pulicaria* (5), *Crepidula marginalis* (5), *Dardanus janethaigae* (5), *Diodora digueti* (5), *Eurytellina rubescens* (5), *Gemophos ringens* (5), *Hesione panamenea* (5), *Heterogorgia hickmani* (5), *Lamelliconcha tortuosa* (5), *Leptarionta venusta* (5), *Leptuca festae* (5), *Leukoma asperrima* (5), *Leukoma columbiensis* (5), *Leukoma pertincta* (5), *Lima tetrica* (5), *Linisa behrii* (5), *Mesembrinus costaricensis* (5), *Mexacanthina lugubris* (5), *Minuca ecuadoriensis* (5), *Pallifera costaricensis* (5), *Panamitra gigantea* (5), *Persicula tessellata* (5), *Petrolisthes donadio* (5), *Polygona socorroensis* (5), *Rabdotus dealbatus* (5), *Speloeophorus schmitti* (5), *Stomolophus* (5), *Succinea clarionensis* (5), *Trigonostoma goniostoma* (5), *Vokesimurex recurvirostris* (5), *Aliena parva* (4), *Anachis boivini* (4), *Belocaulus angustipes* (4), *Caryocorbula ovulata* (4), *Chthamalus panamensis* (4), *Dictyodendrilla dendyi* (4), *Echinolittorina apicina* (4), *Eurytellina simulans* (4), *Favartia vittata* (4), *Felaniella sericata* (4), *Fissurella nigrocincta* (4), *Glaucilla thompsoni* (4), *Inuda luarna* (4), *Kalolophus antillarum* (4), *Leptuca bacillopilosa* (4), *Leptuca beebei* (4), *Leptuca oerstedi* (4), *Leptuca saltitanta* (4), *Littoraria varia* (4), *Lysiosquilla lisa* (4), *Marsupina nana* (4), *Mesembrinus ziegleri* (4), *Microcithara harpiformis* (4), *Minuca herradurensis* (4), *Minuca zacae* (4), *Monoplex keenae* (4), *Neoterebra armillata* (4), *Neoterebra tuberculosa* (4), *Ochetoclava gemmata* (4), *Parhippolyte cavernicola* (4), *Petricola insignis* (4), *Phyllodoce novaehollandiae* (4), *Polygyra cereolus* (4), *Potamocarcinus magnus* (4), *Prunum sapotilla* (4), *Pseudobiceros bajae* (4), *Pseudoceros mexicanus* (4), *Pseudochama picta* (4), *Simnia arcuata* (4), *Simomactra dolabriformis* (4), *Spirobranchus minutus* (4), *Strombina maculosa* (4), *Succinea bettii* (4), *Supplanaxis obsoletus* (4), *Terebra argosyia* (4), *Tivela delessertii* (4), *Trigoniocardia granifera* (4), *Trochomodulus catenulatus* (4), *Anachis pardalis* (3), *Anadara bifrons* (3), *Aspella hastula* (3), *Aspella pyramidalis* (3), *Atya innocous* (3), *Beckianum beckianum* (3), *Berthella grovesi* (3), *Callistochiton elenensis* (3), *Caracolus marginella* (3), *Caryocorbula amethystina* (3), *Cataleptodius taboganus* (3), *Catolasmus pilsbryi* (3), *Chthamalus southwardorum* (3), *Columbella paytensis* (3), *Columbella sonsonatensis* (3), *Cyanoplax beanii* (3), *Dermomurex indentatus* (3), *Diaulula nayarita* (3), *Doriopsilla davebehrensi* (3), *Engina maura* (3), *Engina pulchra* (3), *Epialtus minimus* (3), *Euclia cassidiformis* (3), *Eugorgia aurantiaca* (3), *Eugorgia multifida* (3), *Euvola perulus* (3), *Favartia erosa* (3), *Faxonius virilis* (3), *Felimida macfarlandi* (3), *Gari panamensis* (3), *Gyroscala statuminata* (3), *Happia zeteki* (3), *Hesperaptyxis cinereus* (3), *Histiomena marginata* (3), *Isocheles ingowehrtmanni* (3), *Johngarthia malpilensis* (3), *Leptarionta costaricensis* (3), *Leptuca deichmanni* (3), *Leucosilia jurinii* (3), *Limacus flavus* (3), *Limenandra confusa* (3), *Lottia acutapex* (3), *Lottia pediculus* (3), *Luidia superba* (3), *Mesembrinus emeus* (3), *Mitrella pulchrior* (3), *Naesiotus dentifer* (3), *Naesiotus nux* (3), *Naesiotus wolfi* (3), *Naticarius caneloensis* (3), *Noetia magna* (3), *Olivella cocosensis* (3), *Onchidella binneyi* (3), *Pacifigorgia rubripunctata* (3), *Phrontis pagoda* (3), *Prostheceraeus fitae* (3), *Pseudothelphusa rechingeri* (3), *Semele sowerbyi* (3), *Sesarma aequatoriale* (3), *Solenosteira anomala* (3), *Stenoplax sonorana* (3), *Tellidora burneti* (3), *Tellinidella purpurea* (3), *Thylacodes margaritaceus* (3), *Tonicia arnheimi* (3), *Tucetona bicolor* (3), *Xerarionta veatchii* (3), *Acanthochitona ferreirai* (2), *Achelous xantusii* (2), *Ala cornuta* (2), *Anachis fulva* (2), *Anachis lentiginosa* (2), *Anachis nigrofusca* (2), *Aphera tessellata* (2), *Armases magdalenense* (2), *Atya margaritacea* (2), *Bifurcium bicanaliferum* (2), *Bivetopsia chrysostoma* (2), *Callianax biplicata* (2), *Callistochiton expressus* (2), *Calyptraea lichen* (2), *Colubraria jordani* (2), *Crucibulum pectinatum* (2), *Cyrtopleura crucigera* (2), *Deroceras laeve* (2), *Donax transversus* (2), *Dorsina dorsata* (2), *Euceramus panatelus* (2), *Euglandina striata* (2), *Eupleura vokesorum* (2), *Eurytellina inaequistriata* (2), *Gemophos janellii* (2), *Hastula luctuosa* (2), *Helicina orbiculata* (2), *Hertleinia mitriformis* (2), *Hespererato scabriuscula* (2), *Hesperisternia vibex* (2), *Humboldtiana ootamorum* (2), *Hysteroconcha dione* (2), *Iridopagurus occidentalis* (2), *Ischioscia variegata* (2), *Jorunna tempisquensis* (2), *Laevicaulis alte* (2), *Lamelliconcha alternata* (2), *Leptinaria unilamellata* (2), *Leptuca umbratila* (2), *Leukoma beili* (2), *Macron aethiops* (2), *Mactrellona subalata* (2), *Mammilla caprae* (2), *Megalobrachium sinuimanus* (2), *Mesembrinus sulcosus* (2), *Microeuraphia eastropacensis* (2), *Minuca argillicola* (2), *Minuca brevifrons* (2), *Mitromica solitaria* (2), *Murexsul armatus* (2), *Muricea austera* (2), *Naesiotus achatellinus* (2), *Naesiotus spirifer* (2), *Natica lunaris* (2), *Niparaya regiscorona* (2), *Okenia academica* (2), *Oliva julieta* (2), *Oliva pindarina* (2), *Onchidella lesliei* (2), *Pachycheles panamensis* (2), *Papyridea curvicostata* (2), *Pascula rufonotata* (2), *Pelia pacifica* (2), *Penethais callaoensis* (2), *Perplicaria clarki* (2), *Petrolisthes crenulatus* (2), *Petrolisthes nobilii* (2), *Phimochirus roseus* (2), *Phos crassus* (2), *Phrontis complanata* (2), *Phrontis versicolor* (2), *Placida brookae* (2), *Plicatula spondylopsis* (2), *Pomacea flagellata* (2), *Pseudochama corrugata* (2), *Pseudopusula californiana* (2), *Pseudothelphusa sonorensis* (2), *Purpurellus pinniger* (2), *Pustulatirus hemphilli* (2), *Seila assimilata* (2), *Semele formosa* (2), *Strigilla cicercula* (2), *Strigilla sincera* (2), *Strombina recurva* (2), *Talitroides topitotum* (2), *Tegula picta* (2), *Thyca callista* (2), *Tomoberthella martensi* (2), *Tyche lamellifrons* (2), *Uca intermedia* (2), *Vermicularia frisbeyae* (2), *Vokesimurex tricoronis* (2), *Acartia* (1), *Achelous iridescens* (1), *Acromegalomma coloratum* (1), *Aethra scutata* (1), *Agathistoma cortezianum* (1), *Agathistoma ligulatum* (1), *Agathistoma marianum* (1), *Allopeas clavulinum* (1), *Alpheus hyeyoungae* (1), *Alpheus javieri* (1), *Ambigolimax valentianus* (1), *Americhiton arragonites* (1), *Amphithrax bellii* (1), *Anachis atramentaria* (1), *Aplysina clathrata* (1), *Arcinella californica* (1), *Arcitalitrus sylvaticus* (1), *Arene socorroensis* (1), *Armadillidium nasatum* (1), *Armases americanum* (1), *Ascidia sideralis* (1), *Astrodictyum panamense* (1), *Atrimitra idae* (1), *Atya dressleri* (1), *Atya scabra* (1), *Bailya anomala* (1), *Barynaias caldwellii* (1), *Berendtia taylori* (1), *Bermudella pellucida* (1), *Brachidontes puntarenensis* (1), *Calliostoma bonita* (1), *Callistochiton pulchrior* (1), *Callistoplax retusa* (1), *Cancellaria decussata* (1), *Cancellaria indentata* (1), *Cancellaria jayana* (1), *Cancellaria obesa* (1), *Cardites grayi* (1), *Carminodoris bramale* (1), *Caryocorbula biradiata* (1), *Caryocorbula otra* (1), *Cerithium gallapaginis* (1), *Cerithium nicaraguense* (1), *Chama producta* (1), *Chioneryx squamosa* (1), *Chondrilla pacifica* (1), *Chondrilla verrucosa* (1), *Chrysaora* (1), *Chthamalus hedgecocki* (1), *Cliona vallartensis* (1), *Colubraria lucasensis* (1), *Crepidula rostrata* (1), *Ctena mexicana* (1), *Cyanoplax keepiana* (1), *Cyclothyca corrugata* (1), *Cypraecassis wilmae* (1), *Dactylonida mexicana* (1), *Daldorfia trigona* (1), *Dallocardia quadragenaria* (1), *Diodora pica* (1), *Divalinga perparvula* (1), *Donax caelatus* (1), *Drymaeus josephus* (1), *Dulcerana granularis* (1), *Edmundsella vansyoci* (1), *Encope californica* (1), *Endectyon hispitumulus* (1), *Eoacmaea semirubida* (1), *Epialtoides paradigmus* (1), *Epitonium hexagonum* (1), *Epitonium hindsii* (1), *Epitonium obtusum* (1), *Epitonium reflexum* (1), *Eriphia granulosa* (1), *Eubranchus yolandae* (1), *Euclia balboae* (1), *Euglandina carminensis* (1), *Euglandina rosea* (1), *Euglandina singleyana* (1), *Euglandina turris* (1), *Favartia lappa* (1), *Felimare amalguae* (1), *Felimida galexorum* (1), *Ficopomatus miamiensis* (1), *Fissurella macrotrema* (1), *Geodia media* (1), *Globivenus isocardia* (1), *Glycymeris lintea* (1), *Glyptoxanthus labyrinthicus* (1), *Glyptoxanthus meandricus* (1), *Goniodoridella cochimi* (1), *Helicina amoena* (1), *Helicina funcki* (1), *Helicina monteverdensis* (1), *Hemimycale polyboletus* (1), *Henricia nana* (1), *Herbstia camptacantha* (1), *Herbstia pyriformis* (1), *Hesperaptyxis ambustus* (1), *Heterocrypta craneae* (1), *Holothuria viridiaurantia* (1), *Humboldtiana durangoensis* (1), *Hydra viridissima* (1), *Hyotissa quercinus* (1), *Incidostoma giganteum* (1), *Isara swainsonii* (1), *Ischnochiton tenuisculptus* (1), *Janolus anulatus* (1), *Janua* (1), *Leiosolenus aristatus* (1), *Leopecten diegensis* (1), *Leporimetis cognata* (1), *Leptuca batuenta* (1), *Leptuca coloradensis* (1), *Leptuca inaequalis* (1), *Leptuca tenuipedis* (1), *Leptuca tomentosa* (1), *Littoraria aberrans* (1), *Lottia argrantesta* (1), *Lottia dalliana* (1), *Lottia immaculata* (1), *Lottia strongiana* (1), *Lysmata galapagensis* (1), *Macoploma lamproleuca* (1), *Marionia kinoi* (1), *Marsenia perspicua* (1), *Melampus mousleyi* (1), *Melanella* (1), *Mellita kanakoffi* (1), *Mesembrinus attenuatus* (1), *Mesembrinus hegewischi* (1), *Mesotomura echinata* (1), *Mexichromis tica* (1), *Minyocerus kirki* (1), *Mitrella santabarbarensis* (1), *Monostiolum pictum* (1), *Moreiradromia sarraburei* (1), *Mulinia modesta* (1), *Murexsul skoglundae* (1), *Muricea squarrosa* (1), *Mytella tumbezensis* (1), *Naesiotus montezuma* (1), *Naesiotus pallidior* (1), *Nassarius myristicatus* (1), *Nassarius nodicinctus* (1), *Neobernaya spadicea* (1), *Neodoclea boneti* (1), *Neoterebra carolae* (1), *Neoterebra frigata* (1), *Neoterebra larvaeformis* (1), *Neotiara muricata* (1), *Neotiara sphoni* (1), *Neotrypaea costaricensis* (1), *Norrisia norrisii* (1), *Notoacmea biradiata* (1), *Nuttallina crossota* (1), *Oliva kerstitchi* (1), *Omalacantha bicornuta* (1), *Ophiocomella schmitti* (1), *Orthalicus decolor* (1), *Pachyoliva columellaris* (1), *Pacifigorgia dampieri* (1), *Pagurus rhabdotus* (1), *Panopeus purpureus* (1), *Paphonotia elliptica* (1), *Persicula phrygia* (1), *Petricola exarata* (1), *Petrolisthes occidentalis* (1), *Phlogocardia belcheri* (1), *Pinnixa plectrophoros* (1), *Pittieria* (1), *Planocera tridentata* (1), *Plicatula penicillata* (1), *Polinices panamaensis* (1), *Politoleda polita* (1), *Polymesoda notabilis* (1), *Pomacea maculata* (1), *Psammotreta dombei* (1), *Psammotreta pura* (1), *Pseudobiceros stellae* (1), *Pseudopusula geigeri* (1), *Pseudozonaria aequinoctialis* (1), *Pteropurpura erinaceoides* (1), *Ptychophallus tristani* (1), *Pusio pagodus* (1), *Pyruclia bulbulus* (1), *Pyruclia solida* (1), *Ranilia angustata* (1), *Raninoides benedicti* (1), *Reticutriton lineatus* (1), *Rhizophysa eysenhardtii* (1), *Sardorchestia gracilis* (1), *Semele californica* (1), *Semele elliptica* (1), *Semele rosea* (1), *Septifer zeteki* (1), *Siphonaria aequilirata* (1), *Siphonaria pica* (1), *Sonorella cananea* (1), *Steironepion piperatum* (1), *Stenoplax magdalenensis* (1), *Subcancilla directa* (1), *Subcancilla edithrexae* (1), *Subcancilla hindsii* (1), *Symethis garthi* (1), *Tellinella zacae* (1), *Tenuicorbula tenuis* (1), *Tetragrapsus jouyi* (1), *Thormora setosior* (1), *Thylacodes eruciformis* (1), *Thylaeodus indentatus* (1), *Tornatellides chathamensis* (1), *Trajana perideris* (1), *Trigonostoma breve* (1), *Trigonostoma elegantulum* (1), *Trimusculus stellatus* (1), *Triops newberryi* (1), *Trivettea papalotla* (1), *Tryonigens remondi* (1), *Turritella radula* (1), *Turritriton kobelti* (1), *Unidentia angelvaldesi* (1), *Venezillo longispinis* (1), *Vermicularia pellucida* (1), *Vitta consobrina* (1), *Vokesimurex lividus* (1), *Zetecopsis westonensis* (1), *Zoanthus kuroshio* (1)

</details>

## Nicht aufgelöste Namen der Reihenfolge-Quelle

Die Referenz-DB der App kennt diese Namen nicht; die App fände sie auch nicht.

| Name | iNat |
|---|---|
| *Micropterus nigricans* | 77 |
| *Pterygoplichthys* | 77 |
| *Coralliozetus clausus* | 3 |
| *Eretmobrycon scleroparius* | 3 |
| *Elacatinus rubrifrons* | 2 |
| *Eretmobrycon terrabensis* | 2 |
| *Paraclinus asper* | 1 |
| *Stellifer scierus* | 1 |
| *Stellifer strabo* | 1 |
| *Stellifer typicus* | 1 |
