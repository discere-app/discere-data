# Bericht: Arabisches Meer & Golf von Oman (`recipes/arabian_sea.json`)

Erzeugt von `scripts/build_deck.py`. Daten bestimmen die Reihenfolge, Verbreitungsdaten und Führer bestätigen das Vorkommen, die Highlights sind von Hand gewählt.

- Referenz-DB: v3 (FishBase v26.06, SeaLifeBase v26.06)
- Salz/Süß: FishBase/SeaLifeBase v25.04 (species.parquet)
- iNaturalist: 507 Taxa (Seiten: 2)
- OBIS: 834 Arten mit Nachweisen außer iNaturalist
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

## Zu entscheiden

Hinweise, keine Ausschlüsse: Jede Zeile wird im Rezept entschieden (`exclude` mit Grund, Namenszuordnung, Level) oder bewusst belassen. Schwellen: `warnings` im Rezept.

| Art | Subdeck | Warnung | Zahlen |
|---|---|---|---|
| *Cyclichthys orbicularis* | level-1 | tot beobachtet | 10 von 11 Beobachtungen mit Angabe lebend/tot tot (91 %) |
| *Diodon holocanthus* | level-1 | tot beobachtet | 8 von 10 Beobachtungen mit Angabe lebend/tot tot (80 %) |
| *Carcharhinus limbatus* | level-1 | tot beobachtet | 10 von 10 Beobachtungen mit Angabe lebend/tot tot (100 %) |
| *Sphyrna mokarran* | level-2 | tot beobachtet | 8 von 8 Beobachtungen mit Angabe lebend/tot tot (100 %) |
| *Himantura uarnak* | level-2 | tot beobachtet | 4 von 5 Beobachtungen mit Angabe lebend/tot tot (80 %) |
| *Conomurex persicus* | invertebrates | tot beobachtet | 7 von 8 Beobachtungen mit Angabe lebend/tot tot (88 %) |
| *Cirrhitus spilotoceps* | level-3 | Name der Region | Deck: *Cirrhitus spilotoceps*; die Referenz-DB führt die Art als *Cirrhitus pinnulatus* |
| *Carcharhinus limbatus* | level-1 | wenige Beobachter | 28 von 35 Beobachtungen von 2 Personen (80 %); 8 Beobachter insgesamt |
| *Amphiprion omanensis* | level-1 | wenige Beobachter | 5 von 9 Beobachtungen von 2 Personen (56 %); 6 Beobachter insgesamt |
| *Chlorurus sordidus* | level-2 | wenige Beobachter | 18 von 30 Beobachtungen von 2 Personen (60 %); 12 Beobachter insgesamt |
| *Pterois miles* | level-2 | wenige Beobachter | 13 von 23 Beobachtungen von 2 Personen (57 %); 12 Beobachter insgesamt |
| *Halichoeres marginatus* | level-2 | wenige Beobachter | 15 von 22 Beobachtungen von 2 Personen (68 %); 6 Beobachter insgesamt |
| *Pomacentrus leptus* | level-2 | wenige Beobachter | 10 von 20 Beobachtungen von 2 Personen (50 %); 8 Beobachter insgesamt |
| *Amblyeleotris periophthalmus* | level-2 | wenige Beobachter | 10 von 19 Beobachtungen von 2 Personen (53 %); 9 Beobachter insgesamt |
| *Rhizoprionodon acutus* | level-2 | wenige Beobachter | 13 von 19 Beobachtungen von 2 Personen (68 %); 8 Beobachter insgesamt |
| *Carcharhinus sorrah* | level-2 | wenige Beobachter | 14 von 17 Beobachtungen von 2 Personen (82 %); 5 Beobachter insgesamt |
| *Antennablennius adenensis* | level-2 | wenige Beobachter | 12 von 15 Beobachtungen von 2 Personen (80 %); 4 Beobachter insgesamt |
| *Sphyrna mokarran* | level-2 | wenige Beobachter | 15 von 15 Beobachtungen von 2 Personen (100 %); 2 Beobachter insgesamt |
| *Carcharhinus dussumieri* | level-2 | wenige Beobachter | 11 von 13 Beobachtungen von 2 Personen (85 %); 4 Beobachter insgesamt |
| *Cheilodipterus persicus* | level-2 | wenige Beobachter | 7 von 12 Beobachtungen von 2 Personen (58 %); 7 Beobachter insgesamt |
| *Lutjanus argentimaculatus* | level-1 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Terapon jarbua* | level-1 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Monodactylus argenteus* | level-1 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Pastinachus sephen* | level-2 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Chanos chanos* | level-2 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Gerres longirostris* | level-2 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Rhizoprionodon acutus* | level-2 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Lutjanus ehrenbergii* | level-2 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Acanthopagrus berda* | level-3 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Caranx sexfasciatus* | level-3 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |
| *Lutjanus indicus* | level-3 | Süßwasser-Kennzeichen | FishBase/SeaLifeBase: Fresh gesetzt (Süß/Brack/Meer) |

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

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS ohne iNaturalist oder Verbreitung): 151/155 (97 %)
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
- *Siganus sutor*: Reihenfolge-Quelle

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

Keine.

## Deck

Spalten: Rang unter den Kandidaten, Zählung der Reihenfolge-Quelle (iNat), OBIS-Nachweise ohne den iNaturalist-Datensatz, Einträge der FishBase/SeaLifeBase-Verbreitung in den Rezept-Regionen (~~durchgestrichen~~: Eintrag sagt „nicht vorhanden“), Wasser laut FishBase/SeaLifeBase.

