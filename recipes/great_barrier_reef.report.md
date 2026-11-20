# Bericht: Great Barrier Reef & Korallenmeer (`recipes/great_barrier_reef.json`)

Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.

- Referenz-DB: v3 (FishBase v26.06, SeaLifeBase v26.06)
- Salz/Süß: FishBase/SeaLifeBase v25.04 (species.parquet)
- iNaturalist: 1594 Taxa (Seiten: 4)
- OBIS: 4611 Arten
- Bild: https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Agincourt_Reef%2C_Great_Barrier_Reef%2C_Queensland_%28483804%29_%289440777727%29.jpg/330px-Agincourt_Reef%2C_Great_Barrier_Reef%2C_Queensland_%28483804%29_%289440777727%29.jpg — Robert Linsdell, CC BY 2.0, https://commons.wikimedia.org/wiki/File:Agincourt_Reef,_Great_Barrier_Reef,_Queensland_(483804)_(9440777727).jpg

## Gebiete

- iNaturalist: Great Barrier Reef, AU (50423), Great Barrier Reef World Heritage Site, QL, AU (131021), New Caledonia (7083), New Caledonia (with lagoon), NC (176505), Vanuatu (7082)
- OBIS: Great Barrier Reef und westliches Korallenmeer, Neukaledonien und Vanuatu
- FishBase/SeaLifeBase-Verbreitung: 036:AU-QLD, 540, 548

## Übersicht

- Arten der Reihenfolge-Quelle, aufgelöst: 1585; nicht aufgelöst: 6
- ausgeschlossen: 558
  - zu wenige Nachweise: 496
  - zu klein: 31
  - kein Meeresfisch: 27
  - nur tiefer als die Tauchgrenze: 4
- Kandidaten nach den Filtern: 1027
- Deck: 156 Arten (Level 1: 46, Level 2: 60, Level 3: 50); Umfang laut Rezept 40/60/50 plus Highlights
- Highlights: 7 im Deck, 0 verworfen

## Verworfene Highlights

Keine.

## iNaturalist-Namen zugeordnet

Laut `recipes/inat_names.json`: iNaturalist nennt die Art anders als die Referenz-DB; die Zählung kommt zu der der Referenz-DB-Art.

| iNaturalist | Referenz-DB | iNat | Art | Beleg |
|---|---|---|---|---|
| *Coris schroederii* | *Coris batuensis* | 318 | Abspaltung | https://www.inaturalist.org/taxon_changes/157302 |
| *Pseudanthias cheirospilos* | *Pseudanthias squamipinnis* | 205 | Abspaltung | https://www.inaturalist.org/taxon_changes/147467 |
| *Eviotops sebreei* | *Eviota sebreei* | 72 | Umbenennung | https://www.inaturalist.org/taxon_changes/178922 |
| *Pinnoctopus dierythraeus* | *Callistoctopus dierythraeus* | 42 | Umbenennung | https://www.inaturalist.org/taxon_changes/172610 |
| *Eviotops atriventris* | *Eviota atriventris* | 23 | Umbenennung | https://www.inaturalist.org/taxon_changes/178886 |
| *Eviotops bacatus* | *Eviota bacata* | 23 | Umbenennung | https://www.inaturalist.org/taxon_changes/178887 |
| *Eviotops prasites* | *Eviota prasites* | 17 | Umbenennung | https://www.inaturalist.org/taxon_changes/178916 |
| *Pinnoctopus aspilosomatis* | *Callistoctopus aspilosomatis* | 16 | Umbenennung | https://www.inaturalist.org/taxon_changes/172611 |
| *Pinnoctopus alpheus* | *Callistoctopus alpheus* | 14 | Umbenennung | https://www.inaturalist.org/taxon_changes/172612 |
| *Eviotops longirostris* | *Eviota longirostris* | 12 | Umbenennung | https://www.inaturalist.org/taxon_changes/178903 |
| *Pinnoctopus ornatus* | *Callistoctopus ornatus* | 8 | Umbenennung | https://www.inaturalist.org/taxon_changes/172615 |
| *Ascarosepion plangon* | *Sepia plangon* | 7 | Umbenennung | https://www.inaturalist.org/taxon_changes/131452 |
| *Eviotops spilotus* | *Eviota spilota* | 7 | Umbenennung | https://www.inaturalist.org/taxon_changes/178925 |
| *Acanthosepion ellipticum* | *Sepia elliptica* | 6 | Umbenennung | https://www.inaturalist.org/taxon_changes/131475 |
| *Eviotops nigriventris* | *Eviota nigriventris* | 4 | Umbenennung | https://www.inaturalist.org/taxon_changes/178908 |
| *Filistriatus sexfilis* | *Polydactylus sexfilis* | 2 | Umbenennung | https://www.inaturalist.org/taxon_changes/165559 |
| *Eviotops bifasciatus* | *Eviota bifasciata* | 2 | Umbenennung | https://www.inaturalist.org/taxon_changes/178889 |
| *Eviotops oculineatus* | *Eviota oculineata* | 2 | Umbenennung | https://www.inaturalist.org/taxon_changes/178909 |
| *Ascarosepion papuense* | *Sepia papuensis* | 1 | Umbenennung | https://www.inaturalist.org/taxon_changes/131455 |
| *Ascarosepion pfefferi* | *Metasepia pfefferi* | 1 | Umbenennung | https://www.inaturalist.org/taxon_changes/131489 |
| *Eviotops ancora* | *Eviota ancora* | 1 | Umbenennung | https://www.inaturalist.org/taxon_changes/178883 |
| *Eviotops dorsogilvus* | *Eviota dorsogilva* | 1 | Umbenennung | https://www.inaturalist.org/taxon_changes/178893 |
| *Eviotops sigillatus* | *Eviota sigillata* | 1 | Umbenennung | https://www.inaturalist.org/taxon_changes/178924 |

## Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Mobula alfredi* | Der Riffmanta versammelt sich das ganze Jahr an den Putzerstationen von Lady Elliot Island. | 134 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Cheilinus undulatus* | Der Napoleon, größter Lippfisch der Welt, ist am Ribbon Reef zahm und neugierig. | 26 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Epinephelus lanceolatus* | Der Riesenzackenbarsch ist das Wahrzeichen des Cod Hole und der größte Barsch der Riffe. | 372 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Carcharhinus amblyrhynchos* | Graue Riffhaie patrouillieren in Gruppen an den Steilwänden von Osprey Reef im Korallenmeer. | 141 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Caretta caretta* | Die Unechte Karettschildkröte nistet bei Mon Repos, dem wichtigsten Nistplatz im Südpazifik. | 192 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Dugong dugon* | Der Dugong weidet in den Seegraswiesen innerhalb des Riffs, die größte Population der Welt lebt hier. | – | Verbreitung | Level 1 |
| *Balaenoptera acutorostrata* | Der Zwergzwergwal kommt im Winter an die Ribbon Reefs und schwimmt dort mit Schnorchlern. | – | Verbreitung | Level 1 |

## Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS oder Verbreitung): 154/156 (99 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 0
- Arten ohne Volksnamen `de` in der Referenz-DB: 82/156 (53 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 0/156 (0 %)
- Familien ohne Volksnamen `de`: 8/41 (20 %): *Aetobatidae*, *Balaenopteridae*, *Cheloniidae*, *Dugongidae*, *Epinephelidae*, *Liopropomatidae*, *Mobulidae*, *Octopodidae*
- Familien ohne Volksnamen `en`: 0/41 (0 %)

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

- *Dugong dugon*: Verbreitung
- *Balaenoptera acutorostrata*: Verbreitung

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

- gemeinsamer wissenschaftlicher Name *teuthis lineatus*: *Acanthurus lineatus*, *Siganus lineatus*

## Deck

Spalten: Rang unter den Kandidaten, Zählung der Reihenfolge-Quelle (iNat), OBIS-Nachweise, Einträge der FishBase/SeaLifeBase-Verbreitung in den Rezept-Regionen (~~durchgestrichen~~: Eintrag sagt „nicht vorhanden“), Wasser laut FishBase/SeaLifeBase.

### Level 1 (46)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 1 | *Chelonia mydas* | 3836 | 35420 | native ×3 | Meer |
| 2 | *Pomacentrus moluccensis* | 1701 | 4702 | native ×3 | Meer |
| 3 | *Abudefduf sexfasciatus* | 1687 | 1489 | native ×3 | Meer |
| 4 | *Plectropomus leopardus* | 1637 | 45829 | native ×2 | Meer |
| 5 | *Pomacanthus sexstriatus* | 1610 | 1542 | native ×3 | Meer |
| 6 | *Scolopsis bilineata* | 1324 | 1813 | native ×3 | Meer |
| 7 | *Triaenodon obesus* | 1308 | 5342 | native ×3 | Meer |
| 8 | *Hemigymnus melapterus* | 1286 | 4203 | native ×3 | Meer |
| 9 | *Chaetodon lunulatus* | 1273 | 478 | native ×3 | Meer |
| 10 | *Amphiprion melanopus* | 1251 | 1485 | native ×3 | Meer |
| 11 | *Thalassoma hardwicke* | 1250 | 1324 | native ×3 | Meer |
| 12 | *Chlorurus microrhinos* | 1200 | 3942 | native ×3 | Meer |
| 13 | *Scarus frenatus* | 1149 | 3764 | native ×2 | Meer |
| 14 | *Amphiprion akindynos* | 1123 | 1763 | native ×2 | Meer |
| 15 | *Zebrasoma velifer* | 1116 | 2437 | native ×3 | Meer |
| 16 | *Siganus doliatus* | 1107 | 7339 | native ×2 | Meer |
| 17 | *Thalassoma lunare* | 1095 | 1516 | native ×3 | Meer |
| 18 | *Chlorurus spilurus* | 1053 | 984 | native ×2 | Meer |
| 19 | *Amblyglyphidodon curacao* | 1047 | 4064 | native ×3 | Meer |
| 20 | *Labroides dimidiatus* | 1043 | 1850 | native ×3 | Meer |
| 21 | *Zanclus cornutus* | 1022 | 2880 | native ×3 | Meer |
| 22 | *Scarus rivulatus* | 994 | 11123 | native ×2 | Meer |
| 23 | *Chaetodon aureofasciatus* | 990 | 2590 | native ×1 | Brack/Meer |
| 24 | *Abudefduf whitleyi* | 979 | 917 | native ×2 | Meer |
| 25 | *Acanthochromis polyacanthus* | 912 | 4553 | native ×3 | Meer |
| 26 | *Cheilinus undulatus* (Highlight) | 900 | 1225 | native ×2 | Meer |
| 27 | *Chaetodon vagabundus* | 896 | 2534 | native ×3 | Meer |
| 28 | *Gomphosus varius* | 864 | 3353 | native ×3 | Meer |
| 29 | *Hippocampus kuda* | 842 | 866 | native ×2 | Brack/Meer |
| 30 | *Lutjanus carponotatus* | 835 | 2988 | native ×1 | Meer |
| 31 | *Chaetodon auriga* | 824 | 1984 | native ×3 | Meer |
| 32 | *Naso unicornis* | 797 | 3466 | native ×3 | Meer |
| 33 | *Acanthurus lineatus* | 781 | 2235 | native ×2 | Meer |
| 34 | *Chaetodon melannotus* | 771 | 2502 | native ×2 | Meer |
| 35 | *Abudefduf bengalensis* | 770 | 722 | native ×1 | Meer |
| 36 | *Dascyllus aruanus* | 766 | 1118 | native ×3 | Meer |
| 37 | *Chaetodon plebeius* | 751 | 2632 | native ×3 | Meer |
| 38 | *Balistoides viridescens* | 745 | 704 | native ×2 | Meer |
| 39 | *Pastinachus ater* | 744 | 593 | native ×1 | Brack/Meer |
| 40 | *Canthigaster valentini* | 736 | 1112 | native ×3 | Meer |
| 134 | *Mobula alfredi* (Highlight) | 361 | 5727 | native ×1 | Süß/Meer |
| 372 | *Epinephelus lanceolatus* (Highlight) | 96 | 114 | native ×3 | Brack/Meer |
| 141 | *Carcharhinus amblyrhynchos* (Highlight) | 328 | 120519 | native ×3 | Meer |
| 192 | *Caretta caretta* (Highlight) | 247 | 661 | native ×2 | Meer |
| – | *Dugong dugon* (Highlight) | – | – | native ×3 | Meer |
| – | *Balaenoptera acutorostrata* (Highlight) | – | – | native ×3 | Brack/Meer |

### Level 2 (60)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 41 | *Plectorhinchus chaetodonoides* | 728 | 634 | native ×3 | Brack/Meer |
| 42 | *Arothron hispidus* | 702 | 805 | native ×3 | Brack/Meer |
| 43 | *Ostracion cubicum* | 693 | 674 | native ×3 | Meer |
| 44 | *Caesio cuning* | 679 | 1215 | native ×3 | Meer |
| 45 | *Chaetodon rainfordi* | 674 | 3442 | native ×1 | Meer |
| 46 | *Siganus corallinus* | 671 | 2863 | native ×2 | Meer |
| 47 | *Ctenochaetus striatus* | 669 | 1511 | native ×3 | Meer |
| 48 | *Chromis viridis* | 666 | 896 | native ×3 | Meer |
| 49 | *Chaetodon baronessa* | 656 | 2461 | native ×3 | Meer |
| 50 | *Octopus cyanea* | 645 | 595 | native ×3 | Meer |
| 51 | *Cheilinus chlorourus* | 640 | 1022 | native ×2 | Meer |
| 52 | *Chaetodon trifascialis* | 636 | 2198 | native ×3 | Meer |
| 53 | *Rhinecanthus aculeatus* | 634 | 793 | native ×2 | Meer |
| 54 | *Siganus vulpinus* | 632 | 2174 | native ×2 | Meer |
| 55 | *Chaetodon citrinellus* | 625 | 2589 | native ×3 | Meer |
| 56 | *Epinephelus merra* | 620 | 1370 | native ×3 | Meer |
| 57 | *Lutjanus bohar* | 617 | 1777 | native ×3 | Süß/Brack/Meer |
| 58 | *Carcharhinus melanopterus* | 614 | 167381 | native ×3 | Brack/Meer |
| 59 | *Gymnothorax javanicus* | 612 | 574 | native ×2 | Meer |
| 60 | *Epibulus insidiator* | 604 | 3268 | native ×3 | Meer |
| 61 | *Neotrygon trigonoides* | 602 | 504 | native ×2 | Meer |
| 62 | *Neoglyphidodon nigroris* | 601 | 2216 | native ×3 | Meer |
| 63 | *Plectorhinchus lineatus* | 601 | 568 | native ×3 | Meer |
| 64 | *Chaetodon lineolatus* | 600 | 1617 | native ×2 | Meer |
| 65 | *Arothron nigropunctatus* | 599 | 629 | native ×3 | Meer |
| 66 | *Platax teira* | 596 | 549 | native ×2 | Meer |
| 67 | *Pterois volitans* | 592 | 619 | native ×3 | Meer |
| 68 | *Taeniura lymma* | 588 | 538 | native ×3 | Meer |
| 69 | *Eretmochelys imbricata* | 587 | 1360 | native ×3 | Brack/Meer |
| 70 | *Fistularia commersonii* | 572 | 634 | native ×3 | Meer |
| 71 | *Aetobatus ocellatus* | 571 | 487 | native ×3 | Brack/Meer |
| 72 | *Neoglyphidodon melas* | 568 | 1901 | native ×3 | Meer |
| 73 | *Amblygobius phalaena* | 567 | 940 | native ×3 | Meer |
| 74 | *Hemiscyllium ocellatum* | 566 | 510 | native ×1 | Meer |
| 75 | *Aulostomus chinensis* | 562 | 530 | native ×3 | Meer |
| 76 | *Scarus ghobban* | 558 | 1663 | native ×2 | Brack/Meer |
| 77 | *Stegastes lacrymatus* | 556 | 3004 | native ×3 | Meer |
| 78 | *Cetoscarus ocellatus* | 554 | 1634 | native ×3 | Meer |
| 79 | *Epinephelus quoyanus* | 547 | 615 | native ×1, questionable ×1 | Meer |
| 80 | *Heniochus acuminatus* | 544 | 758 | native ×3 | Brack/Meer |
| 81 | *Thalassoma nigrofasciatum* | 543 | 489 | native ×2 | Meer |
| 82 | *Dascyllus reticulatus* | 525 | 1650 | native ×3 | Meer |
| 83 | *Salarias alboguttatus* | 516 | 477 | native ×2 | Meer |
| 84 | *Chromileptes altivelis* | 504 | 632 | native ×2, questionable ×1 | Meer |
| 85 | *Parupeneus barberinus* | 497 | 763 | native ×3 | Meer |
| 86 | *Pomacentrus amboinensis* | 494 | 2637 | native ×3 | Meer |
| 87 | *Chaetodon ephippium* | 487 | 1286 | native ×3 | Meer |
| 88 | *Salarias fasciatus* | 485 | 684 | native ×2 | Brack/Meer |
| 89 | *Chromis atripectoralis* | 482 | 2228 | native ×2 | Meer |
| 90 | *Stegastes nigricans* | 475 | 815 | native ×3 | Meer |
| 91 | *Zebrasoma scopas* | 475 | 3210 | native ×2 | Meer |
| 92 | *Lutjanus fulviflamma* | 473 | 1615 | native ×3 | Brack/Meer |
| 93 | *Paracirrhites forsteri* | 467 | 607 | native ×3 | Meer |
| 94 | *Siganus lineatus* | 465 | 770 | native ×3 | Meer |
| 95 | *Cephalopholis cyanostigma* | 462 | 1356 | native ×1 | Meer |
| 96 | *Scarus oviceps* | 458 | 1381 | native ×2 | Meer |
| 97 | *Diodon hystrix* | 457 | 488 | native ×2 | Meer |
| 98 | *Amphiprion perideraion* | 456 | 524 | native ×3 | Brack/Meer |
| 99 | *Chelmon rostratus* | 455 | 1673 | native ×1 | Brack/Meer |
| 100 | *Chaetodon flavirostris* | 453 | 1352 | native ×2 | Brack/Meer |

### Level 3 (50)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 101 | *Chaetodon unimaculatus* | 450 | 1136 | native ×3 | Meer |
| 102 | *Chaetodon ulietensis* | 448 | 974 | native ×3 | Meer |
| 103 | *Dischistodus melanotus* | 436 | 912 | native ×3 | Meer |
| 104 | *Scarus altipinnis* | 433 | 2264 | native ×3 | Meer |
| 105 | *Halichoeres trimaculatus* | 432 | 674 | native ×2 | Meer |
| 106 | *Cheilinus fasciatus* (Quelle: *Concholabrus fasciatus*) | 430 | 2623 | native ×3 | Meer |
| 107 | *Centropyge bicolor* | 429 | 649 | native ×3 | Meer |
| 108 | *Acanthurus xanthopterus* | 426 | 767 | native ×3 | Meer |
| 109 | *Abudefduf vaigiensis* | 425 | 437 | native ×3 | Meer |
| 110 | *Caranx ignobilis* | 425 | 5083 | native ×3 | Brack/Meer |
| 111 | *Halichoeres hortulanus* | 422 | 2477 | native ×3 | Meer |
| 112 | *Choerodon graphicus* | 418 | 431 | native ×2 | Meer |
| 113 | *Balistapus undulatus* | 416 | 758 | native ×3 | Meer |
| 114 | *Heniochus chrysostomus* | 413 | 564 | native ×3 | Meer |
| 115 | *Plectropomus laevis* | 409 | 4015 | native ×3 | Meer |
| 116 | *Plectropomus maculatus* | 408 | 7667 | native ×1 | Meer |
| 117 | *Parapercis queenslandica* | 407 | 443 | native ×2 | Meer |
| 118 | *Sufflamen chrysopterum* | 406 | 714 | native ×3 | Meer |
| 119 | *Dendrochirus zebra* | 395 | 458 | native ×3 | Meer |
| 120 | *Scarus schlegeli* | 393 | 2825 | native ×3 | Meer |
| 121 | *Chrysiptera taupou* | 392 | 427 | native ×3 | Meer |
| 122 | *Cymbacephalus beauforti* | 391 | 338 | native ×1 | Meer |
| 123 | *Naso lituratus* | 390 | 1636 | native ×2 | Meer |
| 124 | *Priacanthus hamrur* | 390 | 444 | native ×3 | Meer |
| 125 | *Parupeneus multifasciatus* | 388 | 1007 | native ×3 | Meer |
| 126 | *Caesio caerulaurea* | 386 | 562 | native ×3 | Meer |
| 127 | *Chaetodon speculum* | 386 | 848 | native ×3 | Meer |
| 128 | *Monotaxis grandoculis* | 386 | 1815 | native ×3 | Meer |
| 129 | *Plectorhinchus gibbosus* | 377 | 415 | native ×3 | Süß/Brack/Meer |
| 130 | *Monotaxis heterodon* | 376 | 341 | native ×1 | Meer |
| 131 | *Acanthurus triostegus* | 366 | 1056 | native ×3 | Meer |
| 132 | *Chrysiptera rollandi* | 364 | 2473 | native ×3 | Meer |
| 133 | *Lethrinus nebulosus* | 362 | 10234 | native ×3 | Brack/Meer |
| 135 | *Chaetodon bennetti* | 357 | 427 | native ×2 | Meer |
| 136 | *Chaetodon rafflesii* | 355 | 703 | native ×3 | Brack/Meer |
| 137 | *Oxymonacanthus longirostris* | 349 | 441 | native ×2 | Meer |
| 138 | *Parapercis australis* | 346 | 445 | native ×2 | Meer |
| 139 | *Caranx melampygus* | 331 | 446 | native ×3 | Brack/Meer |
| 140 | *Arothron manilensis* | 330 | 515 | native ×3 | Brack/Meer |
| 142 | *Meiacanthus atrodorsalis* | 326 | 480 | native ×3 | Meer |
| 143 | *Choerodon fasciatus* | 324 | 2690 | native ×3 | Meer |
| 144 | *Naso brevirostris* | 324 | 468 | native ×1 | Meer |
| 145 | *Thalassoma lutescens* | 323 | 567 | native ×2 | Meer |
| 146 | *Lethrinus harak* | 322 | 487 | native ×3 | Brack/Meer |
| 147 | *Pomacanthus semicirculatus* | 320 | 422 | native ×3 | Meer |
| 148 | *Coris batuensis* | 318 | 314 | native ×2 | Meer |
| 149 | *Cirripectes chelomatus* | 313 | 385 | native ×3 | Meer |
| 150 | *Anampses neoguinaicus* | 312 | 456 | native ×3 | Meer |
| 151 | *Diploprion bifasciatus* | 312 | 534 | native ×3 | Meer |
| 152 | *Scarus niger* | 301 | 3905 | native ×3 | Meer |

## Grenzfälle

Je 10 Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels sie nehmen (Highlights ab Level 2 übersprungen).

### Level 1/2

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 31 | *Chaetodon auriga* | 824 | 1984 | native ×3 | Meer | 1 |
| 32 | *Naso unicornis* | 797 | 3466 | native ×3 | Meer | 1 |
| 33 | *Acanthurus lineatus* | 781 | 2235 | native ×2 | Meer | 1 |
| 34 | *Chaetodon melannotus* | 771 | 2502 | native ×2 | Meer | 1 |
| 35 | *Abudefduf bengalensis* | 770 | 722 | native ×1 | Meer | 1 |
| 36 | *Dascyllus aruanus* | 766 | 1118 | native ×3 | Meer | 1 |
| 37 | *Chaetodon plebeius* | 751 | 2632 | native ×3 | Meer | 1 |
| 38 | *Balistoides viridescens* | 745 | 704 | native ×2 | Meer | 1 |
| 39 | *Pastinachus ater* | 744 | 593 | native ×1 | Brack/Meer | 1 |
| 40 | *Canthigaster valentini* | 736 | 1112 | native ×3 | Meer | 1 |
| | **Grenze** | | | | | |
| 41 | *Plectorhinchus chaetodonoides* | 728 | 634 | native ×3 | Brack/Meer | 2 |
| 42 | *Arothron hispidus* | 702 | 805 | native ×3 | Brack/Meer | 2 |
| 43 | *Ostracion cubicum* | 693 | 674 | native ×3 | Meer | 2 |
| 44 | *Caesio cuning* | 679 | 1215 | native ×3 | Meer | 2 |
| 45 | *Chaetodon rainfordi* | 674 | 3442 | native ×1 | Meer | 2 |
| 46 | *Siganus corallinus* | 671 | 2863 | native ×2 | Meer | 2 |
| 47 | *Ctenochaetus striatus* | 669 | 1511 | native ×3 | Meer | 2 |
| 48 | *Chromis viridis* | 666 | 896 | native ×3 | Meer | 2 |
| 49 | *Chaetodon baronessa* | 656 | 2461 | native ×3 | Meer | 2 |
| 50 | *Octopus cyanea* | 645 | 595 | native ×3 | Meer | 2 |

### Level 2/3

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 91 | *Zebrasoma scopas* | 475 | 3210 | native ×2 | Meer | 2 |
| 92 | *Lutjanus fulviflamma* | 473 | 1615 | native ×3 | Brack/Meer | 2 |
| 93 | *Paracirrhites forsteri* | 467 | 607 | native ×3 | Meer | 2 |
| 94 | *Siganus lineatus* | 465 | 770 | native ×3 | Meer | 2 |
| 95 | *Cephalopholis cyanostigma* | 462 | 1356 | native ×1 | Meer | 2 |
| 96 | *Scarus oviceps* | 458 | 1381 | native ×2 | Meer | 2 |
| 97 | *Diodon hystrix* | 457 | 488 | native ×2 | Meer | 2 |
| 98 | *Amphiprion perideraion* | 456 | 524 | native ×3 | Brack/Meer | 2 |
| 99 | *Chelmon rostratus* | 455 | 1673 | native ×1 | Brack/Meer | 2 |
| 100 | *Chaetodon flavirostris* | 453 | 1352 | native ×2 | Brack/Meer | 2 |
| | **Grenze** | | | | | |
| 101 | *Chaetodon unimaculatus* | 450 | 1136 | native ×3 | Meer | 3 |
| 102 | *Chaetodon ulietensis* | 448 | 974 | native ×3 | Meer | 3 |
| 103 | *Dischistodus melanotus* | 436 | 912 | native ×3 | Meer | 3 |
| 104 | *Scarus altipinnis* | 433 | 2264 | native ×3 | Meer | 3 |
| 105 | *Halichoeres trimaculatus* | 432 | 674 | native ×2 | Meer | 3 |
| 106 | *Cheilinus fasciatus* (Quelle: *Concholabrus fasciatus*) | 430 | 2623 | native ×3 | Meer | 3 |
| 107 | *Centropyge bicolor* | 429 | 649 | native ×3 | Meer | 3 |
| 108 | *Acanthurus xanthopterus* | 426 | 767 | native ×3 | Meer | 3 |
| 109 | *Abudefduf vaigiensis* | 425 | 437 | native ×3 | Meer | 3 |
| 110 | *Caranx ignobilis* | 425 | 5083 | native ×3 | Brack/Meer | 3 |

### Level 3/nicht im Deck

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 143 | *Choerodon fasciatus* | 324 | 2690 | native ×3 | Meer | 3 |
| 144 | *Naso brevirostris* | 324 | 468 | native ×1 | Meer | 3 |
| 145 | *Thalassoma lutescens* | 323 | 567 | native ×2 | Meer | 3 |
| 146 | *Lethrinus harak* | 322 | 487 | native ×3 | Brack/Meer | 3 |
| 147 | *Pomacanthus semicirculatus* | 320 | 422 | native ×3 | Meer | 3 |
| 148 | *Coris batuensis* | 318 | 314 | native ×2 | Meer | 3 |
| 149 | *Cirripectes chelomatus* | 313 | 385 | native ×3 | Meer | 3 |
| 150 | *Anampses neoguinaicus* | 312 | 456 | native ×3 | Meer | 3 |
| 151 | *Diploprion bifasciatus* | 312 | 534 | native ×3 | Meer | 3 |
| 152 | *Scarus niger* | 301 | 3905 | native ×3 | Meer | 3 |
| | **Grenze** | | | | | |
| 153 | *Diagramma labiosum* | 300 | 219 | – | Brack/Meer | – |
| 154 | *Amphiprion clarkii* | 297 | 347 | native ×3 | Meer | – |
| 155 | *Scolopsis margaritifera* | 297 | 386 | native ×2 | Meer | – |
| 156 | *Ascarosepion latimanus* | 294 | 308 | native ×2 | Meer | – |
| 157 | *Halichoeres melanurus* | 294 | 615 | native ×2 | Meer | – |
| 158 | *Sepioteuthis lessoniana* | 291 | 224 | native ×3 | Brack/Meer | – |
| 159 | *Dascyllus trimaculatus* | 289 | 581 | native ×3 | Meer | – |
| 160 | *Heniochus monoceros* | 289 | 309 | native ×3 | Meer | – |
| 161 | *Pomacentrus adelus* | 288 | 1168 | native ×3 | Meer | – |
| 162 | *Acanthurus blochii* | 287 | 1636 | native ×2 | Meer | – |

## Abgleich mit Führern

Das Rezept nennt keinen Führer.
## Änderungen gegenüber dem bestehenden Deck

- neu: 0
- entfallen: 0

## Ausgeschlossene Kandidaten

<details><summary>558 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Gobiodon okinawae* | 93 | Meer | zu klein (höchstens 3.5 cm) |
| *Toxotes chatareus* | 90 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota sebreei* | 72 | Meer | zu klein (höchstens 2.5 cm) |
| *Bryaninops yongei* | 65 | Meer | zu klein (höchstens 3.5 cm) |
| *Spirula spirula* | 62 | Meer | nur tiefer als die Tauchgrenze (erst ab 100 m) |
| *Gobiodon histrio* | 57 | Meer | zu klein (höchstens 3.5 cm) |
| *Trimma benjamini* | 52 | Meer | zu klein (höchstens 3 cm) |
| *Eviota teresae* | 44 | Meer | zu klein (höchstens 2.11 cm) |
| *Hippocampus bargibanti* | 44 | Meer | zu klein (höchstens 2.4 cm) |
| *Eviota melasma* | 43 | Meer | zu klein (höchstens 3 cm) |
| *Toxotes jaculatrix* | 41 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ecsenius isos* | 36 | Meer | zu klein (höchstens 3.2 cm) |
| *Enneapterygius niger* | 30 | Meer | zu klein (höchstens 3.2 cm) |
| *Eviota atriventris* | 23 | Meer | zu klein (höchstens 1.71 cm) |
| *Eviota bacata* | 23 | Meer | zu klein (höchstens 2.5 cm) |
| *Bryaninops natans* | 22 | Meer | zu klein (höchstens 2.5 cm) |
| *Poecilia reticulata* | 21 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota prasites* | 17 | Meer | zu klein (höchstens 3 cm) |
| *Pleurosicya mossambica* | 16 | Meer | zu klein (höchstens 3 cm) |
| *Trimma capostriatum* | 16 | Meer | zu klein (höchstens 2.9 cm) |
| *Trimma lantana* | 16 | Meer | zu klein (höchstens 2.94 cm) |
| *Kuhlia marginata* | 13 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota longirostris* | 12 | Meer | zu klein (höchstens 1.78 cm) |
| *Eviota queenslandica* | 11 | Meer | zu klein (höchstens 2.4 cm) |
| *Foa fo* | 10 | Meer | zu klein (höchstens 3.5 cm) |
| *Galaxias neocaledonicus* | 10 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nautilus vanuatuensis* | 10 | Meer | nur tiefer als die Tauchgrenze (erst ab 200 m) |
| *Amblyeleotris callopareia* | 9 | Meer | nur tiefer als die Tauchgrenze (erst ab 50 m) |
| *Gobiodon ceramensis* | 9 | Meer | zu klein (höchstens 3.5 cm) |
| *Oreochromis mossambicus* | 9 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Tomiyamichthys nudus* | 9 | Meer | zu klein (höchstens 3.34 cm) |
| *Alectis ciliaris* | 8 | Meer | nur tiefer als die Tauchgrenze (erst ab 60 m) |
| *Eviota infulata* | 7 | Meer | zu klein (höchstens 2.5 cm) |
| *Eviota spilota* | 7 | Meer | zu klein (höchstens 2.41 cm) |
| *Lentipes kaaea* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma caesiura* | 7 | Meer | zu klein (höchstens 3.5 cm) |
| *Eviota hoesei* | 6 | Meer | zu klein (höchstens 2.05 cm) |
| *Protogobius attiti* | 6 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Solenostomus snuffleupagus* | 6 | ? | zu klein (höchstens 3.51 cm) |
| *Stiphodon sapphirinus* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ceratobregma helenae* | 5 | Meer | zu klein (höchstens 3.5 cm) |
| *Discotrema monogrammum* | 5 | Meer | zu klein (höchstens 2.32 cm) |
| *Fusigobius melacron* | 5 | Meer | zu klein (höchstens 3.52 cm) |
| *Gobiodon axillaris* | 5 | Meer | zu klein (höchstens 3.144 cm) |
| *Smilosicyopus chloe* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ablabys taenianotus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Acanthocybium solandri* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Acreichthys tomentosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Aioliops tetrophthalmus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Alepes apercna* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Anampses geographicus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Atropus mentalis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Carcharhinus falciformis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Chromis xanthochira* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Congrogadus subducens* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Ctenogobiops tangaroai* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Epinephelus corallicola* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Epinephelus spilotoceps* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Eviota fallax* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Eviota nigriventris* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Giuris aporocephalus* | 4 | ? | zu wenige Nachweise (4 < 5) |
| *Giuris viator* | 4 | ? | zu wenige Nachweise (4 < 5) |
| *Gymnothorax cribroris* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gymnothorax richardsonii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hippocampus spinosissimus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Hypseleotris guentheri* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Idiosepius pygmaeus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Istiompax indica* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Johnius amblycephalus* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Lactarius lactarius* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Lubricogobius ornatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lutjanus rufolineatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Meiacanthus ditrema* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Mugil cephalus* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Neocirrhites armatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Netuma thalassina* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Omobranchus obliquus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Ostorhinchus apogonoides* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ostorhinchus neotes* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Oxycheilinus nigromarginatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Periophthalmus gracilis* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Pomacentrus imitator* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pomadasys maculatus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Poroanthias pelicieri* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Praealticus bilineatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pseudanthias rubrizonatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Rhabdamia gracilis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scorpaena jacksoniensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scorpaenodes guamensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scorpaenopsis venosa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sphyraena helleri* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sphyraena putnamae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Strophidon sathete* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Synodus jaculum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Thaumoctopus mimicus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Thunnus tonggol* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Trachyrhamphus bicoarctatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Trimma nasa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Trimma taylori* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Valenciennea alleni* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Valenciennea randalli* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Yarica hyalosoma* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Anampses melanurus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Anguilla megastoma* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Arotrolepis filicauda* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bleheratherina pierucciae* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Callionymus macdonaldi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Calotomus carolinus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Caracanthus unipinna* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Caranx lugubris* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Carcharhinus brevipinna* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Centropyge colini* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chaetodon meyeri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chaetodontoplus conspicillatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chelmon marginalis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Choerodon cephalotes* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Choerodon venustus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cirrhilabrus bathyphilus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cirripectes polyzona* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Coryphaena hippurus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Cryptocentrus cebuanus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dactylopus kuiteri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dipterygonotus balteatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dunckerocampus naia* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Eleotris fusca* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Enneapterygius atrogulare* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Epinephelus sexfasciatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Exyrias puntang* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Gazza minuta* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Gerres erythrourus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Glossogobius illimis* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Glyptoparus delicatulus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gobiodon fuscoruber* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gobiodon spadix* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gunnellichthys viridescens* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gymnothorax enigmaticus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Halicampus boothae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Halicampus macrorhynchus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Herklotsichthys koningsbergeri* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Herklotsichthys quadrimaculatus* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Hippocampus colemani* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hypseleotris compressa* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lactoria fornasini* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Leptojulis cyanopleura* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lobotes surinamensis* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Malvoliophis pinguis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mobula kuhlii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mobula thurstoni* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Monacanthus chinensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Moolgarda seheli* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Myripristis botche* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Myripristis pralinia* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Nautilus stenomphalus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Nemanthias bicolor* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Nemateleotris decora* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ostorhinchus jenkinsi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Parioglossus formosus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Pateobatis jenkinsii* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Platycephalus endrachtensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pleurosicya muscarum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Priolepis nuchifasciata* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Pseudanthias fasciatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pseudochromis wilsoni* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pseudorhombus jenynsii* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Ptereleotris monoptera* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Redigobius bikolanus* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Rhizoprionodon taylori* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rudarius minutus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sargocentron cornutum* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Sebastapistes strongia* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sepia whitleyana* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Siganus randalli* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Solenostomus leptosoma* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Strongylura incisa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Suezichthys devisi* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Synchiropus splendidus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tomiyamichthys lanceolatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Torquigener hypselogeneion* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Trimma anaima* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Trimma maiandros* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Upeneus vittatus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Verulux cypselurus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ablennes hians* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Acanthopagrus akazakii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acreichthys radiatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Aioliops novaeguineae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Albula oligolepis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ambassis vachellii* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Amblyeleotris randalli* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Amblypomacentrus tricinctus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ancistrogobius yoshigoui* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Antennarius maculatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Apogon crassiceps* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Aptychotrema rostrata* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Argyrops spinifer* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Azurina elerae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bathygobius cocosensis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Bathygobius cyclopterus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Blenniella interrupta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bodianus bimaculatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bryaninops loki* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Callechelys marmorata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Callionymus enneactis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Calotomus spinidens* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Canthigaster axiologus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Carcharhinus cautus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Carcharhinus plumbeus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Carcharias taurus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Carcharodon carcharias* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Centriscus scutatus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Centropyge fisheri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chaetodon guentheri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chaetodon ocellicaudus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chaetodon semeion* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cymolutes praetextatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Echinogobius hayashii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epinephelus magniscuttis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epinephelus undulatostriatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eviota bifasciata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eviota lateritea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eviota maculosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Eviota oculineata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Exocoetus volitans* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fusigobius aureus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fusigobius humeralis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Glaucosoma magnificum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gobiodon brochus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gobiodon oculolineatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gorgasia barnesi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnocranius microdon* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnothorax margaritophorus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Halichoeres hartzfeldii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hazeus ammophilus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hemigaleus australiensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hemiscyllium hallstromi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hippocampus dahli* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hologymnosus longipes* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hypoplectrodes jamesoni* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Inimicus didactylus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Istiophorus platypterus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lactoria diaphana* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Leiuranus versicolor* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Leptobrama muelleri* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Leptobrama pectoralis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Lethrinus genivittatus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Lethrinus ravus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lethrinus semicinctus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lotilia klausewitzi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lutjanus bengalensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lutjanus ehrenbergii* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Melanotaenia splendida* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Myripristis amaena* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Myxus elongatus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Naso mcdadei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Naso thynnoides* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nectamia luxuria* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nectamia viria* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Neotrygon australiae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nibea soldado* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Ostorhinchus flavus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ostorhinchus hoevenii* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Ostorhinchus limenus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Oxyurichthys notonema* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Paracentropogon vespa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Paragobiodon lacunicola* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Paramonacanthus curtorhynchos* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Parapercis xanthogramma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Paraplagusia guttata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pelates quadrilineatus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Pempheris analis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Planiliza subviridis* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Pleurosicya boldinghi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plicofollis argyropleuron* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Polydactylus macrochir* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Polydactylus sexfilis* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Priolepis cincta* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Pseudamia gelatinosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudanthias engelhardi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudochromis cyanotaenia* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudomugil signifer* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudorhombus arsius* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Ptereleotris hanae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pteropterus paucispinula* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pycnochromis delta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pycnochromis lineatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Redigobius balteatus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Rhina ancylostomus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rhynchorhamphus georgii* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Sargocentron ittodai* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sargocentron praslin* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sargocentron violaceum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sarotherodon occidentalis* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Saurida tumbil* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scarus xanthopleura* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scomber australasicus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Selaroides leptolepis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Spratelloides delicatulus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Squalomugil nasutus* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Stenogobius yateiensis* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Stonogobiops xanthorhinicus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Synodus rubromarmoratus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trichiurus lepturus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Trimma cana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trimma fangi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Turrum coeruleopinnatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Uropterygius marmoratus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Uropterygius micropterus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Valenciennea immaculata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Xanthichthys auromarginatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Abdopus aculeatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acanthurus bariene* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acanthurus nubilus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acentrogobius caninus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Acentrogobius nigromaculatus* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Aetomylaeus caeruleofasciatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alticus sertatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ambassis interrupta* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Amblyeleotris biguttata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amblyeleotris yanoi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amblygobius buanensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amblygobius linki* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amblypomacentrus breviceps* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anoplocapros inermis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Antennarius hispidus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aphareus rutilans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Apistops caloundra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Apistus carinatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Apogon doryssa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Apogonichthyoides timorensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Apogonichthys ocellatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Argyrosomus japonicus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Arripis trutta* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Aseraggodes magnoculus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Asterropteryx striata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Atherinomorus endrachtensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Atrosalarias hosokawai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aurigequula fasciata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Auxis thazard* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Awaous ocellaris* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Bathygobius krefftii* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Bathygobius laddi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Batrachomoeus trispinosus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Bodianus paraleucosticticus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Brachaluteres jacksonianus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Callionymus keeleyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Callionymus rivatoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calloplesiops altivelis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cantherhines fronticinctus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Canthigaster amboinensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Caranx tille* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carapus mourlani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carcharhinus fitzroyensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Carcharhinus galapagensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carcharhinus macloti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carcharhinus obscurus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Centropyge woodheadi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cercamia cladara* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cestraeus plicatilis* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Cetoscarus bicolor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaetodermis penicilligerus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheilodipterus alleni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheilopogon pinnatibarbatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chilomycterus reticulatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chromis scotochiloptera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirrhilabrus beauperryi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirrhilabrus condei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirrhilabrus efatensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirrhitichthys aprinus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Cirripectes springeri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conidens samoensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cymbacephalus bosschei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cynoglossus quadrilineatus* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Cyprinus rubrofuscus* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cypselurus poecilopterus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Decodon erythroleukos* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Dermochelys coriacea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diodon holocanthus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dunckerocampus dactyliophorus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echidna polyzona* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echidna rhodochilus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Ecsenius tessera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ecsenius tigris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Engraulis australis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus morrhua* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Etelis coruscans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Euprymna berryi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eviota ancora* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eviota bipunctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eviota dorsogilva* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eviota fasciola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eviota prasina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eviota sigillata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Evoxymetopon poeyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Exyrias akihito* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Favonigobius exquisitus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Favonigobius lentiginosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Favonigobius melanobranchus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Festucalex kulbickii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fibramia amboinensis* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Fibramia thermalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Filicampus tigris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gobiodon acicularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gobiodon aoyagii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gobiodon prolixus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gobiodon spilophthalmus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Goniistius francisi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gorgasia maculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gunnellichthys curiosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnocranius grandoculis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax chilospilus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax minor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax porphyreus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax zonipectis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halicampus brocki* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Helcogramma chica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Helcogramma trigloides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hemitrygon fluviorum* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Herklotsichthys lippa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Heteroconger polyzona* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Heteropriacanthus carolinus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Himantura uarnak* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Hippichthys spicifer* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Hippocampus pontohi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hippocampus trimaculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hippocampus zebra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hirundichthys rufipinnis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hyporhamphus australis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Hyporhamphus regularis* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Iracundus signifer* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Istigobius nigroocellatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Katsuwonus pelamis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Kyonemichthys rumengani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Kyphosus sydneyanus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Labropsis alleni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lagocephalus inermis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lagocephalus spadiceus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Leiognathus equula* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Lethrinus amboinensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lethrinus microdon* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Liocranium praepositum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lutjanus fuscescens* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Luzonichthys whitleyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Meiacanthus limbatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Meiacanthus phaeus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Melanotaenia maccullochi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Metasepia pfefferi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Microcanthus strigatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Micrognathus pygmaeus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Microphis cruentus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mobula tarapacana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mola alexandrini* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Monothrix polylepis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mugilogobius mertoni* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Naso caeruleacauda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Naso lopezi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nectamia bandanensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nematalosa erebi* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nemipterus hexodon* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nemipterus nematopus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neoniphon aurolineatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neoniphon opercularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nomeus gronovii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Norfolkia thomasi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Notograptus guttatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Novaculoides macrolepidotus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Octopus wolfi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Omobranchus rotundiceps* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Omox biporos* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Onigocia bimaculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Onigocia spinosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Onuxodon parvibrachium* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Opistognathus seminudus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oplopomops diacanthus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oplopomus caninoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ostorhinchus fasciatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ostorhinchus kiensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Ostorhinchus pallidofasciatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ostorhinchus taeniophorus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Otolithes ruber* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Oxycheilinus arenatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxycheilinus samurai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxymetopon compressus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxyurichthys auchenolepis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxyurichthys papuensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Paragobiodon xanthosoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paramonacanthus otisensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paraplotosus albilabris* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Paraplotosus butleri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paratrypauchen microcephalus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Parioglossus rainfordi* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Parupeneus heptacantha* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pentapodus numberii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Petroscirtes breviceps* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pisodonophis cancrivorus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Plectorhinchus caeruleonothus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plesiops coeruleolineatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pleurosicya bilobata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pleurosicya micheli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomacentrus novaeguineae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Priolepis akihitoi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Priolepis semidoliata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pristipomoides filamentosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pristis zijsron* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Protonibea diacanthus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Psammogobius biocellatus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Psammogobius pisinnus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudanthias flavicauda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pyronotanthias timanoa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Regalecus glesne* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Remora osteochir* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhabdamia novaluna* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhabdoblennius snowi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhabdosargus sarba* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Rotuma lewisi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rudarius excelsus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Salarias segmentatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Samariscus triocellatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sargocentron tiere* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Satyrichthys welchi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Saurida undosquamis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Schindleria praematura* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scorpaenopsis macrochir* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Sepia mira* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sepia papuensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Seriola rivoliana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Seriolina nigrofasciata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Sicyopterus sarasini* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Siganus guttatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Siganus stellatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Siganus virgatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Sillago burrus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Solegnathus dunckeri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Soleichthys maculosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Solenostomus paegnius* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Spratelloides gracilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stanulus seychellensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stiphodon mele* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Synchiropus moyeri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Taeniamia leai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Taeniamia macroptera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thalassoma jansenii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thryssa nasuta* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Thysanoteuthis rhombus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trachurus novaezelandiae* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Trachyrhamphus longirostris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Triacanthus biaculeatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Trimma hollemani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trimma kitrinum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trimmatom eviotops* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Triodon macropterus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Upeneus sundaicus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Uroteuthis edulis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Valenciennea wardii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Wattsia mossambica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xiphasia matsubarai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xiphophorus hellerii* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Zapogon evermanni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Zoramia perlita* | 1 | Meer | zu wenige Nachweise (1 < 5) |

</details>

## Nicht aufgelöste Namen der Reihenfolge-Quelle

Die Referenz-DB der App kennt diese Namen nicht; die App fände sie auch nicht.

| Name | iNat |
|---|---|
| *Stolephorus* | 3 |
| *Chrysophrys auratus* | 1 |
| *Hapalochlaena* | 1 |
| *Lampris* | 1 |
| *Paracheilinus amanda* | 1 |
| *Pegasus* | 1 |
