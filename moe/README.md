# Silver-Milk Final MoE Architecture and Orchestration Package (Team Lab 10)

**Version:** 1.0-design. **Ratified:** 2026-11-24. **Tag:** `moe_design-v1.0-team`. **Status:** designed, not built (built and tested in Lab 11).

## What the team had to produce → where
| Memo item | File |
|---|---|
| 1. Architecture/routing diagram (intake, seven specialists, evidence/governance check, synthesis, human review, logs, fallback) | `architecture_diagram.svg`; spec §1 |
| 2. Orchestrator rules: which experts run, what context they receive and return, missing/failed/abstaining experts | `MoE_Architecture_Spec.md` §2 (O-1 to O-13); `expert_contract.json` |
| 3. Conflict-resolution and synthesis rules that keep disagreement visible | spec §3 (checks and flags F-1 to F-11), §4 (conflict rows, narrow synthesizer, action-to-stage map); `synthesizer_instructions.md` |
| 4. Management-facing output and human authority | spec §5 (brief, dispositions, fallback, logs), §6 (who may decide what) |
| 5. Three-case system test plan with acceptance criteria | `system_test_plan.md` |
| AI as architecture critic | `critique/` (packet, raw ChatGPT reply, `disposition.md`) |
| Dry run on one contemporary case | `dry_run/` (robotics case and pack, 14 runs, brief, synthesizer reply and check, `dry_run_report.md`) |
| Post-class integration work list | `integration_work_list.md` |
| Version before critique and dry run | `records_v0_9/` |
| I-01 evidence from Labs 3–9 | `evidence/cross_lab_label_table.md` |

## Team decision (confirmed as written by Justin Zhong in session, including the operator-drafted rules; D-70 to D-79)

**Routing:**
- All seven team specialists always run, in three fixed waves, driven by a local script.
- Wave 1: Creation, Innovation, Promethean, Diffusion, Landscape.
- Wave 2: Adoption, reading Diffusion's stage and timing, Promethean's class and weight, and Landscape's stance and execution gates, verbatim.
- Wave 3: Org Adoption, reading Adoption's action and gates.
- No language model routes.

**Shared evidence:** a dated source pack curated at intake, checked and classed by the evidence keeper, frozen for all seven.

**The one recommendation:** the Adoption Agent's action. The system may only qualify it:
- when Org Adoption is not ready for the stage the action executes, the headline reads `PREPARE ONLY` and the owner must decide (F-10)
- every action that starts work (Adopt, Bounded experiment, Proof of concept) goes to the owner (F-11)
- conflicts are shown side by side and never averaged
- vendor selection is always the owner's

**The synthesizer:** one narrow ChatGPT run. It writes only the tradeoff prose and conflict explanations, each sentence backed by an exact quoted expert passage that a script checks.

**Human authority:**
- The named decision owner reviews whenever any of eleven flags fires.
- Only a no-start brief (Monitor, Defer, Reject for now, Withheld) with no flags is issued "Accepted by rule", and it can be reopened.
- **What the synthesizer may decide:** nothing beyond its own prose. It cannot change the action, resolve a conflict, add evidence or state an overall confidence.
- **What the human may override:** everything: the action, the conditions, starting despite PREPARE ONLY, and vendor choice. The reason goes in the disposition, never as an edit to an expert's output.

## Best evidence
- **Dry run on robotics** (14 ChatGPT runs, GPT-6.2 Sol, Light):
  - All seven experts produced valid output.
  - The upstream reads worked as designed.
  - The system proposed *Proof of concept*, while Org Adoption said *Not ready* for that stage (no budget, no owner). This is the conflict that led to `PREPARE ONLY` + F-10.
- **An accidental same-packet rerun of Wave 1** showed two pack-bound or routed labels flipping (Innovation ENTREPRENEURSHIP, Promethean WEIGHT). That is now limitation W-1, test AC-C4, and the reopening of D-18.
- **The ChatGPT critic** returned 17 findings. The team accepted 16 (CR-4 through the narrowed synthesizer, CR-15 in part), deferred fixtures to Lab 11, and rejected CR-1.
- **The synthesizer** passed every mechanical check but credited three experts with requests they never made. That is why it was narrowed.

## Dissent and limits
- **No member dissent was raised in session.** Recorded alternatives, not dissent: the critic's CR-1 ("the owner should always decide"; the team rejected it because flags now cover what matters: F-11 sends every action that starts work to the owner, F-10 every readiness block, F-5 Adopt or Severe, F-6 vendor choice) and its simplest alternative (drop the synthesizer).
- **Limits** (spec §7):
  - W-1: rerun instability
  - W-2: review-when-flagged has been measured on one case only
  - W-3: first GPT-6.2 Sol runs of the older agents
  - W-4: project textbook access
  - W-5: no comparison across cases inside one run
  - W-6: **1.0-design changed after the dry run and has not been re-run**
  - W-7: the robotics pack is pending Karuna Srivastava's check
- **Biggest unresolved conflict:** prepare versus start, when the action is sound but the organization is not ready.
- **Criterion most likely to fail:** AC-C4 (rerun stability).

## Roles (D-67)
- Justin Zhong: operator and submitter
- Yuanxiang Zhang: facilitator
- Karuna Srivastava: evidence keeper
- Dian Li: skeptic
- Nini Huang: test-plan owner and PR reviewer

All five present.

## AI use
- **Justin Zhong** coordinated the work and supplied every answer recorded as a team decision.
- **Claude Code** assisted with:
  - reading and inventorying the seven agents and the records
  - drafting the 0.9 and 1.0 specification, contract, synthesizer instructions, test plan, work list and records
  - drafting the robotics case
  - running the ChatGPT sessions through browser automation
  - writing the dry-run helper scripts
  - checking the outputs

  A Claude Code research subagent retrieved and summarized the 12 robotics source cards; they are pending the evidence keeper's check.
- **ChatGPT** (Work mode, GPT-6.2 Sol, Light, project MASY-1800) generated the architecture critique, all 12 expert replies and the synthesizer reply. All are saved unedited.
- **Operator error:** the operator launched five unplanned duplicate expert runs (D-68). They are kept and used as evidence.

## Handoff to Lab 11
- A version-identified design.
- A machine-readable contract for the seven experts.
- Three named cases with a frozen-before-run test plan.
- 12 work items (`integration_work_list.md`).
- Open issues: I-18, I-30, I-32, I-34, I-37, I-38.
