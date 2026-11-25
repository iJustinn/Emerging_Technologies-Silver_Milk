# Silver-Milk MoE System Test Plan (1.0-design)

Defined in Team Lab 10 **before** the integrated system is evaluated.
- **Test-plan owner:** Nini Huang.
- **Freeze:** Lab 11 freezes these cases and criteria at the start of its workshop. They are not rewritten after an inconvenient result (Lab 11 memo).
- **Changes from 0.9** (`records_v0_9/system_test_plan.md`): critic findings CR-15, CR-16, CR-17 and CR-8; dry-run findings DR-1 (new AC-C4) and D-73 (new AC-H4).

## 1. Three materially different cases (team choice, D-69)

| Case | Technology / application / organization | Why it is different | Intake and pack (no new research) |
|---|---|---|---|
| **A: Concept boards** | Text-to-image diffusion · internal advertising concept boards · hypothetical two-person U.S. online homeware retailer, aggressive for reversible internal experiments | Small, reversible, internal; best-checked cards; regression anchor | Merge Dian Li's Lab 7 Adoption primary and Lab 8 Org Adoption primary into one intake. Pack = the cards supplied in those two cases (E-40 to E-43, E-45 to E-49). Pack ID fixed at the Lab 11 freeze |
| **B: Bank coding agents** | AI coding agents · software change work · hypothetical mid-size U.S. regional bank, conservative, regulated, 24-month horizon, with the board-memo hype claim | Regulated, conservative, hard-to-reverse controls; hype pressure | Justin Zhong's case (`team_creation_agent/cases/primary.json`, hype memo from `team_landscape_agent/cases/contrast_3.json`). Pack from already-checked register entries (E-01 to E-13, E-29 to E-39, E-50 onward) |
| **C: Robotics** (Lab 10 dry run) | AI-enabled humanoid robots with VLA models · tote transfer at AMR–conveyor stations · hypothetical mid-size U.S. 3PL | Physical, safety-critical, capital-intensive; contemporary; thin independent evidence | `dry_run/case_robotics.json`, Pack `ROBOTICS-HUMANOID-TOTE-2026-11-24-v1`, **after Karuna Srivastava's card check** |

## 2. Acceptance criteria (pass/fail; one result per case unless noted)

