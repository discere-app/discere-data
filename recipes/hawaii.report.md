# Bericht: Hawaii (`recipes/hawaii.json`)

Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.

- iNaturalist: 544 Taxa (Seiten: 2)
- OBIS: 1625 Arten
- Bild: https://upload.wikimedia.org/wikipedia/commons/thumb/5/52/Reef_Triggerfish_1.JPG/330px-Reef_Triggerfish_1.JPG — Qyd, CC BY 2.5, https://commons.wikimedia.org/wiki/File:Reef_Triggerfish_1.JPG

## Gebiete

- iNaturalist: Hawaii, US (11), Northwestern Hawaiian Islands, US (141380)
- OBIS: Hawaii-Inseln mit den Nordwestlichen Hawaii-Inseln
- FishBase/SeaLifeBase-Verbreitung: 840B, 840:US-HI

## Übersicht

- Arten der Reihenfolge-Quelle, aufgelöst: 533; nicht aufgelöst: 6
- ausgeschlossen: 193
  - zu wenige Nachweise: 139
  - kein Meeresfisch: 39
  - zu klein: 13
  - nur tiefer als die Tauchgrenze: 2
- Kandidaten nach den Filtern: 340
- Deck: 155 Arten (Level 1: 45, Level 2: 60, Level 3: 50); Umfang laut Rezept 40/60/50 plus Highlights
- Highlights: 5 im Deck, 0 verworfen

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

## Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Mobula alfredi* | Der Riffmanta kommt vor Kona nachts ins Lampenlicht, einer der bekanntesten Tauchgänge der Welt. | 62 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Monachus schauinslandi* (Rezept: *Neomonachus schauinslandi*) | Die Hawaii-Mönchsrobbe kommt nur hier vor und ist eine der seltensten Robben der Welt. | – | Verbreitung | Level 1 |
| *Galeocerdo cuvier* | Der Tigerhai ist der große Hai Hawaiis und wird vor Oahu und Maui regelmäßig gesehen. | 203 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
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
| 2 | *Acanthurus triostegus* | 3647 | 8449 | native ×1 | Meer |
| 3 | *Zanclus cornutus* | 2647 | 4560 | native ×1 | Meer |
| 4 | *Thalassoma duperrey* | 2609 | 33754 | native ×1 | Meer |
| 5 | *Zebrasoma flavescens* | 2516 | 7005 | native ×1 | Meer |
| 6 | *Acanthurus nigrofuscus* | 2178 | 13131 | native ×1 | Meer |
| 7 | *Rhinecanthus rectangulus* (Quelle: *Rhinecanthus rectangulus × aculeatus*) | 2177 | 2929 | native ×1 | Meer |
| 8 | *Abudefduf sordidus* | 2146 | 1781 | native ×1 | Brack/Meer |
| 9 | *Naso lituratus* | 2125 | 5753 | native ×1 | Meer |
| 10 | *Ostracion meleagris* | 2108 | 2009 | native ×1 | Meer |
| 11 | *Canthigaster jactator* | 1988 | 7435 | native ×1 | Meer |
| 12 | *Mulloidichthys flavolineatus* | 1797 | 2394 | native ×1 | Meer |
| 13 | *Chaetodon lunula* | 1744 | 1959 | native ×1 | Meer |
| 14 | *Istiblennius zebra* | 1713 | 1263 | endemic ×1 | Meer |
| 15 | *Gymnothorax meleagris* | 1646 | 1499 | native ×1 | Süß/Brack/Meer |
| 16 | *Chaetodon auriga* | 1634 | 2302 | native ×1 | Meer |
| 17 | *Melichthys niger* | 1513 | 3659 | native ×1 | Meer |
| 18 | *Acanthurus olivaceus* | 1506 | 7782 | native ×1 | Meer |
| 19 | *Chaetodon ornatissimus* | 1492 | 3014 | native ×1 | Meer |
| 20 | *Thalassoma trilobatum* | 1487 | 1702 | native ×1 | Meer |
| 21 | *Parupeneus multifasciatus* | 1476 | 10948 | native ×1 | Meer |
| 22 | *Gomphosus varius* | 1415 | 4855 | native ×1 | Meer |
| 23 | *Chaetodon quadrimaculatus* | 1386 | 2355 | native ×1 | Meer |
| 24 | *Scarus rubroviolaceus* | 1347 | 3812 | native ×1 | Meer |
| 25 | *Fistularia commersonii* | 1316 | 1275 | native ×1 | Meer |
| 26 | *Caranx melampygus* | 1303 | 3870 | native ×1 | Brack/Meer |
| 27 | *Aulostomus chinensis* | 1279 | 1815 | native ×1 | Meer |
| 28 | *Coris gaimard* | 1174 | 2426 | native ×1 | Meer |
| 29 | *Dascyllus albisella* | 1142 | 3595 | native ×1 | Meer |
| 30 | *Naso unicornis* | 1064 | 6393 | native ×1 | Meer |
| 31 | *Abudefduf vaigiensis* | 1049 | 1188 | native ×1 | Meer |
| 32 | *Ctenochaetus strigosus* | 1043 | 14130 | native ×1 | Meer |
| 33 | *Scarus psittacus* | 991 | 3099 | native ×1 | Meer |
| 34 | *Chlorurus spilurus* | 978 | 8182 | native ×1 | Meer |
| 35 | *Zebrasoma velifer* | 932 | 1835 | native ×1 | Meer |
| 36 | *Cirrhitus pinnulatus* | 923 | 1575 | native ×1 | Meer |
| 37 | *Octopus cyanea* | 917 | 761 | native ×1 | Meer |
| 38 | *Acanthurus blochii* | 914 | 2291 | native ×1 | Meer |
| 39 | *Melichthys vidua* | 889 | 2759 | native ×1 | Meer |
| 40 | *Echidna nebulosa* | 883 | 638 | native ×1 | Meer |
| 62 | *Mobula alfredi* (Highlight) | 649 | 449 | native ×1 | Süß/Meer |
| – | *Monachus schauinslandi* (Highlight) | – | – | native ×1 | Meer |
| 203 | *Galeocerdo cuvier* (Highlight) | 57 | 42 | native ×1 | Brack/Meer |
| – | *Stenella longirostris* (Highlight) | – | – | native ×1 | Meer |
| – | *Megaptera novaeangliae* (Highlight) | – | – | native ×1 | Meer |

