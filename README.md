# Bewerbungen – automatischer Job-Scanner

Ein kleiner Workflow, der jeden Morgen passende Einstiegsstellen im Raum Mühlacker / Pforzheim / Stuttgart / Karlsruhe / Heilbronn findet (Kernregion 50 km, erweitert bis 100 km).

**So funktioniert es**

1. **GitHub Actions** (`.github/workflows/jobsuche.yml`) startet täglich um ca. 6:30 Uhr (und auf Knopfdruck unter *Actions → Jobsuche → Run workflow*).
2. `scanner/scan.py` fragt die öffentliche Schnittstelle der Jobbörse der Bundesagentur für Arbeit mit allen Suchbegriffen aus `config.yaml` ab, filtert Senior-, Werkstudenten- und Praktikumsstellen heraus und vergibt einen Score nach Schlagwörtern im Titel.
3. Ergebnisse landen in `data/jobs.json` (alle aktuellen Treffer), `data/neu/<Datum>.md` (neu seit gestern) und unten in dieser README.
4. Eine tägliche Claude-Aufgabe liest `data/jobs.json`, ergänzt eigene Websuchen, prüft die Bewerbungsliste auf Duplikate und bereitet für die besten Stellen fertige Anschreiben vor (lokal, nicht in diesem Repo).

Suchprofil ändern: `config.yaml` bearbeiten und committen.

Tech: Python, requests, GitHub Actions, Bundesagentur-für-Arbeit-Jobsuche-API, Claude.

<!-- JOBS:START -->
_Stand 2026-11-28: 208 passende Stellen, 30 neu seit dem letzten Lauf._

## Top-Treffer

60 Stellen