### Level 1 (45)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 1 | *Chelonia mydas* (225 Beobachter) | 386 | 7955 | native ×4 | Meer |
| 2 | *Pomacanthus maculosus* (76 Beobachter) | 139 | 13 | native ×5 | Meer |
| 3 | *Abudefduf vaigiensis* (64 Beobachter) | 106 | 14 | native ×5 | Meer |
| 4 | *Scolopsis ghanam* (54 Beobachter) | 105 | 12 | native ×5 | Meer |
| 5 | *Ostracion cyanurus* (45 Beobachter) | 96 | 28 | native ×5 | Meer |
| 6 | *Lutjanus argentimaculatus* (54 Beobachter) | 92 | 3 | native ×5 | Süß/Brack/Meer |
| 7 | *Gymnothorax undulatus* (39 Beobachter) | 90 | 8 | native ×5 | Brack/Meer |
| 8 | *Acanthosepion pharaonis* (51 Beobachter) | 85 | 6 | native ×5 | Meer |
| 9 | *Chaetodon melapterus* (42 Beobachter) | 83 | 85 | native ×5 | Meer |
| 10 | *Amphiprion clarkii* (38 Beobachter) | 82 | 5 | native ×5 | Meer |
| 11 | *Gymnothorax favagineus* (37 Beobachter) | 75 | – | native ×1 | Brack/Meer |
| 12 | *Acanthopagrus bifasciatus* (37 Beobachter) | 70 | 7 | native ×5 | Brack/Meer |
| 13 | *Acanthurus sohal* (45 Beobachter) | 70 | 4 | native ×5 | Meer |
| 14 | *Cyclichthys orbicularis* (39 Beobachter) | 70 | 2 | native ×2 | Meer |
| 15 | *Pteropterus antennatus* (29 Beobachter) | 69 | 4 | native ×1 | Meer |
| 16 | *Chaetodon nigropunctatus* (39 Beobachter) | 68 | 18 | native ×5 | Meer |
| 17 | *Diodon holocanthus* (46 Beobachter) | 65 | 1 | native ×1 | Meer |
| 18 | *Cephalopholis hemistiktos* (31 Beobachter) | 64 | 15 | native ×5 | Meer |
| 19 | *Scarus persicus* (26 Beobachter) | 62 | 1 | native ×5 | Meer |
| 20 | *Gymnothorax nudivomer* (25 Beobachter) | 59 | – | native ×1 | Meer |
| 21 | *Diodon hystrix* (36 Beobachter) | 57 | 1 | native ×1 | Meer |
| 22 | *Eretmochelys imbricata* (44 Beobachter) | 57 | 182 | native ×4 | Brack/Meer |
| 23 | *Gymnothorax griseus* (24 Beobachter) | 57 | – | native ×1 | Meer |
| 24 | *Cheilinus lunulatus* (29 Beobachter) | 52 | 1 | native ×5 | Meer |
| 25 | *Dascyllus trimaculatus* (24 Beobachter) | 51 | 25 | native ×5 | Meer |
| 26 | *Rhinecanthus assasi* (36 Beobachter) | 50 | 8 | native ×5 | Meer |
| 27 | *Pomacanthus imperator* (27 Beobachter) | 46 | – | native ×1 | Meer |
| 28 | *Thalassoma lunare* (23 Beobachter) | 46 | 4 | native ×5 | Meer |
| 29 | *Terapon jarbua* (39 Beobachter) | 44 | 13 | native ×5 | Süß/Brack/Meer |
| 30 | *Odonus niger* (35 Beobachter) | 43 | 4 | native ×1 | Meer |
| 31 | *Flavocaranx bajad* (21 Beobachter) | 40 | 6 | native ×5 | Meer |
| 32 | *Heniochus acuminatus* (27 Beobachter) | 40 | 11 | native ×5 | Brack/Meer |
| 33 | *Zebrasoma xanthurum* (25 Beobachter) | 40 | 7 | native ×5 | Meer |
| 34 | *Monodactylus argenteus* (26 Beobachter) | 38 | 1 | native ×2 | Süß/Brack/Meer |
| 35 | *Fistularia commersonii* (27 Beobachter) | 37 | 2 | native ×1 | Meer |
| 36 | *Pseudochromis aldabraensis* (20 Beobachter) | 37 | 30 | native ×5 | Meer |
| 37 | *Carcharhinus limbatus* (8 Beobachter) | 35 | 2 | native ×5 | Brack/Meer |
| 38 | *Parupeneus margaritatus* (21 Beobachter) | 34 | 28 | native ×5 | Meer |
| 39 | *Caretta caretta* (25 Beobachter) | 33 | 788 | native ×3 | Meer |
| 40 | *Epinephelus stoliczkae* (22 Beobachter) | 33 | 2 | native ×1 | Meer |
| 104 | *Rhincodon typus* (Highlight; 9 Beobachter) | 11 | 25 | native ×5 | Meer |
| – | *Dugong dugon* (Highlight) | – | – | native ×4 | Meer |
| – | *Mobula birostris* (Highlight) | – | – | native ×1 | Meer |
| 115 | *Amphiprion omanensis* (Highlight; 6 Beobachter) | 9 | 18 | native ×1 | Meer |
| – | *Megaptera novaeangliae* (Highlight) | – | – | native ×5 | Meer |

### Level 2 (60)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 41 | *Caesio varilineata* (20 Beobachter) | 32 | 8 | native ×5 | Meer |
| 42 | *Carcharhinus melanopterus* (18 Beobachter) | 32 | 1 | native ×5 | Brack/Meer |
| 43 | *Labroides dimidiatus* (22 Beobachter) | 32 | 9 | native ×5 | Meer |
| 44 | *Octopus cyanea* (17 Beobachter) | 31 | – | native ×5 | Meer |
| 45 | *Chlorurus sordidus* (12 Beobachter) | 30 | – | native ×5 | Brack/Meer |
| 46 | *Cryptocentrus lutheri* (16 Beobachter) | 30 | 4 | native ×5 | Meer |
| 47 | *Lutjanus fulviflamma* (24 Beobachter) | 29 | 10 | native ×5 | Brack/Meer |
| 48 | *Chaetodon collare* (16 Beobachter) | 28 | 38 | native ×1 | Meer |
| 49 | *Diodon liturosus* (17 Beobachter) | 28 | – | native ×1 | Meer |
| 50 | *Ecsenius pulcher* (13 Beobachter) | 28 | 39 | native ×5 | Meer |
| 51 | *Arothron stellatus* (20 Beobachter) | 27 | 10 | native ×5 | Brack/Meer |
| 52 | *Pastinachus sephen* (18 Beobachter) | 26 | 2 | native ×5 | Süß/Brack/Meer |
| 53 | *Abudefduf sordidus* (15 Beobachter) | 24 | 2 | native ×1 | Brack/Meer |
| 54 | *Chanos chanos* (22 Beobachter) | 24 | 2 | native ×5 | Süß/Brack/Meer |
| 55 | *Platax teira* (15 Beobachter) | 24 | – | native ×5 | Meer |
| 56 | *Epinephelus coioides* (17 Beobachter) | 23 | 2 | native ×5 | Brack/Meer |
| 57 | *Pardachirus marmoratus* (11 Beobachter) | 23 | 2 | native ×5 | Meer |
| 58 | *Pterois miles* (12 Beobachter) | 23 | 5 | native ×5 | Meer |
| 59 | *Taeniurops meyeni* (13 Beobachter) | 23 | – | native ×5 | Meer |
| 60 | *Canthigaster valentini* (16 Beobachter) | 22 | 1 | native ×1 | Meer |
| 61 | *Chaetodon pictus* (13 Beobachter) | 22 | 2 | native ×1 | Meer |
| 62 | *Gerres longirostris* (18 Beobachter) | 22 | 1 | native ×5 | Süß/Brack/Meer |
| 63 | *Halichoeres marginatus* (6 Beobachter) | 22 | 4 | native ×5 | Meer |
| 64 | *Torpedo sinuspersici* (12 Beobachter) | 22 | 3 | native ×5 | Brack/Meer |
| 65 | *Sufflamen fraenatum* (19 Beobachter) | 21 | – | native ×1 | Meer |
| 66 | *Ostorhinchus aureus* (15 Beobachter) | 20 | 17 | native ×1 | Meer |
| 67 | *Pomacentrus leptus* (8 Beobachter) | 20 | 5 | native ×5 | Meer |
| 68 | *Scomberoides commersonnianus* (18 Beobachter) | 20 | – | native ×5 | Brack/Meer |
| 69 | *Stegostoma tigrinum* (15 Beobachter) | 20 | – | native ×5 | Brack/Meer |
| 70 | *Tylosurus choram* (14 Beobachter) | 20 | – | native ×1 | Meer |
| 71 | *Amblyeleotris periophthalmus* (9 Beobachter) | 19 | – | native ×5 | Meer |
| 72 | *Gymnomuraena zebra* (16 Beobachter) | 19 | 2 | native ×5 | Meer |
| 73 | *Parupeneus macronemus* (12 Beobachter) | 19 | 13 | native ×5 | Meer |
| 74 | *Rhizoprionodon acutus* (8 Beobachter) | 19 | 1 | native ×5 | Süß/Brack/Meer |
| 75 | *Sphyraena barracuda* (13 Beobachter) | 19 | 2 | native ×5 | Brack/Meer |
| 76 | *Tetrosomus gibbosus* (17 Beobachter) | 19 | 4 | native ×5 | Meer |
| 77 | *Istigobius ornatus* (12 Beobachter) | 18 | 9 | native ×2 | Brack/Meer |
| 78 | *Lutjanus ehrenbergii* (12 Beobachter) | 18 | 7 | native ×5 | Süß/Brack/Meer |
| 79 | *Platycephalus indicus* (14 Beobachter) | 18 | 10 | native ×5 | Brack/Meer |
| 80 | *Rhinoptera jayakari* (12 Beobachter) | 18 | 1 | native ×1 | Meer |
| 81 | *Carcharhinus sorrah* (5 Beobachter) | 17 | 21 | native ×5 | Brack/Meer |
| 82 | *Cirrhitichthys calliurus* (10 Beobachter) | 16 | 12 | native ×1 | Meer |
| 83 | *Plotosus lineatus* (16 Beobachter) | 16 | 6 | native ×5 | Brack/Meer |
| 84 | *Scuticaria tigrina* (11 Beobachter) | 16 | – | native ×1 | Meer |
| 85 | *Antennablennius adenensis* (4 Beobachter) | 15 | – | native ×5 | Meer |
| 86 | *Gymnothorax pictus* (10 Beobachter) | 15 | 26 | native ×1 | Brack/Meer |
| 87 | *Maculabatis randalli* (13 Beobachter) | 15 | 3 | native ×3 | Meer |
| 88 | *Sphyrna mokarran* (2 Beobachter) | 15 | 1 | native ×5 | Brack/Meer |
| 89 | *Aetobatus ocellatus* (10 Beobachter) | 14 | – | native ×1 | Brack/Meer |
| 90 | *Chromis xanthopterygia* (9 Beobachter) | 14 | 4 | native ×5 | Meer |
| 91 | *Carcharhinus dussumieri* (4 Beobachter) | 13 | 10 | native ×5 | Meer |
| 92 | *Scarus ferrugineus* (9 Beobachter) | 13 | – | native ×5 | Meer |
| 93 | *Scomberomorus commerson* (10 Beobachter) | 13 | 4 | native ×5 | Meer |
| 94 | *Amblygobius albimaculatus* (10 Beobachter) | 12 | 6 | native ×5 | Brack/Meer |
| 95 | *Cheilodipterus persicus* (7 Beobachter) | 12 | 14 | native ×4 | Meer |
| 96 | *Cryptocentroides arabicus* (9 Beobachter) | 12 | 3 | native ×1 | Meer |
| 97 | *Diplodus kotschyi* (10 Beobachter) | 12 | 2 | native ×5 | Meer |
| 98 | *Himantura uarnak* (9 Beobachter) | 12 | 5 | native ×5 | Brack/Meer |
| 99 | *Rhabdosargus sarba* (10 Beobachter) | 12 | 4 | native ×5 | Brack/Meer |
| 100 | *Scolopsis taeniata* (11 Beobachter) | 12 | 4 | native ×5 | Meer |

