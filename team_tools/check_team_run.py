#!/usr/bin/env python3
"""Team §4 context-review helper for the Team Creation Agent (beyond the frozen validator).

Checks the rules that can be checked mechanically. A person still reads the output
(swap test, claim tracing). Usage: python3 check_team_run.py <response.json> <case.json>
"""
import json, re, sys

resp = json.load(open(sys.argv[1])); case = json.load(open(sys.argv[2]))
g = resp["general_et_finding"]
out = []
def chk(name, ok, detail=""): out.append(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")

words = len(g.split())
chk("General ≤350 words [T]", words <= 350, f"({words} words)")
labels = ["NEED:", "PREDECESSORS:", "ENABLERS:", "ARC STAGE:", "TRAJECTORY"]
chk("Five labeled general parts [Z]", all(l in g for l in labels), str([l for l in labels if l not in g]))
m = re.search(r"ARC STAGE:\s*(Emerging→Developing|Developing→Mature|Emerging|Developing|Mature)\b", g)
chk("Allowed stage label [Z]", bool(m), m.group(1) if m else "")
chk("Defining layer named [Z]", "defining layer" in g.lower())

# R-5 leak test: distinctive words from the case's organization/application/industry fields
stop = set("the a an and or of for to in with on by as at is are be this that its from into not no only".split())
case_text = " ".join(case[k] for k in ["organization", "industry_sector"])
case_words = {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z\-]{3,}", case_text)} - stop
tech_words = {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z\-]{4,}", case["emerging_technology"])}
generic = {"software", "models", "model", "language", "technology", "systems", "code", "agents", "agent",
           "development", "tests", "files", "image", "images", "generate", "generation", "product", "products",
           "users", "developers", "engineers", "internal", "approved", "separately", "remain", "final",
           "design", "concept", "concepts", "existing", "engineering", "group", "about", "subject", "services", "current"}
leak = sorted(w for w in case_words - tech_words - generic if re.search(r"\b" + re.escape(w) + r"\b", g, re.I))
out.append(("PASS" if not leak else "FLAG") + "  R-5 organization/industry words in general level (FLAG = human review)  " + str(leak))

av = [x for x in resp["contrary_evidence_or_limitations"] if re.match(r"\s*A[123]\b", x)]
verd = [re.search(r"VERDICT:\s*(HOLDS|DOES NOT HOLD|UNTESTED)", x) for x in av]
chk("R-4 A1–A3 with verdicts [Z]", len(av) >= 3 and all(verd[:3]),
    str([v.group(1) if v else None for v in verd[:3]]))

types = {"primary-technical", "primary-historical", "dated-market", "secondary", "inference", "case-premise"}
bad_t = [e["evidence_type"] for e in resp["evidence"] if e["evidence_type"] not in types]
chk("Evidence types from list [Z][T]", not bad_t, str(bad_t))
bad_s = [i for i, e in enumerate(resp["evidence"]) if not re.match(r"STATUS:\s*(inspected-this-run|supplied|unverified)", e["notes"])]
chk("Every evidence note starts with STATUS [Y]", not bad_s, f"bad indices {bad_s}")
md = [e["source_or_reference"][:50] for e in resp["evidence"] if re.search(r"\]\(http", e["source_or_reference"])]
chk("R-8 no Markdown links", not md, str(md))
stat = [re.match(r"STATUS:\s*([\w-]+)", e["notes"]).group(1) for e in resp["evidence"] if re.match(r"STATUS:\s*([\w-]+)", e["notes"])]
out.append(f"INFO  STATUS counts: { {s: stat.count(s) for s in set(stat)} }")

rec = resp["recommendation_management_implication"]
lane = re.findall(r"\b(we recommend (?:adopting|piloting)|should (?:adopt|pilot|experiment|reject)|run a (?:pilot|sandbox|experiment)|hypothesis:|stop condition)", rec, re.I)
chk("R-9 lane: no adopt/pilot/experiment design", not lane, str(lane))
ho = [x for x in resp["abstention_or_more_information_needed"] if x.startswith("HANDOFF")]
chk("HANDOFF lines present", len(ho) >= 1, f"({len(ho)})")
a2 = next((x for x in av if x.strip().startswith("A2")), "")
fixed = "has converged on a de facto architecture across major providers" in a2
v2 = re.search(r"VERDICT:\s*(HOLDS|DOES NOT HOLD|UNTESTED)", a2)
stage = m.group(1) if m else ""
consistent = bool(v2) and ((v2.group(1) == "HOLDS") == (stage in ("Developing", "Developing→Mature", "Mature")))
chk("A2 fixed affirmative wording [T v1.0]", fixed)
chk("A2 verdict consistent with stage [T v1.0]", consistent, f"A2={v2.group(1) if v2 else None}, stage={stage}")
empty = [k for k in ["evidence", "contrary_evidence_or_limitations", "change_monitoring_triggers", "abstention_or_more_information_needed"] if not resp[k]]
chk("No empty arrays", not empty, str(empty))
print("\n".join(out))
