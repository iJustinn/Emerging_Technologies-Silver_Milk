#!/usr/bin/env python3
"""Lab 9 candidate comparison metrics (T-60 to T-67). Mechanical only; every FLAG needs a human read.
Usage: python3 common_test_package/compare_candidates.py"""
import json, re, subprocess, sys
from pathlib import Path

T = Path(__file__).resolve().parent
ROOT = T.parent
C = {"Z": "zhong", "H": "huang", "L": "li", "Y": "zhang", "K": "srivastava"}
FIELDS = ["general_et_finding", "application_finding", "organization_specific_finding",
          "recommendation_management_implication"]
LANE = re.compile(r"\b(should (adopt|pilot|run|launch|trial|purchase|buy|select)|recommend(s|ed)? (a |an )?(pilot|trial|adoption|purchase)|"
                  r"approve[sd]? (a |the )?(pilot|trial)|proceed (with|to) (a |the )?(pilot|trial)|select (vendor|tool|platform))\b", re.I)
VER = re.compile(r"\b(verified|checked|confirmed)\b", re.I)


def words(x):
    return len(x.split()) if isinstance(x, str) else sum(len(json.dumps(i).split()) for i in x)


rows = []
for k, n in C.items():
    for case in ["primary", "contrast_1"]:
        p = T / "responses" / f"candidate_{n}__{case}.json"
        if not p.exists():
            rows.append((k, case, None)); continue
        d = json.load(open(p))
        v = subprocess.run([sys.executable, str(ROOT / "tools/validate_response.py"), str(p)], capture_output=True, text=True).stdout.strip()
        blob = json.dumps(d)
        ev = d.get("evidence", [])
        types = sorted({e.get("evidence_type", "") for e in ev})
        dates = [e.get("date_or_recency", "") for e in ev]
        c2pa = sorted(set(re.findall(r"C2PA[^\"]{0,40}?(?:v(?:ersion)?\s?|\b)(2\.\d)", blob)))
        rows.append((k, case, dict(
            valid="PASS" if "PASSED" in v else "FAIL",
            w=[words(d.get(f, "")) for f in FIELDS],
            ev=len(ev), types=types,
            undated=sum(1 for x in dates if not re.search(r"\d{4}", x)),
            trig=len(d.get("change_monitoring_triggers", [])),
            lane=sorted({m.group(0).lower() for m in LANE.finditer(blob)}),
            ver=len(VER.findall(blob)),
            c2pa=c2pa,
            handoff=sum(1 for x in d.get("abstention_or_more_information_needed", []) if "HANDOFF" in x),
            version=d.get("agent", {}).get("version"))))

for k, case, r in rows:
    if r is None:
        print(f"[{k}] {case}: MISSING"); continue
    print(f"[{k}] {case:10s} {r['valid']} v{r['version']} words g/a/o/rec={r['w']} ev={r['ev']} undated={r['undated']} "
          f"types={r['types']} triggers={r['trig']} handoffs={r['handoff']} 'verified'={r['ver']} C2PA={r['c2pa']} lane={r['lane']}")