### Level 3 (50)

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser |
|---|---|---|---|---|---|
| 101 | *Zanclus cornutus* | 12 | 2 | native ×1 | Meer |
| 102 | *Acanthopagrus berda* | 11 | 5 | native ×5 | Süß/Brack/Meer |
| 103 | *Hippocampus kuda* | 11 | – | native ×5 | Brack/Meer |
| 105 | *Sepioteuthis lessoniana* | 11 | – | native ×4 | Brack/Meer |
| 106 | *Siganus javus* | 11 | – | native ×5 | Brack/Meer |
| 107 | *Siganus sutor* | 11 | – | – | Brack/Meer |
| 108 | *Canthigaster petersii* | 10 | 4 | native ×1 | Meer |
| 109 | *Chaetodon gardineri* | 10 | 4 | native ×5 | Meer |
| 110 | *Euthynnus affinis* | 10 | 2 | native ×5 | Meer |
| 111 | *Istiblennius pox* | 10 | 14 | native ×5 | Meer |
| 112 | *Taeniura lymma* | 10 | – | native ×5 | Meer |
| 113 | *Valenciennea sexguttata* | 10 | 1 | native ×5 | Meer |
| 114 | *Amblyeleotris triguttata* | 9 | – | native ×1 | Meer |
| 116 | *Argonauta hians* | 9 | 1 | native ×1 | Meer |
| 117 | *Arothron immaculatus* | 9 | – | native ×1 | Brack/Meer |
| 118 | *Carcharhinus brevipinna* | 9 | – | native ×1 | Meer |
| 119 | *Eviota punyit* | 9 | – | native ×1 | Meer |
| 120 | *Istigobius decoratus* | 9 | 29 | native ×4 | Meer |
| 121 | *Scarus ghobban* | 9 | 2 | native ×5 | Brack/Meer |
| 122 | *Bothus pantherinus* | 8 | 2 | native ×5 | Meer |
| 123 | *Caranx sexfasciatus* | 8 | – | native ×5 | Süß/Brack/Meer |
| 124 | *Cyclichthys spilostylus* | 8 | – | native ×1 | Meer |
| 125 | *Glaucostegus halavi* | 8 | – | native ×1 | Meer |
| 126 | *Gnathanodon speciosus* | 8 | 3 | native ×5 | Meer |
| 127 | *Hemipristis elongata* | 8 | – | native ×5 | Meer |
| 128 | *Mulloidichthys vanicolensis* | 8 | 6 | native ×1 | Meer |
| 129 | *Omobranchus fasciolatus* | 8 | 2 | native ×5 | Meer |
| 130 | *Platax orbicularis* | 8 | – | native ×5 | Brack/Meer |
| 131 | *Pseudochromis persicus* | 8 | 6 | native ×5 | Meer |
| 132 | *Selar crumenophthalmus* | 8 | 12 | native ×5 | Meer |
| 133 | *Trachyrhamphus bicoarctatus* | 8 | 1 | native ×5 | Meer |
| 134 | *Aluterus scriptus* | 7 | – | native ×1 | Meer |
| 135 | *Apogonichthyoides taeniatus* | 7 | 15 | native ×5 | Meer |
| 136 | *Cirrhitus spilotoceps* | 7 | – | native ×1 | Meer |
| 137 | *Echidna nebulosa* | 7 | – | native ×5 | Meer |
| 138 | *Gerres oyena* | 7 | 7 | native ×5 | Brack/Meer |
| 139 | *Hippocampus kelloggi* | 7 | – | native ×1 | Meer |
| 140 | *Loxodon macrorhinus* | 7 | – | native ×1 | Meer |
| 141 | *Scolopsis curite* | 7 | – | native ×5 | Meer |
| 142 | *Upeneus oligospilus* | 7 | 1 | native ×3 | Meer |
| 143 | *Ablennes hians* | 6 | 3 | native ×5 | Brack/Meer |
| 144 | *Aetomylaeus wafickii* | 6 | 1 | native ×1 | Meer |
| 145 | *Carcharhinus amboinensis* | 6 | – | native ×5 | Brack/Meer |
| 146 | *Cheilodipterus novemstriatus* | 6 | 9 | native ×5 | Meer |
| 147 | *Coris formosa* | 6 | 3 | native ×1 | Meer |
| 148 | *Echeneis naucrates* | 6 | 17 | native ×5 | Brack/Meer |
| 149 | *Gymnura poecilura* | 6 | 2 | native ×5 | Meer |
| 150 | *Istiblennius edentulus* | 6 | 3 | native ×1 | Brack/Meer |
| 151 | *Lutjanus indicus* | 6 | – | native ×2 | Süß/Brack/Meer |
| 152 | *Lutjanus sapphirolineatus* | 6 | – | native ×1 | Meer |

## Grenzfälle

Je 10 Arten vor und nach jeder Level-Grenze, in der Reihenfolge, in der die Levels sie nehmen (Highlights ab Level 2 übersprungen).

