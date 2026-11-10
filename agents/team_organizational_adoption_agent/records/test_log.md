# Test log (Lab 8)

**Runtime:**
- ChatGPT web in Ego Lite, Work mode, GPT-6.1 Sol at Light (Power slider stop 1 of 0–5; None and Minimal sit below it; Light kept by team choice, D-44).
- A fresh chat per run inside project MASY-1800. Project settings read 2026-11-10: instructions empty; Memory Default; Space access Enabled; source `1800-Textbook.pdf`.
- Packet attached; message `[Run <ID>] …`.
- Run map: `common_test_package/runmap.txt` (ZIP). Launcher and collector: `common_test_package/launch.sh`, `collect.sh`.

**Handling incidents:**
- After the second run, the ChatGPT interface switched to Chinese and back to Chat mode with model "5.6 / Medium".
- The first launcher's check (an English "Work" label) stopped the next eight sends. None was submitted, and the draft text and attachment were cleared.
- The launcher was rewritten to read the visible model and effort labels ("GPT-6.1 Sol" and "Light"/"轻度") and to switch to Work when needed. Every later run printed `GPT-6.1 Sol | 轻度`.
- L8-L-P aborted once (attachment not ready) and was relaunched.
- L8-Z-C was launched by the first launcher, which confirmed Work mode and GPT-6.1 Sol but did not read the effort label.
- Collection: a programmatic click on the copy button left the clipboard empty. A real pointer click copied the reply, and that copy matched the page text exactly (checked on L8-Z-P). All 18 replies were saved with `save_resp.py` under a UTF-8 locale: zero characters removed, no repairs.

| Test | Result |
|---|---|
| T-50 to T-57, candidates | 10 runs valid (validator and strict schema). See `lab08_candidate_comparison.md` |
| T-58 v0.9, 4 cases | Valid. Not ready / Undetermined / Undetermined / Undetermined. **Preserved failure:** DEMAND labels drift across the pair (R-2 FAIL in `checks_v0_9.txt`). Weaknesses: gate-dependent unknown (contrast D4); OPERATING OWNER forced to "None currently exists" for silence |
| T-59 v1.0, 4 cases | Valid. Same verdicts. Pair DEMAND and FIT identical. One mechanical FAIL: contrast 1 COUNTS (W-1). `final_checks_v1_0.txt` |
| T-60 check proof | Every new check fails or flags on its target (5 synthetic edited copies, 4 real outputs, including a wrong pair). `common_test_package/check_proof_on_targets.txt` |

**Human §4 review (v1.0):**
- **Swap test passes:** the two-person retailer is Not ready (D1, D8 Not ready); the staffed retailer is Undetermined, its gaps reduced to D1 Partially ready plus unknown approval and coordination roles. Step 1 and Step 2 labels are identical.
- **Prerequisites stay conditions:** vendor terms, tool selection and management authorization are listed under EXECUTION GATES and never become the gap. Contrast 1 lists two gates with "Owner: not stated" (vendor selection, term acceptance), which R-8 would treat as a D6 question.
- **Lane is clean:** no adopt, experiment or vendor decision; six handoffs in each run.
- **Missing-info case:** gives eight MORE INFO lines and asks first about D6 approval and stop authority.
- **Transfer (SaaS coding agents)** passes with unchanged instructions: provisions stated for the IDE assistant are not extended to the agent (Insufficient evidence for D4 and D6), which is [Z]'s preserved v0.1 lesson.

**Weaknesses:** W-0 to W-7 in `agent_record.md`. W-0 is the main one: F1 made every DEMAND label Moderate.
