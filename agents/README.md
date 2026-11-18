# Agenten für den Info-TV (training/show.html)

Alle laufen als geplante Aufgaben in Claude. Reihenfolge der Sicherheit:
1. Inhalte (Text) stehen nur in `training/content.json`. Der Redakteur ändert NUR diese Datei.
2. Vor jedem Veröffentlichen läuft `python3 tools/check.py`. Bei Fehler: nichts pushen.
3. Design-Änderungen gehen nie direkt auf `main`, sondern auf einen Branch `design/<datum>` + Pull Request. Kilian gibt frei.
4. Zurück zum alten Stand: `git revert <commit>` und pushen.

| Agent | Wann | Datei | Darf auf main pushen? |
|---|---|---|---|
| Wochen-Redakteur | sonntags | redakteur.md | ja, nur content.json, nur nach grünem Check |
| Design-Agent | alle 3 Tage | design.md | nein, nur Branch + PR |
| Wochenbericht | sonntags, nach dem Redakteur | bericht.md | nur lesen, Nachricht an Kilian |

Gemeinsame Regeln: Du-/Sie-Form: die Gäste werden gesiezt. Deutsch, kurz, freundlich, kein Heilversprechen.
Der Prüf-Agent ist `tools/check.py` und wird von den anderen vor jedem Push ausgeführt.
