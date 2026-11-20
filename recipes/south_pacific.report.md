# Bericht: Südpazifik (`recipes/south_pacific.json`)

Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.

- Referenz-DB: v3 (FishBase v26.06, SeaLifeBase v26.06)
- Salz/Süß: FishBase/SeaLifeBase v25.04 (species.parquet)
- iNaturalist: 1142 Taxa (Seiten: 3)
- OBIS: 2769 Arten
- Bild: https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Blacktip_reef_sharks_at_Moorea_2025.jpg/330px-Blacktip_reef_sharks_at_Moorea_2025.jpg — Borut Furlan, CC BY-SA 4.0, https://commons.wikimedia.org/wiki/File:Blacktip_reef_sharks_at_Moorea_2025.jpg

## Gebiete

- iNaturalist: Fiji (7332), French Polynesia (6748), Cook Islands (10288), Samoa (8504), American Samoa (8548), Tonga (7841)
- OBIS: Fidschi westlich 180°, Lau-Inseln, Tonga und Samoa (schließt Wallis und Futuna ein), Cookinseln, Französisch-Polynesien
- FishBase/SeaLifeBase-Verbreitung: 242, 258, 258:PF-AU, 258:PF-GA, 258:PF-MA, 258:PF-SO, 258:PF-TU, 184, 882, 016, 776

## Übersicht

- Arten der Reihenfolge-Quelle, aufgelöst: 1134; nicht aufgelöst: 7
- ausgeschlossen: 394
  - zu wenige Nachweise: 342
  - zu klein: 33
  - kein Meeresfisch: 16
  - nur tiefer als die Tauchgrenze: 3
- Kandidaten nach den Filtern: 740
- Deck: 158 Arten (Level 1: 48, Level 2: 60, Level 3: 50); Umfang laut Rezept 40/60/50 plus Highlights
- Highlights: 8 im Deck, 0 verworfen

## Verworfene Highlights

Keine.

## iNaturalist-Namen zugeordnet

Laut `recipes/inat_names.json`: iNaturalist nennt die Art anders als die Referenz-DB; die Zählung kommt zu der der Referenz-DB-Art.

| iNaturalist | Referenz-DB | iNat | Art | Beleg |
|---|---|---|---|---|
| *Pseudanthias cheirospilos* | *Pseudanthias squamipinnis* | 405 | Abspaltung | https://www.inaturalist.org/taxon_changes/147467 |
| *Coris schroederii* | *Coris batuensis* | 71 | Abspaltung | https://www.inaturalist.org/taxon_changes/157302 |
| *Eviotops sebreei* | *Eviota sebreei* | 50 | Umbenennung | https://www.inaturalist.org/taxon_changes/178922 |
| *Eviotops oculineatus* | *Eviota oculineata* | 33 | Umbenennung | https://www.inaturalist.org/taxon_changes/178909 |
| *Eviotops prasites* | *Eviota prasites* | 22 | Umbenennung | https://www.inaturalist.org/taxon_changes/178916 |
| *Eviotops sigillatus* | *Eviota sigillata* | 22 | Umbenennung | https://www.inaturalist.org/taxon_changes/178924 |
| *Eviotops cometa* | *Eviota cometa* | 16 | Umbenennung | https://www.inaturalist.org/taxon_changes/178892 |
| *Pinnoctopus aspilosomatis* | *Callistoctopus aspilosomatis* | 10 | Umbenennung | https://www.inaturalist.org/taxon_changes/172611 |
| *Eviotops dorsogilvus* | *Eviota dorsogilva* | 7 | Umbenennung | https://www.inaturalist.org/taxon_changes/178893 |
| *Filistriatus sexfilis* | *Polydactylus sexfilis* | 3 | Umbenennung | https://www.inaturalist.org/taxon_changes/165559 |
| *Pinnoctopus ornatus* | *Callistoctopus ornatus* | 2 | Umbenennung | https://www.inaturalist.org/taxon_changes/172615 |

## Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Carcharhinus amblyrhynchos* | Hunderte Graue Riffhaie stehen im Südpass von Fakarava, die bekannte Haiwand. | 79 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Sphyrna mokarran* | Der Große Hammerhai erscheint im Tiputa-Pass von Rangiroa und vor Bora Bora. | 585 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Negaprion acutidens* | Der Sichelflossen-Zitronenhai ist in den Lagunen von Moorea und Bora Bora eine sichere Begegnung. | 182 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Carcharhinus leucas* | Der Bullenhai ist das Ziel des bekannten Haitauchgangs in der Beqa-Lagune auf Fidschi. | 155 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Mobula alfredi* | Der Riffmanta besucht Putzerstationen in Bora Bora, Tikehau und an Fidschis Manta Reef. | 106 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Epinephelus polyphekadion* | Tausende Tarnfleck-Zackenbarsche laichen jedes Jahr gemeinsam im Südpass von Fakarava. | 158 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Cheilinus undulatus* | Der Napoleon ist an vielen Pässen zutraulich und gehört zu den größten Riffbewohnern. | 91 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Megaptera novaeangliae* | Buckelwale kalben von Juli bis Oktober vor Tonga und Rurutu, wo man mit ihnen schnorcheln darf. | – | Verbreitung | Level 1 |

## Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS oder Verbreitung): 157/158 (99 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 0
- Arten ohne Volksnamen `de` in der Referenz-DB: 74/158 (47 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 3/158 (2 %)
- Familien ohne Volksnamen `de`: 7/42 (17 %): *Aetobatidae*, *Anthiadidae*, *Balaenopteridae*, *Cheloniidae*, *Epinephelidae*, *Mobulidae*, *Octopodidae*
- Familien ohne Volksnamen `en`: 0/42 (0 %)

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

- *Megaptera novaeangliae*: Verbreitung

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

- gleicher Volksname `de` „Meerbarbe“: *Mulloidichthys flavolineatus*, *Mulloidichthys vanicolensis*

## Deck

Spalten: Rang unter den Kandidaten, Zählung der Reihenfolge-Quelle (iNat), OBIS-Nachweise, Einträge der FishBase/SeaLifeBase-Verbreitung in den Rezept-Regionen (~~durchgestrichen~~: Eintrag sagt „nicht vorhanden“), Wasser laut FishBase/SeaLifeBase.

### Level 1 (48)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 1 | *Thalassoma hardwicke* | 1082 | 4371 | native ×9 | Meer |
| 2 | *Acanthurus triostegus* | 1033 | 2078 | native ×11 | Meer |
| 3 | *Rhinecanthus aculeatus* | 999 | 1161 | native ×11 | Meer |
| 4 | *Carcharhinus melanopterus* | 966 | 860 | native ×11 | Brack/Meer |
| 5 | *Chaetodon lunulatus* | 960 | 1603 | native ×7 | Meer |
| 6 | *Abudefduf sexfasciatus* | 917 | 1282 | native ×11 | Meer |
| 7 | *Zanclus cornutus* | 916 | 2801 | native ×10 | Meer |
| 8 | *Halichoeres trimaculatus* | 822 | 1730 | native ×9 | Meer |
| 9 | *Chlorurus spilurus* | 805 | 3315 | native ×8 | Meer |
| 10 | *Chaetodon citrinellus* | 799 | 2771 | native ×10 | Meer |
| 11 | *Centropyge flavissima* | 743 | 5835 | native ×10 | Meer |
| 12 | *Chaetodon auriga* (Quelle: *Chaetodon auriga × lunula*) | 735 | 1830 | native ×11 | Meer |
| 13 | *Balistapus undulatus* | 734 | 4747 | native ×10 | Meer |
| 14 | *Gomphosus varius* | 715 | 5359 | native ×10 | Meer |
| 15 | *Amphiprion barberi* | 710 | 598 | native ×3 | Meer |
| 16 | *Chaetodon vagabundus* | 707 | 2108 | native ×9 | Meer |
| 17 | *Chaetodon ulietensis* | 678 | 1570 | native ×9 | Meer |
| 18 | *Dascyllus trimaculatus* | 637 | 1150 | native ×8 | Meer |
| 19 | *Chromis viridis* | 636 | 1194 | native ×9 | Meer |
| 20 | *Halichoeres hortulanus* | 635 | 4195 | native ×9 | Meer |
| 21 | *Heniochus chrysostomus* | 622 | 1489 | native ×9 | Meer |
| 22 | *Ctenochaetus striatus* | 583 | 14540 | native ×10 | Meer |
| 23 | *Cheilinus chlorourus* | 566 | 1691 | native ×10 | Meer |
| 24 | *Amphiprion chrysopterus* | 555 | 803 | native ×6 | Meer |
| 25 | *Chaetodon ephippium* | 555 | 1763 | native ×11 | Meer |
| 26 | *Dascyllus aruanus* | 538 | 1665 | native ×9 | Meer |
| 27 | *Epinephelus merra* | 523 | 1386 | native ×10 | Meer |
| 28 | *Zebrasoma velifer* | 519 | 2093 | native ×10 | Meer |
| 29 | *Chrysiptera taupou* | 516 | 4760 | native ×3 | Meer |
| 30 | *Canthigaster solandri* | 509 | 768 | native ×9 | Meer |
| 31 | *Zebrasoma scopas* | 506 | 4768 | native ×10 | Meer |
| 32 | *Labroides dimidiatus* | 494 | 3542 | native ×10 | Meer |
| 33 | *Acanthurus lineatus* | 485 | 3025 | native ×11 | Meer |
| 34 | *Mulloidichthys flavolineatus* | 479 | 935 | native ×11 | Meer |
| 35 | *Pateobatis fai* | 478 | 340 | native ×8 | Meer |
| 36 | *Chaetodon lunula* | 476 | 1573 | native ×11 | Meer |
| 37 | *Stegastes nigricans* | 457 | 1053 | native ×9 | Meer |
| 38 | *Abudefduf septemfasciatus* | 456 | 365 | native ×7 | Meer |
| 39 | *Pomacentrus pavo* | 454 | 474 | native ×9 | Meer |
| 40 | *Pygoplites diacanthus* | 454 | 2153 | native ×9 | Meer |
| 79 | *Carcharhinus amblyrhynchos* (Highlight) | 290 | 319 | native ×11 | Meer |
| 585 | *Sphyrna mokarran* (Highlight) | 13 | 19 | native ×3 | Brack/Meer |
| 182 | *Negaprion acutidens* (Highlight) | 136 | 126 | native ×10 | Brack/Meer |
| 155 | *Carcharhinus leucas* (Highlight) | 163 | 138 | native ×6 | Süß/Brack/Meer |
| 106 | *Mobula alfredi* (Highlight) | 228 | 170 | native ×2 | Süß/Meer |
| 158 | *Epinephelus polyphekadion* (Highlight) | 162 | 375 | native ×10 | Meer |
| 91 | *Cheilinus undulatus* (Highlight) | 251 | 611 | native ×11 | Meer |
| – | *Megaptera novaeangliae* (Highlight) | – | – | native ×10 | Meer |

### Level 2 (60)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 41 | *Fistularia commersonii* | 444 | 461 | native ×10 | Meer |
| 42 | *Gymnothorax javanicus* | 443 | 443 | native ×10 | Meer |
| 43 | *Parupeneus multifasciatus* | 434 | 5231 | native ×11 | Meer |
| 44 | *Chelonia mydas* | 433 | 334 | native ×9 | Meer |
| 45 | *Epibulus insidiator* | 424 | 1701 | native ×10 | Meer |
| 46 | *Ellochelon vaigiensis* | 416 | 356 | native ×10 | Süß/Brack/Meer |
| 47 | *Caranx melampygus* | 415 | 1335 | native ×10 | Brack/Meer |
| 48 | *Pseudanthias squamipinnis* | 405 | 97 | native ×2 | Meer |
| 49 | *Chaetodon ornatissimus* | 403 | 1305 | native ×10 | Meer |
| 50 | *Paracirrhites arcatus* | 391 | 4263 | native ×10 | Meer |
| 51 | *Lutjanus fulvus* | 385 | 1389 | native ×11 | Süß/Brack/Meer |
| 52 | *Paracirrhites forsteri* | 385 | 1719 | native ×10 | Meer |
| 53 | *Triaenodon obesus* | 378 | 617 | native ×11 | Meer |
| 54 | *Chaetodon unimaculatus* | 377 | 1330 | native ×11 | Meer |
| 55 | *Thalassoma lutescens* | 375 | 3663 | native ×10 | Meer |
| 56 | *Aulostomus chinensis* | 367 | 796 | native ×11 | Meer |
| 57 | *Monotaxis grandoculis* | 367 | 2471 | native ×11 | Meer |
| 58 | *Chaetodon trifascialis* | 361 | 1442 | native ×10 | Meer |
| 59 | *Gnathodentex aureolineatus* | 361 | 1114 | native ×11 | Meer |
| 60 | *Balistoides viridescens* | 357 | 564 | native ×11 | Meer |
| 61 | *Chaetodon reticulatus* | 346 | 3655 | native ×10 | Meer |
| 62 | *Oxymonacanthus longirostris* | 345 | 647 | native ×2 | Meer |
| 63 | *Coris aygula* | 329 | 1161 | native ×10 | Meer |
| 64 | *Dascyllus reticulatus* | 327 | 1425 | native ×4 | Meer |
| 65 | *Scarus schlegeli* | 319 | 3096 | native ×10 | Meer |
| 66 | *Neoniphon sammara* | 318 | 1080 | native ×10 | Meer |
| 67 | *Cephalopholis argus* | 310 | 4127 | native ×11 | Meer |
| 68 | *Naso lituratus* | 309 | 3618 | native ×11 | Meer |
| 69 | *Chaetodon pelewensis* | 308 | 4066 | native ×10 | Meer |
| 70 | *Stethojulis bandanensis* | 307 | 1331 | native ×10 | Meer |
| 71 | *Chaetodon baronessa* | 306 | 788 | native ×2 | Meer |
| 72 | *Parupeneus barberinus* | 305 | 924 | native ×11 | Meer |
| 73 | *Arothron meleagris* | 302 | 363 | native ×10 | Meer |
| 74 | *Scolopsis bilineata* | 302 | 1116 | native ×2 | Meer |
| 75 | *Arothron nigropunctatus* | 298 | 489 | native ×4 | Meer |
| 76 | *Centropyge bicolor* | 295 | 840 | native ×4 | Meer |
| 77 | *Aetobatus ocellatus* | 294 | 234 | native ×7 | Brack/Meer |
| 78 | *Chlorurus bleekeri* | 291 | 860 | native ×3 | Meer |
| 80 | *Ostracion cubicum* | 290 | 334 | native ×10 | Meer |
| 81 | *Scarus psittacus* | 285 | 2139 | native ×10 | Meer |
| 82 | *Forcipiger flavissimus* | 284 | 1334 | native ×10 | Meer |
| 83 | *Pomacentrus vaiuli* | 282 | 9204 | native ×3 | Meer |
| 84 | *Chaetodon rafflesii* | 272 | 727 | native ×6 | Brack/Meer |
| 85 | *Siganus spinus* | 270 | 950 | native ×8 | Meer |
| 86 | *Amphiprion perideraion* | 268 | 280 | native ×4 | Brack/Meer |
| 87 | *Chrysiptera brownriggii* (Quelle: *Chrysiptera leucopoma*) | 266 | 1508 | native ×9 | Meer |
| 88 | *Amphiprion maohiensis* | 261 | 3 | native ×1 | ? |
| 89 | *Coris gaimard* | 260 | 1068 | native ×9, questionable ×1 | Meer |
| 90 | *Myripristis violacea* | 255 | 473 | native ×11 | Meer |
| 92 | *Sargocentron spiniferum* | 251 | 1111 | native ×11 | Meer |
| 93 | *Centropyge bispinosa* | 248 | 3229 | native ×8 | Meer |
| 94 | *Cheilinus trilobatus* | 248 | 1394 | native ×10 | Brack/Meer |
| 95 | *Monotaxis heterodon* | 248 | 517 | – | Meer |
| 96 | *Acanthurus pyroferus* | 242 | 1251 | native ×11 | Meer |
| 97 | *Dascyllus flavicaudus* | 242 | 326 | native ×6 | Meer |
| 98 | *Lutjanus gibbus* | 241 | 1383 | native ×10 | Meer |
| 99 | *Eretmochelys imbricata* | 240 | 202 | native ×7 | Brack/Meer |
| 100 | *Melichthys vidua* | 240 | 4117 | native ×10 | Meer |
| 101 | *Scarus oviceps* | 238 | 1691 | native ×8 | Meer |
| 102 | *Diodon hystrix* | 233 | 296 | native ×11 | Meer |

### Level 3 (50)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 103 | *Valenciennea strigata* | 233 | 638 | native ×9 | Meer |
| 104 | *Chromis atripectoralis* | 230 | 448 | native ×9 | Meer |
| 105 | *Abudefduf sordidus* | 228 | 266 | native ×10 | Brack/Meer |
| 107 | *Heniochus varius* | 225 | 852 | native ×5 | Meer |
| 108 | *Nemateleotris magnifica* | 223 | 849 | native ×11 | Meer |
| 109 | *Cirrhilabrus punctatus* | 219 | 913 | native ×2 | Meer |
| 110 | *Mulloidichthys vanicolensis* | 214 | 983 | native ×11 | Meer |
| 111 | *Amblyglyphidodon curacao* | 212 | 205 | native ×3 | Meer |
| 112 | *Parapercis xanthogramma* | 212 | 179 | native ×3 | Meer |
| 113 | *Thalassoma amblycephalum* | 212 | 1288 | native ×10 | Meer |
| 114 | *Terapon jarbua* | 210 | 205 | native ×4 | Süß/Brack/Meer |
| 115 | *Oxycheilinus digramma* | 209 | 1891 | native ×5 | Brack/Meer |
| 116 | *Octopus cyanea* | 206 | 224 | native ×9 | Meer |
| 117 | *Acanthurus nigricans* | 205 | 6752 | native ×9 | Meer |
| 118 | *Acanthurus olivaceus* | 205 | 1317 | native ×8, ~~misidentification ×1~~ | Meer |
| 119 | *Synodus variegatus* | 205 | 505 | native ×9 | Meer |
| 120 | *Ostracion meleagris* | 204 | 535 | native ×10 | Meer |
| 121 | *Stegastes lacrymatus* | 204 | 3550 | native ×9, questionable ×1 | Meer |
| 122 | *Amblyglyphidodon aureus* | 203 | 243 | native ×3 | Meer |
| 123 | *Pomacentrus callainus* | 196 | 2483 | native ×2 | Meer |
| 124 | *Heniochus monoceros* | 195 | 526 | native ×10 | Meer |
| 125 | *Pomacanthus imperator* | 194 | 546 | native ×9 | Meer |
| 126 | *Lutjanus bohar* | 190 | 2667 | native ×11 | Süß/Brack/Meer |
| 127 | *Amblygobius phalaena* | 189 | 514 | native ×8 | Meer |
| 128 | *Hemigymnus melapterus* | 189 | 1158 | native ×4 | Meer |
| 129 | *Novaculichthys taeniourus* | 189 | 340 | native ×8 | Meer |
| 130 | *Pteropterus antennatus* | 188 | 169 | native ×9 | Meer |
| 131 | *Caesio caerulaurea* | 186 | 414 | native ×4 | Meer |
| 132 | *Chaetodon plebeius* | 186 | 546 | native ×2 | Meer |
| 133 | *Plectroglyphidodon dickii* | 186 | 3589 | native ×9 | Meer |
| 134 | *Naso brevirostris* | 185 | 558 | native ×11 | Meer |
| 135 | *Sufflamen bursa* | 185 | 1644 | native ×11 | Meer |
| 136 | *Siganus doliatus* | 181 | 498 | native ×2 | Meer |
| 137 | *Cheilio inermis* | 178 | 222 | native ×7 | Meer |
| 138 | *Halichoeres margaritaceus* | 178 | 1032 | native ×10 | Meer |
| 139 | *Thalassoma lunare* | 177 | 908 | native ×2 | Meer |
| 140 | *Gymnothorax pictus* | 175 | 261 | native ×11 | Brack/Meer |
| 141 | *Anguilla marmorata* | 174 | 162 | native ×11 | Süß/Brack/Meer |
| 142 | *Pterois volitans* | 172 | 207 | native ×10 | Meer |
| 143 | *Acanthurus nigrofuscus* | 171 | 7429 | native ×10 | Meer |
| 144 | *Pycnochromis margaritifer* | 171 | 4354 | native ×8 | Meer |
| 145 | *Acanthurus nigricauda* | 170 | 667 | native ×10 | Brack/Meer |
| 146 | *Amblyglyphidodon orbicularis* | 167 | 173 | native ×3 | Meer |
| 147 | *Nebrius ferrugineus* | 167 | 144 | native ×11 | Meer |
| 148 | *Arothron hispidus* | 166 | 194 | native ×10 | Brack/Meer |
| 149 | *Chlorurus microrhinos* | 166 | 2182 | native ×11 | Meer |
| 150 | *Scolopsis trilineata* | 166 | 253 | native ×3 | Meer |
| 151 | *Echeneis naucrates* | 165 | 175 | native ×10 | Brack/Meer |
| 152 | *Lutjanus kasmira* | 165 | 1518 | native ×11 | Meer |
| 153 | *Parupeneus cyclostomus* | 165 | 1990 | native ×11 | Meer |

## Grenzfälle

Je 10 Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels sie nehmen (Highlights ab Level 2 übersprungen).

### Level 1/2

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 31 | *Zebrasoma scopas* | 506 | 4768 | native ×10 | Meer | 1 |
| 32 | *Labroides dimidiatus* | 494 | 3542 | native ×10 | Meer | 1 |
| 33 | *Acanthurus lineatus* | 485 | 3025 | native ×11 | Meer | 1 |
| 34 | *Mulloidichthys flavolineatus* | 479 | 935 | native ×11 | Meer | 1 |
| 35 | *Pateobatis fai* | 478 | 340 | native ×8 | Meer | 1 |
| 36 | *Chaetodon lunula* | 476 | 1573 | native ×11 | Meer | 1 |
| 37 | *Stegastes nigricans* | 457 | 1053 | native ×9 | Meer | 1 |
| 38 | *Abudefduf septemfasciatus* | 456 | 365 | native ×7 | Meer | 1 |
| 39 | *Pomacentrus pavo* | 454 | 474 | native ×9 | Meer | 1 |
| 40 | *Pygoplites diacanthus* | 454 | 2153 | native ×9 | Meer | 1 |
| | **Grenze** | | | | | |
| 41 | *Fistularia commersonii* | 444 | 461 | native ×10 | Meer | 2 |
| 42 | *Gymnothorax javanicus* | 443 | 443 | native ×10 | Meer | 2 |
| 43 | *Parupeneus multifasciatus* | 434 | 5231 | native ×11 | Meer | 2 |
| 44 | *Chelonia mydas* | 433 | 334 | native ×9 | Meer | 2 |
| 45 | *Epibulus insidiator* | 424 | 1701 | native ×10 | Meer | 2 |
| 46 | *Ellochelon vaigiensis* | 416 | 356 | native ×10 | Süß/Brack/Meer | 2 |
| 47 | *Caranx melampygus* | 415 | 1335 | native ×10 | Brack/Meer | 2 |
| 48 | *Pseudanthias squamipinnis* | 405 | 97 | native ×2 | Meer | 2 |
| 49 | *Chaetodon ornatissimus* | 403 | 1305 | native ×10 | Meer | 2 |
| 50 | *Paracirrhites arcatus* | 391 | 4263 | native ×10 | Meer | 2 |

### Level 2/3

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 93 | *Centropyge bispinosa* | 248 | 3229 | native ×8 | Meer | 2 |
| 94 | *Cheilinus trilobatus* | 248 | 1394 | native ×10 | Brack/Meer | 2 |
| 95 | *Monotaxis heterodon* | 248 | 517 | – | Meer | 2 |
| 96 | *Acanthurus pyroferus* | 242 | 1251 | native ×11 | Meer | 2 |
| 97 | *Dascyllus flavicaudus* | 242 | 326 | native ×6 | Meer | 2 |
| 98 | *Lutjanus gibbus* | 241 | 1383 | native ×10 | Meer | 2 |
| 99 | *Eretmochelys imbricata* | 240 | 202 | native ×7 | Brack/Meer | 2 |
| 100 | *Melichthys vidua* | 240 | 4117 | native ×10 | Meer | 2 |
| 101 | *Scarus oviceps* | 238 | 1691 | native ×8 | Meer | 2 |
| 102 | *Diodon hystrix* | 233 | 296 | native ×11 | Meer | 2 |
| | **Grenze** | | | | | |
| 103 | *Valenciennea strigata* | 233 | 638 | native ×9 | Meer | 3 |
| 104 | *Chromis atripectoralis* | 230 | 448 | native ×9 | Meer | 3 |
| 105 | *Abudefduf sordidus* | 228 | 266 | native ×10 | Brack/Meer | 3 |
| 107 | *Heniochus varius* | 225 | 852 | native ×5 | Meer | 3 |
| 108 | *Nemateleotris magnifica* | 223 | 849 | native ×11 | Meer | 3 |
| 109 | *Cirrhilabrus punctatus* | 219 | 913 | native ×2 | Meer | 3 |
| 110 | *Mulloidichthys vanicolensis* | 214 | 983 | native ×11 | Meer | 3 |
| 111 | *Amblyglyphidodon curacao* | 212 | 205 | native ×3 | Meer | 3 |
| 112 | *Parapercis xanthogramma* | 212 | 179 | native ×3 | Meer | 3 |
| 113 | *Thalassoma amblycephalum* | 212 | 1288 | native ×10 | Meer | 3 |

### Level 3/nicht im Deck

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 144 | *Pycnochromis margaritifer* | 171 | 4354 | native ×8 | Meer | 3 |
| 145 | *Acanthurus nigricauda* | 170 | 667 | native ×10 | Brack/Meer | 3 |
| 146 | *Amblyglyphidodon orbicularis* | 167 | 173 | native ×3 | Meer | 3 |
| 147 | *Nebrius ferrugineus* | 167 | 144 | native ×11 | Meer | 3 |
| 148 | *Arothron hispidus* | 166 | 194 | native ×10 | Brack/Meer | 3 |
| 149 | *Chlorurus microrhinos* | 166 | 2182 | native ×11 | Meer | 3 |
| 150 | *Scolopsis trilineata* | 166 | 253 | native ×3 | Meer | 3 |
| 151 | *Echeneis naucrates* | 165 | 175 | native ×10 | Brack/Meer | 3 |
| 152 | *Lutjanus kasmira* | 165 | 1518 | native ×11 | Meer | 3 |
| 153 | *Parupeneus cyclostomus* | 165 | 1990 | native ×11 | Meer | 3 |
| | **Grenze** | | | | | |
| 154 | *Cetoscarus ocellatus* | 164 | 472 | native ×10 | Meer | – |
| 156 | *Echidna nebulosa* | 163 | 218 | native ×10 | Meer | – |
| 157 | *Odonus niger* | 163 | 404 | native ×9 | Meer | – |
| 159 | *Plectorhinchus vittatus* | 162 | 304 | native ×3 | Meer | – |
| 160 | *Chaetodon mertensii* | 158 | 1168 | native ×10 | Meer | – |
| 161 | *Thalassoma quinquevittatum* | 157 | 5770 | native ×8 | Meer | – |
| 162 | *Sufflamen chrysopterum* | 154 | 1103 | native ×4 | Meer | – |
| 163 | *Naso vlamingii* | 153 | 586 | native ×10 | Meer | – |
| 164 | *Acanthurus xanthopterus* | 152 | 304 | native ×11 | Meer | – |
| 165 | *Chaetodon melannotus* | 149 | 692 | native ×4 | Meer | – |

## Abgleich mit Führern

Das Rezept nennt keinen Führer.
## Änderungen gegenüber dem bestehenden Deck

- neu: 0
- entfallen: 0

## Ausgeschlossene Kandidaten

<details><summary>394 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Eviota teresae* | 97 | Meer | zu klein (höchstens 2.11 cm) |
| *Ecsenius fijiensis* | 91 | Meer | zu klein (höchstens 3.9 cm) |
| *Eviota sebreei* | 50 | Meer | zu klein (höchstens 2.5 cm) |
| *Trimma benjamini* | 47 | Meer | zu klein (höchstens 3 cm) |
| *Trimma anaima* | 46 | Meer | zu klein (höchstens 3 cm) |
| *Eviota karaspila* | 44 | Meer | zu klein (höchstens 1.79 cm) |
| *Bryaninops yongei* | 42 | Meer | zu klein (höchstens 3.5 cm) |
| *Fusigobius melacron* | 40 | Meer | zu klein (höchstens 3.52 cm) |
| *Eviota oculineata* | 33 | Meer | zu klein (höchstens 1.09 cm) |
| *Hippocampus pontohi* | 30 | Meer | zu klein (höchstens 1.69 cm) |
| *Trimma macrophthalmus* | 27 | Meer | zu klein (höchstens 2.5 cm) |
| *Eviota prasites* | 22 | Meer | zu klein (höchstens 3 cm) |
| *Eviota sigillata* | 22 | Meer | zu klein (höchstens 3 cm) |
| *Sicyopterus pugnans* | 21 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma caesiura* | 21 | Meer | zu klein (höchstens 3.5 cm) |
| *Asterropteryx striata* | 20 | Meer | zu klein (höchstens 2.32 cm) |
| *Eviota albolineata* | 19 | Meer | zu klein (höchstens 3.6 cm) |
| *Oreochromis mossambicus* | 19 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota cometa* | 16 | Meer | zu klein (höchstens 1.64 cm) |
| *Kuhlia marginata* | 16 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota infulata* | 15 | Meer | zu klein (höchstens 2.5 cm) |
| *Poecilia reticulata* | 15 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma anthrenum* | 14 | Meer | zu klein (höchstens 2.04 cm) |
| *Trimma xanthum* | 14 | Meer | zu klein (höchstens 1.78 cm) |
| *Trimma taylori* | 13 | Meer | zu klein (höchstens 3.5 cm) |
| *Xenanthias longimanus* | 13 | Meer | zu klein (höchstens 3.5 cm) |
| *Alectis ciliaris* | 12 | Meer | nur tiefer als die Tauchgrenze (erst ab 60 m) |
| *Trimma annosum* | 12 | Meer | zu klein (höchstens 2.8 cm) |
| *Trimma finistrinum* | 12 | Meer | zu klein (höchstens 2.53 cm) |
| *Bryaninops natans* | 11 | Meer | zu klein (höchstens 2.5 cm) |
| *Nautilus vitiensis* | 10 | Meer | nur tiefer als die Tauchgrenze (erst ab 200 m) |
| *Lotilia klausewitzi* | 9 | Meer | zu klein (höchstens 2.71 cm) |
| *Eviota punctulata* | 8 | Meer | zu klein (höchstens 2.07 cm) |
| *Eviota dorsogilva* | 7 | Meer | zu klein (höchstens 1.25 cm) |
| *Pelmatolapia mariae* | 7 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Priolepis semidoliata* | 7 | Meer | zu klein (höchstens 2.4 cm) |
| *Spirula spirula* | 7 | Meer | nur tiefer als die Tauchgrenze (erst ab 100 m) |
| *Eviota afelei* | 6 | Meer | zu klein (höchstens 1.8 cm) |
| *Fusigobius aureus* | 6 | Meer | zu klein (höchstens 3.48 cm) |
| *Trimma maiandros* | 6 | Meer | zu klein (höchstens 2.7 cm) |
| *Trimma nasa* | 5 | Meer | zu klein (höchstens 2.25 cm) |
| *Abudefduf conformis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Acanthurus leucopareius* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Bathygobius cyclopterus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Bryaninops dianneae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Canthigaster epilampra* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Enneapterygius rhabdotus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Entomacrodus decussatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Epinephelus spilotoceps* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Euthynnus affinis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Fusigobius gracilis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Fusigobius humeralis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gnatholepis ophthalmotaenia* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gunnellichthys pleurotaenia* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hoplolatilus cuniculus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lethrinus nebulosus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Lethrinus variegatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lutjanus rufolineatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lutjanus russellii* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Mahidolia mystacina* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Mulloidichthys mimicus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Myrichthys maculosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Naso brachycentron* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ostorhinchus leslie* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ostorhinchus taeniophorus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Paracirrhites nisus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Parapercis snyderi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Plectroglyphidodon phoenixensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Plesiops corallicola* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pleurosicya micheli* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pseudanthias olivaceus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pseudojuloides polynesica* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Rabaulichthys altipinnis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scarus quoyi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scatophagus argus* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Scorpaenopsis oxycephala* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scuticaria tigrina* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Siphamia jebbi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sphyraena obtusata* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Sufflamen fraenatum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Synchiropus laddi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Trachyrhamphus bicoarctatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Upeneus taeniopterus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Valenciennea randalli* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Xanthichthys auromarginatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Albula glossodonta* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Amblyeleotris biguttata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Brotula multibarbata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bryaninops loki* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Callechelys marmorata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Callionymus simplicicornis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cirripectes perustus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Compsanthias ventralis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Coris roseoviridis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Corythoichthys flavofasciatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cryptocentrus multicinctus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cryptocentrus nanus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cymolutes torquatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cyprinus rubrofuscus* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Diplogrammus goramensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Eviota fallax* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Fowleria vaiulae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Fusigobius pallidus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gymnothorax eurostus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gymnothorax richardsonii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gymnothorax rueppelliae* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Halicampus macrorhynchus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Iniistius auropunctatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Kyonemichthys rumengani* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Makaira nigricans* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Megalaspis cordyla* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Meiacanthus ditrema* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Microphis brachyurus* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Mobula birostris* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mugil cephalus* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Nemateleotris helfrichi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Neochirus brachyptera* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Neopomacentrus filamentosus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ostorhinchus relativus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paragobiodon kasaii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paragobiodon xanthosoma* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Parapercis lineopunctata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Parapercis queenslandica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Periophthalmus kalolo* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Pleurosicya mossambica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pleurosicya plicata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Polydactylus sexfilis* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Pseudanthias hiva* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pseudochromis jamesi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pycnochromis bami* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rhabdoblennius rhabdotrachelus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rhincodon typus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sargocentron ittodai* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sicyopus zosterophorus* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Sphyraena putnamae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Synchiropus ocellatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Taeniamia biguttata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Trichonotus elegans* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Turrum coeruleopinnatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Uropterygius marmoratus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Valenciennea decora* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Verulux cypselurus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Zoramia fragilis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Zoramia viridiventer* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Amblyeleotris marquesas* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Amblyeleotris yanoi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anampses geographicus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Antennarius commerson* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Apogonichthys ocellatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Asterorhombus intermedius* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Blenniella gibbifrons* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bodianus bimaculatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bolbometopon muricatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Brachaluteres taylori* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Brachysomophis crocodilinus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Callistoctopus ornatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Carcharhinus falciformis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cheilopogon pitcairnensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chromis flavapicis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chromis xanthochira* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cirripectes fuscoguttatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cirripectes quagga* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Coryphaena hippurus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Corythoichthys paxtoni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ctenogobiops tangaroai* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Doryrhamphus melanopleura* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Echidna polyzona* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ecsenius pardus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Enchelyurus ater* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Entomacrodus macrospilus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epinephelus coioides* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Eviota fasciola* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eviota hinanoae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eviota smaragdus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fusigobius duospilus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fusigobius inframaculatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gobiodon histrio* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gobiodon rivulatus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Gorgasia galzini* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gunnellichthys viridescens* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnothorax buroensis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Gymnothorax chilospilus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnothorax enigmaticus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnothorax formosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Halicampus mataafae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hemiramphus depauperatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hyporhamphus affinis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Iniistius aneitensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Iniistius melanopus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Iniistius pentadactylus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Istiophorus platypterus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Kyphosus ocyurus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lethrinus lentjan* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Liopropoma mitratum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lutjanus timoriensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Luzonichthys earlei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Micrognathus andersonii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mobula thurstoni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mulloidichthys pfluegeri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Naso lopezi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nemanthias bicolor* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nemateleotris lavandula* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Neoglyphidodon melas* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Neopomacentrus violascens* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Onuxodon fowleri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pardachirus pavoninus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Parupeneus heptacantha* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Pervagor alternans* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plectorhinchus lineatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plectroglyphidodon aureus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plectroglyphidodon sagmarius* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Poecilia mexicana* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pomacentrus lepidogenys* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pomacentrus moluccensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pomacentrus nigriradiatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pristicon rufus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Psammogobius pisinnus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudanthias mooreanus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudechidna brummeri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ptereleotris monoptera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Salarias guttatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scarus festivus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Scarus flavipectoralis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scolecenchelys gymnota* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scorpaenopsis papuensis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Soleichthys heterorhinos* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Solenostomus halimeda* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Solenostomus paegnius* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Stegastes lividus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Stiphodon hydoreibatus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Stiphodon tuivi* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Taeniura lymma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trimma okinawae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trimma sostra* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Uraspis helvola* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Valenciennea helsdingenii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Abudefduf concolor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acanthurus dussumieri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aethaloperca rogaa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alticus sertatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amblyglyphidodon batunaorum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anampses femininus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Antennatus tuberosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Apogon doryssa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Atherinomorus lacunosus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Aurigequula fasciata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Awaous guamensis* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Bathygobius fuscus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Bodianus bilunulatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Brachysomophis henshawi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bryaninops amplus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bryaninops erythrops* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Canthigaster axiologus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Caranx bucculentus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Carassius auratus* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Carcharhinus longimanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Caretta caretta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Centropyge aurantia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Centropyge boylei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Centropyge narcosis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cephalopholis sonnerati* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cercamia cladara* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaetodon smithi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheilopogon spilopterus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chrysiptera rollandi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chrysiptera starcki* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirrhitops hubbardi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirrhitus albopunctatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirripectes polyzona* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Corythoichthys intestinalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cryptocentrus fasciatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ctenogobiops pomastictus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diodon holocanthus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Discordipinna vibrissa* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Ecsenius fourmanoiri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Encheliophis homei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Enchelynassa canina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Enneapterygius flavoccipitis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Enneapterygius tutuilae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus irroratus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus melanostigma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eviota disrupta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eviota taeiae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fibramia lateralis* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Foa fo* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gambusia affinis* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gerres longirostris* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Gobiodon brochus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gobiodon prolixus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gobiodon spadix* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax margaritophorus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax monochrous* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres nebulosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hazeus profusus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Herklotsichthys quadrimaculatus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Heteroconger lentiginosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hippocampus colemani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hyporthodus octofasciatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hypseleotris guentheri* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Kajikia audax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Kuhlia munda* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Kuhlia petiti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lamnostoma orientale* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Leiognathus equula* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Leiuranus semicinctus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Lethrinus amboinensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lethrinus rubrioperculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lobotes surinamensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Lutjanus xanthopinnis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Macropharyngodon kuiteri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Macropharyngodon pakoko* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Moolgarda seheli* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Naso elegans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Naucrates ductor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nautilus pompilius* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nectamia bandanensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nectamia viria* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Novaculops halsteadi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Octopus bocki* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Octopus laqueus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Octopus oliveri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Omobranchus obliquus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Ophichthus altipennis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophichthus bonaparti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiocara ophicephalus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Oreochromis niloticus* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osteomugil engeli* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Ostorhinchus franssedai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxycheilinus arenatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxyurichthys lonchotus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pandaka lidwilli* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paracaesio xanthurus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paragobiodon lacunicola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paragobiodon melanosoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parascorpaena moultoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parascorpaena picta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parexocoetus mento* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Photoblepharon palpebratum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllogobius platycephalops* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Planiliza melinoptera* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Plectorhinchus lessonii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plectroglyphidodon flaviventris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plectropomus maculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Praealticus bilineatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Priolepis cincta* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Priolepis squamogena* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudamia zonata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudanthias pictilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudocaranx dentex* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pseudocheilinus citrinus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudotriakis microdon* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pteroidichthys amboinensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhabdamia gracilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhabdamia novaluna* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ruvettus pretiosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sardinella melanura* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scolopsis monogramma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scomberoides tol* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Scorpaenodes guamensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scorpaenodes parvipinnis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sebastapistes fowleri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sebastapistes mauritiana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sebastapistes strongia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Seriola rivoliana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sicyopterus rapa* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Siganus niger* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Smilosicyopus pentecost* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Solenostomus leptosoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Solenostomus snuffleupagus* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Sphyraena flavicauda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stanulus seychellensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stenogobius genivittatus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Stethojulis marquesensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sthenoteuthis oualaniensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stonogobiops medon* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sunagocia otaitensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Symphorus nematophorus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synanceia horrida* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Synodus autumnus* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Thysanoteuthis rhombus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tomiyamichthys alleni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tomiyamichthys oni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trachinotus macrospilus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Upeneus vittatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Uranoscopus sulphureus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Urolophus paucimaculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Valenciennea parva* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vanderhorstia bella* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Wetmorella albofasciata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Wetmorella tanakai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xiphophorus maculatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Yongeichthys nebulosus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Zenarchopterus buffonis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Zoramia flebila* | 1 | Meer | zu wenige Nachweise (1 < 5) |

</details>

## Nicht aufgelöste Namen der Reihenfolge-Quelle

Die Referenz-DB der App kennt diese Namen nicht; die App fände sie auch nicht.

| Name | iNat |
|---|---|
| *Dascyllus emamo* | 409 |
| *Pomacentrus maafu* | 361 |
| *Priacanthus starnesi* | 2 |
| *Cylix* | 1 |
| *Eviota atrinasa* | 1 |
| *Eviotops bilunulus* | 1 |
| *Eviotops pseudozebrinus* | 1 |
