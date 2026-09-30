# Team Agent Design and Integration Standard — Team Silver Milk

**MASY1-GC 1800 · Team Lab 2 · Version 1.0 — ratified in the 2026-09-29 workshop**  
Members: Dian Li, Justin Zhong, Karuna Srivastava, Nini Huang, Yuanxiang Zhang

> Governing question: *What fixed technical and professional rules must every team-approved specialist satisfy so the seven agents can later operate as one system?*
> Decisions marked **DECIDED** were settled in class on 2026-09-29. The team adopted the proposed defaults and rules R1–R5.

## 1. Fixed vs. editable (inspected in the practice scaffold)

| Category | Files | Rule |
|---|---|---|
| **FROZEN CORE** (hashed in `FROZEN_CORE_SHA256.txt`) | `core/common_instructions.md`, `core/input_schema.json`, `core/output_schema.json`, `tools/build_prompt.py`, `tools/check_frozen_core.py`, `tools/new_agent.py`, `tools/validate_response.py` | Never edit. `check_frozen_core.py` must print `FROZEN CORE INTACT` before any commit. |
| **Not hashed, but not ours to edit** | `agents/_template/`, `course_materials/`, top-level READMEs | Do not edit. The hash check will *not* catch changes here, so reviewers check by eye. |
| **Student-editable (one agent folder)** | `agents/<slug>/specialist_instructions.md`, `agent_metadata.json`, `cases/*.json`, `records/agent_record.md`, `assets/`, `responses/` | All specialist work happens here, created with `tools/new_agent.py`. |

The ET scaffold (`MASY1800_ET_Agent_Scaffold_v1_0`) is assumed to follow the same pattern; we re-confirm its frozen list when it is committed (see `scaffold/README.md`).

## 2. Common contract every specialist keeps

- Uses the frozen intake and output schema unchanged — no added, renamed, or dropped fields.
- Every finding separates **three levels**: the ET generally → the ET for the intended application → the ET for that application in this organization. Organizational posture changes interpretation and action, not the general evidence.
- Evidence is dated and sourced; evidence is separated from inference; unsupported claims are qualified or rejected.
- States confidence, assumptions, missing evidence, and when it abstains.
- Management implications: value, risk/governance, a bounded recommendation, and reassessment triggers.

## 3. Minimum evidence a specialist must carry to enter the team workspace

