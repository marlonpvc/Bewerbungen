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
_Stand 2026-11-18: 236 passende Stellen, 68 neu seit dem letzten Lauf._

## Top-Treffer

60 Stellen

| Score | Stelle | Firma | Ort | km | Veröffentlicht |
|---|---|---|---|---|---|
| 8 | [#AHS2601 / Absolvent*in / Junior Projektmanager*in (m/w/d) in der Projektsteuerung](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996081557-S) | THOST Projektmanagement GmbH | 76135 Karlsruhe, Baden | 35 | 2026-11-12 |
| 7 | [Business Application Consultant (w/m/d) (Microsoft Power Platform & KI Agents)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-266416-S) | Campana & Schott | 70173 Stuttgart | 30 | 2026-11-06 |
| 7 | [Prozess- & Business Analyst Digitalisierung Hochspannung (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12362-TR302112_1479CS-S) | Brunel GmbH NL Mannheim | Stuttgart | 30 | 2026-11-09 |
| 7 | [Junior NetSuite Consultant Digitized Processes (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-186546-S) | PROMATIS software | 76275 Ettlingen | 33 | 2026-11-17 |
| 6 | [(Junior) Consultant (w/m/d) Digitales Baumanagement und Dalux](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996078911-S) | Drees & Sommer SE | 70569 Stuttgart | 29 | 2026-11-12 |
| 6 | [Trainee (w/m/d) im Market Development – Digital Industries Automation](https://www.arbeitsagentur.de/jobsuche/jobdetail/12465-1650996-1-S) | Siemens AG | 70173 Stuttgart | 30 | 2026-11-06 |
| 6 | [IT Automation Engineer (m/w/d) - Schwerpunkt Prozessautomatisierung, KI & M365](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996060662-S) | Gustav Baehr GmbH | 71332 Waiblingen, Rems | 36 | 2026-11-12 |
| 6 | [Junior Prozessmanager Logistik (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/19220-ca6be18691309814-S) | Lidl Dienstleistung GmbH & Co. KG | 74206 Bad Wimpfen | 38 | 2026-11-09 |
| 5 | [Junior Consultant (m/w/d) e-Government / e-Akte](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004012145-S) | ANG GmbH | 75172 Pforzheim | 13 | 2026-11-13 |
| 5 | [Junior Technical Consultant PDM/PLM (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-154872-S) | Inneo | 71277 Rutesheim | 16 | 2026-11-17 |
| 5 | [Projektmanager "Digitalisierung & IoT" (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004025506-S) | NIVUS GmbH | 75031 Eppingen | 18 | 2026-11-17 |
| 5 | [IT Consultant (m/w/d) Software Testing / Test Automation](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-307616-S) | puntus | 71696 Möglingen, Kreis Ludwigsburg, Württ. | 22 | 2026-11-17 |
| 5 | [Junior Consultant (w/m/d) Claim- und Risikomanagement in Bau- und Immobilienprojekten](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996071925-S) | Drees & Sommer SE | 70569 Stuttgart | 29 | 2026-11-12 |
| 5 | [Junior IT Consultant (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-6939-S) | dydocon | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [(Junior) Consultant im Bereich Banking (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-270627-S) | DPS Holding | 70173 Stuttgart | 30 | 2026-11-06 |
| 5 | [(Junior) Cloud Consultant Databricks (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-314207-S) | Infomotion GmbH | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [Junior Consultant IT-Security (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-290809-S) | BridgingIT | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [Junior IT-Consultant für IT-Security + Identity & Access Management (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-204664-S) | Ruhloff & Dauner | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [Consultant Zolltransformation & Digitalisierung (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-311760-S) | Capgemini | 70173 Stuttgart | 30 | 2026-11-17 |
| 5 | [KI- und Digitalisierungsmanager (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13635-2c2411b3_JB5297272-S) | Grub Brugger Partnerschaft von Rechtsanwälten mbB | 70173 Stuttgart | 30 | 2026-11-13 |
| 5 | [Junior Kaufmännische:r Projektmanager:in Finanzierung](https://www.arbeitsagentur.de/jobsuche/jobdetail/12456-1653792-1-S) | Deutsche Bahn AG | 70173 Stuttgart | 30 | 2026-11-13 |
| 5 | [Projektmanager (m/w/d) Logistik & Supply Chain](https://www.arbeitsagentur.de/jobsuche/jobdetail/15006-k40180.6293-S) | prognum Automotive GmbH | 76131 Karlsruhe, Baden | 32 | 2026-11-16 |
| 5 | [Junior Consultant Data Analytics (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-143578-S) | PROMATIS software | 76275 Ettlingen | 33 | 2026-11-17 |
| 5 | [(Junior) Project Manager (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12117-YF-53153-YF-S) | SoftProject GmbH | 76275 Ettlingen | 33 | 2026-11-09 |
| 5 | [Citizen Developer & Consultant Dynamics 365 CRM & Power Platform (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-298094-S) | Objektkultur Software | 76133 Karlsruhe, Baden | 34 | 2026-11-17 |
| 5 | [Junior Consultant HR Dokumentenmanagement (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12265-521218_JB5297886-S) | FERCHAU GmbH Niederlassung Heilbronn | 74172 Neckarsulm | 40 | 2026-11-13 |
| 5 | [Junior Consultant IT-Risk & Compliance (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-309312-S) | Schwarz Digits | 74172 Neckarsulm | 40 | 2026-11-17 |
| 5 | [Junior Cybersecurity Consultant (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-310177-S) | BRANDMAUER IT | 76756 Bellheim | 49 | 2026-11-17 |
| 5 | [IT-Projektmanager - Digitalisierung (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996079002-S) | DIS AG Germany | 69124 Heidelberg, Neckar | 50 | 2026-11-12 |
| 5 | [Technischer Fachplaner / Projektmanager Events Junior (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12117-YF-53252-YF-S) | United Network Development GmbH & Co. KG | 69124 Heidelberg, Neckar | 50 | 2026-11-09 |
| 4 | [Entwickler (m/w/d) Robotic Process Automation](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-5001700734-S) | Serviscope AG | 76227 Karlsruhe, Baden | 28 | 2026-11-17 |
| 4 | [Agentic AI Consultant Public Sector (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-311766-S) | Capgemini | 70173 Stuttgart | 30 | 2026-11-17 |
| 4 | [AI Tech Consultant (all genders)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-309984-S) | BCG Platinion | 70173 Stuttgart | 30 | 2026-11-17 |
| 4 | [AI Software Engineer and Consultant (w/d/m)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-310601-S) | codecentric | 70173 Stuttgart | 30 | 2026-11-17 |
| 4 | [Consultant (m/w/d) Microsoft Dynamics 365 FSCM (Schwerpunkt Supply Chain Management)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-307153-S) | MODUS Consult | 70173 Stuttgart | 30 | 2026-11-17 |
| 4 | [Data & AI Business Analyst Lieferantenregress (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13319-901595/1_6637CS-S) | Hays Professional Solutions GmbH Standort Stuttgart | Stuttgart | 30 | 2026-11-16 |
| 4 | [Data & AI Business Analyst Lieferantenregress (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12634-BB-647173-7878-1953-S) | Akkodis Germany Tech Experts GmbH | 70173 Stuttgart | 30 | 2026-11-13 |
| 4 | [Junior Testmanager (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-295787-S) | Sogeti – Part of Capgemini | 70173 Stuttgart | 30 | 2026-11-17 |
| 4 | [Consultant (w/m/d) Projektmanagement](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-272011-S) | Campana & Schott | 70173 Stuttgart | 30 | 2026-11-06 |
| 4 | [Consultant Projektmanagement (w/m/d) für Infrastrukturprojekte](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-285068-S) | Campana & Schott | 70173 Stuttgart | 30 | 2026-11-06 |
| 4 | [Berater - AI Security (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/15548-1651470-1-S) | EY Consulting GmbH | 70629 Stuttgart | 38 | 2026-11-06 |
| 4 | [AI Consultant (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/15307-1594-1804056-0-S) | MLP Finanzberatung SE | 69168 Wiesloch | 41 | 2026-11-16 |
| 3 | [Junior CRM / Marketing Manager (HubSpot) (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12781-16425445-KAL-S) | Nussbaum Medien | 71263 Weil der Stadt | 21 | 2026-11-10 |
| 3 | [Absolvent Bauwesen (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/14456-k11173.28924-S) | Heinrich Schmid GmbH & Co. KG | 71634 Ludwigsburg, Württemberg | 22 | 2026-11-06 |
| 3 | [Junior Support Operations & Projekte (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1208617107-S) | ABACCO'S STEAKHOUSE GmbH & Co. KG | Ludwigsburg, Württemberg | 26 | 2026-11-10 |
| 3 | [Controller m/w/d - European Logistik & Supply Chain](https://www.arbeitsagentur.de/jobsuche/jobdetail/12513-0007661770-S) | Pentagon GmbH | 71638 Ludwigsburg, Württemberg | 27 | 2026-11-16 |
| 3 | [Consultant (w/m/d) Digital Workplace & Intranet](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-311175-S) | Campana & Schott | 70173 Stuttgart | 30 | 2026-11-17 |
| 3 | [(Junior) Business-Analyst (m/w/d) für die Bereiche Zahlungsverkehr und Wertpapierservice](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-273079-S) | DPS Holding | 70173 Stuttgart | 30 | 2026-11-06 |
| 3 | [Trainee Filialleiter/Shop Manager (m/w/d), Teilzeit/Vollzeit, Stuttgart](https://www.arbeitsagentur.de/jobsuche/jobdetail/11937-35548_59967-1-S) | Tchibo GmbH Abteilung HRO/HRO-P | 70173 Stuttgart | 30 | 2026-11-06 |
| 3 | [Consultant (w/m/d) Digital Workplace](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-182585-S) | Campana & Schott | 70173 Stuttgart | 30 | 2026-11-06 |
| 3 | [Digitalisierungsmanager/in (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12117-YF-54374-YF-S) | Stadt Remseck am Neckar | 71686 Remseck am Neckar | 31 | 2026-11-16 |
| 3 | [Referent für Digitalisierung (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/19022-v9imvknamo-S) | Nikolauspflege Stiftung für blinde und sehbehinderte Menschen | 70372 Stuttgart | 32 | 2026-11-06 |
| 3 | [Digitalisierungsmanager/in (W/M/D)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004029262-S) | Stadt Remseck am Neckar | 71686 Remseck am Neckar | 32 | 2026-11-17 |
| 3 | [Logistikplaner (m/w/d) Prozesssteuerung](https://www.arbeitsagentur.de/jobsuche/jobdetail/15006-k40180.6292-S) | prognum Automotive GmbH | 76131 Karlsruhe, Baden | 32 | 2026-11-16 |
| 3 | [Trainee im Lebensmittelhandel (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1003969033-S) | FrischeParadies GmbH & Co. KG | 70188 Stuttgart | 33 | 2026-11-05 |
| 3 | [Software Developer Dynamics 365 CRM & Power Platform (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13644-290826-S) | Objektkultur Software | 76133 Karlsruhe, Baden | 34 | 2026-11-17 |
| 3 | [(Junior) Einkäufer / Portfoliomanager - Energieeinkauf (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-281696-S) | Schwarz Corporate Solutions KG | 74072 Heilbronn, Neckar | 34 | 2026-11-06 |
| 3 | [Trainee im Versicherungsmanagement am Standort Karlsruhe (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/15719-44570091-1112-S) | Allianz Deutschland AG | 76135 Karlsruhe, Baden | 35 | 2026-11-13 |
| 3 | [Trainee Einkaufsabwicklung International (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12814-13308105-S) | Lidl Dienstleistung GmbH & Co. KG | 74172 Neckarsulm | 40 | 2026-11-05 |
| 3 | [Trainee Audit International (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12814-13308104-S) | Lidl Dienstleistung GmbH & Co. KG | 74172 Neckarsulm | 40 | 2026-11-05 |
<!-- JOBS:END -->
