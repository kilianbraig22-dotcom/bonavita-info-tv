# Feiertags- und Ferien-Agent (monatlich, am 25.)

Ziel: Feiertage, Brückentage und Ferien der kommenden 5 Wochen rechtzeitig als Folie auf dem TV haben. Nur Baden-Württemberg zählt: keine Termine aus Schaffhausen oder der übrigen Schweiz.

## Vorgehen
1. `git pull`. `training/content.json` und `agents/README.md` lesen. Datum bestimmen.
2. Per WebSearch/WebFetch (offizielle Quellen: Feiertage BW, Schulferien BW) die Termine der nächsten 5 Wochen prüfen. Nur eintragen, was in einer verlässlichen Quelle steht.
3. In `aktionen` je Termin eine Folie anlegen: `{"von","bis","kicker":"Feiertag"|"Ferien"|"Brückentag","title"(max. 70),"text"(max. 200),"sec":12,"lime":false}`. Beginn 3 Tage vor dem Termin, Ende am Termin. Freundlicher Gruß oder Hinweis, z. B. „Am Donnerstag ist Feiertag – genießen Sie den freien Tag.“
4. **Niemals** behaupten, dass die Praxis oder das Studio geschlossen ist oder andere Zeiten hat, wenn Kilian das nicht ausdrücklich gesagt hat. Gibt es Zweifel, nur den Gruß schreiben und in `agents/log.md` „Öffnungszeiten für <Termin> klären“ notieren.
5. Abgelaufene Feiertags-Einträge entfernen. Doppelte zu Einträgen des Redakteurs vermeiden (gleicher Anlass: nur einer).
6. `python3 tools/check.py` bis grün (Netzwerk-Fehler `ERR_TUNNEL_CONNECTION_FAILED` ignorieren). `git pull --rebase`, Commit „Feiertage: <was>“ (mit Attribution), push, Zeile in `agents/log.md`.

## Grenzen
Nur `training/content.json` (Bereich `aktionen`) und `agents/log.md` ändern.
