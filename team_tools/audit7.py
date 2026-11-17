#!/usr/bin/env python3
"""Seven-agent integration audit (Lab 9). Reads each team agent's instructions and its latest saved team runs.
Usage: audit7.py <repo root> [extra agent dir ...]"""
import json, re, sys, glob, os
from collections import defaultdict

root = sys.argv[1]
agents = sorted(glob.glob(os.path.join(root, "agents/team_*"))) + sys.argv[2:]
label_re = re.compile(r"`([A-Z][A-Z0-9 /&\-]{2,40}):`")
handoff_re = re.compile(r"HANDOFF\s*→\s*([A-Z][A-Za-z &\-]+?Agent)")
type_re = re.compile(r"`(vendor-claim|industry-analyst|independent|standards-regulatory|inference|case-premise|primary|secondary|analyst|adopter-self-report|[a-z]+-[a-z]+)`")
labels = defaultdict(set)
for a in agents:
    name = os.path.basename(a.rstrip("/"))
    txt = open(os.path.join(a, "specialist_instructions.md")).read()
    md = json.load(open(os.path.join(a, "agent_metadata.json")))
    ls = sorted(set(label_re.findall(txt)))
    for l in ls:
        labels[l].add(name)
    # handoff names actually emitted in final team runs
    v = md["version"].replace("-team", "")
    pats = [f"responses/team_v{v.replace('.', '_')}__*.json", f"responses/*_response_v{v}.json",
            f"responses/*_response_v{v.replace('.', '_')}.json"]
    runs = sorted({r for p in pats for r in glob.glob(os.path.join(a, p))})
    emitted, notes_prefix, ev_types = set(), set(), set()
    for r in runs:
        d = json.load(open(r))
        for x in d.get("abstention_or_more_information_needed", []):
            m = handoff_re.search(x)
            if m:
                emitted.add(m.group(1).strip())
        for e in d.get("evidence", []):
            notes_prefix.add((e.get("notes", "").split(":")[0] or "")[:12])
            ev_types.add(e.get("evidence_type", ""))
    print(f"== {name}  version={md['version']}  words={len(txt.split())}  runs={len(runs)}")
    print("   handoff targets in runs:", sorted(emitted))
    print("   notes prefixes:", sorted(notes_prefix))
    print("   evidence_type values:", sorted(ev_types))
    print("   labels:", ", ".join(ls))
print("\n== Labels used by more than one agent")
for l, s in sorted(labels.items()):
    if len(s) > 1:
        print(f"   {l}: {sorted(s)}")
