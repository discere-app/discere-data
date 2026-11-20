# Bericht: Tropischer Ostpazifik (`recipes/tropical_eastern_pacific.json`)

Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.

- Referenz-DB: v3 (FishBase v26.06, SeaLifeBase v26.06)
- Salz/Süß: FishBase/SeaLifeBase v25.04 (species.parquet)
- iNaturalist: 978 Taxa (Seiten: 2)
- OBIS: 2074 Arten
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

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS oder Verbreitung): 156/159 (98 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 7: *Amblyrhynchus cristatus*, *Brachygenys jessiae*, *Gobioclinus dendriticus*, *Apogon atradorsatus*, *Lepidonectes corallicola*, *Girella freminvillii*, *Archosargus pourtalesii*
- Arten ohne Volksnamen `de` in der Referenz-DB: 115/159 (72 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 6/159 (4 %)
- Familien ohne Volksnamen `de`: 10/58 (17 %): *Aetobatidae*, *Cheloniidae*, *Epinephelidae*, *Girellidae*, *Iguanidae*, *Mobulidae*, *Octopodidae*, *Otariidae*, *Rhinopteridae*, *Urotrygonidae*
- Familien ohne Volksnamen `en`: 2/58 (3 %): *Iguanidae*, *Otariidae*

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

- *Odontaspis ferox*: OBIS, Verbreitung, Führer
- *Amblyrhynchus cristatus*: Verbreitung
- *Zalophus wollebaeki*: Verbreitung

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

- gleicher Volksname `de` „krake“: *Octopus oculifer*, *Octopus hubbsorum*
- gleicher Volksname `de` „Schnapper“: *Lutjanus argentiventris*, *Lutjanus novemfasciatus*, *Lutjanus guttatus*, *Lutjanus colorado*

## Deck

Spalten: Rang unter den Kandidaten, Zählung der Reihenfolge-Quelle (iNat), OBIS-Nachweise, Einträge der FishBase/SeaLifeBase-Verbreitung in den Rezept-Regionen (~~durchgestrichen~~: Eintrag sagt „nicht vorhanden“), Wasser laut FishBase/SeaLifeBase, Nummer des Führers, der die Art listet.

### Level 1 (49)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Führer |
|---|---|---|---|---|---|---|
| 1 | *Chelonia mydas* | 4242 | 5246 | native ×1 | Meer | – |
| 2 | *Abudefduf troschelii* | 2559 | 2858 | native ×2 | Meer | 1 |
| 3 | *Holacanthus passer* | 2507 | 4635 | native ×2 | Meer | 1 |
| 4 | *Prionurus laticlavius* | 2454 | 1946 | native ×2 | Meer | 1 |
| 5 | *Bodianus diplotaenia* | 2419 | 4683 | native ×2 | Meer | 1 |
| 6 | *Thalassoma lucasanum* | 2376 | 4465 | native ×2 | Meer | 1 |
| 7 | *Arothron meleagris* | 2315 | 2765 | native ×1 | Meer | 1 |
| 8 | *Diodon holocanthus* | 1999 | 1962 | native ×1 | Meer | 1 |
| 9 | *Triaenodon obesus* | 1999 | 2212 | native ×2 | Meer | 1 |
| 10 | *Scarus ghobban* | 1954 | 3133 | native ×1 | Brack/Meer | 1 |
| 11 | *Lepidochelys olivacea* | 1555 | 1648 | native ×1 | Meer | – |
| 12 | *Ophioblennius steindachneri* | 1289 | 3128 | native ×1 | Meer | 1 |
| 13 | *Microspathodon dorsalis* | 1281 | 1707 | native ×2 | Meer | 1 |
| 14 | *Sphoeroides annulatus* | 1240 | 1794 | native ×1 | Brack/Meer | 1 |
| 15 | *Johnrandallia nigrirostris* | 1109 | 2955 | native ×2 | Meer | 1 |
| 16 | *Epinephelus labriformis* | 1067 | 3626 | native ×1 | Meer | 1 |
| 17 | *Cephalopholis colonus* | 1034 | 2028 | native ×2 | Meer | 1 |
| 18 | *Cirrhitus rivulatus* | 1005 | 1868 | native ×1 | Meer | 1 |
| 19 | *Stegastes arcifrons* | 994 | 2068 | native ×2 | Meer | 1 |
| 20 | *Scarus rubroviolaceus* | 958 | 1636 | native ×2 | Meer | 1 |
| 21 | *Fistularia commersonii* | 873 | 1243 | native ×1 | Meer | 1 |
| 22 | *Sufflamen verres* | 859 | 2440 | native ×2 | Meer | 1 |
| 23 | *Balistes polylepis* | 836 | 1171 | native ×1 | Meer | 1 |
| 24 | *Carcharhinus limbatus* | 833 | 684 | native ×1 | Brack/Meer | 1 |
| 25 | *Acanthurus xanthopterus* | 821 | 1190 | native ×1 | Meer | 1 |
| 26 | *Zanclus cornutus* | 808 | 1549 | native ×2 | Meer | 1 |
| 27 | *Lutjanus argentiventris* | 807 | 1629 | native ×2 | Brack/Meer | 1 |
| 28 | *Cirrhitichthys oxycephalus* | 770 | 2277 | native ×1 | Meer | 1 |
| 29 | *Stegastes beebei* | 762 | 2700 | native ×2 | Meer | 1 |
| 30 | *Stegastes acapulcoensis* | 757 | 691 | native ×2 | Meer | 1 |
| 31 | *Canthigaster punctatissima* | 732 | 1270 | native ×1 | Meer | 1 |
| 32 | *Eretmochelys imbricata* | 724 | 607 | native ×1 | Brack/Meer | – |
| 33 | *Chaetodon humeralis* | 694 | 1141 | native ×1 | Meer | 1 |
| 34 | *Aetobatus ocellatus* | 691 | 475 | – | Brack/Meer | 1 |
| 35 | *Halichoeres nicholsi* | 673 | 1752 | native ×1 | Meer | 1 |
| 36 | *Lutjanus viridis* | 663 | 1760 | native ×2 | Meer | 1 |
| 37 | *Hypanus dipterurus* | 655 | 814 | native ×1 | Meer | 1 |
| 38 | *Diodon hystrix* | 624 | 652 | native ×1 | Meer | 1 |
| 39 | *Azurina atrilobata* | 599 | 1489 | native ×2 | Meer | 1 |
| 40 | *Halichoeres dispilus* | 580 | 2588 | native ×1 | Meer | 1 |
| 44 | *Sphyrna lewini* (Highlight) | 557 | 1052 | native ×1 | Brack/Meer | 1 |
| 66 | *Rhincodon typus* (Highlight) | 349 | 930 | native ×2 | Meer | 1 |
| 64 | *Mobula birostris* (Highlight) | 351 | 387 | native ×2 | Meer | 1 |
| 74 | *Carcharhinus galapagensis* (Highlight) | 323 | 539 | native ×2 | Meer | 1 |
| 88 | *Mobula munkiana* (Highlight) | 249 | 213 | native ×1 | Meer | 1 |
| – | *Mola mola* (Highlight) | 4 | 39 | native ×1 | Meer | 1 |
| – | *Odontaspis ferox* (Highlight) | – | 9 | native ×2 | Meer | 1 |
| – | *Amblyrhynchus cristatus* (Highlight) | – | – | endemic ×1 | Meer | – |
| – | *Zalophus wollebaeki* (Highlight) | – | – | native ×1, stray ×1 | Meer | – |

### Level 2 (60)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Führer |
|---|---|---|---|---|---|---|
| 41 | *Cephalopholis panamensis* | 572 | 1378 | native ×1 | Meer | 1 |
| 42 | *Mulloidichthys dentatus* | 563 | 945 | native ×1 | Meer | 1 |
| 43 | *Scorpaena mystes* | 563 | 1140 | native ×2 | Meer | 1 |
| 45 | *Caranx sexfasciatus* | 553 | 589 | native ×1 | Süß/Brack/Meer | 1 |
| 46 | *Arothron hispidus* | 548 | 727 | native ×1 | Brack/Meer | 1 |
| 47 | *Muraena lentiginosa* | 526 | 998 | native ×1 | Meer | 1 |
| 48 | *Brachygenys jessiae* | 506 | 391 | endemic ×1 | Meer | 1 |
| 49 | *Thalassoma grammaticum* | 503 | 691 | native ×2 | Meer | 1 |
| 50 | *Haemulon sexfasciatum* | 499 | 515 | native ×1 | Meer | 1 |
| 51 | *Serranus psittacinus* | 493 | 1519 | native ×1 | Meer | 1 |
| 52 | *Acanthurus nigricans* | 492 | 820 | native ×2 | Meer | 1 |
| 53 | *Gymnothorax castaneus* | 464 | 536 | native ×2 | Meer | 1 |
| 54 | *Gobioclinus dendriticus* | 455 | 415 | endemic ×1 | Meer | 1 |
| 55 | *Caranx melampygus* | 454 | 864 | native ×1 | Brack/Meer | 1 |
| 56 | *Acanthurus triostegus* | 448 | 568 | native ×2 | Meer | 1 |
| 57 | *Stegastes flavilatus* | 443 | 584 | native ×2 | Meer | 1 |
| 58 | *Rhinoptera steindachneri* | 435 | 368 | native ×1 | Meer | 1 |
| 59 | *Pomacanthus zonipectus* | 420 | 600 | native ×1 | Meer | 1 |
| 60 | *Hippocampus ingens* | 409 | 453 | native ×2 | Meer | 1 |
| 61 | *Abudefduf concolor* | 397 | 334 | native ×2 | Meer | 1 |
| 62 | *Bathygobius ramosus* | 395 | 553 | – | Meer | 1 |
| 63 | *Haemulon maculicauda* | 378 | 487 | native ×1 | Meer | 1 |
| 65 | *Ostracion meleagris* | 350 | 424 | native ×1 | Meer | 1 |
| 67 | *Scarus perrico* | 349 | 638 | native ×1 | Meer | 1 |
| 68 | *Pseudobalistes naufragium* | 342 | 392 | native ×1 | Meer | 1 |
| 69 | *Apogon atradorsatus* | 339 | 1523 | endemic ×1, native ×1 | Meer | 1 |
| 70 | *Lutjanus novemfasciatus* | 339 | 745 | native ×1 | Brack/Meer | 1 |
| 71 | *Trachinotus rhodopus* | 339 | 433 | native ×1 | Meer | 1 |
| 72 | *Mycteroperca rosacea* | 337 | 428 | – | Meer | 1 |
| 73 | *Halichoeres notospilus* | 325 | 481 | native ×1 | Meer | 1 |
| 75 | *Caranx caninus* | 322 | 312 | native ×1 | Brack/Meer | 1 |
| 76 | *Chilomycterus reticulatus* | 318 | 470 | native ×1 | Meer | 1 |
| 77 | *Gymnothorax dovii* | 299 | 869 | native ×2 | Meer | 1 |
| 78 | *Hoplopagrus guentherii* | 298 | 601 | native ×1 | Meer | 1 |
| 79 | *Myrichthys xysturus* | 293 | 279 | native ×1 | Meer | 1 |
| 80 | *Aulostomus chinensis* | 292 | 808 | native ×2 | Meer | 1 |
| 81 | *Bathygobius lineatus* | 289 | 749 | native ×1 | Meer | 1 |
| 82 | *Echidna nebulosa* | 289 | 330 | native ×1 | Meer | 1 |
| 83 | *Holacanthus clarionensis* | 274 | 290 | – | Meer | 1 |
| 84 | *Hypanus longus* | 271 | 250 | native ×1 | Meer | 1 |
| 85 | *Taeniurops meyeni* | 269 | 341 | native ×2 | Meer | 1 |
| 86 | *Octopus oculifer* | 257 | 388 | native ×1 | Meer | – |
| 87 | *Bodianus eclancheri* | 249 | 913 | native ×1 | Meer | 1 |
| 89 | *Sargocentron suborbitale* (Quelle: *Neoniphon suborbitalis*) | 245 | 584 | native ×2 | Meer | 1 |
| 90 | *Caranx caballus* | 241 | 658 | native ×1 | Brack/Meer | 1 |
| 91 | *Microspathodon bairdii* | 232 | 580 | native ×2 | Meer | 1 |
| 92 | *Dermatolepis dermatolepis* | 231 | 1620 | native ×2 | Meer | 1 |
| 93 | *Aetobatus laticeps* | 227 | 204 | native ×1 | Meer | 1 |
| 94 | *Mycteroperca olfax* | 218 | 3249 | native ×2 | Meer | 1 |
| 95 | *Kyphosus elegans* | 216 | 714 | native ×1 | Meer | 1 |
| 96 | *Lepidonectes corallicola* | 215 | 936 | endemic ×1 | Meer | 1 |
| 97 | *Stegastes rectifraenum* | 213 | 426 | – | Meer | 1 |
| 98 | *Mugil cephalus* | 210 | 515 | native ×1 | Süß/Brack/Meer | 1 |
| 99 | *Alphestes immaculatus* | 206 | 629 | native ×1 | Meer | 1 |
| 100 | *Malacoctenus sudensis* | 205 | 204 | – | Meer | 1 |
| 101 | *Anisotremus taeniatus* | 200 | 191 | – | Meer | 1 |
| 102 | *Haemulon scudderii* | 195 | 531 | native ×1 | Meer | 1 |
| 103 | *Plagiotremus azaleus* | 192 | 1706 | native ×1 | Meer | 1 |
| 104 | *Carcharhinus leucas* | 189 | 176 | – | Süß/Brack/Meer | 1 |
| 105 | *Melichthys niger* | 188 | 1023 | native ×2 | Meer | 1 |

### Level 3 (50)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Führer |
|---|---|---|---|---|---|---|
| 106 | *Urobatis pardalis* | 184 | 141 | – | Meer | 1 |
| 107 | *Kyphosus vaigiensis* | 181 | 424 | native ×1 | Meer | 1 |
| 108 | *Anisotremus espinozai* | 179 | 122 | native ×2 | Meer | 1 |
| 109 | *Novaculichthys taeniourus* | 175 | 352 | native ×1 | Meer | 1 |
| 110 | *Halichoeres chierchiae* | 173 | 240 | native ×1 | Meer | 1 |
| 111 | *Urobatis maculatus* | 169 | 292 | – | Meer | 1 |
| 112 | *Myripristis leiognathus* | 168 | 556 | native ×2 | Meer | 1 |
| 113 | *Forcipiger flavissimus* | 162 | 186 | native ×1 | Meer | 1 |
| 114 | *Acanthemblemaria hancocki* | 157 | 236 | – | Meer | 1 |
| 115 | *Echidna nocturna* | 156 | 238 | native ×2 | Meer | 1 |
| 116 | *Abudefduf declivifrons* | 155 | 174 | – | Meer | 1 |
| 117 | *Dialommus macrocephalus* | 152 | 196 | – | Meer | 1 |
| 118 | *Labrisomus xanti* | 150 | 435 | – | Meer | 1 |
| 119 | *Nematistius pectoralis* | 150 | 204 | native ×1 | Meer | 1 |
| 120 | *Sphoeroides lobatus* | 148 | 244 | native ×1 | Brack/Meer | 1 |
| 121 | *Paralabrax maculatofasciatus* | 146 | 521 | – | Meer | 1 |
| 122 | *Gymnomuraena zebra* | 142 | 253 | native ×1 | Meer | 1 |
| 123 | *Scomberomorus sierra* | 140 | 617 | native ×1 | Meer | 1 |
| 124 | *Synodus lacertinus* | 140 | 493 | native ×1 | Meer | 1 |
| 125 | *Gnathanodon speciosus* | 139 | 188 | native ×1 | Meer | 1 |
| 126 | *Urobatis halleri* | 133 | 374 | – | Meer | 1 |
| 127 | *Caranx lugubris* | 132 | 309 | native ×1 | Meer | 1 |
| 128 | *Lutjanus guttatus* | 132 | 323 | native ×1 | Meer | 1 |
| 129 | *Nicholsina denticulata* | 131 | 433 | native ×1 | Meer | 1 |
| 130 | *Scarus compressus* | 131 | 466 | native ×1 | Meer | 1 |
| 131 | *Lutjanus colorado* | 130 | 174 | – | Brack/Meer | 1 |
| 132 | *Oxycirrhites typus* | 128 | 218 | native ×1 | Meer | 1 |
| 133 | *Aluterus scriptus* | 126 | 234 | native ×1 | Meer | 1 |
| 134 | *Dajaus monticola* | 123 | 166 | native ×1 | Süß/Brack/Meer | 1 |
| 135 | *Kyphosus ocyurus* | 121 | 269 | native ×1 | Meer | 1 |
| 136 | *Urobatis concentricus* | 121 | 124 | – | Meer | 1 |
| 137 | *Dormitator latifrons* | 120 | 180 | native ×1 | Süß/Brack/Meer | 1 |
| 138 | *Anisotremus interruptus* | 118 | 434 | native ×1 | Meer | 1 |
| 139 | *Ctenochaetus marginatus* | 117 | 142 | native ×1 | Meer | 1 |
| 140 | *Heterodontus quoyi* | 116 | 255 | native ×1 | Meer | 1 |
| 141 | *Euthynnus lineatus* | 115 | 356 | native ×1 | Meer | 1 |
| 142 | *Octopus hubbsorum* | 115 | 111 | – | Meer | – |
| 143 | *Gymnothorax flavimarginatus* | 114 | 135 | native ×1 | Meer | 1 |
| 144 | *Stegastes redemptus* | 114 | 150 | – | Meer | 1 |
| 145 | *Girella freminvillii* | 113 | 758 | endemic ×1 | Meer | 1 |
| 146 | *Sphyraena idiastes* | 113 | 355 | native ×2 | Meer | 1 |
| 147 | *Bothus mancus* | 112 | 123 | native ×2 | Meer | 1 |
| 148 | *Coryphopterus urospilus* | 112 | 738 | native ×1 | Meer | 1 |
| 149 | *Elops affinis* | 109 | 147 | native ×1 | Brack/Meer | 1 |
| 150 | *Gerres simillimus* | 104 | 82 | native ×1 | Brack/Meer | 1 |
| 151 | *Myripristis berndti* | 104 | 195 | native ×2 | Meer | 1 |
| 152 | *Archosargus pourtalesii* | 103 | 183 | endemic ×1 | Meer | 1 |
| 153 | *Chromis alta* | 99 | 311 | native ×2 | Meer | 1 |
| 154 | *Elacatinus puncticulatus* | 97 | 257 | – | Meer | 1 |
| 155 | *Thunnus albacares* | 97 | 172 | native ×1 | Brack/Meer | 1 |

## Grenzfälle

Je 10 Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels sie nehmen (Highlights ab Level 2 übersprungen).

### Level 1/2

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Führer | Level |
|---|---|---|---|---|---|---|---|
| 31 | *Canthigaster punctatissima* | 732 | 1270 | native ×1 | Meer | 1 | 1 |
| 32 | *Eretmochelys imbricata* | 724 | 607 | native ×1 | Brack/Meer | – | 1 |
| 33 | *Chaetodon humeralis* | 694 | 1141 | native ×1 | Meer | 1 | 1 |
| 34 | *Aetobatus ocellatus* | 691 | 475 | – | Brack/Meer | 1 | 1 |
| 35 | *Halichoeres nicholsi* | 673 | 1752 | native ×1 | Meer | 1 | 1 |
| 36 | *Lutjanus viridis* | 663 | 1760 | native ×2 | Meer | 1 | 1 |
| 37 | *Hypanus dipterurus* | 655 | 814 | native ×1 | Meer | 1 | 1 |
| 38 | *Diodon hystrix* | 624 | 652 | native ×1 | Meer | 1 | 1 |
| 39 | *Azurina atrilobata* | 599 | 1489 | native ×2 | Meer | 1 | 1 |
| 40 | *Halichoeres dispilus* | 580 | 2588 | native ×1 | Meer | 1 | 1 |
| | **Grenze** | | | | | | |
| 41 | *Cephalopholis panamensis* | 572 | 1378 | native ×1 | Meer | 1 | 2 |
| 42 | *Mulloidichthys dentatus* | 563 | 945 | native ×1 | Meer | 1 | 2 |
| 43 | *Scorpaena mystes* | 563 | 1140 | native ×2 | Meer | 1 | 2 |
| 45 | *Caranx sexfasciatus* | 553 | 589 | native ×1 | Süß/Brack/Meer | 1 | 2 |
| 46 | *Arothron hispidus* | 548 | 727 | native ×1 | Brack/Meer | 1 | 2 |
| 47 | *Muraena lentiginosa* | 526 | 998 | native ×1 | Meer | 1 | 2 |
| 48 | *Brachygenys jessiae* | 506 | 391 | endemic ×1 | Meer | 1 | 2 |
| 49 | *Thalassoma grammaticum* | 503 | 691 | native ×2 | Meer | 1 | 2 |
| 50 | *Haemulon sexfasciatum* | 499 | 515 | native ×1 | Meer | 1 | 2 |
| 51 | *Serranus psittacinus* | 493 | 1519 | native ×1 | Meer | 1 | 2 |

### Level 2/3

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Führer | Level |
|---|---|---|---|---|---|---|---|
| 96 | *Lepidonectes corallicola* | 215 | 936 | endemic ×1 | Meer | 1 | 2 |
| 97 | *Stegastes rectifraenum* | 213 | 426 | – | Meer | 1 | 2 |
| 98 | *Mugil cephalus* | 210 | 515 | native ×1 | Süß/Brack/Meer | 1 | 2 |
| 99 | *Alphestes immaculatus* | 206 | 629 | native ×1 | Meer | 1 | 2 |
| 100 | *Malacoctenus sudensis* | 205 | 204 | – | Meer | 1 | 2 |
| 101 | *Anisotremus taeniatus* | 200 | 191 | – | Meer | 1 | 2 |
| 102 | *Haemulon scudderii* | 195 | 531 | native ×1 | Meer | 1 | 2 |
| 103 | *Plagiotremus azaleus* | 192 | 1706 | native ×1 | Meer | 1 | 2 |
| 104 | *Carcharhinus leucas* | 189 | 176 | – | Süß/Brack/Meer | 1 | 2 |
| 105 | *Melichthys niger* | 188 | 1023 | native ×2 | Meer | 1 | 2 |
| | **Grenze** | | | | | | |
| 106 | *Urobatis pardalis* | 184 | 141 | – | Meer | 1 | 3 |
| 107 | *Kyphosus vaigiensis* | 181 | 424 | native ×1 | Meer | 1 | 3 |
| 108 | *Anisotremus espinozai* | 179 | 122 | native ×2 | Meer | 1 | 3 |
| 109 | *Novaculichthys taeniourus* | 175 | 352 | native ×1 | Meer | 1 | 3 |
| 110 | *Halichoeres chierchiae* | 173 | 240 | native ×1 | Meer | 1 | 3 |
| 111 | *Urobatis maculatus* | 169 | 292 | – | Meer | 1 | 3 |
| 112 | *Myripristis leiognathus* | 168 | 556 | native ×2 | Meer | 1 | 3 |
| 113 | *Forcipiger flavissimus* | 162 | 186 | native ×1 | Meer | 1 | 3 |
| 114 | *Acanthemblemaria hancocki* | 157 | 236 | – | Meer | 1 | 3 |
| 115 | *Echidna nocturna* | 156 | 238 | native ×2 | Meer | 1 | 3 |

### Level 3/nicht im Deck

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Führer | Level |
|---|---|---|---|---|---|---|---|
| 146 | *Sphyraena idiastes* | 113 | 355 | native ×2 | Meer | 1 | 3 |
| 147 | *Bothus mancus* | 112 | 123 | native ×2 | Meer | 1 | 3 |
| 148 | *Coryphopterus urospilus* | 112 | 738 | native ×1 | Meer | 1 | 3 |
| 149 | *Elops affinis* | 109 | 147 | native ×1 | Brack/Meer | 1 | 3 |
| 150 | *Gerres simillimus* | 104 | 82 | native ×1 | Brack/Meer | 1 | 3 |
| 151 | *Myripristis berndti* | 104 | 195 | native ×2 | Meer | 1 | 3 |
| 152 | *Archosargus pourtalesii* | 103 | 183 | endemic ×1 | Meer | 1 | 3 |
| 153 | *Chromis alta* | 99 | 311 | native ×2 | Meer | 1 | 3 |
| 154 | *Elacatinus puncticulatus* | 97 | 257 | – | Meer | 1 | 3 |
| 155 | *Thunnus albacares* | 97 | 172 | native ×1 | Brack/Meer | 1 | 3 |
| | **Grenze** | | | | | | |
| 156 | *Chaetodipterus zonatus* | 94 | 212 | native ×1 | Meer | 1 | – |
| 157 | *Coryphaena hippurus* | 94 | 430 | native ×1 | Brack/Meer | 1 | – |
| 158 | *Narcine entemedor* | 94 | 157 | – | Meer | 1 | – |
| 159 | *Chanos chanos* | 90 | 468 | native ×1 | Süß/Brack/Meer | 1 | – |
| 160 | *Lythrypnus gilberti* | 89 | 679 | endemic ×1 | Meer | 1 | – |
| 161 | *Zapteryx exasperata* | 89 | 111 | – | Meer | 1 | – |
| 162 | *Sphoeroides rosenblatti* | 88 | 107 | – | Brack/Meer | 1 | – |
| 163 | *Styracura pacifica* | 88 | 85 | native ×1 | Meer | 1 | – |
| 164 | *Paralabrax albomaculatus* | 86 | 831 | endemic ×1 | Meer | 1 | – |
| 165 | *Seriola rivoliana* | 84 | 1139 | native ×1 | Meer | 1 | – |

## Abgleich mit Führern

### 1. Smithsonian: Shorefishes of the Tropical Eastern Pacific

- 1480 Namen, 1462 Arten aufgelöst, 17 Namen nicht aufgelöst
- Deck-Arten im Führer: 152/159
  - Level 1: 44/49
  - Level 2: 59/60
  - Level 3: 49/50
- Kandidaten im Führer, aber nicht im Deck: 278

**Im Deck, nicht im Führer** (Verdacht: Fehlbestimmung, falsch verortet oder Süßwasser):

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Führer | Level |
|---|---|---|---|---|---|---|---|
| 1 | *Chelonia mydas* | 4242 | 5246 | native ×1 | Meer | – | 1 |
| 11 | *Lepidochelys olivacea* | 1555 | 1648 | native ×1 | Meer | – | 1 |
| 32 | *Eretmochelys imbricata* | 724 | 607 | native ×1 | Brack/Meer | – | 1 |
| – | *Amblyrhynchus cristatus* (Highlight) | – | – | endemic ×1 | Meer | – | 1 |
| – | *Zalophus wollebaeki* (Highlight) | – | – | native ×1, stray ×1 | Meer | – | 1 |
| 86 | *Octopus oculifer* | 257 | 388 | native ×1 | Meer | – | 2 |
| 142 | *Octopus hubbsorum* | 115 | 111 | – | Meer | – | 3 |

**Im Führer und häufig, aber nicht im Deck** (Kandidaten; die 30 häufigsten):

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Führer |
|---|---|---|---|---|---|---|
| 156 | *Chaetodipterus zonatus* | 94 | 212 | native ×1 | Meer | 1 |
| 157 | *Coryphaena hippurus* | 94 | 430 | native ×1 | Brack/Meer | 1 |
| 158 | *Narcine entemedor* | 94 | 157 | – | Meer | 1 |
| 159 | *Chanos chanos* | 90 | 468 | native ×1 | Süß/Brack/Meer | 1 |
| 160 | *Lythrypnus gilberti* | 89 | 679 | endemic ×1 | Meer | 1 |
| 161 | *Zapteryx exasperata* | 89 | 111 | – | Meer | 1 |
| 162 | *Sphoeroides rosenblatti* | 88 | 107 | – | Brack/Meer | 1 |
| 163 | *Styracura pacifica* | 88 | 85 | native ×1 | Meer | 1 |
| 164 | *Paralabrax albomaculatus* | 86 | 831 | endemic ×1 | Meer | 1 |
| 165 | *Seriola rivoliana* | 84 | 1139 | native ×1 | Meer | 1 |
| 166 | *Trachinotus stilbe* | 84 | 170 | native ×1 | Meer | 1 |
| 167 | *Malacanthus brevirostris* | 83 | 108 | native ×1 | Meer | 1 |
| 168 | *Elagatis bipinnulata* | 81 | 672 | native ×1 | Meer | 1 |
| 169 | *Heteroconger klausewitzi* | 81 | 144 | endemic ×1 | Meer | 1 |
| 170 | *Anisotremus scapularis* | 80 | 680 | native ×1 | Meer | 1 |
| 171 | *Halichoeres discolor* | 80 | 99 | native ×1 | Meer | 1 |
| 172 | *Kuhlia mugil* | 80 | 272 | native ×2 | Brack/Meer | 1 |
| 173 | *Malacoctenus tetranemus* | 78 | 330 | native ×1 | Meer | 1 |
| 174 | *Malacoctenus zonogaster* | 78 | 217 | endemic ×1 | Meer | 1 |
| 175 | *Apogon pacificus* | 76 | 155 | native ×1 | Meer | 1 |
| 176 | *Carcharhinus albimarginatus* | 76 | 86 | native ×2 | Meer | 1 |
| 177 | *Stegastes leucorus* | 75 | 214 | – | Meer | 1 |
| 178 | *Heteropriacanthus carolinus* | 74 | – | native ×1 | Meer | 1 |
| 179 | *Nexilosus latifrons* | 74 | 150 | native ×1 | Meer | 1 |
| 180 | *Muraena clepsydra* | 73 | 154 | native ×1 | Meer | 1 |
| 181 | *Oplegnathus insignis* | 72 | 432 | native ×1 | Meer | 1 |
| 182 | *Xanthichthys mento* | 72 | 509 | native ×2 | Meer | 1 |
| 183 | *Calamus brachysomus* | 70 | 332 | native ×1 | Meer | 1 |
| 184 | *Iniistius pavo* | 70 | 101 | native ×1 | Meer | 1 |
| 185 | *Carcharhinus falciformis* | 68 | 272 | native ×2 | Meer | 1 |

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
| *Awaous banana* | 45 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
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
| *Fonchiiichthys uracanthus* | 12 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
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
| *Hypsophrys nematopus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
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
| *Oligoplites saurus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Opistognathus rhomaleus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paraclinus sini* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paraletharchus opercularis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paralichthys aestuarius* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Phallichthys amates* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pherallodiscus funebris* | 3 | Meer | zu wenige Nachweise (3 < 5) |
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
| *Lasiancistrus caucanus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
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
| *Isopisthus remifer* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
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
| *Sternopygus aequilabiatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
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
