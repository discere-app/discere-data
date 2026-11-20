# Bericht: Korallendreieck (`recipes/korallendreieck.json`)

Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.

- Referenz-DB: v3 (FishBase v26.06, SeaLifeBase v26.06)
- Salz/Süß: FishBase/SeaLifeBase v25.04 (species.parquet)
- iNaturalist: 3082 Taxa (Seiten: 7)
- OBIS: 6311 Arten
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
| *Wunderpus photogenicus* | Der Wunderpus ist der gestreifte Krake, wegen dem viele Taucher nach Lembeh kommen. | 253 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |

## Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS oder Verbreitung): 158/158 (100 %)
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

Spalten: Rang unter den Kandidaten, Zählung der Reihenfolge-Quelle (iNat), OBIS-Nachweise, Einträge der FishBase/SeaLifeBase-Verbreitung in den Rezept-Regionen (~~durchgestrichen~~: Eintrag sagt „nicht vorhanden“), Wasser laut FishBase/SeaLifeBase.

### Level 1 (48)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 1 | *Amphiprion clarkii* | 2925 | 2582 | native ×6 | Meer |
| 2 | *Chelonia mydas* | 2830 | 5124 | native ×6 | Meer |
| 3 | *Amphiprion ocellaris* | 2358 | 2113 | native ×6 | Meer |
| 4 | *Arothron nigropunctatus* | 2244 | 1948 | native ×4 | Meer |
| 5 | *Zanclus cornutus* | 2148 | 2368 | native ×4 | Meer |
| 6 | *Eretmochelys imbricata* | 1896 | 2043 | native ×6 | Brack/Meer |
| 7 | *Pteropterus antennatus* | 1599 | 353 | native ×4 | Meer |
| 8 | *Solenostomus paradoxus* | 1595 | 1231 | native ×6 | Meer |
| 9 | *Aulostomus chinensis* | 1593 | 1328 | native ×4 | Meer |
| 10 | *Pterois volitans* | 1564 | 1446 | native ×5 | Meer |
| 11 | *Dascyllus trimaculatus* | 1538 | 1809 | native ×6 | Meer |
| 12 | *Chaetodon kleinii* | 1502 | 1914 | native ×6 | Meer |
| 13 | *Ascarosepion latimanus* | 1446 | 1108 | native ×5 | Meer |
| 14 | *Canthigaster valentini* | 1403 | 1328 | native ×4 | Meer |
| 15 | *Amphiprion perideraion* | 1349 | 1374 | native ×6 | Brack/Meer |
| 16 | *Amphiprion biaculeatus* | 1344 | 1055 | native ×6 | Meer |
| 17 | *Thalassoma lunare* | 1270 | 2091 | native ×5 | Meer |
| 18 | *Abudefduf vaigiensis* (Quelle: *Abudefduf caudobimaculatus*) | 1239 | 1374 | native ×6 | Meer |
| 19 | *Balistapus undulatus* | 1236 | 2542 | native ×5 | Meer |
| 20 | *Pygoplites diacanthus* | 1201 | 1495 | native ×5 | Meer |
| 21 | *Taenianotus triacanthus* | 1197 | 942 | native ×5 | Meer |
| 22 | *Plotosus lineatus* | 1190 | 1157 | native ×5 | Brack/Meer |
| 23 | *Plectorhinchus chaetodonoides* | 1174 | 1067 | native ×4 | Brack/Meer |
| 24 | *Hippocampus histrix* | 1123 | 797 | native ×4 | Meer |
| 25 | *Gymnothorax thyrsoideus* | 1116 | 934 | native ×5 | Meer |
| 26 | *Arothron mappa* | 1112 | 913 | native ×4 | Meer |
| 27 | *Rhinomuraena quaesita* | 1107 | 823 | native ×4 | Meer |
| 28 | *Balistoides viridescens* | 1098 | 1044 | native ×4 | Meer |
| 29 | *Dascyllus reticulatus* | 1095 | 1544 | native ×5 | Meer |
| 30 | *Halichoeres hortulanus* | 1071 | 1582 | native ×4 | Meer |
| 31 | *Chaetodon lunulatus* | 1065 | 504 | native ×4 | Meer |
| 32 | *Chaetodon baronessa* | 1063 | 1430 | native ×5 | Meer |
| 33 | *Echidna nebulosa* | 1059 | 944 | native ×5 | Meer |
| 34 | *Thalassoma hardwicke* | 1057 | 1487 | native ×5 | Meer |
| 35 | *Odonus niger* | 1044 | 1037 | native ×5 | Meer |
| 36 | *Heniochus varius* | 1043 | 1197 | native ×5 | Meer |
| 37 | *Scolopsis bilineata* | 1035 | 1416 | native ×6 | Meer |
| 38 | *Dendrochirus zebra* | 1031 | 958 | native ×4 | Meer |
| 39 | *Ostracion cubicum* | 999 | 921 | native ×5 | Meer |
| 40 | *Amblyglyphidodon curacao* | 995 | 1095 | native ×6 | Meer |
| 220 | *Rhincodon typus* (Highlight) | 381 | 3219 | native ×7 | Meer |
| 681 | *Mobula birostris* (Highlight) | 73 | 99 | native ×4 | Meer |
| 611 | *Mola alexandrini* (Highlight) | 92 | 65 | – | Meer |
| – | *Hippocampus bargibanti* (Highlight) | 1139 | 854 | native ×5 | Meer |
| 218 | *Synchiropus splendidus* (Highlight) | 385 | 327 | native ×5 | Meer |
| 420 | *Hemiscyllium freycineti* (Highlight) | 168 | 139 | native ×2 | Meer |
| 95 | *Metasepia pfefferi* (Highlight) | 638 | – | native ×2 | Meer |
| 253 | *Wunderpus photogenicus* (Highlight) | 335 | 258 | native ×6 | Meer |

