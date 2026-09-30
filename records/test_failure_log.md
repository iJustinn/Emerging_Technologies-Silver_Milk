# Test and Failure Log

| ID | Date | Lab | Test | Input | Result | Weakness / action |
|---|---|---|---|---|---|---|
| T-01 | 2026-09-29 | 2 (pre-class prep, Justin) | Frozen workflow exercised | Scratch copy of pristine Chart Practice Scaffold v1.0: `check_frozen_core.py` → `new_agent.py` → `build_prompt.py` | `FROZEN CORE INTACT`; agent folder created; 10,836-byte prompt packet built; still `FROZEN CORE INTACT` afterwards | ChatGPT run step not repeated. See T-01b for a full run |
| T-01b | 2026-09-29 | 2 (pre-class prep) | Validator on an individual candidate | Justin Zhong's chart agent: `first_run_primary_response.json` and `primary_response.json` | Both `VALIDATION PASSED`; that working copy is also `FROZEN CORE INTACT` | First run tested only the "women" half of the claim (preserved in its Agent Record) |
| T-02 | 2026-09-29 | 2 (pre-class prep, Justin; team to confirm) | Deliberately weak output probe | `records/evidence/lab02_weak_output_probe.json`: `priority:"urgent"`, empty fidelity/principles arrays, "proven" causal claim, `artifact_created:true` for a missing file | **`VALIDATION PASSED`**: the validator checks only structure | Human context review added (standard §4) |
| T-03 | | 2 (in class) | Context-contrast case | *(same case, different audience/organization)* | | |

Environment: Python 3.10.1, standard library only; no OpenAI API key used.

## Candidate comparison table (Labs 3–9)

| Lab | Candidate (member) | Version / commit | Primary | Contrast | Swap test | Evidence traced | Preserved failure | Selected elements |
|---|---|---|---|---|---|---|---|---|
