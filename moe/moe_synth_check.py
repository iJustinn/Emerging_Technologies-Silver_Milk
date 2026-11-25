#!/usr/bin/env python3
"""Lab 10 dry-run helper: spec S-2 synthesis check (not the Lab 11 orchestrator).
Usage: moe_synth_check.py <synth reply (raw or json)> <template.md> <responses dir> <run prefix> <source pack.md>
Checks: (1) action echo identical to the template; (2) every cite names a known agent and a label that
occurs in that agent's output; (3) no date, URL or number in the synthesizer text that is absent from the
template, the outputs and the pack; (4) every template conflict row answered, types in Q/E/J;
(5) caution signals each cite a label. Prints PASS/FAIL lines and exits 1 on any FAIL."""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from moe_labels import CONTRACT  # noqa: E402

reply_p, tmpl_p, rdir, prefix, pack_p = sys.argv[1:6]
t = open(reply_p).read().strip()
t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t)
R = json.loads(t)
tmpl = open(tmpl_p).read()
pack = open(pack_p).read()
outs, alias = {}, {}
for e in CONTRACT["experts"]:
    p = os.path.join(rdir, f"{prefix}__{e['folder']}.json")
    outs[e["folder"]] = open(p).read() if os.path.exists(p) else ""
    for n in [e["name"], e["name"].replace("Silver-Milk Team ", "")] + e["aliases"]:
        alias[n.lower().replace(" agent", "").strip()] = e["folder"]
alias["org adoption"] = "team_organizational_adoption_agent"
corpus = tmpl + "\n" + pack + "\n" + "\n".join(outs.values())
fails = []


def chk(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (f"  ({detail})" if detail else ""))
    if not ok:
        fails.append(name)


m = re.search(r"## 1 PROPOSED ACTION[^\n]*\n([^\n]+)", tmpl)
chk("S-2a action echo identical to template", m and R.get("proposed_action_echo", "").strip() == m.group(1).strip(),
    f"{R.get('proposed_action_echo')!r} vs {m.group(1) if m else None!r}")

bad = []
for sec in ("conditions", "caution_signals"):
    for i, it in enumerate(R.get(sec, []), 1):
        if not it.get("cites"):
            bad.append(f"{sec}[{i}] no cite")
        for c in it.get("cites", []):
            mm = re.match(r"\s*([^:]+):\s*([A-Z][A-Z0-9 /&\-]+?)(?::|$)", c)
            if not mm:
                bad.append(f"{sec}[{i}] unparsable cite {c!r}"); continue
            ag = alias.get(mm.group(1).lower().replace(" agent", "").strip())
            lab = mm.group(2).strip()
            if not ag:
                bad.append(f"{sec}[{i}] unknown agent {mm.group(1)!r}")
            elif not re.search(re.escape(lab) + r"[^:\n]{0,60}:", outs[ag]):
                bad.append(f"{sec}[{i}] label {lab!r} not in {ag}")
chk("S-2b every condition/caution cites agent + an existing label", not bad, "; ".join(bad))

text = json.dumps({k: v for k, v in R.items() if k != "proposed_action_echo"}, ensure_ascii=False)
dates = set(re.findall(r"\b20\d\d-\d\d(?:-\d\d)?\b|\bQ[1-4] 20\d\d\b", text))
urls = set(re.findall(r"https?://[^\s\"')]+", text))
nums = set(x for x in re.findall(r"(?<![\w.-])\d[\d,.]*%?", text) if len(x.strip(".,")) > 1)
new_d = sorted(d for d in dates if d not in corpus)
new_u = sorted(u for u in urls if u not in corpus)
new_n = sorted(n for n in nums if n.strip(".,") not in corpus)
chk("S-2c no new dates", not new_d, ", ".join(new_d))
chk("S-2c no new URLs", not new_u, ", ".join(new_u))
chk("S-2c no new numbers", not new_n, ", ".join(new_n))

rows = len(re.findall(r"^\| \d+ \|", tmpl, re.M))
got = sorted(c.get("row") for c in R.get("conflicts", []))
chk("S-2d every conflict row answered", got == list(range(1, rows + 1)), f"template {rows}, reply {got}")
chk("S-2d conflict types in Q/E/J", all(c.get("proposed_type") in ("Q", "E", "J") for c in R.get("conflicts", [])))
chk("S-2e no vendor selection wording", not re.search(r"\b(select|choose|recommend)\w*\b[^.]{0,40}\b(vendor|Digit|Figure|Atlas|Apollo|GR00T|Gemini)\b", text, re.I))
print("SYNTHESIS CHECK:", "PASS" if not fails else f"FAIL ({len(fails)}) → F-7, template-only brief")
sys.exit(1 if fails else 0)
