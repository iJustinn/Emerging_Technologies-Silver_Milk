#!/usr/bin/env python3
"""Lab 10 dry-run helper (spec §5.1 template + mechanical flags; not the Lab 11 orchestrator).
Fills the decision-brief template from the seven saved outputs (labels keyed on agent + label).
Flags that need judgment are passed in by the operator and printed as such.
Usage: moe_brief.py <responses dir> <run prefix> <intake case> <run id> <pack id> <out.md>
       [--failed agent_folder,...] [--manual-flag "F-n: reason" ...]"""
import argparse, json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from moe_labels import CONTRACT, labels_for  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("rdir"); ap.add_argument("prefix"); ap.add_argument("case"); ap.add_argument("run_id")
ap.add_argument("pack_id"); ap.add_argument("out")
ap.add_argument("--failed", default=""); ap.add_argument("--manual-flag", action="append", default=[])
a = ap.parse_args()
case = json.load(open(a.case))
E = {e["folder"]: e for e in CONTRACT["experts"]}
failed = set(x for x in a.failed.split(",") if x)
L, raw = {}, {}
for f, e in E.items():
    p = os.path.join(a.rdir, f"{a.prefix}__{f}.json")
    L[f] = None if f in failed else labels_for(e, p)
    raw[f] = None if (f in failed or not os.path.exists(p)) else json.load(open(p))


def g(f, lab, n=None):
    v = (L.get(f) or {}).get(lab)
    v = "not available" if v is None else v
    return v if n is None else v[:n]


def head(v):  # the value before the first explanation dash; a parenthesized value such as
    # 'Indeterminate (Incremental | Breakthrough)' contains ' | ' and is kept whole (dry-run finding)
    m = re.match(r"[^(—–|.]*\([^)]*\)", v)
    if m:
        return m.group(0).strip()
    return re.split(r"\s+[—–]\s+|\.\s|\s\|\s", v, maxsplit=1)[0].strip().rstrip(".")


ado, org, lan, pro, dif, inn, cre = ("team_adoption_agent", "team_organizational_adoption_agent", "team_landscape_agent",
                                     "team_promethean_classification_agent", "team_diffusion_agent",
                                     "team_innovation_classification_agent", "team_creation_agent")
action = g(ado, "RECOMMENDATION") if L[ado] else "NO PROPOSED ACTION — Adoption expert unavailable"

# ---- mechanical flags (spec §3) ----
flags = []
for f in E:
    if L[f] is None:
        flags.append(f"F-1: {E[f]['name']} unavailable or FAILED")
if L[ado] and head(g(ado, "RECOMMENDATION")).startswith("Withheld"):
    flags.append("F-2: Adoption RECOMMENDATION Withheld")
if L[org] and head(g(org, "READINESS VERDICT")).lower().startswith("undetermined"):
    flags.append("F-2: Org Adoption READINESS VERDICT Undetermined")
if L[lan]:
    sh = g(lan, "STALE/HYPE FLAG")
    if re.search(r"\bcase\b|memo|\bS\d+\b|pack", sh, re.I) or (raw[lan] and "CORRECTION:" in json.dumps(raw[lan])):
        flags.append("F-4: Landscape STALE/HYPE FLAG cites the intake/case or a pack card: " + sh[:140])
if L[ado] and (head(action).lower() == "adopt" or head(g(ado, "CONSEQUENCE")).lower() == "severe"):
    flags.append("F-5: Adopt or Severe consequence")
if L[ado] and head(g(ado, "RECOMMENDATION CONFIDENCE") if "RECOMMENDATION CONFIDENCE" in L[ado] else "").lower() == "low":
    flags.append("F-8: Adoption confidence Low")
if L[org]:
    im = g(org, "INTAKE MISSING")
    stage = g(org, "STAGE ASKED").lower()
    if not stage.startswith("preparation") and re.search(r"sponsor|owner|coordinator|environment|budget|fund", im, re.I):
        flags.append("F-9: INTAKE MISSING names sponsor/owner/environment/budget for a stage beyond preparation: " + im[:140])
flags += [m for m in a.manual_flag]

# ---- conflict rows (spec §4.2; readings copied, type proposed by the table default) ----
rows = [
    ("Adoption ↔ Org Adoption", f"Adoption RECOMMENDATION: {g(ado,'RECOMMENDATION',120)}", f"Org Adoption READINESS VERDICT: {g(org,'READINESS VERDICT',120)}", "Q (E/J if readiness blocks a stage beyond the action)"),
    ("Innovation ↔ Promethean", f"Innovation DEGREE: {g(inn,'DEGREE',110)}", f"Promethean SIGNIFICANCE CLASS: {g(pro,'SIGNIFICANCE CLASS',110)}", "J if opposite; Q otherwise"),
    ("Landscape ↔ Diffusion ↔ Adoption", f"Landscape STANCE: {g(lan,'STANCE',60)} · Diffusion TIMING: {g(dif,'TIMING',60)}", f"Adoption: {head(action)}", "Q — never merged (I-31)"),
    ("Creation ↔ Innovation", f"Creation ARC STAGE: {g(cre,'ARC STAGE',80)}", f"Innovation LIFECYCLE: {g(inn,'LIFECYCLE',110)}", "Q (distinct labels, I-09)"),
    ("Promethean ↔ Adoption", f"Promethean WEIGHT: {g(pro,'WEIGHT OF BROAD SIGNIFICANCE ON THIS DECISION',110)}", f"Adoption: {head(action)}", "J only if High weight with Reject/Monitor or Low weight with Adopt"),
]