### Level 2 (60)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 41 | *Sufflamen bursa* | 871 | 5171 | native ×1 | Meer |
| 42 | *Gymnothorax flavimarginatus* | 856 | 869 | native ×1 | Meer |
| 43 | *Abudefduf abdominalis* (Quelle: *Abudefduf abdominalis × vaigiensis*) | 847 | 1832 | native ×1 | Meer |
| 44 | *Gymnothorax eurostus* | 830 | 788 | native ×1 | Meer |
| 45 | *Cephalopholis argus* | 812 | 2924 | introduced ×1 | Meer |
| 46 | *Acanthurus leucopareius* | 810 | 3954 | native ×1 | Meer |
| 47 | *Stethojulis balteata* | 778 | 9474 | native ×1 | Meer |
| 48 | *Paracirrhites arcatus* | 775 | 9610 | native ×1 | Meer |
| 49 | *Rhinecanthus aculeatus* | 773 | 608 | native ×1 | Meer |
| 50 | *Paracirrhites forsteri* | 755 | 2335 | native ×1 | Meer |
| 51 | *Cantherhines dumerilii* | 750 | 964 | native ×1 | Meer |
| 52 | *Plectroglyphidodon marginatus* | 712 | 10866 | native ×1 | Meer |
| 53 | *Gymnothorax pictus* | 704 | 437 | native ×1 | Brack/Meer |
| 54 | *Diodon hystrix* | 702 | 588 | native ×1 | Meer |
| 55 | *Forcipiger flavissimus* | 682 | 2188 | native ×1 | Meer |
| 56 | *Labroides phthirophagus* | 665 | 3436 | native ×1 | Meer |
| 57 | *Mulloidichthys vanicolensis* | 665 | 1118 | native ×1 | Meer |
| 58 | *Lutjanus kasmira* | 664 | 2860 | introduced ×1 | Meer |
| 59 | *Arothron meleagris* | 657 | 513 | native ×1 | Meer |
| 60 | *Novaculichthys taeniourus* | 654 | 727 | native ×1 | Meer |
| 61 | *Plectroglyphidodon imparipennis* | 651 | 2927 | native ×1 | Meer |
| 63 | *Calotomus carolinus* | 647 | 1216 | native ×1 | Meer |
| 64 | *Canthigaster amboinensis* | 636 | 919 | native ×1 | Meer |
| 65 | *Chaetodon unimaculatus* | 579 | 907 | native ×1 | Meer |
| 66 | *Chaetodon miliaris* | 573 | 3968 | native ×1 | Meer |
| 67 | *Lutjanus fulvus* | 569 | 1381 | introduced ×1 | Süß/Brack/Meer |
| 68 | *Sarotherodon melanotheron* | 566 | 423 | introduced ×1 | Süß/Brack/Meer |
| 69 | *Chaetodon multicinctus* | 563 | 4382 | native ×1 | Meer |
| 70 | *Acanthurus xanthopterus* | 543 | 571 | native ×1 | Meer |
| 71 | *Antennarius commerson* | 540 | 491 | native ×1 | Meer |
| 72 | *Bathygobius coalitus* | 506 | 411 | native ×1 | Meer |
| 73 | *Kyphosus cinerascens* | 504 | 514 | native ×1 | Meer |
| 74 | *Arothron hispidus* | 503 | 453 | native ×1 | Brack/Meer |
| 75 | *Triaenodon obesus* | 497 | 1074 | native ×1 | Meer |
| 76 | *Taenianotus triacanthus* | 496 | 442 | native ×1 | Meer |
| 77 | *Acanthurus guttatus* | 480 | 435 | native ×1 | Meer |
| 78 | *Acanthurus achilles* (Quelle: *Acanthurus achilles × nigricans*) | 467 | 920 | native ×1 | Meer |
| 79 | *Gymnothorax undulatus* | 460 | 435 | native ×1 | Brack/Meer |
| 80 | *Monotaxis grandoculis* | 458 | 2705 | native ×1 | Meer |
| 81 | *Aetobatus ocellatus* | 444 | 355 | native ×1 | Brack/Meer |
| 82 | *Gymnomuraena zebra* | 419 | 340 | native ×1 | Meer |
| 83 | *Chaetodon lunulatus* | 408 | 393 | native ×1 | Meer |
| 84 | *Chaetodon ephippium* | 406 | 348 | native ×1 | Meer |
| 85 | *Exallias brevis* | 406 | 647 | native ×1 | Meer |
| 86 | *Anampses cuvier* | 378 | 1850 | native ×1 | Meer |
| 87 | *Parupeneus cyclostomus* | 364 | 1716 | native ×1 | Meer |
| 88 | *Sphyraena barracuda* | 353 | 340 | native ×1 | Brack/Meer |
| 89 | *Chaetodon fremblii* | 352 | 2870 | endemic ×1 | Meer |
| 90 | *Halichoeres ornatissimus* | 348 | 5061 | native ×1 | Meer |
| 91 | *Kyphosus vaigiensis* | 339 | 546 | native ×1 | Meer |
| 92 | *Blenniella gibbifrons* | 337 | 246 | native ×1 | Meer |
| 93 | *Acanthurus dussumieri* | 336 | 2073 | native ×1 | Meer |
| 94 | *Parupeneus insularis* | 334 | 1240 | native ×1 | Meer |
| 95 | *Cirrhitops fasciatus* | 331 | 2596 | native ×1 | Meer |
| 96 | *Pycnochromis vanderbilti* | 328 | 8327 | native ×1 | Meer |
| 97 | *Kuhlia xenura* | 318 | 243 | endemic ×1 | Süß/Brack/Meer |
| 98 | *Pristiapogon kallopterus* | 310 | 675 | native ×1 | Brack/Meer |
| 99 | *Neochirus barberi* | 304 | 86 | native ×1 | Meer |
| 100 | *Diodon holocanthus* | 297 | 269 | native ×1 | Meer |
| 101 | *Platybelone platyura* | 295 | 243 | native ×1 | Meer |

