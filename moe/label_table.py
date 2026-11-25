#!/usr/bin/env python3
"""Cross-lab headline-label table (Lab 10, I-01 evidence).
Reads each team agent's FINAL-version saved runs, maps each run to its case file,
and prints the headline, confidence and abstention labels, grouped by technology.
Read-only. Usage: label_table.py <repo root> [--md]"""
import glob, json, os, re, sys
from collections import defaultdict

HEAD = {  # agent folder -> labels the orchestrator would read (from each agent's output table)
    "team_creation_agent": ["ARC STAGE"],
    "team_innovation_classification_agent": ["DEGREE", "ENTREPRENEURSHIP", "STATUS IN CASE", "NOVELTY"],
    "team_promethean_classification_agent": ["SIGNIFICANCE CLASS", "WEIGHT", "CONFIDENCE AT LEAST", "CONFIDENCE NOT HIGHER"],
    "team_diffusion_agent": ["TECHNOLOGY STAGE", "APPLICATION STAGE", "TIMING", "STAGE CONFIDENCE"],
    "team_adoption_agent": ["RECOMMENDATION", "RECOMMENDATION CONFIDENCE", "DEFER GATE", "POSTURE GATE"],
    "team_organizational_adoption_agent": ["STAGE ASKED", "READINESS VERDICT", "VERDICT CONFIDENCE"],
    "team_landscape_agent": ["CONDITION STATUS", "MOVEMENT", "STANCE", "CONFIDENCE"],
}
SHORT = {"team_creation_agent": "Creation", "team_innovation_classification_agent": "Innovation",
         "team_promethean_classification_agent": "Promethean", "team_diffusion_agent": "Diffusion",
         "team_adoption_agent": "Adoption", "team_organizational_adoption_agent": "OrgAdoption",
         "team_landscape_agent": "Landscape"}
FIELDS = ["general_et_finding", "application_finding", "organization_specific_finding",
          "confidence_and_uncertainty", "recommendation_management_implication"]


def final_runs(adir):
    v = json.load(open(os.path.join(adir, "agent_metadata.json")))["version"].replace("-team", "")
    pats = [f"team_v{v.replace('.', '_')}__*.json", f"*_response_v{v}.json", f"*_response_v{v.replace('.', '_')}.json"]
    return v, sorted({r for p in pats for r in glob.glob(os.path.join(adir, "responses", p))})


def case_for(adir, run):
    b = os.path.basename(run)
    m = re.match(r"team_v[\d_]+__(.+)\.json$", b) or re.match(r"(.+?)(?:_transfer)?_response_v[\d._]+\.json$", b)
    return os.path.join(adir, "cases", m.group(1) + ".json"), m.group(1)


def grab(text, label):
    # first "LABEL:" not preceded by a letter (so "CONFIDENCE" does not match inside "STAGE CONFIDENCE")
    m = re.search(r"(?<![A-Z ])" + re.escape(label) + r":\s*([^\n]*)", text)
    if not m and label == "TIMING":
        m = re.search(r"TIMING[A-Z ]*:\s*([^\n]*)", text)
    if not m:
        return "—"
    val = re.split(r"\s+(?:—|–|-)\s+|\.\s|;\s|\s\|\s", m.group(1).strip(), maxsplit=1)[0]
    return val[:70]


def main():
    root = sys.argv[1]
    rows = []
    for adir in sorted(glob.glob(os.path.join(root, "agents/team_*"))):
        a = os.path.basename(adir)
        v, runs = final_runs(adir)
        for r in runs:
            cpath, cname = case_for(adir, r)
            case = json.load(open(cpath)) if os.path.exists(cpath) else {}
            d = json.load(open(r))
            text = "\n".join(d.get(f, "") for f in FIELDS)
            labs = {l: grab(text, l) for l in HEAD[a]}
            abst = len(d.get("abstention_or_more_information_needed", []))
            rows.append((case.get("emerging_technology", "?")[:60], SHORT[a], v, cname,
                         case.get("organization", "?")[:70], labs, abst))
    by_tech = defaultdict(list)
    for row in rows:
        by_tech[row[0]].append(row)
    md = "--md" in sys.argv
    for tech in sorted(by_tech):
        print(f"\n### {tech}\n" if md else f"\n== {tech}")
        if md:
            print("| Agent | Ver | Case | Organization | Headline labels | Abst. items |\n|---|---|---|---|---|---|")
        for t, ag, v, cn, org, labs, abst in sorted(by_tech[tech], key=lambda x: (x[1], x[3])):
            lab = "; ".join(f"{k}={v2}" for k, v2 in labs.items())
            if md:
                print(f"| {ag} | {v} | {cn} | {org.replace('|', '/')} | {lab.replace('|', '/')} | {abst} |")
            else:
                print(f"  {ag:11} v{v:4} {cn:12} | {org[:45]:45} | {lab} | abst={abst}")


if __name__ == "__main__":
    main()