def disp(v):
    t = head(v).lower()
    if v == "not available": return "—"
    if any(k in t for k in ["withheld", "indeterminate", "undetermined", "insufficient"]): return "Abstained"
    return {"high": "Firm", "moderate": "Qualified", "low": "Weak"}.get(t.split()[0] if t else "", "text")


panel = []
for f, e in E.items():
    if L[f] is None:
        panel.append(f"| {e['name'].replace('Silver-Milk Team ','')} | {e['version']} | FAILED / unavailable | — | — | FAILED |"); continue
    hl = "; ".join(f"{k}: {head(v or 'not found')}" for k, v in L[f].items() if not k.startswith("(") and k not in ("STAGE BASIS", "STALE/HYPE FLAG", "OPTIONS DOCUMENTED", "EXECUTION GATES", "INTAKE MISSING", "MOST CONSEQUENTIAL GAP"))
    ck = [k for k in L[f] if k.startswith("(confidence)")]
    conf = head(L[f][ck[0]] or "not found") if ck else "text only (no fixed label)"
    panel.append(f"| {e['name'].replace('Silver-Milk Team ','')} | {e['version']} | {hl} | {conf} ({disp(L[f][ck[0]] or '') if ck else 'text'}) | {L[f]['(abstention items)']} items | OK |")

ev = []
for f, d in raw.items():
    if d:
        st = [x["notes"].split()[1].strip(";.:") if x.get("notes", "").startswith("STATUS:") else "?" for x in d["evidence"]]
        ev.append(f"{E[f]['name'].replace('Silver-Milk Team ','')}: {st.count('supplied')} pack/supplied, {st.count('inspected-this-run')} retrieved this run, {st.count('unverified')} unverified")

owner = (re.search(r"DECISION OWNER:\s*([^.;]*)", case.get("users_stakeholders", "")) or [None, "Not stated"])[1]
md = f"""# MOE DECISION BRIEF (template, filled by script) — {case['emerging_technology'][:70]}…
**Application:** {case['intended_application'][:160]}…
**Organization:** {case['organization'][:160]}…
Run {a.run_id} · Pack {a.pack_id} · Decision owner: {owner} · Horizon: {case['time_horizon']}
**STATUS:** {'Draft — human review required (flags fired)' if flags else 'Accepted by rule (no flags)'}

## 1 PROPOSED ACTION (Adoption Agent, verbatim)
{action}
CONFIDENCE: {g(ado,'RECOMMENDATION CONFIDENCE') if L[ado] and 'RECOMMENDATION CONFIDENCE' in L[ado] else (L[ado] or {}).get('(confidence) RECOMMENDATION CONFIDENCE','not available')}

## 2 CONDITIONS BEFORE ACTING (copied labels; synthesizer adds cited conditions)
- Org Adoption READINESS VERDICT: {g(org,'READINESS VERDICT')}
- Org Adoption MOST CONSEQUENTIAL GAP: {g(org,'MOST CONSEQUENTIAL GAP')}
- Adoption DEFER GATE: {g(ado,'DEFER GATE')}
- Adoption POSTURE GATE: {g(ado,'POSTURE GATE')}
- Landscape EXECUTION GATES: {g(lan,'EXECUTION GATES')}

## 3 THREE LEVELS (attributed)
- ET generally: Creation ARC STAGE {head(g(cre,'ARC STAGE'))} · Innovation DEGREE {head(g(inn,'DEGREE'))} · Promethean CLASS {g(pro,'SIGNIFICANCE CLASS',45)} · Diffusion TECHNOLOGY STAGE {head(g(dif,'TECHNOLOGY STAGE'))} · Adoption MATURITY ZONE {head(g(ado,'MATURITY ZONE'))}
- For this application: Diffusion APPLICATION STAGE {head(g(dif,'APPLICATION STAGE'))} · Innovation STATUS IN CASE {head(g(inn,'STATUS IN CASE'))}
- In this organization: Landscape STANCE {head(g(lan,'STANCE'))} ({head(g(lan,'CONDITION STATUS'))} × {head(g(lan,'MOVEMENT'))}) · Promethean WEIGHT {head(g(pro,'WEIGHT OF BROAD SIGNIFICANCE ON THIS DECISION'))} · Diffusion TIMING {head(g(dif,'TIMING'))} · Org Adoption {head(g(org,'READINESS VERDICT'))}

## 4 EXPERT PANEL
| Expert | Version | Headline labels | Confidence (display) | Abstentions | Status |
|---|---|---|---|---|---|
""" + "\n".join(panel) + """

## 5 CONFLICTS (never averaged; type proposed, human resolves J)
| # | Pair | Reading A | Reading B | Default type |
|---|---|---|---|---|
""" + "\n".join(f"| {i} | {p} | {x} | {y} | {t} |" for i, (p, x, y, t) in enumerate(rows, 1)) + f"""

## 6 TRADEOFFS — synthesizer text (checked)
## 7 MOST VALUABLE MISSING EVIDENCE / REASSESSMENT TRIGGERS — synthesizer text (checked)

## 8 EVIDENCE
""" + "\n".join("- " + x for x in ev) + f"""
- Landscape STALE/HYPE FLAG: {g(lan,'STALE/HYPE FLAG',260)}

## 9 FLAGS FIRED
""" + ("\n".join("- " + x for x in flags) if flags else "- none") + f"""
Human review required: {'YES' if flags else 'no'}

## 10 HUMAN DISPOSITION
Accept | Modify | Reject | Request more evidence — name, date, reason: ______
"""
open(a.out, "w").write(md)
print(md)
