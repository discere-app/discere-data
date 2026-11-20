# Bericht: Hawaii (`recipes/hawaii.json`)

Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.

- Referenz-DB: v3 (FishBase v26.06, SeaLifeBase v26.06)
- Salz/Süß: FishBase/SeaLifeBase v25.04 (species.parquet)
- iNaturalist: 544 Taxa (Seiten: 2)
- OBIS: 1625 Arten
- Bild: https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Reef_Triggerfish_1.JPG/330px-Reef_Triggerfish_1.JPG — Qyd, CC BY 2.5, https://commons.wikimedia.org/wiki/File:Reef_Triggerfish_1.JPG

## Gebiete

- iNaturalist: Hawaii, US (11), Northwestern Hawaiian Islands, US (141380)
- OBIS: Hawaii-Inseln mit den Nordwestlichen Hawaii-Inseln
- FishBase/SeaLifeBase-Verbreitung: 840B, 840:US-HI

## Übersicht

- Arten der Reihenfolge-Quelle, aufgelöst: 529; nicht aufgelöst: 10
- ausgeschlossen: 192
  - zu wenige Nachweise: 138
  - kein Meeresfisch: 39
  - zu klein: 13
  - nur tiefer als die Tauchgrenze: 2
- Kandidaten nach den Filtern: 337
- Deck: 155 Arten (Level 1: 45, Level 2: 60, Level 3: 50); Umfang laut Rezept 40/60/50 plus Highlights
- Highlights: 5 im Deck, 0 verworfen

## Verworfene Highlights

Keine.

## Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Mobula alfredi* | Der Riffmanta kommt vor Kona nachts ins Lampenlicht, einer der bekanntesten Tauchgänge der Welt. | 61 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Monachus schauinslandi* (Rezept: *Neomonachus schauinslandi*) | Die Hawaii-Mönchsrobbe kommt nur hier vor und ist eine der seltensten Robben der Welt. | – | Verbreitung | Level 1 |
| *Galeocerdo cuvier* | Der Tigerhai ist der große Hai Hawaiis und wird vor Oahu und Maui regelmäßig gesehen. | 201 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Stenella longirostris* | Spinnerdelfine ruhen tagsüber in den Buchten der Kona-Küste. | – | Verbreitung | Level 1 |
| *Megaptera novaeangliae* | Buckelwale kalben im Winter zwischen Maui, Lanai und Molokai. | – | Verbreitung | Level 1 |

## Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS oder Verbreitung): 152/155 (98 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 6: *Istiblennius zebra*, *Chaetodon fremblii*, *Kuhlia xenura*, *Plagiotremus goslinei*, *Canthigaster coronata*, *Pteropterus sphex*
- Arten ohne Volksnamen `de` in der Referenz-DB: 88/155 (57 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 2/155 (1 %)
- Familien ohne Volksnamen `de`: 9/45 (20 %): *Aetobatidae*, *Balaenopteridae*, *Cheloniidae*, *Delphinidae*, *Epinephelidae*, *Galeocerdonidae*, *Mobulidae*, *Octopodidae*, *Phocidae*
- Familien ohne Volksnamen `en`: 1/45 (2 %): *Phocidae*

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

Spalten: Rang unter den Kandidaten, Zählung der Reihenfolge-Quelle (iNat), OBIS-Nachweise, Einträge der FishBase/SeaLifeBase-Verbreitung in den Rezept-Regionen (~~durchgestrichen~~: Eintrag sagt „nicht vorhanden“), Wasser laut FishBase/SeaLifeBase.

### Level 1 (45)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 1 | *Chelonia mydas* | 11604 | 8287 | native ×2 | Meer |
| 2 | *Zanclus cornutus* | 2647 | 4560 | native ×1 | Meer |
| 3 | *Thalassoma duperrey* | 2609 | 33754 | native ×1 | Meer |
| 4 | *Zebrasoma flavescens* | 2516 | 7005 | native ×1 | Meer |
| 5 | *Acanthurus nigrofuscus* | 2178 | 13131 | native ×1 | Meer |
| 6 | *Rhinecanthus rectangulus* (Quelle: *Rhinecanthus rectangulus × aculeatus*) | 2177 | 2929 | native ×1 | Meer |
| 7 | *Abudefduf sordidus* | 2146 | 1781 | native ×1 | Brack/Meer |
| 8 | *Naso lituratus* | 2125 | 5753 | native ×1 | Meer |
| 9 | *Ostracion meleagris* | 2108 | 2009 | native ×1 | Meer |
| 10 | *Canthigaster jactator* | 1988 | 7435 | native ×1 | Meer |
| 11 | *Mulloidichthys flavolineatus* | 1797 | 2394 | native ×1 | Meer |
| 12 | *Chaetodon lunula* | 1744 | 1959 | native ×1 | Meer |
| 13 | *Istiblennius zebra* | 1713 | 1263 | endemic ×1 | Meer |
| 14 | *Gymnothorax meleagris* | 1646 | 1499 | native ×1 | Süß/Brack/Meer |
| 15 | *Chaetodon auriga* | 1634 | 2302 | native ×1 | Meer |
| 16 | *Melichthys niger* | 1513 | 3659 | native ×1 | Meer |
| 17 | *Acanthurus olivaceus* | 1506 | 7782 | native ×1 | Meer |
| 18 | *Chaetodon ornatissimus* | 1492 | 3014 | native ×1 | Meer |
| 19 | *Thalassoma trilobatum* | 1487 | 1702 | native ×1 | Meer |
| 20 | *Parupeneus multifasciatus* | 1476 | 10948 | native ×1 | Meer |
| 21 | *Gomphosus varius* | 1415 | 4855 | native ×1 | Meer |
| 22 | *Chaetodon quadrimaculatus* | 1386 | 2355 | native ×1 | Meer |
| 23 | *Scarus rubroviolaceus* | 1347 | 3812 | native ×1 | Meer |
| 24 | *Fistularia commersonii* | 1316 | 1275 | native ×1 | Meer |
| 25 | *Caranx melampygus* | 1303 | 3870 | native ×1 | Brack/Meer |
| 26 | *Aulostomus chinensis* | 1279 | 1815 | native ×1 | Meer |
| 27 | *Coris gaimard* | 1174 | 2426 | native ×1 | Meer |
| 28 | *Dascyllus albisella* | 1142 | 3595 | native ×1 | Meer |
| 29 | *Naso unicornis* | 1064 | 6393 | native ×1 | Meer |
| 30 | *Abudefduf vaigiensis* | 1049 | 1188 | native ×1 | Meer |
| 31 | *Ctenochaetus strigosus* | 1043 | 14130 | native ×1 | Meer |
| 32 | *Scarus psittacus* | 991 | 3099 | native ×1 | Meer |
| 33 | *Chlorurus spilurus* | 978 | 8182 | native ×1 | Meer |
| 34 | *Zebrasoma velifer* | 932 | 1835 | native ×1 | Meer |
| 35 | *Cirrhitus pinnulatus* | 923 | 1575 | native ×1 | Meer |
| 36 | *Octopus cyanea* | 917 | 761 | native ×1 | Meer |
| 37 | *Acanthurus blochii* | 914 | 2291 | native ×1 | Meer |
| 38 | *Melichthys vidua* | 889 | 2759 | native ×1 | Meer |
| 39 | *Echidna nebulosa* | 883 | 638 | native ×1 | Meer |
| 40 | *Sufflamen bursa* | 871 | 5171 | native ×1 | Meer |
| 61 | *Mobula alfredi* (Highlight) | 649 | 449 | native ×1 | Süß/Meer |
| – | *Monachus schauinslandi* (Highlight) | – | – | native ×1 | Meer |
| 201 | *Galeocerdo cuvier* (Highlight) | 57 | 42 | native ×1 | Brack/Meer |
| – | *Stenella longirostris* (Highlight) | – | – | native ×1 | Meer |
| – | *Megaptera novaeangliae* (Highlight) | – | – | native ×1 | Meer |

### Level 2 (60)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 41 | *Gymnothorax flavimarginatus* | 856 | 869 | native ×1 | Meer |
| 42 | *Abudefduf abdominalis* (Quelle: *Abudefduf abdominalis × vaigiensis*) | 847 | 1832 | native ×1 | Meer |
| 43 | *Gymnothorax eurostus* | 830 | 788 | native ×1 | Meer |
| 44 | *Cephalopholis argus* | 812 | 2924 | introduced ×1 | Meer |
| 45 | *Acanthurus leucopareius* | 810 | 3954 | native ×1 | Meer |
| 46 | *Stethojulis balteata* | 778 | 9474 | native ×1 | Meer |
| 47 | *Paracirrhites arcatus* | 775 | 9610 | native ×1 | Meer |
| 48 | *Rhinecanthus aculeatus* | 773 | 608 | native ×1 | Meer |
| 49 | *Paracirrhites forsteri* | 755 | 2335 | native ×1 | Meer |
| 50 | *Cantherhines dumerilii* | 750 | 964 | native ×1 | Meer |
| 51 | *Plectroglyphidodon marginatus* | 712 | 10866 | native ×1 | Meer |
| 52 | *Gymnothorax pictus* | 704 | 437 | native ×1 | Brack/Meer |
| 53 | *Diodon hystrix* | 702 | 588 | native ×1 | Meer |
| 54 | *Forcipiger flavissimus* | 682 | 2188 | native ×1 | Meer |
| 55 | *Labroides phthirophagus* | 665 | 3436 | native ×1 | Meer |
| 56 | *Mulloidichthys vanicolensis* | 665 | 1118 | native ×1 | Meer |
| 57 | *Lutjanus kasmira* | 664 | 2860 | introduced ×1 | Meer |
| 58 | *Arothron meleagris* | 657 | 513 | native ×1 | Meer |
| 59 | *Novaculichthys taeniourus* | 654 | 727 | native ×1 | Meer |
| 60 | *Plectroglyphidodon imparipennis* | 651 | 2927 | native ×1 | Meer |
| 62 | *Calotomus carolinus* | 647 | 1216 | native ×1 | Meer |
| 63 | *Canthigaster amboinensis* | 636 | 919 | native ×1 | Meer |
| 64 | *Chaetodon unimaculatus* | 579 | 907 | native ×1 | Meer |
| 65 | *Chaetodon miliaris* | 573 | 3968 | native ×1 | Meer |
| 66 | *Lutjanus fulvus* | 569 | 1381 | introduced ×1 | Süß/Brack/Meer |
| 67 | *Sarotherodon melanotheron* | 566 | 423 | introduced ×1 | Süß/Brack/Meer |
| 68 | *Chaetodon multicinctus* | 563 | 4382 | native ×1 | Meer |
| 69 | *Acanthurus xanthopterus* | 543 | 571 | native ×1 | Meer |
| 70 | *Antennarius commerson* | 540 | 491 | native ×1 | Meer |
| 71 | *Bathygobius coalitus* | 506 | 411 | native ×1 | Meer |
| 72 | *Kyphosus cinerascens* | 504 | 514 | native ×1 | Meer |
| 73 | *Arothron hispidus* | 503 | 453 | native ×1 | Brack/Meer |
| 74 | *Triaenodon obesus* | 497 | 1074 | native ×1 | Meer |
| 75 | *Taenianotus triacanthus* | 496 | 442 | native ×1 | Meer |
| 76 | *Acanthurus guttatus* | 480 | 435 | native ×1 | Meer |
| 77 | *Acanthurus achilles* (Quelle: *Acanthurus achilles × nigricans*) | 467 | 920 | native ×1 | Meer |
| 78 | *Gymnothorax undulatus* | 460 | 435 | native ×1 | Brack/Meer |
| 79 | *Monotaxis grandoculis* | 458 | 2705 | native ×1 | Meer |
| 80 | *Aetobatus ocellatus* | 444 | 355 | native ×1 | Brack/Meer |
| 81 | *Gymnomuraena zebra* | 419 | 340 | native ×1 | Meer |
| 82 | *Chaetodon lunulatus* | 408 | 393 | native ×1 | Meer |
| 83 | *Chaetodon ephippium* | 406 | 348 | native ×1 | Meer |
| 84 | *Exallias brevis* | 406 | 647 | native ×1 | Meer |
| 85 | *Anampses cuvier* | 378 | 1850 | native ×1 | Meer |
| 86 | *Parupeneus cyclostomus* | 364 | 1716 | native ×1 | Meer |
| 87 | *Sphyraena barracuda* | 353 | 340 | native ×1 | Brack/Meer |
| 88 | *Chaetodon fremblii* | 352 | 2870 | endemic ×1 | Meer |
| 89 | *Halichoeres ornatissimus* | 348 | 5061 | native ×1 | Meer |
| 90 | *Kyphosus vaigiensis* | 339 | 546 | native ×1 | Meer |
| 91 | *Blenniella gibbifrons* | 337 | 246 | native ×1 | Meer |
| 92 | *Acanthurus dussumieri* | 336 | 2073 | native ×1 | Meer |
| 93 | *Parupeneus insularis* | 334 | 1240 | native ×1 | Meer |
| 94 | *Cirrhitops fasciatus* | 331 | 2596 | native ×1 | Meer |
| 95 | *Pycnochromis vanderbilti* | 328 | 8327 | native ×1 | Meer |
| 96 | *Kuhlia xenura* | 318 | 243 | endemic ×1 | Süß/Brack/Meer |
| 97 | *Pristiapogon kallopterus* | 310 | 675 | native ×1 | Brack/Meer |
| 98 | *Neochirus barberi* | 304 | 86 | native ×1 | Meer |
| 99 | *Diodon holocanthus* | 297 | 269 | native ×1 | Meer |
| 100 | *Platybelone platyura* | 295 | 243 | native ×1 | Meer |
| 101 | *Gymnothorax melatremus* | 291 | 298 | native ×1 | Meer |

### Level 3 (50)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 102 | *Bodianus albotaeniatus* | 290 | 8618 | native ×1 | Meer |
| 103 | *Scorpaenopsis diabolus* | 275 | 255 | native ×1 | Meer |
| 104 | *Thalassoma purpureum* | 258 | 1156 | native ×1 | Meer |
| 105 | *Kuhlia sandvicensis* | 256 | 284 | native ×1 | Süß/Brack/Meer |
| 106 | *Myripristis kuntee* | 245 | 796 | native ×1 | Meer |
| 107 | *Plagiotremus goslinei* | 244 | 1359 | endemic ×1 | Meer |
| 108 | *Centropyge potteri* | 238 | 5832 | native ×1 | Meer |
| 109 | *Neoniphon sammara* | 236 | 771 | native ×1 | Meer |
| 110 | *Canthigaster coronata* | 230 | 921 | endemic ×1 | Meer |
| 111 | *Bothus mancus* | 225 | 176 | native ×1 | Meer |
| 112 | *Neomyxus leuciscus* | 221 | 191 | native ×1 | Brack/Meer |
| 113 | *Aluterus scriptus* | 218 | 211 | native ×1 | Meer |
| 114 | *Forcipiger longirostris* | 216 | 456 | native ×1 | Meer |
| 115 | *Gymnothorax rueppelliae* | 210 | 179 | native ×1 | Brack/Meer |
| 116 | *Macropharyngodon geoffroy* | 207 | 4355 | native ×1 | Meer |
| 117 | *Plectroglyphidodon johnstonianus* | 201 | 5965 | native ×1 | Meer |
| 118 | *Sargocentron punctatissimum* | 201 | 227 | native ×1 | Meer |
| 119 | *Coris venusta* | 200 | 6070 | native ×1 | Meer |
| 120 | *Chaetodon lineolatus* | 198 | 168 | native ×1 | Meer |
| 121 | *Oxycheilinus unifasciatus* | 196 | 2976 | native ×1 | Meer |
| 122 | *Scomberoides lysan* | 193 | 272 | native ×1 | Brack/Meer |
| 123 | *Pycnochromis pacifica* | 192 | 138 | native ×1 | Meer |
| 124 | *Heniochus diphreutes* | 176 | 429 | native ×1 | Meer |
| 125 | *Naso brevirostris* | 174 | 1523 | native ×1 | Meer |
| 126 | *Dactyloptena orientalis* | 169 | 213 | native ×1 | Meer |
| 127 | *Hemitaurichthys polylepis* | 168 | 227 | native ×1 | Meer |
| 128 | *Bothus pantherinus* | 166 | 208 | native ×1 | Meer |
| 129 | *Myripristis berndti* | 162 | 1251 | native ×1 | Meer |
| 130 | *Cheilio inermis* | 161 | 247 | native ×1 | Meer |
| 131 | *Coris flavovittata* | 160 | 1495 | native ×1 | Meer |
| 132 | *Chaetodon kleinii* | 158 | 1197 | native ×1 | Meer |
| 133 | *Cirripectes vanderbilti* | 158 | 1536 | native ×1 | Meer |
| 134 | *Iniistius pavo* | 155 | 178 | native ×1 | Meer |
| 135 | *Parupeneus porphyreus* | 155 | 444 | native ×1 | Meer |
| 136 | *Pseudocheilinus octotaenia* | 150 | 2019 | native ×1 | Meer |
| 137 | *Mugil cephalus* | 147 | 136 | native ×1 | Süß/Brack/Meer |
| 138 | *Antennatus tuberosus* | 145 | 158 | native ×1 | Meer |
| 139 | *Cantherhines sandwichiensis* | 144 | 642 | native ×1 | Meer |
| 140 | *Caranx ignobilis* | 141 | 4002 | native ×1 | Brack/Meer |
| 141 | *Sufflamen fraenatum* | 141 | 2183 | native ×1 | Meer |
| 142 | *Tylosurus crocodilus* | 140 | 154 | native ×1 | Meer |
| 143 | *Lactoria fornasini* | 139 | 255 | native ×1 | Meer |
| 144 | *Acanthurus nigricans* | 134 | 258 | native ×1 | Meer |
| 145 | *Sebastapistes coniorta* | 133 | 279 | native ×1 | Meer |
| 146 | *Carcharhinus galapagensis* | 130 | 841 | native ×1 | Meer |
| 147 | *Chanos chanos* | 127 | 168 | native ×1 | Süß/Brack/Meer |
| 148 | *Echidna polyzona* | 127 | 135 | native ×1 | Meer |
| 149 | *Conger marginatus* | 121 | 128 | native ×1 | Meer |
| 150 | *Pteropterus sphex* | 120 | 63 | endemic ×1 | Meer |
| 151 | *Ctenochaetus hawaiiensis* | 118 | 627 | native ×1 | Meer |

## Grenzfälle

Je 10 Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels sie nehmen (Highlights ab Level 2 übersprungen).

### Level 1/2

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 31 | *Ctenochaetus strigosus* | 1043 | 14130 | native ×1 | Meer | 1 |
| 32 | *Scarus psittacus* | 991 | 3099 | native ×1 | Meer | 1 |
| 33 | *Chlorurus spilurus* | 978 | 8182 | native ×1 | Meer | 1 |
| 34 | *Zebrasoma velifer* | 932 | 1835 | native ×1 | Meer | 1 |
| 35 | *Cirrhitus pinnulatus* | 923 | 1575 | native ×1 | Meer | 1 |
| 36 | *Octopus cyanea* | 917 | 761 | native ×1 | Meer | 1 |
| 37 | *Acanthurus blochii* | 914 | 2291 | native ×1 | Meer | 1 |
| 38 | *Melichthys vidua* | 889 | 2759 | native ×1 | Meer | 1 |
| 39 | *Echidna nebulosa* | 883 | 638 | native ×1 | Meer | 1 |
| 40 | *Sufflamen bursa* | 871 | 5171 | native ×1 | Meer | 1 |
| | **Grenze** | | | | | |
| 41 | *Gymnothorax flavimarginatus* | 856 | 869 | native ×1 | Meer | 2 |
| 42 | *Abudefduf abdominalis* (Quelle: *Abudefduf abdominalis × vaigiensis*) | 847 | 1832 | native ×1 | Meer | 2 |
| 43 | *Gymnothorax eurostus* | 830 | 788 | native ×1 | Meer | 2 |
| 44 | *Cephalopholis argus* | 812 | 2924 | introduced ×1 | Meer | 2 |
| 45 | *Acanthurus leucopareius* | 810 | 3954 | native ×1 | Meer | 2 |
| 46 | *Stethojulis balteata* | 778 | 9474 | native ×1 | Meer | 2 |
| 47 | *Paracirrhites arcatus* | 775 | 9610 | native ×1 | Meer | 2 |
| 48 | *Rhinecanthus aculeatus* | 773 | 608 | native ×1 | Meer | 2 |
| 49 | *Paracirrhites forsteri* | 755 | 2335 | native ×1 | Meer | 2 |
| 50 | *Cantherhines dumerilii* | 750 | 964 | native ×1 | Meer | 2 |

### Level 2/3

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 92 | *Acanthurus dussumieri* | 336 | 2073 | native ×1 | Meer | 2 |
| 93 | *Parupeneus insularis* | 334 | 1240 | native ×1 | Meer | 2 |
| 94 | *Cirrhitops fasciatus* | 331 | 2596 | native ×1 | Meer | 2 |
| 95 | *Pycnochromis vanderbilti* | 328 | 8327 | native ×1 | Meer | 2 |
| 96 | *Kuhlia xenura* | 318 | 243 | endemic ×1 | Süß/Brack/Meer | 2 |
| 97 | *Pristiapogon kallopterus* | 310 | 675 | native ×1 | Brack/Meer | 2 |
| 98 | *Neochirus barberi* | 304 | 86 | native ×1 | Meer | 2 |
| 99 | *Diodon holocanthus* | 297 | 269 | native ×1 | Meer | 2 |
| 100 | *Platybelone platyura* | 295 | 243 | native ×1 | Meer | 2 |
| 101 | *Gymnothorax melatremus* | 291 | 298 | native ×1 | Meer | 2 |
| | **Grenze** | | | | | |
| 102 | *Bodianus albotaeniatus* | 290 | 8618 | native ×1 | Meer | 3 |
| 103 | *Scorpaenopsis diabolus* | 275 | 255 | native ×1 | Meer | 3 |
| 104 | *Thalassoma purpureum* | 258 | 1156 | native ×1 | Meer | 3 |
| 105 | *Kuhlia sandvicensis* | 256 | 284 | native ×1 | Süß/Brack/Meer | 3 |
| 106 | *Myripristis kuntee* | 245 | 796 | native ×1 | Meer | 3 |
| 107 | *Plagiotremus goslinei* | 244 | 1359 | endemic ×1 | Meer | 3 |
| 108 | *Centropyge potteri* | 238 | 5832 | native ×1 | Meer | 3 |
| 109 | *Neoniphon sammara* | 236 | 771 | native ×1 | Meer | 3 |
| 110 | *Canthigaster coronata* | 230 | 921 | endemic ×1 | Meer | 3 |
| 111 | *Bothus mancus* | 225 | 176 | native ×1 | Meer | 3 |

### Level 3/nicht im Deck

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 142 | *Tylosurus crocodilus* | 140 | 154 | native ×1 | Meer | 3 |
| 143 | *Lactoria fornasini* | 139 | 255 | native ×1 | Meer | 3 |
| 144 | *Acanthurus nigricans* | 134 | 258 | native ×1 | Meer | 3 |
| 145 | *Sebastapistes coniorta* | 133 | 279 | native ×1 | Meer | 3 |
| 146 | *Carcharhinus galapagensis* | 130 | 841 | native ×1 | Meer | 3 |
| 147 | *Chanos chanos* | 127 | 168 | native ×1 | Süß/Brack/Meer | 3 |
| 148 | *Echidna polyzona* | 127 | 135 | native ×1 | Meer | 3 |
| 149 | *Conger marginatus* | 121 | 128 | native ×1 | Meer | 3 |
| 150 | *Pteropterus sphex* | 120 | 63 | endemic ×1 | Meer | 3 |
| 151 | *Ctenochaetus hawaiiensis* | 118 | 627 | native ×1 | Meer | 3 |
| | **Grenze** | | | | | |
| 152 | *Heteropriacanthus carolinus* | 118 | – | native ×1 | Meer | – |
| 153 | *Acanthurus nigroris* | 114 | 6666 | native ×1 | ? | – |
| 154 | *Chromis ovalis* | 113 | 2999 | native ×1 | Meer | – |
| 155 | *Eretmochelys imbricata* | 113 | 63 | native ×1 | Brack/Meer | – |
| 156 | *Xanthichthys auromarginatus* | 112 | 318 | native ×1 | Meer | – |
| 157 | *Pseudojuloides cerasinus* | 111 | 1335 | native ×1 | Meer | – |
| 158 | *Sepioteuthis lessoniana* | 108 | 70 | native ×1 | Brack/Meer | – |
| 159 | *Pycnochromis hanui* | 106 | 5219 | endemic ×1 | Meer | – |
| 160 | *Decapterus macarellus* | 104 | 497 | native ×1 | Meer | – |
| 161 | *Scorpaenopsis cacopsis* | 103 | 105 | native ×1 | Meer | – |

## Abgleich mit Führern

Das Rezept nennt keinen Führer.
## Änderungen gegenüber dem bestehenden Deck

- neu: 0
- entfallen: 0

## Ausgeschlossene Kandidaten

<details><summary>192 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Oreochromis mossambicus* | 375 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Awaous stamineus* | 164 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Poecilia reticulata* | 146 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bryaninops yongei* | 134 | Meer | zu klein (höchstens 3.5 cm) |
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
| *Synchiropus corallinus* | 7 | Meer | zu klein (höchstens 3.71 cm) |
| *Cyprinus carpio* | 6 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Misgurnus anguillicaudatus* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pleurosicya larsonae* | 5 | Meer | zu klein (höchstens 1.95 cm) |
| *Torquigener florealis* | 5 | Meer | nur tiefer als die Tauchgrenze (erst ab 90 m) |
| *Antennarius striatus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
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
| *Pseudocaranx dentex* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
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
| *Limia vittata* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
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

## Nicht aufgelöste Namen der Reihenfolge-Quelle

Die Referenz-DB der App kennt diese Namen nicht; die App fände sie auch nicht.

| Name | iNat |
|---|---|
| *Acanthurus sandvicensis* | 3647 |
| *Pinnoctopus ornatus* | 99 |
| *Filistriatus sexfilis* | 56 |
| *Hypostomus* | 19 |
| *Micropterus nigricans* | 14 |
| *Ancistrus* | 12 |
| *Pterygoplichthys* | 9 |
| *Pinnoctopus luteus* | 4 |
| *Rubricatochromis* | 1 |
| *Schindleria* | 1 |
