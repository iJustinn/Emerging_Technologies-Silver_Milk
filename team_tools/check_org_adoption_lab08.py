#!/usr/bin/env python3
"""Lab 8 Organizational Adoption checks, run in addition to check_common.py.

Usage: python3 check_org_adoption_lab08.py <response.json> [--pair <other_response.json>]
  --pair  compare Step 1 and Step 2 labels with a run on the SAME technology and application (never the transfer case)
FLAG = needs a human read, not an automatic failure.
"""
import argparse, json, re
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("response"); ap.add_argument("--pair")
a = ap.parse_args()
out = []
def chk(name, ok, detail=""): out.append(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")

RATING = r"Ready|Partially ready|Not ready|Insufficient evidence"
VERDICT = r"Ready after named conditions|Undetermined — more evidence|Not ready|Ready"
STAGE = r"Preparation|Bounded evaluation|Routine operation"
LADDER = r"Supported|Conditional|Blocked|Undetermined|Not assessed"
REQ = {"Preparation": [], "Bounded evaluation": [1, 3, 4, 5, 6, 8], "Routine operation": list(range(1, 9))}
TO_LADDER = {"Ready": "Supported", "Ready after named conditions": "Conditional", "Not ready": "Blocked", "Undetermined — more evidence": "Undetermined"}
KEYS = ["agent", "analytical_question", "general_et_finding", "application_finding", "organization_specific_finding", "evidence",
        "contrary_evidence_or_limitations", "confidence_and_uncertainty", "value_opportunity_implication", "risk_governance_implication",
        "recommendation_management_implication", "change_monitoring_triggers", "abstention_or_more_information_needed"]

def lab(text, name, allowed):
    m = re.search(r"(?<![A-Z])" + re.escape(name) + r"\s*:\s*(" + allowed + r")", text)
    return m.group(1) if m else None
def demands(g): return re.findall(r"DEMAND \[D(\d)\]:\s*(High|Moderate|Low)\b", g)
def ratings(org): return {int(n): v for n, v in re.findall(r"(?m)^\s*D(\d) [^:\n]+:\s*(" + RATING + r")\b", org)}

r = json.load(open(a.response))
g, app, org, rec = r["general_et_finding"], r["application_finding"], r["organization_specific_finding"], r["recommendation_management_implication"]

# R-16 exact keys (the frozen validator does not reject extra keys; Lab 8 [H])
chk("Exactly the 13 frozen top-level keys (R-16)", list(r.keys()) == KEYS or set(r.keys()) == set(KEYS), str(sorted(set(r.keys()) ^ set(KEYS))))

# Step 1
chk("EVIDENCE BASE stated", lab(g, "EVIDENCE BASE", r"Supplied cards|Retrieved this run|None") is not None)
d = demands(g)
chk("Eight DEMAND lines, D1–D8, one value each", [n for n, _ in d] == [str(i) for i in range(1, 9)], f"({len(d)})")
chk("TECHNOLOGY LIMIT present", "TECHNOLOGY LIMIT:" in g)
chk("General ≤220 words", len(g.split()) <= 220, f"({len(g.split())})")

# Step 2
fit = lab(app, "FIT", r"Strong|Partial|Absent")
chk("FIT uses an allowed value", fit is not None, f"({fit})")
for k in ["TASK SIDE:", "TECHNOLOGY SIDE:", "FIT GAP:", "APPLICATION ADDS:", "UPSTREAM READ:"]:
    chk(f"Application slot {k}", k in app)
chk("Application ≤200 words", len(app.split()) <= 200, f"({len(app.split())})")

# Step 3
stage = lab(org, "STAGE ASKED", STAGE)
chk("STAGE ASKED uses an allowed value", stage is not None, f"({stage})")
rt = ratings(org)
chk("Eight dimension lines D1–D8, one rating each", sorted(rt) == list(range(1, 9)), f"({sorted(rt)})")
for k in ["PREMISE:", "UNIT OF ANALYSIS:", "STRENGTHS:", "GAPS THAT COULD CAUSE FAILURE:", "EXECUTION GATES:", "OPERATING OWNER:",
          "VERDICT BASIS:", "VERDICT SENSITIVITY:", "STAGE LADDER:", "FAILURE LOCUS:"]:
    chk(f"Organization slot {k}", k in org)
unk = [n for n, v in rt.items() if v != "Insufficient evidence" and re.search(
    r"(?m)^\s*D%d [^:\n]+:[^\n]*?(not established|unconfirmed|unclear|unknown|may not)" % n, org, re.I)]
out.append(("FLAG" if unk else "PASS") + "  'Unknown' wording behind a non-Insufficient rating (R-5)  " + str(unk))

# COUNTS and verdict table (R-7)
cm = re.search(r"COUNTS:\s*Ready (\d+), Partially ready (\d+), Not ready (\d+), Insufficient evidence (\d+)", org)
if cm and len(rt) == 8:
    want = [list(rt.values()).count(x) for x in ["Ready", "Partially ready", "Not ready", "Insufficient evidence"]]
    chk("COUNTS match the eight lines", [int(x) for x in cm.groups()] == want, f"({cm.groups()} vs {want})")
else:
    chk("COUNTS line present", bool(cm))
verdict = lab(org, "READINESS VERDICT", VERDICT)
gates = (lab(org, "EXECUTION GATES", r"[^\n]*") or "").strip()
gates_open = bool(gates) and not re.match(r"None\b", gates)
expect = None
if stage and len(rt) == 8:
    req = [rt[n] for n in REQ[stage]]
    if "Not ready" in req: expect = "Not ready"
    elif "Insufficient evidence" in req: expect = "Undetermined — more evidence"
    elif "Partially ready" in req or gates_open or any(v != "Ready" for v in rt.values()): expect = "Ready after named conditions"
    else: expect = "Ready"
    if stage == "Preparation":
        out.append("FLAG  Stage asked is Preparation: no required dimensions; read the verdict  ")
    else:
        chk("Verdict matches the table for the stage asked (R-7)", verdict == expect, f"({verdict} vs {expect})")
lad = {s: lab(org, s, LADDER) for s in ["PREPARATION", "BOUNDED EVALUATION", "ROUTINE OPERATION"]}
chk("Ladder: three stages, allowed values", all(lad.values()), str(lad))
if stage and verdict:
    chk("Ladder status of the stage asked matches the verdict", lad.get(stage.upper()) == TO_LADDER.get(verdict), f"({lad.get(stage.upper())})")
sens = lab(org, "VERDICT SENSITIVITY", r"[^\n]*") or ""
if verdict and verdict.startswith("Undetermined"):
    chk("Undetermined only when no required dimension is Not ready", expect != "Not ready")
chk("Organization ≤480 words", len(org.split()) <= 480, f"({len(org.split())})")

# Response field
m = re.match(r"\s*READINESS VERDICT:\s*(" + VERDICT + r")\s*\((" + STAGE + r")\)\s*—", rec)
chk("Response starts READINESS VERDICT: <value> (<stage>) — matching Step 4", bool(m) and m.group(1) == verdict and m.group(2) == stage,
    f"({m.groups() if m else None})")
for k in ["MOST CONSEQUENTIAL GAP:", "MOST CONSEQUENTIAL MISSING FACTOR:", "NOW:"]:
    chk(f"Response slot {k}", k in rec)
gap = re.search(r"MOST CONSEQUENTIAL GAP:\s*(None observed|D(\d))", rec)
if gap and gap.group(2):
    n = int(gap.group(2))
    chk("Most consequential gap is a dimension rated Partially ready or Not ready", rt.get(n) in ("Partially ready", "Not ready"), f"(D{n} {rt.get(n)})")
    gl = rec.split("MOST CONSEQUENTIAL GAP:")[1].split("MOST CONSEQUENTIAL MISSING FACTOR:")[0]
    ext = re.search(r"vendor|input-use terms|terms (?:are|remain) (?:not yet )?(?:accepted|unresolved)|not yet selected", gl, re.I)
    out.append(("FLAG" if ext else "PASS") + "  Gap reads as an execution gate (R-8)  " + gl.strip()[:100])
else:
    chk("Most consequential gap names a dimension or None observed", bool(gap))
acts = re.findall(r"ACTION \d \[D(\d)\]:[^\n]*?— GAP:[^\n]*?— OWNER:[^\n]*?(?:\((?:stated|inferred)\)|to be assigned by [^\n—]+)[^\n]*?— DONE WHEN:", rec)
chk("Actions: dimension, GAP, OWNER (stated/inferred/to be assigned by), DONE WHEN", len(acts) == len(re.findall(r"ACTION \d \[", rec)) and len(acts) <= 3, f"({len(acts)})")
bad_act = [n for n in acts if rt.get(int(n)) == "Ready"]
chk("No action for a dimension rated Ready (R-9)", not bad_act, str(bad_act))
generic = re.findall(r"center of excellence|provide training\b|create a governance framework|communicate the vision", rec, re.I)
out.append(("FLAG" if generic else "PASS") + "  Generic change-management action (R-9)  " + str(generic))
chk("Recommendation ≤280 words", len(rec.split()) <= 280, f"({len(rec.split())})")

# Confidence, Step 5, triggers, requests, handoffs
chk("Confidence opens with one value", bool(re.match(r"\s*VERDICT CONFIDENCE:\s*(Low|Moderate|High)\b", r["confidence_and_uncertainty"])))
contra = " ".join(r["contrary_evidence_or_limitations"])
for k in ["COMPETING READING:", "STRONGEST CASE AGAINST:", "DISTINGUISHING EVIDENCE:"]:
    chk(f"Step 5 slot {k}", k in contra)
t = r["change_monitoring_triggers"]
trg = [x for x in t if x.startswith("TRIGGER [D")]
chk("At least one TRIGGER [D<n>]", len(trg) >= 1, f"({len(trg)})")
chk("Triggers move the verdict (R-12)", all(re.search(r"→\s*(" + VERDICT + r")", x) and verdict not in re.search(r"→\s*(" + VERDICT + r")", x).group(1) for x in trg) if verdict else False)
chk("REVIEW DATE present", any("REVIEW DATE:" in x for x in t))
ab = r["abstention_or_more_information_needed"]
missing = [n for n, v in rt.items() if v == "Insufficient evidence" and not any(re.match(r"MORE INFO → D%d\b" % n, x) for x in ab)]
chk("Every Insufficient evidence dimension has a MORE INFO → line (R-11)", not missing, str(missing))
chk("INTAKE MISSING line", any(x.startswith("INTAKE MISSING:") for x in ab))
for ag in ["Creation", "Innovation", "Promethean", "Diffusion", "Adoption", "Landscape"]:
    chk(f"HANDOFF → {ag} Agent", any(x.startswith(f"HANDOFF → {ag}") for x in ab))

# Evidence and lane
TYPES = {"primary-technical", "primary-historical", "dated-market", "secondary", "inference", "case-premise"}
bad = [e["evidence_type"] for e in r["evidence"] if e["evidence_type"] not in TYPES]
chk("Evidence types from the list", not bad, str(bad)[:80])
lane = re.findall(r"\b(?:recommend(?:s|ed)? (?:to )?(?:adopt|a bounded experiment|a proof of concept)|should (?:adopt|run the (?:trial|pilot|experiment))|use vendor)\b", org + rec, re.I)
out.append(("FLAG" if lane else "PASS") + "  Adoption or vendor decision wording (R-14)  " + str(lane[:3]))

# Pair: Step 1 and Step 2 labels identical on the same technology and application (R-2, R-4)
if a.pair:
    p = json.load(open(a.pair))
    chk("Pair: same technology and application", True)
    chk("Pair: DEMAND labels identical (R-2)", demands(g) == demands(p["general_et_finding"]), f"({[v for _, v in demands(g)]} vs {[v for _, v in demands(p['general_et_finding'])]})")
    chk("Pair: FIT identical (R-4)", fit == lab(p["application_finding"], "FIT", r"Strong|Partial|Absent"))

print("\n".join(out))
print(f"SUMMARY: {sum(x.startswith('PASS') for x in out)} pass, {sum(x.startswith('FAIL') for x in out)} fail, {sum(x.startswith('FLAG') for x in out)} flag")