### Level 3 (50)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 102 | *Gymnothorax melatremus* | 291 | 298 | native ×1 | Meer |
| 103 | *Bodianus albotaeniatus* | 290 | 8618 | native ×1 | Meer |
| 104 | *Scorpaenopsis diabolus* | 275 | 255 | native ×1 | Meer |
| 105 | *Thalassoma purpureum* | 258 | 1156 | native ×1 | Meer |
| 106 | *Kuhlia sandvicensis* | 256 | 284 | native ×1 | Süß/Brack/Meer |
| 107 | *Myripristis kuntee* | 245 | 796 | native ×1 | Meer |
| 108 | *Plagiotremus goslinei* | 244 | 1359 | endemic ×1 | Meer |
| 109 | *Centropyge potteri* | 238 | 5832 | native ×1 | Meer |
| 110 | *Neoniphon sammara* | 236 | 771 | native ×1 | Meer |
| 111 | *Canthigaster coronata* | 230 | 921 | endemic ×1 | Meer |
| 112 | *Bothus mancus* | 225 | 176 | native ×1 | Meer |
| 113 | *Neomyxus leuciscus* | 221 | 191 | native ×1 | Brack/Meer |
| 114 | *Aluterus scriptus* | 218 | 211 | native ×1 | Meer |
| 115 | *Forcipiger longirostris* | 216 | 456 | native ×1 | Meer |
| 116 | *Gymnothorax rueppelliae* | 210 | 179 | native ×1 | Brack/Meer |
| 117 | *Macropharyngodon geoffroy* | 207 | 4355 | native ×1 | Meer |
| 118 | *Plectroglyphidodon johnstonianus* | 201 | 5965 | native ×1 | Meer |
| 119 | *Sargocentron punctatissimum* | 201 | 227 | native ×1 | Meer |
| 120 | *Coris venusta* | 200 | 6070 | native ×1 | Meer |
| 121 | *Chaetodon lineolatus* | 198 | 168 | native ×1 | Meer |
| 122 | *Oxycheilinus unifasciatus* | 196 | 2976 | native ×1 | Meer |
| 123 | *Scomberoides lysan* | 193 | 272 | native ×1 | Brack/Meer |
| 124 | *Pycnochromis pacifica* | 192 | 138 | native ×1 | Meer |
| 125 | *Heniochus diphreutes* | 176 | 429 | native ×1 | Meer |
| 126 | *Naso brevirostris* | 174 | 1523 | native ×1 | Meer |
| 127 | *Dactyloptena orientalis* | 169 | 213 | native ×1 | Meer |
| 128 | *Hemitaurichthys polylepis* | 168 | 227 | native ×1 | Meer |
| 129 | *Bothus pantherinus* | 166 | 208 | native ×1 | Meer |
| 130 | *Myripristis berndti* | 162 | 1251 | native ×1 | Meer |
| 131 | *Cheilio inermis* | 161 | 247 | native ×1 | Meer |
| 132 | *Coris flavovittata* | 160 | 1495 | native ×1 | Meer |
| 133 | *Chaetodon kleinii* | 158 | 1197 | native ×1 | Meer |
| 134 | *Cirripectes vanderbilti* | 158 | 1536 | native ×1 | Meer |
| 135 | *Iniistius pavo* | 155 | 178 | native ×1 | Meer |
| 136 | *Parupeneus porphyreus* | 155 | 444 | native ×1 | Meer |
| 137 | *Pseudocheilinus octotaenia* | 150 | 2019 | native ×1 | Meer |
| 138 | *Mugil cephalus* | 147 | 136 | native ×1 | Süß/Brack/Meer |
| 139 | *Antennatus tuberosus* | 145 | 158 | native ×1 | Meer |
| 140 | *Cantherhines sandwichiensis* | 144 | 642 | native ×1 | Meer |
| 141 | *Caranx ignobilis* | 141 | 4002 | native ×1 | Brack/Meer |
| 142 | *Sufflamen fraenatum* | 141 | 2183 | native ×1 | Meer |
| 143 | *Tylosurus crocodilus* | 140 | 154 | native ×1 | Meer |
| 144 | *Lactoria fornasini* | 139 | 255 | native ×1 | Meer |
| 145 | *Acanthurus nigricans* | 134 | 258 | native ×1 | Meer |
| 146 | *Sebastapistes coniorta* | 133 | 279 | native ×1 | Meer |
| 147 | *Carcharhinus galapagensis* | 130 | 841 | native ×1 | Meer |
| 148 | *Chanos chanos* | 127 | 168 | native ×1 | Süß/Brack/Meer |
| 149 | *Echidna polyzona* | 127 | 135 | native ×1 | Meer |
| 150 | *Conger marginatus* | 121 | 128 | native ×1 | Meer |
| 151 | *Pteropterus sphex* | 120 | 63 | endemic ×1 | Meer |

## Grenzfälle

Je 10 Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels sie nehmen (Highlights ab Level 2 übersprungen).

### Level 1/2

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 31 | *Abudefduf vaigiensis* | 1049 | 1188 | native ×1 | Meer | 1 |
| 32 | *Ctenochaetus strigosus* | 1043 | 14130 | native ×1 | Meer | 1 |
| 33 | *Scarus psittacus* | 991 | 3099 | native ×1 | Meer | 1 |
| 34 | *Chlorurus spilurus* | 978 | 8182 | native ×1 | Meer | 1 |
| 35 | *Zebrasoma velifer* | 932 | 1835 | native ×1 | Meer | 1 |
| 36 | *Cirrhitus pinnulatus* | 923 | 1575 | native ×1 | Meer | 1 |
| 37 | *Octopus cyanea* | 917 | 761 | native ×1 | Meer | 1 |
| 38 | *Acanthurus blochii* | 914 | 2291 | native ×1 | Meer | 1 |
| 39 | *Melichthys vidua* | 889 | 2759 | native ×1 | Meer | 1 |
| 40 | *Echidna nebulosa* | 883 | 638 | native ×1 | Meer | 1 |
| | **Grenze** | | | | | |
| 41 | *Sufflamen bursa* | 871 | 5171 | native ×1 | Meer | 2 |
| 42 | *Gymnothorax flavimarginatus* | 856 | 869 | native ×1 | Meer | 2 |
| 43 | *Abudefduf abdominalis* (Quelle: *Abudefduf abdominalis × vaigiensis*) | 847 | 1832 | native ×1 | Meer | 2 |
| 44 | *Gymnothorax eurostus* | 830 | 788 | native ×1 | Meer | 2 |
| 45 | *Cephalopholis argus* | 812 | 2924 | introduced ×1 | Meer | 2 |
| 46 | *Acanthurus leucopareius* | 810 | 3954 | native ×1 | Meer | 2 |
| 47 | *Stethojulis balteata* | 778 | 9474 | native ×1 | Meer | 2 |
| 48 | *Paracirrhites arcatus* | 775 | 9610 | native ×1 | Meer | 2 |
| 49 | *Rhinecanthus aculeatus* | 773 | 608 | native ×1 | Meer | 2 |
| 50 | *Paracirrhites forsteri* | 755 | 2335 | native ×1 | Meer | 2 |

