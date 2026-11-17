#!/usr/bin/env python3
"""Lab 9 Landscape-specific §4 checks (on top of check_common.py). FLAG = needs a human read.
Usage: check_landscape_lab09.py <response.json> <case.json> [--pair <other_response.json> [--same-app]]
--pair compares Step 1 labels (and Step 2 labels with --same-app) across two runs on one technology."""
import argparse, json, re

ap = argparse.ArgumentParser()
ap.add_argument("response"); ap.add_argument("case")
ap.add_argument("--pair"); ap.add_argument("--same-app", action="store_true")
a = ap.parse_args()
r = json.load(open(a.response)); case = json.load(open(a.case))
out = []
def chk(name, ok, detail=""): out.append(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")
def flag(name, ok, detail=""): out.append(f"{'PASS' if ok else 'FLAG'}  {name}  {detail}")

SETS = {"L1 TECHNICAL CAPABILITY": ["Emerging", "Developing", "Established"],
        "L2 USE-CASE EVIDENCE": ["Demonstrations dominate", "Use cases emerging", "Use cases routine"],
        "L4 VENDOR/ECOSYSTEM STRUCTURE": ["Fragmented", "Consolidating", "Concentrated"],
        "L5 STANDARDS & REGULATION": ["None specific", "Emerging", "Established"],
        "L6 PRICE/PERFORMANCE": ["Falling", "Stable", "Rising", "Mixed"],
        "L7 COVERAGE TONE": ["Enthusiastic", "Mixed", "Backlash", "Steady"]}
TABLE = {("Met", "Toward"): "Landscape not the constraint", ("Met", "None"): "Landscape not the constraint",
         ("Met", "Away"): "Landscape not the constraint", ("Partly met", "Toward"): "Active watch",
         ("Partly met", "None"): "Scheduled watch", ("Partly met", "Away"): "Scheduled watch",
         ("Not met", "Toward"): "Scheduled watch", ("Not met", "None"): "Background scan", ("Not met", "Away"): "Background scan"}
STANCES = sorted(set(TABLE.values()))
TYPES = {"primary-technical", "primary-historical", "dated-market", "secondary", "inference", "case-premise"}
CLASSES = ["vendor-claim", "industry-analyst", "independent", "standards-regulatory", "adopter-self-report", "inference", "case-premise"]


def labels(resp):
    g = resp.get("general_et_finding", "")
    got = {}
    for lab, vals in SETS.items():
        m = re.search(re.escape(lab) + r":\s*(" + "|".join(map(re.escape, vals + ["Insufficient evidence"])) + r")\b", g)
        got[lab] = m.group(1) if m else None
    m = re.search(r"L3 TRACKER PLACEMENT:(.*?)(?=L4 )", g, re.S)
    got["L3"] = re.sub(r"\s+", " ", m.group(1)).strip()[:90] if m else None
    a_ = resp.get("application_finding", "")
    m = re.search(r"APPLICATION-SPECIFIC EVIDENCE:\s*(Present|Thin|Absent)", a_)
    got["APP EVIDENCE"] = m.group(1) if m else None
    m = re.search(r"STRONGEST ALTERNATIVE:\s*([^.—\-]{3,60})", a_)
    got["APP ALTERNATIVE"] = m.group(1).strip() if m else None
    return got


g = r.get("general_et_finding", ""); o = r.get("organization_specific_finding", "")
L = labels(r)
for lab in SETS:
    chk(f"{lab[:3]} label from allowed set", L[lab] is not None, f"({L[lab]})")
basis = re.findall(r"BASIS:\s*E\d", g)
chk("BASIS on L1, L2, L4–L7 (≥6)", len(basis) >= 6, f"({len(basis)})")
chk("L3 present", L["L3"] is not None, f"({L['L3']})")
asof = re.search(r"AS OF:\s*(20\d\d)-(\d\d)", g)
am = int(asof.group(1)) * 12 + int(asof.group(2)) if asof else 2026 * 12 + 11
l3full = re.search(r"L3 TRACKER PLACEMENT:(.*?)(?=L4 )", g, re.S)
old = [f"{y}-{mo}" for y, mo in re.findall(r"\b(20\d\d)-(\d\d)", l3full.group(1) if l3full else "") if am - (int(y) * 12 + int(mo)) > 24]
flag("L3 placement >24 months old is marked Stale (R-11)", not old or "Stale" in (l3full.group(1) if l3full else ""), f"({old})")
chk("POSITION present, no score", "POSITION:" in g and not re.search(r"\b\d+(\.\d+)?\s*/\s*10\b|score of", g, re.I))

cs = re.search(r"CONDITION STATUS:\s*(Met|Partly met|Not met)", o)
mv = re.search(r"MOVEMENT:\s*(Toward|None|Away)", o)
st = re.search(r"STANCE:\s*(" + "|".join(STANCES) + ")", o)
if cs and mv and st:
    chk("STANCE matches table (R-5)", TABLE[(cs.group(1), mv.group(1))] == st.group(1), f"({cs.group(1)} × {mv.group(1)} → {st.group(1)})")
else:
    chk("CONDITION STATUS / MOVEMENT / STANCE present", False, f"({bool(cs)}, {bool(mv)}, {bool(st)})")
rec = r.get("recommendation_management_implication", "")
chk("Recommendation starts with the same STANCE", bool(st) and rec.startswith(f"STANCE: {st.group(1)}"), rec[:45])
for lab in ["EXECUTION GATES:", "RELEVANT SIGNALS:", "POPULAR BUT NOT DECISIVE HERE:", "MOST CONSEQUENTIAL DEVELOPMENT:",
            "ECOSYSTEM DEPENDENCY:", "OPTIONS DOCUMENTED:"]:
    chk(f"{lab} present", lab in o)
chk("OPTIONS DOCUMENTED says NO SELECTION", "NO SELECTION" in o)
# R-8: gate words inside RELEVANT SIGNALS / MOST CONSEQUENTIAL
gate = re.compile(r"\b(terms|permission|rights|retention|security review|procurement|authori[sz]ation|contract)\b", re.I)
for lab in ["RELEVANT SIGNALS:", "MOST CONSEQUENTIAL DEVELOPMENT:"]:
    m = re.search(re.escape(lab) + r"(.*?)(?=[A-Z][A-Z /&\-]{6,}:|$)", o, re.S)
    hits = sorted({h.lower() for h in gate.findall(m.group(1))}) if m else []
    flag(f"R-8 gate words in {lab[:-1]}", not hits, str(hits))

# F2 (v1.0): MOVEMENT Toward may not rest only on vendor-claim / adopter-self-report items
cls = {}
for e in r.get("evidence", []):
    mm = re.match(r"(E\d+):", e.get("claim", "")); sc_ = re.search(r"SOURCE CLASS:\s*([a-z\-]+)", e.get("notes", ""))
    if mm and sc_: cls[mm.group(1)] = sc_.group(1)
mvb = re.search(r"MOVEMENT:\s*Toward.*?BASIS:\s*((?:E\d+[,\s]*)+)", o, re.S)
if mvb:
    ids = re.findall(r"E\d+", mvb.group(1)); kinds = {cls.get(i, "?") for i in ids}
    chk("F2 Toward not only vendor/self-report items", not kinds <= {"vendor-claim", "adopter-self-report"}, f"{ids} {sorted(kinds)}")
lim = " ".join(r.get("contrary_evidence_or_limitations", []))
for lab in ["COMPETING READING:", "CHASM EVIDENCE FOR:", "CHASM EVIDENCE AGAINST:", "DISTINGUISHING EVIDENCE:", "STALE/HYPE FLAG:"]:
    chk(f"{lab} present", lab in lim)
m = re.search(r"STALE/HYPE FLAG:(.*?)(?=CORRECTION:|$)", lim, re.S)
sf = m.group(1) if m else ""
chk("Flag has CONTROL and REFRESH BY date", "CONTROL:" in sf and bool(re.search(r"REFRESH BY:\s*20\d\d-\d\d", sf)))
chk("Flag names a dated claim (E-number or case location, a date)", bool(re.search(r"\bE\d+\b|memo|case|business_need|additional_context", sf)) and bool(re.search(r"20\d\d", sf)))

conf = r.get("confidence_and_uncertainty", "")
chk("CONFIDENCE label", bool(re.match(r"CONFIDENCE:\s*(Low|Moderate|High)", conf)), conf[:30])

trig = r.get("change_monitoring_triggers", [])
tl = [t for t in trig if t.startswith("TRIGGER")]
chk("2–4 TRIGGER lines", 2 <= len(tl) <= 4, f"({len(tl)})")
bad = [i for i, t in enumerate(tl) if not re.search(r"\[L\d\]\s*(CAPABILITY|USE-CASE|ECOSYSTEM|REGULATORY|PRICE|REVERSAL)", t)
       or not all(k in t for k in ["SOURCE:", "OWNER:", "CADENCE:", "→"])]
chk("Each trigger: [L<n>] TYPE, SOURCE, OWNER, CADENCE, →", not bad, f"bad {bad}")
if st:
    same = [i for i, t in enumerate(tl) if t.split("→")[-1].strip().startswith(st.group(1))]
    chk("No trigger lands on the current stance (R-7)", not same, f"{same}")
chk("One REVERSAL trigger", any("REVERSAL" in t for t in tl))
chk("REVIEW DATE present", any(t.startswith("REVIEW DATE:") for t in trig))
case_nums = set(re.findall(r"\d+(?:\.\d+)?", json.dumps(case)))
inv = []
for t in tl:
    body = re.sub(r"20\d\d-\d\d(-\d\d)?|\[L\d\]|TRIGGER \d|E\d+", "", t)
    for n in re.findall(r"\b\d+(?:\.\d+)?%?|\b\d+ of \d+", body):
        if n.rstrip("%") not in case_nums:
            inv.append(n)
flag("Numbers in triggers not given by the case (R-7)", not inv, str(sorted(set(inv))))

ev = r.get("evidence", [])
chk("6–12 evidence items", 6 <= len(ev) <= 12, f"({len(ev)})")
chk("evidence_type in team set", all(e.get("evidence_type") in TYPES for e in ev), str(sorted({e.get('evidence_type') for e in ev} - TYPES)))
sc = [re.search(r"SOURCE CLASS:\s*([a-z\-]+)", e.get("notes", "")) for e in ev]
chk("Every note has SOURCE CLASS from the set", all(s and s.group(1) in CLASSES for s in sc))
used = {s.group(1) for s in sc if s}
chk("≥4 source classes", len(used) >= 4, str(sorted(used)))
chk("Claims numbered E<n>:", all(re.match(r"E\d+:", e.get("claim", "")) for e in ev))
und = [e.get("date_or_recency") for e in ev if not re.search(r"\d{4}", e.get("date_or_recency", ""))]
chk("Every item dated", not und, str(und))
blob = json.dumps(r)
stds = re.findall(r"C2PA[^\"]{0,30}?(?:version|v)\s?(2\.\d)", blob)
flag("C2PA version cited (latest is 2.5 as of 2026-10; R-11)", all(v == "2.5" for v in stds), str(sorted(set(stds))))
ho = [x for x in r.get("abstention_or_more_information_needed", []) if x.startswith("HANDOFF")]
chk("Six HANDOFF lines", len(ho) >= 6, f"({len(ho)})")
lane = re.findall(r"\b(should (adopt|pilot|launch|purchase|select)|we recommend (adopting|piloting)|select (vendor|tool)|recommend(ed)? (vendor|tool|product))\b", blob, re.I)
chk("No lane violation (R-12)", not lane, str(lane[:3]))
caps = {"general_et_finding": 300, "application_finding": 150, "organization_specific_finding": 320, "recommendation_management_implication": 150}
for f, c in caps.items():
    n = len(r.get(f, "").split())
    chk(f"{f} ≤{c} words", n <= c, f"({n})")

if a.pair:
    P = labels(json.load(open(a.pair)))
    keys = list(SETS) + (["APP EVIDENCE"] if a.same_app else [])
    diff = {k: (L[k], P[k]) for k in keys if L[k] != P[k]}
    chk("Pair: Step 1 labels identical (R-3)" + (" + Step 2" if a.same_app else ""), not diff, str(diff))
    flag("Pair: L3 text identical", L["L3"] == P["L3"], f"({L['L3']} | {P['L3']})")
print("\n".join(out))
