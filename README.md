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
Nach dem Mergen eines PRs nach `main` einmal ausführen, um sie zu
aktualisieren:

```
./scripts/sync_index.sh
```

Das Script pullt `main`, regeneriert `data/decks/index.json` und pusht das
Ergebnis. Es gibt (noch) keinen CI-Runner, der das automatisch macht.

Daten dürfen nicht-kommerziell genutzt werden; Attribution bei Bildern empfohlen (z. B. iNaturalist, FishBase)