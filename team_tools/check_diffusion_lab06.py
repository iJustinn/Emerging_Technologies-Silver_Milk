#!/usr/bin/env python3
"""Lab 6 Diffusion checks, run in addition to check_common.py.

Usage: python3 check_diffusion_lab06.py <response.json> [--pair <other_response.json>] [--posture-pair]
  --pair          compare Step 1 and Step 2 labels with a run on the SAME technology, application and cards (never the transfer case)
  --posture-pair  the pair differs only in adoption posture: TIMING or POSTURE EFFECT must differ
FLAG = needs a human read, not an automatic failure.
"""
import argparse, json, re

ap = argparse.ArgumentParser()
ap.add_argument("response"); ap.add_argument("--pair"); ap.add_argument("--posture-pair", action="store_true")
a = ap.parse_args()
out = []
def chk(name, ok, detail=""): out.append(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")

STAGE = r"Withheld — insufficient evidence|Innovators|Early adopters|Chasm|Early majority|Late majority|Laggards"
POSTURE = r"Innovator/early adopter|Fast follower|Conservative adopter"
TIMING = r"Urgency|Patience|Continued monitoring"
def lab(text, name, allowed):
    m = re.search(r"(?<![A-Z ])" + re.escape(name) + r"\s*:\s*(" + allowed + r")", text)
    return m.group(1) if m else None
def basis(text, after):
    m = re.search(re.escape(after) + r".*?STAGE BASIS:\s*([^\n]*)", text, re.S)
    return m.group(1) if m else ""

GEN = {"EVIDENCE BASE": r"Supplied cards|Retrieved this run", "USE LEVEL OBSERVED": r"Available|Piloted|In production|Scaled",
       "TECHNOLOGY STAGE": STAGE, "STANDARDS": r"Settled|Contested|None", "COMPLEMENTARY ASSETS": r"In place|Partial|Missing",
       "BASE CASE": r"Named|None", "MESSAGING SHIFT": r"Observed|Not observed", "NETWORK-EFFECT DEPENDENCY": r"Yes|No"}
FAC = ["RELATIVE ADVANTAGE", "COMPATIBILITY", "COMPLEXITY", "TRIALABILITY", "OBSERVABILITY"]
def step1(g):
    d = {k: lab(g, k, v) for k, v in GEN.items()}
    for f in FAC:
        d[f] = lab(g, f, r"(?:Favors|Neutral|Inhibits) · (?:Observed|Speculative)")
    d["MAIN INHIBITOR type"] = (re.search(r"MAIN INHIBITOR:[^\n]*?\b(Observed|Hypothesized)\b", g) or [None, None])[1]
    return d
def step2(app):
    return {"USE LEVEL OBSERVED": lab(app, "USE LEVEL OBSERVED", GEN["USE LEVEL OBSERVED"]), "APPLICATION STAGE": lab(app, "APPLICATION STAGE", STAGE)}

TABLE = {"Innovators": ("Urgency", "Continued monitoring", "Continued monitoring"),
         "Early adopters": ("Urgency", "Patience", "Continued monitoring"),
         "Chasm": ("Urgency", "Patience", "Continued monitoring"),
         "Early majority": ("Urgency", "Urgency", "Patience"),
         "Late majority": ("Urgency", "Urgency", "Urgency"), "Laggards": ("Urgency", "Urgency", "Urgency")}
COL = {"Innovator/early adopter": 0, "Fast follower": 1, "Conservative adopter": 2}

r = json.load(open(a.response))
g, app, org, rec = r["general_et_finding"], r["application_finding"], r["organization_specific_finding"], r["recommendation_management_implication"]
s1, s2 = step1(g), step2(app)
for k, v in s1.items():
    chk(f"Step 1 label {k} uses an allowed value", v is not None, f"({v})")
for k in ["UNIT:", "PARENT:", "STAGE BASIS:", "CHANGE AGENTS:", "OPINION LEADERS:", "STRONGEST SIGNAL:", "MAIN INHIBITOR:"]:
    chk(f"General slot {k}", k in g)
spec = [f for f in FAC if re.search(f + r":\s*(Favors|Inhibits) · Speculative", g + "\n" + app)]
chk("Speculative factors are Neutral (R-7, factor rule after T-38)", not spec, str(spec))
chk("General finding ≤350 words", len(g.split()) <= 350, f"({len(g.split())})")
for k, v in s2.items():
    chk(f"Step 2 label {k} uses an allowed value", v is not None, f"({v})")
for k in ["APPLICATION:", "ADOPTION MEANS:", "STAGE BASIS:", "STRONGEST APPLICATION SIGNAL:", "APPLICATION FACTORS:"] + [f + ":" for f in FAC]:
    chk(f"Application slot {k}", k in app)
chk("Application finding ≤250 words", len(app.split()) <= 250, f"({len(app.split())})")

# Stage rule (R-4): a stage above Early adopters needs a qualifying share; FLAG self-report wording
HIGH = {"Early majority", "Late majority", "Laggards", "Chasm"}
for lvl, txt, key in [("technology", g, "TECHNOLOGY STAGE"), ("application", app, "APPLICATION STAGE"), ("peer group", org, "PEER GROUP STAGE")]:
    st = lab(txt, key, STAGE)
    b = basis(txt, key + ":") if lvl != "peer group" else (re.search(r"PEER GROUP STAGE:[^\n]*", org) or [""])[0]
    if st in HIGH:
        has_share = bool(re.search(r"\d+(\.\d+)?\s*%", b))
        chk(f"{lvl} stage {st} names a share in its basis (R-4)", has_share, f"[{b[:90]}]")
        if re.search(r"respondent|self-report|opt-in|panel|vendor survey", b, re.I) and not re.search(r"representative|census", b, re.I):
            out.append(f"FAIL  {lvl} stage {st} rests on a respondent self-report, not a qualifying share (R-4)  [{b[:90]}]")
    if st == "Early adopters" and not re.search(r"\d+(\.\d+)?\s*%", b):
        out.append(f"FLAG  {lvl} stage Early adopters without a share: confirm a DATED base case (stage rule 4)  [{b[:90]}]")

# Org level and timing table (R-9)
for k in ["UNIT OF ANALYSIS", "PEER GROUP", "PEER GROUP STAGE", "ORG POSTURE", "PEER EVIDENCE ROLE", "ORG-SPECIFIC FORCES", "TABLE INPUT", "TIMING IMPLICATION", "POSTURE EFFECT"]:
    chk(f"Org label {k}", k + ":" in org)
chk("PEER GROUP STAGE uses an allowed value", lab(org, "PEER GROUP STAGE", STAGE) is not None)
pos = lab(org, "ORG POSTURE", POSTURE); per = lab(org, "PEER EVIDENCE ROLE", r"Prerequisite|Parallel")
chk("ORG POSTURE allowed", pos is not None, f"({pos})"); chk("PEER EVIDENCE ROLE allowed", per is not None, f"({per})")
ti = re.search(r"TABLE INPUT:\s*(" + STAGE + r")[^\n×x]*[×x]\s*(" + POSTURE + r")", org)
tim = lab(org, "TIMING IMPLICATION", TIMING)
appst = s2["APPLICATION STAGE"]
row = "Early adopters" if appst and appst.startswith("Withheld") else appst
chk("TABLE INPUT uses the APPLICATION STAGE (Withheld → Early adopters row) (R-9)",
    bool(ti) and (ti.group(1) == appst or (appst and appst.startswith("Withheld") and ti.group(1) in ("Early adopters", "Withheld — insufficient evidence"))),
    f"({ti.groups() if ti else None}; application {appst})")
exp = TABLE.get(row, (None,) * 3)[COL[pos]] if row in TABLE and pos in COL else None
chk("TIMING IMPLICATION matches the table cell (R-9)", tim is not None and tim == exp, f"({row} × {pos} → expected {exp}, got {tim})")
pe = re.search(r"POSTURE EFFECT:(.*)$", org, re.S); pe_text = pe.group(1) if pe else ""
dirw = re.findall(r"\b(adopt\w*|pilot\w*|proceed\w*|roll ?out|deploy\w*|evaluat\w*)\b", pe_text, re.I)
chk("POSTURE EFFECT gives no adopt/pilot/evaluation direction", not dirw, str(dirw))
chk("Org finding ≤300 words", len(org.split()) <= 300, f"({len(org.split())})")

con = " ".join(r.get("contrary_evidence_or_limitations", []))
for k in ["COMPETING STAGE READ", "DISTINGUISHING EVIDENCE", "WEAKEST DIFFUSION CLAIM", "EVIDENCE GAPS"]:
    chk(f"Step 4 label {k}", k in con)
chk("WEAKEST DIFFUSION CLAIM gives one allowed reason (R-12)", bool(re.search(r"WEAKEST DIFFUSION CLAIM:[^\n]*\b(weak|stale|geographically narrow|industry-specific|indirect)\b", con)))
c = r["confidence_and_uncertainty"]; c = c if isinstance(c, str) else " ".join(c)
lv = {k: (re.search(k + r"[^.;\n]{0,15}?\b(Low|Moderate|High)\b", c, re.I) or [None, None])[1] for k in ["technology", "application", "peer group"]}
chk("STAGE CONFIDENCE first, one value per level", c.strip().startswith("STAGE CONFIDENCE:") and None not in lv.values() and not re.search(r"(Low|Moderate|High)-to-", c), str(lv))

m = re.match(r"TIMING:\s*(" + TIMING + r")\s*—", rec)
chk("Recommendation starts 'TIMING: <value> —' and matches TIMING IMPLICATION", bool(m) and m.group(1) == tim, f"({m.group(1) if m else None} vs {tim})")
chk("Recommendation ≤150 words", len(rec.split()) <= 150, f"({len(rec.split())})")
lane = re.findall(r"\b(pilot\w*|proceed\w*|roll ?out|scale up|expand\w*|threshold\w*|cadence|owner|fortnightly|monthly reviews?|bounded evaluation|run an? evaluation|prepare an? (?:bounded )?evaluation)\b", rec, re.I)
chk("Recommendation stays in lane (R-10)", not lane, str(lane))

ev = r.get("evidence", [])
bad_type = [e["evidence_type"] for e in ev if e["evidence_type"] not in
            {"primary-technical", "primary-historical", "dated-market", "secondary", "inference", "case-premise"}]
chk("evidence_type from the team list (R-13)", not bad_type, str(sorted(set(bad_type)))[:120])
bad_date = [i for i, e in enumerate(ev) if e["evidence_type"] not in ("inference", "case-premise") and not re.search(r"published:\s*\S", e.get("date_or_recency", ""))]
chk("date_or_recency gives 'published:' for sourced items (dates rule)", not bad_date, f"indices {bad_date}")
if s1["EVIDENCE BASE"] == "Supplied cards":
    insp = [e["source_or_reference"][:50] for e in ev if e.get("notes", "").startswith("STATUS: inspected-this-run")]
    if insp:
        out.append(f"FLAG  Supplied cards, but {len(insp)} item(s) inspected this run: confirm no label rests on them (R-2) {insp}")
ho = [x for x in r.get("abstention_or_more_information_needed", []) if x.startswith("HANDOFF")]
named = {n for n in ["Creation", "Innovation", "Promethean", "Adoption Agent", "Organizational Adoption", "Landscape"] if any(n in h for h in ho)}
chk("HANDOFF lines name the other six specialists", len(named) == 6, f"({sorted(named)})")

if a.pair:
    p = json.load(open(a.pair))
    p1, p2 = step1(p["general_et_finding"]), step2(p["application_finding"])
    d1 = {k: (s1[k], p1[k]) for k in s1 if s1[k] != p1[k]}
    d2 = {k: (s2[k], p2[k]) for k in s2 if s2[k] != p2[k]}
    chk("Same Step 1 labels as paired run (R-8)", not d1 and None not in s1.values(), str(d1 or "identical"))
    chk("Same Step 2 labels as paired run (R-8)", not d2 and None not in s2.values(), str(d2 or "identical"))
    if a.posture_pair:
        po = p["organization_specific_finding"]
        ptim = lab(po, "TIMING IMPLICATION", TIMING)
        pp = re.search(r"POSTURE EFFECT:(.*)$", po, re.S)
        chk("Posture pair: TIMING or PEER EVIDENCE ROLE differs", (tim != ptim) or (per != lab(po, "PEER EVIDENCE ROLE", r"Prerequisite|Parallel")), f"({tim} vs {ptim})")
        chk("Posture pair: POSTURE EFFECT differs", bool(pe and pp) and pe_text.strip() != pp.group(1).strip())
print("\n".join(out))
