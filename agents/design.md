# Design-Agent (täglich)

Ziel: Kleine sichtbare Änderungen am Look, damit es nicht immer gleich aussieht. Läuft selbstständig: keine Rückfrage, kein Pull Request, keine Freigabe nötig.

## Vorgehen
1. `git pull` auf `main`. Nicht nachfragen, nicht auf Freigabe warten.
2. Jeden Tag genau eine kleine, passende Änderung wählen und umsetzen, z. B. neue Farbvariante (`data-look`-Paletten), ein dezenter Effekt zur Jahreszeit oder zum Wetter, neue Akzentform. Passend zur Saison (Herbst, Winter/Weihnachten ab Dezember, Schnee, Neujahr). Selbst entscheiden, was gut aussieht; abwechslungsreich bleiben und nicht dasselbe wiederholen (`git log` ansehen).
3. Fire-TV-Regeln einhalten: keine Weichzeichner (`filter:blur`), keine vollflächigen Tönungsschichten, keine Slide-Transforms, wenig Partikel (Auf dem TV `window.hwTV` nutzen). Nichts, was flackern oder ruckeln kann.
4. `python3 tools/check.py --shots shots` laufen lassen. Fehler wegen gesperrter Netzwerkzugriffe in der Agent-Umgebung (`ERR_TUNNEL_CONNECTION_FAILED`, Google Fonts, Wetter-API) sind kein Fehler der Änderung und werden ignoriert, wenn sie auf `main` identisch auftreten. Alle anderen Fehler: korrigieren oder die Änderung verwerfen.
5. Screenshot prüfen (`shots/`), dann direkt auf `main` committen und pushen. Kurze, deutsche Commit-Nachricht: was wurde geändert und wie testet man es (`?look=…`).
6. Rückgängig machen kann Kilian jederzeit mit `git revert <commit>`.

## Grenzen
- Keine Änderungen an Inhalten, Öffnungszeiten, Preisen, Texten.
- Maximal eine Änderung pro Lauf, aber jeden Tag eine.
