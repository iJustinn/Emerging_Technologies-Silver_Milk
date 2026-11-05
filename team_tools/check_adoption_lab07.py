#!/usr/bin/env python3
"""Lab 7 Adoption checks, run in addition to check_common.py.

Usage: python3 check_adoption_lab07.py <response.json> [--pair <other_response.json>] [--posture-pair]
  --pair          compare Step 1 and Step 2 labels with a run on the SAME technology, application and evidence base (never the transfer case)
  --posture-pair  the pair differs only in adoption posture: the recommendation or POSTURE EFFECT must differ
FLAG = needs a human read, not an automatic failure.
"""
import argparse, json, re

ap = argparse.ArgumentParser()
ap.add_argument("response"); ap.add_argument("--pair"); ap.add_argument("--posture-pair", action="store_true")
a = ap.parse_args()
out = []
def chk(name, ok, detail=""): out.append(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")

ZONE = r"Bleeding edge|Leading edge|Commodity|Trailing edge"
REC = r"Adopt|Bounded experiment|Proof of concept|Monitor|Defer|Reject for now|Withheld — more evidence"
POSTURE = r"Innovator/early adopter|Fast follower|Conservative adopter"
def lab(text, name, allowed):
    m = re.search(r"(?<![A-Z])" + re.escape(name) + r"\s*:\s*(" + allowed + r")", text)
    return m.group(1) if m else None
GEN = {"EVIDENCE BASE": r"Supplied cards|Retrieved this run|None", "MATURITY ZONE": ZONE, "MESSAGING SHIFT": r"Observed|Not observed",
       "RELATIVE ADVANTAGE": r"Demonstrated|Claimed|Unclear"}
APP = {"APPLICATION ZONE": ZONE, "FIT": r"Strong|Partial|Absent", "ADVANTAGE OVER ALTERNATIVE": r"Clear|Marginal|None"}
ORG = {"ORG POSTURE": POSTURE, "CONSEQUENCE": r"Severe|Costly|Reversible", "REVERSIBILITY": r"High|Partial|Low",
       "CONFIGURATION": r"Acceptable|Unacceptable", "DEFER GATE": r"Present|None", "PRIMARY UNCERTAINTY": r"Feasibility|Value",
       "MODIFIER": r"applied|not applied", "RECOMMENDATION": REC}
TABLE = {"Bleeding edge": ("Bounded experiment", "Proof of concept", "Monitor"), "Leading edge": ("Adopt", "Adopt", "Bounded experiment"),
         "Commodity": ("Adopt", "Adopt", "Adopt"), "Trailing edge": ("Reject for now",) * 3}
COL = {"Innovator/early adopter": 0, "Fast follower": 1, "Conservative adopter": 2}
STEP = {"Adopt": "Bounded experiment", "Bounded experiment": "Proof of concept"}

r = json.load(open(a.response))
g, app, org, rec = r["general_et_finding"], r["application_finding"], r["organization_specific_finding"], r["recommendation_management_implication"]
gl = {k: lab(g, k, v) for k, v in GEN.items()}
al = {k: lab(app, k, v) for k, v in APP.items()}
ol = {k: lab(org, k, v) for k, v in ORG.items()}
for k, v in {**gl, **al, **ol}.items():
    chk(f"Label {k} uses an allowed value", v is not None, f"({v})")
for k in ["UNIT:", "PARENT:", "ZONE BASIS:", "DIFFUSION EVIDENCE:", "KEY UNCERTAINTY:"]:
    chk(f"General slot {k}", k in g)
for k in ["ZONE BASIS:", "BEST ALTERNATIVE:", "UPSTREAM READ:"]:
    chk(f"Application slot {k}", k in app)
for k in ["UNIT OF ANALYSIS:", "POSTURE GATE:", "SCOPING CONDITIONS:", "DEPARTURE:", "GATES:", "TABLE INPUT:", "POSTURE EFFECT:"]:
    chk(f"Organization slot {k}", k in org)
chk("Key uncertainty type", bool(re.search(r"KEY UNCERTAINTY:[^\n]*\b(Testable|External|Unbounded)\b", g)))
chk("General ≤220 words", len(g.split()) <= 220, f"({len(g.split())})")
chk("Application ≤200 words", len(app.split()) <= 200, f"({len(app.split())})")
chk("Organization ≤380 words", len(org.split()) <= 380, f"({len(org.split())})")
chk("Recommendation ≤300 words", len(rec.split()) <= 300, f"({len(rec.split())})")

# Procedure: the recommendation must follow the gates, table, uncertainty rule and modifier
final = ol["RECOMMENDATION"]; expect = None
if al["FIT"] == "Absent" or al["ADVANTAGE OVER ALTERNATIVE"] == "None" or ol["CONFIGURATION"] == "Unacceptable":
    expect = "Reject for now"
elif ol["DEFER GATE"] == "Present":
    expect = "Defer"
elif al["APPLICATION ZONE"] in TABLE and ol["ORG POSTURE"] in COL:
    expect = TABLE[al["APPLICATION ZONE"]][COL[ol["ORG POSTURE"]]]
    if expect == "Bounded experiment" and ol["PRIMARY UNCERTAINTY"] == "Feasibility": expect = "Proof of concept"
    if ol["CONSEQUENCE"] == "Severe": expect = STEP.get(expect, expect)
if final and final.startswith("Withheld"):
    out.append("FLAG  Withheld recommendation: read the EVIDENCE REQUEST lines  ")
else:
    chk("Recommendation matches gates, table, uncertainty rule and modifier (R-5)", final == expect, f"({final} vs {expect})")
tm = lab(org, "TABLE INPUT", r"[^\n]*")
reached = expect not in ("Defer", "Reject for now") if expect else True
if reached and al["APPLICATION ZONE"] in TABLE and ol["ORG POSTURE"] in COL:
    chk("TABLE INPUT uses the application zone and posture", bool(tm) and al["APPLICATION ZONE"] in tm and ol["ORG POSTURE"] in tm, f"({(tm or '')[:70]})")
else:
    chk("TABLE INPUT says Not reached when a gate decided", bool(tm) and "Not reached" in tm, f"({(tm or '')[:70]})")

# Response field
m = re.match(r"\s*RECOMMENDATION:\s*(" + REC + r")\s*—", rec)
chk("Response starts RECOMMENDATION: <value> — and matches Step 4", bool(m) and m.group(1) == final, f"({m.group(1) if m else None})")
for k in ["NOW:", "BEFORE EXECUTION:", "BEFORE WIDER USE:", "EXPERIMENT DESIGN:", "DECISIVE FACTORS:", "DRIVING FACTOR:"]:
    chk(f"Response slot {k}", k in rec)
chk("Decisive factors carry a level tag", bool(re.search(r"\[(General|Application|Organization)\]", rec)))
if final in ("Bounded experiment", "Proof of concept"):
    for k in ["HYPOTHESIS", "COMPARATOR", "SCOPE", "OWNER ROLE", "MEASURES", "PROPOSED ACCEPTANCE RULE", "PROPOSED STOP RULE"]:
        chk(f"Experiment design part {k} (I-06)", k in rec)
    chk("Experiment design marked pending approval", bool(re.search(r"pending (management )?approval", rec, re.I)))
elif final:
    chk("Experiment design Not applicable for this category", bool(re.search(r"EXPERIMENT DESIGN:\s*Not applicable", rec)))
if final == "Defer":
    gate = lab(org, "DEFER GATE", r"[^\n]*") or ""
    ordinary = re.search(r"no (tool|vendor|model)[^.;]*(selected|chosen)", gate, re.I)
    out.append(("FLAG" if ordinary else "PASS") + "  Defer gate is not only an ordinary precondition (R-6)  " + gate[:90])

# Step 5 and confidence
contra = " ".join(r["contrary_evidence_or_limitations"])
for k in ["ADVOCATE CASE:", "RISK OFFICER CASE:", "NEAREST ALTERNATIVE:", "BIAS CHECK:", "DISTINGUISHING EVIDENCE:"]:
    chk(f"Step 5 slot {k}", k in contra)
chk("BIAS CHECK covers all four", all(re.search(b, contra, re.I) for b in ["Novelty", "FOMO", "Sunk cost", "Excessive conservatism"]))
c = r["confidence_and_uncertainty"]
chk("Confidence opens with one value", bool(re.match(r"\s*RECOMMENDATION CONFIDENCE:\s*(Low|Moderate|High)\b", c)))
chk("ZONE CONFIDENCE present", "ZONE CONFIDENCE:" in c)

# Triggers and handoffs
t = r["change_monitoring_triggers"]; tj = " ".join(t)
chk("At least two categorized triggers", len([x for x in t if re.match(r"TRIGGER \[(new evidence|maturity|cost|regulation|peer adoption|internal capability)\]", x)]) >= 2)
chk("Trigger arrows name a recommendation", all(re.search(r"→\s*(" + REC + r")", x) for x in t if x.startswith("TRIGGER")))
for k in ["REVALIDATE:", "REVERSAL CONDITION:", "REVIEW DATE:"]:
    chk(f"Trigger slot {k}", k in tj)
ab = r["abstention_or_more_information_needed"]
for ag in ["Creation", "Innovation", "Promethean", "Diffusion", "Organizational Adoption", "Landscape"]:
    chk(f"HANDOFF → {ag} Agent", any(x.startswith(f"HANDOFF → {ag}") for x in ab))
chk("At least one EVIDENCE REQUEST", any(x.startswith("EVIDENCE REQUEST:") for x in ab))

# Evidence types and lane
TYPES = {"primary-technical", "primary-historical", "dated-market", "secondary", "inference", "case-premise"}
bad = [e["evidence_type"] for e in r["evidence"] if e["evidence_type"] not in TYPES]
chk("Evidence types from the list", not bad, str(bad)[:80])
adv = re.findall(r"(?:team|organization|retailer|staff) (?:is|are) (?:ready|capable|not ready|unable)", org + rec, re.I)
out.append(("FLAG" if adv else "PASS") + "  Readiness verdict wording (R-14)  " + str(adv))
stg = re.findall(r"\b(Early majority|Late majority|Early adopters|Laggards|Chasm)\b", g + app + org)
out.append(("FLAG" if stg else "PASS") + "  Diffusion stage word used here (I-17)  " + str(stg[:3]))
started = re.findall(r"\b(?:conduct|run|start|launch) the (?:trial|experiment|pilot|proof of concept)\b(?! only)", rec, re.I)
out.append(("FLAG" if started else "PASS") + "  Wording implies a test has started (R-7)  " + str(started[:2]))

if a.pair:
    o = json.load(open(a.pair))
    for k, v in GEN.items():
        chk(f"Pair: general {k} identical (R-4)", lab(o["general_et_finding"], k, v) == gl[k], f"({gl[k]} vs {lab(o['general_et_finding'], k, v)})")
    for k, v in APP.items():
        chk(f"Pair: application {k} identical (R-4)", lab(o["application_finding"], k, v) == al[k], f"({al[k]} vs {lab(o['application_finding'], k, v)})")
    if a.posture_pair:
        orec = lab(o["organization_specific_finding"], "RECOMMENDATION", REC)
        pe = lambda s: (re.search(r"POSTURE EFFECT:\s*([^\n]*)", s) or [None, ""])[1]
        chk("Posture pair: recommendation or POSTURE EFFECT differs", orec != final or pe(org) != pe(o["organization_specific_finding"]), f"({final} vs {orec})")
        out.append(f"INFO  Posture pair recommendations: {final} vs {orec}")
print("\n".join(out))
fails = sum(1 for x in out if x.startswith("FAIL"))
print(f"SUMMARY: {sum(1 for x in out if x.startswith('PASS'))} pass, {fails} fail, {sum(1 for x in out if x.startswith('FLAG'))} flag")
