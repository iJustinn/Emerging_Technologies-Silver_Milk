# Lab 10 dry run: MOE-C-1 (robotics, test case C) against spec 0.9-design

**Date:** 2026-11-24. **Built against 0.9-design:** the template, flags and upstream blocks here were produced with `records_v0_9/expert_contract.json` and the 0.9 rules. After the 1.0 changes, `moe_labels.py` was rerun with the 1.0 contract on these same outputs, and the DR-1 flips are unchanged.

**Runtime:**
- ChatGPT web in Ego Lite, Work mode, GPT-6.2 Sol, Light, project MASY-1800.
- The launcher read the model and effort labels before every send.
- A fresh chat per run. Run IDs and notes are in `runmap_public.txt`; the chat URLs are in the package's `moe/runmap.txt` only, kept out of the public repo.

**Who did what:**
- **Justin Zhong** coordinated the runs and approved the case.
- **Claude Code** assisted. It drafted the case, ran the browser automation and wrote the dry-run helper scripts (`moe_labels.py`, `moe_upstream.py`, `moe_brief.py`, `moe_synth_check.py`). These are dry-run helpers, not the Lab 11 orchestrator.
- **The source pack** (`source_pack_robotics.md`, Pack ID `ROBOTICS-HUMANOID-TOTE-2026-11-24-v1`) was retrieved and summarized by a Claude Code research subagent, which opened each page on 2026-11-24. It is **pending the evidence keeper's (Karuna Srivastava's) check** under spec O-2.
- **ChatGPT** generated every expert, critic and synthesizer reply. Each is saved unedited (`*.raw_copy.txt`).

## Runs (14, team-approved after an overrun; budget was 12)

| Run | What | Result |
|---|---|---|
| L10-CR1 | Architecture critic on the 0.9-design package | 17 findings (`../critique/`) |
| L10-DR-W1-CRE / INN / PRO / DIF / LAN | Wave 1 on the identical packet | all `VALIDATION PASSED` |
| same five, `(dup)` | **Unplanned duplicates (operator error).** The launch loop printed no output, so the operator relaunched, and every Wave 1 expert ran twice on the byte-identical packet. All are kept as `moe_L10-DR-dup__*`. Used as a same-packet rerun test | all `VALIDATION PASSED` |
| L10-DR-W2-ADO | Adoption, with the upstream block built from the first-launch Wave 1 runs | `VALIDATION PASSED` |
| L10-DR-W3-ORG | Org Adoption, with Adoption's action and gates and Landscape's execution gates | `VALIDATION PASSED` |
| L10-DR-SYN | Synthesizer: template plus seven outputs plus pack. The first attempt aborted before sending (attachment not visible after 5 s); relaunched with a 15 s wait | S-2 check PASS; see DR-7 for what it misses |

## What the system produced (template: `brief_template_MOE-C-1.md`; synthesizer reply: `synth_reply_MOE-C-1.raw_copy.txt`)

**Proposed action (Adoption, verbatim):** Proof of concept — prepare an isolated feasibility proposal. Confidence: Moderate. Zone: Bleeding edge. DEFER GATE: None. POSTURE GATE: adoption only. CONSEQUENCE: Reversible.

**Readiness (Org Adoption):** Not ready (bounded evaluation), confidence High.
- MOST CONSEQUENTIAL GAP: D5 (no approved evaluation budget).
- STAGE LADDER: Preparation Supported · Bounded evaluation Blocked · Routine operation Blocked.
- COUNTS were recomputed from the D-lines (G-2): 1/4/1/2, matching the agent's own line.

**General level (all hedged):**
- Creation: Emerging→Developing
- Innovation: DEGREE Contested (breakthrough candidate)
- Promethean: Indeterminate (Incremental | Breakthrough)
- Diffusion: every stage Withheld, TIMING Patience
- Landscape: Scheduled watch (Partly met × None)

**Conflicts:** five rows, all proposed as type Q by the synthesizer. Every label difference answers a different question.

**Flags fired:**
- F-4: the case memo's "already in production at major 3PLs" was flagged and traced by Landscape.
- F-9: no coordinator, owner or budget.
- F-6 (operator): a proof of concept implies a vendor or tool choice.
- F-1 pending (see DR-5).

**→ The brief stays Draft; human review is required.**

## Findings