| Score | Stelle | Firma | Ort | km | Veröffentlicht |
|---|---|---|---|---|---|
| 10 | [(Junior) Consultant Digitalisierung & Prozesse im Public Sector (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004058242-S) | BearingPoint  GmbH | 70174 Stuttgart | 30 | 2026-11-23 |
| 7 | [Junior Consultant - Projektmgmt / Prozesse / Software (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-5008043566-S) | Workwise GmbH | 70192 Stuttgart | 29 | 2026-11-23 |
| 7 | [(Junior) Consultant Generative AI (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004058235-S) | BearingPoint  GmbH | 70174 Stuttgart | 30 | 2026-11-23 |
| 7 | [(Junior) Consultant Supply Chain Management (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004058318-S) | BearingPoint  GmbH | 70174 Stuttgart | 30 | 2026-11-23 |
| 7 | [Consultant Public Health - Schwerpunkt Healthcare Digitalisierung & KI (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/18989-986960748-S) | PricewaterhouseCoopers GmbH WPG | 70174 Stuttgart | 30 | 2026-11-27 |
| 6 | [(Junior) Consultant Digitale Lösungen (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004058261-S) | BearingPoint  GmbH | 70174 Stuttgart | 30 | 2026-11-23 |
| 6 | [(Junior) Consultant Digital Transformation Banking (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004058306-S) | BearingPoint  GmbH | 70174 Stuttgart | 30 | 2026-11-23 |
| 6 | [(Junior) Consultant Digital Marketing, Sales & Customer Services (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004058264-S) | BearingPoint  GmbH | 70174 Stuttgart | 30 | 2026-11-23 |
| 6 | [Junior Projektmanager (m/w/d) Automotive](https://www.arbeitsagentur.de/jobsuche/jobdetail/12265-348796_JB5305069-S) | Ferchau GmbH Karlsruhe Mobility | 76135 Karlsruhe, Baden | 35 | 2026-11-24 |
| 5 | [Junior Technical Consultant PDM/PLM (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-154872-S) | Inneo | 71277 Rutesheim | 16 | 2026-11-17 |
| 5 | [Projektmanager "Digitalisierung & IoT" (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004025506-S) | NIVUS GmbH | 75031 Eppingen | 18 | 2026-11-17 |
| 5 | [IT Consultant (m/w/d) Software Testing / Test Automation](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-307616-S) | puntus | 71696 Möglingen, Kreis Ludwigsburg, Württ. | 22 | 2026-11-17 |
| 5 | [(Junior-) Software-Projektmanager (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/14820-0068854255-S) | HESS Cash Systems GmbH | 71106 Magstadt | 25 | 2026-11-19 |
| 5 | [Junior Supply Chain Experte (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12787-274664251126-S) | dm-drogerie markt GmbH + Co.KG | 76227 Karlsruhe, Baden | 29 | 2026-11-25 |
| 5 | [Junior IT Consultant (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-6939-S) | dydocon | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [(Junior) Personalberater / Recruitment Consultant (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-5011396863-S) | Harvey Nash GmbH | 70174 Stuttgart | 30 | 2026-11-26 |
| 5 | [(Junior) Cloud Consultant Databricks (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-314207-S) | Infomotion GmbH | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [Junior Consultant (m/w/d) Bereich Asset- und Risikomanag ...](https://www.arbeitsagentur.de/jobsuche/jobdetail/13884-168234-S) | Preyer GmbH | Stuttgart | 30 | 2026-11-20 |
| 5 | [(Junior) Consultant Datenmanagement / Facility Management (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004058292-S) | BearingPoint  GmbH | 70174 Stuttgart | 30 | 2026-11-23 |
| 5 | [(Junior) Consultant IT Service Management (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004057406-S) | BearingPoint  GmbH | 70174 Stuttgart | 30 | 2026-11-23 |
| 5 | [(Junior) Consultant / Anti-Financial Crime & Compliance (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004058316-S) | BearingPoint  GmbH | 70174 Stuttgart | 30 | 2026-11-23 |
| 5 | [(Junior) Consultant Microsoft / Modern Work & Cloud (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004057313-S) | BearingPoint  GmbH | 70174 Stuttgart | 30 | 2026-11-23 |
| 5 | [Junior Consultant IT-Security (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-290809-S) | BridgingIT | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [Junior IT-Consultant für IT-Security + Identity & Access Management (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-204664-S) | Ruhloff & Dauner | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [Consultant Zolltransformation & Digitalisierung (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-311760-S) | Capgemini | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [Consultant Public Sector Transformation, Infrastrukturförderung und Digitalisierung (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/18989-986961195-S) | PricewaterhouseCoopers GmbH WPG | 70174 Stuttgart | 30 | 2026-11-27 |
| 5 | [Consultant IT & Prozesse - Automotive (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/18989-986960685-S) | PricewaterhouseCoopers GmbH WPG | 70174 Stuttgart | 30 | 2026-11-27 |
| 5 | [(Junior) Consultant (m/w/d) Corporate Finance & M&A – Energie und Infrastruktur](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004040447-S) | Becker Büttner Held PartG mbB Becker Büttner Held Becker Büttner Held | 70565 Stuttgart | 31 | 2026-11-19 |
| 5 | [(Junior) Consultant (m/w/d) Corporate Finance & M&A - Energie und Infrastruktur in Stuttgart](https://www.arbeitsagentur.de/jobsuche/jobdetail/12117-YF-54597-YF-S) | Becker Büttner Held Rechtsanwälte Steuerberater Unternehmensberater PartGmbB | 70565 Stuttgart | 32 | 2026-11-19 |
| 5 | [MINT-Absolvent als Business Analyst (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/15719-44579879-1118-S) | Allianz Deutschland AG | 70565 Stuttgart | 32 | 2026-11-19 |
| 5 | [Projektmanager (m/w/d) Logistik & Supply Chain](https://www.arbeitsagentur.de/jobsuche/jobdetail/15006-k40180.6293-S) | prognum Automotive GmbH | 76131 Karlsruhe, Baden | 32 | 2026-11-16 |
| 5 | [Citizen Developer & Consultant Dynamics 365 CRM & Power Platform (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-298094-S) | Objektkultur Software | 76133 Karlsruhe, Baden | 34 | 2026-11-17 |
| 5 | [(Junior) Projektmanager Industriebau (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/19220-e8341f84a7739682-S) | Lidl Dienstleistung GmbH & Co. KG | 74206 Bad Wimpfen | 38 | 2026-11-27 |
| 5 | [(Junior) Consultant IT-Risk & Compliance (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004052076-S) | Halbauer GmbH | Neckarsulm | 40 | 2026-11-23 |
| 5 | [Junior Financial Consultant - Kundenaufbau / Finanzkonzepte (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-5009123673-S) | MLP Finanzberatung SE | 69168 Wiesloch | 40 | 2026-11-23 |
| 5 | [Junior Cybersecurity Consultant (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-310177-S) | BRANDMAUER IT | 76756 Bellheim | 49 | 2026-11-17 |
| 5 | [IT-Projektmanager - Digitalisierung (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-5009148322-S) | DIS AG Germany | 69124 Heidelberg, Neckar | 50 | 2026-11-23 |
| 4 | [Betriebswirt, Wirtschaftsingenieur - Prozessmanagement (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/14225-b7266128c26fad85-S) | Müller - Die lila Logistik Service GmbH | 71691 Freiberg am Neckar | 27 | 2026-11-25 |
| 4 | [Entwickler (m/w/d) Robotic Process Automation](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-5001700734-S) | Serviscope AG | 76227 Karlsruhe, Baden | 28 | 2026-11-17 |
| 4 | [IT-Consultant Supply Chain Forecasting (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12787-274322181126-S) | dmTECH GmbH | 76227 Karlsruhe, Baden | 29 | 2026-11-19 |
| 4 | [Consultant IT & Prozesse (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/18989-986961261-S) | PricewaterhouseCoopers GmbH WPG | 70174 Stuttgart | 30 | 2026-11-27 |
| 4 | [Consultant Projektmanagement Public Sector (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/18989-986960105-S) | PricewaterhouseCoopers GmbH WPG | 70174 Stuttgart | 30 | 2026-11-27 |
| 4 | [Consultant Tax Tech- und Prozessberatung (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/18989-986960611-S) | PricewaterhouseCoopers GmbH WPG | 70174 Stuttgart | 30 | 2026-11-27 |
| 4 | [Consultant Low Code Development Public Sector (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/18989-986960415-S) | PricewaterhouseCoopers GmbH WPG | 70174 Stuttgart | 30 | 2026-11-27 |
| 4 | [Agentic AI Consultant Public Sector (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-311766-S) | Capgemini | 70173 Stuttgart | 30 | 2026-11-17 |
| 4 | [AI Tech Consultant (all genders)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-309984-S) | BCG Platinion | 70173 Stuttgart | 30 | 2026-11-17 |
| 4 | [AI Software Engineer and Consultant (w/d/m)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-310601-S) | codecentric | 70173 Stuttgart | 30 | 2026-11-17 |
| 4 | [Consultant (m/w/d) Microsoft Dynamics 365 FSCM (Schwerpunkt Supply Chain Management)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-307153-S) | MODUS Consult | 70173 Stuttgart | 30 | 2026-11-17 |
| 4 | [DACH Consultant Digitized Processes - SCM & Logistics Operations - Ettlingen](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-314942-S) | PROMATIS software | 76275 Ettlingen | 33 | 2026-11-21 |
| 4 | [AI Consultant (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/15307-1594-1804056-0-S) | MLP Finanzberatung SE | 69168 Wiesloch | 41 | 2026-11-16 |
| 3 | [(Junior) Projektleiter Elektrotechnik (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12265-326077_JB5303882-S) | FERCHAU GmbH Niederlassung Heilbronn | 74321 Bietigheim-Bissingen | 20 | 2026-11-23 |
| 3 | [Trainee im Bautenschutz (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/14456-k11173.28964-S) | Tricosal Heinrich Schmid GmbH & Co. KG | 71106 Magstadt | 24 | 2026-11-25 |
| 3 | [Referent der Geschäftsführung Technologie und Digitalisierung (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-315143-S) | SCHUNK | 74348 Lauffen am Neckar | 27 | 2026-11-25 |
| 3 | [Consultant IKS Beratung & Optimierung (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/18989-986960710-S) | PricewaterhouseCoopers GmbH WPG | 70174 Stuttgart | 30 | 2026-11-27 |
| 3 | [Consultant Digital Transformation - Financial Services (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/18989-986961238-S) | PricewaterhouseCoopers GmbH WPG | 70174 Stuttgart | 30 | 2026-11-27 |
| 3 | [Consultant - IT Beratung Energiewirtschaft (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/18989-986960911-S) | PricewaterhouseCoopers GmbH WPG | 70174 Stuttgart | 30 | 2026-11-27 |
| 3 | [Consultant (w/m/d) Digital Workplace & Intranet](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-311175-S) | Campana & Schott | 70173 Stuttgart | 30 | 2026-11-17 |
| 3 | [Prozessmanager Bau & Lean Construction (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-286815-S) | MPS Bauplanung | 70173 Stuttgart | 30 | 2026-11-23 |
| 3 | [Digitalisierungsmanager/in (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12117-YF-54374-YF-S) | Stadt Remseck am Neckar | 71686 Remseck am Neckar | 31 | 2026-11-16 |
| 3 | [Trainee zur Büroleitung (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004077205-S) | Mömax Deutschland GmbH & Co. KG | 76139 Karlsruhe, Baden | 31 | 2026-11-26 |
<!-- JOBS:END -->
