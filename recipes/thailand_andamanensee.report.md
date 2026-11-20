# Bericht: Thailand & Andamanensee (`recipes/thailand_andamanensee.json`)

Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.

- Referenz-DB: v3 (FishBase v26.06, SeaLifeBase v26.06)
- Salz/Süß: FishBase/SeaLifeBase v25.04 (species.parquet)
- iNaturalist: 1013 Taxa (Seiten: 3)
- OBIS: 2098 Arten
- Bild: https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Thailand_-_Sea_Turtle_diving_-_Similan_Islands_%2816964389292%29.jpg/330px-Thailand_-_Sea_Turtle_diving_-_Similan_Islands_%2816964389292%29.jpg — Reinhard Link, CC BY-SA 2.0, https://commons.wikimedia.org/wiki/File:Thailand_-_Sea_Turtle_diving_-_Similan_Islands_(16964389292).jpg

## Gebiete

- iNaturalist: Ranong, TH (13253), Phangnga, TH (13249), Phuket, TH (12075), Krabi, TH (13325), Trang, TH (13261), Satun, TH (12096), Tanintharyi, MM (13122), Andaman and Nicobar, IN (13065)
- OBIS: Andamanensee ohne Golf von Thailand
- FishBase/SeaLifeBase-Verbreitung: 764, 104, 356:IN-AN

## Übersicht

- Arten der Reihenfolge-Quelle, aufgelöst: 995; nicht aufgelöst: 12
- ausgeschlossen: 531
  - zu wenige Nachweise: 420
  - kein Meeresfisch: 110
  - nur tiefer als die Tauchgrenze: 1
- Kandidaten nach den Filtern: 464
- Deck: 156 Arten (Level 1: 46, Level 2: 60, Level 3: 50); Umfang laut Rezept 40/60/50 plus Highlights
- Highlights: 6 im Deck, 0 verworfen

## Verworfene Highlights

Keine.

## Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Rhincodon typus* | Der Walhai besucht von Februar bis April Richelieu Rock und Koh Tachai. | 268 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Mobula birostris* | Riesenmantas ziehen an Koh Bon und Hin Daeng vorbei, den Manta-Plätzen der Region. | 135 | Reihenfolge-Quelle, OBIS | Level 1 |
| *Stegostoma tigrinum* | Der Zebrahai liegt tagsüber auf dem Sand vor Koh Lanta und den Phi-Phi-Inseln. | 127 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Hippocampus histrix* | Das Dornen-Seepferdchen ist eine der Makro-Attraktionen von Richelieu Rock. | 372 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Solenostomus paradoxus* | Der Harlekin-Geisterpfeifenfisch versteckt sich in Haarsternen und Gorgonien der Similan-Inseln. | 119 | Reihenfolge-Quelle, OBIS | Level 1 |
| *Dugong dugon* | Vor Trang und Ko Libong weidet die größte Dugong-Gruppe Thailands in den Seegraswiesen. | – | Verbreitung | Level 1 |

## Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS oder Verbreitung): 155/156 (99 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 0
- Arten ohne Volksnamen `de` in der Referenz-DB: 74/156 (47 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 1/156 (1 %)
- Familien ohne Volksnamen `de`: 8/45 (18 %): *Cheloniidae*, *Dugongidae*, *Epinephelidae*, *Mobulidae*, *Octopodidae*, *Oxudercidae*, *Sepiidae*, *Zenarchopteridae*
- Familien ohne Volksnamen `en`: 0/45 (0 %)

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

- *Dugong dugon*: Verbreitung

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

- gleicher Volksname `de` „Schnapper“: *Lutjanus decussatus*, *Lutjanus lutjanus*, *Lutjanus quinquelineatus*, *Lutjanus fulviflamma*

## Deck

Spalten: Rang unter den Kandidaten, Zählung der Reihenfolge-Quelle (iNat), OBIS-Nachweise, Einträge der FishBase/SeaLifeBase-Verbreitung in den Rezept-Regionen (~~durchgestrichen~~: Eintrag sagt „nicht vorhanden“), Wasser laut FishBase/SeaLifeBase.

### Level 1 (46)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 1 | *Zanclus cornutus* | 482 | 381 | native ×2 | Meer |
| 2 | *Amphiprion ocellaris* | 416 | 345 | native ×3 | Meer |
| 3 | *Abudefduf vaigiensis* | 412 | 346 | native ×1 | Meer |
| 4 | *Thalassoma lunare* | 368 | 396 | native ×2 | Meer |
| 5 | *Halichoeres hortulanus* | 301 | 281 | native ×1 | Meer |
| 6 | *Arothron nigropunctatus* | 295 | 259 | native ×1 | Meer |
| 7 | *Gymnothorax javanicus* | 288 | 256 | native ×1 | Meer |
| 8 | *Chaetodon collare* | 287 | 253 | native ×1 | Meer |
| 9 | *Siganus javus* | 262 | 251 | native ×2 | Brack/Meer |
| 10 | *Chaetodon trifasciatus* | 243 | 196 | native ×1 | Meer |
| 11 | *Scarus niger* | 241 | 239 | native ×1 | Meer |
| 12 | *Pterois miles* | 223 | 159 | native ×1 | Meer |
| 13 | *Balistoides viridescens* | 222 | 180 | native ×2 | Meer |
| 14 | *Acanthurus lineatus* | 214 | 185 | native ×1 | Meer |
| 15 | *Diodon hystrix* | 205 | 166 | native ×1, questionable ×1 | Meer |
| 16 | *Scarus quoyi* | 203 | 167 | – | Meer |
| 17 | *Acanthurus leucosternon* | 201 | 175 | native ×2 | Meer |
| 18 | *Lutjanus decussatus* | 198 | 183 | native ×2 | Meer |
| 19 | *Scarus rubroviolaceus* | 193 | 162 | native ×1 | Meer |
| 20 | *Amphiprion akallopisos* | 186 | 173 | native ×2 | Meer |
| 21 | *Siganus guttatus* | 184 | 167 | native ×1 | Brack/Meer |
| 22 | *Dischistodus perspicillatus* | 181 | 139 | native ×2 | Brack/Meer |
| 23 | *Amphiprion clarkii* | 171 | 159 | native ×1 | Meer |
| 24 | *Cephalopholis miniata* | 168 | 177 | native ×1, questionable ×1 | Meer |
| 25 | *Dascyllus trimaculatus* | 167 | 182 | native ×2 | Meer |
| 26 | *Chaetodon triangulum* | 163 | 179 | native ×1 | Meer |
| 27 | *Scarus prasiognathos* | 158 | 134 | native ×1 | Meer |
| 28 | *Chlorurus sordidus* | 151 | 139 | – | Brack/Meer |
| 29 | *Hemigymnus melapterus* | 149 | 144 | native ×1 | Meer |
| 30 | *Labroides dimidiatus* | 143 | 181 | native ×1 | Meer |
| 31 | *Cephalopholis formosa* | 140 | 149 | native ×1 | Meer |
| 32 | *Pomacentrus moluccensis* | 138 | 147 | native ×2 | Meer |
| 33 | *Chaetodon octofasciatus* | 136 | 123 | native ×1 | Meer |
| 34 | *Chaetodon decussatus* | 135 | 109 | native ×2 | Meer |
| 35 | *Carcharhinus melanopterus* | 125 | 105 | native ×2 | Brack/Meer |
| 36 | *Chaetodon andamanensis* | 122 | 107 | native ×3 | Meer |
| 37 | *Boleophthalmus boddarti* | 121 | 118 | native ×2 | Süß/Brack/Meer |
| 38 | *Heniochus singularius* | 116 | 104 | native ×1 | Meer |
| 39 | *Scolopsis bilineata* | 116 | 154 | native ×2 | Meer |
| 40 | *Diodon liturosus* | 114 | 93 | – | Meer |
| 268 | *Rhincodon typus* (Highlight) | 16 | 62 | native ×2 | Meer |
| 135 | *Mobula birostris* (Highlight) | 43 | 32 | – | Meer |
| 127 | *Stegostoma tigrinum* (Highlight) | 47 | 40 | native ×2 | Brack/Meer |
| 372 | *Hippocampus histrix* (Highlight) | 8 | 7 | native ×1 | Meer |
| 119 | *Solenostomus paradoxus* (Highlight) | 51 | 55 | – | Meer |
| – | *Dugong dugon* (Highlight) | – | – | native ×2 | Meer |

### Level 2 (60)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 41 | *Lutjanus biguttatus* | 113 | 114 | native ×2 | Meer |
| 42 | *Cephalopholis argus* | 111 | 120 | native ×2 | Meer |
| 43 | *Ostracion cubicum* | 111 | 117 | native ×2 | Meer |
| 44 | *Balistapus undulatus* | 108 | 107 | native ×2 | Meer |
| 45 | *Halichoeres scapularis* | 108 | 107 | native ×1 | Meer |
| 46 | *Chaetodon vagabundus* | 107 | 88 | native ×2 | Meer |
| 47 | *Eretmochelys imbricata* | 104 | 83 | native ×2 | Brack/Meer |
| 48 | *Fistularia commersonii* | 104 | 101 | – | Meer |
| 49 | *Chelonia mydas* | 103 | 68 | native ×2 | Meer |
| 50 | *Pomacanthus imperator* | 100 | 94 | native ×1 | Meer |
| 51 | *Dascyllus carneus* | 99 | 89 | – | Meer |
| 52 | *Neotrygon malaccensis* | 96 | 79 | native ×1 | Meer |
| 53 | *Scolopsis margaritifera* | 95 | 90 | native ×1 | Meer |
| 54 | *Caranx melampygus* | 94 | 89 | native ×2 | Brack/Meer |
| 55 | *Istiblennius dussumieri* | 94 | 100 | native ×2 | Brack/Meer |
| 56 | *Ecsenius bicolor* | 93 | 146 | native ×2 | Meer |
| 57 | *Halichoeres marginatus* (Quelle: *Halichoeres annularis*) | 92 | 39 | native ×1 | Meer |
| 58 | *Hippocampus comes* | 92 | 70 | native ×1 | Meer |
| 59 | *Istigobius ornatus* | 92 | 90 | native ×2 | Brack/Meer |
| 60 | *Acanthosepion pharaonis* | 91 | 69 | native ×2 | Meer |
| 61 | *Tylosurus crocodilus* | 90 | 79 | native ×2 | Meer |
| 62 | *Abudefduf bengalensis* | 89 | 83 | native ×1 | Meer |
| 63 | *Cheilinus fasciatus* (Quelle: *Concholabrus fasciatus*) | 89 | 96 | native ×2 | Meer |
| 64 | *Gymnothorax thyrsoideus* | 86 | 111 | native ×1 | Meer |
| 65 | *Plectorhinchus vittatus* | 86 | 73 | native ×1 | Meer |
| 66 | *Chrysiptera unimaculata* | 84 | 84 | native ×1 | Meer |
| 67 | *Ostracion meleagris* | 84 | 73 | native ×1 | Meer |
| 68 | *Epibulus insidiator* | 83 | 113 | native ×1 | Meer |
| 69 | *Epinephelus quoyanus* | 83 | 71 | native ×1 | Meer |
| 70 | *Arothron stellatus* | 82 | 72 | native ×1 | Brack/Meer |
| 71 | *Dendrochirus zebra* | 81 | 90 | native ×1 | Meer |
| 72 | *Upeneus tragula* | 81 | 80 | native ×2 | Brack/Meer |
| 73 | *Platax teira* | 80 | 75 | native ×1 | Meer |
| 74 | *Heniochus acuminatus* | 79 | 72 | native ×2 | Brack/Meer |
| 75 | *Naso elegans* | 79 | 64 | native ×2 | Meer |
| 76 | *Chelmon rostratus* | 77 | 71 | native ×1 | Brack/Meer |
| 77 | *Cheilinus chlorourus* | 74 | 88 | native ×2 | Meer |
| 78 | *Scolopsis lineata* | 74 | 73 | native ×1 | Meer |
| 79 | *Abudefduf sordidus* | 72 | 76 | native ×1 | Brack/Meer |
| 80 | *Acanthurus xanthopterus* | 72 | 76 | native ×1 | Meer |
| 81 | *Chaetodon lineolatus* | 72 | 62 | native ×1 | Meer |
| 82 | *Gymnothorax favagineus* | 72 | 74 | native ×2 | Brack/Meer |
| 83 | *Scolopsis ciliata* | 72 | 82 | native ×2 | Brack/Meer |
| 84 | *Amblyglyphidodon aureus* | 71 | 68 | native ×1 | Meer |
| 85 | *Scarus ghobban* | 71 | 76 | native ×1 | Brack/Meer |
| 86 | *Amphiprion ephippium* | 70 | 77 | native ×3 | Meer |
| 87 | *Chaetodon rafflesii* | 70 | 57 | native ×1 | Brack/Meer |
| 88 | *Melichthys indicus* | 70 | 60 | native ×2 | Meer |
| 89 | *Parapercis hexophtalma* | 70 | 93 | native ×1 | Meer |
| 90 | *Kyphosus cinerascens* | 68 | 67 | native ×1 | Meer |
| 91 | *Chlorurus troschelii* | 67 | 63 | native ×2 | Meer |
| 92 | *Chaetodon auriga* | 66 | 60 | native ×1 | Meer |
| 93 | *Chaetodon lunula* | 66 | 50 | native ×1 | Meer |
| 94 | *Halichoeres chloropterus* | 66 | 61 | native ×2 | Meer |
| 95 | *Pomacentrus pavo* | 66 | 86 | native ×1 | Meer |
| 96 | *Sufflamen chrysopterum* | 64 | 51 | native ×1 | Meer |
| 97 | *Heniochus pleurotaenia* | 63 | 49 | native ×2 | Meer |
| 98 | *Parupeneus macronemus* | 63 | 56 | native ×2 | Meer |
| 99 | *Pomacanthus annularis* | 63 | 68 | native ×1 | Meer |
| 100 | *Zenarchopterus buffonis* | 63 | 59 | native ×1 | Brack/Meer |

### Level 3 (50)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 101 | *Salarias fasciatus* | 62 | 64 | native ×1 | Brack/Meer |
| 102 | *Echidna nebulosa* | 61 | 49 | native ×2 | Meer |
| 103 | *Parupeneus barberinus* | 61 | 72 | native ×2 | Meer |
| 104 | *Ctenochaetus striatus* | 60 | 66 | – | Meer |
| 105 | *Octopus cyanea* | 60 | 46 | native ×2 | Meer |
| 106 | *Siganus virgatus* | 59 | 66 | native ×1 | Brack/Meer |
| 107 | *Aluterus scriptus* | 58 | 47 | – | Meer |
| 108 | *Terapon jarbua* | 57 | 45 | native ×2 | Süß/Brack/Meer |
| 109 | *Gomphosus caeruleus* | 56 | 51 | native ×2 | Meer |
| 110 | *Halichoeres argus* | 56 | 64 | native ×2 | Meer |
| 111 | *Canthigaster petersii* | 55 | 45 | native ×2 | Meer |
| 112 | *Pteropterus antennatus* | 55 | 24 | – | Meer |
| 113 | *Siganus corallinus* | 55 | 49 | native ×1 | Meer |
| 114 | *Caesio xanthonota* | 53 | 53 | native ×2 | Meer |
| 115 | *Lutjanus lutjanus* | 53 | 90 | native ×2 | Meer |
| 116 | *Epinephelus coeruleopunctatus* | 52 | 67 | native ×2 | Meer |
| 117 | *Lutjanus quinquelineatus* | 52 | 72 | native ×2 | Meer |
| 118 | *Cirrhitichthys oxycephalus* | 51 | 67 | – | Meer |
| 120 | *Halichoeres vrolikii* (Quelle: *Halichoeres chrysotaenia*) | 50 | 78 | native ×1 | Meer |
| 121 | *Plectorhinchus gibbosus* | 50 | 50 | native ×1 | Süß/Brack/Meer |
| 122 | *Abudefduf notatus* | 48 | 47 | native ×1 | Meer |
| 123 | *Acanthurus triostegus* | 48 | 45 | native ×1 | Meer |
| 124 | *Chaetodon trifascialis* | 48 | 45 | native ×1 | Meer |
| 125 | *Lutjanus fulviflamma* | 48 | 56 | native ×2 | Brack/Meer |
| 126 | *Valenciennea sexguttata* | 48 | 81 | native ×2 | Meer |
| 128 | *Platax orbicularis* | 46 | 31 | native ×2 | Brack/Meer |
| 129 | *Arothron mappa* | 45 | 32 | questionable ×1 | Meer |
| 130 | *Chaetodon falcula* | 45 | 28 | native ×1 | Meer |
| 131 | *Bodianus neilli* | 44 | 48 | native ×3 | Meer |
| 132 | *Thalassoma jansenii* | 44 | 47 | native ×1 | Meer |
| 133 | *Anyperodon leucogrammicus* | 43 | 57 | native ×1 | Meer |
| 134 | *Cephalopholis boenak* | 43 | 99 | native ×2 | Meer |
| 136 | *Scolopsis monogramma* | 43 | 58 | native ×1 | Meer |
| 137 | *Aulostomus chinensis* | 42 | 46 | native ×1 | Meer |
| 138 | *Cephalopholis polyspila* | 42 | 91 | native ×1 | Meer |
| 139 | *Coris batuensis* | 42 | 41 | – | Meer |
| 140 | *Odonus niger* | 42 | 53 | native ×1 | Meer |
| 141 | *Plectorhinchus chaetodonoides* | 42 | 44 | native ×1 | Brack/Meer |
| 142 | *Scolopsis vosmeri* | 42 | 20 | native ×2 | Meer |
| 143 | *Siganus magnificus* | 42 | 45 | native ×2 | Meer |
| 144 | *Bodianus mesothorax* | 41 | 45 | native ×2 | Meer |
| 145 | *Dascyllus abudafur* | 41 | 35 | – | Meer |
| 146 | *Balistoides conspicillum* | 40 | 38 | – | Brack/Meer |
| 147 | *Helcogramma striata* | 40 | 67 | native ×2 | Meer |
| 148 | *Abudefduf septemfasciatus* | 39 | 37 | native ×2 | Meer |
| 149 | *Acanthurus nigricauda* | 39 | 38 | – | Brack/Meer |
| 150 | *Chlorurus strongylocephalus* | 39 | 38 | – | Meer |
| 151 | *Monotaxis grandoculis* | 39 | 32 | native ×2 | Meer |
| 152 | *Naso unicornis* | 39 | 30 | – | Meer |
| 153 | *Pomacentrus chrysurus* | 39 | 64 | native ×1 | Meer |

## Grenzfälle

Je 10 Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels sie nehmen (Highlights ab Level 2 übersprungen).

### Level 1/2

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 31 | *Cephalopholis formosa* | 140 | 149 | native ×1 | Meer | 1 |
| 32 | *Pomacentrus moluccensis* | 138 | 147 | native ×2 | Meer | 1 |
| 33 | *Chaetodon octofasciatus* | 136 | 123 | native ×1 | Meer | 1 |
| 34 | *Chaetodon decussatus* | 135 | 109 | native ×2 | Meer | 1 |
| 35 | *Carcharhinus melanopterus* | 125 | 105 | native ×2 | Brack/Meer | 1 |
| 36 | *Chaetodon andamanensis* | 122 | 107 | native ×3 | Meer | 1 |
| 37 | *Boleophthalmus boddarti* | 121 | 118 | native ×2 | Süß/Brack/Meer | 1 |
| 38 | *Heniochus singularius* | 116 | 104 | native ×1 | Meer | 1 |
| 39 | *Scolopsis bilineata* | 116 | 154 | native ×2 | Meer | 1 |
| 40 | *Diodon liturosus* | 114 | 93 | – | Meer | 1 |
| | **Grenze** | | | | | |
| 41 | *Lutjanus biguttatus* | 113 | 114 | native ×2 | Meer | 2 |
| 42 | *Cephalopholis argus* | 111 | 120 | native ×2 | Meer | 2 |
| 43 | *Ostracion cubicum* | 111 | 117 | native ×2 | Meer | 2 |
| 44 | *Balistapus undulatus* | 108 | 107 | native ×2 | Meer | 2 |
| 45 | *Halichoeres scapularis* | 108 | 107 | native ×1 | Meer | 2 |
| 46 | *Chaetodon vagabundus* | 107 | 88 | native ×2 | Meer | 2 |
| 47 | *Eretmochelys imbricata* | 104 | 83 | native ×2 | Brack/Meer | 2 |
| 48 | *Fistularia commersonii* | 104 | 101 | – | Meer | 2 |
| 49 | *Chelonia mydas* | 103 | 68 | native ×2 | Meer | 2 |
| 50 | *Pomacanthus imperator* | 100 | 94 | native ×1 | Meer | 2 |

### Level 2/3

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 91 | *Chlorurus troschelii* | 67 | 63 | native ×2 | Meer | 2 |
| 92 | *Chaetodon auriga* | 66 | 60 | native ×1 | Meer | 2 |
| 93 | *Chaetodon lunula* | 66 | 50 | native ×1 | Meer | 2 |
| 94 | *Halichoeres chloropterus* | 66 | 61 | native ×2 | Meer | 2 |
| 95 | *Pomacentrus pavo* | 66 | 86 | native ×1 | Meer | 2 |
| 96 | *Sufflamen chrysopterum* | 64 | 51 | native ×1 | Meer | 2 |
| 97 | *Heniochus pleurotaenia* | 63 | 49 | native ×2 | Meer | 2 |
| 98 | *Parupeneus macronemus* | 63 | 56 | native ×2 | Meer | 2 |
| 99 | *Pomacanthus annularis* | 63 | 68 | native ×1 | Meer | 2 |
| 100 | *Zenarchopterus buffonis* | 63 | 59 | native ×1 | Brack/Meer | 2 |
| | **Grenze** | | | | | |
| 101 | *Salarias fasciatus* | 62 | 64 | native ×1 | Brack/Meer | 3 |
| 102 | *Echidna nebulosa* | 61 | 49 | native ×2 | Meer | 3 |
| 103 | *Parupeneus barberinus* | 61 | 72 | native ×2 | Meer | 3 |
| 104 | *Ctenochaetus striatus* | 60 | 66 | – | Meer | 3 |
| 105 | *Octopus cyanea* | 60 | 46 | native ×2 | Meer | 3 |
| 106 | *Siganus virgatus* | 59 | 66 | native ×1 | Brack/Meer | 3 |
| 107 | *Aluterus scriptus* | 58 | 47 | – | Meer | 3 |
| 108 | *Terapon jarbua* | 57 | 45 | native ×2 | Süß/Brack/Meer | 3 |
| 109 | *Gomphosus caeruleus* | 56 | 51 | native ×2 | Meer | 3 |
| 110 | *Halichoeres argus* | 56 | 64 | native ×2 | Meer | 3 |

### Level 3/nicht im Deck

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 144 | *Bodianus mesothorax* | 41 | 45 | native ×2 | Meer | 3 |
| 145 | *Dascyllus abudafur* | 41 | 35 | – | Meer | 3 |
| 146 | *Balistoides conspicillum* | 40 | 38 | – | Brack/Meer | 3 |
| 147 | *Helcogramma striata* | 40 | 67 | native ×2 | Meer | 3 |
| 148 | *Abudefduf septemfasciatus* | 39 | 37 | native ×2 | Meer | 3 |
| 149 | *Acanthurus nigricauda* | 39 | 38 | – | Brack/Meer | 3 |
| 150 | *Chlorurus strongylocephalus* | 39 | 38 | – | Meer | 3 |
| 151 | *Monotaxis grandoculis* | 39 | 32 | native ×2 | Meer | 3 |
| 152 | *Naso unicornis* | 39 | 30 | – | Meer | 3 |
| 153 | *Pomacentrus chrysurus* | 39 | 64 | native ×1 | Meer | 3 |
| | **Grenze** | | | | | |
| 154 | *Centropyge eibli* | 38 | 55 | native ×1 | Meer | – |
| 155 | *Gymnothorax fimbriatus* | 38 | 52 | native ×2 | Brack/Meer | – |
| 156 | *Hemitaurichthys zoster* | 38 | 35 | native ×1 | Meer | – |
| 157 | *Lutjanus monostigma* | 38 | 44 | native ×2 | Brack/Meer | – |
| 158 | *Pygoplites diacanthus* | 38 | 36 | native ×1 | Meer | – |
| 159 | *Stethojulis trilineata* | 38 | 45 | native ×1 | Meer | – |
| 160 | *Aethaloperca rogaa* | 37 | 48 | native ×1 | Meer | – |
| 161 | *Synodus variegatus* | 37 | 107 | questionable ×1 | Meer | – |
| 162 | *Epinephelus erythrurus* | 36 | 46 | native ×1 | Brack/Meer | – |
| 163 | *Neopomacentrus sororius* | 36 | 29 | native ×1 | Meer | – |

## Abgleich mit Führern

Das Rezept nennt keinen Führer.
## Ausgeschlossene Kandidaten

<details><summary>531 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Striuntius lateristriga* | 72 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Toxotes jaculatrix* | 61 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Neolissochilus soroides* | 23 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Channa gachua* | 22 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Channa striata* | 21 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oryzias javanicus* | 21 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Dichotomyctere nigroviridis* | 19 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
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
| *Chaetodon ephippium* | 3 | Meer | zu wenige Nachweise (3 < 5) |
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
| *Monopterus albus* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
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

## Nicht aufgelöste Namen der Reihenfolge-Quelle

Die Referenz-DB der App kennt diese Namen nicht; die App fände sie auch nicht.

| Name | iNat |
|---|---|
| *Eviotops sebreei* | 19 |
| *Valenciennea schlieweni* | 7 |
| *Aplocheilus armatus* | 4 |
| *Pinnoctopus aspilosomatis* | 4 |
| *Eviotops mikiae* | 3 |
| *Acanthosepion aculeatum* | 2 |
| *Paracanthocobitis epimekes* | 2 |
| *Pterygoplichthys* | 2 |
| *Doboatherina salangensis* | 1 |
| *Mystacoleucus obtusirostris* | 1 |
| *Tor* | 1 |
| *Valenciennea zaboae* | 1 |
