# Team Agent Design and Integration Standard — Team Silver Milk

**MASY1-GC 1800 · Team Lab 2 · Status: DRAFT v0 — for team ratification in the 2026-09-29 workshop**
Members: Dian Li, Justin Zhong, Karuna Srivastava, Nini Huang, Yuanxiang Zhang

> Governing question: *What fixed technical and professional rules must every team-approved specialist satisfy so the seven agents can later operate as one system?*
> Items marked **TEAM DECIDES** carry a suggested default; the team confirms, changes, or records dissent in class.

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

1. Completed **Agent Record** (all template fields; "None" is allowed only with a reason).
2. **Version + commit**: `version` in `agent_metadata.json` and the git commit SHA in the Agent Record.
3. **Primary case** and **context-contrast case** (same technology, different organization/posture), each with the saved response JSON and validator output.
4. **One preserved failure** from an earlier run, plus the instruction revision it caused and the rerun result. Failed outputs stay in `responses/` under their original names; they are never deleted or overwritten.
5. **One named limitation** that remains unresolved.
6. **Verification note**: which consequential claims were checked against original sources, by whom.
7. `FROZEN CORE INTACT` output from the commit being promoted.

## 4. Passing validation is necessary, not sufficient

`validate_response.py` checks only that the top-level keys exist and have basic types. It does **not** check enum values, the fields inside array items, empty arrays, whether the artifact exists, or content. A pre-workshop probe (Justin, AI-assisted; for the team to re-run or confirm in class) saved a deliberately broken response (`priority: "urgent"`, zero data-fidelity checks, zero principles applied, a causal "proven" claim, `artifact_created: true` for a missing file). It printed **`VALIDATION PASSED`** (`records/evidence/lab02_weak_output_probe.json`, logged as T-02).

So every candidate also gets a **human context review**:
- **Swap test:** change the organization or posture in the case. If the organization-level finding barely changes, the agent is fluent, not contextual.
- **Evidence test:** pick the two most consequential claims and trace each to a dated source.
- **Array/enum check:** no empty evidence arrays; enums match the schema.
- **Artifact check:** every file the response claims to have created exists.

## 5. Procedure for comparing candidates (Labs 3–9)

1. Every member arrives with their individual package (Agent Record, charts/responses, validation outputs).
2. The team fixes **one common primary case and one common contrast case** before any runs. Every candidate is run on the same saved inputs.
3. Score each candidate on the Section 3 evidence items and the Section 4 context review. Record the scores in the comparison table in `records/test_failure_log.md`.
4. Choose what survives: adopt one candidate, or combine specific instruction rules from several. Record which member's elements made it in and why.
5. Run the team version on both cases, validate, do the context review, then promote it (Section 6).
- **TEAM DECIDES — tie-breaker:** *default:* prefer the candidate with the stronger contrast-case behavior and traceable evidence, not the most polished prose or the longest code. If still tied, the skeptic's objection decides what gets retested.
- **Not allowed:** pasting outputs together, choosing by author or by length, or letting AI settle a conflict between criteria.

## 6. Versions, commits, and promotion into the team workspace

- Individual versions: `0.x-student`. On promotion the team version becomes **`1.0-team`**; later changes go to `1.1-team`, and so on.
- Promotion = one commit on `main` that adds `agents/<slug>/`, updates `records/agent_inventory.md`, adds a `records/decision_log.md` entry, and includes the `FROZEN CORE INTACT` output. Message: `Promote <slug> v1.0-team (Lab N)`. Git tag: `<slug>-v1.0-team`.
- A prior team decision is never overwritten without a new decision-log entry saying what changed and why.
- **TEAM DECIDES — direct push vs. pull request:** *default:* the technical operator opens a PR and one other member reviews it before merge.

## 7. Roles and records

- **TEAM DECIDES — rotating roles each lab:** facilitator, technical operator, evidence keeper, skeptic.
- Records kept in `records/`: decision log, agent inventory, test and failure log, evidence/source register, integration issue log, contribution record. The evidence keeper updates them before the session ends.
- AI (ChatGPT/Codex) may compare, critique, and draft; the team makes the decision. Consequential factual, current, regulatory, and market claims are checked against original sources.

## 8. Report-out

- **One frozen rule:** FROZEN CORE and the intake/output schema are never edited; `FROZEN CORE INTACT` is required on every promoted commit.
- **One team convention:** one common primary and contrast case for all candidates, with a `1.0-team` version and a git commit and tag on promotion.
- **One integration failure we intend to prevent:** a specialist that passes the validator but is generic or unsupported — fluent output that would silently bias the final MoE recommendation. Prevented by the Section 4 human context review.

## 9. Team decision *(pending ratification)*

Every team-approved specialist must: keep FROZEN CORE and the frozen schema unchanged; keep the three-level ET → application → organization distinction; carry the Section 3 evidence package; pass both the validator and the Section 4 human context review; and enter `main` only through the Section 6 promotion procedure.

## 10. Open issues and dissent (fill in class)

- **Inventory mismatch:** our Lab 1 mission lists creation, innovation, diffusion, *disruption*, *readiness*, adoption. The course's seven are Creation, Innovation, Promethean, Diffusion, Adoption, Organizational Adoption, Landscape. *Default:* follow the course seven; map "readiness" to Organizational Adoption; disruption is covered inside Promethean and Innovation. TEAM DECIDES.
- **Carried from Lab 1:** how to reconcile conflicting specialist findings. Deferred to Lab 10 (`records/integration_issue_log.md`, I-01).
- **Blocker:** the ET scaffold ZIP is not yet in the team workspace; the standard was exercised on the Chart Improvement practice scaffold.
- **Public repo vs. frozen check:** the promotion procedure needs the scaffold's `tools/` in the repo, but instructor materials must not be published in a public repo. Must be resolved before Lab 3 (make the repo private, or get instructor approval). TEAM DECIDES.
- **Dissent recorded:** _(none yet — record any disagreement about versioning, testing, evidence quality, or workspace conventions here)_

## 11. Version, AI use, and handoff

- **Version / workspace:** `github.com/iJustinn/Emerging_Technologies-Silver_Milk`, draft v0 at commit `1d851d5` (updated after ratification). Contributions: `records/contribution_record.md`.
- **AI use / verification:** Claude Code drafted this v0 and the record templates from the course instructions and scaffold files. Claims about the scaffold were checked by running the local tools: `check_frozen_core.py`, `new_agent.py`, `build_prompt.py`, and `validate_response.py` on saved responses and on the probe (T-01, T-02). The rules themselves are the team's to accept.
- **Final-project handoff:** gives the MoE system a common contract, the seven-agent inventory, a promotion and version procedure, and a comparison and testing protocol. Still open for integration: I-01 (reconciling conflicting findings) and I-02 (the validator checks only structure).
