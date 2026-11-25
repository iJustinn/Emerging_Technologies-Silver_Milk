#!/usr/bin/env python3
"""Lab 10 dry-run helper (not the Lab 11 orchestrator): read the contract's headline and
confidence labels from saved expert outputs, keyed on agent + label.
Usage: moe_labels.py <responses dir> <run prefix> [<second run prefix> to compare]
  e.g. moe_labels.py dry_run/responses moe_L10-DR moe_L10-DR-dup"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
CONTRACT = json.load(open(os.path.join(HERE, "expert_contract.json")))


def text_of(d):
    parts = []
    for k, v in d.items():
        if isinstance(v, str):
            parts.append(v)
        elif isinstance(v, list):
            parts += [x if isinstance(x, str) else json.dumps(x, ensure_ascii=False) for x in v]
    return "\n".join(parts)


def read_label(text, label):
    """First 'LABEL:' not preceded by a letter or a space after a capital (so CONFIDENCE != STAGE CONFIDENCE)."""
    m = re.search(r"(?<![A-Za-z])(?<![A-Z] )" + re.escape(label) + r"\s*:\s*([^\n]*)", text)
    return m.group(1).strip() if m else None


def labels_for(expert, path):
    if not os.path.exists(path):
        return None
    d = json.load(open(path))
    t = text_of(d)
    out = {}
    for h in expert["headline"]:
        # the contract's named field first (a label can appear twice in one output, e.g. Landscape MOVEMENT), then anywhere
        fields = [f.strip() for f in h.get("field", "").replace(" or ", ",").split(",") if f.strip() in d]
        v = None
        for f in fields:
            ft = d[f] if isinstance(d[f], str) else "\n".join(map(str, d[f]))
            v = read_label(ft, h["label"]) or (read_label(ft, h["alt_label"]) if h.get("alt_label") else None)
            if v:
                break
        if v is None:
            v = read_label(t, h["label"]) or (read_label(t, h["alt_label"]) if h.get("alt_label") else None)
        out[h["label"]] = v
    c = expert["confidence"]["label"]
    if c:
        first = c.split(" / ")[0].split(" <")[0]
        cu = d.get("confidence_and_uncertainty", "")
        m = re.search(re.escape(first) + r"[^:\n]{0,60}:\s*([^\n]*)", cu)  # Promethean: 'CONFIDENCE AT LEAST <class>:'
        out["(confidence) " + first] = m.group(1).strip() if m else None
    out["(version)"] = d.get("agent", {}).get("version")
    out["(abstention items)"] = len(d.get("abstention_or_more_information_needed", []))
    return out


def short(v, n=95):
    return "MISSING" if v is None else str(v)[:n]


def main():
    rdir, prefixes = sys.argv[1], sys.argv[2:]
    for e in CONTRACT["experts"]:
        runs = [labels_for(e, os.path.join(rdir, f"{p}__{e['folder']}.json")) for p in prefixes]
        if all(r is None for r in runs):
            continue
        print(f"\n== {e['name']} (wave {e['wave']})")
        keys = next(r for r in runs if r).keys()
        for k in keys:
            vals = [short(r.get(k)) if r else "—" for r in runs]
            same = "" if len(vals) == 1 else ("  SAME" if len(set(vals)) == 1 else "  DIFFERS")
            print(f"  {k}:{same}")
            for p, v in zip(prefixes, vals):
                print(f"     [{p}] {v}")


if __name__ == "__main__":
    main()
