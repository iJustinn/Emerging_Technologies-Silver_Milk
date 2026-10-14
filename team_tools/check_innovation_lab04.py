#!/usr/bin/env python3
"""Lab 4 Innovation Classification checks, run in addition to check_common.py.

Usage: python3 check_innovation_lab04.py <response.json> [--pair <other_response.json>] [--same-application]
  --pair             compare the general level (degree, lifecycle verdicts) with a run on the SAME technology (not the transfer case)
  --same-application also compare application-level labels (use when both cases share the application)
FLAG = needs a human read, not an automatic failure.
"""
import argparse, json, re

ap = argparse.ArgumentParser()
ap.add_argument("response"); ap.add_argument("--pair"); ap.add_argument("--same-application", action="store_true")
a = ap.parse_args()
out = []
def chk(name, ok, detail=""): out.append(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")

def degree(g):
    # team format "DEGREE: <label>"; also reads candidate formats ("Degree of change: X", "INNOVATION TYPE (general): X")
    m = re.search(r"(?:DEGREE|Degree of change|INNOVATION TYPE \(general\))\s*:\s*(Contested \(breakthrough candidate\)|Incremental|Breakthrough)", g)
    return m.group(1) if m else None

def lifecycle(g):
    return {k: (re.search(k + r"\s+(HOLDS|DOES NOT HOLD|UNTESTED)", g) or [None, None])[1]
            for k in ["INVENTION", "INNOVATION", "COMMERCIALIZATION"]}

def app_labels(t):
    # compare only the allowed label, not the explanation that follows it
    pats = {"STATUS IN CASE": r"Proposed|Demonstration|Trial or pilot in use|Implemented",
            "NOVELTY": r"New to the world|New to the industry|New to the organization only|Not new|Withheld",
            "APPLICATION CLASS": r"\w+"}
    labs = {}
    for k, v in pats.items():
        m = re.search(re.escape(k) + r"\s*:\s*(" + v + ")", t)
        if m: labs[k] = m.group(1)
    return labs

r = json.load(open(a.response))
g, app, org = r["general_et_finding"], r["application_finding"], r["organization_specific_finding"]

lc = lifecycle(g)
chk("LIFECYCLE slots INVENTION/INNOVATION/COMMERCIALIZATION each have a verdict", all(lc.values()), str(lc))
chk("DEGREE uses an allowed label", degree(g) is not None, f"({degree(g)})")
ent = re.search(r"ENTREPRENEURSHIP\s*:\s*(Incumbent-led|Entrepreneur-led|Mixed|Not yet entrepreneurial|Not established)", g)
chk("ENTREPRENEURSHIP uses an allowed label", bool(ent), f"({ent.group(1) if ent else None})")
if degree(g) == "Breakthrough":
    out.append("FLAG  Breakthrough: confirm a named baseline and dated comparative evidence (R-3)")

st = re.search(r"STATUS IN CASE\s*:\s*(Proposed|Demonstration|Trial or pilot in use|Implemented)", app)
chk("STATUS IN CASE uses an allowed label", bool(st), f"({st.group(1) if st else None})")
nov = re.search(r"NOVELTY\s*:\s*(New to the world|New to the industry|New to the organization only|Not new|Withheld)", app)
chk("NOVELTY uses an allowed label", bool(nov), f"({nov.group(1) if nov else None})")
chk("No organization-dependent APPLICATION CLASS in application_finding (R-5)", "APPLICATION CLASS" not in app)
stline = re.search(r"STATUS IN CASE\s*:.*?(?=REAL-WORLD VERIFICATION|\n|$)", app, re.S)
stext = stline.group(0) if stline else app[:200]  # candidate formats: check the opening status statement
chk("Status is not called 'unspecified' (R-6 default = Proposed)", not re.search(r"\bunspecified\b", stext, re.I))

sig = re.search(r"SIGNIFICANCE\s*:\s*(Low|Moderate|High|Potentially Existential|Withheld)\s*(\((provisional|withheld)\))?", org)
chk("SIGNIFICANCE label present", bool(sig), f"({sig.group(0) if sig else None})")
if sig and sig.group(1) != "Withheld":
    chk("Non-withheld SIGNIFICANCE marked provisional", bool(sig.group(2)))
for lab in ["UNIT OF ANALYSIS", "REVENUE MECHANISM", "CORE OR SUPPORT", "MATERIALITY", "HORIZON", "STRATEGIC RISK"]:
    chk(f"Org label {lab}", lab + ":" in org)
chk("Org finding ≤350 words", len(org.split()) <= 350, f"({len(org.split())})")
chk("Application finding ≤150 words", len(app.split()) <= 150, f"({len(app.split())})")
chk("General finding ≤200 words", len(g.split()) <= 200, f"({len(g.split())})")

con = " ".join(r.get("contrary_evidence_or_limitations", []))
chk("COMPETING CLASSIFICATION + DISTINGUISHING EVIDENCE present", "COMPETING CLASSIFICATION" in con and "DISTINGUISHING EVIDENCE" in con)

rec = r["recommendation_management_implication"]
lane = re.findall(r"\b(pilot\w*|partner\b|adopt\b|adopting|roll ?out|scale up|reject\b|stop rule|hypothesis)\b", rec, re.I)
chk("Recommendation stays in lane (R-10)", not lane, str(lane))

ev = r.get("evidence", [])
md = [e["source_or_reference"][:40] for e in ev if re.search(r"\]\(https?://", e.get("source_or_reference", ""))]
chk("No Markdown links in sources (R-9)", not md, str(md))
over = [i for i, e in enumerate(ev)
        if re.search(r"(?<!not )(?<!not an )(?<!not externally )(?<!not an externally )\bverified\b", e.get("evidence_type", "") + " " + e.get("notes", "") + " " + e.get("date_or_recency", ""), re.I)
        and not e.get("notes", "").startswith("STATUS: inspected-this-run")]
chk("No 'verified' wording on evidence not inspected this run (R-9)", not over, f"indices {over}")
bad_type = [e["evidence_type"] for e in ev if e["evidence_type"] not in
            {"primary-technical", "primary-historical", "dated-market", "secondary", "inference", "case-premise"}]
chk("evidence_type from the team list", not bad_type, str(sorted(set(bad_type)))[:120])

ho = [x for x in r.get("abstention_or_more_information_needed", []) if x.startswith("HANDOFF")]
named = {n for n in ["Creation", "Promethean", "Diffusion", "Adoption", "Organizational Adoption", "Landscape"] if any(n in h for h in ho)}
chk("HANDOFF lines present", len(ho) >= 1, f"({len(ho)}; agents: {sorted(named)})")

if a.pair:
    p = json.load(open(a.pair))
    d1, d2 = degree(g), degree(p["general_et_finding"])
    chk("Same DEGREE as paired run (R-4)", d1 is not None and d1 == d2, f"({d1} vs {d2})")
    e2 = re.search(r"ENTREPRENEURSHIP\s*:\s*(Incumbent-led|Entrepreneur-led|Mixed|Not yet entrepreneurial|Not established)", p["general_et_finding"])
    e1 = re.search(r"ENTREPRENEURSHIP\s*:\s*(Incumbent-led|Entrepreneur-led|Mixed|Not yet entrepreneurial|Not established)", g)
    if e1 or e2:
        chk("Same ENTREPRENEURSHIP label as paired run (R-4)", bool(e1 and e2) and e1.group(1) == e2.group(1),
            f"({e1.group(1) if e1 else None} vs {e2.group(1) if e2 else None})")
    l2 = lifecycle(p["general_et_finding"])
    if any(lc.values()) or any(l2.values()):
        chk("Same LIFECYCLE verdicts as paired run (R-4)", lc == l2, f"({lc} vs {l2})")
    if a.same_application:
        a1, a2 = app_labels(app), app_labels(p["application_finding"])
        chk("Same application-level labels as paired run (R-5)", a1 == a2, f"({a1} vs {a2})")
print("\n".join(out))
