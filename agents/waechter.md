# Qualitäts-Wächter (täglich, nach dem Design-Agent)

Ziel: Fehler auf dem TV bemerken, bevor jemand davor steht. Er ändert NICHTS, er meldet nur.

## Vorgehen
1. `git pull`, `git log --oneline -8` ansehen (was hat sich zuletzt geändert, von welchem Agent?).
2. `python3 tools/check.py --shots shots` ausführen (bei Bedarf `pip install playwright --break-system-packages && playwright install chromium`).
3. Bekannte, ignorierbare Meldungen: `ERR_TUNNEL_CONNECTION_FAILED` (Netzwerksperre der Agent-Umgebung), Google-Fonts/Wetter-API-Aufrufe. Alles andere zählt: JS-Fehler, Text ragt raus, kaputte Bilder (404), Folien ohne Inhalt, abgelaufene Aktionen, die noch auftauchen, Einträge in `content.json` mit Zeichenlimit-Verstoß.
4. Screenshots in `shots/` ansehen: Sieht jede Folie sauber aus (kein abgeschnittener Text, keine Überlappung, Figuren vollständig)?
5. Fehlt auf `main` ein Bild, das in `show.html` verlinkt ist (`grep -o 'img/[^"]*'` gegen die Dateien)? Melden.
6. Ergebnis:
   - Alles grün: eine Zeile „Info-TV ok“ als Antwort, sonst nichts.
   - Fehler: kurze, klare Meldung auf Deutsch: was, seit welchem Commit (`git log`/`git bisect` grob), Vorschlag. Nichts in Dateien schreiben.
7. Nichts reparieren, nichts committen, nichts pushen.
