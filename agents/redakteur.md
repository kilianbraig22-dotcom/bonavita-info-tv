# Wochen-Redakteur (sonntags)

Ziel: Die Präsentation soll sich jede Woche frisch anfühlen, ohne dass jemand etwas tun muss.

## Vorgehen
1. `git pull`. `training/content.json` und `agents/README.md` lesen. Heutiges Datum bestimmen.
2. Die kommende Woche (Mo–Sa) planen. Anlässe beachten: Advent (29.11., 6.12., 13.12., 20.12.), Nikolaus 6.12., Weihnachten 24.–26.12., Silvester 31.12., Neujahr/Vorsätze im Januar, Ferien in Baden-Württemberg und Schweizer Feiertage (Jestetten liegt an der Grenze), Jahreszeit und Wetter.
3. In `content.json` ändern (und nur dort):
   - `mottoAlt`: je Wochentag 2 bis 3 Sprüche, höchstens 60 Zeichen. Alte Sprüche nicht sofort wiederholen, neue ergänzen.
   - `fakten`: pro Woche 3 bis 5 neue Fakten rund um Bewegung, Training, Schlaf, Ernährung, Rücken. Höchstens 150 Zeichen. Nur allgemein anerkanntes Wissen, kein Heilversprechen, keine Zahlen, die du nicht sicher weißt. Die Liste soll bei etwa 60 bleiben: älteste/schwächste streichen.
   - `aktionen`: Folien für Anlässe mit `von`/`bis` (JJJJ-MM-TT), `kicker`, `title` (max. 70 Zeichen), `text` (max. 200). Beispiel: `{"von":"2026-12-05","bis":"2026-12-06","kicker":"Nikolaus","title":"Schönen Nikolaustag!","text":"Heute gibt es etwas Süßes an der Rezeption."}` Aber nur Dinge behaupten, die sicher stimmen. Angebote, Preise, Öffnungszeiten, Aktionen der Praxis niemals erfinden.
   - Abgelaufene Aktionen entfernen.
4. `python3 tools/check.py` ausführen. Bei Fehlern korrigieren, bis es grün ist. Wenn es nach 3 Versuchen nicht klappt: nichts pushen, Grund im Bericht nennen.
5. Commit „Redakteur KW<nr>: <kurz was>“ (mit den Attribution-Zeilen), `git push origin main`.
6. In `agents/log.md` eine Zeile mit Datum und Änderungen anhängen.

## Grenzen
- Nicht anfassen: `show.html`, Bilder, `physio/`, `test/`.
- Keine Gesundheitsaussagen mit Zahlen oder Versprechen. Im Zweifel weglassen.
- Keine Namen oder Fotos von Personen.

## Adventskalender
Für den 1.–24. Dezember 2026 liegen in `aktionen` fertige „Türchen“-Folien (Kicker „Türchen N“). Nur ändern, wenn ein Text fachlich falsch ist oder besser passt.
