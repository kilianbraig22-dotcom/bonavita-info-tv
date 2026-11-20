# Agenten für den Info-TV (training/show.html)

Alle laufen als geplante Aufgaben in Claude. Reihenfolge der Sicherheit:
1. Inhalte (Text) stehen nur in `training/content.json`. Der Redakteur ändert NUR diese Datei.
2. Vor jedem Veröffentlichen läuft `python3 tools/check.py`. Bei Fehler: nichts pushen.
3. Design-Änderungen macht der Design-Agent selbstständig und pusht sie direkt auf `main`, nur nach grünem Check (Netzwerk-Sperren der Agent-Umgebung ausgenommen). Keine Freigabe nötig.
4. Zurück zum alten Stand: `git revert <commit>` und pushen.

| Agent | Wann | Datei | Darf auf main pushen? |
|---|---|---|---|
| Wochen-Redakteur | sonntags | redakteur.md | ja, nur content.json, nur nach grünem Check |
| Design-Agent | täglich | design.md | ja, nur Design, nur nach grünem Check |
| Wochenbericht | sonntags, nach dem Redakteur | bericht.md | nur lesen, Nachricht an Kilian |
| Feiertags-Agent | am 25. jeden Monats | feiertag.md | ja, nur `aktionen` in content.json, nur nach grünem Check |
| Qualitäts-Wächter | täglich, nach dem Design-Agent | waechter.md | nein, nur melden |
| Saison-Vorbereiter | am 1. jeden Monats | saison.md | ja, nur `agents/saison/` |
| Wetter-Tipps | täglich früh | wetter.md | ja, nur Wetter-Tipp in content.json, nur nach grünem Check |

Gemeinsame Regeln: Du-/Sie-Form: die Gäste werden gesiezt. Deutsch, kurz, freundlich, kein Heilversprechen.
Der Prüf-Agent ist `tools/check.py` und wird von den anderen vor jedem Push ausgeführt.