### Level 1/2

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 31 | *Flavocaranx bajad* (21 Beobachter) | 40 | 6 | native ×5 | Meer | 1 |
| 32 | *Heniochus acuminatus* (27 Beobachter) | 40 | 11 | native ×5 | Brack/Meer | 1 |
| 33 | *Zebrasoma xanthurum* (25 Beobachter) | 40 | 7 | native ×5 | Meer | 1 |
| 34 | *Monodactylus argenteus* (26 Beobachter) | 38 | 1 | native ×2 | Süß/Brack/Meer | 1 |
| 35 | *Fistularia commersonii* (27 Beobachter) | 37 | 2 | native ×1 | Meer | 1 |
| 36 | *Pseudochromis aldabraensis* (20 Beobachter) | 37 | 30 | native ×5 | Meer | 1 |
| 37 | *Carcharhinus limbatus* (8 Beobachter) | 35 | 2 | native ×5 | Brack/Meer | 1 |
| 38 | *Parupeneus margaritatus* (21 Beobachter) | 34 | 28 | native ×5 | Meer | 1 |
| 39 | *Caretta caretta* (25 Beobachter) | 33 | 788 | native ×3 | Meer | 1 |
| 40 | *Epinephelus stoliczkae* (22 Beobachter) | 33 | 2 | native ×1 | Meer | 1 |
| | **Grenze** | | | | | |
| 41 | *Caesio varilineata* (20 Beobachter) | 32 | 8 | native ×5 | Meer | 2 |
| 42 | *Carcharhinus melanopterus* (18 Beobachter) | 32 | 1 | native ×5 | Brack/Meer | 2 |
| 43 | *Labroides dimidiatus* (22 Beobachter) | 32 | 9 | native ×5 | Meer | 2 |
| 44 | *Octopus cyanea* (17 Beobachter) | 31 | – | native ×5 | Meer | 2 |
| 45 | *Chlorurus sordidus* (12 Beobachter) | 30 | – | native ×5 | Brack/Meer | 2 |
| 46 | *Cryptocentrus lutheri* (16 Beobachter) | 30 | 4 | native ×5 | Meer | 2 |
| 47 | *Lutjanus fulviflamma* (24 Beobachter) | 29 | 10 | native ×5 | Brack/Meer | 2 |
| 48 | *Chaetodon collare* (16 Beobachter) | 28 | 38 | native ×1 | Meer | 2 |
| 49 | *Diodon liturosus* (17 Beobachter) | 28 | – | native ×1 | Meer | 2 |
| 50 | *Ecsenius pulcher* (13 Beobachter) | 28 | 39 | native ×5 | Meer | 2 |

### Level 2/3

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 91 | *Carcharhinus dussumieri* (4 Beobachter) | 13 | 10 | native ×5 | Meer | 2 |
| 92 | *Scarus ferrugineus* (9 Beobachter) | 13 | – | native ×5 | Meer | 2 |
| 93 | *Scomberomorus commerson* (10 Beobachter) | 13 | 4 | native ×5 | Meer | 2 |
| 94 | *Amblygobius albimaculatus* (10 Beobachter) | 12 | 6 | native ×5 | Brack/Meer | 2 |
| 95 | *Cheilodipterus persicus* (7 Beobachter) | 12 | 14 | native ×4 | Meer | 2 |
| 96 | *Cryptocentroides arabicus* (9 Beobachter) | 12 | 3 | native ×1 | Meer | 2 |
| 97 | *Diplodus kotschyi* (10 Beobachter) | 12 | 2 | native ×5 | Meer | 2 |
| 98 | *Himantura uarnak* (9 Beobachter) | 12 | 5 | native ×5 | Brack/Meer | 2 |
| 99 | *Rhabdosargus sarba* (10 Beobachter) | 12 | 4 | native ×5 | Brack/Meer | 2 |
| 100 | *Scolopsis taeniata* (11 Beobachter) | 12 | 4 | native ×5 | Meer | 2 |
| | **Grenze** | | | | | |
| 101 | *Zanclus cornutus* | 12 | 2 | native ×1 | Meer | 3 |
| 102 | *Acanthopagrus berda* | 11 | 5 | native ×5 | Süß/Brack/Meer | 3 |
| 103 | *Hippocampus kuda* | 11 | – | native ×5 | Brack/Meer | 3 |
| 105 | *Sepioteuthis lessoniana* | 11 | – | native ×4 | Brack/Meer | 3 |
| 106 | *Siganus javus* | 11 | – | native ×5 | Brack/Meer | 3 |
| 107 | *Siganus sutor* | 11 | – | – | Brack/Meer | 3 |
| 108 | *Canthigaster petersii* | 10 | 4 | native ×1 | Meer | 3 |
| 109 | *Chaetodon gardineri* | 10 | 4 | native ×5 | Meer | 3 |
| 110 | *Euthynnus affinis* | 10 | 2 | native ×5 | Meer | 3 |
| 111 | *Istiblennius pox* | 10 | 14 | native ×5 | Meer | 3 |

### Level 3/nicht im Deck

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Level |
|---|---|---|---|---|---|---|
| 143 | *Ablennes hians* | 6 | 3 | native ×5 | Brack/Meer | 3 |
| 144 | *Aetomylaeus wafickii* | 6 | 1 | native ×1 | Meer | 3 |
| 145 | *Carcharhinus amboinensis* | 6 | – | native ×5 | Brack/Meer | 3 |
| 146 | *Cheilodipterus novemstriatus* | 6 | 9 | native ×5 | Meer | 3 |
| 147 | *Coris formosa* | 6 | 3 | native ×1 | Meer | 3 |
| 148 | *Echeneis naucrates* | 6 | 17 | native ×5 | Brack/Meer | 3 |
| 149 | *Gymnura poecilura* | 6 | 2 | native ×5 | Meer | 3 |
| 150 | *Istiblennius edentulus* | 6 | 3 | native ×1 | Brack/Meer | 3 |
| 151 | *Lutjanus indicus* | 6 | – | native ×2 | Süß/Brack/Meer | 3 |
| 152 | *Lutjanus sapphirolineatus* | 6 | – | native ×1 | Meer | 3 |
| | **Grenze** | | | | | |
| 153 | *Mulloidichthys flavolineatus* (Quelle: *Mulloidichthys flavicaudus*) | 6 | – | native ×5 | Meer | – |
| 154 | *Neopomacentrus cyanomos* | 6 | 9 | native ×5 | Meer | – |
| 155 | *Neotrygon indica* | 6 | – | – | Meer | – |
| 156 | *Netuma bilineata* | 6 | 7 | native ×5 | Süß/Brack/Meer | – |
| 157 | *Parablennius pilicornis* | 6 | 1 | native ×1 | Meer | – |
| 158 | *Paragaleus longicaudatus* | 6 | 3 | native ×5 | Meer | – |
| 159 | *Pomacentrus arabicus* | 6 | 2 | native ×1 | Meer | – |
| 160 | *Pomadasys argenteus* | 6 | 2 | native ×5 | Süß/Brack/Meer | – |
| 161 | *Rastrelliger kanagurta* | 6 | 6 | native ×5 | Meer | – |
| 162 | *Rhynchobatus djiddensis* | 6 | – | native ×5 | Brack/Meer | – |

## Abgleich mit Führern

Das Rezept nennt keinen Führer.
## Änderungen gegenüber dem bestehenden Deck

