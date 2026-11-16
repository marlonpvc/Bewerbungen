#!/usr/bin/env python3
"""Job-Scanner: sucht passende Einstiegsstellen über die Jobbörse der Bundesagentur für Arbeit.

Ergebnis:
  data/jobs.json        alle aktuell passenden Stellen (mit Score, Links, erstmals gesehen)
  data/neu/<datum>.md   die heute neu gefundenen Stellen
  README.md             Tabelle der besten aktuellen Treffer (zwischen den Markern)
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
import time
from pathlib import Path

import requests
import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
API = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v6/jobs"
HEADERS = {"X-API-Key": "jobboerse-jobsuche", "User-Agent": "bewerbungen-scanner/1.0"}
DETAIL_URL = "https://www.arbeitsagentur.de/jobsuche/jobdetail/{refnr}"


def lade_config() -> dict:
    return yaml.safe_load((ROOT / "config.yaml").read_text(encoding="utf-8"))


def suche(begriff: str, cfg: dict, session: requests.Session) -> list[dict]:
    region = cfg["region"]
    treffer: list[dict] = []
    for seite in range(1, 6):  # max. 500 Treffer pro Begriff
        params = {
            "was": begriff,
            "wo": region["wo"],
            "umkreis": region["umkreis_km"],
            "angebotsart": 1,  # Arbeit (keine Ausbildung/Praktika)
            "veroeffentlichtseit": region["veroeffentlicht_seit_tagen"],
            "size": 100,
            "page": seite,
        }
        for versuch in range(3):
            try:
                r = session.get(API, params=params, headers=HEADERS, timeout=30)
                if r.status_code == 200:
                    break
                print(f"  HTTP {r.status_code} für '{begriff}' (Versuch {versuch + 1})", file=sys.stderr)
            except requests.RequestException as e:
                print(f"  Fehler für '{begriff}': {e}", file=sys.stderr)
            time.sleep(2 * (versuch + 1))
        else:
            break
        daten = r.json()
        angebote = daten.get("ergebnisliste") or daten.get("stellenangebote") or []
        treffer.extend(angebote)
        if len(angebote) < 100:
            break
        time.sleep(0.5)
    return treffer


def muster(begriff: str) -> re.Pattern:
    b = begriff.strip().lower()
    if len(b) <= 3:
        return re.compile(rf"\b{re.escape(b)}\b")
    return re.compile(rf"\b{re.escape(b)}")


def bewerte(titel: str, cfg: dict) -> int | None:
    t = f" {titel.lower()} "
    for aus in cfg["ausschluss"]:
        if muster(aus).search(t):
            return None
    score = sum(p for k, p in cfg["punkte"].items() if muster(k).search(t))
    return min(score, 10)


def zahl(wert) -> int | None:
    try:
        return round(float(wert))
    except (TypeError, ValueError):
        return None


def normalisiere(a: dict, begriff: str, cfg: dict) -> dict | None:
    titel = (a.get("stellenangebotsTitel") or a.get("titel") or a.get("hauptberuf") or "").strip()
    score = bewerte(titel, cfg)
    if score is None or score == 0:
        return None
    lok = (a.get("stellenlokationen") or [{}])[0].get("adresse") or a.get("arbeitsort") or {}
    refnr = a.get("referenznummer") or a.get("refnr") or ""
    gehalt = None
    if a.get("gehaltsspanneVon"):
        bis = a.get("gehaltsspanneBis")
        gehalt = f"{a['gehaltsspanneVon']:,}" + (f"–{bis:,}" if bis else "") + " €"
        gehalt = gehalt.replace(",", ".")
    return {
        "id": refnr,
        "titel": titel,
        "firma": (a.get("firma") or a.get("arbeitgeber") or "").strip(),
        "ort": " ".join(x for x in [lok.get("plz", ""), lok.get("ort", "")] if x).strip(),
        "entfernung_km": zahl(a.get("entfernung", lok.get("entfernung"))),
        "veroeffentlicht": a.get("datumErsteVeroeffentlichung") or a.get("aktuelleVeroeffentlichungsdatum"),
        "eintritt": (a.get("eintrittszeitraum") or {}).get("von") or a.get("eintrittsdatum"),
        "beruf": a.get("hauptberuf") or a.get("beruf"),
        "gehalt": gehalt,
        "befristung": a.get("vertragsdauer"),
        "score": score,
        "erweitert": (zahl(a.get("entfernung", lok.get("entfernung"))) or 0) > cfg["region"].get("kernregion_km", 50),
        "link_jobboerse": DETAIL_URL.format(refnr=refnr),
        "link_extern": a.get("externeUrl"),
        "suchbegriffe": [begriff],
    }


def main() -> None:
    cfg = lade_config()
    heute = dt.date.today().isoformat()
    DATA.mkdir(exist_ok=True)
    (DATA / "neu").mkdir(exist_ok=True)

    alt_pfad = DATA / "jobs.json"
    alt = {j["id"]: j for j in json.loads(alt_pfad.read_text())} if alt_pfad.exists() else {}
    gesehen_pfad = DATA / "gesehen.json"
    gesehen: dict[str, str] = json.loads(gesehen_pfad.read_text()) if gesehen_pfad.exists() else {}

    jobs: dict[str, dict] = {}
    session = requests.Session()
    for begriff in cfg["suchbegriffe"]:
        roh = suche(begriff, cfg, session)
        print(f"{begriff}: {len(roh)} Treffer")
        for a in roh:
            j = normalisiere(a, begriff, cfg)
            if not j or not j["id"]:
                continue
            if j["id"] in jobs:
                if begriff not in jobs[j["id"]]["suchbegriffe"]:
                    jobs[j["id"]]["suchbegriffe"].append(begriff)
                continue
            jobs[j["id"]] = j

    if not jobs:
        sys.exit("Keine Stellen gefunden – API-Problem? Daten bleiben unverändert.")

    # Dubletten (gleiche Firma + gleicher Titel, z. B. mehrere Standorte) zusammenfassen
    eindeutig: dict[tuple, dict] = {}
    for j in jobs.values():
        schluessel = (j["firma"].lower(), j["titel"].lower())
        if schluessel not in eindeutig or (j["entfernung_km"] or 999) < (eindeutig[schluessel]["entfernung_km"] or 999):
            eindeutig[schluessel] = j
    jobs = {j["id"]: j for j in eindeutig.values()}

    neue = []
    for j in jobs.values():
        j["erstmals_gesehen"] = gesehen.get(j["id"]) or alt.get(j["id"], {}).get("erstmals_gesehen") or heute
        if j["id"] not in gesehen:
            gesehen[j["id"]] = j["erstmals_gesehen"]
            neue.append(j)

    sortiert = sorted(jobs.values(), key=lambda j: (j["erweitert"], -j["score"], j["entfernung_km"] or 999))
    alt_pfad.write_text(json.dumps(sortiert, ensure_ascii=False, indent=1))
    # gesehen.json klein halten: nur letzte 120 Tage
    grenze = (dt.date.today() - dt.timedelta(days=120)).isoformat()
    gesehen = {k: v for k, v in gesehen.items() if v >= grenze}
    gesehen_pfad.write_text(json.dumps(gesehen, ensure_ascii=False, indent=0, sort_keys=True))

    neue.sort(key=lambda j: (j["erweitert"], -j["score"], j["entfernung_km"] or 999))
    (DATA / "neu" / f"{heute}.md").write_text(tabelle(neue, f"Neue Stellen am {heute}"), encoding="utf-8")
    schreibe_readme([j for j in sortiert if not j["erweitert"]][:60], len(sortiert), len(neue), heute)
    print(f"Fertig: {len(sortiert)} passende Stellen, davon {len(neue)} neu.")


def tabelle(jobs: list[dict], ueberschrift: str) -> str:
    zeilen = [f"## {ueberschrift}", "", f"{len(jobs)} Stellen", "",
              "| Score | Stelle | Firma | Ort | km | Veröffentlicht |", "|---|---|---|---|---|---|"]
    for j in jobs:
        link = j["link_extern"] or j["link_jobboerse"]
        titel = j["titel"].replace("|", "/")
        zeilen.append(
            f"| {j['score']} | [{titel}]({link}) | {j['firma'].replace('|', '/')} | {j['ort']} | "
            f"{j['entfernung_km'] if j['entfernung_km'] is not None else ''} | {j['veroeffentlicht'] or ''} |"
        )
    return "\n".join(zeilen) + "\n"


def schreibe_readme(top: list[dict], gesamt: int, neu: int, heute: str) -> None:
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    block = (f"<!-- JOBS:START -->\n_Stand {heute}: {gesamt} passende Stellen, {neu} neu seit dem letzten Lauf._\n\n"
             + tabelle(top, "Top-Treffer") + "<!-- JOBS:END -->")
    text = re.sub(r"<!-- JOBS:START -->.*?<!-- JOBS:END -->", block, text, flags=re.S)
    readme.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
