# Design-Agent (alle 3 Tage)

Ziel: Kleine sichtbare Änderungen am Look, damit es nicht immer gleich aussieht. Nur als Vorschlag.

## Vorgehen
1. `git pull`, Branch `design/<JJJJ-MM-TT>` anlegen. Nie auf `main` committen.
2. Eine kleine, passende Änderung wählen, z. B. neue Farbvariante (`data-look`-Paletten), ein neuer dezenter Effekt zur Jahreszeit oder zum Wetter, neue Akzentform. Passend zur Saison (Herbst, Winter/Weihnachten ab Dezember, Schnee, Neujahr).
3. Fire-TV-Regeln einhalten: keine Weichzeichner (`filter:blur`), keine vollflächigen Tönungsschichten, keine Slide-Transforms, wenig Partikel (Auf dem TV `window.hwTV` nutzen). Nichts, was flackern oder ruckeln kann.
4. `python3 tools/check.py --shots shots` laufen lassen. Bei Fehlern korrigieren oder verwerfen.
5. Push des Branches und Pull Request mit `gh pr create`. Beschreibung: was ändert sich, Screenshots (`shots/`) einchecken oder beschreiben, wie man es testet (`?look=…`).
6. Nichts mergen. Kilian entscheidet.

## Grenzen
- Keine Änderungen an Inhalten, Öffnungszeiten, Preisen, Texten.
- Maximal eine Änderung pro Lauf. Offene PRs vorher prüfen: Ist einer offen, keinen neuen anlegen.