- neu: 0
- entfallen: 0

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
| *Halichoeres dussumieri* | 3 | Meer | zu wenige Nachweise (3 < 5) |
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
| *Apogonichthyoides enigmaticus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
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
| *Umbrina robinsoni* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Upeneus guttatus* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Upeneus heemstra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Upeneus sulphureus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |

</details>

## Subdeck `invertebrates` (40)

Eigene Taxa, Größe und Filter, Reihenfolge-Quelle und Region des Rezepts. Arten, die schon in einem Level oder einem früheren Subdeck stehen, bleiben draußen; die Führer werden nicht abgeglichen.

- iNaturalist: 533 Taxa (Seiten: 2)
- OBIS: 2874 Arten mit Nachweisen außer iNaturalist

### iNaturalist-Namen zugeordnet

Laut `recipes/inat_names.json`: iNaturalist nennt die Art anders als die Referenz-DB; die Zählung kommt zu der der Referenz-DB-Art.

| iNaturalist | Referenz-DB | iNat | Art | Beleg |
|---|---|---|---|---|
| *Pinnoctopus ornatus* | *Callistoctopus ornatus* | 3 | Umbenennung | https://www.inaturalist.org/taxon_changes/172615 |
| *Pinnoctopus luteus* | *Callistoctopus luteus* | 1 | Umbenennung | https://www.inaturalist.org/taxon_changes/172616 |

### Von Hand ausgeschlossen

| Art | iNat | Grund |
|---|---|---|
| *Metopograpsus messor* | 103 | Uferkrabbe der Mangroven und Felsküste, lebt in der Gezeitenzone über dem Wasser. |
| *Cardites bicolor* | 99 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 7 von 7 Beobachtungen mit Angabe „tot“). |
| *Coenobita scaevola* | 80 | Landeinsiedlerkrebs, lebt an Land und geht nur zur Eiablage ans Meer. |
| *Oliva bulbosa* | 74 | Fast nur als leere Schale am Strand beobachtet (iNaturalist: 16 von 17 Beobachtungen mit Angabe „tot“). |
| *Portunus pelagicus* | 72 | Schwimmkrabbe der Lagunen und Flussmündungen, vor allem als Fang auf Märkten beobachtet. |
| *Grapsus albolineatus* | 70 | Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen. |
| *Eurycarcinus orientalis* | 53 | Krabbe der Mangroven und Gezeitenzone, lebt bei Ebbe über dem Wasser. |
| *Ocypode rotundata* | 53 | Geisterkrabbe, lebt am trockenen Sandstrand. |
| *Acanthopleura vaillantii* | 52 | Käferschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Amphibalanus amphitrite* | 33 | Seepocke der Gezeitenzone, sitzt an Hafenmauern und Mangrovenwurzeln. |
| *Ocypode saratan* | 29 | Geisterkrabbe, lebt am trockenen Sandstrand. |
| *Scylla serrata* | 29 | Mangrovenkrabbe, lebt in Mangroven und Schlick, vor allem als Fang auf Märkten beobachtet. |
| *Portunus segnis* | 24 | Schwimmkrabbe der Lagunen und Flussmündungen, vor allem als Fang auf Märkten beobachtet. |
| *Porcellio evansi* | 20 | Landassel, kein Meerestier. |
| *Cellana karachiensis* | 15 | Napfschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser. |
| *Gelasimus hesperiae* | 14 | Winkerkrabbe des Schlickwatts, lebt bei Ebbe an Land. |
| *Terebralia palustris* | 13 | Mangrovenschnecke, lebt auf dem Schlick der Mangroven. |

### Highlights

| Highlight | Begründung | Rang | Belege | Status |
|---|---|---|---|---|
| *Acanthaster planci* | Die Dornenkrone frisst Korallen; ihre Massenvermehrungen zerstören ganze Riffe, und ihre Stacheln sind giftig. | 55 | Reihenfolge-Quelle, OBIS, Verbreitung | invertebrates |
| *Toxopneustes pileolus* | Der Blumenseeigel trägt zwischen den Stacheln giftige Greifzangen, die zu den gefährlichsten des Meeres zählen. | 30 | Reihenfolge-Quelle, Verbreitung | invertebrates |
| *Stenopus hispidus* | Die Gebänderte Scherengarnele putzt Fische vor ihrer Höhle und ist eine der auffälligsten Garnelen des Riffs. | 41 | Reihenfolge-Quelle, OBIS, Verbreitung | invertebrates |

### Prüfung

- Nachweis aus zwei unabhängigen Quellen (Reihenfolge-Quelle und OBIS ohne iNaturalist oder Verbreitung): 39/40 (98 %)
- Endemisch in einer Rezept-Region laut FishBase/SeaLifeBase: 0
- Arten ohne Volksnamen `de` in der Referenz-DB: 31/40 (78 %)
- Arten ohne Volksnamen `en` in der Referenz-DB: 7/40 (18 %)
- Familien ohne Volksnamen `de`: 33/33 (100 %): *Acanthasteridae*, *Actiniidae*, *Arcidae*, *Asterinidae*, *Astriclypeidae*, *Astropectinidae*, *Cassiopeidae*, *Catostylidae*, *Cepheidae*, *Chromodorididae*, *Clypeasteridae*, *Conidae*, *Cypraeidae*, *Diadematidae*, *Diogenidae*, *Discodorididae*, *Echinometridae*, *Facelinidae*, *Gymnodorididae*, *Holothuriidae*, *Muricidae*, *Ophiocomidae*, *Oreasteridae*, *Palinuridae*, *Psammobiidae*, *Stenopodidae*, *Strombidae*, *Synaptidae*, *Thoridae*, *Toxopneustidae*, *Trochidae*, *Turbinidae*, *Zoanthidae*
- Familien ohne Volksnamen `en`: 20/33 (61 %): *Actiniidae*, *Arcidae*, *Astriclypeidae*, *Astropectinidae*, *Cassiopeidae*, *Catostylidae*, *Cepheidae*, *Chromodorididae*, *Clypeasteridae*, *Diadematidae*, *Discodorididae*, *Echinometridae*, *Facelinidae*, *Gymnodorididae*, *Ophiocomidae*, *Oreasteridae*, *Synaptidae*, *Thoridae*, *Toxopneustidae*, *Zoanthidae*

Volksnamen wie die App sie wählt (ohne Landesbezug; zur Laufzeit kann die App Namen aus iNaturalist ergänzen). Im Lernmodus Familie fragt die App den Familiennamen ab und fällt ohne Namen in der App-Sprache auf Englisch, dann auf den wissenschaftlichen Namen zurück.

**Arten ohne zweite, unabhängige Quelle:**

- *Cotylorhiza erythraea*: Reihenfolge-Quelle

**Eine Art unter zwei Einträgen?** Deck-Arten mit gleichem Volksnamen oder gemeinsamem wissenschaftlichem Namen:

- gleicher Volksname `en` „Echinoid“: *Clypeaster humilis*, *Sculpsitechinus auritus*

