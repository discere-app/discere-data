# discere-data

Discere Data – zentralisierte Lern-Decks und Arteninformationen

Dieses Repository enthält strukturierte Biodiversitätsdaten für die Discere-App.
Ziel ist es, fertige Lern-Decks (Fische, Vögel, Pflanzen etc.) bereitzustellen, damit Nutzer nicht selbst Decks erstellen müssen.

Hinweis:

main Branch ist geschützt.
Änderungen bitte über Pull Requests.

## Neues Deck hinzufügen

Einfach eine neue JSON-Datei unter `data/decks/` anlegen (Felder: `name`,
`description`, `imageUrl`, `speciesNames`) und einen PR nach `main` öffnen.
Mehr ist nicht nötig - `data/decks/index.json` wird nicht von Hand gepflegt.

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