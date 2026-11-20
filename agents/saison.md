# Saison-Vorbereiter (monatlich, am 1.)

Ziel: Kilian rechtzeitig die Figuren-Prompts für die nächste Saison liefern, auch für Neue im Team.

## Vorgehen
1. `git pull`. Datum bestimmen. Saisons: Herbst (ab 2.11. bzw. Verwandlungen), Weihnachten (ab 1.12.), Neujahr/Winter (Januar), Ostern (3 Wochen vor Ostern), Sommer (Juni), Halloween (ab 20.10.), Herbst (ab Oktober). Liegt der Start der nächsten Saison in den kommenden 5 Wochen, vorbereiten, sonst nur melden „nichts fällig“.
2. Team ermitteln: `training/show.html` (Team-Folien, `figure.hwskel`) und `physio/show.html`. Für jede Person prüfen, ob die Figuren-Dateien für diese Saison existieren (`training/img/<saison>-<name>.jpg`, `cut-<saison>-<name>.webp`). Fehlende Personen auflisten.
3. Für jede fehlende Person einen Bild-Prompt schreiben (Englisch, Stil wie bei den bestehenden Figuren; Rollen/Figuren nicht doppelt vergeben: `AU`/`XM`-Liste in `test/index.html` lesen). Jeder Prompt: „Use the attached photo as reference…“, Gesicht erkennbar, passende saisonale Kleidung, Hintergrund, 3:4, kein Text.
4. Datei `agents/saison/<saison>-<jahr>.md` mit allen Prompts anlegen, `git pull --rebase`, committen („Saison-Prompts <saison>“, mit Attribution), pushen.
5. Antwort an Kilian (max. 10 Zeilen): welche Saison, welche Personen noch fehlen, wo die Prompts liegen. Er erzeugt die Bilder und schickt sie; der Einbau erfolgt danach in einer Sitzung.

## Grenzen
Nur `agents/saison/` und `agents/log.md` ändern, keinen Code.
