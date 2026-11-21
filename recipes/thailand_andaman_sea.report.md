# Bericht: Thailand & Andamanensee (`recipes/thailand_andaman_sea.json`)

Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.

- Referenz-DB: v3 (FishBase v26.06, SeaLifeBase v26.06)
- Salz/Süß: FishBase/SeaLifeBase v25.04 (species.parquet)
- iNaturalist: 1013 Taxa (Seiten: 3)
- OBIS: 1933 Arten mit Nachweisen außer iNaturalist
- Bild: https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Thailand_-_Sea_Turtle_diving_-_Similan_Islands_%2816964389292%29.jpg/330px-Thailand_-_Sea_Turtle_diving_-_Similan_Islands_%2816964389292%29.jpg — Reinhard Link, CC BY-SA 2.0, https://commons.wikimedia.org/wiki/File:Thailand_-_Sea_Turtle_diving_-_Similan_Islands_(16964389292).jpg

## Gebiete

- iNaturalist: Ranong, TH (13253), Phangnga, TH (13249), Phuket, TH (12075), Krabi, TH (13325), Trang, TH (13261), Satun, TH (12096), Tanintharyi, MM (13122), Andaman and Nicobar, IN (13065)
- OBIS: Andamanensee ohne Golf von Thailand
- FishBase/SeaLifeBase-Verbreitung: 764, 104, 356:IN-AN

## Übersicht

- Arten der Reihenfolge-Quelle, aufgelöst: 997; nicht aufgelöst: 10
- ausgeschlossen: 535
  - zu wenige Nachweise: 421
  - kein Meeresfisch: 110
  - von Hand ausgeschlossen: 2
  - zu klein: 1
  - nur tiefer als die Tauchgrenze: 1
- Kandidaten nach den Filtern: 462
- Deck: 156 Arten (Level 1: 46, Level 2: 60, Level 3: 50); Umfang laut Rezept 40/60/50 plus Highlights
- Highlights: 6 im Deck, 0 verworfen

## Zu entscheiden

Hinweise, keine Ausschlüsse: Jede Zeile wird im Rezept entschieden (`exclude` mit Grund, Namenszuordnung, Level) oder bewusst belassen. Schwellen: `warnings` im Rezept.

| Art | Subdeck | Warnung | Zahlen |
|---|---|---|---|
| *Halichoeres annularis* | level-2 | Name der Region | Deck: *Halichoeres annularis*; die Referenz-DB führt die Art als *Halichoeres marginatus* |
| *Concholabrus fasciatus* | level-2 | Name der Region | Deck: *Concholabrus fasciatus*; die Referenz-DB führt die Art als *Cheilinus fasciatus* |
| *Halichoeres chrysotaenia* | level-3 | Name der Region | Deck: *Halichoeres chrysotaenia*; die Referenz-DB führt die Art als *Halichoeres vrolikii* |
| *Pteraeolidia semperi* | invertebrates | Name der Region | Deck: *Pteraeolidia semperi*; die Referenz-DB führt die Art als *Pteraeolidia ianthina* |
| *Mobula birostris* | level-1 | wenige Beobachter | 23 von 43 Beobachtungen von 2 Personen (53 %); 18 Beobachter insgesamt |
| *Hippocampus histrix* | level-1 | wenige Beobachter | 4 von 8 Beobachtungen von 2 Personen (50 %); 6 Beobachter insgesamt |
| *Terapon jarbua* | level-3 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Plectorhinchus gibbosus* | level-3 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |

## Verworfene Highlights

Keine.

## iNaturalist-Namen zugeordnet

Laut `recipes/inat_names.json`: iNaturalist nennt die Art anders als die Referenz-DB; die Zählung kommt zu der der Referenz-DB-Art.

| iNaturalist | Referenz-DB | iNat | Art | Beleg |
|---|---|---|---|---|
| *Eviotops sebreei* | *Eviota sebreei* | 19 | Umbenennung | https://www.inaturalist.org/taxon_changes/178922 |
| *Pinnoctopus aspilosomatis* | *Callistoctopus aspilosomatis* | 4 | Umbenennung | https://www.inaturalist.org/taxon_changes/172611 |

## Von Hand ausgeschlossen

| Art | iNat | Grund |
|---|---|---|
| *Boleophthalmus boddarti* | 121 | Schlammspringer, lebt auf dem Schlickwatt der Mangroven außerhalb des Wassers. |
| *Zenarchopterus buffonis* | 63 | Halbschnabelhecht der Mangrovenkanäle und Flussmündungen, keine Begegnung am Riff. |

## Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Rhincodon typus* | Der Walhai besucht von Februar bis April Richelieu Rock und Koh Tachai. | 266 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Mobula birostris* | Riesenmantas ziehen an Koh Bon und Hin Daeng vorbei, den Manta-Plätzen der Region. | 133 | Reihenfolge-Quelle, OBIS | Level 1 |
| *Stegostoma tigrinum* | Der Zebrahai liegt tagsüber auf dem Sand vor Koh Lanta und den Phi-Phi-Inseln. | 125 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Hippocampus histrix* | Das Dornen-Seepferdchen ist eine der Makro-Attraktionen von Richelieu Rock. | 370 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Solenostomus paradoxus* | Der Harlekin-Geisterpfeifenfisch versteckt sich in Haarsternen und Gorgonien der Similan-Inseln. | 117 | Reihenfolge-Quelle, OBIS | Level 1 |
| *Dugong dugon* | Vor Trang und Ko Libong weidet die größte Dugong-Gruppe Thailands in den Seegraswiesen. | – | Verbreitung | Level 1 |

## Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS ohne iNaturalist oder Verbreitung): 154/156 (99 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 0
- Arten ohne Volksnamen `de` in der Referenz-DB: 75/156 (48 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 1/156 (1 %)
- Familien ohne Volksnamen `de`: 6/43 (14 %): *Cheloniidae*, *Dugongidae*, *Epinephelidae*, *Mobulidae*, *Octopodidae*, *Sepiidae*
- Familien ohne Volksnamen `en`: 0/43 (0 %)

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

- *Dugong dugon*: Verbreitung
- *Dascyllus abudafur*: Reihenfolge-Quelle

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

- gleicher Volksname `de` „Schnapper“: *Lutjanus decussatus*, *Lutjanus lutjanus*, *Lutjanus quinquelineatus*, *Lutjanus fulviflamma*

## Deck

Spalten: Rang unter den Kandidaten, Zählung der Reihenfolge-Quelle (iNat), OBIS-Nachweise ohne den iNaturalist-Datensatz, Einträge der FishBase/SeaLifeBase-Verbreitung in den Rezept-Regionen (~~durchgestrichen~~: Eintrag sagt „nicht vorhanden“), Wasser laut FishBase/SeaLifeBase.

### Level 1 (46)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 1 | *Zanclus cornutus* (259 Beobachter) | 482 | 24 | native ×2 | Meer |
| 2 | *Amphiprion ocellaris* (243 Beobachter) | 416 | 26 | native ×3 | Meer |
| 3 | *Abudefduf vaigiensis* (268 Beobachter) | 412 | 23 | native ×1 | Meer |
| 4 | *Thalassoma lunare* (147 Beobachter) | 368 | 84 | native ×2 | Meer |
| 5 | *Halichoeres hortulanus* (134 Beobachter) | 301 | 51 | native ×1 | Meer |
| 6 | *Arothron nigropunctatus* (160 Beobachter) | 295 | 24 | native ×1 | Meer |
| 7 | *Gymnothorax javanicus* (145 Beobachter) | 288 | 27 | native ×1 | Meer |
| 8 | *Chaetodon collare* (144 Beobachter) | 287 | 24 | native ×1 | Meer |
| 9 | *Siganus javus* (149 Beobachter) | 262 | 24 | native ×2 | Brack/Meer |
| 10 | *Chaetodon trifasciatus* (123 Beobachter) | 243 | 10 | native ×1 | Meer |
| 11 | *Scarus niger* (95 Beobachter) | 241 | 38 | native ×1 | Meer |
| 12 | *Pterois miles* (135 Beobachter) | 223 | 5 | native ×1 | Meer |
| 13 | *Balistoides viridescens* (142 Beobachter) | 222 | 8 | native ×2 | Meer |
| 14 | *Acanthurus lineatus* (127 Beobachter) | 214 | 16 | native ×1 | Meer |
| 15 | *Diodon hystrix* (136 Beobachter) | 205 | 4 | native ×1, questionable ×1 | Meer |
| 16 | *Scarus quoyi* (103 Beobachter) | 203 | 7 | – | Meer |
| 17 | *Acanthurus leucosternon* (123 Beobachter) | 201 | 24 | native ×2 | Meer |
| 18 | *Lutjanus decussatus* (116 Beobachter) | 198 | 24 | native ×2 | Meer |
| 19 | *Scarus rubroviolaceus* (103 Beobachter) | 193 | 8 | native ×1 | Meer |
| 20 | *Amphiprion akallopisos* (117 Beobachter) | 186 | 25 | native ×2 | Meer |
| 21 | *Siganus guttatus* (107 Beobachter) | 184 | 15 | native ×1 | Brack/Meer |
| 22 | *Dischistodus perspicillatus* (90 Beobachter) | 181 | 15 | native ×2 | Brack/Meer |
| 23 | *Amphiprion clarkii* (106 Beobachter) | 171 | 12 | native ×1 | Meer |
| 24 | *Cephalopholis miniata* (87 Beobachter) | 168 | 38 | native ×1, questionable ×1 | Meer |
| 25 | *Dascyllus trimaculatus* (96 Beobachter) | 167 | 35 | native ×2 | Meer |
| 26 | *Chaetodon triangulum* (89 Beobachter) | 163 | 49 | native ×1 | Meer |
| 27 | *Scarus prasiognathos* (86 Beobachter) | 158 | 10 | native ×1 | Meer |
| 28 | *Chlorurus sordidus* (64 Beobachter) | 151 | 17 | – | Brack/Meer |
| 29 | *Hemigymnus melapterus* (81 Beobachter) | 149 | 15 | native ×1 | Meer |
| 30 | *Labroides dimidiatus* (81 Beobachter) | 143 | 65 | native ×1 | Meer |
| 31 | *Cephalopholis formosa* (80 Beobachter) | 140 | 30 | native ×1 | Meer |
| 32 | *Pomacentrus moluccensis* (77 Beobachter) | 138 | 44 | native ×2 | Meer |
| 33 | *Chaetodon octofasciatus* (77 Beobachter) | 136 | 16 | native ×1 | Meer |
| 34 | *Chaetodon decussatus* (75 Beobachter) | 135 | 4 | native ×2 | Meer |
| 35 | *Carcharhinus melanopterus* (111 Beobachter) | 125 | 11 | native ×2 | Brack/Meer |
| 36 | *Chaetodon andamanensis* (74 Beobachter) | 122 | 5 | native ×3 | Meer |
| 37 | *Heniochus singularius* (78 Beobachter) | 116 | 11 | native ×1 | Meer |
| 38 | *Scolopsis bilineata* (73 Beobachter) | 116 | 61 | native ×2 | Meer |
| 39 | *Diodon liturosus* (86 Beobachter) | 114 | 7 | – | Meer |
| 40 | *Lutjanus biguttatus* (68 Beobachter) | 113 | 14 | native ×2 | Meer |
| 266 | *Rhincodon typus* (Highlight; 14 Beobachter) | 16 | 45 | native ×2 | Meer |
| 133 | *Mobula birostris* (Highlight; 18 Beobachter) | 43 | 3 | – | Meer |
| 125 | *Stegostoma tigrinum* (Highlight; 34 Beobachter) | 47 | 1 | native ×2 | Brack/Meer |
| 370 | *Hippocampus histrix* (Highlight; 6 Beobachter) | 8 | 4 | native ×1 | Meer |
| 117 | *Solenostomus paradoxus* (Highlight; 32 Beobachter) | 51 | 4 | – | Meer |
| – | *Dugong dugon* (Highlight) | – | – | native ×2 | Meer |

### Level 2 (60)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 41 | *Cephalopholis argus* (71 Beobachter) | 111 | 29 | native ×2 | Meer |
| 42 | *Ostracion cubicum* (75 Beobachter) | 111 | 23 | native ×2 | Meer |
| 43 | *Balistapus undulatus* (76 Beobachter) | 108 | 19 | native ×2 | Meer |
| 44 | *Halichoeres scapularis* (53 Beobachter) | 108 | 22 | native ×1 | Meer |
| 45 | *Chaetodon vagabundus* (65 Beobachter) | 107 | 7 | native ×2 | Meer |
| 46 | *Eretmochelys imbricata* (83 Beobachter) | 104 | 8 | native ×2 | Brack/Meer |
| 47 | *Fistularia commersonii* (69 Beobachter) | 104 | 8 | – | Meer |
| 48 | *Chelonia mydas* (83 Beobachter) | 103 | 9 | native ×2 | Meer |
| 49 | *Pomacanthus imperator* (66 Beobachter) | 100 | 9 | native ×1 | Meer |
| 50 | *Dascyllus carneus* (59 Beobachter) | 99 | 22 | – | Meer |
| 51 | *Neotrygon malaccensis* (66 Beobachter) | 96 | – | native ×1 | Meer |
| 52 | *Scolopsis margaritifera* (42 Beobachter) | 95 | 7 | native ×1 | Meer |
| 53 | *Caranx melampygus* (56 Beobachter) | 94 | 9 | native ×2 | Brack/Meer |
| 54 | *Istiblennius dussumieri* (62 Beobachter) | 94 | 29 | native ×2 | Brack/Meer |
| 55 | *Ecsenius bicolor* (46 Beobachter) | 93 | 76 | native ×2 | Meer |
| 56 | *Halichoeres annularis* (35 Beobachter) | 92 | 39 | native ×1 | Meer |
| 57 | *Hippocampus comes* (51 Beobachter) | 92 | – | native ×1 | Meer |
| 58 | *Istigobius ornatus* (63 Beobachter) | 92 | 18 | native ×2 | Brack/Meer |
| 59 | *Acanthosepion pharaonis* (71 Beobachter) | 91 | – | native ×2 | Meer |
| 60 | *Tylosurus crocodilus* (67 Beobachter) | 90 | 9 | native ×2 | Meer |
| 61 | *Abudefduf bengalensis* (49 Beobachter) | 89 | 6 | native ×1 | Meer |
| 62 | *Concholabrus fasciatus* (56 Beobachter) | 89 | 17 | native ×2 | Meer |
| 63 | *Gymnothorax thyrsoideus* (69 Beobachter) | 86 | 24 | native ×1 | Meer |
| 64 | *Plectorhinchus vittatus* (59 Beobachter) | 86 | 7 | native ×1 | Meer |
| 65 | *Chrysiptera unimaculata* (39 Beobachter) | 84 | 13 | native ×1 | Meer |
| 66 | *Ostracion meleagris* (62 Beobachter) | 84 | 9 | native ×1 | Meer |
| 67 | *Epibulus insidiator* (42 Beobachter) | 83 | 45 | native ×1 | Meer |
| 68 | *Epinephelus quoyanus* (51 Beobachter) | 83 | 8 | native ×1 | Meer |
| 69 | *Arothron stellatus* (67 Beobachter) | 82 | 8 | native ×1 | Brack/Meer |
| 70 | *Dendrochirus zebra* (54 Beobachter) | 81 | 29 | native ×1 | Meer |
| 71 | *Upeneus tragula* (56 Beobachter) | 81 | 16 | native ×2 | Brack/Meer |
| 72 | *Platax teira* (61 Beobachter) | 80 | 11 | native ×1 | Meer |
| 73 | *Heniochus acuminatus* (56 Beobachter) | 79 | 21 | native ×2 | Brack/Meer |
| 74 | *Naso elegans* (47 Beobachter) | 79 | – | native ×2 | Meer |
| 75 | *Chelmon rostratus* (53 Beobachter) | 77 | 2 | native ×1 | Brack/Meer |
| 76 | *Cheilinus chlorourus* (36 Beobachter) | 74 | 23 | native ×2 | Meer |
| 77 | *Scolopsis lineata* (44 Beobachter) | 74 | 5 | native ×1 | Meer |
| 78 | *Abudefduf sordidus* (47 Beobachter) | 72 | 14 | native ×1 | Brack/Meer |
| 79 | *Acanthurus xanthopterus* (50 Beobachter) | 72 | 12 | native ×1 | Meer |
| 80 | *Chaetodon lineolatus* (48 Beobachter) | 72 | 7 | native ×1 | Meer |
| 81 | *Gymnothorax favagineus* (52 Beobachter) | 72 | 15 | native ×2 | Brack/Meer |
| 82 | *Scolopsis ciliata* (41 Beobachter) | 72 | 23 | native ×2 | Brack/Meer |
| 83 | *Amblyglyphidodon aureus* (45 Beobachter) | 71 | 13 | native ×1 | Meer |
| 84 | *Scarus ghobban* (48 Beobachter) | 71 | 13 | native ×1 | Brack/Meer |
| 85 | *Amphiprion ephippium* (45 Beobachter) | 70 | 20 | native ×3 | Meer |
| 86 | *Chaetodon rafflesii* (41 Beobachter) | 70 | 4 | native ×1 | Brack/Meer |
| 87 | *Melichthys indicus* (53 Beobachter) | 70 | 6 | native ×2 | Meer |
| 88 | *Parapercis hexophtalma* (44 Beobachter) | 70 | 40 | native ×1 | Meer |
| 89 | *Kyphosus cinerascens* (42 Beobachter) | 68 | 6 | native ×1 | Meer |
| 90 | *Chlorurus troschelii* (36 Beobachter) | 67 | 5 | native ×2 | Meer |
| 91 | *Chaetodon auriga* (49 Beobachter) | 66 | 13 | native ×1 | Meer |
| 92 | *Chaetodon lunula* (50 Beobachter) | 66 | 5 | native ×1 | Meer |
| 93 | *Halichoeres chloropterus* (30 Beobachter) | 66 | 3 | native ×2 | Meer |
| 94 | *Pomacentrus pavo* (39 Beobachter) | 66 | 30 | native ×1 | Meer |
| 95 | *Sufflamen chrysopterum* (36 Beobachter) | 64 | 4 | native ×1 | Meer |
| 96 | *Heniochus pleurotaenia* (47 Beobachter) | 63 | 7 | native ×2 | Meer |
| 97 | *Parupeneus macronemus* (40 Beobachter) | 63 | 18 | native ×2 | Meer |
| 98 | *Pomacanthus annularis* (55 Beobachter) | 63 | 14 | native ×1 | Meer |
| 99 | *Salarias fasciatus* (32 Beobachter) | 62 | 11 | native ×1 | Brack/Meer |
| 100 | *Echidna nebulosa* (56 Beobachter) | 61 | 10 | native ×2 | Meer |

### Level 3 (50)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 101 | *Parupeneus barberinus* | 61 | 22 | native ×2 | Meer |
| 102 | *Ctenochaetus striatus* | 60 | 11 | – | Meer |
| 103 | *Octopus cyanea* | 60 | 4 | native ×2 | Meer |
| 104 | *Siganus virgatus* | 59 | 12 | native ×1 | Brack/Meer |
| 105 | *Aluterus scriptus* | 58 | 6 | – | Meer |
| 106 | *Terapon jarbua* | 57 | 8 | native ×2 | Süß/Brack/Meer |
| 107 | *Gomphosus caeruleus* | 56 | 14 | native ×2 | Meer |
| 108 | *Halichoeres argus* | 56 | 16 | native ×2 | Meer |
| 109 | *Canthigaster petersii* | 55 | 1 | native ×2 | Meer |
| 110 | *Pteropterus antennatus* | 55 | 24 | – | Meer |
| 111 | *Siganus corallinus* | 55 | 4 | native ×1 | Meer |
| 112 | *Caesio xanthonota* | 53 | 9 | native ×2 | Meer |
| 113 | *Lutjanus lutjanus* | 53 | 43 | native ×2 | Meer |
| 114 | *Epinephelus coeruleopunctatus* | 52 | 24 | native ×2 | Meer |
| 115 | *Lutjanus quinquelineatus* | 52 | 28 | native ×2 | Meer |
| 116 | *Cirrhitichthys oxycephalus* | 51 | 14 | – | Meer |
| 118 | *Halichoeres chrysotaenia* | 50 | 36 | native ×1 | Meer |
| 119 | *Plectorhinchus gibbosus* | 50 | 13 | native ×1 | Süß/Brack/Meer |
| 120 | *Abudefduf notatus* | 48 | 8 | native ×1 | Meer |
| 121 | *Acanthurus triostegus* | 48 | 8 | native ×1 | Meer |
| 122 | *Chaetodon trifascialis* | 48 | 9 | native ×1 | Meer |
| 123 | *Lutjanus fulviflamma* | 48 | 13 | native ×2 | Brack/Meer |
| 124 | *Valenciennea sexguttata* | 48 | 40 | native ×2 | Meer |
| 126 | *Platax orbicularis* | 46 | – | native ×2 | Brack/Meer |
| 127 | *Arothron mappa* | 45 | 4 | questionable ×1 | Meer |
| 128 | *Chaetodon falcula* | 45 | 4 | native ×1 | Meer |
| 129 | *Bodianus neilli* | 44 | 10 | native ×3 | Meer |
| 130 | *Thalassoma jansenii* | 44 | 7 | native ×1 | Meer |
| 131 | *Anyperodon leucogrammicus* | 43 | 23 | native ×1 | Meer |
| 132 | *Cephalopholis boenak* | 43 | 62 | native ×2 | Meer |
| 134 | *Scolopsis monogramma* | 43 | 20 | native ×1 | Meer |
| 135 | *Aulostomus chinensis* | 42 | 10 | native ×1 | Meer |
| 136 | *Cephalopholis polyspila* | 42 | 53 | native ×1 | Meer |
| 137 | *Coris batuensis* | 42 | 13 | – | Meer |
| 138 | *Odonus niger* | 42 | 16 | native ×1 | Meer |
| 139 | *Plectorhinchus chaetodonoides* | 42 | 8 | native ×1 | Brack/Meer |
| 140 | *Scolopsis vosmeri* | 42 | 20 | native ×2 | Meer |
| 141 | *Siganus magnificus* | 42 | 11 | native ×2 | Meer |
| 142 | *Bodianus mesothorax* | 41 | 13 | native ×2 | Meer |
| 143 | *Dascyllus abudafur* | 41 | – | – | Meer |
| 144 | *Balistoides conspicillum* | 40 | 2 | – | Brack/Meer |
| 145 | *Helcogramma striata* | 40 | 35 | native ×2 | Meer |
| 146 | *Abudefduf septemfasciatus* | 39 | 4 | native ×2 | Meer |
| 147 | *Acanthurus nigricauda* | 39 | 6 | – | Brack/Meer |
| 148 | *Chlorurus strongylocephalus* | 39 | 2 | – | Meer |
| 149 | *Monotaxis grandoculis* | 39 | 4 | native ×2 | Meer |
| 150 | *Naso unicornis* | 39 | 1 | – | Meer |
| 151 | *Pomacentrus chrysurus* | 39 | 30 | native ×1 | Meer |
| 152 | *Centropyge eibli* | 38 | 26 | native ×1 | Meer |
| 153 | *Gymnothorax fimbriatus* | 38 | 16 | native ×2 | Brack/Meer |

## Grenzfälle

Je 10 Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels sie nehmen (Highlights ab Level 2 übersprungen).

### Level 1/2

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 31 | *Cephalopholis formosa* (80 Beobachter) | 140 | 30 | native ×1 | Meer | 1 |
| 32 | *Pomacentrus moluccensis* (77 Beobachter) | 138 | 44 | native ×2 | Meer | 1 |
| 33 | *Chaetodon octofasciatus* (77 Beobachter) | 136 | 16 | native ×1 | Meer | 1 |
| 34 | *Chaetodon decussatus* (75 Beobachter) | 135 | 4 | native ×2 | Meer | 1 |
| 35 | *Carcharhinus melanopterus* (111 Beobachter) | 125 | 11 | native ×2 | Brack/Meer | 1 |
| 36 | *Chaetodon andamanensis* (74 Beobachter) | 122 | 5 | native ×3 | Meer | 1 |
| 37 | *Heniochus singularius* (78 Beobachter) | 116 | 11 | native ×1 | Meer | 1 |
| 38 | *Scolopsis bilineata* (73 Beobachter) | 116 | 61 | native ×2 | Meer | 1 |
| 39 | *Diodon liturosus* (86 Beobachter) | 114 | 7 | – | Meer | 1 |
| 40 | *Lutjanus biguttatus* (68 Beobachter) | 113 | 14 | native ×2 | Meer | 1 |
| | **Grenze** | | | | | |
| 41 | *Cephalopholis argus* (71 Beobachter) | 111 | 29 | native ×2 | Meer | 2 |
| 42 | *Ostracion cubicum* (75 Beobachter) | 111 | 23 | native ×2 | Meer | 2 |
| 43 | *Balistapus undulatus* (76 Beobachter) | 108 | 19 | native ×2 | Meer | 2 |
| 44 | *Halichoeres scapularis* (53 Beobachter) | 108 | 22 | native ×1 | Meer | 2 |
| 45 | *Chaetodon vagabundus* (65 Beobachter) | 107 | 7 | native ×2 | Meer | 2 |
| 46 | *Eretmochelys imbricata* (83 Beobachter) | 104 | 8 | native ×2 | Brack/Meer | 2 |
| 47 | *Fistularia commersonii* (69 Beobachter) | 104 | 8 | – | Meer | 2 |
| 48 | *Chelonia mydas* (83 Beobachter) | 103 | 9 | native ×2 | Meer | 2 |
| 49 | *Pomacanthus imperator* (66 Beobachter) | 100 | 9 | native ×1 | Meer | 2 |
| 50 | *Dascyllus carneus* (59 Beobachter) | 99 | 22 | – | Meer | 2 |

### Level 2/3

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 91 | *Chaetodon auriga* (49 Beobachter) | 66 | 13 | native ×1 | Meer | 2 |
| 92 | *Chaetodon lunula* (50 Beobachter) | 66 | 5 | native ×1 | Meer | 2 |
| 93 | *Halichoeres chloropterus* (30 Beobachter) | 66 | 3 | native ×2 | Meer | 2 |
| 94 | *Pomacentrus pavo* (39 Beobachter) | 66 | 30 | native ×1 | Meer | 2 |
| 95 | *Sufflamen chrysopterum* (36 Beobachter) | 64 | 4 | native ×1 | Meer | 2 |
| 96 | *Heniochus pleurotaenia* (47 Beobachter) | 63 | 7 | native ×2 | Meer | 2 |
| 97 | *Parupeneus macronemus* (40 Beobachter) | 63 | 18 | native ×2 | Meer | 2 |
| 98 | *Pomacanthus annularis* (55 Beobachter) | 63 | 14 | native ×1 | Meer | 2 |
| 99 | *Salarias fasciatus* (32 Beobachter) | 62 | 11 | native ×1 | Brack/Meer | 2 |
| 100 | *Echidna nebulosa* (56 Beobachter) | 61 | 10 | native ×2 | Meer | 2 |
| | **Grenze** | | | | | |
| 101 | *Parupeneus barberinus* | 61 | 22 | native ×2 | Meer | 3 |
| 102 | *Ctenochaetus striatus* | 60 | 11 | – | Meer | 3 |
| 103 | *Octopus cyanea* | 60 | 4 | native ×2 | Meer | 3 |
| 104 | *Siganus virgatus* | 59 | 12 | native ×1 | Brack/Meer | 3 |
| 105 | *Aluterus scriptus* | 58 | 6 | – | Meer | 3 |
| 106 | *Terapon jarbua* | 57 | 8 | native ×2 | Süß/Brack/Meer | 3 |
| 107 | *Gomphosus caeruleus* | 56 | 14 | native ×2 | Meer | 3 |
| 108 | *Halichoeres argus* | 56 | 16 | native ×2 | Meer | 3 |
| 109 | *Canthigaster petersii* | 55 | 1 | native ×2 | Meer | 3 |
| 110 | *Pteropterus antennatus* | 55 | 24 | – | Meer | 3 |

### Level 3/nicht im Deck

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 144 | *Balistoides conspicillum* | 40 | 2 | – | Brack/Meer | 3 |
| 145 | *Helcogramma striata* | 40 | 35 | native ×2 | Meer | 3 |
| 146 | *Abudefduf septemfasciatus* | 39 | 4 | native ×2 | Meer | 3 |
| 147 | *Acanthurus nigricauda* | 39 | 6 | – | Brack/Meer | 3 |
| 148 | *Chlorurus strongylocephalus* | 39 | 2 | – | Meer | 3 |
| 149 | *Monotaxis grandoculis* | 39 | 4 | native ×2 | Meer | 3 |
| 150 | *Naso unicornis* | 39 | 1 | – | Meer | 3 |
| 151 | *Pomacentrus chrysurus* | 39 | 30 | native ×1 | Meer | 3 |
| 152 | *Centropyge eibli* | 38 | 26 | native ×1 | Meer | 3 |
| 153 | *Gymnothorax fimbriatus* | 38 | 16 | native ×2 | Brack/Meer | 3 |
| | **Grenze** | | | | | |
| 154 | *Hemitaurichthys zoster* | 38 | 4 | native ×1 | Meer | – |
| 155 | *Lutjanus monostigma* | 38 | 5 | native ×2 | Brack/Meer | – |
| 156 | *Pygoplites diacanthus* | 38 | 4 | native ×1 | Meer | – |
| 157 | *Stethojulis trilineata* | 38 | 15 | native ×1 | Meer | – |
| 158 | *Aethaloperca rogaa* | 37 | 17 | native ×1 | Meer | – |
| 159 | *Synodus variegatus* | 37 | 77 | questionable ×1 | Meer | – |
| 160 | *Epinephelus erythrurus* | 36 | 13 | native ×1 | Brack/Meer | – |
| 161 | *Neopomacentrus sororius* | 36 | – | native ×1 | Meer | – |
| 162 | *Pomacentrus andamanensis* | 36 | – | native ×2 | Meer | – |
| 163 | *Pomacentrus umbratilus* | 36 | – | native ×2 | Meer | – |

## Abgleich mit Führern

Das Rezept nennt keinen Führer.
## Änderungen gegenüber dem bestehenden Deck

- neu: 4: *Concholabrus fasciatus*, *Halichoeres annularis*, *Halichoeres chrysotaenia*, *Pteraeolidia semperi*
- entfallen: 4: *Cheilinus fasciatus*, *Halichoeres marginatus*, *Halichoeres vrolikii*, *Pteraeolidia ianthina*

## Ausgeschlossene Kandidaten

<details><summary>535 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Boleophthalmus boddarti* | 121 | Süß/Brack/Meer | von Hand ausgeschlossen (Schlammspringer, lebt auf dem Schlickwatt der Mangroven außerhalb des Wassers.) |
| *Striuntius lateristriga* | 72 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Zenarchopterus buffonis* | 63 | Brack/Meer | von Hand ausgeschlossen (Halbschnabelhecht der Mangrovenkanäle und Flussmündungen, keine Begegnung am Riff.) |
| *Toxotes jaculatrix* | 61 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neolissochilus soroides* | 23 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Channa limbata* | 22 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Channa striata* | 21 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oryzias javanicus* | 21 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Dichotomyctere nigroviridis* | 19 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eviota sebreei* | 19 | Meer | zu klein (höchstens 2.5 cm) |
| *Poecilia reticulata* | 19 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Aplocheilus panchax* | 18 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Channa lucius* | 18 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Toxotes chatareus* | 18 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Devario regina* | 17 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora paviana* | 16 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Periophthalmodon septemradiatus* | 15 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Danio kerri* | 14 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Schistura robertsi* | 14 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Microdevario kubotai* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Schistura udomritthiruji* | 11 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oreochromis niloticus* | 10 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudogobiopsis oligactis* | 10 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta imbellis* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oreochromis mossambicus* | 9 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paracanthocobitis phuketensis* | 9 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Periophthalmus walailakae* | 9 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Batasio fluviatilis* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Stiphodon ornatus* | 8 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Badis siamensis* | 7 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mugilogobius tigrinus* | 7 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Spirula spirula* | 7 | Meer | nur tiefer als die Tauchgrenze (erst ab 100 m) |
| *Barbonymus gonionotus* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinus rubrofuscus* | 6 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Dermogenys siamensis* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hampala siamensis* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Opsarius bernatziki* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Osphronemus goramy* | 6 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Xenentodon canciloides* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Barbonymus schwanefeldii* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Betta simplex* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hampala macrolepidota* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trichopodus trichopterus* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acanthurus maculiceps* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Acanthurus thompsoni* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Acentronura breviperula* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Andamia heteroptera* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Antennarius maculatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Atherinomorus lacunosus* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Bothus pantherinus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Callistoctopus aspilosomatis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Carcharhinus leucas* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Chaetodon oxycephalus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Chromis opercularis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cirripectes filamentosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Coris cuvieri* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cryptocentrus caeruleomaculatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cryptocentrus leucostictus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ctenogobiops pomastictus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Drepane punctata* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Epinephelus lanceolatus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Epinephelus malabaricus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Epinephelus sexfasciatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Eviota maculosa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Eviota teresae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gazza rhombea* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Halichoeres nebulosus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Herklotsichthys quadrimaculatus* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Himantura leoparda* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hippocampus trimaculatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Leptojulis cyanopleura* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lethrinus microdon* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Maculabatis gerrardi* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Megalops cyprinoides* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Mulloidichthys flavolineatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Muraenesox bagio* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Nandus nebulosus* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nectamia savayensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Neopomacentrus anabatoides* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ophichthus altipennis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ophiocara cantoris* | 4 | ? | zu wenige Nachweise (4 < 5) |
| *Osteochilus vittatus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ostorhinchus cyanosoma* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Parupeneus heptacantha* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Periophthalmus novemradiatus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Platax boersii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Plectorhinchus albovittatus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Plesiops corallicola* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pomacentrus nagasakiensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Poropuntius genyognathus* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pycnochromis flavipectoralis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Rastrelliger kanagurta* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Rhinecanthus aculeatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sargocentron cornutum* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Scarus rivulatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scolopsis curite* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scyris indica* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Selar boops* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sillago sihama* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Stigmatogobius sadanundio* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trachinotus blochii* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Trimma striatum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Amphioctopus aegina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Antennarius commerson* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ascarosepion latimanus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Asterropteryx semipunctata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Atelomycterus marmoratus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Barbodes rhombeus* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bathygobius fuscus* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Chaetodon ephippium × xanthocephalus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chaetodon madagaskariensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cheilodipterus artus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Choerodon anchorago* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chromileptes altivelis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cirrhilabrus exquisitus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cirripectes auritus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cryptocentrus maudae* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Ctenochaetus binotatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ctenogobiops feroculus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dischistodus prosopotaenia* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Epinephelus areolatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Epinephelus flavocaeruleus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Eurypegasus draconis* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Glyptothorax prashadi* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Glyptothorax schmidti* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gymnothorax pseudothyrsoideus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gymnothorax rueppelliae* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Gymnura poecilura* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hemiramphus far* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Himantura undulata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Leiodon cutcutia* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Leptobarbus rubripinna* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lobotes surinamensis* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Lutjanus bengalensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Macolor macularis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Nemanthias ignitus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Neochirus brachyptera* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Neoniphon sammara* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Neopomacentrus bankieri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Otolithes ruber* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Oxycheilinus bimaculatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pandaka rouxi* | 3 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parapercis xanthozona* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Petroscirtes mitratus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pinjalo lewisi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Plagiotremus phenax* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pomacentrus adelus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pomacentrus azuremaculatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Priacanthus blochii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pseudocheilinus hexataenia* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Puntigrus partipentazona* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora caudimaculata* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rasbora trilineata* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Scartelaos histophorus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Scarus viridifucatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Scolopsis aurata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Selaroides leptolepis* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Sphyraena flavicauda* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sphyrna lewini* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Stegastes punctatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Taenianotus triacanthus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Taeniura lymma* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Thalassoma quinquevittatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Thaumoctopus mimicus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Trichopsis vittata* | 3 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma ukkriti* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Valenciennea puellaris* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Abalistes stellatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Abdopus aculeatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Alectis ciliaris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Alepes djedaba* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Alopias pelagicus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ambassis nalua* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Ambassis urotaenia* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Ambassis vachellii* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Amblyglyphidodon curacao* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Amblygobius nocturnus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anabas testudineus* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Aphareus furca* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Arothron meleagris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Atropus armatus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Atropus mentalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bathygobius cocosensis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Brachaluteres taylori* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bryaninops yongei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Caesio teres* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cantherhines dumerilii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Canthidermis maculata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Carcharhinus sorrah* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Cephalopholis nigripinnis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cephalopholis sonnerati* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chaetodon interruptus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Channa harcourtbutleri* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Chiloscyllium griseum* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Chiloscyllium hasseltii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chlorurus bleekeri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chlorurus rhakoura* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Clarias batrachus* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Clarias gariepinus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ctenogobiops aurocingulus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ctenogobiops crocineus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cyclocheilichthys apogon* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Dactylopus kuiteri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ecsenius paroculus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ecsenius polystictus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ephippus orbis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epinephelus longispinis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Esomus metallicus* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Eubleekeria splendens* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Euthynnus affinis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Favonigobius reichei* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Fibramia thermalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fusigobius melacron* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gazza minuta* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Gerres filamentosus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Gobiodon rivulatus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Gomphosus varius* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnothorax isingteena* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Halichoeres bicolor* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hippocampus kelloggi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Hipposcarus harid* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Homalopteroides modestus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Homalopteroides tweediei* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Idiosepius pygmaeus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Inimicus didactylus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Lactoria fornasini* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Laiphognathus multimaculatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Leiognathus equula* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Leptomelanosoma indicum* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Lutjanus ehrenbergii* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Lutjanus johnii* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Macropharyngodon meleagris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mastacembelus favus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mirolabrichthys evansi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mobula tarapacana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mobula thurstoni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Monopterus javanensis* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Moolgarda crenilabis* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Myripristis adusta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Naso tonganus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nebrius ferrugineus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nemateleotris decora* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nemipterus hexodon* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Neolissochilus hendersoni* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neolissochilus stracheyi* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ostorhinchus moluccensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ostorhinchus nigrofasciatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pao leiurus* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parapercis snyderi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Parapriacanthus ransonneti* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Parascorpaena aurita* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Parascorpaena picta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Platax batavianus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plectorhinchus ceylonensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plectropomus laevis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plectropomus leopardus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pleurosicya mossambica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plotosus canius* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Pomadasys kaakan* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Psettodes erumei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudochromis andamanensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pterocaesio randalli* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pteropterus mombasae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rastrelliger faughni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rhina ancylostomus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rhinobatos ranongensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rhinoptera jayakari* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sargocentron spiniferum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scarus psittacus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Schistura mahnerti* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Scomberoides tol* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Scorpaenopsis venosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Selar crumenophthalmus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sepiella inermis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sillago asiatica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sillago ingenuua* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sphyraena putnamae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sphyrna mokarran* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Synodus dermatogenys* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Taeniamia macroptera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tetrosomus gibbosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Thryssa setirostris* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Thysanoteuthis rhombus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Triacanthus biaculeatus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Upeneus vittatus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Urogymnus granulatus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Verulux cypselurus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Xiphophorus maculatus* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Zenarchopterus gilli* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Abantennarius nummifer* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ablennes hians* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Acanthopagrus berda* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Acanthurus blochii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acanthurus nigrofuscus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acantopsis rungthipae* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Acentrogobius viridipunctatus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Acreichthys tomentosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aluterus monoceros* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amblyeleotris guttata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amphiprion sandaracinos* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anampses melanurus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Antennarius pictus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Arcygobius baliurus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Asterropteryx ensifera* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Asterropteryx striata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Atropus hedlandensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aurigequula longispinis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Balitoropsis zollingeri* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Barbodes binotatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Barbonymus altus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Blenniella chrysospilos* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Boleophthalmus dussumieri* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Boleophthalmus pectinirostris* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Bothus lunatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Botia udomritthiruji* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Bryaninops natans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Butis butis* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Butis koilomatodon* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Callechelys marmorata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Canthigaster valentini* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carangichthys oblongus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Caranx papuensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Carcharhinus amboinensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Carcharhinus brevipinna* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Centropyge flavipectoralis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaetodon bennetti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaetodon citrinellus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaetodon gardineri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaetodontoplus mesoleucus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Channa pyrophthalmus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cheilodipterus alleni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheilopogon dorsomacula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chilomycterus reticulatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chlorurus microrhinos* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Choerodon robustus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cirrhinus mrigala* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cirrhitichthys aprinus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Clarias macrocephalus* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Coris aygula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coris gaimard* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Craterognathus plagiotaenia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cryptocentrus cyanotaenia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cypselurus oligolepis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dermogenys collettei* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Dipterygonotus balteatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Discotrema crinophilum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Doboatherina duodecimalis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Dunckerocampus dactyliophorus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echidna polyzona* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Enchelycore schismatorhynchus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Entomacrodus caudofasciatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Entomacrodus thalassinus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus bleekeri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus macrospilos* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Equulites leuciscus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Escualosa thoracata* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Etelis carbunculus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eubleekeria rapsoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eugnathogobius mas* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Euprymna berryi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Exyrias belissimus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fibramia lateralis* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Filimanus similis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fusigobius neophytus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fusigobius signipinnis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Galeocerdo cuvier* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Giuris viator* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Glyptothorax fuscus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gobiopterus chuno* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gymnocaesio gymnoptera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnocranius grandoculis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax griseus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax margaritophorus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax phasmatodes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax reticularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax shaoi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax undulatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres cosmetus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres kallochroma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres pardaleocephalus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres zeylonicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hampala salweenensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hapalochlaena nierstraszi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Helcogramma lacuna* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hemigobius mingi* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Hemipristis elongata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Heteromycteris oculus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Heteropneustes kemratensis* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Homalopteroides smithi* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Hyporhamphus dussumieri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hyporthodus octofasciatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Iniistius bimaculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Katsuwonus pelamis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Kuhlia rupestris* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Labeo catla* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lactarius lactarius* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Lepidocephalichthys hasselti* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Leptobarbus hoevenii* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Lethrinus crocineus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lethrinus obsoletus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lipocheilus carnolabrum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lutjanus carponotatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lutjanus lunulatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lutjanus malabaricus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Lutjanus rufolineatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lutjanus russellii* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Macrognathus circumcinctus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrognathus maculatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macropharyngodon ornatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Maculabatis pastinacoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mahidolia mystacina* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Mastacembelus armatus* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mastacembelus tinwini* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mene maculata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Micrognathus andersonii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Monacanthus chinensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Moolgarda seheli* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Mugilogobius mertoni* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Mugilogobius rambaiae* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Mustelus andamanensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Myripristis berndti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Myripristis botche* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nannosalarias nativitatis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Narcine prodorsalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Narcine timlei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nectamia luxuria* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nemacheilus masyae* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nemacheilus ornatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Nemipterus bipunctatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nemipterus furcosus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Omobranchus elongatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Ompok siluroides* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ophiocara porocephalum* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Opistognathus cyanospilotus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Opistognathus wassi* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Orbiraja powelli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Orectolobus leptolineatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oreichthys parvus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oryzias dancena* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oryzias minutillus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Ostorhinchus angustatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ostorhinchus apogonoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ostorhinchus aureus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ostorhinchus chrysotaenia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxycirrhites typus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxyeleotris marmorata* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pangasianodon hypophthalmus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paracaesio sordida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paracanthocobitis nigrolineata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Paragaleus longicaudatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parambassis apogonoides* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Parapercis lineopunctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pastinachus ater* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pateobatis fai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pempheris adusta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pempheris oualensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Petroscirtes variabilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Piaractus brachypomus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pinjalo pinjalo* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Platycephalus indicus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Plectorhinchus flavomaculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plectorhinchus lessonii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plectroglyphidodon obreptus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pleurosicya labiata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Polynemus paradiseus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pomacentrus philippinus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomacentrus proteus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomadasys andamanensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Poropuntius deauratus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Priacanthus tayenus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pristicon trimaculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Protonibea diacanthus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Psammogobius biocellatus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pseudobagarius leucorhynchus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudochromis fuscus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudochromis tapeinosoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudogobius fulvicaudus* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pseudogobius poicilosoma* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pseudorhombus triocellatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ptereleotris hanae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pterocaesio marri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pterocaesio tessellata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pterocaesio trilineata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ranzania laevis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhabdamia spilota* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhinopias frondosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sardinella gibbosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sargocentron diadema* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scarus oviceps* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scarus schlegeli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Schistura aurantiaca* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Scomberoides tala* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scomberomorus guttatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Scorpaenopsis cirrosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scorpaenopsis possi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scuticaria tigrina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Seriolina nigrofasciata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Sicyopus rubicundus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Siganus punctatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Siganus spinus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sillaginopodys chondropus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Silurichthys schneideri* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Spratelloides delicatulus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stigmatogobius pleurostigma* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Stonogobiops nematodes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Strongylura leiurus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Symphorus nematophorus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synanceia horrida* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Synchiropus stellatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Syngnathoides biaculeatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synodus binotatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synodus rubromarmoratus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Takifugu oblongus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Telatrygon biasa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Temera hardwickii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thalassoma amblycephalum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thryssa malabarica* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Thunnus alalunga* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trachinotus botla* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Trichiurus lepturus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Trigonostigma espei* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Trimma flammeum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trimma naudei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trimma winterbottomi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trimmatom eviotops* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tuberoschistura baenzigeri* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Turrum gymnostethus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ucla xenogrammus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Upeneus moluccensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Uraspis uraspis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Urogymnus asperrimus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Uropterygius marmoratus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Valenciennea randalli* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Variola albimarginata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Wattsia mossambica* | 1 | Meer | zu wenige Nachweise (1 < 5) |

</details>

## Subdeck `invertebrates` (40)

Eigene Taxa, Größe und Filter, Reihenfolge-Quelle und Region des Rezepts. Arten, die schon in einem Level oder einem früheren Subdeck stehen, bleiben draußen; die Führer werden nicht abgeglichen.

- iNaturalist: 1251 Taxa (Seiten: 3)
- OBIS: 5719 Arten mit Nachweisen außer iNaturalist

### iNaturalist-Namen zugeordnet

Laut `recipes/inat_names.json`: iNaturalist nennt die Art anders als die Referenz-DB; die Zählung kommt zu der der Referenz-DB-Art.

| iNaturalist | Referenz-DB | iNat | Art | Beleg |
|---|---|---|---|---|
| *Pinnoctopus aspilosomatis* | *Callistoctopus aspilosomatis* | 4 | Umbenennung | https://www.inaturalist.org/taxon_changes/172611 |

### Von Hand ausgeschlossen

| Art | iNat | Grund |
|---|---|---|
| *Coenobita rugosus* | 858 | Landeinsiedlerkrebs, lebt an Land und geht nur zur Eiablage ans Meer. |
| *Coenobita violascens* | 383 | Landeinsiedlerkrebs, lebt an Land und geht nur zur Eiablage ans Meer. |
| *Grapsus albolineatus* | 368 | Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen. |
| *Coenobita brevimanus* | 135 | Landeinsiedlerkrebs, lebt an Land und geht nur zur Eiablage ans Meer. |
| *Acanthopleura gemmata* | 92 | Käferschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Dotilla myctiroides* | 82 | Soldatenkrabbe, lebt bei Ebbe auf den Sandflächen am Strand. |
| *Eriphia sebana* | 72 | Felsenkrabbe der Gezeitenzone, sitzt bei Ebbe in Felsspalten über dem Wasser. |
| *Gecarcoidea humei* | 66 | Landkrabbe, lebt an Land und geht nur zum Laichen ans Meer. |
| *Lepas anserifera* | 65 | Entenmuschel auf Treibgut im offenen Meer, fast nur angespült am Strand beobachtet. |
| *Nerita costata* | 65 | Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Matuta victor* | 61 | Mondkrabbe, gräbt sich in der Brandung des Sandstrands ein. |
| *Nerita chamaeleon* | 57 | Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Episesarma versicolor* | 53 | Mangrovenkrabbe, lebt im Wurzelwerk und Schlick über dem Wasser. |
| *Cardisoma carnifex* | 44 | Landkrabbe, lebt an Land und geht nur zum Laichen ans Meer. |
| *Portunus sanguinolentus* | 39 | Schwimmkrabbe der Lagunen und Flussmündungen, vor allem als Fang auf Märkten beobachtet. |
| *Hecuba scortum* | 31 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 5 von 5 Beobachtungen mit Angabe „tot“). |

### Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Odontodactylus scyllarus* | Der Pfauenfangschreckenkrebs schlägt mit seinen Keulen so schnell zu, dass Wasser verdampft; Taucher suchen ihn gezielt. | 47 | Reihenfolge-Quelle, Verbreitung | invertebrates |
| *Hymenocera picta* | Die Harlekingarnele frisst nur Seesterne und ist einer der begehrtesten Funde für Unterwasserfotografen. | 152 | Reihenfolge-Quelle, OBIS | invertebrates |

### Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS ohne iNaturalist oder Verbreitung): 37/40 (92 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 0
- Arten ohne Volksnamen `de` in der Referenz-DB: 25/40 (62 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 2/40 (5 %)
- Familien ohne Volksnamen `de`: 27/27 (100 %): *Acanthasteridae*, *Archasteridae*, *Cardiidae*, *Chromodorididae*, *Diadematidae*, *Diogenidae*, *Echinometridae*, *Facelinidae*, *Faviidae*, *Gonodactylidae*, *Holothuriidae*, *Oculinidae*, *Odontodactylidae*, *Ophidiasteridae*, *Ophiocomidae*, *Oreasteridae*, *Palaemonidae*, *Palinuridae*, *Pectinidae*, *Petrosiidae*, *Phyllidiidae*, *Plakobranchidae*, *Plerogyridae*, *Porcellanidae*, *Porpitidae*, *Stenopodidae*, *Stichopodidae*
- Familien ohne Volksnamen `en`: 16/27 (59 %): *Archasteridae*, *Chromodorididae*, *Diadematidae*, *Echinometridae*, *Facelinidae*, *Faviidae*, *Oculinidae*, *Ophidiasteridae*, *Ophiocomidae*, *Oreasteridae*, *Petrosiidae*, *Phyllidiidae*, *Plakobranchidae*, *Plerogyridae*, *Porpitidae*, *Stichopodidae*

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

- *Stenopus hispidus*: Reihenfolge-Quelle
- *Porpita porpita*: Reihenfolge-Quelle
- *Neopetrolisthes maculatus*: Reihenfolge-Quelle

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

- gleicher Volksname `de` „Nacktschnecke“: *Pteraeolidia semperi*, *Phyllidia elegans*

### Arten

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Klasse |
|---|---|---|---|---|---|---|
| 1 | *Tridacna crocea* | 313 | 12 | native ×2 | Meer | Bivalvia |
| 2 | *Acanthaster planci* | 213 | 32 | native ×1 | Meer | Asteroidea |
| 3 | *Diadema setosum* | 213 | 8 | – | Meer | Echinoidea |
| 4 | *Linckia laevigata* | 213 | 53 | – | Meer | Asteroidea |
| 5 | *Pteraeolidia semperi* | 161 | 26 | – | Meer | Gastropoda |
| 6 | *Phyllidia varicosa* | 157 | 38 | native ×1 | Meer | Gastropoda |
| 7 | *Holothuria atra* | 154 | 2 | native ×2 | Meer | Holothuroidea |
| 8 | *Holothuria leucospilota* | 151 | 11 | native ×2 | Meer | Holothuroidea |
| 9 | *Echinothrix calamaris* | 148 | 12 | – | Meer | Echinoidea |
| 10 | *Pearsonothuria graeffei* | 140 | 1 | native ×2 | Meer | Holothuroidea |
| 11 | *Culcita schmideliana* | 125 | 13 | – | Meer | Asteroidea |
| 12 | *Xestospongia testudinaria* | 121 | 6 | native ×1 | Meer | Demospongiae |
| 13 | *Panulirus versicolor* | 114 | 1 | native ×2 | Meer | Malacostraca |
| 14 | *Tridacna maxima* | 113 | 17 | native ×3 | Brack/Meer | Bivalvia |
| 15 | *Archaster typicus* | 108 | 20 | native ×1 | Meer | Asteroidea |
| 16 | *Plakobranchus ocellatus* | 104 | 5 | native ×1 | Meer | Gastropoda |
| 17 | *Tridacna squamosa* | 90 | 10 | native ×2 | Meer | Bivalvia |
| 18 | *Stichopus chloronotus* | 85 | 5 | native ×2 | Meer | Holothuroidea |
| 19 | *Hypselodoris pulchella* | 81 | 42 | native ×1 | Meer | Gastropoda |
| 20 | *Diploastrea heliopora* | 73 | 16 | – | Meer | Hexacorallia |
| 21 | *Actinopyga mauritiana* | 65 | 4 | native ×2 | Meer | Holothuroidea |
| 22 | *Ophiocoma scolopendrina* | 63 | 11 | – | Meer | Ophiuroidea |
| 23 | *Pedum spondyloideum* | 59 | 5 | – | Meer | Bivalvia |
| 24 | *Phyllidiella nigra* | 59 | 15 | native ×1 | Meer | Gastropoda |
| 25 | *Plerogyra sinuosa* | 58 | 10 | native ×2 | Meer | Hexacorallia |
| 26 | *Stenopus hispidus* | 58 | – | – | Meer | Malacostraca |
| 27 | *Galaxea fascicularis* | 57 | 14 | native ×1 | Meer | Hexacorallia |
| 28 | *Phyllidiella zeylanica* | 54 | 46 | native ×1 | Meer | Gastropoda |
| 29 | *Goniobranchus annulatus* | 53 | 28 | – | Meer | Gastropoda |
| 30 | *Protoreaster nodosus* | 53 | 6 | native ×1 | Meer | Asteroidea |
| 31 | *Dardanus megistos* | 52 | 1 | native ×2 | Meer | Malacostraca |
| 32 | *Echinometra mathaei* | 52 | 7 | – | Meer | Echinoidea |
| 33 | *Porpita porpita* | 52 | – | – | Meer | Hydrozoa |
| 34 | *Neopetrolisthes maculatus* | 50 | – | – | Meer | Malacostraca |
| 35 | *Phyllidia elegans* | 50 | 20 | – | Meer | Gastropoda |
| 36 | *Phyllidia coelestis* | 49 | 13 | – | Meer | Gastropoda |
| 37 | *Goniobranchus geminus* | 47 | 33 | – | Meer | Gastropoda |
| 38 | *Gonodactylus chiragra* | 44 | 1 | native ×1 | Meer | Malacostraca |
| 47 | *Odontodactylus scyllarus* (Highlight; 33 Beobachter) | 39 | – | native ×1 | Meer | Malacostraca |
| 152 | *Hymenocera picta* (Highlight; 11 Beobachter) | 13 | 4 | – | Meer | Malacostraca |

### Grenzfälle

Je 10 Arten vor und nach der Grenze (Highlights übersprungen).

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Klasse | Im Subdeck |
|---|---|---|---|---|---|---|---|
| 29 | *Goniobranchus annulatus* | 53 | 28 | – | Meer | Gastropoda | ja |
| 30 | *Protoreaster nodosus* | 53 | 6 | native ×1 | Meer | Asteroidea | ja |
| 31 | *Dardanus megistos* | 52 | 1 | native ×2 | Meer | Malacostraca | ja |
| 32 | *Echinometra mathaei* | 52 | 7 | – | Meer | Echinoidea | ja |
| 33 | *Porpita porpita* | 52 | – | – | Meer | Hydrozoa | ja |
| 34 | *Neopetrolisthes maculatus* | 50 | – | – | Meer | Malacostraca | ja |
| 35 | *Phyllidia elegans* | 50 | 20 | – | Meer | Gastropoda | ja |
| 36 | *Phyllidia coelestis* | 49 | 13 | – | Meer | Gastropoda | ja |
| 37 | *Goniobranchus geminus* | 47 | 33 | – | Meer | Gastropoda | ja |
| 38 | *Gonodactylus chiragra* | 44 | 1 | native ×1 | Meer | Malacostraca | ja |
| | **Grenze** | | | | | | |
| 39 | *Rhynchocinetes durbanensis* | 44 | 4 | – | Meer | ? | nein |
| 40 | *Tonna dolium* | 44 | 7 | native ×2 | Meer | ? | nein |
| 41 | *Dardanus lagopodes* | 43 | – | native ×1 | Meer | ? | nein |
| 42 | *Synapta maculata* | 42 | 1 | – | Meer | ? | nein |
| 43 | *Phyllidia ocellata* | 41 | 47 | native ×1 | Meer | ? | nein |
| 44 | *Thelenota ananas* | 41 | 1 | native ×2 | Meer | ? | nein |
| 45 | *Stylissa massa* | 40 | 5 | native ×1 | Meer | ? | nein |
| 46 | *Mauritia arabica* | 39 | 31 | native ×2 | Meer | ? | nein |
| 48 | *Tubastraea micranthus* | 39 | 13 | – | Meer | ? | nein |
| 49 | *Versuriga anadyomene* | 38 | 1 | native ×1 | Meer | ? | nein |

### Ausgeschlossene Kandidaten

<details><summary>628 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Coenobita rugosus* | 858 | Meer | von Hand ausgeschlossen (Landeinsiedlerkrebs, lebt an Land und geht nur zur Eiablage ans Meer.) |
| *Coenobita violascens* | 383 | Meer | von Hand ausgeschlossen (Landeinsiedlerkrebs, lebt an Land und geht nur zur Eiablage ans Meer.) |
| *Grapsus albolineatus* | 368 | Meer | von Hand ausgeschlossen (Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen.) |
| *Coenobita brevimanus* | 135 | Süß/Meer | von Hand ausgeschlossen (Landeinsiedlerkrebs, lebt an Land und geht nur zur Eiablage ans Meer.) |
| *Acanthopleura gemmata* | 92 | Meer | von Hand ausgeschlossen (Käferschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Acanthosepion pharaonis* | 91 | Meer | schon in einem anderen Subdeck (level-2) |
| *Dotilla myctiroides* | 82 | Brack/Meer | von Hand ausgeschlossen (Soldatenkrabbe, lebt bei Ebbe auf den Sandflächen am Strand.) |
| *Eriphia sebana* | 72 | Meer | von Hand ausgeschlossen (Felsenkrabbe der Gezeitenzone, sitzt bei Ebbe in Felsspalten über dem Wasser.) |
| *Gecarcoidea humei* | 66 | Meer | von Hand ausgeschlossen (Landkrabbe, lebt an Land und geht nur zum Laichen ans Meer.) |
| *Lepas anserifera* | 65 | Meer | von Hand ausgeschlossen (Entenmuschel auf Treibgut im offenen Meer, fast nur angespült am Strand beobachtet.) |
| *Nerita costata* | 65 | Meer | von Hand ausgeschlossen (Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Matuta victor* | 61 | Meer | von Hand ausgeschlossen (Mondkrabbe, gräbt sich in der Brandung des Sandstrands ein.) |
| *Octopus cyanea* | 60 | Meer | schon in einem anderen Subdeck (level-3) |
| *Nerita chamaeleon* | 57 | Brack/Meer | von Hand ausgeschlossen (Schnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Episesarma versicolor* | 53 | Meer | von Hand ausgeschlossen (Mangrovenkrabbe, lebt im Wurzelwerk und Schlick über dem Wasser.) |
| *Cardisoma carnifex* | 44 | Meer | von Hand ausgeschlossen (Landkrabbe, lebt an Land und geht nur zum Laichen ans Meer.) |
| *Portunus sanguinolentus* | 39 | Brack/Meer | von Hand ausgeschlossen (Schwimmkrabbe der Lagunen und Flussmündungen, vor allem als Fang auf Märkten beobachtet.) |
| *Hecuba scortum* | 31 | Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 5 von 5 Beobachtungen mit Angabe „tot“).) |
| *Jacksonaster depressum* | 27 | Meer | nur tiefer als die Tauchgrenze (erst ab 50 m) |
| *Spirula spirula* | 7 | Meer | nur tiefer als die Tauchgrenze (erst ab 100 m) |
| *Acropora gemmifera* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Actinopyga caerulea* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Aplysia nigrocincta* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Astropecten indicus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Bohadschia koellikeri* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Boloceroides mcmurrichi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Callistoctopus aspilosomatis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ceratosoma gracillimum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Chicoreus capucinus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Chicoreus torrefactus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Clibanarius padavensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Conus achatinus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ctenactis crassa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Dactylospongia metachromia* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Dardanus crassimanus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Dichotella gemmacea* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Diversidoris flava* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Elysia pusilla* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Etisus splendidus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Etisus utilis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Faunus ater* | 4 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Favorinus tsuruganus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Goniastrea minuta* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Goniobranchus alius* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hyotissa hyotis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hypselodoris bullockii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hypselodoris iacula* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hypselodoris whitei* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Iciligorgia rubra* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lamellodysidea herbacea* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Leptoseris mycetoseroides* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ligia dentipes* | 4 | ? | zu wenige Nachweise (4 < 5) |
| *Lopha cristagalli* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lydia annulipes* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Montipora hispida* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ocypode cordimana* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ophiolepis superba* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Oxymeris maculata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Panulirus ornatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Panulirus polyphagus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Pavona duerdeni* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Philinopsis speciosa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Phyllidia polkadotsa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Phyllorhiza punctata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Physalia utriculus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Physella acuta* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Plocamopherus tilesii* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Poraster superbus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pseudosquilla ciliata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Saron marmoratus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sculpsitechinus auritus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Scylla serrata* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Selatium brockii* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Spheciospongia inconstans* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Stichopus pseudohorrens* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Dolomena marginata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Talparia talpa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Turbo petholatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Turricula javana* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Varuna litterata* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Verconia simplex* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Volegalea cochlidium* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Aclyvolva lanceolata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Acropora clathrata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Acropora longicyathus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Acrosterigma maculosum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Actinodendron alcyonoideum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Amphioctopus aegina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Anthopleura anjunae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ascarosepion latimanus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Brissus latecarinatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bulbaeolidia alba* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Bulla ampulla* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Calcinus elegans* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Callyspongia diffusa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Canarium urceus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Phyllospongia foliascens* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cassis cornuta* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Charybdis natator* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chthamalus malayensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Clibanarius cruentatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Clibanarius demani* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Colobometra perspinosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus coronatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus distans* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus zonatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Coscinaraea crassa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cuapetes tenuipes* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cymo quadrilobatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dasycaris zanzibarica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dendrodoris tuberculosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Dolabrifera dolabrifera* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Doridomorpha gardineri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ellobium aurisjudae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Engina zonalis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Eriphia scabricula* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Euphyllia glabrescens* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Glossodoris pallida* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gonioinfradens paucidentatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Goniopora albiconus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hypselodoris emma* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hypselodoris krakatoa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Laevistrombus canarium* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Littoraria scabra* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Lobophyllia radians* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lunulicardia retusa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Macrorhynchia philippina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Marivagia stellata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Melibe viridis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Merulina scabricula* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Metaplax elegans* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Metopograpsus thukuhar* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Monetaria annulus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mycale grandis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Nemanthus nitidus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Neosarmatium smithi* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Neripteron violaceum* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Ophiomastix elegans* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ophiothela mirabilis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ophiothrix purpurea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Oulophyllia crispa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paragoniastrea russelli* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paramontastraea salebrosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Paratapes undulatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pennaria disticha* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Phyllidiopsis krempfi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Maoricardium pseudolatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pontiometra andersoni* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Protoreaster lincki* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Psammocora haimiana* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pythia trigona* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Quadrella boopsis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rhabdastrella globostellata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sabellastarte spectabilis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sagaminopteron nigropunctatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Stelletta clavosa* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Stichodactyla mertensii* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Thalamitoides quadridens* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Thalassina anomala* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Thaumoctopus mimicus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Toxopneustes pileolus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Trapezia rufopunctata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tubastraea violacea* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tubulophilinopsis gardineri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Vepricardium coronatum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Vexillum plicarium* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Abdopus aculeatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acanthella cavernosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acromitus flagellatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora aspera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora cytherea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora digitifera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora florida* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora grandis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora humilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora latistella* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora muricata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora rudis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acropora valida* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Actaeodes tomentosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Actinodendron arboreum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Actinopyga echinites* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Allogalathea elegans* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Alpheus lottini* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Amphibalanus reticulatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Amphinome rostrata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Exaiptasia diaphana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anthenea regalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anthopleura handi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Asteropsis carinifera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Astraeosmilia maxima* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Astreopora myriophthalma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Atagema intecta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Atys semistriatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bathytormus radiatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bernardpora stutchburyi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Biuve fulvipunctata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Calcinus morgani* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Calpurnus verrucosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Carupa tenuipes* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cephea cephea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ceratosoma tenue* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cerberilla ambonensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cerithidea obtusa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cerithium coralium* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Charybdis affinis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chelidonura pallida* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chelonaplysilla violacea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Circe scripta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Clibanarius arethusa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Coecella horsfieldii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conomurex decorus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus araneosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus bandanus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus bengalensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus betulinus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus collisus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus virgo* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Corculum cardissa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Coryphellina flamma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ctenoides ales* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Culcita novaeguineae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cyanea buitendijki* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cyerce elegans* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cymbiola nobilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cynarina lacrymalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dardanus guttatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dendrodoris carbunculosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dendrodoris fumata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dictyodendrilla pallasi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dipsastraea rosaria* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Latona faba* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Duplicaria duplicata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Echinophyllia aspera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Echinopora pacificus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Euxanthus exsculptus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Favites rotundata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gafrarium dispar* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Geloina expansa* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Gloripallium pallium* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Goniobranchus albopunctatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Goniobranchus hintuanensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Goniobranchus sinensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Goniodiscaster scaber* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnodoris impudica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gyrineum natator* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Haliclona baeri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Haliotis asinina* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Harpiosquilla raphidea* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Heliofungia actiniformis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Holothuria fuscogilva* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Idiosepius pygmaeus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Janolus flavoanulatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Julia exquisita* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lambis truncata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Leptoseris hawaiiensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Leucosia craniolaris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lithophyllon undulatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Littoraria undulata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lobactis scutaria* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lobophyllia corymbosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lobophyllia hemprichii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lunella cinerea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Malleus albus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Matuta planipes* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Menippe rumphii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Merulina cylindrica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mexichromis mariei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nassarius globosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nassarius pullus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nerita planospira* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Niphates aga* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Notobryon wardi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ocypode brevicornis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ophiarachna incrassata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Paguritta harmsi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Palaemonella philippinensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Panulirus penicillatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pavona frondifera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pavona venosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Percnon guinotae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Phyllognathia ceratophthalma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pinufius rebus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plagusia squamosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Platydoris cinereobranchiata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Platydoris scabra* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pocillopora acuta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Podophthalmus vigil* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Monomia gladiator* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Psammocora profundacella* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudosuccinea columella* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Rhinolambrus pelagicus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rhopilema hispidum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sabellastarte magnifica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scylla paramamosain* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Selatium elongatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sepiella inermis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sinularia brassica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Siphonaria laciniosa* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Stellamedusa ventana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Stephanometra indica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Stichopus ocellatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tarebia granifera* | 2 | Süß/Meer | zu wenige Nachweise (2 < 5) |
| *Tetralia glaberrima* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Thysanoteuthis rhombus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tozeuma lanceolatum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trapezia tigrina* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tridacna noae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tripedalia cystophora* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tritoniopsis elegans* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trochus maculatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Turbo argyrostomus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Turbo bruneus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Turbo intercostalis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Urocaridella pulchella* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vasticardium pectiniforme* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vasum turbinellus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Xanthias lamarckii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Xenocarcinus depressus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Xenocarcinus tuberculatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Zenopontonia rex* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acanthostrongylophora ingens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acromitus maculosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora globiceps* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora hyacinthus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora kosurini* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora millepora* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora monticulosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora papillare* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora plumosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora robusta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora samoensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora sarmentosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acropora tenuis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alitropus typus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Allogalathea babai* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alveopora gigas* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anadara crebricostata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ancylomenes magnificus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Angaria delphinus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anthemiphyllia dentata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Anthopleura nigrescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Antigona lamellaris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aplysia argus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Arca navicularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Arcuatula senhousia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Armina papillata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Astreopora expansa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Atergatopsis signata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Atys naucum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aulacolambrus hoplonotus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Babylonia areolata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Beguina semiorbiculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Birgus latro* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Bistolida ursellus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bohadschia maculisparsa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bohadschia marmorata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Botryllus schlosseri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Brissus agassizii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bursatella leachii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calcarovula gracillima* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calcarovula longirostrata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calliactis polypus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Carpilius convexus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cerberilla asamusiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cerithium nodulosum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Charybdis orientalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chlorodiella nigra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chromodoris lineolata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chrysostoma paradoxum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clavelina robusta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cloridopsis scorpio* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clypeomorus petrosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Colochirus quadrangularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Comaster nobilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conchoderma hunteri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conchoderma virgatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus ammiralis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus chaldaeus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus leopardus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus nussatella* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus radiatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus rattus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus sanguinolentus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus sponsalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coralliocaris graminea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Coriocella nigra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Costasiella fridae* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Costasiella kuroshimae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Crambionella orsini* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cratena lineata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cribrarula cribraria* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cryptospira fischeri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cycloachelous granulatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cymo melanodactylus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cymothoa pulchrum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lyncina carneola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dactylospongia elegans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Daldorfia horrida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Danafungia horrida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dardanus gemmatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dendrodoris arborescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dentiovula dorsuosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dentiovula eizoi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dermatobranchus fortunatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diadumene lineata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diminovula alabaster* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diniatys dentifer* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diogenes pallescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diogenes planimanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dipsastraea lizardensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Doclea armata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Doriopsis pecten* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dotilla wichmanni* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Drupella margariticola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echinopora horrida* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echinostrephus aciculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Eirene hexanemalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ellisella ceratophyta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ellobium aurismidae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epigrapsus politus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epixanthus dentatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Erugosquilla woodmasoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Euphyllia cristata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Euprymna berryi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Euryspongia coerulea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Euselenops luniceps* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Excirolana orientalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Favites colemani* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Favites vasta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ficus ficus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fistulobalanus albicostatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gastrolepidia clavigera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Geograpsus grayi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Glossodoris acosti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gnathophyllum americanum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Goniobranchus bombayanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Goniobranchus collingwoodi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Goniobranchus verrieri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Goniopora djiboutiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gonodactylus platysoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gonodactylus smithii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnangium hians* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnodoris nigricolor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halgerda punctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Haliotis ovina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hallaxa fuscescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hapalochlaena nierstraszi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Harpa articularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hastula cinerea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hastula hectica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hemilienardia malleti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hippa marmorata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria lineata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria pardalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria pervicax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria verrucosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hydatina physis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hypselodoris maridadilus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hyrtios erectus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ilyoplax delsmani* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Ixa cylindrus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Junceella juncea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Marcia japonica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lambis scorpius* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lamprohaminoea ovalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lentigo pipus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lepas anatifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leptoseris gardineri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Limaria fragilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lioconcha ornata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Liomera cinctimanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Liosina paradoxa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lissocarcinus laevis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Littoraria intermedia* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Littoraria melanostoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lobophyllia valenciennesii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lophozozymus pictor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lovenia elongata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lytocarpia brevirostris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Macrobrachium lanchesteri* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrobrachium lar* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrobrachium rosenbergii* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Macrophthalmus convexus* | 1 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Macrorhynchia phoenicea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mactra violacea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Magallana belcheri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Magallana gigas* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Mancinella armigera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Megabalanus tintinnabulum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Megalactis hemprichi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Melanoides tuberculata* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Menathais tuberosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mesactinia ganensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Metalia sternalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mexichromis macropus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mexichromis multituberculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Miamira miamirana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Micippa platipes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Micromussa amakusensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Millepora tenera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mithrodia clavigera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Strigatella retusa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Miyakella nepa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Modiolus philippinarum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Monoplex pilearis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Montipora aequituberculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Montipora cactus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Montipora crassituberculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Montipora spumosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Murex ternispina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Murphydoris maracabranchia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mycedium elephantotus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mycedium robokaki* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Myra fugax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mytilopsis sallei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nassarius albescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nassarius margaritifer* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Naticarius onca* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neoferdina offreti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nerita undata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neritopsis radula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Netrostoma coerulescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Netrostoma setouchianum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ocypode macrocera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oliva elegans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oliva mustelina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oliva sericea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oliva todosina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Opalia australis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiomastix caryophyllata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oxypora lacera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ozius tuberculosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pagurixus rubrovittatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paracondylactis hertwigi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paracondylactis sinensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parasesarma pictum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pavona bipartita* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pavona cactus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pavona clavus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pectinia lactuca* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pelocoetes exul* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Penaeus setiferus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Manipontonia psamathe* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Periglypta puerpera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Periglypta reticulata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Petrolisthes boscii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Petrolisthes haswelli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phallusia arabica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phanerophthalmus olivaceus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllidia exquisita* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllidiopsis cardinalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllidiopsis shireenae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllodesmium opalescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pinctada fucata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pinctada maculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pinna saccata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pirenella incisa* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Placuna placenta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pleurobranchus forskalii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plocamopherus ceylonicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plococidaris verticillata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plumularia spiralis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mammilla simiae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pollia undosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Geloina coaxans* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pomacea canaliculata* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pontonides unciger* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Porites deformis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Porites evermanni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Prionovolva brevis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudobiceros flowersi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pteria peasei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pteria penguin* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Purpuradusta gracilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pustularia cicercula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Quidnipagus palatam* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ranina ranina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhopalaea macrothorax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rumphella aggregata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Saccostrea echinata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sanderia malayensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Saron neglectus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scopimera inflata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scutarcopagia scobinata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Semicassis bisulcata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Smaragdia pulcherrima* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Smaragdia souverbiana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Solen vagina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Spheciospongia peleia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Staphylaea staphylaea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stegopontonia commensalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stichopus naso* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Strigatella pica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Canarium labiatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stylocoeniella armata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sunetta effossa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Symplegma brakenhielmi* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Synaptula lamperti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Syphonota geographica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tambja affinis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tapes literatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tectus pyramis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Isactinia citrina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tetilla dactyloidea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tetraclita squamosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tetralia rubridactyla* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thenus unimaculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thuridilla gracilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Timoides agassizii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tmethypocoelis ceratophora* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tozeuma armatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trachyphyllia geoffroyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trapania naeva* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trapezia cymodoce* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trapezia richtersi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trochus radiatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tubastraea diaphana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tubulophilinopsis reticulata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tumidodromia dormia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Turbo chrysostomus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Turbo crassus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Turbo marmoratus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tutufa bubo* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vasticardium subrugosum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vasum ceramicum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Vepricardium asiaticum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xenocarcinus conicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |

</details>

### Nicht aufgelöste Namen

<details><summary>288 Namen</summary>

*Lissachatina fulica* (495), *Sarika siamensis* (276), *Austruca annulipes* (224), *Radianthus magnifica* (183), *Austruca bengali* (123), *Phricotelphusa limula* (81), *Gelasimus tetragonon* (65), *Tubuca rosea* (52), *Tubuca forcipata* (48), *Ancylocaris brevicarpalis* (36), *Thranita crenata* (35), *Phyllidia marindica* (33), *Perisesarma dusumieri* (29), *Halgerda stricklandi* (28), *Thranita prymna* (28), *Nerita balteata* (26), *Samla bicolor* (25), *Tuerkayana magnum* (25), *Pseudoceros concinnus* (24), *Valiguna siamensis* (24), *Sarika resplendens* (23), *Fromia nodosa* (21), *Halgerda indotessellata* (21), *Atergatis ocyroe* (20), *Demanietta renongensis* (19), *Aldisa erwinkoehleri* (18), *Parmarion martensi* (18), *Tubuca paradussumieri* (17), *Amphidromus atricallosus* (16), *Thuridilla coerulea* (16), *Leptopoma perlucidum* (14), *Amphimedon paraviridis* (13), *Metaplax crenulata* (13), *Reishia bitubercularis* (13), *Macrophthalmus pacificus* (12), *Pseudoceros meenae* (12), *Hyalimax andamanica* (11), *Scopalina rubra* (11), *Haliclona nematifera* (10), *Reticulidia suzanneae* (10), *Thuridilla moebii* (10), *Caloria militaris* (9), *Coenobita lila* (9), *Cryptoplax oculata* (9), *Goniobranchus gleniei* (9), *Haliclona acoroides* (9), *Hemiplecta salangana* (9), *Sayamia sexpunctata* (9), *Terrapotamon longitarsus* (9), *Amphimedon queenslandica* (8), *Atyopsis moluccensis* (8), *Cerberilla annulata* (8), *Edwardsianthus pudicus* (8), *Ocypode sinensis* (8), *Paratectonatica tigrina* (8), *Pseudoceros prudhoei* (8), *Tubuca coarctata* (8), *Coryphellina exoptata* (7), *Emerita emeritus* (7), *Halgerda bacalusia* (7), *Laevicaulis alte* (7), *Naria lamarckii* (7), *Phyllidia alyta* (7), *Phyllidia multituberculata* (7), *Thranita spinimana* (7), *Dotilla intermedia* (6), *Echinodiscus andamanensis* (6), *Fasciarma fasciatum* (6), *Hemiplecta retrorsa* (6), *Leptopoma taivanum* (6), *Clarkcomanthus mirabilis* (5), *Costasiella usagi* (5), *Cycloporus venetus* (5), *Neosarmatium asiaticum* (5), *Ophiomastix pictum* (5), *Siphonaria radiata* (5), *Tubuca alcocki* (5), *Amphidromus andamanicus* (4), *Caridina sumatrensis* (4), *Hexabranchus lacer* (4), *Hypselodoris zebrina* (4), *Lysiosquilla lisa* (4), *Nemalecium caeruleus* (4), *Oxynoe jordani* (4), *Pila celebensis* (4), *Salangathelphusa anophrys* (4), *Sarika kawtaoensis* (4), *Taphrenalla alba* (4), *Tenellia puti* (4), *Thranita danae* (4), *Tortulosa tortuosa* (4), *Tytthosoceros lizardensis* (4), *Armina scotti* (3), *Bradybaena similaris* (3), *Circulium vitatum* (3), *Dermatobranchus caeruleomaculatus* (3), *Dermatobranchus gonatophorus* (3), *Desmaulus extinctorium* (3), *Dolomena vittata* (3), *Elysia aowthai* (3), *Goniobranchus conchyliatus* (3), *Goniobranchus trimarginatus* (3), *Hermania orca* (3), *Laevicaulis haroldi* (3), *Lamarcka avellana* (3), *Paracondylactis singaporensis* (3), *Paraleptuca crassipes* (3), *Phricotelphusa deharvengi* (3), *Plesiastrea peroni* (3), *Pseudobiceros splendidus* (3), *Pseudoceros goslineri* (3), *Pseudoceros magangensis* (3), *Pseudoceros paralaticlavus* (3), *Pseudoceros vishnui* (3), *Samla riwo* (3), *Sesarmops indicus* (3), *Tenellia viei* (3), *Terrapotamon abbotti* (3), *Tetraclita kuroshioensis* (3), *Zenopontonia soror* (3), *Acanthosepion aculeatum* (2), *Agaronia gibbosa* (2), *Amphidromus leucoxanthus* (2), *Arakawania granulata* (2), *Austruca perplexa* (2), *Baeolidia moebii* (2), *Baptozius vinosus* (2), *Clibanarius boschmai* (2), *Cliona caesia* (2), *Cryptospira strigata* (2), *Cyerce basi* (2), *Diminovula kosugei* (2), *Doxander operosus* (2), *Elysia asbecki* (2), *Epidendrium billeeanum* (2), *Eubranchopsis virginalis* (2), *Eubranchus ocellatus* (2), *Euplexaura erecta* (2), *Favites valenciennesi* (2), *Filifusus filamentosus* (2), *Goniobranchus leopardus* (2), *Haloa aptei* (2), *Latona solida* (2), *Lissachatina immaculata* (2), *Longchaeus acus* (2), *Megaustenia siamensis* (2), *Melithaea variabilis* (2), *Mictyris thailandensis* (2), *Murex djarianensis* (2), *Palaemonella smiti* (2), *Pentaster hybridus* (2), *Phricotelphusa ranongi* (2), *Phricotelphusa sukreei* (2), *Phycocaris simulans* (2), *Platygyra* (2), *Produnga rubropunctata* (2), *Pseudoceros auranticrinis* (2), *Pseudoceros laingensis* (2), *Pseudoceros scintillatus* (2), *Rhodactis bryoides* (2), *Rhodactis inchoata* (2), *Salangathelphusa brevicarinata* (2), *Sarika bocourti* (2), *Satiella christinae* (2), *Scopimera proxima* (2), *Sheldonella lateralis* (2), *Siphopteron tigrinum* (2), *Tegillarca aequilatera* (2), *Thaksinthelphusa yongchindaratae* (2), *Thorunna horologia* (2), *Tylothais virgata* (2), *Aegires flores* (1), *Alpheus richardsoni* (1), *Alycaeus conformis* (1), *Amonovula piriei* (1), *Amphidromus areolatus* (1), *Amphimedon sulcata* (1), *Arestorides argus* (1), *Belocaulus angustipes* (1), *Berndtia purpurea* (1), *Bistolida hirundo* (1), *Cantharus tranquebaricus* (1), *Caridina macrophora* (1), *Cellana cylindrica* (1), *Chelidonura castanea* (1), *Chloeia incerta* (1), *Chloritis helferi* (1), *Chloritis wimberleyi* (1), *Clithon oualaniense* (1), *Conus nicobaricus* (1), *Conus renateae* (1), *Corymorpha tropica* (1), *Cryptosemelus tigrinus* (1), *Cubaris murina* (1), *Cyclophorus leai* (1), *Cyclophorus malayanus* (1), *Cyclotus setosus* (1), *Dendrodoris krusensternii* (1), *Diplommatina canaliculata* (1), *Dolomena turturella* (1), *Dosinia* (1), *Eclogavena interrupta* (1), *Elysia thompsoni* (1), *Enoplolambrus pransor* (1), *Ergaea walshi* (1), *Euthria aracanensis* (1), *Fromia armata* (1), *Goniosupradens obtusifrons* (1), *Gracidina gracillima* (1), *Gymnodoris feyae* (1), *Haloa constricta* (1), *Herviella albida* (1), *Hyalimax reinhardti* (1), *Hypselodoris ghardaqana* (1), *Hypselodoris juniperae* (1), *Ilyella gigas* (1), *Ilyoplax integra* (1), *Indianastra sarasini* (1), *Indoplanorbis exustus* (1), *Kabeiro rubroreticulata* (1), *Kermidaphnella pumila* (1), *Labuanium politum* (1), *Lamarcka ventricosa* (1), *Leptodius affinis* (1), *Leptopoma marginellus* (1), *Leptopoma roepstorffianum* (1), *Lysiosquilla sulcata* (1), *Lysmata rauli* (1), *Melampus* (1), *Myra hainanica* (1), *Nerita nigrita* (1), *Noumeaella rehderi* (1), *Okenia rhinorma* (1), *Oliva pacifica* (1), *Optediceros breviculum* (1), *Parasesarma ungulata* (1), *Parvioris fulvescens* (1), *Percnon sinense* (1), *Petrosia hebes* (1), *Phalium fimbria* (1), *Philyra granulosa* (1), *Phricotelphusa sirindhorn* (1), *Phyllodesmium undulatum* (1), *Phyllognathia simplex* (1), *Pillucina pisidium* (1), *Pirenella microptera* (1), *Placamen placidum* (1), *Plakortis badabaluensis* (1), *Planorbarius corneus* (1), *Platyzoanthus mussoides* (1), *Pleuropoma nicobarica* (1), *Polybranchia jannae* (1), *Primovula panthera* (1), *Prostheceraeus fuscolineatus* (1), *Pseudobiceros gloriosus* (1), *Pseudobiceros hymanae* (1), *Pseudoceros agattiensis* (1), *Pseudoceros depiliktabub* (1), *Pseudoceros monostichos* (1), *Quantula striata* (1), *Radianthus doreensis* (1), *Rhiostoma jalorense* (1), *Rhyssoplax peregrina* (1), *Ruditapes aspera* (1), *Scopalina hapalia* (1), *Sesarmops weberi* (1), *Siamthelphusa improvisa* (1), *Sinotaia quadrata* (1), *Siphonaria radians* (1), *Strigatella scutulata* (1), *Subulina octona* (1), *Tanychlamys kelantanensis* (1), *Taphrenalla corona* (1), *Taphrenalla diadema* (1), *Tenellia bughaw* (1), *Tenellia goniophaga* (1), *Tenellia nakapila* (1), *Terebra commaculata* (1), *Thalamita* (1), *Thuridilla ratna* (1), *Tomoberthella martensi* (1), *Trapania euryeia* (1), *Tubulophilinopsis lineolata* (1), *Unidentia sandramillenae* (1), *Verconia alboannulata* (1), *Verconia romeri* (1), *Vexillum woldemarii* (1), *Videna pseudosanis* (1)

</details>

## Nicht aufgelöste Namen der Reihenfolge-Quelle

Die Referenz-DB der App kennt diese Namen nicht; die App fände sie auch nicht.

| Name | iNat |
|---|---|
| *Valenciennea schlieweni* | 7 |
| *Aplocheilus armatus* | 4 |
| *Eviotops mikiae* | 3 |
| *Acanthosepion aculeatum* | 2 |
| *Paracanthocobitis epimekes* | 2 |
| *Pterygoplichthys* | 2 |
| *Doboatherina salangensis* | 1 |
| *Mystacoleucus obtusirostris* | 1 |
| *Tor* | 1 |
| *Valenciennea zaboae* | 1 |
