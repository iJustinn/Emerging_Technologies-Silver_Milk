# Silver-Milk MoE System Test Plan (0.9-design)

Defined in Team Lab 10, **before** the integrated system is evaluated. Lab 11 freezes these cases and criteria at the start of the workshop. They are not rewritten after an inconvenient result (Lab 11 memo). Test-plan owner: Nini Huang.

## 1. Three materially different cases (team choice, Lab 10 session)

| Case | Technology / application / organization | Why it is different | Intake and pack sources (no new research) |
|---|---|---|---|
| **A: Concept boards** | Text-to-image diffusion models · internal advertising concept boards · hypothetical two-person U.S. online homeware retailer, aggressive for reversible internal experiments | Small, reversible, internal; consumer marketing; best-checked cards; regression anchor (5 of 7 experts already ran on this technology in Labs 3–9) | Dian Li's Lab 7/8 primary case (`team_adoption_agent/cases/primary.json`, `team_organizational_adoption_agent/cases/primary.json`) merged into one intake; pack = the supplied cards in those cases (evidence register E-40 to E-43, E-45 to E-49) |
| **B: Bank coding agents** | AI coding agents · software change work · hypothetical mid-size U.S. regional bank, conservative, regulated, 24-month horizon, with the board memo "hype" claim | Regulated, conservative, hard-to-reverse controls; hype pressure; vendor-approval cycle | Justin Zhong's case (`team_creation_agent/cases/primary.json`; `team_landscape_agent/cases/contrast_3.json` hype variant); pack from checked register entries E-01 to E-13, E-29 to E-39 and E-50 onward (OCC/Fed supervisory items) |
| **C: Robotics (dry run in Lab 10)** | AI-enabled humanoid robots driven by robot foundation (VLA) models · tote moving in warehouse intralogistics · hypothetical mid-size U.S. third-party logistics provider | Physical, safety-critical, capital-intensive; the course's contemporary case; thin independent evidence | New intake and source pack drafted in Lab 10 (`dry_run/case_robotics.json`), checked by the evidence keeper |

The intakes and packs for cases A and B are assembled before Lab 11 from existing, already-checked material only (integration work list W-L1).

## 2. Acceptance criteria (pass/fail; one result per case unless noted)

| ID | Dimension | Criterion | How it is observed |
|---|---|---|---|
| AC-E1 | Evidence quality | Every expert output passes G-1 to G-4 (validator, strict schema, common and per-agent checks, recomputed COUNTS, pack discipline, no `unverified` behind a headline), after at most one rerun per expert | Check log in the run record |
| AC-E2 | Evidence quality | Every headline label in the brief traces to a pack card or a dated evidence item in that expert's output; no headline rests only on `vendor-claim` | Script trace + evidence keeper's read of the two most consequential claims per case against the original source |
| AC-E3 | Evidence quality | The synthesizer text adds no URL, date, number or source absent from the outputs and the pack | S-2 check |
| AC-C1 | Contextual consistency | **Case A only:** each pack-bound general label matches the label the same agent gave in its saved team run on the same technology and cards: Promethean `SIGNIFICANCE CLASS`, Adoption `MATURITY ZONE`, Org Adoption DEMAND set | Compare with `agents/*/responses/` final runs |
| AC-C2 | Contextual consistency | No organization, industry, application or user words in any `general_et_finding`; the brief's §3 keeps general / application / organization lines apart | Existing R-1 checks + brief layout |
| AC-C3 | Contextual consistency | Adoption and Org Adoption show the supplied upstream labels in `UPSTREAM READ`, typed `case-premise`, and do not re-derive them | Check + read |
| AC-R1 | Routing | All seven ran, in wave order. Each upstream block byte-matches the label lines in the source outputs | Script diff |
| AC-R2 | Routing | The run record has every O-13 field for every expert run | Script |
| AC-S1 | Synthesis | The brief's PROPOSED ACTION equals Adoption's `RECOMMENDATION` verbatim | S-2 check |
| AC-S2 | Synthesis | Every §4.2 pair whose labels disagree appears as a conflict row with both readings. Nothing is averaged. Every condition and caution cites agent + label | S-2 check + read |
| AC-S3 | Synthesis | No confidence in the brief is higher than the lowest decisive confidence | S-2 check |
| AC-U1 | Usability | The brief fits one page. The test-plan owner, reading it cold, states the proposed action, the top condition and the biggest conflict correctly in under two minutes | Timed read, recorded |
| AC-F1 | Failure handling | Injected: one Wave-1 expert marked FAILED. The brief shows the row `FAILED`, F-1 fires, and Adoption's upstream block says `unavailable` | Offline replay of a saved run with one output replaced by the Lab 2 weak-output probe |
| AC-F2 | Failure handling | Injected: Adoption output missing. The brief says `NO PROPOSED ACTION`, F-1 fires, and the status is Draft | Offline replay |
| AC-F3 | Failure handling | Injected: a synthesizer reply that changes the action category. S-2 fails, F-7 fires, and a template-only brief is issued | Offline replay with an edited copy (the original is kept) |
| AC-F4 | Failure handling | Injected: intake with sponsor and owner `Not stated` for a stage beyond preparation. F-9 fires | Rerun of Org Adoption only on the edited intake (one ChatGPT run) |
| AC-H1 | Human authority | No brief with any flag is issued as `Accepted by rule`. Every flagged brief carries a recorded disposition, with name, date and reason | Run record |
| AC-H2 | Human authority | No expert or synthesizer output selects a vendor, tool or model. If the intake asks for one, F-6 fires | G-6 + read |
| AC-H3 | Human authority | A `Modify` disposition keeps the expert reading beside the human one. No expert output or synthesizer text is edited | File hashes before and after the disposition |
| AC-G1 | Risk / governance | Each brief's TRADEOFFS or CONDITIONS name at least one risk or governance item, cited to an expert | Read |

**Observation, not pass/fail:** the number of flags fired per case. If every case fires a flag, record that "review when flagged" behaved as always-review (spec W-2).

## 3. Pass rule
- **The integrated version passes** when, on all three cases, every AC passes (AC-C1 on case A only) and AC-F1 to AC-F4 pass once each.
- **A failure** is preserved, logged as T-xx, and corrected only by a bounded, versioned change, followed by a retest (Lab 11 memo).

## 4. Criterion most likely to fail (Lab 10 prediction)
**AC-C1 / AC-E1 for the older agents on GPT-6.2 Sol.** Six agents were promoted on GPT-6.1 Sol or GPT-6, and the dry run is their first run on GPT-6.2 Sol. The prediction will be updated after the dry run.
