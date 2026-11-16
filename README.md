# Bewerbungen – automatischer Job-Scanner

Ein kleiner Workflow, der jeden Morgen passende Einstiegsstellen im Raum Mühlacker / Pforzheim / Stuttgart / Karlsruhe / Heilbronn findet.

**So funktioniert es**

1. **GitHub Actions** (`.github/workflows/jobsuche.yml`) startet täglich um ca. 6:30 Uhr (und auf Knopfdruck unter *Actions → Jobsuche → Run workflow*).
2. `scanner/scan.py` fragt die öffentliche Schnittstelle der Jobbörse der Bundesagentur für Arbeit mit allen Suchbegriffen aus `config.yaml` ab, filtert Senior-, Werkstudenten- und Praktikumsstellen heraus und vergibt einen Score nach Schlagwörtern im Titel.
3. Ergebnisse landen in `data/jobs.json` (alle aktuellen Treffer), `data/neu/<Datum>.md` (neu seit gestern) und unten in dieser README.
4. Eine tägliche Claude-Aufgabe liest `data/jobs.json`, ergänzt eigene Websuchen, prüft die Bewerbungsliste auf Duplikate und bereitet für die besten Stellen fertige Anschreiben vor (lokal, nicht in diesem Repo).

Suchprofil ändern: `config.yaml` bearbeiten und committen.

Tech: Python, requests, GitHub Actions, Bundesagentur-für-Arbeit-Jobsuche-API, Claude.

<!-- JOBS:START -->
_Noch kein Lauf._
<!-- JOBS:END -->