| ID | Finding | Evidence | Bears on |
|---|---|---|---|
| DR-1 | **Pack-bound labels still flip on an identical packet.** Innovation ENTREPRENEURSHIP: `Not established` vs `Incumbent-led` (the pack is supposed to fix it). Promethean WEIGHT: `Moderate` vs `Low`, and WEIGHT is routed to Adoption. Promethean confidence: `Low` vs `Moderate` | `checks_dry_run.txt`: `check_innovation_lab04 --pair` FAIL; `check_promethean_lab05 --pair` FAIL; `moe_labels.py` output | O-2, spec W-1, AC-C1; I-05 family. **A single MoE run cannot see this instability.** |
| DR-2 | **Landscape general label drifts** across the rerun: L1 TECHNICAL CAPABILITY `Developing` vs `Emerging` (Landscape retrieves; predicted as W-1). STANCE, CONDITION STATUS and MOVEMENT are stable | `check_landscape_lab09 --pair` FAIL | W-1 |
| DR-3 | **Stable on rerun:** Creation ARC STAGE; Innovation DEGREE, STATUS IN CASE, NOVELTY; Promethean SIGNIFICANCE CLASS; all Diffusion labels; Landscape stance inputs | `moe_labels.py` | — |
| DR-4 | **Interface defects found by extraction:** (a) Landscape writes `MOVEMENT:` twice (L3 tracker and Step 3), so extraction must read the named field first. (b) Promethean's confidence label embeds the class (`CONFIDENCE AT LEAST <class>:`). (c) Promethean's class value contains ` \| `, which splits on the team's part separator. (d) Org Adoption wrote its stage in lowercase, so its own Lab 8 format check fails. (e) Promethean writes both `WEIGHT OF BROAD SIGNIFICANCE ON THIS DECISION:` and `WEIGHT:` | Fixed in the dry-run helpers; matches critic CR-5 | contract, O-6, O-8 |
| DR-5 | **G-1 as written is too strict.** Landscape's organization finding was 322 words against a 320 cap, and Org Adoption's response format check failed only on case. Under draft O-10 both would force a rerun. Not rerun (budget) | `checks_dry_run.txt` | O-10, G-1 |
| DR-6 | **Upstream reads worked as designed.** Adoption typed the block `case-premise`, kept Patience as "a timing read only", and used the Promethean class for attention only. Org Adoption named Adoption's gates and Landscape's execution gates | Adoption and Org Adoption `UPSTREAM READ:` lines | O-5, O-6, AC-C3 |
| DR-7 | **Synthesizer: mechanically in bounds, but one unsupported attribution.** S-2 passed: action echoed exactly; every cite names an existing label; no new date, URL or number ("By 2027-01-15" traces to Org Adoption's DISTINGUISHING EVIDENCE, the stop rule to Adoption's PROPOSED STOP RULE). The operator read the whole reply: the five conflict rows are all Q, and TRADEOFFS stays inside the outputs. **Defects S-2 cannot see:** (a) `most_valuable_missing_evidence.asked_by` credits Creation, Innovation and Promethean with asking for funding, staffing and permissions, which none of them asks for (checked against their abstention lists); (b) two of four `caution_signals` are not cautions (they restate Landscape's stance and Diffusion's timing); (c) S-2 checks that a cited label exists, not that the condition follows from it | `synth_check_MOE-C-1.txt`; operator read of the full reply | S-2, critic CR-4, CR-10 |
| DR-8 | **"Review when flagged" fired on the first case** (F-4, F-6, F-9). This is the first data point for spec W-2 | brief §9 | H-1, critic CR-1 |
| DR-9 | **F-4's 18-month age rule would wrongly fire on durable standards.** ISO 10218-1:2025 is 21 months old but is the current edition | pack S10 | F-4 |
| DR-10 | **Operator tooling:** a multi-launch shell loop returned no output while the launches succeeded, which caused 5 duplicate runs. Lab 11's runner must log each launch to a file before relaunching anything | `runmap.txt` | O-9, I-16 |
| DR-11 | **First GPT-6.2 Sol runs of the six older agents.** Ran: the frozen validator, `check_common.py` and each agent's own lab check, on single runs. Results: all pass except DR-5's two format items, and the pair FAILs in DR-1/DR-2. Not exercised by any script: G-3, G-4, G-6. By hand: the pack-bound experts cite 0 retrieved items; the four `unverified` items (Creation E15/E16, Promethean E6/E7) are case-premise or inference, not external evidence; no expert selects a vendor (Landscape writes `NO SELECTION`). Every check FLAG was read: "transfer"/"already" are technical terms ("skill transfer"), and "verified" hits are "unverified" | `checks_dry_run.txt` | spec W-3 (D-55) |
| DR-12 | **The conflict table covered 5 of the 8 §4.2 pairs.** The other three were checked by hand. Adoption ↔ Diffusion: Bleeding edge vs Withheld, type Q. Expert ↔ pack: no pack-bound general label rests on retrieved evidence. Lab 1 example: not applicable. The closest factual tension: Diffusion "no dated routine-use account identifies the controlling model" vs Landscape "reported in live operations … remain unverified". These are consistent readings of S4/S5, so no type E/J row and **F-3 had nothing to fire on** | operator read | §4.2, F-3 |
| DR-13 | **Earlier decisions touched.** D-18's reopen condition is met: ENTREPRENEURSHIP drifted on identical supplied cards (DR-1). D-53: not recurred, since DEMAND labels are no longer all Moderate (D6 High). D-65: CONDITION STATUS is Partly met again, but this is not a clearly met or unmet case, so it is not triggered | DR-1; Org Adoption Step 1; Landscape Step 3 | decision log |

## Report-out (memo 56–60 min; as of 0.9-design, before the dispositions)
*Superseded in 1.0 (see `../README.md`): the conflict is now handled by `PREPARE ONLY` + F-10 and F-11; the criterion most likely to fail is now AC-C4.*

- **Architecture choice:** all seven, three fixed waves, script-run. Adoption's action is the headline. Template plus one bounded ChatGPT synthesizer, with a mechanical synthesis check. A human decides whenever a flag fires.
- **Biggest unresolved conflict:** Adoption says prepare a proof of concept, while Org Adoption says the organization is not ready to run one (no budget, no owner). Both are right about different questions. The design must make the owner choose between "prepare only" and "start", not let the headline imply a start.
- **Acceptance criterion most likely to fail:** AC-C1 (general-label stability), now with evidence. Two pack-bound labels flipped on an identical packet (DR-1). The critic independently named AC-C1, for a different reason: no exact baseline files.
