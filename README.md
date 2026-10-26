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
| `subdecks` | nein | Unterteilung, siehe [Subdecks](#subdecks-levels) |
| `supersedes` | nein | Abgelöste Decks, siehe [Decks ablösen](#decks-ablösen-supersedes) |
| `sourceId` | – | Vergibt `scripts/sync_index.sh` nach dem Merge, nicht von Hand setzen |

Andere Felder sind nicht erlaubt; so fällt ein Tippfehler wie `subDecks` auf,
statt in der App stillschweigend ignoriert zu werden.

Jeder PR, der Decks ändert, läuft durch den Check „Validate decks“
(`.github/workflows/validate-decks.yml`). Er prüft alle Decks gegen das Schema
und dazu, was ein Schema nicht ausdrücken kann: Subdecks nennen nur Arten aus
`speciesNames`, jede Art steht in höchstens einem Subdeck, sourceIds sind
eindeutig. Lokal:

```
pip install "jsonschema[format]"
python3 scripts/validate_decks.py
```

### Subdecks (Levels)

Ein Deck kann in Subdecks unterteilt sein, z. B. nach Schwierigkeitsgrad. In
der App schaltet der Nutzer jedes Subdeck einzeln ein oder aus:

```json
{
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
neue Deck übernimmt den Fortschritt jeder Art, die es selbst enthält. Die
abgelösten Deck-Dateien werden im selben PR gelöscht.

Die Generatoren unter `scripts/reef/` erzeugen weiterhin Level-Dateien
(`<base>_level1.json` …). Liegen diese in `data/decks/`, macht

```
python3 scripts/merge_level_decks.py <base>
```

daraus ein Deck `<base>.json` mit Subdecks und `supersedes` und löscht die
Level-Dateien. Die Level-Dateien brauchen dafür ihre `sourceId`, also müssen
sie schon einmal auf `main` gewesen sein. Für ein ganz neues Deck reicht es,
`supersedes` wegzulassen.

Die App lädt Decks über `data/decks/index.json`, eine generierte Datei, die
alle einzelnen Deck-Dateien zusammenfasst (ein Request statt einer pro Deck).
Ein GitHub-Actions-Workflow (`.github/workflows/sync-deck-index.yml`)
regeneriert sie automatisch nach jedem Merge eines PRs nach `main` und pusht
das Ergebnis. Contributors müssen dafür nichts tun.

Bei Bedarf lässt sich der Lauf auch manuell anstoßen (Tab "Actions" ->
"Sync deck index" -> "Run workflow"), oder lokal:

```
./scripts/sync_index.sh
```

Daten dürfen nicht-kommerziell genutzt werden; Attribution bei Bildern empfohlen (z. B. iNaturalist, FishBase)