### Level 2/3

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 92 | *Blenniella gibbifrons* | 337 | 246 | native ×1 | Meer | 2 |
| 93 | *Acanthurus dussumieri* | 336 | 2073 | native ×1 | Meer | 2 |
| 94 | *Parupeneus insularis* | 334 | 1240 | native ×1 | Meer | 2 |
| 95 | *Cirrhitops fasciatus* | 331 | 2596 | native ×1 | Meer | 2 |
| 96 | *Pycnochromis vanderbilti* | 328 | 8327 | native ×1 | Meer | 2 |
| 97 | *Kuhlia xenura* | 318 | 243 | endemic ×1 | Süß/Brack/Meer | 2 |
| 98 | *Pristiapogon kallopterus* | 310 | 675 | native ×1 | Brack/Meer | 2 |
| 99 | *Neochirus barberi* | 304 | 86 | native ×1 | Meer | 2 |
| 100 | *Diodon holocanthus* | 297 | 269 | native ×1 | Meer | 2 |
| 101 | *Platybelone platyura* | 295 | 243 | native ×1 | Meer | 2 |
| | **Grenze** | | | | | |
| 102 | *Gymnothorax melatremus* | 291 | 298 | native ×1 | Meer | 3 |
| 103 | *Bodianus albotaeniatus* | 290 | 8618 | native ×1 | Meer | 3 |
| 104 | *Scorpaenopsis diabolus* | 275 | 255 | native ×1 | Meer | 3 |
| 105 | *Thalassoma purpureum* | 258 | 1156 | native ×1 | Meer | 3 |
| 106 | *Kuhlia sandvicensis* | 256 | 284 | native ×1 | Süß/Brack/Meer | 3 |
| 107 | *Myripristis kuntee* | 245 | 796 | native ×1 | Meer | 3 |
| 108 | *Plagiotremus goslinei* | 244 | 1359 | endemic ×1 | Meer | 3 |
| 109 | *Centropyge potteri* | 238 | 5832 | native ×1 | Meer | 3 |
| 110 | *Neoniphon sammara* | 236 | 771 | native ×1 | Meer | 3 |
| 111 | *Canthigaster coronata* | 230 | 921 | endemic ×1 | Meer | 3 |

### Level 3/nicht im Deck

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 142 | *Sufflamen fraenatum* | 141 | 2183 | native ×1 | Meer | 3 |
| 143 | *Tylosurus crocodilus* | 140 | 154 | native ×1 | Meer | 3 |
| 144 | *Lactoria fornasini* | 139 | 255 | native ×1 | Meer | 3 |
| 145 | *Acanthurus nigricans* | 134 | 258 | native ×1 | Meer | 3 |
| 146 | *Sebastapistes coniorta* | 133 | 279 | native ×1 | Meer | 3 |
| 147 | *Carcharhinus galapagensis* | 130 | 841 | native ×1 | Meer | 3 |
| 148 | *Chanos chanos* | 127 | 168 | native ×1 | Süß/Brack/Meer | 3 |
| 149 | *Echidna polyzona* | 127 | 135 | native ×1 | Meer | 3 |
| 150 | *Conger marginatus* | 121 | 128 | native ×1 | Meer | 3 |
| 151 | *Pteropterus sphex* | 120 | 63 | endemic ×1 | Meer | 3 |
| | **Grenze** | | | | | |
| 152 | *Ctenochaetus hawaiiensis* | 118 | 627 | native ×1 | Meer | – |
| 153 | *Heteropriacanthus carolinus* | 118 | – | native ×1 | Meer | – |
| 154 | *Acanthurus nigroris* | 114 | 6666 | native ×1 | ? | – |
| 155 | *Chromis ovalis* | 113 | 2999 | native ×1 | Meer | – |
| 156 | *Eretmochelys imbricata* | 113 | 63 | native ×1 | Brack/Meer | – |
| 157 | *Xanthichthys auromarginatus* | 112 | 318 | native ×1 | Meer | – |
| 158 | *Pseudojuloides cerasinus* | 111 | 1335 | native ×1 | Meer | – |
| 159 | *Sepioteuthis lessoniana* | 108 | 70 | native ×1 | Brack/Meer | – |
| 160 | *Pycnochromis hanui* | 106 | 5219 | endemic ×1 | Meer | – |
| 161 | *Decapterus macarellus* | 104 | 497 | native ×1 | Meer | – |

## Abgleich mit Führern

Das Rezept nennt keinen Führer.
## Ausgeschlossene Kandidaten

<details><summary>193 Arten</summary>

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

## Subdeck `invertebrates` (40)

Eigene Taxa, Größe und Filter, Reihenfolge-Quelle und Region des Rezepts. Arten, die schon in einem Level oder einem früheren Subdeck stehen, bleiben draußen; die Führer werden nicht abgeglichen.

- iNaturalist: 1570 Taxa (Seiten: 4)
- OBIS: 3748 Arten

### iNaturalist-Namen zugeordnet

Laut `recipes/inat_names.json`: iNaturalist nennt die Art anders als die Referenz-DB; die Zählung kommt zu der der Referenz-DB-Art.

| iNaturalist | Referenz-DB | iNat | Art | Beleg |
|---|---|---|---|---|
| *Pinnoctopus ornatus* | *Callistoctopus ornatus* | 99 | Umbenennung | https://www.inaturalist.org/taxon_changes/172615 |
| *Pinnoctopus luteus* | *Callistoctopus luteus* | 4 | Umbenennung | https://www.inaturalist.org/taxon_changes/172616 |

### Von Hand ausgeschlossen

| Art | iNat | Grund |
|---|---|---|
| *Grapsus tenuicrustatus* | 4601 | Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen. |
| *Nerita picea* | 1464 | Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Littoraria pintado* | 1158 | Strandschnecke der Spritzwasserzone, sitzt über dem Wasser auf den Uferfelsen. |
| *Veronicella cubensis* | 659 | Landnacktschnecke, kein Meerestier. |
| *Ocypode pallidula* | 655 | Geisterkrabbe, lebt am trockenen Sandstrand. |
| *Metopograpsus thukuhar* | 461 | Uferkrabbe der Felsküste und Hafenmauern, lebt in der Gezeitenzone über dem Wasser. |
| *Cellana exarata* | 424 | Napfschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Grapsus longitarsis* | 348 | Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen. |
| *Nerita polita* | 280 | Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Trochus intextus* | 251 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 27 von 29 Beobachtungen mit Angabe „tot“). |
| *Echinolittorina hawaiiensis* | 212 | Strandschnecke der Spritzwasserzone, sitzt über dem Wasser auf den Uferfelsen. |

### Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Hymenocera picta* | Die Harlekingarnele frisst nur Seesterne und ist einer der begehrtesten Funde für Unterwasserfotografen. | 114 | Reihenfolge-Quelle, OBIS, Verbreitung | invertebrates |
| *Charonia tritonis* | Das Tritonshorn frisst Dornenkronen-Seesterne und ist selten geworden, weil seine Schale begehrt ist. | 112 | Reihenfolge-Quelle, OBIS, Verbreitung | invertebrates |
| *Panulirus marginatus* | Die Hawaii-Languste lebt nur auf Hawaii und versteckt sich tagsüber in Riffhöhlen. | 134 | Reihenfolge-Quelle, OBIS, Verbreitung | invertebrates |

### Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS oder Verbreitung): 40/40 (100 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 3: *Halgerda terramtuentis*, *Calcinus pictus*, *Panulirus marginatus*
- Arten ohne Volksnamen `de` in der Referenz-DB: 31/40 (78 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 4/40 (10 %)
- Familien ohne Volksnamen `de`: 25/25 (100 %): *Acanthasteridae*, *Acroporidae*, *Aglajidae*, *Aplustridae*, *Aplysiidae*, *Chromodorididae*, *Cypraeidae*, *Diadematidae*, *Diogenidae*, *Dorididae*, *Echinometridae*, *Facelinidae*, *Holothuriidae*, *Notarchidae*, *Ophidiasteridae*, *Oreasteridae*, *Palaemonidae*, *Palinuridae*, *Phyllidiidae*, *Physaliidae*, *Pocilloporidae*, *Ranellidae*, *Stenopodidae*, *Toxopneustidae*, *Zoanthidae*
- Familien ohne Volksnamen `en`: 16/25 (64 %): *Acroporidae*, *Aglajidae*, *Aplustridae*, *Chromodorididae*, *Diadematidae*, *Dorididae*, *Echinometridae*, *Facelinidae*, *Notarchidae*, *Ophidiasteridae*, *Oreasteridae*, *Phyllidiidae*, *Physaliidae*, *Pocilloporidae*, *Toxopneustidae*, *Zoanthidae*

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

Keine.

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

Keine.

### Arten

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Klasse |
|---|---|---|---|---|---|---|
| 1 | *Echinometra mathaei* | 2812 | 3033 | native ×1 | Meer | Echinoidea |
| 2 | *Actinopyga varians* | 2445 | 1718 | – | Meer | Holothuroidea |
| 3 | *Colobocentrotus atratus* | 2199 | – | native ×1 | Meer | Echinoidea |
| 4 | *Heterocentrotus mamillatus* | 2093 | 1762 | native ×1 | Meer | Echinoidea |
| 5 | *Calcinus seurati* | 1144 | 834 | native ×1 | Meer | Malacostraca |
| 6 | *Tripneustes gratilla* | 1131 | 910 | native ×1 | Meer | Echinoidea |
| 7 | *Holothuria atra* | 861 | 2011 | native ×1 | Meer | Holothuroidea |
| 8 | *Physalia physalis* (Quelle: *Physalia utriculus*) | 778 | 510 | native ×1 | Meer | Hydrozoa |
| 9 | *Hypselodoris imperialis* | 761 | 677 | native ×1 | Meer | Gastropoda |
| 10 | *Diadema savignyi* | 736 | 515 | – | Meer | Echinoidea |
| 11 | *Pocillopora meandrina* | 727 | 11378 | native ×1 | Meer | Hexacorallia |
| 12 | *Cypraea mauritiana* (Quelle: *Mauritia mauritiana*) | 701 | 495 | native ×1 | Meer | Gastropoda |
| 13 | *Culcita novaeguineae* | 676 | 513 | – | Meer | Asteroidea |
| 14 | *Halgerda terramtuentis* | 672 | 626 | endemic ×1 | Meer | Gastropoda |
| 15 | *Stenopus hispidus* | 669 | 567 | native ×1 | Meer | Malacostraca |
| 16 | *Phyllidiella pustulosa* | 645 | 557 | native ×1 | Meer | Gastropoda |
| 17 | *Glossodoris rufomarginata* | 632 | 558 | native ×1 | Meer | Gastropoda |
| 18 | *Calcinus laevimanus* | 580 | 426 | native ×1 | Meer | Malacostraca |
| 19 | *Echinothrix calamaris* | 563 | 468 | native ×1 | Meer | Echinoidea |
| 20 | *Palythoa tuberculosa* | 547 | 437 | native ×1 | Meer | Hexacorallia |
| 21 | *Echinothrix diadema* | 454 | 439 | native ×1 | Meer | Echinoidea |
| 22 | *Goniobranchus vibratus* | 426 | 380 | native ×1 | Meer | Gastropoda |
| 23 | *Calcinus pictus* | 423 | 324 | endemic ×1 | Meer | Malacostraca |
| 24 | *Phyllidia varicosa* | 398 | 351 | native ×1 | Meer | Gastropoda |
| 25 | *Echinometra oblonga* | 391 | 297 | native ×1 | Meer | Echinoidea |
| 26 | *Montipora capitata* | 388 | 17710 | native ×1 | Meer | Hexacorallia |
| 27 | *Pteraeolidia ianthina* (Quelle: *Pteraeolidia semperi*) | 383 | 444 | native ×1 | Meer | Gastropoda |
| 28 | *Mauritia maculifera* | 377 | 313 | native ×1 | Meer | Gastropoda |
| 29 | *Linckia multifora* | 373 | 662 | native ×1 | Meer | Asteroidea |
| 30 | *Holothuria whitmaei* | 360 | 1617 | – | Meer | Holothuroidea |
| 31 | *Ardeadoris tomsmithi* | 347 | 322 | native ×1 | Meer | Gastropoda |
| 32 | *Acanthaster planci* (Quelle: *Acanthaster solaris*) | 338 | 585 | native ×1 | Meer | Asteroidea |
| 33 | *Hydatina amplustre* | 313 | 250 | native ×1 | Meer | Gastropoda |
| 34 | *Aplysia argus* | 309 | 198 | native ×1 | Meer | Gastropoda |
| 35 | *Luria isabella* | 309 | 308 | – | Meer | Gastropoda |
| 36 | *Stylocheilus longicauda* (Quelle: *Stylocheilus striatus*) | 301 | 255 | – | Meer | Gastropoda |
| 37 | *Chelidonura hirundinina* | 297 | 259 | native ×1 | Meer | Gastropoda |
| 112 | *Charonia tritonis* (Highlight) | 105 | 123 | native ×1 | Meer | Gastropoda |
| 114 | *Hymenocera picta* (Highlight) | 103 | 87 | native ×1 | Meer | Malacostraca |
| 134 | *Panulirus marginatus* (Highlight) | 86 | 675 | endemic ×1 | Meer | Malacostraca |

### Grenzfälle

Je 10 Arten vor und nach der Grenze (Highlights übersprungen).

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Klasse | Im Subdeck |
|---|---|---|---|---|---|---|---|
| 28 | *Mauritia maculifera* | 377 | 313 | native ×1 | Meer | Gastropoda | ja |
| 29 | *Linckia multifora* | 373 | 662 | native ×1 | Meer | Asteroidea | ja |
| 30 | *Holothuria whitmaei* | 360 | 1617 | – | Meer | Holothuroidea | ja |
| 31 | *Ardeadoris tomsmithi* | 347 | 322 | native ×1 | Meer | Gastropoda | ja |
| 32 | *Acanthaster planci* (Quelle: *Acanthaster solaris*) | 338 | 585 | native ×1 | Meer | Asteroidea | ja |
| 33 | *Hydatina amplustre* | 313 | 250 | native ×1 | Meer | Gastropoda | ja |
| 34 | *Aplysia argus* | 309 | 198 | native ×1 | Meer | Gastropoda | ja |
| 35 | *Luria isabella* | 309 | 308 | – | Meer | Gastropoda | ja |
| 36 | *Stylocheilus longicauda* (Quelle: *Stylocheilus striatus*) | 301 | 255 | – | Meer | Gastropoda | ja |
| 37 | *Chelidonura hirundinina* | 297 | 259 | native ×1 | Meer | Gastropoda | ja |
| | **Grenze** | | | | | | |
| 38 | *Tambja morosa* | 297 | 259 | native ×1 | Meer | ? | nein |
| 39 | *Thorunna daniellae* | 297 | 281 | – | Meer | ? | nein |
| 40 | *Mithrodia fisheri* | 294 | 441 | endemic ×1 | Meer | ? | nein |
| 41 | *Plakobranchus ocellatus* | 293 | 330 | native ×1 | Meer | ? | nein |
| 42 | *Andresia partenopea* (Quelle: *Exaiptasia diaphana*) | 284 | 207 | – | Meer | ? | nein |
| 43 | *Conus ebraeus* | 284 | 259 | native ×1 | Meer | ? | nein |
| 44 | *Holothuria cinerascens* | 281 | 222 | native ×1 | Meer | ? | nein |
| 45 | *Parribacus antarcticus* | 277 | 216 | native ×1 | Meer | ? | nein |
| 46 | *Cypraea tigris* | 274 | 166 | native ×1 | Meer | ? | nein |
| 47 | *Panulirus penicillatus* | 267 | 572 | native ×1 | Meer | ? | nein |

### Ausgeschlossene Kandidaten

<details><summary>481 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Grapsus tenuicrustatus* | 4601 | Meer | von Hand ausgeschlossen (Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen.) |
| *Nerita picea* | 1464 | Meer | von Hand ausgeschlossen (Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Littoraria pintado* | 1158 | Meer | von Hand ausgeschlossen (Strandschnecke der Spritzwasserzone, sitzt über dem Wasser auf den Uferfelsen.) |
| *Octopus cyanea* | 917 | Meer | schon in einem anderen Subdeck (level-1) |
| *Veronicella cubensis* | 659 | Meer | von Hand ausgeschlossen (Landnacktschnecke, kein Meerestier.) |
| *Ocypode pallidula* | 655 | Meer | von Hand ausgeschlossen (Geisterkrabbe, lebt am trockenen Sandstrand.) |
| *Metopograpsus thukuhar* | 461 | Brack/Meer | von Hand ausgeschlossen (Uferkrabbe der Felsküste und Hafenmauern, lebt in der Gezeitenzone über dem Wasser.) |
| *Cellana exarata* | 424 | Meer | von Hand ausgeschlossen (Napfschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Grapsus longitarsis* | 348 | Meer | von Hand ausgeschlossen (Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen.) |
| *Nerita polita* | 280 | Meer | von Hand ausgeschlossen (Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Macrobrachium lar* | 258 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trochus intextus* | 251 | Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 27 von 29 Beobachtungen mit Angabe „tot“).) |
| *Echinolittorina hawaiiensis* | 212 | Meer | von Hand ausgeschlossen (Strandschnecke der Spritzwasserzone, sitzt über dem Wasser auf den Uferfelsen.) |
| *Pomacea canaliculata* | 198 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Procambarus clarkii* | 139 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Corbicula fluminea* | 69 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Palaemon debilis* | 69 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Halocaridina rubra* | 51 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Melanoides tuberculatus* | 30 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
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
| *Callistoctopus luteus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
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
| *Lysiosquillina maculata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
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
| *Sthenoteuthis oualaniensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
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
| *Cypraea carneola* | 3 | Meer | zu wenige Nachweise (3 < 5) |
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
| *Homalacantha anatomica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
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
| *Argonauta argo* | 2 | Meer | zu wenige Nachweise (2 < 5) |
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
| *Enoplometopus holthuisi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
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
| *Octopus bocki* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Odostomia stearnsiella* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Oenone fulgida* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ommastrephes bartramii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
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
| *Tellina robusta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tellinella crucigera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Terebra argus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Thor spinosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Thysanoteuthis rhombus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tremoctopus gracilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trichorhina heterophthalma* | 2 | ? | zu wenige Nachweise (2 < 5) |
| *Tritonoturris cumingii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tweedieia laysani* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Usilla avenacea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vanikoro cancellata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vexillum diutenerum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Xenuroturris kingae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora cytherea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aegires exeches* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aliculastrum cylindricum* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Alpheus rapacida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alvania isolata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amorphinopsis excavans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anarithma metula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ancistrocheirus lesueurii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
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
| *Cypraea ventriculus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
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
| *Hyaloteuthis pelagica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
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
| *Mycale parishi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
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
| *Ostrea capsa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
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

<details><summary>426 Namen</summary>

*Lissachatina fulica* (4692), *Monetaria caputophidii* (1167), *Laevicaulis alte* (673), *Ocypode urvillii* (539), *Euglandina rosea* (524), *Hypselodoris peasei* (398), *Isognomon californicus* (328), *Coryphellina exoptata* (291), *Hexabranchus sandwichensis* (281), *Thorunna kahuna* (276), *Hexabranchus aureomarginatus* (245), *Arakawania granulata* (240), *Naria helvola* (188), *Bradybaena similaris* (170), *Hiatodoris fellowsi* (165), *Parmarion martensi* (161), *Aplysia elongata* (146), *Samla bicolor* (146), *Chelidonura alisonae* (141), *Peronia platei* (136), *Limax maximus* (130), *Sistrum ricinus* (130), *Ovachlamys fulgens* (121), *Goniosupradens hawaiensis* (117), *Meghimatium bilineatum* (115), *Hypselodoris violabranchia* (113), *Pseudoceros paralaticlavus* (112), *Breviturma pica* (104), *Danarma obtusifrons* (100), *Armadillidium vulgare* (98), *Maculastrombus maculatus* (98), *Lamarcka ventricosa* (95), *Ardeadoris poliahu* (82), *Elasmias luakahaense* (81), *Corallianassa oahuensis* (74), *Zoanthus kuroshio* (67), *Achatinella mustelina* (62), *Peasiella tantilla* (59), *Thranita crenata* (58), *Marioniopsis hawaiiensis* (57), *Thysanozoon tentaculatum* (57), *Partulina mighelsiana* (51), *Ricinella rubusidaeus* (50), *Tenellia nakapila* (47), *Homalopoma verruca* (44), *Neocaridina davidi* (44), *Subulina octona* (44), *Vasticardium hawaiense* (42), *Auriculella diaphana* (41), *Cornu aspersum* (41), *Breviturma brevipes* (40), *Dendrodoris krusensternii* (40), *Siphopteron quadrispinosum* (40), *Zenopontonia soror* (40), *Portunus hawaiiensis* (38), *Pleurobranchus varians* (37), *Dardanus sanguinolentus* (34), *Philonesia chamissoi* (34), *Bostrycapulus calyptraeiformis* (31), *Siphonaria nuttallii* (30), *Tayloria kibweziensis* (30), *Noumeaella rehderi* (29), *Naria poraria* (27), *Phycophila euchlora* (27), *Breviturma dentata* (26), *Goniosupradens erythrodactylus* (26), *Auriculella perpusilla* (25), *Ecmanis ignea* (25), *Nodolatirus nodatus* (25), *Vexillum adamsi* (25), *Sclerophytum densa* (24), *Philonesia hartmanni* (23), *Pleurehdera pellucida* (23), *Bulla peasiana* (22), *Terebra achates* (22), *Nesobornia hawaiensis* (21), *Triops longicaudatus* (21), *Breviturma krohi* (19), *Echinocyamus incertus* (19), *Phidiana semidecora* (19), *Scopalina hapalia* (19), *Tauphaedusa tau* (19), *Venezillo parvus* (19), *Hypselodoris insulana* (18), *Microcollonia rubricincta* (18), *Elysia nealae* (17), *Succinea newcombiana* (17), *Imbricariopsis punctata* (16), *Ligia rolliensis* (16), *Polygyra cereolus* (16), *Pseudoceros leptostictus* (16), *Reductoniscus costulatus* (16), *Catinella rotundata* (15), *Percnon sinense* (15), *Amplidrupa aperta* (14), *Arion intermedius* (14), *Clathria mima* (14), *Isarachnanthus bandanensis* (14), *Limenandra rosanae* (14), *Myurella pygmaea* (14), *Nebularia ferruginea* (14), *Pseudobiceros splendidus* (14), *Spondylus violacescens* (14), *Strigatella aurora* (14), *Bermudella pellucida* (13), *Condylomitra tuberosa* (13), *Cubaris murina* (13), *Eupusia lauta* (13), *Limenandra confusa* (13), *Oliva ozodona* (13), *Succinea cepulla* (13), *Aliculastrum debile* (12), *Partulina semicarinata* (12), *Pleurolidia juliae* (12), *Scabricola olivaeformis* (12), *Zachrysia provisoria* (12), *Baeolidia moebii* (11), *Deroceras laeve* (11), *Gyroscala commutata* (11), *Hastula inconstans* (11), *Kermidaphnella pumila* (11), *Xiphonectes longispinosus* (11), *Auriculella turritella* (10), *Casmaria kayae* (10), *Hiloa variabilis* (10), *Homalocantha pele* (10), *Longchaeus maculosus* (10), *Siphopteron flavum* (10), *Thuridilla kathae* (10), *Allopeas clavulinum* (9), *Burmoniscus mauritiensis* (9), *Carelia cochlea* (9), *Conus peasei* (9), *Cyerce liliuokalaniae* (9), *Elasmias fuscum* (9), *Halgerda paliensis* (9), *Hiona exaequata* (9), *Ligia kamehameha* (9), *Lytocarpia nigra* (9), *Paropeas achatinaceum* (9), *Partulina redfieldi* (9), *Pseudobiceros gratus* (9), *Pseudobiceros stellae* (9), *Achatinella pulcherrima* (8), *Andvakia discipulorum* (8), *Elysia lobata* (8), *Hawaiistrombus hellii* (8), *Ligia mauinuiensis* (8), *Nebularia incompta* (8), *Tonna hawaiiensis* (8), *Achatinella fulgens* (7), *Auriculella armata* (7), *Deroceras reticulatum* (7), *Perdicella helena* (7), *Achatinella lorata* (6), *Atagema scabriuscula* (6), *Auriculella ambusta* (6), *Calliasmata pholidota* (6), *Coralliophila cumingii* (6), *Gastrocopta servilis* (6), *Nemalecium caeruleus* (6), *Partulina proxima* (6), *Partulina rufa* (6), *Phyllamphion elegans* (6), *Platorchestia pickeringi* (6), *Pseudonebularia cucumerina* (6), *Thuridilla multimarginata* (6), *Tornatellides kilauea* (6), *Aegires lemoncello* (5), *Auriculella crassula* (5), *Coscinasterias acutispina* (5), *Hiona pilsbryi* (5), *Laminella gravida* (5), *Mieniplotia scabra* (5), *Paradaphne interrupta* (5), *Partulina variabilis* (5), *Phyllodesmium undulatum* (5), *Placida barackobamai* (5), *Plesiothyreus scobinatus* (5), *Pseudoceros scintillatus* (5), *Siphonaria undans* (5), *Strigatella luctuosa* (5), *Tornatellides procerulus* (5), *Achatinella apexfulva* (4), *Achatinella viridans* (4), *Asterodiscides tuberculosus* (4), *Batzella melanos* (4), *Bulbaeolidia paulae* (4), *Bulimulus guadalupensis* (4), *Doris nucleola* (4), *Euprotomus hawaiensis* (4), *Herviella mietta* (4), *Hypselodoris paulinae* (4), *Janolus toyamensis* (4), *Lamellidea polygnampta* (4), *Lampasopsis cruentata* (4), *Launsina rubropurpurata* (4), *Microcollonia candida* (4), *Moloha major* (4), *Nebularia pellisserpentis* (4), *Oxymeris suffusa* (4), *Paragiopagurus laperousei* (4), *Pedipes sandwicensis* (4), *Pelagella joubini* (4), *Ptilocaulis spiculifer* (4), *Rissoella confusa* (4), *Sclerodoris rubicunda* (4), *Semicassis umbilicata* (4), *Tomoberthella martensi* (4), *Achatinella stewartii* (3), *Achatinella vulpina* (3), *Amastra rugulosa* (3), *Anteaeolidiella cacaotica* (3), *Astropecten hawaiiensis* (3), *Auriculella tenella* (3), *Elasmias anceyanum* (3), *Geograpsus* (3), *Isognomon incisus* (3), *Jorunna ramicola* (3), *Leiosolenus mucronatus* (3), *Levicaris mammillata* (3), *Ligia dante* (3), *Lyncina propinqua* (3), *Mastoniaeforis hinuhinu* (3), *Namalycastis hawaiiensis* (3), *Nebularia fastigium* (3), *Pacificella baldwini* (3), *Paraplanocera marginata* (3), *Partulina perdix* (3), *Pseudoceros bolool* (3), *Pseudoceros rubronanus* (3), *Roxaniella pittmani* (3), *Siphonaria mauiensis* (3), *Strigatella pudica* (3), *Subulophora peasei* (3), *Succinea caduca* (3), *Succinea konaensis* (3), *Succinea thaanumi* (3), *Tytthosoceros nocturnus* (3), *Volvarina unilineata* (3), *Abronica turon* (2), *Achatinella abbreviata* (2), *Achatinella bellula* (2), *Achatinella bulimoides* (2), *Achatinella sowerbyana* (2), *Agathotoma mighelsi* (2), *Auriculella uniplicata* (2), *Avaldesia tamatoa* (2), *Berthella caledonica* (2), *Cardita excisa* (2), *Carelia dolei* (2), *Carelia evelynae* (2), *Carelia necra* (2), *Carinomitra saltata* (2), *Cerithiopsis granata* (2), *Cleotrivia globosa* (2), *Cliona caesia* (2), *Costasiella formicaria* (2), *Dulcerana granularis* (2), *Euapta tahitiensis* (2), *Eubranchus* (2), *Glaucilla marginata* (2), *Glaucilla mcfarlanei* (2), *Hastula betsyae* (2), *Hermania orca* (2), *Kaala subrutila* (2), *Kellia hawaiensis* (2), *Leucascus flavus* (2), *Limacus flavus* (2), *Litharium maculatum* (2), *Lytocarpia phyteuma* (2), *Maritigrella eschara* (2), *Mastoniaeforis ordinata* (2), *Melanella kanaka* (2), *Milax gagates* (2), *Mnestia villica* (2), *Oppomorus funiculatus* (2), *Orphanopusia patriarchalis* (2), *Pacifilux rubra* (2), *Paradaphne ornata* (2), *Pherecardia distincta* (2), *Phrikoceros katoi* (2), *Procaris hawaiana* (2), *Pronesopupa hystricella* (2), *Pseudobiceros gloriosus* (2), *Pseudobiceros murinus* (2), *Pseudobiceros periculosus* (2), *Pseudonebularia connectens* (2), *Pyramidelloides gracilis* (2), *Reticunassa silvardi* (2), *Septa occidentalis* (2), *Simulamerelina granulosa* (2), *Simulamerelina hewa* (2), *Sistrum albolabris* (2), *Stauridiosarsia nipponica* (2), *Stebbingdromia plumosa* (2), *Strigatella coronata* (2), *Strigatella fulvescens* (2), *Succinea lumbalis* (2), *Thor leptochelus* (2), *Thranita coeruleipes* (2), *Tornatellides konaensis* (2), *Tornatellides macromphala* (2), *Tornatellides perkinsi* (2), *Vitularia sandwicensis* (2), *Acanthocidaris hastigera* (1), *Achatinella byronii* (1), *Achatinella curta* (1), *Achatinella lila* (1), *Achatinella livida* (1), *Allopeas gracile* (1), *Amastra assimilis* (1), *Amastra cyclostoma* (1), *Amastra forbesi* (1), *Amastra nucleola* (1), *Amastra turritella* (1), *Ambigolimax* (1), *Angustassiminea nitida* (1), *Arakawania marginalba* (1), *Arion distinctus* (1), *Arion subfuscus* (1), *Armina rubida* (1), *Atolla* (1), *Babamunida kanaloa* (1), *Bermudella lahainensis* (1), *Carelia bicolor* (1), *Carelia lirata* (1), *Carelia pilsbryi* (1), *Cautor intermissus* (1), *Centrostephanus asteriscus* (1), *Cheilea* (1), *Cherusius triunguiculatus* (1), *Clathropsis fosterae* (1), *Clavus pusillus* (1), *Conus spiceri* (1), *Cookeconcha paucicostata* (1), *Cycloscala peaseana* (1), *Cyerce basi* (1), *Dentimargo pumila* (1), *Dermatobranchus piperoides* (1), *Doris immonda* (1), *Dulcerana affinis* (1), *Edwardsianthus gilbertensis* (1), *Edwardsianthus pudicus* (1), *Euanodontia hawaiensis* (1), *Euchirograpsus danielae* (1), *Furtipodia gemma* (1), *Godwinia caperata* (1), *Harpa goodwini* (1), *Helenia apiculata* (1), *Heteronucia minuta* (1), *Hymenopenaeus fallax* (1), *Inella pagoda* (1), *Iotrochota sinki* (1), *Kermidaphnella daedalea* (1), *Lamellidea gracilis* (1), *Lamellidea peponum* (1), *Laminella straminea* (1), *Leptachatina haenensis* (1), *Ligia honu* (1), *Lophocochlias parvissimus* (1), *Lucilina pacifica* (1), *Lyropupa thaanumi* (1), *Lyropupa thaumasia* (1), *Mactra thaanumi* (1), *Maculastrombus mutabilis* (1), *Margarya chinensis* (1), *Melanella acanthyllis* (1), *Melanella major* (1), *Monoplex comptus* (1), *Myurellopsis columellaris* (1), *Nebularia chrysostoma* (1), *Nebularia eremitarum* (1), *Nebularia ustulata* (1), *Nesophila prestonsutteri* (1), *Nesopupa newcombi* (1), *Newcombia gagei* (1), *Ophiomastix macroplaca* (1), *Oscilla indica* (1), *Pallifera* (1), *Partulina anceyana* (1), *Partulina crassa* (1), *Partulina dubiosa* (1), *Partulina marmorata* (1), *Partulina tappaniana* (1), *Partulina terebra* (1), *Peltidium* (1), *Pennella* (1), *Periclimenaeus devaneyi* (1), *Philonesia oahuensis* (1), *Phyllidia scottjohnsoni* (1), *Phyllognathia simplex* (1), *Physalia megalista* (1), *Platorchestia kaalensis* (1), *Plesiothyreus cancellatus* (1), *Produnga rubropunctata* (1), *Pseudobiceros pardalis* (1), *Pseudoceros jebborum* (1), *Rumina decollata* (1), *Sacoproteus thomasleei* (1), *Sagaminopteron pohnpei* (1), *Sakaila wanawana* (1), *Sarasinula plebeia* (1), *Sclerophytum abrupta* (1), *Siphonaria waikoloaensis* (1), *Starmeria conica* (1), *Stiliger* (1), *Strigatella coffea* (1), *Strigatella lugubris* (1), *Sturanya baldwini* (1), *Sturanya laciniosa* (1), *Styloptygma lacteolum* (1), *Temnotrema hawaiiense* (1), *Tempuractis rinkai* (1), *Tenellia pinnifera* (1), *Terestrombus fragilis* (1), *Tetraclitella purpurascens* (1), *Thala exilis* (1), *Thranita pseudopelsarti* (1), *Tornatellaria newcombi* (1), *Tornatellides serrarius* (1), *Tornatellides spaldingi* (1), *Trapania euryeia* (1), *Vayssierea felis* (1), *Weedingia paulayi* (1), *Xenuroturris devoizei* (1)

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