| ID | Dimension | Criterion | How observed |
|---|---|---|---|
| AC-E1 | Evidence quality | Every expert passes the **hard** checks (validator, strict schema, pack discipline O-2a, recomputed COUNTS, no external `unverified` behind a headline, lane), after at most one rerun. Soft warnings are listed, not failed | Check log in the run record |
| AC-E2 | Evidence quality | Each decisive headline (Adoption RECOMMENDATION, Org Adoption READINESS VERDICT, Landscape STANCE) names its **supporting passage and source class**, and none rests only on `vendor-claim`. The evidence keeper reads those three passages against their sources | Script + evidence keeper's read |
| AC-E3 | Evidence quality | Every synthesizer `support.passage` occurs verbatim in the named expert's output. No date, URL or number appears outside the outputs and the pack | Support check (S-2) |
| AC-C1 | Contextual consistency | **Case A only**, against frozen baselines with the same cards. Promethean `SIGNIFICANCE CLASS` vs. `team_promethean_classification_agent/responses/primary_response_v1_0.json`. Adoption `MATURITY ZONE` and Step 1 labels vs. `team_adoption_agent/responses/team_v1_0__primary.json`. Org Adoption DEMAND set vs. `team_organizational_adoption_agent/responses/team_v1_0__primary.json`. A comparison whose baseline used different cards from the case-A pack is recorded as **changed input**, not passed or failed. Innovation and Diffusion have no baseline on this technology (covered by AC-C4) | Compare extracted labels; record pack differences |
| AC-C2 | Contextual consistency | No organization, industry, application or user words in any `general_et_finding` after a human read of each check FLAG. The brief's §3 keeps the three levels apart | Checks + read |
| AC-C3 | Contextual consistency | Adoption and Org Adoption show the upstream passages in `UPSTREAM READ`, typed `case-premise`, without re-deriving them | Check + read |
| AC-C4 | Contextual consistency (new, DR-1) | **Case A:** the routed Wave-1 experts (Promethean, Diffusion, Landscape) and Innovation are each run **twice** on the identical packet. Every routed label and every pack-bound label is identical across the two. A difference is a FAIL, preserved and logged | `moe_labels.py <dir> <run> <rerun>` |
| AC-R1 | Routing | All seven ran, in wave order. Each upstream line equals the full source line of the attempt the run record names | Script diff |
| AC-R2 | Routing | The run record has every O-13 field. No undocumented or duplicate chat exists for the Run ID (O-9) | Script + project chat list |
| AC-S1 | Synthesis | The PROPOSED ACTION category equals Adoption's `RECOMMENDATION`, plus `PREPARE ONLY` exactly when F-10 fires | Support check |
| AC-S2 | Synthesis | Every §4.2 row is present, with both readings verbatim. Nothing is averaged. `asked_by` for each missing-evidence item matches the experts whose abstention lists contain it | Script |
| AC-S3 | Synthesis | The brief contains no overall confidence claim. Each expert's original confidence words are kept | Script + read |
| AC-U1 | Usability | The brief fits one page. The test-plan owner, reading it cold, states the action (with any PREPARE ONLY), the top condition and the main conflict correctly in under two minutes | Timed read, recorded |
| AC-F1 | Failure handling | Injected: a **routed** Wave-1 expert (Diffusion) marked FAILED. The panel row shows `FAILED`, F-1 fires, and **the packet Adoption actually received** contains `Diffusion … unavailable` | Offline replay; inspect the Adoption packet |
| AC-F2 | Failure handling | Injected: Adoption output missing. The brief says `NO PROPOSED ACTION`, F-1 fires, and the status is Draft | Offline replay |
| AC-F3 | Failure handling | Injected: a synthesizer reply with a correct action echo and a real cite, but a passage altered to reverse a condition (the fixture CR-4 names). The support check fails, F-7 fires, and a script-only brief is issued | Offline replay with an edited copy (original kept) |
| AC-F4 | Failure handling | Injected through the **whole flow**: an intake with sponsor and owner `Not stated` → frozen packets → Org Adoption run → brief. F-9 fires from the intake and appears in the issued brief | One Org Adoption run on the edited intake + script replay |
| AC-H1 | Human authority | No brief with any flag is issued `Accepted by rule`. Every flagged brief carries a recorded disposition (name, date, reason) | Run record |
| AC-H2 | Human authority | No expert or synthesizer output selects a vendor, tool or model. If an action requires one, F-6 fires | G-6 + read |
| AC-H3 | Human authority | A Modify disposition keeps the expert reading beside the human one. Expert outputs and synthesizer text are byte-identical before and after | File hashes |
| AC-H4 | Human authority (new, D-73) | When Org Adoption is Not ready or Undetermined for the stage the action executes, the headline carries `PREPARE ONLY` with the gap named, and F-10 fires. Case C's dry-run outputs are the fixture: Proof of concept vs. Not ready (bounded evaluation) | Script replay on `dry_run/responses/` |
| AC-G1 | Risk / governance | TRADEOFFS or §2 names at least one risk or governance item, with its supporting passage | Read |

**Observation, not pass/fail (W-2):** the number of flags fired per case, and whether any case was issued `Accepted by rule`.

**Offline fixtures** (Lab 11 work list W-L8; built from saved outputs, no ChatGPT runs):
- AC-F1, AC-F2, AC-F3, AC-H4
- the CR-15 fixture: a vendor claim cited for the headline next to an independent item about a different claim must fail AC-E2

## 3. Pass rule
- **Passes** when, on all three cases, every AC passes (AC-C1 and AC-C4 on case A only) and every fixture passes once.
- **A failure** is preserved, logged as T-xx, and corrected only by a bounded, versioned change followed by a retest.

## 4. Criterion most likely to fail (updated after the dry run)
**AC-C4 (rerun stability).** In the Lab 10 dry run, Innovation ENTREPRENEURSHIP and Promethean WEIGHT, which is routed to Adoption, flipped on a byte-identical packet (DR-1). AC-C1 is second: the critic notes that baselines may not share the case-A pack (CR-16), which is why changed input is now recorded rather than failed.