### Arten

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Klasse |
|---|---|---|---|---|---|---|
| 1 | *Hypselodoris pulchella* | 65 | 28 | native ×2 | Meer | Gastropoda |
| 2 | *Catostylus perezi* | 48 | – | native ×5 | Meer | Scyphozoa |
| 3 | *Goniobranchus annulatus* | 40 | 22 | native ×1 | Meer | Gastropoda |
| 4 | *Diadema setosum* | 38 | 15 | native ×4 | Meer | Echinoidea |
| 5 | *Conomurex persicus* | 37 | 17 | native ×5 | Meer | Gastropoda |
| 6 | *Astropecten polyacanthus* | 36 | 1 | native ×2 | Meer | Asteroidea |
| 7 | *Cassiopea andromeda* | 35 | 1 | native ×2 | Meer | Scyphozoa |
| 8 | *Culcita coriacea* | 35 | – | native ×1 | Meer | Asteroidea |
| 9 | *Cotylorhiza erythraea* | 22 | – | – | Meer | Scyphozoa |
| 10 | *Entacmaea quadricolor* | 21 | 7 | native ×1 | Meer | Hexacorallia |
| 11 | *Panulirus versicolor* | 21 | 5 | native ×5 | Meer | Malacostraca |
| 12 | *Aquilonastra iranica* | 20 | 5 | native ×1 | Meer | Asteroidea |
| 13 | *Caloria indica* | 20 | 9 | – | Meer | Gastropoda |
| 14 | *Dardanus tinctor* | 20 | 12 | native ×4 | Meer | Malacostraca |
| 15 | *Conus textile* | 18 | 11 | – | Meer | Gastropoda |
| 16 | *Echinometra mathaei* | 18 | 7 | native ×4 | Meer | Echinoidea |
| 17 | *Jorunna funebris* | 18 | 10 | native ×2 | Meer | Gastropoda |
| 18 | *Mauritia grayana* | 18 | 32 | native ×1 | Meer | Gastropoda |
| 19 | *Clypeaster humilis* | 17 | 4 | native ×3 | Meer | Echinoidea |
| 20 | *Goniobranchus obsoletus* | 17 | 3 | – | Meer | Gastropoda |
| 21 | *Thor amboinensis* | 17 | 5 | native ×2 | Meer | Malacostraca |
| 22 | *Asaphis violascens* | 16 | 3 | native ×5 | Brack/Meer | Bivalvia |
| 23 | *Hexaplex kuesterianus* | 16 | 25 | native ×4 | Meer | Gastropoda |
| 24 | *Hypselodoris dollfusi* | 16 | 14 | native ×2 | Meer | Gastropoda |
| 25 | *Hypselodoris nigrostriata* | 16 | 14 | native ×1 | Meer | Gastropoda |
| 26 | *Clanculus pharaonius* | 15 | 16 | native ×5 | Meer | Gastropoda |
| 27 | *Holothuria atra* | 15 | 6 | native ×4 | Meer | Holothuroidea |
| 28 | *Holothuria leucospilota* | 15 | 8 | native ×2 | Meer | Holothuroidea |
| 29 | *Lunella coronata* | 15 | 18 | native ×5 | Meer | Gastropoda |
| 30 | *Toxopneustes pileolus* (Highlight; 9 Beobachter) | 15 | – | native ×1 | Meer | Echinoidea |
| 31 | *Sculpsitechinus auritus* | 14 | 4 | native ×3 | Meer | Echinoidea |
| 32 | *Clibanarius signatus* | 13 | 17 | native ×2 | Meer | Malacostraca |
| 33 | *Euapta godeffroyi* | 13 | 8 | native ×1 | Meer | Holothuroidea |
| 34 | *Gymnodoris impudica* | 13 | 5 | – | Meer | Gastropoda |
| 35 | *Zoanthus sansibaricus* | 13 | 6 | – | Meer | Hexacorallia |
| 36 | *Barbatia setigera* | 12 | 11 | native ×4 | Meer | Bivalvia |
| 37 | *Hypselodoris infucata* | 12 | 16 | native ×3 | Meer | Gastropoda |
| 38 | *Ophiocoma scolopendrina* | 12 | 7 | native ×1 | Meer | Ophiuroidea |
| 41 | *Stenopus hispidus* (Highlight; 10 Beobachter) | 12 | 1 | native ×1 | Meer | Malacostraca |
| 55 | *Acanthaster planci* (Highlight; 7 Beobachter) | 8 | 32 | native ×2 | Meer | Asteroidea |

### Grenzfälle

Je 10 Arten vor und nach der Grenze (Highlights übersprungen).

| Rang | Art | iNat | OBIS ohne iNat | FishBase/SLB im Gebiet | Wasser | Klasse | Im Subdeck |
|---|---|---|---|---|---|---|---|
| 28 | *Holothuria leucospilota* | 15 | 8 | native ×2 | Meer | Holothuroidea | ja |
| 29 | *Lunella coronata* | 15 | 18 | native ×5 | Meer | Gastropoda | ja |
| 31 | *Sculpsitechinus auritus* | 14 | 4 | native ×3 | Meer | Echinoidea | ja |
| 32 | *Clibanarius signatus* | 13 | 17 | native ×2 | Meer | Malacostraca | ja |
| 33 | *Euapta godeffroyi* | 13 | 8 | native ×1 | Meer | Holothuroidea | ja |
| 34 | *Gymnodoris impudica* | 13 | 5 | – | Meer | Gastropoda | ja |
| 35 | *Zoanthus sansibaricus* | 13 | 6 | – | Meer | Hexacorallia | ja |
| 36 | *Barbatia setigera* | 12 | 11 | native ×4 | Meer | Bivalvia | ja |
| 37 | *Hypselodoris infucata* | 12 | 16 | native ×3 | Meer | Gastropoda | ja |
| 38 | *Ophiocoma scolopendrina* | 12 | 7 | native ×1 | Meer | Ophiuroidea | ja |
| | **Grenze** | | | | | | |
| 39 | *Petrolisthes rufescens* | 12 | 15 | native ×5 | Meer | ? | nein |
| 40 | *Pinctada radiata* | 12 | 17 | native ×4 | Meer | ? | nein |
| 42 | *Linckia multifora* | 11 | 11 | native ×3 | Meer | ? | nein |
| 43 | *Ceratosoma gracillimum* | 10 | – | – | Meer | ? | nein |
| 44 | *Clibanarius longitarsus* | 10 | 3 | native ×2 | Brack/Meer | ? | nein |
| 45 | *Conus betulinus* | 10 | 1 | – | Meer | ? | nein |
| 46 | *Eriphia smithii* | 10 | 40 | native ×2 | Meer | ? | nein |
| 47 | *Chelonibia testudinaria* | 9 | – | – | Meer | ? | nein |
| 48 | *Conus coronatus* (Quelle: *Conus aristophanes*) | 9 | 4 | – | Meer | ? | nein |
| 49 | *Goniobranchus tinctorius* | 9 | 6 | – | Meer | ? | nein |

### Ausgeschlossene Kandidaten

<details><summary>319 Arten</summary>