1. Completed **Agent Record** (all template fields; "None" is allowed only with a reason). The case quotes the **exact** instructor question, and a placeholder blocks the run (**R1**).
2. **Version + commit**: `version` in `agent_metadata.json` and the git commit SHA in the Agent Record. The cited commit must match the submitted files, with a clean working tree (**R2**). Submitted ZIPs contain no `.git/` or IDE folders (**R4**).
3. **Primary case** and **context-contrast case** (same technology, different organization/posture), each with the saved response JSON and validator output.
4. **One preserved failure** from an earlier run, plus the instruction revision it caused and the rerun result. Failed outputs stay in `responses/` under their original names; they are never deleted or overwritten.
5. **One named limitation** that remains unresolved.
6. **Transfer test passed:** the same specialist instructions, *unchanged*, run on a second case with a different question and baseline. They must pass the validator and the §4 review. Instructions hard-coded to one case fail this rule. (Added after the instructor's sample submission.)
7. **Verification note**: which consequential claims were checked against original sources, by whom.
8. `FROZEN CORE INTACT` output from the commit being promoted.

## 4. Passing validation is necessary, not sufficient

`validate_response.py` checks only that the top-level keys exist and have basic types. It does **not** check enum values, the fields inside array items, empty arrays, whether the artifact exists, or content. A pre-workshop probe (Justin, AI-assisted; for the team to re-run or confirm in class) saved a deliberately broken response (`priority: "urgent"`, zero data-fidelity checks, zero principles applied, a causal "proven" claim, `artifact_created: true` for a missing file). It printed **`VALIDATION PASSED`** (`records/evidence/lab02_weak_output_probe.json`, logged as T-02).

So every candidate also gets a **human context review**:
- **Swap test:** change the organization or posture in the case. If the organization-level finding barely changes, the agent is fluent, not contextual. (**DECIDED** after T-03: when the question fixes the content, as in the chart case, a small change is acceptable. For ET specialists the contrast case must change the organization, and the organization-level finding must change.)
- **Claim-language check:** no causal or policy wording in titles, subtitles, or headline findings unless the evidence supports it (**R3**).
- **Evidence test:** pick the two most consequential claims and trace each to a dated source.
- **Array/enum check:** no empty evidence arrays; enums match the schema.
- **Artifact check:** every file the response claims to have created exists.

## 5. Procedure for comparing candidates (Labs 3–9)

1. Every member arrives with their individual package (Agent Record, charts/responses, validation outputs).
2. The team fixes **one common primary case and one common contrast case** before any runs. Every candidate is run on the same saved inputs.
3. Score each candidate on the Section 3 evidence items and the Section 4 context review. Record the scores in the comparison table in `records/test_failure_log.md`.
4. Choose what survives: adopt one candidate, or combine specific instruction rules from several. Record which member's elements made it in and why.
5. Write specialist instructions as **Check / FAIL / FIX** rules, one per framework element (**R5**, from Karuna's candidate), and keep a traceable YES/NO judgment per element (from Justin's candidate).
6. Run the team version on both cases, validate, do the context review, then promote it (Section 6).
- **DECIDED — tie-breaker:** prefer the candidate with the stronger contrast-case behavior and traceable evidence, not the most polished prose or the longest code. If still tied, the skeptic's objection decides what gets retested.
- **Not allowed:** pasting outputs together, choosing by author or by length, or letting AI settle a conflict between criteria.

## 6. Versions, commits, and promotion into the team workspace

- Individual versions: `0.x-student`. On promotion the team version becomes **`1.0-team`**; later changes go to `1.1-team`, and so on.
- Promotion = one commit on `main` that adds `agents/<slug>/`, updates `records/agent_inventory.md`, adds a `records/decision_log.md` entry, and includes the `FROZEN CORE INTACT` output. Message: `Promote <slug> v1.0-team (Lab N)`. Git tag: `<slug>-v1.0-team`.
- A prior team decision is never overwritten without a new decision-log entry saying what changed and why.
- **DECIDED — pull requests:** the technical operator opens a PR and one other member reviews it before merge.

## 7. Roles and records

- **DECIDED — rotating roles each lab:** facilitator, technical operator, evidence keeper, skeptic. Lab 2 technical operator: Justin.
- Records kept in `records/`: decision log, agent inventory, test and failure log, evidence/source register, integration issue log, contribution record. The evidence keeper updates them before the session ends.
- AI (ChatGPT/Codex) may compare, critique, and draft; the team makes the decision. Consequential factual, current, regulatory, and market claims are checked against original sources.

## 8. Report-out

- **One frozen rule:** FROZEN CORE and the intake/output schema are never edited; `FROZEN CORE INTACT` is required on every promoted commit.
- **One team convention:** one common primary and contrast case for all candidates, with a `1.0-team` version and a git commit and tag on promotion.
- **One integration failure we intend to prevent:** a specialist that passes the validator but is generic or unsupported — fluent output that would silently bias the final MoE recommendation. Prevented by the Section 4 human context review.

## 9. Team decision

Every team-approved specialist must: keep FROZEN CORE and the frozen schema unchanged; keep the three-level ET → application → organization distinction; carry the Section 3 evidence package; pass both the validator and the Section 4 human context review; and enter `main` only through the Section 6 promotion procedure. Evidence: T-03 showed that two candidates that looked very different converged once they were run on the exact same case. So a common case (R1) is the rule most needed before any comparison.

## 10. Open issues and dissent

- **Inventory mismatch:** our Lab 1 mission lists creation, innovation, diffusion, *disruption*, *readiness*, adoption. The course's seven are Creation, Innovation, Promethean, Diffusion, Adoption, Organizational Adoption, Landscape. *Default:* follow the course seven; map "readiness" to Organizational Adoption; disruption is covered inside Promethean and Innovation. **DECIDED:** follow the course seven.
- **Carried from Lab 1:** how to reconcile conflicting specialist findings. Deferred to Lab 10 (`records/integration_issue_log.md`, I-01).
- **Blocker:** the ET scaffold ZIP is not yet in the team workspace; the standard was exercised on the Chart Improvement practice scaffold.
- **Public repo vs. frozen check:** the promotion procedure needs the scaffold's `tools/` in the repo, but instructor materials must not be published in a public repo. **DECIDED:** make the repo private before Lab 3 (owner: Justin; not yet done).
- **Dissent recorded:** none raised at ratification. Evidence that would reopen these decisions: a candidate that loses on the common case but clearly wins on a second case (would reopen the tie-breaker); a context-contrast case where the organization-level finding does not change (would reopen the swap-test threshold).
- **Participation limitation:** only 2 of 5 members (Justin, Karuna) brought individual chart-agent packages; the comparison therefore covers two candidates.

## 11. Version, AI use, and handoff

- **Version / workspace:** `github.com/iJustinn/Emerging_Technologies-Silver_Milk`, v1.0 (commit ID in the submission). Contributions: `records/contribution_record.md`.
- **AI use / verification:** Claude Code drafted v0, the records, and the candidate comparison, and operated the T-03 runs in ChatGPT Work for Justin. Claims were checked by running the local tools (`check_frozen_core.py`, `new_agent.py`, `build_prompt.py`, `validate_response.py`) and by recomputing every chart number from `Titanic.xlsx` (T-01 to T-03). The team decided the rules.
- **Final-project handoff:** gives the MoE system a common contract, the seven-agent inventory, a promotion and version procedure, and a comparison and testing protocol. Still open for integration: I-01 (reconciling conflicting findings) and I-02 (the validator checks only structure).
