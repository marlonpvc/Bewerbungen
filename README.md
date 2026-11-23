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
_Stand 2026-11-23: 209 passende Stellen, 10 neu seit dem letzten Lauf._

## Top-Treffer

60 Stellen

| Score | Stelle | Firma | Ort | km | Veröffentlicht |
|---|---|---|---|---|---|
| 8 | [#AHS2601 / Absolvent*in / Junior Projektmanager*in (m/w/d) in der Projektsteuerung](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996081557-S) | THOST Projektmanagement GmbH | 76135 Karlsruhe, Baden | 35 | 2026-11-12 |
| 7 | [Junior Consultant - Projektmgmt / Prozesse / Software (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-5008043566-S) | Workwise GmbH | 70192 Stuttgart | 29 | 2026-11-23 |
| 7 | [Prozess- & Business Analyst Digitalisierung Hochspannung (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12362-TR302112_1479CS-S) | Brunel GmbH NL Mannheim | Stuttgart | 30 | 2026-11-09 |
| 6 | [IT Automation Engineer (m/w/d) - Schwerpunkt Prozessautomatisierung, KI & M365](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996060662-S) | Gustav Baehr GmbH | 71332 Waiblingen, Rems | 36 | 2026-11-12 |
| 6 | [Junior Prozessmanager Logistik (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/19220-ca6be18691309814-S) | Lidl Dienstleistung GmbH & Co. KG | 74206 Bad Wimpfen | 38 | 2026-11-09 |
| 5 | [Junior Consultant (m/w/d) e-Government / e-Akte](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004048015-S) | ANG GmbH | 75172 Pforzheim | 13 | 2026-11-20 |
| 5 | [Junior Technical Consultant PDM/PLM (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-154872-S) | Inneo | 71277 Rutesheim | 16 | 2026-11-17 |
| 5 | [Projektmanager "Digitalisierung & IoT" (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004025506-S) | NIVUS GmbH | 75031 Eppingen | 18 | 2026-11-17 |
| 5 | [IT Consultant (m/w/d) Software Testing / Test Automation](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-307616-S) | puntus | 71696 Möglingen, Kreis Ludwigsburg, Württ. | 22 | 2026-11-17 |
| 5 | [(Junior-) Software-Projektmanager (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/14820-0068854255-S) | HESS Cash Systems GmbH | 71106 Magstadt | 25 | 2026-11-19 |
| 5 | [Junior IT Consultant (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-6939-S) | dydocon | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [(Junior) Consultant IT-Risk & Compliance (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12634-BB-647439-7878-8061-S) | Akkodis Germany Tech Experts GmbH | 70173 Stuttgart | 30 | 2026-11-20 |
| 5 | [Junior Consultant (m/w/d) Bereich Asset- und Risikomanag ...](https://www.arbeitsagentur.de/jobsuche/jobdetail/13884-168234-S) | Preyer GmbH | Stuttgart | 30 | 2026-11-20 |
| 5 | [(Junior) Cloud Consultant Databricks (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-314207-S) | Infomotion GmbH | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [Junior Consultant IT-Security (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-290809-S) | BridgingIT | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [Junior IT-Consultant für IT-Security + Identity & Access Management (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-204664-S) | Ruhloff & Dauner | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [Consultant Zolltransformation & Digitalisierung (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-311760-S) | Capgemini | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [KI- und Digitalisierungsmanager (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13635-2c2411b3_JB5297272-S) | Grub Brugger Partnerschaft von Rechtsanwälten mbB | 70173 Stuttgart | 30 | 2026-11-13 |
| 5 | [Junior Kaufmännische:r Projektmanager:in Finanzierung](https://www.arbeitsagentur.de/jobsuche/jobdetail/12456-1653792-1-S) | Deutsche Bahn AG | 70173 Stuttgart | 30 | 2026-11-13 |
| 5 | [(Junior) Consultant (m/w/d) Corporate Finance & M&A – Energie und Infrastruktur](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004040447-S) | Becker Büttner Held PartG mbB Becker Büttner Held Becker Büttner Held | 70565 Stuttgart | 31 | 2026-11-19 |
| 5 | [(Junior) Consultant (m/w/d) Corporate Finance & M&A - Energie und Infrastruktur in Stuttgart](https://www.arbeitsagentur.de/jobsuche/jobdetail/12117-YF-54597-YF-S) | Becker Büttner Held Rechtsanwälte Steuerberater Unternehmensberater PartGmbB | 70565 Stuttgart | 32 | 2026-11-19 |
| 5 | [MINT-Absolvent als Business Analyst (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/15719-44579879-1118-S) | Allianz Deutschland AG | 70565 Stuttgart | 32 | 2026-11-19 |
| 5 | [Projektmanager (m/w/d) Logistik & Supply Chain](https://www.arbeitsagentur.de/jobsuche/jobdetail/15006-k40180.6293-S) | prognum Automotive GmbH | 76131 Karlsruhe, Baden | 32 | 2026-11-16 |
| 5 | [Citizen Developer & Consultant Dynamics 365 CRM & Power Platform (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-298094-S) | Objektkultur Software | 76133 Karlsruhe, Baden | 34 | 2026-11-17 |
| 5 | [Junior Consultant HR Dokumentenmanagement (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12265-521218_JB5297886-S) | FERCHAU GmbH Niederlassung Heilbronn | 74172 Neckarsulm | 40 | 2026-11-13 |
| 5 | [Junior Consultant IT-Risk & Compliance (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-309312-S) | Schwarz Digits | 74172 Neckarsulm | 40 | 2026-11-17 |
| 5 | [Junior Financial Consultant - Kundenaufbau / Finanzkonzepte (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-5009123673-S) | MLP Finanzberatung SE | 69168 Wiesloch | 40 | 2026-11-23 |
| 5 | [Junior Cybersecurity Consultant (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-310177-S) | BRANDMAUER IT | 76756 Bellheim | 49 | 2026-11-17 |
| 5 | [IT-Projektmanager - Digitalisierung (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-5009148322-S) | DIS AG Germany | 69124 Heidelberg, Neckar | 50 | 2026-11-23 |
| 5 | [Technischer Fachplaner / Projektmanager Events Junior (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12117-YF-53252-YF-S) | United Network Development GmbH & Co. KG | 69124 Heidelberg, Neckar | 50 | 2026-11-09 |
| 4 | [KI-Prozessberater (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004047973-S) | ANG GmbH | 75172 Pforzheim | 13 | 2026-11-20 |
| 4 | [Entwickler (m/w/d) Robotic Process Automation](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-5001700734-S) | Serviscope AG | 76227 Karlsruhe, Baden | 28 | 2026-11-17 |
| 4 | [IT-Consultant Supply Chain Forecasting (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12787-274322181126-S) | dmTECH GmbH | 76227 Karlsruhe, Baden | 29 | 2026-11-19 |
| 4 | [Agentic AI Consultant Public Sector (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-311766-S) | Capgemini | 70173 Stuttgart | 30 | 2026-11-17 |
| 4 | [AI Tech Consultant (all genders)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-309984-S) | BCG Platinion | 70173 Stuttgart | 30 | 2026-11-17 |
| 4 | [AI Software Engineer and Consultant (w/d/m)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-310601-S) | codecentric | 70173 Stuttgart | 30 | 2026-11-17 |
| 4 | [Consultant (m/w/d) Microsoft Dynamics 365 FSCM (Schwerpunkt Supply Chain Management)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-307153-S) | MODUS Consult | 70173 Stuttgart | 30 | 2026-11-17 |
| 4 | [Data & AI Business Analyst Lieferantenregress (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12634-BB-647173-7878-1953-S) | Akkodis Germany Tech Experts GmbH | 70173 Stuttgart | 30 | 2026-11-13 |
| 4 | [Junior Testmanager (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-295787-S) | Sogeti – Part of Capgemini | 70173 Stuttgart | 30 | 2026-11-17 |
| 4 | [DACH Consultant Digitized Processes - SCM & Logistics Operations - Ettlingen](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-314942-S) | PROMATIS software | 76275 Ettlingen | 33 | 2026-11-21 |
| 4 | [AI Consultant (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/15307-1594-1804056-0-S) | MLP Finanzberatung SE | 69168 Wiesloch | 41 | 2026-11-16 |
| 3 | [Junior CRM / Marketing Manager (HubSpot) (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12781-16425445-KAL-S) | Nussbaum Medien | 71263 Weil der Stadt | 21 | 2026-11-10 |
| 3 | [Controller m/w/d - European Logistik & Supply Chain](https://www.arbeitsagentur.de/jobsuche/jobdetail/12513-0007661770-S) | Pentagon GmbH | 71638 Ludwigsburg, Württemberg | 27 | 2026-11-16 |
| 3 | [Consultant (w/m/d) Digital Workplace & Intranet](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-311175-S) | Campana & Schott | 70173 Stuttgart | 30 | 2026-11-17 |
| 3 | [Digitalisierungsmanager/in (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12117-YF-54374-YF-S) | Stadt Remseck am Neckar | 71686 Remseck am Neckar | 31 | 2026-11-16 |
| 3 | [Digitalisierungsmanager/in (W/M/D)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004029262-S) | Stadt Remseck am Neckar | 71686 Remseck am Neckar | 32 | 2026-11-17 |
| 3 | [Logistikplaner (m/w/d) Prozesssteuerung](https://www.arbeitsagentur.de/jobsuche/jobdetail/15006-k40180.6292-S) | prognum Automotive GmbH | 76131 Karlsruhe, Baden | 32 | 2026-11-16 |
| 3 | [IT-Infrastructure Consultant Architekt Digitale Energiewende (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004039398-S) | Schleupen SE | 76275 Ettlingen | 34 | 2026-11-19 |
| 3 | [Software Developer Dynamics 365 CRM & Power Platform (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-290826-S) | Objektkultur Software | 76133 Karlsruhe, Baden | 34 | 2026-11-17 |
| 3 | [Trainee Strategisches Management (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/16506-0068871420-S) | Omexom Distribution Management GmbH | 70736 Fellbach, Württemberg | 34 | 2026-11-20 |
| 3 | [Trainee im Versicherungsmanagement am Standort Karlsruhe (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/15719-44570091-1112-S) | Allianz Deutschland AG | 76135 Karlsruhe, Baden | 35 | 2026-11-13 |
| 3 | [Trainee Filialleiter/Shop Manager (m/w/d), Teilzeit, Wiesloch](https://www.arbeitsagentur.de/jobsuche/jobdetail/11937-35700_60034-1-S) | Tchibo GmbH Abteilung HRO/HRO-P | 69168 Wiesloch | 40 | 2026-11-15 |
| 3 | [Trainee Postproduction Videoschnitte & Grafik (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004034774-S) | Sidney R. Wolff Partner für Gemeinschaftsverpf | 74626 Bretzfeld | 48 | 2026-11-18 |
| 2 | [Technical Consultant (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-299795-S) | WidasConcepts | 71299 Wimsheim | 11 | 2026-11-17 |
| 2 | [Business Process Manager (m/w/d) Finance/Controlling, befristet](https://www.arbeitsagentur.de/jobsuche/jobdetail/12117-YF-53319-YF-S) | Witzenmann GmbH | 75175 Pforzheim | 11 | 2026-11-09 |
| 2 | [Projektmanager Vertrieb und Projektmanagement m/w/d](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004051566-S) | TeamPower Personaldienstleistungs GmbH | 75175 Pforzheim | 11 | 2026-11-22 |
| 2 | [Consultant IT-Security (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004048110-S) | ANG GmbH | 75172 Pforzheim | 13 | 2026-11-20 |
| 2 | [Supply Chain Manager (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996062436-S) | DIS AG Germany | 75172 Pforzheim | 13 | 2026-11-12 |
| 2 | [Prozess-, Risiko- und Qualitätsmanager (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004047905-S) | ANG GmbH | 75172 Pforzheim | 13 | 2026-11-20 |
| 2 | [IT-Systems Engineer / Consultant (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-312571-S) | Inneo | 71277 Rutesheim | 16 | 2026-11-17 |
<!-- JOBS:END -->
