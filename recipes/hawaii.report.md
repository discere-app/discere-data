# Bericht: Hawaii (`recipes/hawaii.json`)

Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.

- Referenz-DB: v3 (FishBase v26.06, SeaLifeBase v26.06)
- Salz/Süß: FishBase/SeaLifeBase v25.04 (species.parquet)
- iNaturalist: 544 Taxa (Seiten: 2)
- OBIS: 1606 Arten mit Nachweisen außer iNaturalist
- Bild: https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Reef_Triggerfish_1.JPG/330px-Reef_Triggerfish_1.JPG — Qyd, CC BY 2.5, https://commons.wikimedia.org/wiki/File:Reef_Triggerfish_1.JPG

## Gebiete

- iNaturalist: Hawaii, US (11), Northwestern Hawaiian Islands, US (141380)
- OBIS: Hawaii-Inseln mit den Nordwestlichen Hawaii-Inseln
- FishBase/SeaLifeBase-Verbreitung: 840B, 840:US-HI

## Übersicht

- Arten der Reihenfolge-Quelle, aufgelöst: 533; nicht aufgelöst: 6
- ausgeschlossen: 196
  - zu wenige Nachweise: 139
  - kein Meeresfisch: 39
  - zu klein: 13
  - von Hand ausgeschlossen: 3
  - nur tiefer als die Tauchgrenze: 2
- Kandidaten nach den Filtern: 337
- Deck: 155 Arten (Level 1: 45, Level 2: 60, Level 3: 50); Umfang laut Rezept 40/60/50 plus Highlights
- Highlights: 5 im Deck, 0 verworfen

## Zu entscheiden

Warnungen, keine Ausschlüsse: Jede Zeile wird im Rezept entschieden (`exclude` mit Grund, Level) oder bewusst belassen. Schwellen: `warnings` im Rezept.

| Art | Subdeck | Warnung | Zahlen |
|---|---|---|---|
| *Antennarius commerson* | level-2 | wenige Beobachter | 324 von 540 Beobachtungen von 2 Personen (60 %); 87 Beobachter insgesamt |
| *Gymnothorax melatremus* | level-2 | wenige Beobachter | 169 von 291 Beobachtungen von 2 Personen (58 %); 61 Beobachter insgesamt |

## Hinweise: Namen

Diese Arten führt das Deck nicht unter dem bevorzugten Namen der Referenz-DB, sondern unter dem der Quelle, bei iNaturalist unter dem, unter dem sie in der Region zählt. Nichts zu entscheiden: Die App löst jeden davon über die Synonyme der Referenz-DB zur selben Art auf.

| Name im Deck | Subdeck | Referenz-DB |
|---|---|---|
| *Mauritia mauritiana* | invertebrates | *Cypraea mauritiana* |
| *Pteraeolidia semperi* | invertebrates | *Pteraeolidia ianthina* |
| *Acanthaster solaris* | invertebrates | *Acanthaster planci* |
| *Stylocheilus striatus* | invertebrates | *Stylocheilus longicauda* |

## Verworfene Highlights

Keine.

## iNaturalist-Namen zugeordnet

Laut `recipes/inat_names.json`: iNaturalist nennt die Art anders als die Referenz-DB; die Zählung kommt zu der der Referenz-DB-Art.

| iNaturalist | Referenz-DB | iNat | Art | Beleg |
|---|---|---|---|---|
| *Acanthurus sandvicensis* | *Acanthurus triostegus* | 3647 | Abspaltung | https://www.inaturalist.org/taxon_changes/162767 |
| *Pinnoctopus ornatus* | *Callistoctopus ornatus* | 99 | Umbenennung | https://www.inaturalist.org/taxon_changes/172615 |
| *Filistriatus sexfilis* | *Polydactylus sexfilis* | 56 | Umbenennung | https://www.inaturalist.org/taxon_changes/165559 |
| *Pinnoctopus luteus* | *Callistoctopus luteus* | 4 | Umbenennung | https://www.inaturalist.org/taxon_changes/172616 |

## Von Hand ausgeschlossen

| Art | iNat | Grund |
|---|---|---|
| *Istiblennius zebra* | 1713 | Felsenspringer, lebt in Gezeitentümpeln und auf Felsen über der Brandung. |
| *Sarotherodon melanotheron* | 566 | Eingeführter Buntbarsch der Häfen, Kanäle und Brackwasserteiche. |
| *Chanos chanos* | 127 | Milchfisch der Lagunen, Fischteiche und Flussmündungen, keine Begegnung am Riff. |

## Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Mobula alfredi* | Der Riffmanta kommt vor Kona nachts ins Lampenlicht, einer der bekanntesten Tauchgänge der Welt. | 61 | Reihenfolge-Quelle, Verbreitung | Level 1 |
| *Monachus schauinslandi* (Rezept: *Neomonachus schauinslandi*) | Die Hawaii-Mönchsrobbe kommt nur hier vor und ist eine der seltensten Robben der Welt. | – | Verbreitung | Level 1 |
| *Galeocerdo cuvier* | Der Tigerhai ist der große Hai Hawaiis und wird vor Oahu und Maui regelmäßig gesehen. | 200 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Stenella longirostris* | Spinnerdelfine ruhen tagsüber in den Buchten der Kona-Küste. | – | Verbreitung | Level 1 |
| *Megaptera novaeangliae* | Buckelwale kalben im Winter zwischen Maui, Lanai und Molokai. | – | Verbreitung | Level 1 |

## Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS ohne iNaturalist oder Verbreitung): 152/155 (98 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 5: *Chaetodon fremblii*, *Kuhlia xenura*, *Plagiotremus goslinei*, *Canthigaster coronata*, *Pteropterus sphex*
- Arten ohne Volksnamen `de` in der Referenz-DB: 89/155 (57 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 2/155 (1 %)
- Familien ohne Volksnamen `de`: 9/44 (20 %): *Aetobatidae*, *Balaenopteridae*, *Cheloniidae*, *Delphinidae*, *Epinephelidae*, *Galeocerdonidae*, *Mobulidae*, *Octopodidae*, *Phocidae*
- Familien ohne Volksnamen `en`: 1/44 (2 %): *Phocidae*

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

- *Monachus schauinslandi*: Verbreitung
- *Stenella longirostris*: Verbreitung
- *Megaptera novaeangliae*: Verbreitung

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

- gleicher Volksname `de` „Lippfisch“: *Coris gaimard*, *Iniistius pavo*
- gleicher Volksname `de` „Meerbarbe“: *Mulloidichthys flavolineatus*, *Mulloidichthys vanicolensis*
- gleicher Volksname `en` „Hawaiian flagtail“: *Kuhlia xenura*, *Kuhlia sandvicensis*

## Deck

Spalten: Rang unter den Kandidaten, Zählung der Reihenfolge-Quelle (iNat), OBIS-Nachweise ohne den iNaturalist-Datensatz, Einträge der FishBase/SeaLifeBase-Verbreitung in den Rezept-Regionen (~~durchgestrichen~~: Eintrag sagt „nicht vorhanden“), Wasser laut FishBase/SeaLifeBase.

### Level 1 (45)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 1 | *Chelonia mydas* (6095 Beobachter) | 11604 | 450 | native ×2 | Meer |
| 2 | *Acanthurus triostegus* (1544 Beobachter) | 3647 | 5824 | native ×1 | Meer |
| 3 | *Zanclus cornutus* (1313 Beobachter) | 2647 | 2629 | native ×1 | Meer |
| 4 | *Thalassoma duperrey* (979 Beobachter) | 2609 | 31893 | native ×1 | Meer |
| 5 | *Zebrasoma flavescens* (1053 Beobachter) | 2516 | 5079 | native ×1 | Meer |
| 6 | *Acanthurus nigrofuscus* (724 Beobachter) | 2178 | 11546 | native ×1 | Meer |
| 7 | *Rhinecanthus rectangulus* (Quelle: *Rhinecanthus rectangulus × aculeatus*; 998 Beobachter) | 2177 | 1363 | native ×1 | Meer |
| 8 | *Abudefduf sordidus* (1011 Beobachter) | 2146 | 234 | native ×1 | Brack/Meer |
| 9 | *Naso lituratus* (880 Beobachter) | 2125 | 4239 | native ×1 | Meer |
| 10 | *Ostracion meleagris* (850 Beobachter) | 2108 | 520 | native ×1 | Meer |
| 11 | *Canthigaster jactator* (813 Beobachter) | 1988 | 6061 | native ×1 | Meer |
| 12 | *Mulloidichthys flavolineatus* (794 Beobachter) | 1797 | 1122 | native ×1 | Meer |
| 13 | *Chaetodon lunula* (853 Beobachter) | 1744 | 688 | native ×1 | Meer |
| 14 | *Gymnothorax meleagris* (558 Beobachter) | 1646 | 282 | native ×1 | Süß/Brack/Meer |
| 15 | *Chaetodon auriga* (825 Beobachter) | 1634 | 1120 | native ×1 | Meer |
| 16 | *Melichthys niger* (823 Beobachter) | 1513 | 2543 | native ×1 | Meer |
| 17 | *Acanthurus olivaceus* (684 Beobachter) | 1506 | 6683 | native ×1 | Meer |
| 18 | *Chaetodon ornatissimus* (627 Beobachter) | 1492 | 1926 | native ×1 | Meer |
| 19 | *Thalassoma trilobatum* (704 Beobachter) | 1487 | 661 | native ×1 | Meer |
| 20 | *Parupeneus multifasciatus* (650 Beobachter) | 1476 | 9884 | native ×1 | Meer |
| 21 | *Gomphosus varius* (577 Beobachter) | 1415 | 3818 | native ×1 | Meer |
| 22 | *Chaetodon quadrimaculatus* (652 Beobachter) | 1386 | 1345 | native ×1 | Meer |
| 23 | *Scarus rubroviolaceus* (581 Beobachter) | 1347 | 2868 | native ×1 | Meer |
| 24 | *Fistularia commersonii* (684 Beobachter) | 1316 | 359 | native ×1 | Meer |
| 25 | *Caranx melampygus* (623 Beobachter) | 1303 | 2964 | native ×1 | Brack/Meer |
| 26 | *Aulostomus chinensis* (586 Beobachter) | 1279 | 926 | native ×1 | Meer |
| 27 | *Coris gaimard* (475 Beobachter) | 1174 | 1529 | native ×1 | Meer |
| 28 | *Dascyllus albisella* (518 Beobachter) | 1142 | 2779 | native ×1 | Meer |
| 29 | *Naso unicornis* (473 Beobachter) | 1064 | 5610 | native ×1 | Meer |
| 30 | *Abudefduf vaigiensis* (603 Beobachter) | 1049 | 459 | native ×1 | Meer |
| 31 | *Ctenochaetus strigosus* (431 Beobachter) | 1043 | 13364 | native ×1 | Meer |
| 32 | *Scarus psittacus* (438 Beobachter) | 991 | 2386 | native ×1 | Meer |
| 33 | *Chlorurus spilurus* (387 Beobachter) | 978 | 7506 | native ×1 | Meer |
| 34 | *Zebrasoma velifer* (498 Beobachter) | 932 | 1197 | native ×1 | Meer |
| 35 | *Cirrhitus pinnulatus* (505 Beobachter) | 923 | 946 | native ×1 | Meer |
| 36 | *Octopus cyanea* (322 Beobachter) | 917 | 90 | native ×1 | Meer |
| 37 | *Acanthurus blochii* (467 Beobachter) | 914 | 1649 | native ×1 | Meer |
| 38 | *Melichthys vidua* (496 Beobachter) | 889 | 2111 | native ×1 | Meer |
| 39 | *Echidna nebulosa* (596 Beobachter) | 883 | 30 | native ×1 | Meer |
| 40 | *Sufflamen bursa* (358 Beobachter) | 871 | 4586 | native ×1 | Meer |
| 61 | *Mobula alfredi* (Highlight; 447 Beobachter) | 649 | – | native ×1 | Süß/Meer |
| – | *Monachus schauinslandi* (Highlight) | – | – | native ×1 | Meer |
| 200 | *Galeocerdo cuvier* (Highlight; 49 Beobachter) | 57 | 3 | native ×1 | Brack/Meer |
| – | *Stenella longirostris* (Highlight) | – | – | native ×1 | Meer |
| – | *Megaptera novaeangliae* (Highlight) | – | – | native ×1 | Meer |

### Level 2 (60)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 41 | *Gymnothorax flavimarginatus* (284 Beobachter) | 856 | 235 | native ×1 | Meer |
| 42 | *Abudefduf abdominalis* (Quelle: *Abudefduf abdominalis × vaigiensis*; 441 Beobachter) | 847 | 1250 | native ×1 | Meer |
| 43 | *Gymnothorax eurostus* (252 Beobachter) | 830 | 179 | native ×1 | Meer |
| 44 | *Cephalopholis argus* (419 Beobachter) | 812 | 2335 | introduced ×1 | Meer |
| 45 | *Acanthurus leucopareius* (415 Beobachter) | 810 | 3384 | native ×1 | Meer |
| 46 | *Stethojulis balteata* (293 Beobachter) | 778 | 8892 | native ×1 | Meer |
| 47 | *Paracirrhites arcatus* (317 Beobachter) | 775 | 9039 | native ×1 | Meer |
| 48 | *Rhinecanthus aculeatus* (461 Beobachter) | 773 | 59 | native ×1 | Meer |
| 49 | *Paracirrhites forsteri* (345 Beobachter) | 755 | 1795 | native ×1 | Meer |
| 50 | *Cantherhines dumerilii* (391 Beobachter) | 750 | 416 | native ×1 | Meer |
| 51 | *Plectroglyphidodon marginatus* (351 Beobachter) | 712 | 10349 | native ×1 | Meer |
| 52 | *Gymnothorax pictus* (481 Beobachter) | 704 | 12 | native ×1 | Brack/Meer |
| 53 | *Diodon hystrix* (417 Beobachter) | 702 | 105 | native ×1 | Meer |
| 54 | *Forcipiger flavissimus* (304 Beobachter) | 682 | 1700 | native ×1 | Meer |
| 55 | *Labroides phthirophagus* (313 Beobachter) | 665 | 2952 | native ×1 | Meer |
| 56 | *Mulloidichthys vanicolensis* (273 Beobachter) | 665 | 665 | native ×1 | Meer |
| 57 | *Lutjanus kasmira* (333 Beobachter) | 664 | 2401 | introduced ×1 | Meer |
| 58 | *Arothron meleagris* (339 Beobachter) | 657 | 46 | native ×1 | Meer |
| 59 | *Novaculichthys taeniourus* (306 Beobachter) | 654 | 243 | native ×1 | Meer |
| 60 | *Plectroglyphidodon imparipennis* (385 Beobachter) | 651 | 2443 | native ×1 | Meer |
| 62 | *Calotomus carolinus* (292 Beobachter) | 647 | 723 | native ×1 | Meer |
| 63 | *Canthigaster amboinensis* (339 Beobachter) | 636 | 455 | native ×1 | Meer |
| 64 | *Chaetodon unimaculatus* (244 Beobachter) | 579 | 485 | native ×1 | Meer |
| 65 | *Chaetodon miliaris* (257 Beobachter) | 573 | 3551 | native ×1 | Meer |
| 66 | *Lutjanus fulvus* (326 Beobachter) | 569 | 960 | introduced ×1 | Süß/Brack/Meer |
| 67 | *Chaetodon multicinctus* (226 Beobachter) | 563 | 3960 | native ×1 | Meer |
| 68 | *Acanthurus xanthopterus* (328 Beobachter) | 543 | 186 | native ×1 | Meer |
| 69 | *Antennarius commerson* (87 Beobachter) | 540 | 6 | native ×1 | Meer |
| 70 | *Bathygobius coalitus* (291 Beobachter) | 506 | 36 | native ×1 | Meer |
| 71 | *Kyphosus cinerascens* (282 Beobachter) | 504 | 170 | native ×1 | Meer |
| 72 | *Arothron hispidus* (340 Beobachter) | 503 | 79 | native ×1 | Brack/Meer |
| 73 | *Triaenodon obesus* (191 Beobachter) | 497 | 699 | native ×1 | Meer |
| 74 | *Taenianotus triacanthus* (84 Beobachter) | 496 | 42 | native ×1 | Meer |
| 75 | *Acanthurus guttatus* (274 Beobachter) | 480 | 95 | native ×1 | Meer |
| 76 | *Acanthurus achilles* (Quelle: *Acanthurus achilles × nigricans*; 260 Beobachter) | 467 | 579 | native ×1 | Meer |
| 77 | *Gymnothorax undulatus* (190 Beobachter) | 460 | 84 | native ×1 | Brack/Meer |
| 78 | *Monotaxis grandoculis* (206 Beobachter) | 458 | 2361 | native ×1 | Meer |
| 79 | *Aetobatus ocellatus* (295 Beobachter) | 444 | 43 | native ×1 | Brack/Meer |
| 80 | *Gymnomuraena zebra* (238 Beobachter) | 419 | 16 | native ×1 | Meer |
| 81 | *Chaetodon lunulatus* (196 Beobachter) | 408 | 393 | native ×1 | Meer |
| 82 | *Chaetodon ephippium* (239 Beobachter) | 406 | 45 | native ×1 | Meer |
| 83 | *Exallias brevis* (142 Beobachter) | 406 | 337 | native ×1 | Meer |
| 84 | *Anampses cuvier* (180 Beobachter) | 378 | 1572 | native ×1 | Meer |
| 85 | *Parupeneus cyclostomus* (176 Beobachter) | 364 | 1449 | native ×1 | Meer |
| 86 | *Sphyraena barracuda* (233 Beobachter) | 353 | 101 | native ×1 | Brack/Meer |
| 87 | *Chaetodon fremblii* (176 Beobachter) | 352 | 2637 | endemic ×1 | Meer |
| 88 | *Halichoeres ornatissimus* (106 Beobachter) | 348 | 4832 | native ×1 | Meer |
| 89 | *Kyphosus vaigiensis* (218 Beobachter) | 339 | 300 | native ×1 | Meer |
| 90 | *Blenniella gibbifrons* (195 Beobachter) | 337 | 41 | native ×1 | Meer |
| 91 | *Acanthurus dussumieri* (182 Beobachter) | 336 | 1834 | native ×1 | Meer |
| 92 | *Parupeneus insularis* (183 Beobachter) | 334 | 991 | native ×1 | Meer |
| 93 | *Cirrhitops fasciatus* (139 Beobachter) | 331 | 2359 | native ×1 | Meer |
| 94 | *Pycnochromis vanderbilti* (120 Beobachter) | 328 | 8071 | native ×1 | Meer |
| 95 | *Kuhlia xenura* (210 Beobachter) | 318 | 7 | endemic ×1 | Süß/Brack/Meer |
| 96 | *Pristiapogon kallopterus* (130 Beobachter) | 310 | 450 | native ×1 | Brack/Meer |
| 97 | *Neochirus barberi* (53 Beobachter) | 304 | 86 | native ×1 | Meer |
| 98 | *Diodon holocanthus* (154 Beobachter) | 297 | 47 | native ×1 | Meer |
| 99 | *Platybelone platyura* (201 Beobachter) | 295 | 22 | native ×1 | Meer |
| 100 | *Gymnothorax melatremus* (61 Beobachter) | 291 | 61 | native ×1 | Meer |
| 101 | *Bodianus albotaeniatus* (106 Beobachter) | 290 | 8401 | native ×1 | Meer |

### Level 3 (50)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 102 | *Scorpaenopsis diabolus* | 275 | 57 | native ×1 | Meer |
| 103 | *Thalassoma purpureum* | 258 | 1001 | native ×1 | Meer |
| 104 | *Kuhlia sandvicensis* | 256 | 90 | native ×1 | Süß/Brack/Meer |
| 105 | *Myripristis kuntee* | 245 | 609 | native ×1 | Meer |
| 106 | *Plagiotremus goslinei* | 244 | 1182 | endemic ×1 | Meer |
| 107 | *Centropyge potteri* | 238 | 5671 | native ×1 | Meer |
| 108 | *Neoniphon sammara* | 236 | 603 | native ×1 | Meer |
| 109 | *Canthigaster coronata* | 230 | 760 | endemic ×1 | Meer |
| 110 | *Bothus mancus* | 225 | 22 | native ×1 | Meer |
| 111 | *Neomyxus leuciscus* | 221 | 34 | native ×1 | Brack/Meer |
| 112 | *Aluterus scriptus* | 218 | 51 | native ×1 | Meer |
| 113 | *Forcipiger longirostris* | 216 | 302 | native ×1 | Meer |
| 114 | *Gymnothorax rueppelliae* | 210 | 25 | native ×1 | Brack/Meer |
| 115 | *Macropharyngodon geoffroy* | 207 | 4212 | native ×1 | Meer |
| 116 | *Plectroglyphidodon johnstonianus* | 201 | 5810 | native ×1 | Meer |
| 117 | *Sargocentron punctatissimum* | 201 | 96 | native ×1 | Meer |
| 118 | *Coris venusta* | 200 | 5939 | native ×1 | Meer |
| 119 | *Chaetodon lineolatus* | 198 | 25 | native ×1 | Meer |
| 120 | *Oxycheilinus unifasciatus* | 196 | 2845 | native ×1 | Meer |
| 121 | *Scomberoides lysan* | 193 | 150 | native ×1 | Brack/Meer |
| 122 | *Pycnochromis pacifica* | 192 | – | native ×1 | Meer |
| 123 | *Heniochus diphreutes* | 176 | 283 | native ×1 | Meer |
| 124 | *Naso brevirostris* | 174 | 1400 | native ×1 | Meer |
| 125 | *Dactyloptena orientalis* | 169 | 95 | native ×1 | Meer |
| 126 | *Hemitaurichthys polylepis* | 168 | 88 | native ×1 | Meer |
| 127 | *Bothus pantherinus* | 166 | 74 | native ×1 | Meer |
| 128 | *Myripristis berndti* | 162 | 1146 | native ×1 | Meer |
| 129 | *Cheilio inermis* | 161 | 126 | native ×1 | Meer |
| 130 | *Coris flavovittata* | 160 | 1409 | native ×1 | Meer |
| 131 | *Chaetodon kleinii* | 158 | 1075 | native ×1 | Meer |
| 132 | *Cirripectes vanderbilti* | 158 | 1416 | native ×1 | Meer |
| 133 | *Iniistius pavo* | 155 | 66 | native ×1 | Meer |
| 134 | *Parupeneus porphyreus* | 155 | 334 | native ×1 | Meer |
| 135 | *Pseudocheilinus octotaenia* | 150 | 1906 | native ×1 | Meer |
| 136 | *Mugil cephalus* | 147 | 38 | native ×1 | Süß/Brack/Meer |
| 137 | *Antennatus tuberosus* | 145 | 15 | native ×1 | Meer |
| 138 | *Cantherhines sandwichiensis* | 144 | 530 | native ×1 | Meer |
| 139 | *Caranx ignobilis* | 141 | 3920 | native ×1 | Brack/Meer |
| 140 | *Sufflamen fraenatum* | 141 | 2076 | native ×1 | Meer |
| 141 | *Tylosurus crocodilus* | 140 | 51 | native ×1 | Meer |
| 142 | *Lactoria fornasini* | 139 | 130 | native ×1 | Meer |
| 143 | *Acanthurus nigricans* | 134 | 145 | native ×1 | Meer |
| 144 | *Sebastapistes coniorta* | 133 | 172 | native ×1 | Meer |
| 145 | *Carcharhinus galapagensis* | 130 | 750 | native ×1 | Meer |
| 146 | *Echidna polyzona* | 127 | 31 | native ×1 | Meer |
| 147 | *Conger marginatus* | 121 | 34 | native ×1 | Meer |
| 148 | *Pteropterus sphex* | 120 | 63 | endemic ×1 | Meer |
| 149 | *Ctenochaetus hawaiiensis* | 118 | 543 | native ×1 | Meer |
| 150 | *Heteropriacanthus carolinus* | 118 | – | native ×1 | Meer |
| 151 | *Acanthurus nigroris* | 114 | 6600 | native ×1 | ? |

## Grenzfälle

Je 10 Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels sie nehmen (Highlights ab Level 2 übersprungen).

### Level 1/2

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 31 | *Ctenochaetus strigosus* (431 Beobachter) | 1043 | 13364 | native ×1 | Meer | 1 |
| 32 | *Scarus psittacus* (438 Beobachter) | 991 | 2386 | native ×1 | Meer | 1 |
| 33 | *Chlorurus spilurus* (387 Beobachter) | 978 | 7506 | native ×1 | Meer | 1 |
| 34 | *Zebrasoma velifer* (498 Beobachter) | 932 | 1197 | native ×1 | Meer | 1 |
| 35 | *Cirrhitus pinnulatus* (505 Beobachter) | 923 | 946 | native ×1 | Meer | 1 |
| 36 | *Octopus cyanea* (322 Beobachter) | 917 | 90 | native ×1 | Meer | 1 |
| 37 | *Acanthurus blochii* (467 Beobachter) | 914 | 1649 | native ×1 | Meer | 1 |
| 38 | *Melichthys vidua* (496 Beobachter) | 889 | 2111 | native ×1 | Meer | 1 |
| 39 | *Echidna nebulosa* (596 Beobachter) | 883 | 30 | native ×1 | Meer | 1 |
| 40 | *Sufflamen bursa* (358 Beobachter) | 871 | 4586 | native ×1 | Meer | 1 |
| | **Grenze** | | | | | |
| 41 | *Gymnothorax flavimarginatus* (284 Beobachter) | 856 | 235 | native ×1 | Meer | 2 |
| 42 | *Abudefduf abdominalis* (Quelle: *Abudefduf abdominalis × vaigiensis*; 441 Beobachter) | 847 | 1250 | native ×1 | Meer | 2 |
| 43 | *Gymnothorax eurostus* (252 Beobachter) | 830 | 179 | native ×1 | Meer | 2 |
| 44 | *Cephalopholis argus* (419 Beobachter) | 812 | 2335 | introduced ×1 | Meer | 2 |
| 45 | *Acanthurus leucopareius* (415 Beobachter) | 810 | 3384 | native ×1 | Meer | 2 |
| 46 | *Stethojulis balteata* (293 Beobachter) | 778 | 8892 | native ×1 | Meer | 2 |
| 47 | *Paracirrhites arcatus* (317 Beobachter) | 775 | 9039 | native ×1 | Meer | 2 |
| 48 | *Rhinecanthus aculeatus* (461 Beobachter) | 773 | 59 | native ×1 | Meer | 2 |
| 49 | *Paracirrhites forsteri* (345 Beobachter) | 755 | 1795 | native ×1 | Meer | 2 |
| 50 | *Cantherhines dumerilii* (391 Beobachter) | 750 | 416 | native ×1 | Meer | 2 |

### Level 2/3

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 92 | *Parupeneus insularis* (183 Beobachter) | 334 | 991 | native ×1 | Meer | 2 |
| 93 | *Cirrhitops fasciatus* (139 Beobachter) | 331 | 2359 | native ×1 | Meer | 2 |
| 94 | *Pycnochromis vanderbilti* (120 Beobachter) | 328 | 8071 | native ×1 | Meer | 2 |
| 95 | *Kuhlia xenura* (210 Beobachter) | 318 | 7 | endemic ×1 | Süß/Brack/Meer | 2 |
| 96 | *Pristiapogon kallopterus* (130 Beobachter) | 310 | 450 | native ×1 | Brack/Meer | 2 |
| 97 | *Neochirus barberi* (53 Beobachter) | 304 | 86 | native ×1 | Meer | 2 |
| 98 | *Diodon holocanthus* (154 Beobachter) | 297 | 47 | native ×1 | Meer | 2 |
| 99 | *Platybelone platyura* (201 Beobachter) | 295 | 22 | native ×1 | Meer | 2 |
| 100 | *Gymnothorax melatremus* (61 Beobachter) | 291 | 61 | native ×1 | Meer | 2 |
| 101 | *Bodianus albotaeniatus* (106 Beobachter) | 290 | 8401 | native ×1 | Meer | 2 |
| | **Grenze** | | | | | |
| 102 | *Scorpaenopsis diabolus* | 275 | 57 | native ×1 | Meer | 3 |
| 103 | *Thalassoma purpureum* | 258 | 1001 | native ×1 | Meer | 3 |
| 104 | *Kuhlia sandvicensis* | 256 | 90 | native ×1 | Süß/Brack/Meer | 3 |
| 105 | *Myripristis kuntee* | 245 | 609 | native ×1 | Meer | 3 |
| 106 | *Plagiotremus goslinei* | 244 | 1182 | endemic ×1 | Meer | 3 |
| 107 | *Centropyge potteri* | 238 | 5671 | native ×1 | Meer | 3 |
| 108 | *Neoniphon sammara* | 236 | 603 | native ×1 | Meer | 3 |
| 109 | *Canthigaster coronata* | 230 | 760 | endemic ×1 | Meer | 3 |
| 110 | *Bothus mancus* | 225 | 22 | native ×1 | Meer | 3 |
| 111 | *Neomyxus leuciscus* | 221 | 34 | native ×1 | Brack/Meer | 3 |

### Level 3/nicht im Deck

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 142 | *Lactoria fornasini* | 139 | 130 | native ×1 | Meer | 3 |
| 143 | *Acanthurus nigricans* | 134 | 145 | native ×1 | Meer | 3 |
| 144 | *Sebastapistes coniorta* | 133 | 172 | native ×1 | Meer | 3 |
| 145 | *Carcharhinus galapagensis* | 130 | 750 | native ×1 | Meer | 3 |
| 146 | *Echidna polyzona* | 127 | 31 | native ×1 | Meer | 3 |
| 147 | *Conger marginatus* | 121 | 34 | native ×1 | Meer | 3 |
| 148 | *Pteropterus sphex* | 120 | 63 | endemic ×1 | Meer | 3 |
| 149 | *Ctenochaetus hawaiiensis* | 118 | 543 | native ×1 | Meer | 3 |
| 150 | *Heteropriacanthus carolinus* | 118 | – | native ×1 | Meer | 3 |
| 151 | *Acanthurus nigroris* | 114 | 6600 | native ×1 | ? | 3 |
| | **Grenze** | | | | | |
| 152 | *Chromis ovalis* | 113 | 2999 | native ×1 | Meer | – |
| 153 | *Eretmochelys imbricata* | 113 | 6 | native ×1 | Brack/Meer | – |
| 154 | *Xanthichthys auromarginatus* | 112 | 225 | native ×1 | Meer | – |
| 155 | *Pseudojuloides cerasinus* | 111 | 1244 | native ×1 | Meer | – |
| 156 | *Sepioteuthis lessoniana* | 108 | 5 | native ×1 | Brack/Meer | – |
| 157 | *Pycnochromis hanui* | 106 | 5135 | endemic ×1 | Meer | – |
| 158 | *Decapterus macarellus* | 104 | 422 | native ×1 | Meer | – |
| 159 | *Scorpaenopsis cacopsis* | 103 | 19 | native ×1 | Meer | – |
| 160 | *Oxycheilinus bimaculatus* | 100 | 2668 | native ×1 | Meer | – |
| 161 | *Callistoctopus ornatus* | 99 | – | native ×1 | Meer | – |

## Abgleich mit Führern

Das Rezept nennt keinen Führer.
## Änderungen gegenüber dem bestehenden Deck

- neu: 6: *Acanthurus nigroris*, *Ctenochaetus hawaiiensis*, *Heteropriacanthus carolinus*, *Mithrodia fisheri*, *Tambja morosa*, *Thorunna daniellae*
- entfallen: 6: *Calcinus seurati*, *Chanos chanos*, *Colobocentrotus atratus*, *Istiblennius zebra*, *Physalia utriculus*, *Sarotherodon melanotheron*

## Ausgeschlossene Kandidaten

<details><summary>196 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Istiblennius zebra* | 1713 | Meer | von Hand ausgeschlossen (Felsenspringer, lebt in Gezeitentümpeln und auf Felsen über der Brandung.) |
| *Sarotherodon melanotheron* | 566 | Süß/Brack/Meer | von Hand ausgeschlossen (Eingeführter Buntbarsch der Häfen, Kanäle und Brackwasserteiche.) |
| *Oreochromis mossambicus* | 375 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Awaous stamineus* | 164 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia reticulata* | 146 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bryaninops yongei* | 134 | Meer | zu klein (höchstens 3.5 cm) |
| *Chanos chanos* | 127 | Süß/Brack/Meer | von Hand ausgeschlossen (Milchfisch der Lagunen, Fischteiche und Flussmündungen, keine Begegnung am Riff.) |
| *Enneapterygius atriceps* | 97 | Meer | zu klein (höchstens 2.6 cm) |
| *Eleotris sandwicensis* | 83 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Kelloggella oligolepis* | 82 | Meer | zu klein (höchstens 1.8 cm) |
| *Stenogobius hawaiiensis* | 70 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amatitlania nigrofasciata* | 60 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hemichromis camerounensis* | 60 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Xiphophorus hellerii* | 58 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Caracanthus typicus* | 52 | Meer | zu klein (höchstens 2.9 cm) |
| *Gambusia affinis* | 50 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota epiphanes* | 43 | Meer | zu klein (höchstens 1.41 cm) |
| *Coptodon rendalli* | 39 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma unisquame* | 35 | Meer | zu klein (höchstens 2.6 cm) |
| *Amphilophus labiatus* | 34 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Psilogobius mainlandi* | 33 | Meer | zu klein (höchstens 3.7 cm) |
| *Lentipes concolor* | 29 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Amphilophus citrinellus* | 26 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Clarias fuscus* | 24 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Micropterus dolomieu* | 22 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Alectis ciliaris* | 20 | Meer | nur tiefer als die Tauchgrenze (erst ab 60 m) |
| *Cichla ocellaris* | 20 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parachromis managuensis* | 17 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Euprymna scolopes* | 16 | Meer | zu klein (höchstens 3 cm) |
| *Synchiropus rosulentus* | 16 | Meer | zu klein (höchstens 2.15 cm) |
| *Trimma taylori* | 15 | Meer | zu klein (höchstens 3.5 cm) |
| *Tanichthys albonubes* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota susanae* | 8 | Meer | zu klein (höchstens 1.85 cm) |
| *Lepomis macrochirus* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Carassius auratus* | 7 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Coptodon zillii* | 7 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Callionymus corallinus* | 7 | Meer | zu klein (höchstens 3.71 cm) |
| *Cyprinus carpio* | 6 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Misgurnus anguillicaudatus* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pleurosicya larsonae* | 5 | Meer | zu klein (höchstens 1.95 cm) |
| *Torquigener florealis* | 5 | Meer | nur tiefer als die Tauchgrenze (erst ab 90 m) |
| *Antennarius striatus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Callistoctopus luteus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cyprinus rubrofuscus* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Echeneis naucrates* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Gymnothorax berndti* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Myrichthys colubrinus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Naucrates ductor* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Novaculops woodi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Remora remora* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sthenoteuthis oualaniensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ablennes hians* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Antennarius maculatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Callionymus comptus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Centropyge interrupta* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chaetodon trifascialis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gymnothorax nuttingi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hypanus dipterurus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hyporthodus quernus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hypsophrys nicaraguensis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Luzonichthys earlei* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Odontanthias fuscipinnis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Oncorhynchus mykiss* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Ophichthus fowleri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Oreochromis niloticus* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pleurosicya micheli* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Seriola lalandi* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Squalus hawaiiensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Synodus capricornis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Synodus rubromarmoratus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Xenentodon cancila* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Albula virgata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Andinoacara rivulatus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Argonauta argo* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Aseraggodes borehami* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Astronotus ocellatus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bodianus sanguineus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bryaninops tigris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Caranx caballus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Caretta caretta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chitala ornata* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Crystallodytes cookei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ctenopharyngodon idella* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Encheliophis gracilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epibulus insidiator* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Etelis carbunculus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnothorax albimarginatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hippocampus fisheri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ictalurus punctatus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Iniistius baldwini* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Leiuranus semicinctus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Nomeus gronovii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Octopus bocki* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ommastrephes bartramii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Osteogaster aenea* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oxyurichthys lonchotus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Petroscirtes breviceps* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Pleurosicya mossambica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Poecilia latipinna* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Polymixia berndti* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pristipomoides filamentosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pristipomoides zonatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudocaranx cheilio* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Pycnochromis leucurus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ranzania laevis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sargocentron ensifer* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scorpaenodes evides* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Synodus lobeli* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Thysanoteuthis rhombus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tremoctopus gracilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Uraspis helvola* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Xanthichthys caeruleolineatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Xenanthias nanus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Abantennarius drombus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acanthurus lineatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ammolabrus dicrus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ancistrocheirus lesueurii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Antennatus linearis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Antigonia capros* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aphareus rutilans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Apogon deetsie* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Apterichtus flavicaudus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Apterichtus klazingai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aulotrachichthys heptalepis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Benthosema fibulatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Canthidermis maculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Caprodon unicolor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carcharhinus falciformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carcharodon carcharias* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Centropyge nahackyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheilopogon cyanopterus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheilopogon pinnatibarbatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheilopogon spilonotopterus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chrionema chryseres* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chrysiptera cyanea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirrhilabrus jordani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirrhimuraena playfairii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Colossoma macropomum* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cosmocampus balli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ctenochaetus striatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diceratias pileatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Draculo pogognathus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Encrasicholina punctifer* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Engyprosopon hawaiiense* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Etelis coruscans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eurypegasus papilio* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eviota rubra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Evistias acutirostris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax nudivomer* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hemichromis elongatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hyaloteuthis pelagica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Kajikia audax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lachneratus phasmaticus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lagocephalus lagocephalus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lepidochelys olivacea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lepomis cyanellus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia vittata* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Limnichthys nitidus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Liopropoma aurora* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lutjanus gibbus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mobula tarapacana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mugilogobius cavifrons* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Myripristis murdjan* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Myripristis vittata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Naso brachycentron* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Osteoglossum bicirrhosum* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parupeneus chrysonemus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phtheirichthys lineatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Physiculus sterops* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plectrypops lima* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Poecilia sphenops* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pomacanthus imperator* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pontinus macrocephalus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pristilepis oligolepis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pristipomoides sieboldii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Promethichthys prometheus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudamiops diaphanes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Remora australis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhinopias xenops* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rondeletia loricata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ruvettus pretiosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sargocentron iota* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scarus ghobban* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Scorpaena colorata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scorpaenodes guamensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scuticaria okinawae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sphoeroides pachygaster* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sphyraena qenie* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synaphobranchus kaupii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tetrapturus angustirostris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thalassoma hardwicke* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thunnus obesus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trimma milta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tylosurus pacificus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ventrifossa atherodon* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Zebrasoma rostratum* | 1 | Meer | zu wenige Nachweise (1 < 5) |

</details>

## Subdeck `invertebrates` (40)

Eigene Taxa, Größe und Filter, Reihenfolge-Quelle und Region des Rezepts. Arten, die schon in einem Level oder einem früheren Subdeck stehen, bleiben draußen; die Führer werden nicht abgeglichen.

- iNaturalist: 1557 Taxa (Seiten: 4)
- OBIS: 3425 Arten mit Nachweisen außer iNaturalist

### iNaturalist-Namen zugeordnet

Keine (`recipes/inat_names.json`).

### Von Hand ausgeschlossen

| Art | iNat | Grund |
|---|---|---|
| *Grapsus tenuicrustatus* | 4607 | Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen. |
| *Colobocentrotus atratus* | 2200 | Sitzt in der Brandungszone auf Uferfelsen, keine Begegnung unter Wasser. |
| *Nerita picea* | 1465 | Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Littoraria pintado* | 1158 | Strandschnecke der Spritzwasserzone, sitzt über dem Wasser auf den Uferfelsen. |
| *Calcinus seurati* | 1144 | Einsiedlerkrebs der oberen Gezeitentümpel, lebt über der Brandung. |
| *Physalia utriculus* | 779 | Treibt an der Oberfläche der Hochsee und wird vor allem angespült am Strand beobachtet, keine Begegnung am Riff. |
| *Veronicella cubensis* | 666 | Landnacktschnecke, kein Meerestier. |
| *Ocypode pallidula* | 656 | Geisterkrabbe, lebt am trockenen Sandstrand. |
| *Metopograpsus thukuhar* | 461 | Uferkrabbe der Felsküste und Hafenmauern, lebt in der Gezeitenzone über dem Wasser. |
| *Cellana exarata* | 424 | Napfschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Grapsus longitarsis* | 348 | Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen. |
| *Nerita polita* | 280 | Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Trochus intextus* | 252 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 27 von 29 Beobachtungen mit Angabe „tot“). |
| *Echinolittorina hawaiiensis* | 212 | Strandschnecke der Spritzwasserzone, sitzt über dem Wasser auf den Uferfelsen. |

### Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Hymenocera picta* | Die Harlekingarnele frisst nur Seesterne und ist einer der begehrtesten Funde für Unterwasserfotografen. | 110 | Reihenfolge-Quelle, Verbreitung | invertebrates |
| *Charonia tritonis* | Das Tritonshorn frisst Dornenkronen-Seesterne und ist selten geworden, weil seine Schale begehrt ist. | 108 | Reihenfolge-Quelle, OBIS, Verbreitung | invertebrates |
| *Panulirus marginatus* | Die Hawaii-Languste lebt nur auf Hawaii und versteckt sich tagsüber in Riffhöhlen. | 129 | Reihenfolge-Quelle, OBIS, Verbreitung | invertebrates |

### Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS ohne iNaturalist oder Verbreitung): 39/40 (98 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 4: *Halgerda terramtuentis*, *Calcinus pictus*, *Mithrodia fisheri*, *Panulirus marginatus*
- Arten ohne Volksnamen `de` in der Referenz-DB: 29/40 (72 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 3/40 (8 %)
- Familien ohne Volksnamen `de`: 26/26 (100 %): *Acanthasteridae*, *Acroporidae*, *Aglajidae*, *Aplustridae*, *Aplysiidae*, *Chromodorididae*, *Cypraeidae*, *Diadematidae*, *Diogenidae*, *Dorididae*, *Echinometridae*, *Facelinidae*, *Holothuriidae*, *Mithrodiidae*, *Notarchidae*, *Ophidiasteridae*, *Oreasteridae*, *Palaemonidae*, *Palinuridae*, *Phyllidiidae*, *Pocilloporidae*, *Polyceridae*, *Ranellidae*, *Stenopodidae*, *Toxopneustidae*, *Zoanthidae*
- Familien ohne Volksnamen `en`: 17/26 (65 %): *Acroporidae*, *Aglajidae*, *Aplustridae*, *Chromodorididae*, *Diadematidae*, *Dorididae*, *Echinometridae*, *Facelinidae*, *Mithrodiidae*, *Notarchidae*, *Ophidiasteridae*, *Oreasteridae*, *Phyllidiidae*, *Pocilloporidae*, *Polyceridae*, *Toxopneustidae*, *Zoanthidae*

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

- *Diadema savignyi*: Reihenfolge-Quelle

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

- gleicher Volksname `de` „Nacktschnecke“: *Pteraeolidia semperi*, *Tambja morosa*, *Thorunna daniellae*

### Arten

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Klasse |
|---|---|---|---|---|---|---|
| 1 | *Echinometra mathaei* | 2812 | 983 | native ×1 | Meer | Echinoidea |
| 2 | *Actinopyga varians* | 2447 | 8 | – | Meer | Holothuroidea |
| 3 | *Heterocentrotus mamillatus* | 2093 | 224 | native ×1 | Meer | Echinoidea |
| 4 | *Tripneustes gratilla* | 1131 | 87 | native ×1 | Meer | Echinoidea |
| 5 | *Holothuria atra* | 861 | 1402 | native ×1 | Meer | Holothuroidea |
| 6 | *Hypselodoris imperialis* | 761 | 66 | native ×1 | Meer | Gastropoda |
| 7 | *Diadema savignyi* | 736 | – | – | Meer | Echinoidea |
| 8 | *Pocillopora meandrina* | 727 | 10890 | native ×1 | Meer | Hexacorallia |
| 9 | *Mauritia mauritiana* | 701 | 35 | native ×1 | Meer | Gastropoda |
| 10 | *Culcita novaeguineae* | 676 | 4 | – | Meer | Asteroidea |
| 11 | *Halgerda terramtuentis* | 672 | 60 | endemic ×1 | Meer | Gastropoda |
| 12 | *Stenopus hispidus* | 669 | 105 | native ×1 | Meer | Malacostraca |
| 13 | *Phyllidiella pustulosa* | 645 | 31 | native ×1 | Meer | Gastropoda |
| 14 | *Glossodoris rufomarginata* | 632 | 37 | native ×1 | Meer | Gastropoda |
| 15 | *Calcinus laevimanus* | 580 | 5 | native ×1 | Meer | Malacostraca |
| 16 | *Echinothrix calamaris* | 563 | 63 | native ×1 | Meer | Echinoidea |
| 17 | *Palythoa tuberculosa* | 547 | 41 | native ×1 | Meer | Hexacorallia |
| 18 | *Echinothrix diadema* | 454 | 115 | native ×1 | Meer | Echinoidea |
| 19 | *Goniobranchus vibratus* | 426 | 32 | native ×1 | Meer | Gastropoda |
| 20 | *Calcinus pictus* | 424 | 12 | endemic ×1 | Meer | Malacostraca |
| 21 | *Phyllidia varicosa* | 398 | 34 | native ×1 | Meer | Gastropoda |
| 22 | *Echinometra oblonga* | 391 | 19 | native ×1 | Meer | Echinoidea |
| 23 | *Montipora capitata* | 388 | 17436 | native ×1 | Meer | Hexacorallia |
| 24 | *Pteraeolidia semperi* | 383 | 151 | native ×1 | Meer | Gastropoda |
| 25 | *Mauritia maculifera* | 377 | 34 | native ×1 | Meer | Gastropoda |
| 26 | *Linckia multifora* | 373 | 395 | native ×1 | Meer | Asteroidea |
| 27 | *Holothuria whitmaei* | 360 | 1392 | – | Meer | Holothuroidea |
| 28 | *Ardeadoris tomsmithi* | 347 | 26 | native ×1 | Meer | Gastropoda |
| 29 | *Acanthaster solaris* | 338 | 334 | native ×1 | Meer | Asteroidea |
| 30 | *Hydatina amplustre* | 315 | 37 | native ×1 | Meer | Gastropoda |
| 31 | *Aplysia argus* | 309 | 6 | native ×1 | Meer | Gastropoda |
| 32 | *Luria isabella* | 309 | 78 | – | Meer | Gastropoda |
| 33 | *Stylocheilus striatus* (Quelle: *Stylocheilus longicauda*) | 301 | 30 | – | Meer | Gastropoda |
| 34 | *Chelidonura hirundinina* | 297 | 18 | native ×1 | Meer | Gastropoda |
| 35 | *Tambja morosa* | 297 | 17 | native ×1 | Meer | Gastropoda |
| 36 | *Thorunna daniellae* | 297 | 14 | – | Meer | Gastropoda |
| 37 | *Mithrodia fisheri* | 294 | 218 | endemic ×1 | Meer | Asteroidea |
| 108 | *Charonia tritonis* (Highlight; 59 Beobachter) | 105 | 47 | native ×1 | Meer | Gastropoda |
| 110 | *Hymenocera picta* (Highlight; 30 Beobachter) | 103 | – | native ×1 | Meer | Malacostraca |
| 129 | *Panulirus marginatus* (Highlight; 25 Beobachter) | 86 | 615 | endemic ×1 | Meer | Malacostraca |

### Grenzfälle

Je 10 Arten vor und nach der Grenze (Highlights übersprungen).

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Klasse | Im Subdeck |
|---|---|---|---|---|---|---|---|
| 28 | *Ardeadoris tomsmithi* | 347 | 26 | native ×1 | Meer | Gastropoda | ja |
| 29 | *Acanthaster solaris* | 338 | 334 | native ×1 | Meer | Asteroidea | ja |
| 30 | *Hydatina amplustre* | 315 | 37 | native ×1 | Meer | Gastropoda | ja |
| 31 | *Aplysia argus* | 309 | 6 | native ×1 | Meer | Gastropoda | ja |
| 32 | *Luria isabella* | 309 | 78 | – | Meer | Gastropoda | ja |
| 33 | *Stylocheilus striatus* (Quelle: *Stylocheilus longicauda*) | 301 | 30 | – | Meer | Gastropoda | ja |
| 34 | *Chelidonura hirundinina* | 297 | 18 | native ×1 | Meer | Gastropoda | ja |
| 35 | *Tambja morosa* | 297 | 17 | native ×1 | Meer | Gastropoda | ja |
| 36 | *Thorunna daniellae* | 297 | 14 | – | Meer | Gastropoda | ja |
| 37 | *Mithrodia fisheri* | 294 | 218 | endemic ×1 | Meer | Asteroidea | ja |
| | **Grenze** | | | | | | |
| 38 | *Plakobranchus ocellatus* | 293 | 111 | native ×1 | Meer | ? | nein |
| 39 | *Exaiptasia diaphana* | 284 | 13 | – | Meer | ? | nein |
| 40 | *Conus ebraeus* | 284 | 53 | native ×1 | Meer | ? | nein |
| 41 | *Holothuria cinerascens* | 281 | 14 | native ×1 | Meer | ? | nein |
| 42 | *Parribacus antarcticus* | 277 | 7 | native ×1 | Meer | ? | nein |
| 43 | *Cypraea tigris* | 274 | 20 | native ×1 | Meer | ? | nein |
| 44 | *Panulirus penicillatus* | 268 | 394 | native ×1 | Meer | ? | nein |
| 45 | *Dolabrifera dolabrifera* | 265 | 31 | – | Meer | ? | nein |
| 46 | *Porites lobata* | 265 | 40307 | native ×1 | Meer | ? | nein |
| 47 | *Goniobranchus albopustulosus* | 256 | 14 | native ×1 | Meer | ? | nein |

### Ausgeschlossene Kandidaten

<details><summary>475 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Grapsus tenuicrustatus* | 4607 | Meer | von Hand ausgeschlossen (Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen.) |
| *Colobocentrotus atratus* | 2200 | Meer | von Hand ausgeschlossen (Sitzt in der Brandungszone auf Uferfelsen, keine Begegnung unter Wasser.) |
| *Nerita picea* | 1465 | Meer | von Hand ausgeschlossen (Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Littoraria pintado* | 1158 | Meer | von Hand ausgeschlossen (Strandschnecke der Spritzwasserzone, sitzt über dem Wasser auf den Uferfelsen.) |
| *Calcinus seurati* | 1144 | Meer | von Hand ausgeschlossen (Einsiedlerkrebs der oberen Gezeitentümpel, lebt über der Brandung.) |
| *Physalia utriculus* | 779 | Meer | von Hand ausgeschlossen (Treibt an der Oberfläche der Hochsee und wird vor allem angespült am Strand beobachtet, keine Begegnung am Riff.) |
| *Veronicella cubensis* | 666 | Meer | von Hand ausgeschlossen (Landnacktschnecke, kein Meerestier.) |
| *Ocypode pallidula* | 656 | Meer | von Hand ausgeschlossen (Geisterkrabbe, lebt am trockenen Sandstrand.) |
| *Metopograpsus thukuhar* | 461 | Brack/Meer | von Hand ausgeschlossen (Uferkrabbe der Felsküste und Hafenmauern, lebt in der Gezeitenzone über dem Wasser.) |
| *Cellana exarata* | 424 | Meer | von Hand ausgeschlossen (Napfschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Grapsus longitarsis* | 348 | Meer | von Hand ausgeschlossen (Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen.) |
| *Nerita polita* | 280 | Meer | von Hand ausgeschlossen (Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Macrobrachium lar* | 258 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trochus intextus* | 252 | Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 27 von 29 Beobachtungen mit Angabe „tot“).) |
| *Echinolittorina hawaiiensis* | 212 | Meer | von Hand ausgeschlossen (Strandschnecke der Spritzwasserzone, sitzt über dem Wasser auf den Uferfelsen.) |
| *Pomacea canaliculata* | 198 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Procambarus clarkii* | 139 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Corbicula fluminea* | 69 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Palaemon debilis* | 69 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Halocaridina rubra* | 51 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Melanoides tuberculata* | 30 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Atyoida bisulcata* | 28 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neripteron cariosum* | 16 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrobrachium grandimanus* | 13 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neritona granosa* | 11 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Harpa major* | 10 | Meer | nur tiefer als die Tauchgrenze (erst ab 62 m) |
| *Alatina alata* | 9 | Meer | nur tiefer als die Tauchgrenze (erst ab 55 m) |
| *Palaemon pacificus* | 7 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Actaeomorpha erosa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Aplysia reticulata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Barbatia parva* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Beuroisia major* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Bittinella hiloensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Calcinus isabellae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Callyspongia diffusa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Carminodoris bifurcata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Casmaria kalosmodix* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cerithium rostratum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Chondrosia corticata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cinetorhynchus hiatti* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cuapetes grandis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cycloachelous suborbicularis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cyerce bourbonica* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cyphastrea agassizi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Dendropoma platypus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Distorsio anus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Goniobranchus albonares* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hapalocarcinus marsupialis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Heliacus implexus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Holothuria leucospilota* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hyotissa numisma* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Iphione muricata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Iphione ovata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Janolus mirabilis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lampasopsis rhodostoma* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lovellona atramentosa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lysiosquilla maculata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Melanella cumingii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Melibe megaceras* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Menaethius orientalis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Metalia spatagus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Montipora incrassata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Morula porphyrostoma* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Oliva richerti* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ovatipsa rashleighana* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Oxymeris felina* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Peasistilifer nitidula* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Plaxiphora kamehamehae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Polyplectana kefersteinii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Portunus pubescens* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Rhinoclavis articulata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Rhizopsammia verrilli* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scintilla hiloa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Swainsonia newcombii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Symplegma rubra* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Synaptocochlea concinna* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Terebra amanda* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Terebra babylonia* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Viriola abbotti* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Williamia radiata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Acanthephyra eximia* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Acteocina sandwicensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Albunea speciosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Anomalorhiza shawi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Biemna fistulosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Brachycarpus biunguiculatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bunodeopsis medusoides* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Calappa pokipoki* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cerithium placidum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chicoreus insularum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ciliopagurus hawaiiensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cinetorhynchus concolor* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cinetorhynchus fasciatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conchoderma virgatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus acutangulus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus pertusus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Copula sivickisi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Coralliophila erosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Coralliophila violacea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Coronula diadema* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cupolaconcha meroclista* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cyclodius obscurus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lyncina carneola* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Daldorfia dimorpha* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dendrodoris coronata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Diala semistriata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Diaugasma olyra* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Drupina grossularia* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dynomene praedator* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Echinosquilla guerinii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Eualetes tulipa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Euplica ionida* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Euthymella concors* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gymnodoris citrina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gyrineum pusillum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Halgerda dalanghita* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hamigera strongylata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Heliacus mighelsi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hemilienardia apiculata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Homalocantha anatomica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Isognomon legumen* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Janthina exigua* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Labidodemas semperianum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Macrophthalmus telescopicus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Melanella aciculata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Metalia sternalis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Metopograpsus oceanicus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Monetaria annulus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Morula echinata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Murphydoris puncticulata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Myurella flavofasciata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Notobryon wardi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Oxymeris areolata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Oxymeris chlorata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pachycheles pisoides* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pagurixus laevimanus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Phyllidiopsis cardinalis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Phyllidiopsis loricata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Physella acuta* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Plesiotrochus luteus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Plocamopherus ceylonicus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pterynotus elongatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rhinoclavis fasciata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rhynchocinetes rathbunae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sabellastarte magnifica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Scyllarides haanii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Septifer cumingii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Soliella flava* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Solmissus incisa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Spondylus linguafelis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Staphylaea staphylaea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Stenopus earlei* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sulcorissoina imbricata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Talostolida latior* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Talostolida teres* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tethocyathus minor* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Thalamita picta* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Thetys vagina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Thromidia catalai* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Triphora laddi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tugali oblonga* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Vexillum piceum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Vexillum salisburyi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Xanthias canaliculatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Agalma okenii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ascidia sydneiensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Branchiosyllis cirropunctata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bulaceros newcannorum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bursa rosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Catriona pinnifera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cerberilla albopunctata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chama asperella* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chicoreus brunneus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chlorodiella laevissima* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cistina columbiae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Colubraria obscura* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus bullatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus capitaneus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Corallianassa borradailei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Coriocella nigra* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Creniola breviceps* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Crithe huna* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Crucibulum spinosum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cytharomorula lefevreiana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dactylosaster cylindricus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dairoides kusei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Didemnum perlucidum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Diodora ruppellii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Doriprismatica atromarginata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eatoniella janetaylorae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Elysia obtusa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hoplometopus holthuisi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epifungium ulu* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epitonium goldsmithi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epitonium paumotense* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eucithara angiostoma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eucithara pusilla* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Euplica livescens* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Euplica turturina* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Euthymella elongata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Evalea eclecta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fiona pinnata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fossarus garrettii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Furtipodia petrosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gelagna succincta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Granulina vitrea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnodoris alba* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Harpiliopsis beaupresii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Haurakia marmorata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Herviera gliriella* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Heterocarpus ensifer* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Huenia heraldica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hymeniacidon chloris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Jactellina clathrata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Joeropsis hawaiiensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lovenia hawaiiensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mammilla melanostoma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Metaxia brunnicephala* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Microdaphne morrisoni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mitrella nympha* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Murphydoris cobbi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Myriopathes ulex* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nematocarcinus gracilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Neoliomera pubescens* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Neonaesa rugosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nerita albicilla* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Notopygos albiseta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nucleolaria nucleus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Odostomia stearnsiella* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Oenone fulgida* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Oscarella lobularis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Palaemonella burnsi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pandalosia ephamilla* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Panopeus lacustris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pascula ochrostoma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Periclimenes pholeter* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Phyllochaetopterus verrilli* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Planaxis suturalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Platorchestia lanipo* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Platydoris inornata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plesionika narval* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pocillopora acuta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pocillopora ligulata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Prionocidaris thomasi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Prosthiostomum trilineatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pteria brunnea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pterygia crenulata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rhinolambrus contrarius* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Salmacina dysteri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scalenostoma carinatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Schizophroida hilensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Spinoaglaja orientalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Stichodactyla tapetum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Stilifer linckiae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Strigatella ticaonica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Syphonota geographica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pinguitellina robusta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tellinella crucigera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Terebra argus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Thor spinosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trichorhina heterophthalma* | 2 | ? | zu wenige Nachweise (2 < 5) |
| *Tritonoturris cumingii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tweedieia laysani* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Usilla avenacea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vanikoro cancellata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vexillum diutenerum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Xenuroturris kingae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Abylopsis tetragona* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora cytherea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aegires exeches* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aliculastrum cylindricum* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Alpheus rapacida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alvania isolata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amorphinopsis excavans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anarithma metula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aplysilla sulfurea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Arca kauaia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Architectonica perspectiva* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Argathona rhinoceros* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Argulus japonicus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Armadilloniscus ellipticus* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Astropecten polyacanthus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Atagema echinata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Atagema intecta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ataxocerithium serotinum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Atergatopsis signata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Athorybia rosacea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Barbatia decussata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Benthesicymus laciniatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Botryllus schlosseri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bractechlamys nodulifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calcinus vachoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cephalopyge trematoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cephea cephea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cerithidium diplax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cerithiopsis pulvis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Charybdis hellerii* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Chiton squamosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chlorodiella nigra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chrystella suta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cinetorhynchus hendersoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cladonema radiatum* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Clibanarius englaucus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clio pyramidata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coelocarcinus foliatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Colidotea edmondsoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Colubraria tortuosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus coronatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus geographus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus sanguinolentus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Corella minuta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Crassostrea virginica* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Cyamus boopis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cyclodius nitidus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lyncina ventriculus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cystisoma magna* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Daphnella varicosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dardanus pedunculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dendostrea sandvichensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dendrodoris albopurpura* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Discodoris cebuensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Doriopsis granulosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dysidea fragilis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Echineulima robusta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echinocyamus crispus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echinodictyum asperum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Elaphoidella bidens* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Epiactaea nodulosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epitonium deificum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epitonium sandwichense* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epitonium umbilicatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eucidaris tribuloides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Euthymella bilix* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Euthymella lutea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Evalea waikikiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Favartia garrettii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Finella pupoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fossarus multicostatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Geryonia proboscidalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gnathophyllum precipuum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gonodactylellus affinis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gonodactylus platysoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halicreas minimum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Harpa amouretta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Harpiliopsis spinigera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hemiliostraca peasei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hippolyte edmondsoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hipponoe gaudichaudi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria conusalba* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria rigida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria verrucosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Homola dickinsoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hydatina zonata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Iniforis peleae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Intesius crosnieri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Iotrochota baculifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Janthina globosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Joculator ridiculus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Justitia longimana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Kaloplocamus ramosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Kermia aniani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Kraussia rugulosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Laemodonta clausa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lamoha williamsi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leucaltis nodusgordii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leucetta chagosensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Liocarpilodes biunguis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lissoclinum patella* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lissodiadema lorioli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Litharium oceanida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Litiopa melanostoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Littoraria intermedia* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Littoraria undulata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lotoria lotoria* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Macrorhynchia philippina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mareleptopoma iredalei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Melanella teinostoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mesactinia ganensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Metapenaeopsis hilarula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Microcosmus exasperatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Miralda paulbartschi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mitrella albuginosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mnestia girardi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Modiolus matris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Monophorus quadrimaculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Monoplex gemmatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mycale parishii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nanaphora triticea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Naria erosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Naria ostergaardi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nassa tuamotuensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nassarius crematus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nassarius splendidulus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nectopyramis natans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nemanthus nitidus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nematocarcinus tenuirostris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neocancilla papilio* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neognathophausia ingens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neoliomera demani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nerita signata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Notarchus indicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Notopoides latus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nucula hawaiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiactis modesta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophidiaster duncani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oreotlos lagarodes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ostrea stentina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ovula ovum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pandea conica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Papuaphiloscia laevis* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Parashiela ambulata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parhippolyte misticia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paromola japonica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pecten waikikius* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pelagia flaveola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Peltodoris rubra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Penaeus monodon* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Phylladiorhynchus integrirostris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllidiella lizae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllorhiza punctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pilumnus taeniola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pinaxia versicolor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Planorbella duryi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Planorbella trivolvis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Plesionika edwardsii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plesionika ocellus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Porites solida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Psammocora nierstraszi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudozius caystrus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pulicicochlea faba* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pullosquilla litoralis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Punctoterebra swainsoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pupa tessellata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pustularia bistrinotata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pylopaguropsis lemaitrei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pyrgulina oodes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pyrosomella verticillata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Quadrimaera quadrimana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Radobornia bryani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Roboastra gracilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rochefortina sandwichensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sagaminopteron psychedelicum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sansonia shigemitsui* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scolanthus armatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Septa rubecula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Simulamerelina wanawana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Smaragdia bryanae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Solmundella bitentaculata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Spondylus candidus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Spondylus nicobaricus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Strebloceras subannulatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sulculeolaria turgida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sympagurus dofleini* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synapta maculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tanaoa distinctus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tetraclitella divisa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thorunna australis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thuridilla vataae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thyca crystallina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thyrolambrus efflorescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Timarete punctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tonganaella perna* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tonna melanostoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Turbo chrysostomus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Turbonilla thaanumi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Turridrupa consobrina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tweedieia odhneri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vanikoro acuta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Verconia simplex* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexilla taeniata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum approximatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vexillum unifasciatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Viriola cancellata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vitularia miliaris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xenophora peroniana* | 1 | Meer | zu wenige Nachweise (1 < 5) |

</details>

### Nicht aufgelöste Namen

<details><summary>427 Namen</summary>

*Lissachatina fulica* (4693), *Monetaria caputophidii* (1167), *Laevicaulis alte* (673), *Ocypode urvillii* (540), *Euglandina rosea* (524), *Hypselodoris peasei* (398), *Isognomon californicus* (328), *Coryphellina exoptata* (291), *Hexabranchus sandwichensis* (281), *Thorunna kahuna* (276), *Hexabranchus aureomarginatus* (245), *Arakawania granulata* (240), *Naria helvola* (188), *Bradybaena similaris* (170), *Hiatodoris fellowsi* (165), *Parmarion martensi* (163), *Aplysia elongata* (146), *Samla bicolor* (146), *Chelidonura alisonae* (141), *Peronia platei* (136), *Limax maximus* (130), *Sistrum ricinus* (130), *Ovachlamys fulgens* (122), *Goniosupradens hawaiensis* (117), *Meghimatium bilineatum* (115), *Hypselodoris violabranchia* (113), *Pseudoceros paralaticlavus* (112), *Breviturma pica* (104), *Danarma obtusifrons* (100), *Armadillidium vulgare* (98), *Maculastrombus maculatus* (98), *Lamarcka ventricosa* (95), *Ardeadoris poliahu* (82), *Elasmias luakahaense* (81), *Corallianassa oahuensis* (75), *Zoanthus kuroshio* (67), *Achatinella mustelina* (62), *Peasiella tantilla* (59), *Thranita crenata* (58), *Marioniopsis hawaiiensis* (57), *Thysanozoon tentaculatum* (57), *Partulina mighelsiana* (51), *Ricinella rubusidaeus* (50), *Tenellia nakapila* (47), *Homalopoma verruca* (44), *Neocaridina davidi* (44), *Subulina octona* (44), *Vasticardium hawaiense* (42), *Auriculella diaphana* (41), *Cornu aspersum* (41), *Breviturma brevipes* (40), *Dendrodoris krusensternii* (40), *Siphopteron quadrispinosum* (40), *Zenopontonia soror* (40), *Portunus hawaiiensis* (38), *Pleurobranchus varians* (37), *Dardanus sanguinolentus* (34), *Philonesia chamissoi* (34), *Bostrycapulus calyptraeiformis* (31), *Siphonaria nuttallii* (30), *Tayloria kibweziensis* (30), *Noumeaella rehderi* (29), *Naria poraria* (27), *Phycophila euchlora* (27), *Breviturma dentata* (26), *Goniosupradens erythrodactylus* (26), *Auriculella perpusilla* (25), *Ecmanis ignea* (25), *Nodolatirus nodatus* (25), *Vexillum adamsi* (25), *Sclerophytum densa* (24), *Philonesia hartmanni* (23), *Pleurehdera pellucida* (23), *Bulla peasiana* (22), *Terebra achates* (22), *Nesobornia hawaiensis* (21), *Triops longicaudatus* (21), *Breviturma krohi* (19), *Echinocyamus incertus* (19), *Phidiana semidecora* (19), *Scopalina hapalia* (19), *Tauphaedusa tau* (19), *Venezillo parvus* (19), *Hypselodoris insulana* (18), *Microcollonia rubricincta* (18), *Elysia nealae* (17), *Succinea newcombiana* (17), *Imbricariopsis punctata* (16), *Ligia rolliensis* (16), *Polygyra cereolus* (16), *Pseudoceros leptostictus* (16), *Reductoniscus costulatus* (16), *Catinella rotundata* (15), *Percnon sinense* (15), *Amplidrupa aperta* (14), *Arion intermedius* (14), *Clathria mima* (14), *Isarachnanthus bandanensis* (14), *Limenandra rosanae* (14), *Myurella pygmaea* (14), *Nebularia ferruginea* (14), *Pseudobiceros splendidus* (14), *Spondylus violacescens* (14), *Strigatella aurora* (14), *Bermudella pellucida* (13), *Condylomitra tuberosa* (13), *Cubaris murina* (13), *Eupusia lauta* (13), *Limenandra confusa* (13), *Oliva ozodona* (13), *Succinea cepulla* (13), *Aliculastrum debile* (12), *Partulina semicarinata* (12), *Pleurolidia juliae* (12), *Scabricola olivaeformis* (12), *Zachrysia provisoria* (12), *Baeolidia moebii* (11), *Deroceras laeve* (11), *Gyroscala commutata* (11), *Hastula inconstans* (11), *Kermidaphnella pumila* (11), *Xiphonectes longispinosus* (11), *Auriculella turritella* (10), *Casmaria kayae* (10), *Hiloa variabilis* (10), *Homalocantha pele* (10), *Longchaeus maculosus* (10), *Siphopteron flavum* (10), *Thuridilla kathae* (10), *Allopeas clavulinum* (9), *Burmoniscus mauritiensis* (9), *Carelia cochlea* (9), *Conus peasei* (9), *Cyerce liliuokalaniae* (9), *Elasmias fuscum* (9), *Halgerda paliensis* (9), *Hiona exaequata* (9), *Ligia kamehameha* (9), *Lytocarpia nigra* (9), *Paropeas achatinaceum* (9), *Partulina redfieldi* (9), *Pseudobiceros gratus* (9), *Pseudobiceros stellae* (9), *Achatinella pulcherrima* (8), *Andvakia discipulorum* (8), *Elysia lobata* (8), *Hawaiistrombus hellii* (8), *Ligia mauinuiensis* (8), *Nebularia incompta* (8), *Tonna hawaiiensis* (8), *Achatinella fulgens* (7), *Auriculella armata* (7), *Deroceras reticulatum* (7), *Perdicella helena* (7), *Achatinella lorata* (6), *Atagema scabriuscula* (6), *Auriculella ambusta* (6), *Calliasmata pholidota* (6), *Coralliophila cumingii* (6), *Gastrocopta servilis* (6), *Nemalecium caeruleus* (6), *Partulina proxima* (6), *Partulina rufa* (6), *Phyllamphion elegans* (6), *Platorchestia pickeringi* (6), *Pseudonebularia cucumerina* (6), *Thuridilla multimarginata* (6), *Tornatellides kilauea* (6), *Aegires lemoncello* (5), *Auriculella crassula* (5), *Coscinasterias acutispina* (5), *Hiona pilsbryi* (5), *Laminella gravida* (5), *Mieniplotia scabra* (5), *Paradaphne interrupta* (5), *Partulina variabilis* (5), *Phyllodesmium undulatum* (5), *Placida barackobamai* (5), *Plesiothyreus scobinatus* (5), *Pseudoceros scintillatus* (5), *Siphonaria undans* (5), *Strigatella luctuosa* (5), *Tornatellides procerulus* (5), *Achatinella apexfulva* (4), *Achatinella viridans* (4), *Asterodiscides tuberculosus* (4), *Batzella melanos* (4), *Bulbaeolidia paulae* (4), *Bulimulus guadalupensis* (4), *Doris nucleola* (4), *Euprotomus hawaiensis* (4), *Herviella mietta* (4), *Hypselodoris paulinae* (4), *Janolus toyamensis* (4), *Lamellidea polygnampta* (4), *Lampasopsis cruentata* (4), *Launsina rubropurpurata* (4), *Microcollonia candida* (4), *Moloha major* (4), *Nebularia pellisserpentis* (4), *Oxymeris suffusa* (4), *Paragiopagurus laperousei* (4), *Pedipes sandwicensis* (4), *Pelagella joubini* (4), *Ptilocaulis spiculifer* (4), *Rissoella confusa* (4), *Sclerodoris rubicunda* (4), *Semicassis umbilicata* (4), *Tomoberthella martensi* (4), *Achatinella stewartii* (3), *Achatinella vulpina* (3), *Amastra rugulosa* (3), *Anteaeolidiella cacaotica* (3), *Astropecten hawaiiensis* (3), *Auriculella tenella* (3), *Elasmias anceyanum* (3), *Geograpsus* (3), *Isognomon incisus* (3), *Jorunna ramicola* (3), *Leiosolenus mucronatus* (3), *Levicaris mammillata* (3), *Ligia dante* (3), *Lyncina propinqua* (3), *Mastoniaeforis hinuhinu* (3), *Namalycastis hawaiiensis* (3), *Nebularia fastigium* (3), *Pacificella baldwini* (3), *Paraplanocera marginata* (3), *Partulina perdix* (3), *Pseudoceros bolool* (3), *Pseudoceros rubronanus* (3), *Roxaniella pittmani* (3), *Siphonaria mauiensis* (3), *Strigatella pudica* (3), *Subulophora peasei* (3), *Succinea caduca* (3), *Succinea konaensis* (3), *Succinea thaanumi* (3), *Tytthosoceros nocturnus* (3), *Volvarina unilineata* (3), *Abronica turon* (2), *Achatinella abbreviata* (2), *Achatinella bellula* (2), *Achatinella bulimoides* (2), *Achatinella sowerbyana* (2), *Agathotoma mighelsi* (2), *Auriculella uniplicata* (2), *Avaldesia tamatoa* (2), *Berthella caledonica* (2), *Cardita excisa* (2), *Carelia dolei* (2), *Carelia evelynae* (2), *Carelia necra* (2), *Carinomitra saltata* (2), *Cerithiopsis granata* (2), *Cleotrivia globosa* (2), *Cliona caesia* (2), *Costasiella formicaria* (2), *Dulcerana granularis* (2), *Euapta tahitiensis* (2), *Eubranchus* (2), *Glaucilla marginata* (2), *Glaucilla mcfarlanei* (2), *Hastula betsyae* (2), *Hermania orca* (2), *Kaala subrutila* (2), *Kellia hawaiensis* (2), *Leucascus flavus* (2), *Limacus flavus* (2), *Litharium maculatum* (2), *Lytocarpia phyteuma* (2), *Maritigrella eschara* (2), *Mastoniaeforis ordinata* (2), *Melanella kanaka* (2), *Milax gagates* (2), *Mnestia villica* (2), *Oppomorus funiculatus* (2), *Orphanopusia patriarchalis* (2), *Pacifilux rubra* (2), *Paradaphne ornata* (2), *Pherecardia distincta* (2), *Phrikoceros katoi* (2), *Procaris hawaiana* (2), *Pronesopupa hystricella* (2), *Pseudobiceros gloriosus* (2), *Pseudobiceros murinus* (2), *Pseudobiceros periculosus* (2), *Pseudonebularia connectens* (2), *Pyramidelloides gracilis* (2), *Reticunassa silvardi* (2), *Septa occidentalis* (2), *Simulamerelina granulosa* (2), *Simulamerelina hewa* (2), *Sistrum albolabris* (2), *Stauridiosarsia nipponica* (2), *Stebbingdromia plumosa* (2), *Strigatella coronata* (2), *Strigatella fulvescens* (2), *Succinea lumbalis* (2), *Thor leptochelus* (2), *Thranita coeruleipes* (2), *Tornatellides konaensis* (2), *Tornatellides macromphala* (2), *Tornatellides perkinsi* (2), *Vitularia sandwicensis* (2), *Acanthocidaris hastigera* (1), *Achatinella byronii* (1), *Achatinella curta* (1), *Achatinella lila* (1), *Achatinella livida* (1), *Allopeas gracile* (1), *Amastra assimilis* (1), *Amastra cyclostoma* (1), *Amastra forbesi* (1), *Amastra nucleola* (1), *Amastra turritella* (1), *Ambigolimax* (1), *Angustassiminea nitida* (1), *Arakawania marginalba* (1), *Arion distinctus* (1), *Arion subfuscus* (1), *Armina rubida* (1), *Atolla* (1), *Babamunida kanaloa* (1), *Bermudella lahainensis* (1), *Carelia bicolor* (1), *Carelia lirata* (1), *Carelia pilsbryi* (1), *Cautor intermissus* (1), *Centrostephanus asteriscus* (1), *Cheilea* (1), *Cherusius triunguiculatus* (1), *Clathropsis fosterae* (1), *Clavus pusillus* (1), *Clypeaster eurypetalus* (1), *Conus spiceri* (1), *Cookeconcha paucicostata* (1), *Cycloscala peaseana* (1), *Cyerce basi* (1), *Dentimargo pumila* (1), *Dermatobranchus piperoides* (1), *Doris immonda* (1), *Dulcerana affinis* (1), *Edwardsianthus gilbertensis* (1), *Edwardsianthus pudicus* (1), *Euanodontia hawaiensis* (1), *Euchirograpsus danielae* (1), *Furtipodia gemma* (1), *Godwinia caperata* (1), *Harpa goodwini* (1), *Helenia apiculata* (1), *Heteronucia minuta* (1), *Hymenopenaeus fallax* (1), *Inella pagoda* (1), *Iotrochota sinki* (1), *Kermidaphnella daedalea* (1), *Lamellidea gracilis* (1), *Lamellidea peponum* (1), *Laminella straminea* (1), *Leptachatina haenensis* (1), *Ligia honu* (1), *Lophocochlias parvissimus* (1), *Lucilina pacifica* (1), *Lyropupa thaanumi* (1), *Lyropupa thaumasia* (1), *Mactra thaanumi* (1), *Maculastrombus mutabilis* (1), *Margarya chinensis* (1), *Melanella acanthyllis* (1), *Melanella major* (1), *Monoplex comptus* (1), *Myurellopsis columellaris* (1), *Nebularia chrysostoma* (1), *Nebularia eremitarum* (1), *Nebularia ustulata* (1), *Nesophila prestonsutteri* (1), *Nesopupa newcombi* (1), *Newcombia gagei* (1), *Ophiomastix macroplaca* (1), *Oscilla indica* (1), *Pallifera* (1), *Partulina anceyana* (1), *Partulina crassa* (1), *Partulina dubiosa* (1), *Partulina marmorata* (1), *Partulina tappaniana* (1), *Partulina terebra* (1), *Peltidium* (1), *Pennella* (1), *Periclimenaeus devaneyi* (1), *Philonesia oahuensis* (1), *Phyllidia scottjohnsoni* (1), *Phyllognathia simplex* (1), *Physalia megalista* (1), *Platorchestia kaalensis* (1), *Plesiothyreus cancellatus* (1), *Produnga rubropunctata* (1), *Pseudobiceros pardalis* (1), *Pseudoceros jebborum* (1), *Rumina decollata* (1), *Sacoproteus thomasleei* (1), *Sagaminopteron pohnpei* (1), *Sakaila wanawana* (1), *Sarasinula plebeia* (1), *Sclerophytum abrupta* (1), *Siphonaria waikoloaensis* (1), *Starmeria conica* (1), *Stiliger* (1), *Strigatella coffea* (1), *Strigatella lugubris* (1), *Sturanya baldwini* (1), *Sturanya laciniosa* (1), *Styloptygma lacteolum* (1), *Temnotrema hawaiiense* (1), *Tempuractis rinkai* (1), *Tenellia pinnifera* (1), *Terestrombus fragilis* (1), *Tetraclitella purpurascens* (1), *Thala exilis* (1), *Thranita pseudopelsarti* (1), *Tornatellaria newcombi* (1), *Tornatellides serrarius* (1), *Tornatellides spaldingi* (1), *Trapania euryeia* (1), *Vayssierea felis* (1), *Weedingia paulayi* (1), *Xenuroturris devoizei* (1)

</details>

## Nicht aufgelöste Namen der Reihenfolge-Quelle

Die Referenz-DB der App kennt diese Namen nicht; die App fände sie auch nicht.

| Name | iNat |
|---|---|
| *Hypostomus* | 19 |
| *Micropterus nigricans* | 14 |
| *Ancistrus* | 12 |
| *Pterygoplichthys* | 9 |
| *Rubricatochromis* | 1 |
| *Schindleria* | 1 |
