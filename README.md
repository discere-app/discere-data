# discere-data

Discere Data – zentralisierte Lern-Decks und Arteninformationen

Dieses Repository enthält strukturierte Biodiversitätsdaten für die Discere-App.
Ziel ist es, fertige Lern-Decks (Fische, Vögel, Pflanzen etc.) bereitzustellen, damit Nutzer nicht selbst Decks erstellen müssen.

Hinweis:

main Branch ist geschützt.
Änderungen bitte über Pull Requests.

## Neues Deck hinzufügen

Einfach eine neue JSON-Datei unter `data/decks/` anlegen und einen PR nach
`main` öffnen. Mehr ist nicht nötig - `data/decks/index.json` wird nicht von
Hand gepflegt.

```json
{
  "$schema": "../../schema/deck.schema.json",
  "name": "Kopffüßer",
  "description": "Kraken, Sepien und Kalmare",
  "imageUrl": "https://…",
  "sources": [{"name": "FishBase", "url": "https://www.fishbase.org/"}],
  "createdBy": "Dein Name",
  "speciesNames": ["Octopus vulgaris", "Sepia officinalis"]
}
```

### Format

Das Format ist als JSON Schema festgehalten:
[`schema/deck.schema.json`](schema/deck.schema.json). Mit der
`"$schema"`-Zeile oben vervollständigen und prüfen Editoren wie VS Code
schon beim Schreiben.

