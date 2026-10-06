# Test Log: Silver-Milk Team Creation Agent (Team Lab 3, 2026-10-06)

## Runtime (the same for every run in this lab)

- The ChatGPT macOS app in **Work** mode, model **GPT-6.1 Sol**, thinking effort **Light** (the app's lowest setting; the team asked for "low").
- No project attached. Each run used a fresh conversation, and the app's own web retrieval was active.
- Claude Code drove the app by computer use for Justin (technical operator). Each packet was pasted as an attachment with one fixed message: *"[Run ID] Run the attached MASY1800 specialist agent prompt packet exactly as written. Return JSON only, in this chat reply; do not create files."*
- The responses were copied with ChatGPT's copy button. `common_test_package/save_resp.py` saved the clipboard exactly (`*.raw_copy.txt`) and a `.json` copy. No run needed any cleanup (`removed_by_cleanup=0`), so each `.json` is the raw text re-indented.
- **Difference from earlier runs:** the candidates' Assignment 2 runs used other settings (Justin: Chat mode, High; others: not recorded). The common condition here is fair across the candidates, but these runs are not directly comparable with the Assignment 2 results.

## Common test package

| File | Role | Source |
|---|---|---|
| `common_test_package/cases/primary_bank.json` | Primary: AI coding agents, conservative regional bank, 24 months | Justin's Assignment 2 case (chosen because its consequential claims were already verified, V1–V6) |
| `common_test_package/cases/contrast_startup.json` | Context contrast: same technology and question; seed-stage startup, aggressive posture, 12 months | Justin's Assignment 2 case |
| `common_test_package/cases/transfer_diffusion_retailer.json` | Transfer test: a different technology (text-to-image diffusion) with Dian's supplied source cards | Dian's Assignment 2 primary case (chosen to offset the use of Justin's case as the common pair) |

## T-07: All four candidates on the common case (instructions unchanged)

| Run | Validator | General words | Stage label | General level stable bank ↔ startup? | Case leak in general level | Source labelling | Lane |
|---|---|---|---|---|---|---|---|
| Z (Zhong 0.2) | PASS / PASS | 555 / 590 | Emerging→Developing / Emerging→Developing | **Yes:** same label, defining layer, A1–A3 verdicts (HOLDS / DOES NOT HOLD / UNTESTED); predecessors overlap (Transformer, Codex, ReAct) | None | Typed enum; honest partial-retrieval notes | 3–5 HANDOFF lines; no adopt or pilot |
| H (Huang 0.1) | PASS / PASS | 224 / 211 | None (free-text "commercial offerings with continued experimentation") | Substantively yes (same feedback-loop recombination and position), but unlabeled; named predecessors vary (Transformer and SWE-agent only in the bank run); no dated economic enabler | None | Markdown links; "retrieved" claims | Explicitly does not authorize a pilot |
| L (Li 0.3) | PASS / PASS | 232 / 243 | None (dated arc, no label) | Mostly (Transformer, ReAct, SWE-agent in both) | None | Five of six items per run say "checked" or "verified in this run"; all are typed "Original-source"; Markdown links | Stays in lane |
| Y (Zhang 0.3) | PASS / PASS | 340 / 335 | None ("beyond concept and prototype") | Mostly (Transformer, ReAct, SWE-agent in both) | **Yes:** the bank-run general level says "a bank-specific maintenance application" and "not bank maintenance" | Best: separates "abstract inspected" from "full paper not inspected" | **Out of lane:** the startup run designs a two-week sandbox experiment with named owners; the bank run outputs "The referenced official assignment DOCX was not supplied" |

**Swap test (organization finding):** all four candidates pass. The bank finding centres on a 6–12-month approval cycle inside a 24-month horizon and on anchoring to change management. The startup finding centres on churn being absorbable over the runway and on protecting financial data.

**Convergence finding:** all four reached nearly the same recommendation ("assume the pattern persists, expect vendor and harness churn, keep repository assets portable"). The common case drove the recommendation, as in Lab 2 T-03. The candidates were distinguished by **general-level stability and comparability** and by **evidence discipline**, not by recommendation quality.

## T-08: Team v0.9 on the primary and contrast cases (**preserved failure**)

| Run | Validator | Words | Stage | A1 / A2 / A3 | Predecessors | §4 checks |
|---|---|---|---|---|---|---|
| primary v0.9 | PASS | 314 | Emerging→Developing | HOLDS / **DOES NOT HOLD** / UNTESTED | UNIX files (1974), UNIX shell (1974), Codex, ReAct, SWE-agent | All other checks pass |
| contrast v0.9 | PASS | 305 | Emerging→Developing | HOLDS / **HOLDS** / UNTESTED | Transformer, Codex, ReAct, SWE-agent, HumanEval | All other checks pass |

**Failure:** the model wrote the A2 statement itself. In the bank run A2 said the architecture "has already settled" (→ DOES NOT HOLD). In the startup run it said it "does not yet establish a de facto standard" (→ HOLDS). The judgment was the same but the polarity was opposite, so the verdicts contradicted each other. The startup run's A2 = HOLDS also sits next to a stage label that says the architecture has not converged. Only 3 of 5 predecessors were shared. This is the same failure Justin's v0.1 showed, in a new form: an orchestrator would receive contradictory "general" facts.

## T-09: Team v0.9 transfer test (text-to-image diffusion, instructions unchanged)

Validator PASS; 312 words; stage Emerging→Developing; A2 again phrased in the negative ("has not yet converged" → HOLDS), confirming the T-08 cause. **Supplied source cards were labeled `STATUS: supplied` (9 items)**, which fixes the attribution failure in Dian's Assignment 2. All six HANDOFF lines are present and the run stays in lane.

## Revision v0.9 → v1.0-team (cause → change)

- A1–A3 now have **fixed affirmative statements**. A2 is always "The defining layer has converged on a de facto architecture across major providers."
- Added the **A2 ↔ stage consistency rule**.
- **Predecessors are traced** from each defining-layer component to its canonical original record, oldest first.
- R-4 was updated. `check_team_run.py` gained two checks (A2 fixed wording; A2 consistent with the stage). Applied to the v0.9 outputs, they FAIL on 2 of 3 runs, so they detect the failure.

## T-10: Team v1.0-team on primary, contrast, and transfer

| Run | Validator | Words | Stage | A1 / A2 / A3 | A2 wording + consistency | Predecessors | STATUS (inspected / supplied / unverified) | HANDOFF lines |
|---|---|---|---|---|---|---|---|---|
| primary v1.0 | PASS | 301 | Emerging→Developing | HOLDS / UNTESTED / UNTESTED | PASS / PASS | Unix (1971), Transformer, GPT (2018), Codex, ReAct | 11 / 1 / 0 | 6 |
| contrast v1.0 | PASS | 284 | Emerging→Developing | HOLDS / UNTESTED / UNTESTED | PASS / PASS | UNIX (1974), Transformer, GPT (2018), Codex, ReAct | 11 / 1 / 1 | 6 |
| transfer v1.0 | PASS | 306 | Emerging→Developing | HOLDS / UNTESTED / UNTESTED | PASS / PASS | VAE 2013, attention 2014, diffusion 2015, U-Net 2015, Transformer 2017, … (7) | 12 / 4 / 0 | 6 |

All other `check_team_run.py` checks pass on all three runs: five labels, ≤350 words, no organization or industry words in the general level, evidence types, STATUS prefixes, no Markdown links, no adopt/pilot/experiment design, no empty arrays.

**Human §4 review (Claude Code drafted; the team confirms):**
- **Rerun stability:** same stage label, same defining layer (worded differently), same A1–A3 verdicts, and the **same five predecessors** for bank and startup (v0.9: 3 of 5 shared).
- **Swap test:** the bank finding is about the approval cycle consuming the 24-month horizon and an "established supplier name does not resolve architectural uncertainty". The startup finding is that its "binding constraint is scarce runway and engineering attention" and churn is absorbable. Each would be wrong for the other organization. **Pass.**
- **Prerequisites as conditions:** transfer: "Owner approval must precede acceptance of concepts; separate authorship and checking must precede any customer-facing campaign use." **Pass** (Dian's Assignment 2 failure is fixed).
- **Lane:** every run defers adopt/experiment to the Adoption Agent. The startup run's abstention explicitly declines "experiment design". **Pass.**
- **Evidence test:** every stage marker and economic enabler cited by the team runs was checked (`records/evidence_register.md` E-01 to E-13). v1.0 primary: E-04, E-02, E-11. v1.0 contrast: E-12 (month only; the day "05-22" is not confirmed) and E-13. v1.0 transfer: Rombach (supplied card), E-09, E-10, E-07. No v1.0 output uses "verified" or "checked" wording.

## Remaining weaknesses (preserved, not fixed)

- **W-1 Economic enabler and cited markers vary across runs.** The primary v1.0 cites GitHub's February 2025 product distribution; the contrast v1.0 cites Anthropic's 2026-02-12 revenue report. Both are flagged as weak evidence of sustainable economics, but they are different evidence for the same general claim.
- **W-2 Same predecessor, different date.** Unix is dated 1971 (first manual) in one run and 1974 (the CACM paper) in the other.
- **W-3 One run per case per version.** Stability rests on two v1.0 runs on one technology; it is not a reliability rate.
- **W-4 The stage label for text-to-image diffusion (Emerging→Developing in 2026) is open to challenge.** See dissent DS-01.
- **W-5 Runtime.** Light effort with web retrieval. Results at High effort, or without retrieval, are untested.

The contrast v1.0 output itself stated that "a frozen technology-level baseline is needed to assess exact rerun consistency". This supports integration issue I-05.
