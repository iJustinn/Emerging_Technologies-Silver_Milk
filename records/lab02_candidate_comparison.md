# Lab 2 Candidate Comparison: Chart Improvement Practice Agents

**Status:** pre-read prepared before the team discussion (Justin, AI-assisted). §4 was completed in class on 2026-09-29.
**Packages selected:** Justin Zhong (`Zhong_Chart_Improvement_Agent.zip`) and Karuna Srivastava (`Karuna_Chart_Improvement_Practice_Scaffold_v1_0 3.zip`). The team chose these two as the stronger candidates for this exercise and decided not to include the individual candidates from Dian Li, Nini Huang, and Yuanxiang Zhang.
Purpose: to test the draft standard (`docs/team_agent_standard.md`) on real candidates and to build the team chart-improvement agent (v1.0) from them.

## 1. Checks run (same tools, same data for both)

| Check | Justin | Karuna |
|---|---|---|
| `check_frozen_core.py` in the candidate's own copy | `FROZEN CORE INTACT` | `FROZEN CORE INTACT` |
| `validate_response.py` (pristine tools), first and final response | PASSED / PASSED | PASSED / PASSED |
| Beyond the validator (§4): enums valid, no empty arrays, claimed file exists | OK. First-run `filename` was an absolute machine path, fixed in the revision | OK. v1 had an empty `abstention` array, filled in v2 |
| Every displayed number recomputed from `Titanic.xlsx` | All match (339/466 = 72.7%, 161/843 = 19.1%, +53.6 pp, 3.81×) | All 12 match (e.g., 3rd class: women 47/106 = 44.3%, children 39/106 = 36.8%, men 45/289 = 15.6%) |
| Baseline chart preserved | Yes (hash recorded in the Agent Record) | Yes (file present; no hash recorded) |
| Version lineage | `0.1-student` → `0.2-student`; **no git repo/commit** ("None" in the record) | `0.1` → `0.2`; commit `4cf00be` in her own repo, **but the ZIP has uncommitted changes** (modified `agent_record.md`, untracked `improved_chart.png`), so the commit does not match what was submitted |
| Preserved failure → revision → rerun | Yes. The chart showed only the sex half of the claim, so a scope rule was added and v1 files kept | Yes. The emphasis didn't match the title and labels overlapped, so an emphasis rule was added and v1 files kept |
| Package hygiene | Clean | Includes `.git/` and `.idea/` (IDE files) |

## 2. The comparison was not on a common case (main finding)

| | Justin | Karuna |
|---|---|---|
| Business question | The instructor text in `upload/business_question.txt`: sex vs. survival, with counts, rates, pp difference, and relative rate; association ≠ policy | A reworded question ("What evidence… that this rule was actually followed?"), written because her `business_question.txt` still held the placeholder |
| Audience / decision | NYT editor deciding whether a reporter's statement can be published | Maritime safety review board; whether the norm applied equally across classes |
| Baseline chart | Sex only, no labels | Women / children / men with rates and counts |
| Improved chart | 2 bars + a stat box (53.6 pp, 3.81×) + scope and causation notes | 9 bars by class, 3rd class highlighted, definitions and a missing-age note |

Different questions, audiences, and baselines mean the two outputs **cannot be ranked against each other**. This is the situation the General Instructions warn about ("use a common test… so the comparison is meaningful"). It is direct evidence for standard §5, step 2: fix one common case before any runs.

## 3. Differences worth debating (evidence for team judgment)

| Issue | Justin | Karuna | Evidence |
|---|---|---|---|
| Coverage of the claim | Tests only "women"; says on the chart that children were not tested | Covers women, children, and class. Has more analysis, but the standard says to verify, not start a new analysis | Charts; business question |
| Causal/policy language | Explicit on-chart "does not establish… policy" | Final subtitle: "*the policy pattern* was not equally strong across classes." The v1 title said "patterns *support*" the rule. JSON limitations do disclaim causation | `improved_chart.png`, `primary_response_v1.json` |
| Required numbers | pp difference and relative rate shown | No pp difference or relative rate (not required by her question) | Instructor question |
| Readability | Text-dense (self-reported) | Clean hierarchy; 1st/2nd class use two grays that encode nothing (self-reported) | Agent Records |
| Instruction design | Traceable YES/NO judgment on all 18 elements; claim-component mapping | 18 elements written as Check / FAIL / FIX rules; explicit list of testing failures | `specialist_instructions.md` (2,386 vs. 1,725 words) |

**Candidate rules for the team standard** (team decides which, if any, to adopt):
- R1: the case must quote the **exact** instructor question; a placeholder blocks the run.
- R2: the commit cited in the Agent Record must match the submitted files (clean working tree).
- R3: keep causal/policy wording out of titles and subtitles unless the evidence supports it.
- R4: no `.git`/IDE folders in submitted ZIPs.
- R5: adopt Karuna's Check / FAIL / FIX rule format as the team template for specialist instructions.

## 3b. T-03 result: common case (evidence, run in class)

Same instructor question, same baseline, same 5 inputs, three runs (see `test_failure_log.md` T-03, charts in `records/evidence/lab02_t03/`):

| Run | Agent | Audience | Title | On-chart limits | Checks |
|---|---|---|---|---|---|
| A | Karuna | NYT editor | "Female passengers had a higher survival rate" (generic) | No policy/cause; age NA included; **no "children not tested"** | All pass; numbers correct |
| B1 | Justin | Safety board | "Female survival was 53.6 percentage points higher" | "Child prioritization was not tested"; no policy/cause | All pass; numbers correct |
| B2 | Karuna | Safety board | "Female passengers had a higher survival rate" (generic) | No policy/cause; "children not analyzed separately" | All pass; numbers correct |

What this shows: once the case is common, the two agents produce nearly the same chart. That supports rule R1 and standard §5 step 2. The remaining differences are title strength and whether the chart itself says the children claim was untested. The swap test (editor → board) changed little for either agent. Decide whether that is fine for a fixed question or a sign of weak context sensitivity.

## 4. Team judgment (fill in class)

- Which rules (R1–R5) go into the standard: **all five** (D-04)
- Which candidate is stronger on the *common* case (T-03): no winner declared. They converge; Justin's agent writes a stronger title and states on the chart that the children claim was untested. Both candidates were merged into the team agent v1.0 (`records/contribution_lineage.md` in the ZIP).
- Dissent: none raised.