| Feld | Pflicht | Inhalt |
|---|---|---|
| `name` | ja | Name des Decks in der App |
| `description` | ja | Kurzbeschreibung, darf leer sein |
| `speciesNames` | ja | Wissenschaftliche Namen aller Arten, ohne Doppelte |
| `imageUrl` | nein | Titelbild (`http(s)://…`) oder leer |
| `sources` | nein | Datenquellen, je `name` und optional `url` |
| `createdBy` | nein | Wer das Deck erstellt hat |
| `formatVersion` | nein | Formatversion, siehe [Formatversion](#formatversion); fehlt = 1 |
| `subdecks` | nein | Unterteilung, siehe [Subdecks](#subdecks-levels) |
| `supersedes` | nein | Abgelöste Decks, siehe [Decks ablösen](#decks-ablösen-supersedes) |
| `learningMode` | nein | Startwert nach dem Import: `species` (Standard), `genus` oder `family` |
| `nameType` | nein | Startwert nach dem Import: `commonName` (Standard) oder `scientificName` |
| `reviewMode` | nein | Startwert nach dem Import: `flip` (Standard) oder `multipleChoice` |
| `sourceId` | – | Vergibt `scripts/sync_index.sh` nach dem Merge, nicht von Hand setzen |

Andere Felder sind nicht erlaubt; so fällt ein Tippfehler wie `subDecks` auf,
statt in der App stillschweigend ignoriert zu werden.

`learningMode`, `nameType` und `reviewMode` gelten nur beim ersten Import:
Danach gehören die Einstellungen dem Nutzer, ein Update des Decks ändert sie
nicht. Multiple Choice braucht genug verschiedene Namen im gewählten Modus;
fehlen sie, fällt die App pro Karte auf Umdrehen zurück.

Jeder PR, der Decks ändert, läuft durch den Check „Validate decks“
(`.github/workflows/validate-decks.yml`). Er prüft alle Decks gegen das Schema
und dazu, was ein Schema nicht ausdrücken kann: Subdecks nennen nur Arten aus
`speciesNames`, jede Art steht in höchstens einem Subdeck, sourceIds sind
eindeutig. Lokal:

```
pip install "jsonschema[format]"
python3 scripts/validate_decks.py
```

### Formatversion

Ein Deck nennt seine Formatversion in `formatVersion`, einer ganzen Zahl;
fehlt das Feld, ist es Version 1. Die Version steigt nur mit einer Änderung,
die eine ältere App falsch oder verlustbehaftet lesen würde, wenn sie sie
übergeht – Version 2 brachte `subdecks` und `supersedes`. Ein Feld, das eine
ältere App gefahrlos übergehen kann (wie `learningMode`), bleibt optional
und hebt die Version nicht; was sein Fehlen bedeutet, ändert sich nie.

Eine App liest jedes Format bis zu ihrem neuesten und lehnt ein neueres
verständlich ab, statt es halb zu importieren. Deshalb gibt es einen Index
pro Format, jeweils mit allen Decks bis zu diesem Format:
`data/decks/index.json` für Format 1, `data/decks/v<N>/index.json` für jedes
Format N ab 2. Ein Deck steht so in jedem Index ab seinem Format; ein
Community-Deck bleibt in dem Format, in dem es geschrieben ist, und niemand
migriert es.

Das neueste Format ist das `maximum` von `formatVersion` im Schema. Ein neues
Format heißt: dieses `maximum` heben – der nächste Lauf von
`scripts/sync_index.sh` legt dann den Index des neuen Formats an. Der muss
stehen, bevor eine App-Version erscheint, die ihn liest.

### Subdecks (Levels)

Ein Deck kann in Subdecks unterteilt sein, z. B. nach Schwierigkeitsgrad. In
der App schaltet der Nutzer jedes Subdeck einzeln ein oder aus. Subdecks
brauchen `formatVersion` 2:

```json
{
  "formatVersion": 2,
  "name": "Mittelmeer",
  "speciesNames": ["Diplodus vulgaris", "Sarpa salpa", "…"],
  "subdecks": [
    {"id": "level-1", "name": "Level 1", "speciesNames": ["Diplodus vulgaris"]},
    {"id": "level-2", "name": "Level 2", "speciesNames": ["Sarpa salpa"]}
  ]
}
```

- `speciesNames` enthält **alle** Arten des Decks, auch die der Subdecks.
  App-Versionen ohne Subdecks importieren das Deck daraus flach.
- Eine Art steht in höchstens einem Subdeck.
- Die `id` eines Subdecks bleibt über Updates gleich. An ihr erkennt die App
  das Subdeck wieder und behält, ob der Nutzer es abgeschaltet hat. Der
  `name` darf sich ändern.

### Decks ablösen (`supersedes`)

Ersetzt ein Deck andere Decks, z. B. drei Level-Decks durch ein Deck mit drei
Subdecks oder ein Deck, das aufgeteilt wird, listet es deren `sourceId`s in
`supersedes`. Wer die alten Decks importiert hat, bekommt in der App
angeboten, sie zusammenzuführen. Der Lernfortschritt folgt dabei der Art: Das
neue Deck übernimmt den Fortschritt jeder Art, die es selbst enthält.

Ein ablösendes Deck trägt `formatVersion` 2, ein abgelöstes eine kleinere
Formatversion als das ablösende. Die abgelösten Dateien bleiben liegen: Sie
stehen weiter in den Indizes der älteren Formate, für App-Versionen, die
`supersedes` nicht kennen, und fehlen in den Indizes ab dem Format des
ablösenden Decks. Gelöscht werden sie erst, wenn der Index ihres Formats
stillgelegt wird. Der Check prüft beides.

Die Generatoren unter `scripts/reef/` erzeugen weiterhin Level-Dateien
(`<base>_level1.json` …). Liegen diese in `data/decks/`, macht

```
python3 scripts/merge_level_decks.py <base>
```

daraus ein Deck `<base>.json` mit `formatVersion` 2, Subdecks und
`supersedes`; die Level-Dateien bleiben liegen. Sie brauchen dafür ihre
`sourceId`, also müssen sie schon einmal auf `main` gewesen sein. Für ein
ganz neues Deck reicht es, `supersedes` wegzulassen.

Die App lädt Decks über den Index ihres Formats (siehe
[Formatversion](#formatversion)), eine generierte Datei, die die einzelnen
Deck-Dateien zusammenfasst (ein Request statt einer pro Deck). Ein
GitHub-Actions-Workflow (`.github/workflows/sync-deck-index.yml`) regeneriert
alle Indizes automatisch nach jedem Merge eines PRs nach `main`, der Decks
oder das Schema ändert, und pusht das Ergebnis. Contributors müssen dafür
nichts tun.

Bei Bedarf lässt sich der Lauf auch manuell anstoßen (Tab "Actions" ->
"Sync deck index" -> "Run workflow"), oder lokal:

```
./scripts/sync_index.sh
```

Daten dürfen nicht-kommerziell genutzt werden; Attribution bei Bildern empfohlen (z. B. iNaturalist, FishBase)