### Level 2 (60)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 41 | *Gymnothorax javanicus* | 993 | 824 | native ×5 | Meer |
| 42 | *Chaetodon vagabundus* | 988 | 1470 | native ×4 | Meer |
| 43 | *Pomacentrus moluccensis* | 968 | 1198 | native ×6 | Meer |
| 44 | *Labroides dimidiatus* | 957 | 1771 | native ×5 | Meer |
| 45 | *Macolor macularis* | 950 | 1018 | native ×7 | Meer |
| 46 | *Pomacanthus imperator* | 928 | 805 | native ×5 | Meer |
| 47 | *Amblyglyphidodon aureus* | 924 | 996 | native ×6 | Meer |
| 48 | *Pseudanthias huchtii* | 924 | 1157 | native ×5 | Meer |
| 49 | *Paracirrhites forsteri* | 923 | 966 | native ×4 | Meer |
| 50 | *Acanthurus lineatus* | 896 | 1990 | native ×6 | Meer |
| 51 | *Amphiprion frenatus* | 887 | 738 | native ×3 | Meer |
| 52 | *Mobula alfredi* | 880 | 631 | native ×2 | Süß/Meer |
| 53 | *Octopus cyanea* | 866 | 681 | native ×6 | Meer |
| 54 | *Arothron hispidus* | 862 | 910 | native ×5 | Brack/Meer |
| 55 | *Antennarius pictus* | 849 | 643 | native ×3 | Meer |
| 56 | *Chlorurus bleekeri* | 842 | 1152 | native ×5 | Meer |
| 57 | *Antennarius maculatus* | 838 | 598 | native ×4 | Meer |
| 58 | *Ostracion meleagris* | 835 | 718 | native ×4 | Meer |
| 59 | *Ctenochaetus striatus* | 821 | 2744 | native ×5 | Meer |
| 60 | *Zebrasoma scopas* | 819 | 1671 | native ×5 | Meer |
| 61 | *Neochirus brachyptera* | 818 | 103 | native ×5 | Meer |
| 62 | *Hemigymnus melapterus* | 803 | 1071 | native ×5 | Meer |
| 63 | *Arothron manilensis* | 784 | 778 | native ×5 | Brack/Meer |
| 64 | *Fistularia commersonii* | 784 | 719 | native ×5 | Meer |
| 65 | *Cephalopholis miniata* | 780 | 797 | native ×6 | Meer |
| 66 | *Acanthurus pyroferus* | 777 | 1445 | native ×4 | Meer |
| 67 | *Coris gaimard* | 777 | 735 | native ×6 | Meer |
| 68 | *Cheilinus fasciatus* (Quelle: *Concholabrus fasciatus*) | 771 | 1072 | native ×5 | Meer |
| 69 | *Centropyge bicolor* | 768 | 1066 | native ×6 | Meer |
| 70 | *Antennarius commerson* | 760 | 542 | native ×3 | Meer |
| 71 | *Carcharhinus melanopterus* | 757 | 812 | native ×6 | Brack/Meer |
| 72 | *Chaetodon rafflesii* | 753 | 943 | native ×4 | Brack/Meer |
| 73 | *Melichthys vidua* (Quelle: *Melichthys vidua × indicus*) | 752 | 1041 | native ×5 | Meer |
| 74 | *Dunckerocampus dactyliophorus* | 751 | 745 | native ×3 | Meer |
| 75 | *Taeniura lymma* | 742 | 795 | native ×6 | Meer |
| 76 | *Amphiprion polymnus* (Quelle: *Amphiprion annamensis*) | 741 | 632 | native ×6 | Meer |
| 77 | *Gymnothorax flavimarginatus* | 741 | 662 | native ×3 | Meer |
| 78 | *Caranx melampygus* | 730 | 860 | native ×7 | Brack/Meer |
| 79 | *Pomacentrus coelestis* | 714 | 998 | native ×4 | Meer |
| 80 | *Halichoeres scapularis* | 689 | 756 | native ×6 | Meer |
| 81 | *Naso vlamingii* | 689 | 702 | native ×5 | Meer |
| 82 | *Triaenodon obesus* | 688 | 675 | native ×6 | Meer |
| 83 | *Abudefduf sexfasciatus* | 682 | 745 | native ×6 | Meer |
| 84 | *Neoglyphidodon nigroris* | 680 | 832 | native ×5 | Meer |
| 85 | *Chlorurus spilurus* | 675 | 588 | native ×4 | Meer |
| 86 | *Lutjanus decussatus* | 672 | 704 | native ×5 | Meer |
| 87 | *Plectorhinchus vittatus* | 670 | 606 | native ×6 | Meer |
| 88 | *Rhinecanthus verrucosus* | 670 | 627 | native ×6 | Meer |
| 89 | *Amphiprion sandaracinos* | 665 | 537 | native ×6 | Meer |
| 90 | *Dascyllus aruanus* | 662 | 791 | native ×5 | Meer |
| 91 | *Canthigaster papua* | 651 | 487 | native ×5 | Meer |
| 92 | *Cirrhitichthys falco* | 646 | 661 | native ×5 | Meer |
| 93 | *Hippocampus kuda* | 643 | 555 | native ×6 | Brack/Meer |
| 94 | *Oxycheilinus bimaculatus* | 643 | 802 | native ×5 | Meer |
| 96 | *Amphioctopus marginatus* | 637 | 488 | native ×4 | Meer |
| 97 | *Cheilinus undulatus* | 635 | 637 | native ×5 | Meer |
| 98 | *Helcogramma striata* | 629 | 609 | native ×5 | Meer |
| 99 | *Scolopsis lineata* | 629 | 634 | native ×6 | Meer |
| 100 | *Balistoides conspicillum* | 627 | 551 | native ×4 | Brack/Meer |
| 101 | *Chaetodon adiergastos* | 626 | 543 | native ×4 | Meer |

