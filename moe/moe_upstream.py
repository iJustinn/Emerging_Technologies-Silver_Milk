#!/usr/bin/env python3
"""Lab 10 dry-run helper (spec O-5/O-6): write a wave-2/3 case = the intake case plus an
'# Upstream expert reads' block appended to additional_context. Label lines are copied verbatim
(full line) from the saved outputs of the experts named in the contract's receives_upstream.
Usage: moe_upstream.py <intake case> <responses dir> <run prefix> <target agent folder> <run id> <out case>"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from moe_labels import CONTRACT, labels_for  # noqa: E402

case_path, rdir, prefix, target, run_id, out = sys.argv[1:7]
experts = {e["folder"]: e for e in CONTRACT["experts"]}
lines = [f"# Upstream expert reads (case-premise; produced by other Silver-Milk team specialists in MoE run {run_id})"]
for src in experts[target]["receives_upstream"]:
    e = experts[src["from"]]
    labs = labels_for(e, os.path.join(rdir, f"{prefix}__{e['folder']}.json"))
    if labs is None:
        lines.append(f"- {e['name']}: unavailable in this run (failed check)")
        continue
    for lab in src["labels"]:
        v = labs.get(lab)
        lines.append(f"- {e['name']} {e['version']}: {lab}: {v if v is not None else 'not found in output'}")
case = json.load(open(case_path))
case["additional_context"] = case.get("additional_context", "") + "\n\n" + "\n".join(lines) + "\n"
json.dump(case, open(out, "w"), ensure_ascii=False, indent=2)
print("\n".join(lines))
