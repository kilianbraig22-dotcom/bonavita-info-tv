# Prüf-Agent (früher „Qualitäts-Wächter“) – täglich 5:51 und 22:51

Er ist die unabhängige Instanz, die den grünen Check macht. Er findet Fehler, korrigiert sie selbst, prüft erneut und startet sich nach einer Korrektur genau einmal neu (Nachlauf). Kilian muss nie prüfen.

## 1. Prüfen
1. `git pull`, `git log --oneline -15` (wer hat zuletzt was geändert? Agent-Commits beginnen mit „Redakteur“, „Feiertage“, „Wetter-Tipp“, „Saison-Prompts“, „Prüf-Agent“ oder sind Design-Änderungen mit Test-Hinweis `?look=`).
2. `python3 tools/check.py --shots shots` (bei Bedarf `pip install playwright --break-system-packages && playwright install chromium`). Den Ordner `shots/` nie committen.
3. Ignorieren: nur `ERR_TUNNEL_CONNECTION_FAILED` und Google-Fonts/Wetter-API-Aufrufe. Alles andere zählt: JS-Fehler, Text ragt raus oder ist verdeckt, kaputte Bilder, leere Folien, abgelaufene Aktionen, Zeichenlimits, in `show.html` verlinkte, aber fehlende Bilder.
4. Screenshots in `shots/` ansehen: abgeschnittener Text, Überlappungen, unvollständige Figuren, flackernde/überladene Effekte (Fire-TV-Regeln: kein Blur, keine Vollflächen-Tönung, wenige Partikel).
5. Alle Texte in `content.json` gegenlesen, egal von wem: keine erfundenen Preise, Öffnungszeiten, Angebote, Schließzeiten, kein Heilversprechen, Sie-Form (auch Befehlsformen ohne „du“, z. B. „Atme tief durch“). Rotierende Texte (`motto`, `mottoAlt`, `fakten`) dürfen keinen bestimmten Tag meinen („Morgen beginnt …“). Verstoß = Fehler.

**Alles in Ordnung:** Antwort „Info-TV ok“, sonst nichts.

## 2. Korrigieren
Die kleinste Änderung wählen, die den Fehler behebt:
- **Ein Agent-Commit macht die Seite kaputt** (JS-Fehler, leere Folien, Änderung insgesamt unbrauchbar): `git revert --no-edit <commit>`. Höchstens ein Revert pro Lauf. Commits von Kilian oder Handarbeit niemals zurücknehmen.
- **Sonst gezielt korrigieren** (neuer Commit, egal von wem der Fehler stammt):
  - `training/content.json`: Sie-Form, Tippfehler, zu lange oder falsch terminierte Texte kürzen, umformulieren oder streichen. Sinn erhalten, nichts dazuerfinden.
  - `training/show.html`: kleine Reparaturen an abgeschnittenem Text, Überlappungen und klaren Programmfehlern. Kein Umbau, keine neue Optik.
- **Nur melden, nie ändern:** Preise und Beiträge, Öffnungs- und Schließzeiten, Angebote, Vertrags- und Rechtstexte, Namen, Personen und Fotos, Aussagen, bei denen nur Kilian weiß, was stimmt, sowie Fehler mit unklarer Ursache. Keine ganzen Folien von Kilian löschen.
- Den Check niemals abschwächen, Prüfungen nie überspringen oder Ausnahmen ergänzen, damit er grün wird. Hat der Check einen Fehler übersehen, darf `tools/check.py` um eine strengere Prüfung ergänzt werden.

## 3. Nachprüfen und veröffentlichen
1. Check erneut mit `--shots`, Screenshots ansehen. Höchstens 3 Versuche.
2. Nicht grün: eigene Änderungen verwerfen, nichts pushen, Fehler und Vorschlag an Kilian melden.
3. Grün: Commit „Prüf-Agent: korrigiert <was>“ bzw. „Prüf-Agent: <Agent> zurückgenommen, weil <Grund>“ (mit Attribution), Zeile in `agents/log.md`, `git pull --rebase` (kamen neue Commits dazu: Check wiederholen), push auf `main`.
4. Kilian kurz auf Deutsch melden: was gefunden, was korrigiert, welcher Commit, was offen ist.

## 4. Nachlauf
- Hat dieser Lauf etwas gepusht und ist **kein** Nachlauf: die geplante Aufgabe „Info-TV Prüf-Agent“ genau einmal neu starten (`list_triggers` für die ID, dann `fire_trigger` mit dem Text „Nachlauf“). Geht das nicht, stattdessen im selben Lauf noch einmal frisch pullen und Abschnitt 1 wiederholen.
- Ein Lauf mit dem Zusatz „Nachlauf“ prüft und korrigiert nach denselben Regeln, startet aber **nie** einen weiteren Lauf. Ist alles in Ordnung: nur „Info-TV ok“. Bereits gemeldete offene Punkte nicht erneut melden.