### Level 3 (50)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 102 | *Hemitaurichthys polylepis* | 623 | 584 | native ×4 | Meer |
| 103 | *Parupeneus barberinus* | 623 | 897 | native ×6 | Meer |
| 104 | *Aluterus scriptus* | 622 | 593 | native ×5 | Meer |
| 105 | *Chaetodon speculum* | 613 | 504 | native ×5 | Meer |
| 106 | *Gymnothorax fimbriatus* | 612 | 573 | native ×4 | Brack/Meer |
| 107 | *Scarus dimidiatus* | 607 | 825 | native ×6 | Brack/Meer |
| 108 | *Solenostomus cyanopterus* | 603 | 460 | native ×4 | Meer |
| 109 | *Chaetodon octofasciatus* | 602 | 688 | native ×5 | Meer |
| 110 | *Cephalopholis argus* | 601 | 856 | native ×6 | Meer |
| 111 | *Pomacanthus navarchus* | 594 | 483 | native ×5 | Meer |
| 112 | *Chaetodon melannotus* | 591 | 600 | native ×5 | Meer |
| 113 | *Chaetodontoplus mesoleucus* | 591 | 598 | native ×5 | Meer |
| 114 | *Oxycheilinus digramma* | 591 | 858 | native ×5 | Brack/Meer |
| 115 | *Scolopsis margaritifera* | 591 | 797 | native ×6 | Meer |
| 116 | *Siganus vulpinus* | 585 | 715 | native ×5 | Meer |
| 117 | *Platax pinnatus* | 584 | 570 | native ×6 | Meer |
| 118 | *Plectorhinchus lineatus* | 580 | 557 | native ×6 | Meer |
| 119 | *Forcipiger flavissimus* | 577 | 645 | native ×4 | Meer |
| 120 | *Acanthurus nigricans* (Quelle: *Acanthurus nigricans × leucosternon*) | 573 | 690 | native ×5 | Meer |
| 121 | *Bodianus mesothorax* | 573 | 718 | native ×6 | Meer |
| 122 | *Pseudanthias squamipinnis* | 572 | 261 | native ×5 | Meer |
| 123 | *Dischistodus perspicillatus* | 569 | 474 | native ×6 | Brack/Meer |
| 124 | *Platax teira* | 566 | 646 | native ×5 | Meer |
| 125 | *Chaetodon trifascialis* | 565 | 693 | native ×5 | Meer |
| 126 | *Choerodon anchorago* | 556 | 761 | native ×5 | Meer |
| 127 | *Heniochus chrysostomus* | 556 | 670 | native ×4 | Meer |
| 128 | *Parupeneus multifasciatus* | 551 | 1233 | native ×5 | Meer |
| 129 | *Centropyge vrolikii* | 550 | 1137 | native ×5 | Meer |
| 130 | *Lactoria fornasini* | 550 | 411 | native ×2 | Meer |
| 131 | *Synodus variegatus* | 549 | 959 | native ×4 | Meer |
| 132 | *Nemateleotris magnifica* | 548 | 538 | native ×5 | Meer |
| 133 | *Caranx sexfasciatus* | 547 | 784 | native ×7 | Süß/Brack/Meer |
| 134 | *Sepioteuthis lessoniana* | 540 | 378 | native ×6 | Brack/Meer |
| 135 | *Plectorhinchus polytaenia* | 539 | 461 | native ×5 | Meer |
| 136 | *Bodianus dictynna* | 533 | 450 | native ×6 | Meer |
| 137 | *Cheilinus chlorourus* | 529 | 688 | native ×6 | Meer |
| 138 | *Cephalopholis cyanostigma* | 520 | 705 | native ×6 | Meer |
| 139 | *Caesio caerulaurea* | 514 | 815 | native ×6 | Meer |
| 140 | *Pentapodus trivittatus* | 512 | 486 | native ×6 | Meer |
| 141 | *Pomacentrus amboinensis* | 512 | 850 | native ×5 | Meer |
| 142 | *Amblyglyphidodon leucogaster* | 511 | 625 | native ×4 | Meer |
| 143 | *Dischistodus melanotus* | 506 | 420 | native ×6 | Meer |
| 144 | *Amphiprion melanopus* | 503 | 438 | native ×5 | Meer |
| 145 | *Mirolabrichthys tuka* | 503 | 586 | native ×5 | Meer |
| 146 | *Diodon hystrix* | 500 | 449 | native ×5 | Meer |
| 147 | *Plagiotremus rhinorhynchos* | 500 | 556 | native ×5 | Meer |
| 148 | *Epinephelus merra* | 499 | 896 | native ×6 | Meer |
| 149 | *Valenciennea puellaris* | 498 | 463 | native ×5 | Meer |
| 150 | *Cymbacephalus beauforti* | 495 | 401 | native ×4 | Meer |
| 151 | *Sufflamen chrysopterum* | 495 | 653 | native ×4 | Meer |

