#!/usr/bin/env python3
"""Save the ChatGPT response currently on the clipboard.

Writes <out>.raw_copy.txt (clipboard exactly as copied) and <out>.json.
The .json removes only ChatGPT citation markers and an outer ``` fence;
no other text is changed. Then runs the frozen validator.
Usage: python3 common_test_package/save_resp.py <out_path_without_ext>
"""
import json, re, subprocess, sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
out = Path(sys.argv[1])
J = Path(str(out) + ".json"); RAW = Path(str(out) + ".raw_copy.txt")
out.parent.mkdir(parents=True, exist_ok=True)
raw = subprocess.run(["pbpaste"], capture_output=True, text=True).stdout
RAW.write_text(raw)

text = re.sub(r":?chatgpt-content-reference\{[^}]*\}", "", raw)
text = re.sub(r"[^]*", "", text)  # private-use citation tokens, if any
text = text.strip()
text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text)
removed = len(raw.strip()) - len(text)
data = json.loads(text)
J.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

res = subprocess.run([sys.executable, str(root / "tools/validate_response.py"), str(J)],
                     capture_output=True, text=True)
print(res.stdout.strip())
print(f"raw chars={len(raw)} removed_by_cleanup={removed}")
print("agent:", data.get("agent"))
print("general_et_finding words:", len(data.get("general_et_finding", "").split()),
      "| org words:", len(data.get("organization_specific_finding", "").split()),
      "| evidence items:", len(data.get("evidence", [])))
for k in ["contrary_evidence_or_limitations", "change_monitoring_triggers", "abstention_or_more_information_needed"]:
    print(k, "items:", len(data.get(k, [])))
blob = json.dumps(data).lower()
print("case check: bank mentions =", blob.count("bank"), "| startup mentions =", blob.count("startup"),
      "| retailer mentions =", blob.count("retailer"))
