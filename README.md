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
_Stand 2026-11-16: 189 passende Stellen, 80 neu seit dem letzten Lauf._

## Top-Treffer

60 Stellen

| Score | Stelle | Firma | Ort | km | Veröffentlicht |
|---|---|---|---|---|---|
| 8 | [#AHS2601 / Absolvent*in / Junior Projektmanager*in (m/w/d) in der Projektsteuerung](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996081557-S) | THOST Projektmanagement GmbH | 76135 Karlsruhe, Baden | 35 | 2026-11-12 |
| 7 | [Business Application Consultant (w/m/d) (Microsoft Power Platform & KI Agents)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-266416-S) | Campana & Schott | 70173 Stuttgart | 30 | 2026-11-06 |
| 7 | [Prozess- & Business Analyst Digitalisierung Hochspannung (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12362-TR302112_1479CS-S) | Brunel GmbH NL Mannheim | Stuttgart | 30 | 2026-11-09 |
| 6 | [(Junior) Consultant (w/m/d) Digitales Baumanagement und Dalux](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996078911-S) | Drees & Sommer SE | 70569 Stuttgart | 29 | 2026-11-12 |
| 6 | [Trainee (w/m/d) im Market Development – Digital Industries Automation](https://www.arbeitsagentur.de/jobsuche/jobdetail/12465-1650996-1-S) | Siemens AG | 70173 Stuttgart | 30 | 2026-11-06 |
| 6 | [IT Automation Engineer (m/w/d) - Schwerpunkt Prozessautomatisierung, KI & M365](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996060662-S) | Gustav Baehr GmbH | 71332 Waiblingen, Rems | 36 | 2026-11-12 |
| 6 | [Junior Prozessmanager Logistik (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/19220-ca6be18691309814-S) | Lidl Dienstleistung GmbH & Co. KG | 74206 Bad Wimpfen | 38 | 2026-11-09 |
| 5 | [Junior Consultant (m/w/d) e-Government / e-Akte](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004012145-S) | ANG GmbH | 75172 Pforzheim | 13 | 2026-11-13 |
| 5 | [Junior Consultant (w/m/d) Claim- und Risikomanagement in Bau- und Immobilienprojekten](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996071925-S) | Drees & Sommer SE | 70569 Stuttgart | 29 | 2026-11-12 |
| 5 | [(Junior) Consultant im Bereich Banking (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-270627-S) | DPS Holding | 70173 Stuttgart | 30 | 2026-11-06 |
| 5 | [KI- und Digitalisierungsmanager (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13635-2c2411b3_JB5297272-S) | Grub Brugger Partnerschaft von Rechtsanwälten mbB | 70173 Stuttgart | 30 | 2026-11-13 |
| 5 | [Junior Kaufmännische:r Projektmanager:in Finanzierung](https://www.arbeitsagentur.de/jobsuche/jobdetail/12456-1653792-1-S) | Deutsche Bahn AG | 70173 Stuttgart | 30 | 2026-11-13 |
| 5 | [Projektmanager (m/w/d) Logistik & Supply Chain](https://www.arbeitsagentur.de/jobsuche/jobdetail/15006-k40180.6293-S) | prognum Automotive GmbH | 76131 Karlsruhe, Baden | 32 | 2026-11-16 |
| 5 | [(Junior) Project Manager (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12117-YF-53153-YF-S) | SoftProject GmbH | 76275 Ettlingen | 33 | 2026-11-09 |
| 5 | [Junior Consultant HR Dokumentenmanagement (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12265-521218_JB5297886-S) | FERCHAU GmbH Niederlassung Heilbronn | 74172 Neckarsulm | 40 | 2026-11-13 |
| 5 | [IT-Projektmanager - Digitalisierung (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996079002-S) | DIS AG Germany | 69124 Heidelberg, Neckar | 50 | 2026-11-12 |
| 5 | [Technischer Fachplaner / Projektmanager Events Junior (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12117-YF-53252-YF-S) | United Network Development GmbH & Co. KG | 69124 Heidelberg, Neckar | 50 | 2026-11-09 |
| 4 | [Software Developer (all genders) Prozessautomatisierung & KI](https://www.arbeitsagentur.de/jobsuche/jobdetail/17700-0068499277-S) | Almato AG | 70174 Stuttgart | 30 | 2026-11-02 |
| 4 | [Data & AI Business Analyst Lieferantenregress (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13319-901595/1_6637CS-S) | Hays Professional Solutions GmbH Standort Stuttgart | Stuttgart | 30 | 2026-11-16 |
| 4 | [Data & AI Business Analyst Lieferantenregress (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12634-BB-647173-7878-1953-S) | Akkodis Germany Tech Experts GmbH | 70173 Stuttgart | 30 | 2026-11-13 |
| 4 | [Consultant (w/m/d) Projektmanagement](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-272011-S) | Campana & Schott | 70173 Stuttgart | 30 | 2026-11-06 |
| 4 | [Consultant Projektmanagement (w/m/d) für Infrastrukturprojekte](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-285068-S) | Campana & Schott | 70173 Stuttgart | 30 | 2026-11-06 |
| 4 | [AI Solutions Consultant Mercedes-Benz Management Consulting (d/m/w/x)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13151-1649549-1-S) | Mercedes-Benz Group AG | 70565 Stuttgart | 32 | 2026-11-02 |
| 4 | [Berater - AI Security (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/15548-1651470-1-S) | EY Consulting GmbH | 70629 Stuttgart | 38 | 2026-11-06 |
| 4 | [AI Consultant (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/15307-1594-1804056-0-S) | MLP Finanzberatung SE | 69168 Wiesloch | 41 | 2026-11-16 |
| 3 | [Junior CRM / Marketing Manager (HubSpot) (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12781-16425445-KAL-S) | Nussbaum Medien | 71263 Weil der Stadt | 21 | 2026-11-10 |
| 3 | [Absolvent Bauwesen (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/14456-k11173.28924-S) | Heinrich Schmid GmbH & Co. KG | 71634 Ludwigsburg, Württemberg | 22 | 2026-11-06 |
| 3 | [Junior Support Operations & Projekte (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1208617107-S) | ABACCO'S STEAKHOUSE GmbH & Co. KG | Ludwigsburg, Württemberg | 26 | 2026-11-10 |
| 3 | [Controller m/w/d - European Logistik & Supply Chain](https://www.arbeitsagentur.de/jobsuche/jobdetail/12513-0007661770-S) | Pentagon GmbH | 71638 Ludwigsburg, Württemberg | 27 | 2026-11-16 |
| 3 | [(Junior) Business-Analyst (m/w/d) für die Bereiche Zahlungsverkehr und Wertpapierservice](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-273079-S) | DPS Holding | 70173 Stuttgart | 30 | 2026-11-06 |
| 3 | [Trainee Filialleiter/Shop Manager (m/w/d), Teilzeit/Vollzeit, Stuttgart](https://www.arbeitsagentur.de/jobsuche/jobdetail/11937-35548_59967-1-S) | Tchibo GmbH Abteilung HRO/HRO-P | 70173 Stuttgart | 30 | 2026-11-06 |
| 3 | [Consultant (w/m/d) Digital Workplace](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-182585-S) | Campana & Schott | 70173 Stuttgart | 30 | 2026-11-06 |
| 3 | [Digitalisierungsmanager/in (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12117-YF-54374-YF-S) | Stadt Remseck am Neckar | 71686 Remseck am Neckar | 31 | 2026-11-16 |
| 3 | [Referent für Digitalisierung (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/19022-v9imvknamo-S) | Nikolauspflege Stiftung für blinde und sehbehinderte Menschen | 70372 Stuttgart | 32 | 2026-11-06 |
| 3 | [Logistikplaner (m/w/d) Prozesssteuerung](https://www.arbeitsagentur.de/jobsuche/jobdetail/15006-k40180.6292-S) | prognum Automotive GmbH | 76131 Karlsruhe, Baden | 32 | 2026-11-16 |
| 3 | [Trainee im Lebensmittelhandel (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1003969033-S) | FrischeParadies GmbH & Co. KG | 70188 Stuttgart | 33 | 2026-11-05 |
| 3 | [(Junior) Einkäufer / Portfoliomanager - Energieeinkauf (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-281696-S) | Schwarz Corporate Solutions KG | 74072 Heilbronn, Neckar | 34 | 2026-11-06 |
| 3 | [Trainee im Versicherungsmanagement am Standort Karlsruhe (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/15719-44570091-1112-S) | Allianz Deutschland AG | 76135 Karlsruhe, Baden | 35 | 2026-11-13 |
| 3 | [Trainee Einkaufsabwicklung International (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12814-13308105-S) | Lidl Dienstleistung GmbH & Co. KG | 74172 Neckarsulm | 40 | 2026-11-05 |
| 3 | [Trainee Audit International (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12814-13308104-S) | Lidl Dienstleistung GmbH & Co. KG | 74172 Neckarsulm | 40 | 2026-11-05 |
| 3 | [Trainee Filialleiter/Shop Manager (m/w/d), Teilzeit, Wiesloch](https://www.arbeitsagentur.de/jobsuche/jobdetail/11937-35700_60034-1-S) | Tchibo GmbH Abteilung HRO/HRO-P | 69168 Wiesloch | 40 | 2026-11-15 |
| 3 | [Trainee Filialleiter/Shop Manager (m/w/d), Teilzeit/Vollzeit, Winnenden](https://www.arbeitsagentur.de/jobsuche/jobdetail/11937-35379_59894-1-S) | Tchibo GmbH Abteilung HRO/HRO-P | 71364 Winnenden, Württemberg | 42 | 2026-11-05 |
| 2 | [Business Process Manager (m/w/d) Finance/Controlling, befristet](https://www.arbeitsagentur.de/jobsuche/jobdetail/12117-YF-53319-YF-S) | Witzenmann GmbH | 75175 Pforzheim | 11 | 2026-11-09 |
| 2 | [Projektmanager Vertrieb und Projektmanagement m/w/d](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004015504-S) | TeamPower Personaldienstleistungs GmbH | 75175 Pforzheim | 11 | 2026-11-14 |
| 2 | [Consultant IT-Security (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1004012200-S) | ANG GmbH | 75172 Pforzheim | 13 | 2026-11-13 |
| 2 | [Supply Chain Manager (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996062436-S) | DIS AG Germany | 75172 Pforzheim | 13 | 2026-11-12 |
| 2 | [Business Partner IT - Datenspezialist & Prozessautomatisierung (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12288-4996079814-S) | auteega Gmbh | 74321 Bietigheim-Bissingen | 20 | 2026-11-12 |
| 2 | [Technischer Projektmanager (w/m/d) mit Erfahrung](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-275786-S) | pmX | 71229 Leonberg, Württemberg | 21 | 2026-11-06 |
| 2 | [Planungsingenieur Produktion und Logistik Automotive (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12265-484348_JB5297442-S) | Ferchau  GmbH | 70435 Stuttgart | 26 | 2026-11-13 |
| 2 | [BE-terna GmbH: Solution Sales Specialist (w/m/d) Qlik, Microsoft Data Analytics & AI](https://www.arbeitsagentur.de/jobsuche/jobdetail/11956-3062801794783601-S) | BE-terna GmbH | 71069 Sindelfingen | 27 | 2026-11-16 |
| 2 | [IT Business Analyst (m/w/d) in Direktvermittlung](https://www.arbeitsagentur.de/jobsuche/jobdetail/12265-508540_JB5299621-S) | FERCHAU GmbH Niederlassung Stuttgart Automotive | 70197 Stuttgart | 27 | 2026-11-16 |
| 2 | [IT Consultant Finance (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12787-274066131126-S) | dmTECH GmbH | 76227 Karlsruhe, Baden | 29 | 2026-11-13 |
| 2 | [Technical Solution Consultant Forecasting & Replenishment (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12787-266149111126-S) | dmTECH GmbH | 76227 Karlsruhe, Baden | 29 | 2026-11-11 |
| 2 | [Platform Engineer (DevOps) - Snowflake & KI (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/12787-273774091126-S) | dmTECH GmbH | 76227 Karlsruhe, Baden | 29 | 2026-11-09 |
| 2 | [PMO - Manager Projektoffice – Schwerpunkt Projektsteuerung (w/m/d) - Stuttgart](https://www.arbeitsagentur.de/jobsuche/jobdetail/14087-CDYB1L3YXOMZP960-S) | ACS Services GmbH | 70191 Stuttgart | 29 | 2026-11-09 |
| 2 | [IT Validation Consultant (w/m/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-280183-S) | Capgemini Deutschland | 70173 Stuttgart | 30 | 2026-11-06 |
| 2 | [Consultant (w/m/d) IT Projekt- und Programmmanagement](https://www.arbeitsagentur.de/jobsuche/jobdetail/13645-266419-S) | Campana & Schott | 70173 Stuttgart | 30 | 2026-11-06 |
| 2 | [Consultant Datenschutz als Volljurist (m/w/d), ab sofort in HH, Berlin, Köln, Stuttgart, München](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1003994242-S) | intersoft consulting services AG | 70173 Stuttgart | 30 | 2026-11-10 |
| 2 | [Projektleiter / Prozessberater (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10000-1208627692-S) | The Quality Group Systemberatung GmbH | Stuttgart | 30 | 2026-11-11 |
| 2 | [Business Analyst - Security Operations (m/w/d)](https://www.arbeitsagentur.de/jobsuche/jobdetail/10001-1003952592-S) | emagine GmbH | Stuttgart | 30 | 2026-11-03 |
<!-- JOBS:END -->