## Grenzfälle

Je 10 Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels sie nehmen (Highlights ab Level 2 übersprungen).

### Level 1/2

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 31 | *Chaetodon lunulatus* | 1065 | 504 | native ×4 | Meer | 1 |
| 32 | *Chaetodon baronessa* | 1063 | 1430 | native ×5 | Meer | 1 |
| 33 | *Echidna nebulosa* | 1059 | 944 | native ×5 | Meer | 1 |
| 34 | *Thalassoma hardwicke* | 1057 | 1487 | native ×5 | Meer | 1 |
| 35 | *Odonus niger* | 1044 | 1037 | native ×5 | Meer | 1 |
| 36 | *Heniochus varius* | 1043 | 1197 | native ×5 | Meer | 1 |
| 37 | *Scolopsis bilineata* | 1035 | 1416 | native ×6 | Meer | 1 |
| 38 | *Dendrochirus zebra* | 1031 | 958 | native ×4 | Meer | 1 |
| 39 | *Ostracion cubicum* | 999 | 921 | native ×5 | Meer | 1 |
| 40 | *Amblyglyphidodon curacao* | 995 | 1095 | native ×6 | Meer | 1 |
| | **Grenze** | | | | | |
| 41 | *Gymnothorax javanicus* | 993 | 824 | native ×5 | Meer | 2 |
| 42 | *Chaetodon vagabundus* | 988 | 1470 | native ×4 | Meer | 2 |
| 43 | *Pomacentrus moluccensis* | 968 | 1198 | native ×6 | Meer | 2 |
| 44 | *Labroides dimidiatus* | 957 | 1771 | native ×5 | Meer | 2 |
| 45 | *Macolor macularis* | 950 | 1018 | native ×7 | Meer | 2 |
| 46 | *Pomacanthus imperator* | 928 | 805 | native ×5 | Meer | 2 |
| 47 | *Amblyglyphidodon aureus* | 924 | 996 | native ×6 | Meer | 2 |
| 48 | *Pseudanthias huchtii* | 924 | 1157 | native ×5 | Meer | 2 |
| 49 | *Paracirrhites forsteri* | 923 | 966 | native ×4 | Meer | 2 |
| 50 | *Acanthurus lineatus* | 896 | 1990 | native ×6 | Meer | 2 |

