#!/usr/bin/env python3
"""Generic team §4 checks for any MASY1800 specialist response (beyond the frozen validator).

Usage: python3 check_common.py <response.json> <case.json> [--cap 350] [--metadata agent_metadata.json]
Copy into <scaffold>/common_test_package/ and extend per lab with specialist rules
(see check_creation_lab03_example.py for the Lab 3 Creation-specific version).
FLAG = needs a human read, not an automatic failure.
"""
import argparse, json, re

ap = argparse.ArgumentParser()
ap.add_argument("response"); ap.add_argument("case")
ap.add_argument("--cap", type=int, default=350, help="max words in general_et_finding")
ap.add_argument("--metadata", help="agent_metadata.json to compare version against")
a = ap.parse_args()
resp = json.load(open(a.response)); case = json.load(open(a.case))
out = []
def chk(name, ok, detail=""): out.append(f"{'PASS' if ok else 'FAIL'}  {name}  {detail}")

g = resp.get("general_et_finding", "")
chk(f"General ≤{a.cap} words", len(g.split()) <= a.cap, f"({len(g.split())} words)")

# Case leak: organization/industry words appearing in the general level
generic = {"software", "models", "model", "language", "technology", "systems", "agents", "agent", "development",
           "users", "developers", "engineers", "internal", "approved", "final", "existing", "engineering", "group",
           "about", "subject", "services", "current", "with", "that", "this", "from", "their"}
words = {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z\-]{3,}", case["organization"] + " " + case["industry_sector"])}
tech = {w.lower() for w in re.findall(r"[A-Za-z][A-Za-z\-]{3,}", case["emerging_technology"])}
leak = sorted(w for w in words - tech - generic if re.search(r"\b" + re.escape(w) + r"\b", g, re.I))
out.append(("PASS" if not leak else "FLAG") + "  Org/industry words in general level  " + str(leak))

ev = resp.get("evidence", [])
bad_s = [i for i, e in enumerate(ev) if not re.match(r"STATUS:\s*(inspected-this-run|supplied|unverified)", e.get("notes", ""))]
chk("Every evidence note starts with STATUS", not bad_s, f"bad indices {bad_s}")
md = [e["source_or_reference"][:50] for e in ev if re.search(r"\]\(http", e.get("source_or_reference", ""))]
chk("No Markdown links in sources", not md, str(md))
blob = json.dumps(resp)
vc = len(re.findall(r"\b(verified|checked)\b", blob, re.I))
out.append(("PASS" if vc == 0 else "FLAG") + f"  'verified'/'checked' wording (allowed only if retrieved)  ({vc})")

ho = [x for x in resp.get("abstention_or_more_information_needed", []) if x.startswith("HANDOFF")]
chk("HANDOFF lines present", len(ho) >= 1, f"({len(ho)})")
empty = [k for k in ["evidence", "contrary_evidence_or_limitations", "change_monitoring_triggers",
                     "abstention_or_more_information_needed"] if not resp.get(k)]
chk("No empty arrays", not empty, str(empty))
if a.metadata:
    mv = json.load(open(a.metadata)).get("version")
    chk("agent.version matches metadata", resp.get("agent", {}).get("version") == mv, f"({resp.get('agent',{}).get('version')} vs {mv})")
for f in ["application_finding", "organization_specific_finding"]:
    out.append(f"INFO  {f} words: {len(resp.get(f, '').split())}")
print("\n".join(out))