| Art | iNat | Wasser | Grund |
|---|---|---|---|
| *Metopograpsus messor* | 103 | Brack/Meer | von Hand ausgeschlossen (Uferkrabbe der Mangroven und Felsküste, lebt in der Gezeitenzone über dem Wasser.) |
| *Cardites bicolor* | 99 | Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 7 von 7 Beobachtungen mit Angabe „tot“).) |
| *Acanthosepion pharaonis* | 85 | Meer | schon in einem anderen Subdeck (level-1) |
| *Coenobita scaevola* | 80 | Meer | von Hand ausgeschlossen (Landeinsiedlerkrebs, lebt an Land und geht nur zur Eiablage ans Meer.) |
| *Oliva bulbosa* | 74 | Meer | von Hand ausgeschlossen (Fast nur als leere Schale am Strand beobachtet (iNaturalist: 16 von 17 Beobachtungen mit Angabe „tot“).) |
| *Portunus pelagicus* | 72 | Brack/Meer | von Hand ausgeschlossen (Schwimmkrabbe der Lagunen und Flussmündungen, vor allem als Fang auf Märkten beobachtet.) |
| *Grapsus albolineatus* | 70 | Meer | von Hand ausgeschlossen (Felsenkrabbe der Spritzwasserzone, läuft über dem Wasser auf den Uferfelsen.) |
| *Eurycarcinus orientalis* | 53 | Brack/Meer | von Hand ausgeschlossen (Krabbe der Mangroven und Gezeitenzone, lebt bei Ebbe über dem Wasser.) |
| *Ocypode rotundata* | 53 | Meer | von Hand ausgeschlossen (Geisterkrabbe, lebt am trockenen Sandstrand.) |
| *Acanthopleura vaillantii* | 52 | Meer | von Hand ausgeschlossen (Käferschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Amphibalanus amphitrite* | 33 | Brack/Meer | von Hand ausgeschlossen (Seepocke der Gezeitenzone, sitzt an Hafenmauern und Mangrovenwurzeln.) |
| *Octopus cyanea* | 31 | Meer | schon in einem anderen Subdeck (level-2) |
| *Ocypode saratan* | 29 | Meer | von Hand ausgeschlossen (Geisterkrabbe, lebt am trockenen Sandstrand.) |
| *Scylla serrata* | 29 | Brack/Meer | von Hand ausgeschlossen (Mangrovenkrabbe, lebt in Mangroven und Schlick, vor allem als Fang auf Märkten beobachtet.) |
| *Portunus segnis* | 24 | Meer | von Hand ausgeschlossen (Schwimmkrabbe der Lagunen und Flussmündungen, vor allem als Fang auf Märkten beobachtet.) |
| *Porcellio evansi* | 20 | ? | von Hand ausgeschlossen (Landassel, kein Meerestier.) |
| *Cellana karachiensis* | 15 | Meer | von Hand ausgeschlossen (Napfschnecke der Felsküste, sitzt in der Gezeitenzone über dem Wasser.) |
| *Gelasimus hesperiae* | 14 | Brack/Meer | von Hand ausgeschlossen (Winkerkrabbe des Schlickwatts, lebt bei Ebbe an Land.) |
| *Terebralia palustris* | 13 | Brack/Meer | von Hand ausgeschlossen (Mangrovenschnecke, lebt auf dem Schlick der Mangroven.) |
| *Austruca iranica* | 11 | Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Sepioteuthis lessoniana* | 11 | Brack/Meer | schon in einem anderen Subdeck (level-3) |
| *Argonauta hians* | 9 | Meer | schon in einem anderen Subdeck (level-3) |
| *Melanoides tuberculata* | 6 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Anadara ehrenbergi* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Balanus trigonus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Bullia mauritiana* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Calappa hepatica* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Catostylus mosaicus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Ceratosoma trilobatum* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Erronea caurica* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Glycymeris arabica* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Goniobranchus setoensis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Halocynthia spinosa* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hiatula rosea* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Hydatina physis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Lepas anserifera* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Murex scolopax* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Nerita textilis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Parasesarma persicum* | 4 | Brack/Meer | zu wenige Nachweise (4 < 5) |
| *Pinna bicolor* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Pyura gangelion* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Rapana rapiformis* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Trapezia cymodoce* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Tubastraea diaphana* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Turbo radiatus* | 4 | Meer | zu wenige Nachweise (4 < 5) |
| *Alpheus djiboutensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Amphioctopus aegina* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Aquilonastra burtoni* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Aquilonastra watersi* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Astropecten indicus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Calcinus latens* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Callistoctopus ornatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cardisoma carnifex* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Carpilius convexus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Chrysaora chinensis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Circenita callipyga* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Conus tessulatus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cuapetes tenuipes* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Cucullaea labiata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Lyncina carneola* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Grapsus granulosus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Gyractis sesere* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Hastula hectica* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Holothuria hilla* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Monetaria annulus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Glyphepithema alapapilionis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Ovula ovum* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Palythoa mutuki* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Physalia utriculus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pleurobranchus grandis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Pocillopora damicornis* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Polinices mammilla* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Proporcellio vulcanius* | 3 | ? | zu wenige Nachweise (3 < 5) |
| *Saccostrea cuccullata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Salmacis bicolor* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Scyllarides squammosus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Trapania aurata* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Tubastraea micranthus* | 3 | Meer | zu wenige Nachweise (3 < 5) |
| *Acropora downingi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Actinopyga mauritiana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anachis fauroti* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Anadara uropigimelana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Atergatis integerrimus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Barbatia obliquata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Bulla arabica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cadlinella ornatissima* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Calcinus rosaceus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Callyspongia biru* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cherax quadricarinatus* | 2 | Süß/Brack | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Chromodoris hamiltoni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Cladopsammia gracilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Clathrina maremeccae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Clibanarius rhabdodactylus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Clypeomorus bifasciata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus ardisiaceus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus frigidus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Conus melvilli* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Culcita schmideliana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Dardanus woodmasoni* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Donax scalpellum* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Elysia marginata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Engina mendicaria* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Etisus laevimanus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fromia indica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fulvia fragilis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Fusinus arabicus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Glycymeris livida* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Goniobranchus alius* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Gymnodoris ceylonica* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Heliacus variegatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Herdmania momus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Heterocentrotus mamillatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Leiaster speciosus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Leptastrea purpurea* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Linckia laevigata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lissocarcinus orbicularis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Lomanotus vermiformis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Luidia maculata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Luria pulchra* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Megalactis hemprichi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Mithrodia clavigera* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Monetaria caputserpentis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Monoplex pilearis* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Nerita sanguinolenta* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Paratapes textile* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Petrolisthes leptocheles* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Phestilla lugubris* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pilumnus vespertilio* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Pinna muricata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Portunus sanguinolentus* | 2 | Brack/Meer | zu wenige Nachweise (2 < 5) |
| *Punctacteon eloiseae* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Saron neglectus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Siderastrea savignyana* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Siphonaria belcheri* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tanea lineata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Trapania scurra* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Turritella maculata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Tylothais savignyi* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Vasticardium assimile* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Xenocarcinus tuberculatus* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Xenophora corrugata* | 2 | Meer | zu wenige Nachweise (2 < 5) |
| *Acanthaster mauritiensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Agabiformius obtusus* | 1 | ? | zu wenige Nachweise (1 < 5) |
| *Alpheus djeddensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Alpheus ochrostriatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Amorphinopsis excavans* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ancilla ovalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Arca navicularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Arcuatula senhousia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ardeadoris symmetrica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Artemia salina* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Asteronotus cespitosus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Asteronotus hepaticus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Astropecten pugnax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Atagema spongiosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Atergatis floridus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Atergatis roseus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Atrina vexillum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Berthellina citrina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Biemna fistulosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Boloceroides mcmurrichi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Botrylloides niger* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bufonaria echinata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bulbaeolidia alba* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Bulla ampulla* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Calappa lophos* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Callistoctopus luteus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Cardita variegata* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Ceratosoma tenue* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chama pacifica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Charybdis annulata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Charybdis feriata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Charybdis smithii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chelidonura punctata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chondrosia corticata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chromodoris quadricolor* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Chthamalus barnesi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Clibanarius striolatus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Clibanarius virescens* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus pennaceus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus striatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus taeniatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Conus vexillum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Corbula sulculosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mauritia mauritiana* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dardanus lagopodes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dardanus pedunculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dasycaris zanzibarica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dendrodoris coronata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dendrodoris nigra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dentalium octangulatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Didemnum membranaceum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Diminovula aurantiomacula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dipsastraea lacuna* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dofleinia armata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Dosinia histrio* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Duncanopsammia peltata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echinophyllia aspera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Echinopora hirsutissima* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ergalatax junionae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Etisus splendidus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Favites pentagona* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Favorinus tsuruganus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Gafrarium pectinatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Geograpsus crinipes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Goniobranchus geminus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Goniodoridella savignyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Goniosupradens acutifrons* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Halgerda willeyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Haliclona caerulea* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Haloa pemphis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hamopontonia corallicola* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Heteractis aurora* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hexaplex rileyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hipponix ticaonicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria nobilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Holothuria scabra* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Homalocantha anatomica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hydatina zonata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hydra oligactis* | 1 | Süß/Meer | zu wenige Nachweise (1 < 5) |
| *Hymenocera picta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Hypselodoris kanga* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Indothais lacera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lambis truncata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Leptodius exaratus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ligia exotica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Limacia langavi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lophozozymus pulchellus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lybia caestifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lydia tenax* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Lyncina vitellus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Malleus regula* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Melampus castaneus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Melicerona felina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mexichromis lemniscata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Microcyphus rousseaui* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Strigatella litterata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Modiolus auriculatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Morula aspera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Murex troscheli* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Muricodrupa anaxares* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mycale grandis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nassarius arcularia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Natica pulicaris* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nembrotha aurea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Neotrapezium sublaevigatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Nerita adenensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Niso venosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiactis savignyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiocoma erinaceus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiothela mirabilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ophiothela venusta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Palmadusta lentiginosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paracondylactis hertwigi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paraiptasia radiata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Paraxanthodes cumatodes* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Patiriella paradoxa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pavona varians* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Penaeus latisulcatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pennaria disticha* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Peronia peronii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Peronia verruculata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Petrolisthes boscii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phestilla melanobrachia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllacanthus imperialis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllidia varicosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Phyllognathia ceratophthalma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Physella acuta* | 1 | Süß | kein Meeresfisch (Saltwater nicht gesetzt) |
| *Pilumnus incanus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pilumnus propinquus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pirenella conica* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Placamen lamellatum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Platydoris formosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Platypodia pseudogranulosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pleurobranchus forskalii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plocamopherus ocellatus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Plocamopherus tilesii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Mammilla sebae* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Psammocora contigua* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pterelectroma physoides* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pupa affinis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Pupa sulcata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Purpuradusta gracilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Ranularia boschi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhodactis rhodostoma* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhynchocinetes brucei* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Rhynchocinetes durbanensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sabellastarte spectabilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sansibia claereboudti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Schizophrys aspera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Scutellastra flexuosa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Semicassis bisulcata* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Semiricinula tissoti* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sphaerechinus granularis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Spondylus exilis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stichodactyla tapetum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Stomatella impertusa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Styela canopus* | 1 | Brack/Meer | zu wenige Nachweise (1 < 5) |
| *Suberites aurantiacus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Sunetta effossa* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Taringa sublutea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tegula gallina* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Temnopleurus toreumaticus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Terebellum terebellum* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Terebra babylonia* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Terebra cingulifera* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thalamita savignyi* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thaumoctopus mimicus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Thenus orientalis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tibia curta* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Timoides agassizii* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Tonna dolium* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trapania japonica* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trapania naeva* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Trochus erithreus* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Turritella cochlea* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Verconia norba* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xanthias sinensis* | 1 | Meer | zu wenige Nachweise (1 < 5) |
| *Xenophora pallidula* | 1 | Meer | zu wenige Nachweise (1 < 5) |

</details>

### Nicht aufgelöste Namen

<details><summary>107 Namen</summary>

*Euryptyxis latireflexa* (71), *Polygyra cereolus* (71), *Naria turdus* (28), *Laevicaulis alte* (24), *Phyllidia rueppelii* (23), *Zootecus insularis* (22), *Austruca albimana* (21), *Caloria militaris* (15), *Thranita crenata* (13), *Laevicaulis haroldi* (11), *Rumina decollata* (11), *Vasticardium lacunosum* (10), *Cranuca inversa* (8), *Pupoides coenopictus* (8), *Babylonia valentiana* (7), *Pirenella cingulata* (7), *Plocamopherus margaretae* (7), *Coryphellina rubrolineata* (6), *Dendrodoris krusensternii* (6), *Hexabranchus lacer* (5), *Kabeiro rubroreticulata* (5), *Maoricardium pseudolima* (5), *Naria nebrites* (5), *Spirobranchus sinuspersicus* (5), *Tambja zulu* (5), *Bullia semiplicata* (4), *Dermatobranchus caeruleomaculatus* (4), *Laevicaulis stuhlmanni* (4), *Naria ocellata* (4), *Siphonaria asghar* (4), *Zoanthus vietnamensis* (4), *Echinolittorina omanensis* (3), *Haliclona qatari* (3), *Periscyphis omanensis* (3), *Pione mussae* (3), *Pirenella arabica* (3), *Pseudobiceros gloriosus* (3), *Rhyssoplax peregrina* (3), *Actinimenes ornatus* (2), *Arakawania granulata* (2), *Armadillidium vulgare* (2), *Austruca sindensis* (2), *Clathrina luteoculcitella* (2), *Cubaris murina* (2), *Cymatium ranzanii* (2), *Gelasimus tetragonon* (2), *Gelastocaris paronai* (2), *Hypselodoris ghardaqana* (2), *Hypselodoris rudmani* (2), *Lissachatina fulica* (2), *Maculastrombus mutabilis* (2), *Plesiastrea peroni* (2), *Psammotreta angulata* (2), *Pseudoceros scintillatus* (2), *Siliqua polita* (2), *Tanychlamys indica* (2), *Thranita prymna* (2), *Tivela stefaninii* (2), *Tylos maindroni* (2), *Aequorea* (1), *Allopeas gracile* (1), *Ancilla scaphella* (1), *Argulus* (1), *Aurelia dubia* (1), *Babylonia umbilifusca* (1), *Calappa dumortieri* (1), *Calcinus tropidomanus* (1), *Callyspongia siphonella* (1), *Cantharus tranquebaricus* (1), *Conus adenensis* (1), *Conus koukae* (1), *Conus quasimagnificus* (1), *Cornu aspersum* (1), *Costacallista erycina* (1), *Dermatobranchus tuberculatus* (1), *Diodora townsendi* (1), *Diogenes nitidimanus* (1), *Donax erythraeensis* (1), *Donax townsendi* (1), *Dulcerana granularis* (1), *Edwardsianthus pudicus* (1), *Exolaternula erythraea* (1), *Hexabranchus giganteus* (1), *Hypselodoris yarae* (1), *Iranopsis omanensis* (1), *Lissachatina immaculata* (1), *Mexichromis katalexis* (1), *Nerita lianae* (1), *Percnon sinense* (1), *Phenacovolva barbieri* (1), *Prionocidaris pistillaris* (1), *Pseudonapaeus jousseaumei* (1), *Radianthus crispa* (1), *Rochebrunia bentiana* (1), *Sagittalia brinkae* (1), *Samla bicolor* (1), *Scutellastra exusta* (1), *Sigatica pomatiella* (1), *Tenellia goniophaga* (1), *Tetraclita ehsani* (1), *Tivela mulawana* (1), *Tomoberthella martensi* (1), *Triops granarius* (1), *Trisidos torta* (1), *Trochita dhofarensis* (1), *Tutufa bardeyi* (1), *Xeroniscus siegfriedhuberi* (1)

</details>

## Nicht aufgelöste Namen der Reihenfolge-Quelle

Die Referenz-DB der App kennt diese Namen nicht; die App fände sie auch nicht.

| Name | iNat |
|---|---|
| *Pterygoplichthys* | 3 |
| *Valenciennea schlieweni* | 2 |
| *Priolepis zebra* | 1 |
