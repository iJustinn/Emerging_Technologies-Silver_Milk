#!/usr/bin/env python3
"""Lab 5 Promethean Classification checks, run in addition to check_common.py.

Usage: python3 check_promethean_lab05.py <response.json> [--pair <other_response.json>] [--posture-pair]
  --pair          compare Step 1 labels and confidence lines with a run on the SAME technology and cards (never the transfer case)
  --posture-pair  the pair differs only in adoption posture: weight must match, POSTURE EFFECT must differ
FLAG = needs a human read, not an automatic failure.
"""
import argparse, json, re

ap = argparse.ArgumentParser()
ap.add_argument("response"); ap.add_argument("--pair"); ap.add_argument("--posture-pair", action="store_true")
a = ap.parse_args()
out = []
def chk(name, ok, detail=""): out.append(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")

CLASS = r"Indeterminate \(Breakthrough \| Potential Promethean\)|Indeterminate \(Incremental \| Breakthrough\)|Withheld — insufficient evidence|Potential Promethean|Breakthrough|Incremental"
def lab(text, name, allowed):
    m = re.search(re.escape(name) + r"\s*:\s*(" + allowed + r")", text)
    return m.group(1) if m else None

def step1(g):
    return {"EVIDENCE BASE": lab(g, "EVIDENCE BASE", r"Supplied cards|Retrieved this run"),
            "LAYER 1": lab(g, "LAYER 1", r"System|Component"),
            "DISSOLUTION": lab(g, "DISSOLUTION", r"Dissolved|Reduced|Not yet determinable"),
            "EARLIEST UNRESOLVED GATE": lab(g, "EARLIEST UNRESOLVED GATE", r"Layer 1|Barrier|Suppression|Dissolution|Tiers|Layer 3|None"),
            "SIGNIFICANCE CLASS": lab(g, "SIGNIFICANCE CLASS", CLASS),
            "MODE": lab(g, "MODE", r"Prospective|Retrospective|Confirmed"),
            "CEILING": lab(g, "CEILING", r"Potential Promethean")}

def conf(r):
    c = r["confidence_and_uncertainty"]
    c = c if isinstance(c, str) else " ".join(c)
    m1 = re.search(r"CONFIDENCE AT LEAST ([^:]+):\s*(Low|Moderate|High|n/a)", c)
    m2 = re.search(r"CONFIDENCE NOT HIGHER:\s*(Low|Moderate|High|n/a)", c)
    return (m1.group(1).strip() + "=" + m1.group(2)) if m1 else None, m2.group(1) if m2 else None

def weight(org):
    return lab(org, "WEIGHT OF BROAD SIGNIFICANCE ON THIS DECISION", r"Low|Moderate|High")

r = json.load(open(a.response))
g, app, org, rec = r["general_et_finding"], r["application_finding"], r["organization_specific_finding"], r["recommendation_management_implication"]
s1 = step1(g)
for k, v in s1.items():
    chk(f"Step 1 label {k} uses an allowed value", v is not None, f"({v})")
chk("MODE is Prospective (R-7)", s1["MODE"] == "Prospective")
for k in ["UNIT CLASSIFIED:", "PARENT SYSTEM:", "BARRIER STATEMENT:", "SUPPRESSION TEST:", "LAYER 3 CRITERIA:", "WHY NOT LOWER:", "HIGHER-SIGNIFICANCE HYPOTHESIS:"]:
    chk(f"General slot {k}", k in g)
chk("Suppression test has Observed and Prospective parts", bool(re.search(r"Observed", g)) and bool(re.search(r"Prospective\s*[—:-]", g)))
d = s1["DISSOLUTION"]
if d == "Dissolved":
    chk("TIERS: slot present after Dissolved", bool(re.search(r"(?<!DISSOLVED, )TIERS:", g)))
else:
    chk("IF DISSOLVED, TIERS: slot present when not Dissolved", "IF DISSOLVED, TIERS:" in g)
    chk("Layer 3 not scored before Dissolved (R-4)", bool(re.search(r"LAYER 3 CRITERIA:\s*not scored", g)))
c = s1["SIGNIFICANCE CLASS"]
if c == "Potential Promethean":
    chk("Ceiling self-check: Potential Promethean needs Dissolved (R-5)", d == "Dissolved")
if c and c.startswith("Indeterminate (Breakthrough"):
    chk("Ceiling self-check: Indeterminate (B | PP) only via Not yet determinable (R-9)", d == "Not yet determinable")
if c and c.startswith("Indeterminate (Incremental"):
    chk("Ceiling self-check: Indeterminate (I | B) only with Reduced (R-9)", d == "Reduced")
if c == "Incremental":
    out.append("FLAG  Incremental: confirm affirmative comparative evidence, not missing higher evidence (R-5)")
chk("No 'provisionally' Promethean escape (R-9)", not re.search(r"Potential(ly)? Promethean[^.]{0,30}provisional", g, re.I))
chk("General finding ≤350 words", len(g.split()) <= 350, f"({len(g.split())})")

chk("APPLICATION SIGNIFICANCE uses an allowed label", lab(app, "APPLICATION SIGNIFICANCE", r"Incremental|Breakthrough") is not None)
chk("Application finding ≤150 words", len(app.split()) <= 150, f"({len(app.split())})")
for k in ["UNIT OF ANALYSIS", "CORE ACTIVITY ON BARRIER", "CONSEQUENCE FOR THE ORGANIZATION", "REVERSIBILITY OF THE DECISION", "WINDOW EVIDENCE", "WEIGHT OF BROAD SIGNIFICANCE ON THIS DECISION", "POSTURE EFFECT"]:
    chk(f"Org label {k}", k + ":" in org)
core = lab(org, "CORE ACTIVITY ON BARRIER", r"Yes|No"); win = lab(org, "WINDOW EVIDENCE", r"Dated|None found")
table = {("No", "None found"): "Low", ("No", "Dated"): "Moderate", ("Yes", "None found"): "Moderate", ("Yes", "Dated"): "High"}
w = weight(org)
chk("Weight read from the table (R-12)", w is not None and table.get((core, win)) == w, f"({core}, {win} -> {w})")
pe = re.search(r"POSTURE EFFECT:(.*)$", org, re.S)
pe_text = pe.group(1) if pe else ""
dirw = re.findall(r"\b(adopt\w*|pilot\w*|proceed\w*|roll ?out|deploy\w*|evaluat\w*)\b", pe_text, re.I)
chk("POSTURE EFFECT gives no adopt/pilot/evaluation direction (R-12)", not dirw, str(dirw))
chk("Org finding ≤300 words", len(org.split()) <= 300, f"({len(org.split())})")

con = " ".join(r.get("contrary_evidence_or_limitations", []))
for k in ["EVIDENCE FOR HIGHER CLASS", "EVIDENCE AGAINST HIGHER CLASS", "STRONGEST CASE FOR LOWER CLASS", "DISTINGUISHING EVIDENCE"]:
    chk(f"Step 4 label {k}", k in con)
c1, c2 = conf(r)
chk("Two-direction confidence lines (R-10)", bool(c1) and bool(c2), f"({c1}; NOT HIGHER={c2})")

m = re.match(r"WEIGHT:\s*(Low|Moderate|High)\s*—", rec)
chk("Recommendation starts 'WEIGHT: <level> —' and matches org weight", bool(m) and m.group(1) == w, f"({m.group(1) if m else None} vs {w})")
chk("Recommendation ≤150 words", len(rec.split()) <= 150, f"({len(rec.split())})")
lane = re.findall(r"\b(pilot\w*|proceed\w*|continue only|hold if|roll ?out|scale up|baseline|matched|paired|threshold|stop rule|acceptance criteria)\b", rec, re.I)
chk("Recommendation stays in lane (R-13)", not lane, str(lane))

ev = r.get("evidence", [])
bad_type = [e["evidence_type"] for e in ev if e["evidence_type"] not in
            {"primary-technical", "primary-historical", "dated-market", "secondary", "inference", "case-premise"}]
chk("evidence_type from the team list (R-14)", not bad_type, str(sorted(set(bad_type)))[:120])
if s1["EVIDENCE BASE"] == "Supplied cards":
    insp = [e["source_or_reference"][:50] for e in ev if e.get("notes", "").startswith("STATUS: inspected-this-run")]
    if insp:
        out.append(f"FLAG  Supplied cards, but {len(insp)} item(s) inspected this run: confirm no general label rests on them (R-2) {insp}")
ho = [x for x in r.get("abstention_or_more_information_needed", []) if x.startswith("HANDOFF")]
named = {n for n in ["Creation", "Innovation", "Diffusion", "Adoption", "Organizational Adoption", "Landscape"] if any(n in h for h in ho)}
chk("HANDOFF lines name the other six specialists", len(named) == 6, f"({sorted(named)})")

if a.pair:
    p = json.load(open(a.pair))
    p1 = step1(p["general_et_finding"])
    diff = {k: (s1[k], p1[k]) for k in s1 if s1[k] != p1[k]}
    chk("Same Step 1 labels as paired run (R-1, rerun test)", not diff and None not in s1.values(), str(diff or s1))
    chk("Same confidence lines as paired run", conf(r) == conf(p) and None not in conf(r), f"({conf(r)} vs {conf(p)})")
    if a.posture_pair:
        pw = weight(p["organization_specific_finding"])
        chk("Posture pair: same weight (posture never changes the weight)", w == pw, f"({w} vs {pw})")
        pp = re.search(r"POSTURE EFFECT:(.*)$", p["organization_specific_finding"], re.S)
        chk("Posture pair: POSTURE EFFECT differs", bool(pe and pp) and pe_text.strip() != pp.group(1).strip())
print("\n".join(out))
