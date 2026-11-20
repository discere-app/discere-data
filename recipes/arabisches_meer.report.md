# Bericht: Arabisches Meer & Golf von Oman (`recipes/arabisches_meer.json`)

Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.

- Referenz-DB: v3 (FishBase v26.06, SeaLifeBase v26.06)
- Salz/Süß: FishBase/SeaLifeBase v25.04 (species.parquet)
- iNaturalist: 507 Taxa (Seiten: 2)
- OBIS: 1013 Arten
- Bild: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Pez_mariposa_ar%C3%A1bigo_%28Chaetodon_melapterus%29%2C_islas_Ad_Dimaniyat%2C_Om%C3%A1n%2C_2024-08-13%2C_DD_77.jpg/330px-Pez_mariposa_ar%C3%A1bigo_%28Chaetodon_melapterus%29%2C_islas_Ad_Dimaniyat%2C_Om%C3%A1n%2C_2024-08-13%2C_DD_77.jpg — Diego Delso, CC BY-SA 4.0, https://commons.wikimedia.org/wiki/File:Pez_mariposa_ar%C3%A1bigo_(Chaetodon_melapterus),_islas_Ad_Dimaniyat,_Om%C3%A1n,_2024-08-13,_DD_77.jpg

## Gebiete

- iNaturalist: Oman (7356), United Arab Emirates (7359), Qatar (7357), Bahrain (10284), Kuwait (7355)
- OBIS: Persischer Golf (schließt die iranische Küste ein), Golf von Oman und Arabisches Meer vor Nordoman (schließt die iranische Küste ein), Arabisches Meer vor Zentral- und Südoman
- FishBase/SeaLifeBase-Verbreitung: 512, 784, 634, 048, 414

## Übersicht

- Arten der Reihenfolge-Quelle, aufgelöst: 502; nicht aufgelöst: 3
- ausgeschlossen: 314
  - zu wenige Nachweise: 293
  - kein Meeresfisch: 16
  - von Hand ausgeschlossen: 3
  - nur tiefer als die Tauchgrenze: 1
  - zu klein: 1
- Kandidaten nach den Filtern: 188
- Deck: 155 Arten (Level 1: 45, Level 2: 60, Level 3: 50); Umfang laut Rezept 40/60/50 plus Highlights
- Highlights: 5 im Deck, 0 verworfen

## Verworfene Highlights

Keine.

## iNaturalist-Namen zugeordnet

Laut `recipes/inat_names.json`: iNaturalist nennt die Art anders als die Referenz-DB; die Zählung kommt zu der der Referenz-DB-Art.

| iNaturalist | Referenz-DB | iNat | Art | Beleg |
|---|---|---|---|---|
| *Eviotops punyit* | *Eviota punyit* | 9 | Umbenennung | https://www.inaturalist.org/taxon_changes/178918 |
| *Pinnoctopus ornatus* | *Callistoctopus ornatus* | 3 | Umbenennung | https://www.inaturalist.org/taxon_changes/172615 |
| *Pinnoctopus luteus* | *Callistoctopus luteus* | 1 | Umbenennung | https://www.inaturalist.org/taxon_changes/172616 |

## Von Hand ausgeschlossen

| Art | iNat | Grund |
|---|---|---|
| *Aphaniops stoliczkanus* | 101 | Kärpfling der Küstenlagunen, Salzmarschen und Khors, keine Begegnung am Riff. |
| *Alticus kirkii* | 15 | Springschleimfisch, lebt auf Felsen in der Spritzwasserzone über der Wasserlinie. |
| *Boleophthalmus dussumieri* | 6 | Schlammspringer, lebt auf dem Schlickwatt außerhalb des Wassers. |

## Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Rhincodon typus* | Walhaie sammeln sich vor Katar (Al Shaheen) und ziehen durch die Daymaniyat-Inseln. | 104 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Dugong dugon* | Im Persischen Golf lebt die zweitgrößte Dugong-Population der Welt. | – | Verbreitung | Level 1 |
| *Mobula birostris* | Riesenmantas besuchen im Herbst die Riffe vor Musandam und den Daymaniyat-Inseln. | – | Verbreitung | Level 1 |
| *Amphiprion omanensis* | Der Oman-Anemonenfisch kommt nur an der Küste Omans und des Jemen vor. | 115 | Reihenfolge-Quelle, OBIS, Verbreitung | Level 1 |
| *Megaptera novaeangliae* | Vor Oman lebt die einzige Buckelwal-Population, die nie wandert. | – | Verbreitung | Level 1 |

## Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS oder Verbreitung): 152/155 (98 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 0
- Arten ohne Volksnamen `de` in der Referenz-DB: 78/155 (50 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 2/155 (1 %)
- Familien ohne Volksnamen `de`: 12/60 (20 %): *Aetobatidae*, *Argonautidae*, *Balaenopteridae*, *Cheloniidae*, *Dugongidae*, *Epinephelidae*, *Glaucostegidae*, *Loliginidae*, *Mobulidae*, *Octopodidae*, *Rhinopteridae*, *Sepiidae*
- Familien ohne Volksnamen `en`: 0/60 (0 %)

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

- *Dugong dugon*: Verbreitung
- *Mobula birostris*: Verbreitung
- *Megaptera novaeangliae*: Verbreitung

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

Keine.

## Deck

Spalten: Rang unter den Kandidaten, Zählung der Reihenfolge-Quelle (iNat), OBIS-Nachweise, Einträge der FishBase/SeaLifeBase-Verbreitung in den Rezept-Regionen (~~durchgestrichen~~: Eintrag sagt „nicht vorhanden“), Wasser laut FishBase/SeaLifeBase.

### Level 1 (45)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 1 | *Chelonia mydas* | 386 | 8249 | native ×4 | Meer |
| 2 | *Pomacanthus maculosus* | 139 | 117 | native ×5 | Meer |
| 3 | *Abudefduf vaigiensis* | 106 | 103 | native ×5 | Meer |
| 4 | *Scolopsis ghanam* | 105 | 100 | native ×5 | Meer |
| 5 | *Ostracion cyanurus* | 96 | 95 | native ×5 | Meer |
| 6 | *Lutjanus argentimaculatus* | 92 | 75 | native ×5 | Süß/Brack/Meer |
| 7 | *Gymnothorax undulatus* | 90 | 75 | native ×5 | Brack/Meer |
| 8 | *Acanthosepion pharaonis* | 85 | 63 | native ×5 | Meer |
| 9 | *Chaetodon melapterus* | 83 | 139 | native ×5 | Meer |
| 10 | *Amphiprion clarkii* | 82 | 67 | native ×5 | Meer |
| 11 | *Gymnothorax favagineus* | 75 | 57 | native ×1 | Brack/Meer |
| 12 | *Acanthopagrus bifasciatus* | 70 | 65 | native ×5 | Brack/Meer |
| 13 | *Acanthurus sohal* | 70 | 51 | native ×5 | Meer |
| 14 | *Cyclichthys orbicularis* | 70 | 55 | native ×2 | Meer |
| 15 | *Pteropterus antennatus* | 69 | 4 | native ×1 | Meer |
| 16 | *Chaetodon nigropunctatus* | 68 | 69 | native ×5 | Meer |
| 17 | *Diodon holocanthus* | 65 | 43 | native ×1 | Meer |
| 18 | *Cephalopholis hemistiktos* | 64 | 64 | native ×5 | Meer |
| 19 | *Scarus persicus* | 62 | 42 | native ×5 | Meer |
| 20 | *Gymnothorax nudivomer* | 59 | 42 | native ×1 | Meer |
| 21 | *Diodon hystrix* | 57 | 42 | native ×1 | Meer |
| 22 | *Eretmochelys imbricata* | 57 | 227 | native ×4 | Brack/Meer |
| 23 | *Gymnothorax griseus* | 57 | 44 | native ×1 | Meer |
| 24 | *Cheilinus lunulatus* | 52 | 42 | native ×5 | Meer |
| 25 | *Dascyllus trimaculatus* | 51 | 69 | native ×5 | Meer |
| 26 | *Rhinecanthus assasi* | 50 | 45 | native ×5 | Meer |
| 27 | *Pomacanthus imperator* | 46 | 32 | native ×1 | Meer |
| 28 | *Thalassoma lunare* | 46 | 38 | native ×5 | Meer |
| 29 | *Terapon jarbua* | 44 | 49 | native ×5 | Süß/Brack/Meer |
| 30 | *Odonus niger* | 43 | 40 | native ×1 | Meer |
| 31 | *Flavocaranx bajad* | 40 | 36 | native ×5 | Meer |
| 32 | *Heniochus acuminatus* | 40 | 41 | native ×5 | Brack/Meer |
| 33 | *Zebrasoma xanthurum* | 40 | 38 | native ×5 | Meer |
| 34 | *Monodactylus argenteus* | 38 | 31 | native ×2 | Süß/Brack/Meer |
| 35 | *Fistularia commersonii* | 37 | 33 | native ×1 | Meer |
| 36 | *Pseudochromis aldabraensis* | 37 | 58 | native ×5 | Meer |
| 37 | *Carcharhinus limbatus* | 35 | 7 | native ×5 | Brack/Meer |
| 38 | *Parupeneus margaritatus* | 34 | 54 | native ×5 | Meer |
| 39 | *Caretta caretta* | 33 | 814 | native ×3 | Meer |
| 40 | *Epinephelus stoliczkae* | 33 | 32 | native ×1 | Meer |
| 104 | *Rhincodon typus* (Highlight) | 11 | 37 | native ×5 | Meer |
| – | *Dugong dugon* (Highlight) | – | – | native ×4 | Meer |
| – | *Mobula birostris* (Highlight) | – | – | native ×1 | Meer |
| 115 | *Amphiprion omanensis* (Highlight) | 9 | 28 | native ×1 | Meer |
| – | *Megaptera novaeangliae* (Highlight) | – | – | native ×5 | Meer |

### Level 2 (60)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 41 | *Caesio varilineata* | 32 | 37 | native ×5 | Meer |
| 42 | *Carcharhinus melanopterus* | 32 | 12 | native ×5 | Brack/Meer |
| 43 | *Labroides dimidiatus* | 32 | 36 | native ×5 | Meer |
| 44 | *Octopus cyanea* | 31 | 25 | native ×5 | Meer |
| 45 | *Chlorurus sordidus* | 30 | 13 | native ×5 | Brack/Meer |
| 46 | *Cryptocentrus lutheri* | 30 | 33 | native ×5 | Meer |
| 47 | *Lutjanus fulviflamma* | 29 | 32 | native ×5 | Brack/Meer |
| 48 | *Chaetodon collare* | 28 | 58 | native ×1 | Meer |
| 49 | *Diodon liturosus* | 28 | 22 | native ×1 | Meer |
| 50 | *Ecsenius pulcher* | 28 | 64 | native ×5 | Meer |
| 51 | *Arothron stellatus* | 27 | 30 | native ×5 | Brack/Meer |
| 52 | *Pastinachus sephen* | 26 | 15 | native ×5 | Süß/Brack/Meer |
| 53 | *Abudefduf sordidus* | 24 | 20 | native ×1 | Brack/Meer |
| 54 | *Chanos chanos* | 24 | 20 | native ×5 | Süß/Brack/Meer |
| 55 | *Platax teira* | 24 | 18 | native ×5 | Meer |
| 56 | *Epinephelus coioides* | 23 | 20 | native ×5 | Brack/Meer |
| 57 | *Pardachirus marmoratus* | 23 | 18 | native ×5 | Meer |
| 58 | *Pterois miles* | 23 | 18 | native ×5 | Meer |
| 59 | *Taeniurops meyeni* | 23 | 22 | native ×5 | Meer |
| 60 | *Canthigaster valentini* | 22 | 18 | native ×1 | Meer |
| 61 | *Chaetodon pictus* | 22 | 15 | native ×1 | Meer |
| 62 | *Gerres longirostris* | 22 | 1 | native ×5 | Süß/Brack/Meer |
| 63 | *Halichoeres marginatus* | 22 | 26 | native ×5 | Meer |
| 64 | *Torpedo sinuspersici* | 22 | 29 | native ×5 | Brack/Meer |
| 65 | *Sufflamen fraenatum* | 21 | 17 | native ×1 | Meer |
| 66 | *Ostorhinchus aureus* | 20 | 38 | native ×1 | Meer |
| 67 | *Pomacentrus leptus* | 20 | 25 | native ×5 | Meer |
| 68 | *Scomberoides commersonnianus* | 20 | 15 | native ×5 | Brack/Meer |
| 69 | *Stegostoma tigrinum* | 20 | 16 | native ×5 | Brack/Meer |
| 70 | *Tylosurus choram* | 20 | 13 | native ×1 | Meer |
| 71 | *Amblyeleotris periophthalmus* | 19 | 14 | native ×5 | Meer |
| 72 | *Gymnomuraena zebra* | 19 | 18 | native ×5 | Meer |
| 73 | *Parupeneus macronemus* | 19 | 23 | native ×5 | Meer |
| 74 | *Rhizoprionodon acutus* | 19 | 7 | native ×5 | Süß/Brack/Meer |
| 75 | *Sphyraena barracuda* | 19 | 18 | native ×5 | Brack/Meer |
| 76 | *Tetrosomus gibbosus* | 19 | 16 | native ×5 | Meer |
| 77 | *Istigobius ornatus* | 18 | 24 | native ×2 | Brack/Meer |
| 78 | *Lutjanus ehrenbergii* | 18 | 21 | native ×5 | Süß/Brack/Meer |
| 79 | *Platycephalus indicus* | 18 | 24 | native ×5 | Brack/Meer |
| 80 | *Rhinoptera jayakari* | 18 | 9 | native ×1 | Meer |
| 81 | *Carcharhinus sorrah* | 17 | 23 | native ×5 | Brack/Meer |
| 82 | *Cirrhitichthys calliurus* | 16 | 22 | native ×1 | Meer |
| 83 | *Plotosus lineatus* | 16 | 18 | native ×5 | Brack/Meer |
| 84 | *Scuticaria tigrina* | 16 | 10 | native ×1 | Meer |
| 85 | *Antennablennius adenensis* | 15 | 13 | native ×5 | Meer |
| 86 | *Gymnothorax pictus* | 15 | 38 | native ×1 | Brack/Meer |
| 87 | *Maculabatis randalli* | 15 | 12 | native ×3 | Meer |
| 88 | *Sphyrna mokarran* | 15 | 1 | native ×5 | Brack/Meer |
| 89 | *Aetobatus ocellatus* | 14 | 17 | native ×1 | Brack/Meer |
| 90 | *Chromis xanthopterygia* | 14 | 17 | native ×5 | Meer |
| 91 | *Carcharhinus dussumieri* | 13 | 11 | native ×5 | Meer |
| 92 | *Scarus ferrugineus* | 13 | 9 | native ×5 | Meer |
| 93 | *Scomberomorus commerson* | 13 | 15 | native ×5 | Meer |
| 94 | *Amblygobius albimaculatus* | 12 | 15 | native ×5 | Brack/Meer |
| 95 | *Cheilodipterus persicus* | 12 | 23 | native ×4 | Meer |
| 96 | *Cryptocentroides arabicus* | 12 | 10 | native ×1 | Meer |
| 97 | *Diplodus kotschyi* | 12 | 8 | native ×5 | Meer |
| 98 | *Himantura uarnak* | 12 | 17 | native ×5 | Brack/Meer |
| 99 | *Rhabdosargus sarba* | 12 | 12 | native ×5 | Brack/Meer |
| 100 | *Scolopsis taeniata* | 12 | 16 | native ×5 | Meer |

### Level 3 (50)

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 101 | *Zanclus cornutus* | 12 | 11 | native ×1 | Meer |
| 102 | *Acanthopagrus berda* | 11 | 15 | native ×5 | Süß/Brack/Meer |
| 103 | *Hippocampus kuda* | 11 | 8 | native ×5 | Brack/Meer |
| 105 | *Sepioteuthis lessoniana* | 11 | 9 | native ×4 | Brack/Meer |
| 106 | *Siganus javus* | 11 | 10 | native ×5 | Brack/Meer |
| 107 | *Siganus sutor* | 11 | 7 | – | Brack/Meer |
| 108 | *Canthigaster petersii* | 10 | 14 | native ×1 | Meer |
| 109 | *Chaetodon gardineri* | 10 | 12 | native ×5 | Meer |
| 110 | *Euthynnus affinis* | 10 | 9 | native ×5 | Meer |
| 111 | *Istiblennius pox* | 10 | 23 | native ×5 | Meer |
| 112 | *Taeniura lymma* | 10 | 9 | native ×5 | Meer |
| 113 | *Valenciennea sexguttata* | 10 | 11 | native ×5 | Meer |
| 114 | *Amblyeleotris triguttata* | 9 | 9 | native ×1 | Meer |
| 116 | *Argonauta hians* | 9 | 6 | native ×1 | Meer |
| 117 | *Arothron immaculatus* | 9 | 9 | native ×1 | Brack/Meer |
| 118 | *Carcharhinus brevipinna* | 9 | 1 | native ×1 | Meer |
| 119 | *Eviota punyit* | 9 | 9 | native ×1 | Meer |
| 120 | *Istigobius decoratus* | 9 | 43 | native ×4 | Meer |
| 121 | *Scarus ghobban* | 9 | 10 | native ×5 | Brack/Meer |
| 122 | *Bothus pantherinus* | 8 | 9 | native ×5 | Meer |
| 123 | *Caranx sexfasciatus* | 8 | 8 | native ×5 | Süß/Brack/Meer |
| 124 | *Cyclichthys spilostylus* | 8 | 6 | native ×1 | Meer |
| 125 | *Glaucostegus halavi* | 8 | 5 | native ×1 | Meer |
| 126 | *Gnathanodon speciosus* | 8 | 10 | native ×5 | Meer |
| 127 | *Hemipristis elongata* | 8 | – | native ×5 | Meer |
| 128 | *Mulloidichthys vanicolensis* | 8 | 18 | native ×1 | Meer |
| 129 | *Omobranchus fasciolatus* | 8 | 7 | native ×5 | Meer |
| 130 | *Platax orbicularis* | 8 | 7 | native ×5 | Brack/Meer |
| 131 | *Pseudochromis persicus* | 8 | 15 | native ×5 | Meer |
| 132 | *Selar crumenophthalmus* | 8 | 19 | native ×5 | Meer |
| 133 | *Trachyrhamphus bicoarctatus* | 8 | 8 | native ×5 | Meer |
| 134 | *Aluterus scriptus* | 7 | 5 | native ×1 | Meer |
| 135 | *Apogonichthyoides taeniatus* | 7 | 20 | native ×5 | Meer |
| 136 | *Cirrhitus pinnulatus* (Quelle: *Cirrhitus spilotoceps*) | 7 | 7 | native ×1 | Meer |
| 137 | *Echidna nebulosa* | 7 | 3 | native ×5 | Meer |
| 138 | *Gerres oyena* | 7 | 13 | native ×5 | Brack/Meer |
| 139 | *Hippocampus kelloggi* | 7 | 5 | native ×1 | Meer |
| 140 | *Loxodon macrorhinus* | 7 | 1 | native ×1 | Meer |
| 141 | *Scolopsis curite* | 7 | 7 | native ×5 | Meer |
| 142 | *Upeneus oligospilus* | 7 | 5 | native ×3 | Meer |
| 143 | *Ablennes hians* | 6 | 9 | native ×5 | Brack/Meer |
| 144 | *Aetomylaeus wafickii* | 6 | 1 | native ×1 | Meer |
| 145 | *Carcharhinus amboinensis* | 6 | – | native ×5 | Brack/Meer |
| 146 | *Cheilodipterus novemstriatus* | 6 | 13 | native ×5 | Meer |
| 147 | *Coris formosa* | 6 | 9 | native ×1 | Meer |
| 148 | *Echeneis naucrates* | 6 | 27 | native ×5 | Brack/Meer |
| 149 | *Gymnura poecilura* | 6 | 6 | native ×5 | Meer |
| 150 | *Istiblennius edentulus* | 6 | 9 | native ×1 | Brack/Meer |
| 151 | *Lutjanus indicus* | 6 | 4 | native ×2 | Süß/Brack/Meer |
| 152 | *Lutjanus sapphirolineatus* | 6 | 5 | native ×1 | Meer |

## Grenzfälle

Je 10 Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels sie nehmen (Highlights ab Level 2 übersprungen).

### Level 1/2

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 31 | *Flavocaranx bajad* | 40 | 36 | native ×5 | Meer | 1 |
| 32 | *Heniochus acuminatus* | 40 | 41 | native ×5 | Brack/Meer | 1 |
| 33 | *Zebrasoma xanthurum* | 40 | 38 | native ×5 | Meer | 1 |
| 34 | *Monodactylus argenteus* | 38 | 31 | native ×2 | Süß/Brack/Meer | 1 |
| 35 | *Fistularia commersonii* | 37 | 33 | native ×1 | Meer | 1 |
| 36 | *Pseudochromis aldabraensis* | 37 | 58 | native ×5 | Meer | 1 |
| 37 | *Carcharhinus limbatus* | 35 | 7 | native ×5 | Brack/Meer | 1 |
| 38 | *Parupeneus margaritatus* | 34 | 54 | native ×5 | Meer | 1 |
| 39 | *Caretta caretta* | 33 | 814 | native ×3 | Meer | 1 |
| 40 | *Epinephelus stoliczkae* | 33 | 32 | native ×1 | Meer | 1 |
| | **Grenze** | | | | | |
| 41 | *Caesio varilineata* | 32 | 37 | native ×5 | Meer | 2 |
| 42 | *Carcharhinus melanopterus* | 32 | 12 | native ×5 | Brack/Meer | 2 |
| 43 | *Labroides dimidiatus* | 32 | 36 | native ×5 | Meer | 2 |
| 44 | *Octopus cyanea* | 31 | 25 | native ×5 | Meer | 2 |
| 45 | *Chlorurus sordidus* | 30 | 13 | native ×5 | Brack/Meer | 2 |
| 46 | *Cryptocentrus lutheri* | 30 | 33 | native ×5 | Meer | 2 |
| 47 | *Lutjanus fulviflamma* | 29 | 32 | native ×5 | Brack/Meer | 2 |
| 48 | *Chaetodon collare* | 28 | 58 | native ×1 | Meer | 2 |
| 49 | *Diodon liturosus* | 28 | 22 | native ×1 | Meer | 2 |
| 50 | *Ecsenius pulcher* | 28 | 64 | native ×5 | Meer | 2 |

### Level 2/3

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 91 | *Carcharhinus dussumieri* | 13 | 11 | native ×5 | Meer | 2 |
| 92 | *Scarus ferrugineus* | 13 | 9 | native ×5 | Meer | 2 |
| 93 | *Scomberomorus commerson* | 13 | 15 | native ×5 | Meer | 2 |
| 94 | *Amblygobius albimaculatus* | 12 | 15 | native ×5 | Brack/Meer | 2 |
| 95 | *Cheilodipterus persicus* | 12 | 23 | native ×4 | Meer | 2 |
| 96 | *Cryptocentroides arabicus* | 12 | 10 | native ×1 | Meer | 2 |
| 97 | *Diplodus kotschyi* | 12 | 8 | native ×5 | Meer | 2 |
| 98 | *Himantura uarnak* | 12 | 17 | native ×5 | Brack/Meer | 2 |
| 99 | *Rhabdosargus sarba* | 12 | 12 | native ×5 | Brack/Meer | 2 |
| 100 | *Scolopsis taeniata* | 12 | 16 | native ×5 | Meer | 2 |
| | **Grenze** | | | | | |
| 101 | *Zanclus cornutus* | 12 | 11 | native ×1 | Meer | 3 |
| 102 | *Acanthopagrus berda* | 11 | 15 | native ×5 | Süß/Brack/Meer | 3 |
| 103 | *Hippocampus kuda* | 11 | 8 | native ×5 | Brack/Meer | 3 |
| 105 | *Sepioteuthis lessoniana* | 11 | 9 | native ×4 | Brack/Meer | 3 |
| 106 | *Siganus javus* | 11 | 10 | native ×5 | Brack/Meer | 3 |
| 107 | *Siganus sutor* | 11 | 7 | – | Brack/Meer | 3 |
| 108 | *Canthigaster petersii* | 10 | 14 | native ×1 | Meer | 3 |
| 109 | *Chaetodon gardineri* | 10 | 12 | native ×5 | Meer | 3 |
| 110 | *Euthynnus affinis* | 10 | 9 | native ×5 | Meer | 3 |
| 111 | *Istiblennius pox* | 10 | 23 | native ×5 | Meer | 3 |

### Level 3/nicht im Deck

| Rang | Art | iNat | OBIS | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 143 | *Ablennes hians* | 6 | 9 | native ×5 | Brack/Meer | 3 |
| 144 | *Aetomylaeus wafickii* | 6 | 1 | native ×1 | Meer | 3 |
| 145 | *Carcharhinus amboinensis* | 6 | – | native ×5 | Brack/Meer | 3 |
| 146 | *Cheilodipterus novemstriatus* | 6 | 13 | native ×5 | Meer | 3 |
| 147 | *Coris formosa* | 6 | 9 | native ×1 | Meer | 3 |
| 148 | *Echeneis naucrates* | 6 | 27 | native ×5 | Brack/Meer | 3 |
| 149 | *Gymnura poecilura* | 6 | 6 | native ×5 | Meer | 3 |
| 150 | *Istiblennius edentulus* | 6 | 9 | native ×1 | Brack/Meer | 3 |
| 151 | *Lutjanus indicus* | 6 | 4 | native ×2 | Süß/Brack/Meer | 3 |
| 152 | *Lutjanus sapphirolineatus* | 6 | 5 | native ×1 | Meer | 3 |
| | **Grenze** | | | | | |
| 153 | *Mulloidichthys flavolineatus* (Quelle: *Mulloidichthys flavicaudus*) | 6 | 3 | native ×5 | Meer | – |
| 154 | *Neopomacentrus cyanomos* | 6 | 17 | native ×5 | Meer | – |
| 155 | *Neotrygon indica* | 6 | 5 | – | Meer | – |
| 156 | *Netuma bilineata* | 6 | 11 | native ×5 | Süß/Brack/Meer | – |
| 157 | *Parablennius pilicornis* | 6 | 3 | native ×1 | Meer | – |
| 158 | *Paragaleus longicaudatus* | 6 | 3 | native ×5 | Meer | – |
| 159 | *Pomacentrus arabicus* | 6 | 8 | native ×1 | Meer | – |
| 160 | *Pomadasys argenteus* | 6 | 6 | native ×5 | Süß/Brack/Meer | – |
| 161 | *Rastrelliger kanagurta* | 6 | 11 | native ×5 | Meer | – |
| 162 | *Rhynchobatus djiddensis* | 6 | 3 | native ×5 | Brack/Meer | – |

## Abgleich mit Führern

Das Rezept nennt keinen Führer.
## Änderungen gegenüber dem bestehenden Deck

- neu: 3: *Istiblennius edentulus*, *Lutjanus indicus*, *Lutjanus sapphirolineatus*
- entfallen: 3: *Alticus kirkii*, *Aphaniops stoliczkanus*, *Boleophthalmus dussumieri*

## Ausgeschlossene Kandidaten

<details><summary>314 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Garra barreimiae* | 105 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Aphaniops stoliczkanus* | 101 | Süß/Brack/Meer | von Hand ausgeschlossen (Kärpfling der Küstenlagunen, Salzmarschen und Khors, keine Begegnung am Riff.) |
| *Oreochromis mossambicus* | 67 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinus rubrofuscus* | 35 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Plectorhinchus gaterinus* | 29 | Meer | nur tiefer als die Tauchgrenze (erst ab 55 m) |
| *Aphaniops kruppi* | 23 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Oreochromis niloticus* | 19 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinion muscatense* | 16 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Alticus kirkii* | 15 | Meer | von Hand ausgeschlossen (Springschleimfisch, lebt auf Felsen in der Spritzwasserzone über der Wasserlinie.) |
| *Eviota guttata* | 15 | Meer | zu klein (höchstens 3.2 cm) |
| *Boleophthalmus dussumieri* | 6 | Süß/Brack/Meer | von Hand ausgeschlossen (Schlammspringer, lebt auf dem Schlickwatt außerhalb des Wassers.) |
| *Garra shamal* | 6 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Garra longipinnis* | 5 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Aluterus monoceros* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Argyrops spinifer* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Bodianus macrognathos* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Carcharhinus amblyrhynchoides* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Carcharhinus macloti* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Chaenogaleus macrostoma* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Cheilodipterus macrodon* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Chilomycterus reticulatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Chrysiptera unimaculata* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Coryphaena hippurus* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Diagramma pictum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Epinephelus coeruleopunctatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Garra gallagheri* | 4 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gymnothorax elaineheemstrae* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Gymnothorax flavoculus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Kyphosus vaigiensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lepidochelys olivacea* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Melichthys indicus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Muraenesox cinereus* | 4 | Süß/Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Ostorhinchus fleurieu* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Pseudanthias townsendi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Rachycentron canadum* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Rhynchobatus laevis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Stephanolepis diaspros* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Sufflamen chrysopterum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Thalassoma loxum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Abalistes stellatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Aetomylaeus milvus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Alectis ciliaris* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Amphioctopus aegina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Blenniella periophthalmus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Callistoctopus ornatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cheilinus trilobatus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Ctenochaetus striatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ecsenius nalolo* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Enchelycore pardalis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Epinephelus malabaricus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Halichoeres nigrescens* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Herklotsichthys lossei* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lagocephalus laevigatus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Lethrinus lentjan* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Lethrinus microdon* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lethrinus nebulosus* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Mimoblennius cirrosus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Mulloidichthys ayliffe* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pateobatis jenkinsii* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Pinjalo pinjalo* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Platax pinnatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Platycaranx chrysophrys* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Plectorhinchus sordidus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Plicomugil labiosus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pomadasys aheneus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pseudochromis nigrovittatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pteropterus mombasae* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Rhabdosargus haffara* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Scarus fuscopurpureus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Scomberoides tol* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Sphyraena qenie* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Sphyrna lewini* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Synodus variegatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Terapon puta* | 3 | Süß/Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Thunnus albacares* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Trachinotus baillonii* | 3 | Brack/Meer | zu wenige Nachweise (3 < 5) |
| *Valenciennea persica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Acanthopagrus catenula* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Apogonichthyoides pharaonis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Aurigequula fasciata* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Brevitrygon manjajiae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Callechelys marmorata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Caranx heberi* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Cheilodipterus quinquelineatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Choerodon robustus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Chrysiptera sheila* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cirripectes filamentosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Coris nigrotaenia* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Corythoichthys flavofasciatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Crenidens crenidens* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dascyllus marginatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Diplodus omanensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Doryrhamphus excisus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ecsenius lineatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epinephelus polylepis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Epinephelus tukula* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ferdauia ferdau* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Garra cavernicola* | 2 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gerres filamentosus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Gerres infasciatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Glaucostegus granulatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnothorax fimbriatus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Gymnothorax punctatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Halichoeres signifer* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Halichoeres zeylonicus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Istiblennius spilotus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Karalla daura* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lepidamia omanensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lutjanus malabaricus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Lutjanus quinquelineatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mobula kuhlii* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mustelus mosis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Myrichthys colubrinus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Narcine oculifera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nemipterus japonicus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nemipterus peronii* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Neopomacentrus sindensis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Omobranchus elongatus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Ostorhinchus apogonoides* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ostorhinchus cyanosoma* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Ostracion cubicum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Parapercis robinsoni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Parioglossus raoi* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Parupeneus rubescens* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pateobatis fai* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pempheris tominagai* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Periophthalmus argentilineatus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Plectorhinchus flavomaculatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plectorhinchus playfairi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Plectorhinchus schotaf* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Pomacentrus trichrourus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pomadasys commersonnii* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Pomadasys taeniatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Psettodes erumei* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudochromis leucorhynchus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pseudochromis punctatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rhinobatos punctifer* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Rhinolepadichthys lineatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sargocentron rubrum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Saurida tumbil* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scarus zufar* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scatophagus argus* | 2 | Süß/Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Scorpaenopsis oxycephala* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Scyris indica* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Sparidentex hasta* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Sphyraena flavicauda* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Sphyraena putnamae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Thunnus tonggol* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trichiurus lepturus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Trimma winterbottomi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tripterodon orbis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Urogymnus asperrimus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Abantennarius coccineus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Acanthurus nigricauda* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Aethaloperca rogaa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Aetomylaeus nichofii* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Alepes djedaba* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amblyeleotris downingi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amblyeleotris wheeleri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amblypomacentrus annulatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Antennablennius simonyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Antennarius indicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Apogonichthyoides nigripinnis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Argyrosomus heinii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Arothron multilineatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Asterropteryx semipunctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Atherinomorus lacunosus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Atule mate* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Auxis rochei* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Bathygobius fuscus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Bifax lacinia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bodianus axillaris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Boops lineatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bryaninops tigris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Caesio cuning* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Callistoctopus luteus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Canthigaster punctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Caranx ignobilis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Carcharhinus leucas* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Carcharhinus plumbeus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Cephalopholis argus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaetodon dialeucos* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chaetodon semilarvatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Channa striata* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cheilodipterus arabicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cheimerius nufar* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chelon ramada* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Chiloscyllium arabicum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chirocentrus dorab* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Chirocentrus nudus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Choridactylus multibarbus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clarias gariepinus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Coris caudimacula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cryptocentrus fasciatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ctenopharyngodon idella* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Cyprinus carpio* | 1 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Decapterus russelli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dermatolepis striolata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dinoperca petersi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Drepane longimana* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Elagatis bipinnulata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ellochelon vaigiensis* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Enneapterygius ventermaculus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ephippus orbis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus areolatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus bleekeri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus epistictus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus flavocaeruleus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus gabriellae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus marginatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Epinephelus radiatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fowlerichthys scriptissimus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Fusigobius inframaculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Galeocerdo cuvier* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Garra dunsirei* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Gnatholepis anjerensis* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Gobiodon reticulatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax javanicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gymnothorax phasmatodes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres iridis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres lapillus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres melas* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halichoeres stigmaticus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Haliophis diademus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Harpadon nehereus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Helcogramma steinitzi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hetereleotris nasoramosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hetereleotris zonata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Himantura leoparda* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hyporhamphus affinis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Istiophorus platypterus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Katsuwonus pelamis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lates calcarifer* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Lepidamia natalensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leptojulis cyanopleura* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lithognathus mormyrus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Lutjanus coeruleolineatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lutjanus kasmira* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lutjanus rivulatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lutjanus russellii* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Macropharyngodon bipartitus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Maculabatis gerrardi* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Megalaspis cordyla* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Mene maculata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Mobula eregoodoo* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mola alexandrini* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Monocentris japonica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Moolgarda tade* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Mugil cephalus* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Myripristis murdjan* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Naso brevirostris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Naso fageni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Negaprion acutidens* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Nematalosa resticularia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nemipterus zysron* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neoglyphidodon melas* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Oman ypsilon* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Otolithes cuvieri* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pampus argenteus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Papilloculiceps longiceps* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parascolopsis akatamae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parastromateus niger* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pardachirus balius* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Parupeneus barberinus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pelates quadrilineatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pempheris darvelli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pempheris wilsoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Periophthalmus waltoni* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Petroscirtes ancylodon* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Platybelone platura* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plectorhinchus pictus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plesiops nigricans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plicofollis dussumieri* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pomacanthus semicirculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomacentrus aquilus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomadasys punctulatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pomatomus saltatrix* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pristis zijsron* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Pseudanthias marcia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudochromis caudalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudochromis fuscus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudochromis omanensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pseudorhombus elevatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ptereleotris arabica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ptereleotris monoptera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Remora albescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhina ancylostomus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhinobatos annandalei* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Rhinoptera javanica* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Rhynchorhamphus georgii* | 1 | Süß/Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Rusichthys explicitus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scarus caudofasciatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scomberoides lysan* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Seriola dumerili* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Seriolina nigrofasciata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Sillago sihama* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Solenostomus cyanopterus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sparus aurata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Sphyraena obtusata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Suezichthys gracilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sufflamen albicaudatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Synanceia verrucosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thaumoctopus mimicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thunnus alalunga* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Torpedo adenensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trachinotus blochii* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Triaenodon obesus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trichonotus arabicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trichonotus nikii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trimma haima* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Umbrina ronchus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Upeneus guttatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Upeneus heemstra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Upeneus sulphureus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |

</details>

## Nicht aufgelöste Namen der Reihenfolge-Quelle

Die Referenz-DB der App kennt diese Namen nicht; die App fände sie auch nicht.

| Name | iNat |
|---|---|
| *Pterygoplichthys* | 3 |
| *Valenciennea schlieweni* | 2 |
| *Priolepis zebra* | 1 |