### Level 2/3

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 91 | *Canthigaster papua* | 651 | 487 | native ×5 | Meer | 2 |
| 92 | *Cirrhitichthys falco* | 646 | 661 | native ×5 | Meer | 2 |
| 93 | *Hippocampus kuda* | 643 | 555 | native ×6 | Brack/Meer | 2 |
| 94 | *Oxycheilinus bimaculatus* | 643 | 802 | native ×5 | Meer | 2 |
| 96 | *Amphioctopus marginatus* | 637 | 488 | native ×4 | Meer | 2 |
| 97 | *Cheilinus undulatus* | 635 | 637 | native ×5 | Meer | 2 |
| 98 | *Helcogramma striata* | 629 | 609 | native ×5 | Meer | 2 |
| 99 | *Scolopsis lineata* | 629 | 634 | native ×6 | Meer | 2 |
| 100 | *Balistoides conspicillum* | 627 | 551 | native ×4 | Brack/Meer | 2 |
| 101 | *Chaetodon adiergastos* | 626 | 543 | native ×4 | Meer | 2 |
| | **Grenze** | | | | | |
| 102 | *Hemitaurichthys polylepis* | 623 | 584 | native ×4 | Meer | 3 |
| 103 | *Parupeneus barberinus* | 623 | 897 | native ×6 | Meer | 3 |
| 104 | *Aluterus scriptus* | 622 | 593 | native ×5 | Meer | 3 |
| 105 | *Chaetodon speculum* | 613 | 504 | native ×5 | Meer | 3 |
| 106 | *Gymnothorax fimbriatus* | 612 | 573 | native ×4 | Brack/Meer | 3 |
| 107 | *Scarus dimidiatus* | 607 | 825 | native ×6 | Brack/Meer | 3 |
| 108 | *Solenostomus cyanopterus* | 603 | 460 | native ×4 | Meer | 3 |
| 109 | *Chaetodon octofasciatus* | 602 | 688 | native ×5 | Meer | 3 |
| 110 | *Cephalopholis argus* | 601 | 856 | native ×6 | Meer | 3 |
| 111 | *Pomacanthus navarchus* | 594 | 483 | native ×5 | Meer | 3 |

