# Seven-agent integration-readiness audit (Lab 9, 2026-11-17)

Memo item 5. The audit read every team agent at its tag on `main` (`6f6a83c`), plus this lab's `team_landscape_agent` 1.1-team. Method: `agent_metadata.json`, `specialist_instructions.md`, and the final-version team runs saved in each agent's `responses/`, scanned by a script (`audit7.py`, kept in the ZIP's `common_test_package/`) and read by eye. **Team decision (D-63):** the seven are consistent and versioned enough to **begin MoE design**; the mismatches below go to the issue log for Lab 10. No promoted agent was edited in Lab 9.

## Inventory

| # | Agent (`name`) | Version | Tag on `main` | Final team runs | Headline label(s) the orchestrator reads | Open weaknesses / issues |
|---|---|---|---|---|---|---|
| 1 | Silver-Milk Team Creation Agent | 1.0-team | `team_creation_agent-v1.0-team` ✔ | 3 (`*_response_v1.0.json`) | NEED, PREDECESSORS, ENABLERS, arc stage | I-05 |
| 2 | Silver-Milk Team Innovation Classification Agent | 1.1-team | `team_innovation_classification_agent-v1.1-team` ✔ | 3 (`*_response_v1_1.json`) | LIFECYCLE, DEGREE | I-09, I-10 |
| 3 | Silver-Milk Team Promethean Classification Agent | 1.0-team | `team_promethean_classification_agent-v1.0-team` ✔ | 4 (`*_response_v1_0.json`) | SIGNIFICANCE CLASS, WEIGHT | I-11, I-12, I-13 |
| 4 | Silver-Milk Team Diffusion Agent | 1.0-team | `team_diffusion_agent-v1.0-team` ✔ | 3 (`team_v1_0__*.json`) | TECHNOLOGY / APPLICATION / PEER GROUP STAGE, TIMING | I-15, I-16 |
| 5 | Silver-Milk Team Adoption Agent | 1.0-team | `team_adoption_agent-v1.0-team` ✔ | 4 (`team_v1_0__*.json`) | RECOMMENDATION, DEFER GATE, POSTURE GATE | I-17, I-18, I-19 |
| 6 | Silver-Milk Team Organizational Adoption Agent | 1.0-team | `team_organizational_adoption_agent-v1.0-team` ✔ | 4 (`team_v1_0__*.json`) | READINESS VERDICT, STAGE LADDER, EXECUTION GATES | W-0 (D-53), I-21 to I-24 |
| 7 | Silver-Milk Team Landscape Agent | **1.1-team** (this lab) | `team_landscape_agent-v1.1-team` (PR, Lab 9) | 4 (`team_v1_1__*.json`) | STANCE (with CONDITION STATUS, MOVEMENT), EXECUTION GATES, triggers | W-1 to W-6 below |

## What is consistent across all seven
- Frozen intake and output schema unchanged; `FROZEN CORE INTACT` on every promotion.
- Three levels kept in `general_et_finding` → `application_finding` → `organization_specific_finding`, each with labelled parts.
- Every evidence `notes` starts `STATUS: inspected-this-run | supplied | unverified` (all final runs of all seven).
- One evidence-type vocabulary (`primary-technical`, `primary-historical`, `dated-market`, `secondary`, `inference`, `case-premise`), used in every final run; Landscape adds `SOURCE CLASS:` inside `notes` instead of changing it (D-59).
- Every agent writes `HANDOFF →` lines naming the other six.
- No agent makes another agent's call (checked by each lab's lane review).

## Mismatches found (logged as I-25 to I-31)
1. **Vendor selection has no owner (I-25).** Adoption and Org Adoption hand "which vendor, tool, model or deployment product" to the Landscape Agent; Landscape 1.1 compares documented options and never selects (`OPTIONS DOCUMENTED: … NO SELECTION`, D-59). Selection is a human procurement decision; the orchestrator must route it there, not to a specialist.
2. **Two evidence taxonomies (I-26).** The memo's source classes (vendor / analyst / independent / standards / inference) exist only in Landscape's `SOURCE CLASS`; the other six cannot tell a vendor page from an independent study inside `dated-market` or `secondary`.
3. **Shared label names (I-27).** `FIT` and `NOW` (Adoption, Org Adoption), `UNIT` (Adoption, Diffusion, Org Adoption, Landscape), `UPSTREAM READ` (Adoption, Org Adoption), `EXECUTION GATES` (Org Adoption, Landscape), `POSTURE EFFECT` (Adoption, Diffusion, Promethean). Same names, different meanings in places (Adoption's `FIT` is a gate; Org Adoption's is task-technology fit). Extends I-09: the orchestrator must key on agent + label.
4. **Handoff name for Innovation (I-28).** Creation's runs write `Innovation Classification Agent`; the others write `Innovation Agent`. The `name` field says "Silver-Milk Team Innovation Classification Agent".
5. **Run-file naming (I-29).** Three conventions: `primary_response_v1.0.json`, `primary_response_v1_0.json`, `team_v1_0__primary.json`. A loader must handle all three, or Lab 11 renames.
6. **Promotion reviews not recorded on GitHub (I-30).** PRs #2 to #6 were merged by the operator's account with no GitHub review (D-27, D-34, D-42, D-50, D-58). The standard §6 asks for one member's review.
7. **Stance cadence vs. other agents' timing (I-31).** Landscape's `Scheduled watch` / `Active watch` is monitoring cadence, Diffusion's `TIMING` is urgency, and Adoption's `Monitor` is an action. Same words, three meanings; never merge them.
8. **Carried open:** I-05/I-10/I-13/I-15/I-19 (general labels follow per-run retrieval) — **the single most important integration issue** (team report-out, D-64). Proposed owner of the reconciled source pack: Landscape; mechanism decided in Lab 10 (D-63). Also D-53's W-0 (Org Adoption's DEMAND labels all Moderate): its reopen condition ("a later lab needs Step 1 to tell technologies apart") is not triggered by Lab 9.

## Not checked
Whether each older agent still behaves the same on GPT-6.2 Sol (Labs 3–8 ran on GPT-6.1 Sol or GPT-6). No older agent was rerun in Lab 9.
