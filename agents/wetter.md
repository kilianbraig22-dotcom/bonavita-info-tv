# Wetter-Tipps-Agent (täglich früh)

Ziel: Ein kurzer Praxis-Tipp, der zum Wetter der nächsten zwei Tage passt.

## Vorgehen
1. `git pull`. `training/content.json` lesen. Prognose für Jestetten (47.65 N, 8.57 O) holen: WebFetch `https://api.open-meteo.com/v1/forecast?latitude=47.65&longitude=8.57&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,snowfall_sum,weathercode,wind_gusts_10m_max&timezone=Europe/Berlin&forecast_days=3`. Geht das nicht, WebSearch „Wetter Jestetten morgen“. Keine Prognose = nichts ändern, im Log „Wetter nicht erreichbar“.
2. Passenden Tipp wählen (nur ein Eintrag, nur bei auffälligem Wetter):
   - Glatteis/Frost/Schnee: Sturzprävention, sicheres Gehen, Aufwärmen vor dem Training.
   - Hitze (ab ca. 30 °C): trinken, Kreislauf, Training in die Morgen-/Abendstunden.
   - Dauerregen/Sturm: drinnen bewegen, Mobilisation, Trainingsidee ohne Draußen.
   - Kälteeinbruch: Muskeln und Sehnen länger aufwärmen.
   - Ruhiges Wetter: keinen Eintrag.
3. In `aktionen` genau einen Eintrag mit `kicker":"Wetter-Tipp"` anlegen oder ersetzen: `von` heute, `bis` übermorgen, `title` max. 70, `text` max. 200, `sec` 12. Allgemein anerkanntes Wissen, kein Heilversprechen, keine Zahlen, die nicht sicher sind. Alte Wetter-Tipp-Einträge entfernen.
4. `python3 tools/check.py` bis grün (Netzwerk-Fehler ignorieren), `git pull --rebase`, Commit „Wetter-Tipp <Datum>“ (mit Attribution), push. Kurze Zeile in `agents/log.md` nur wenn ein Tipp gesetzt wurde.

## Grenzen
Nur `training/content.json` (`aktionen`, nur Wetter-Tipp-Einträge) und `agents/log.md`.