### Level 3/nicht im Deck

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 142 | *Amblyglyphidodon leucogaster* | 511 | 625 | native ×4 | Meer | 3 |
| 143 | *Dischistodus melanotus* | 506 | 420 | native ×6 | Meer | 3 |
| 144 | *Amphiprion melanopus* | 503 | 438 | native ×5 | Meer | 3 |
| 145 | *Mirolabrichthys tuka* | 503 | 586 | native ×5 | Meer | 3 |
| 146 | *Diodon hystrix* | 500 | 449 | native ×5 | Meer | 3 |
| 147 | *Plagiotremus rhinorhynchos* | 500 | 556 | native ×5 | Meer | 3 |
| 148 | *Epinephelus merra* | 499 | 896 | native ×6 | Meer | 3 |
| 149 | *Valenciennea puellaris* | 498 | 463 | native ×5 | Meer | 3 |
| 150 | *Cymbacephalus beauforti* | 495 | 401 | native ×4 | Meer | 3 |
| 151 | *Sufflamen chrysopterum* | 495 | 653 | native ×4 | Meer | 3 |
| | **Grenze** | | | | | |
| 152 | *Thalassoma amblycephalum* | 488 | 940 | native ×5 | Meer | – |
| 153 | *Lutjanus biguttatus* | 485 | 563 | native ×7 | Meer | – |
| 154 | *Epinephelus fasciatus* | 483 | 630 | native ×6 | Brack/Meer | – |
| 155 | *Chaetodon ornatissimus* | 481 | 618 | native ×4 | Meer | – |
| 156 | *Chaetodon lunula* | 475 | 573 | native ×4 | Meer | – |
| 157 | *Cyclichthys orbicularis* | 475 | 428 | native ×4 | Meer | – |
| 158 | *Cetoscarus ocellatus* | 471 | 472 | native ×6 | Meer | – |
| 159 | *Ostracion solorense* | 471 | 373 | native ×4 | Meer | – |
| 160 | *Pomacentrus bankanensis* | 471 | 697 | native ×5 | Meer | – |
| 161 | *Sargocentron caudimaculatum* | 470 | 672 | native ×5 | Meer | – |

## Abgleich mit Führern

Das Rezept nennt keinen Führer.
## Änderungen gegenüber dem bestehenden Deck

- neu: 1: *Pseudanthias squamipinnis*
- entfallen: 1: *Thalassoma amblycephalum*

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
| *Channa gachua* | 129 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
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
| *Monopterus albus* | 80 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
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
| *Sepiadarium kochi* | 51 | Meer | nur tiefer als die Tauchgrenze (erst ab 60 m) |
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
| *Puntius sealei* | 43 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
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
| *Hemibagrus fortis* | 19 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
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
| *Eviota storthynx* | 14 | Meer | zu klein (höchstens 2.5 cm) |
| *Grallenia baliensis* | 14 | Meer | zu klein (höchstens 1.48 cm) |
| *Lentipes palawanirufus* | 14 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora lateristriata* | 14 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Wallago leerii* | 14 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
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
| *Eviota infulata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
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
| *Anematichthys repasson* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
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
| *Halichoeres vrolikii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
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
| *Thrissina samam* | 3 | ? | zu wenige Nachweise (3 < 5) |
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
| *Doryichthys boaja* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
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
| *Synchiropus corallinus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
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
| *Centropyge flavissima* | 1 | Meer | zu wenige Nachweise (1 < 5) |
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
| *Enneapterygius rubicauda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
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
| *Phoxocampus tetrophthalmus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phractocephalus hemioliopterus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pictichromis aurifrons* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plagiotremus phenax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plectorhinchus schotaf* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
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
| *Siganus stellatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
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
| *Systomus endecanalis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
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
