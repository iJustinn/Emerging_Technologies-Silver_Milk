# Lab 6 candidate comparison (Diffusion), T-31 to T-37

## Common cases (D-28)

| File | Origin | Content |
|---|---|---|
| `cases/primary.json` | Nini Huang, Assignment 5 `primary` | GenAI-assisted incident summaries and resolution notes in internal enterprise IT service desks; hypothetical mid-to-large enterprise; **moderate / fast follower**; fixed evidence packet E1–E8 (URL-level, retrieved 2026-10-22 per the case) and the pre-flagged unsupported claim W1; six-month horizon |
| `cases/contrast_1.json` | Nini Huang, Assignment 5 `contrast_1` | Identical except **conservative / risk-averse** posture and stricter governance text (posture-only contrast: the memo's 23–37 min test) |
| `cases/transfer.json` | Justin Zhong, Assignment 5 `primary` | **Transfer test for the team agent only:** AI coding agents at an illustrative U.S. regional bank, conservative adopter; no source cards |

Caveat (home field): [H]'s instructions name ITSM, E1–E8 and W1, so [H] runs on its own case. [Y]'s instructions assume a bank. [L]'s assume a supplied packet. [Z] and [K] are generic.

## Runtime

ChatGPT web in Ego Lite, Work mode, composer label "GPT-6.1 Sol Light" (model set "Default", Power slider stop 1 of 0–5, as in Lab 5), fast mode off, a fresh chat per run inside the ChatGPT project MASY-1800 (instructions empty; Memory "Default"; Space access enabled; source `1800-Textbook.pdf`; re-checked 2026-10-27, unchanged). Packet attached as a file; message `[Run <ID>] Run the attached MASY1800 specialist agent prompt packet exactly as written. Return JSON only, in this chat reply; do not create files.` Justin Zhong coordinated the runs, with Claude Code assisting through browser automation (ego-browser scripts). ChatGPT produced every response. Responses copied with each reply's own Copy button and saved with `save_resp.py`; no repairs.

Handling incidents (no effect on any saved output): the first launch scripts stalled before sending, so nothing was sent; `L6-Z-P` was then sent step by step. The first `L6-L-C` chat produced no reply at all and was relaunched in a fresh chat; the empty chat is kept and listed in `runmap.txt` (ZIP only). Attachment names carry "(1)"/"(2)" suffixes because the Files space already held files of the same name (Lab 5 used the same packet names).

**Paths:** in the ZIP, the runs are in `common_test_package/responses/` and the cases in `common_test_package/cases/`. In the repo, the runs are in `records/evidence/lab06_candidate_runs/`; the cases are in the ZIP only, and the team agent's copies are in `agents/team_diffusion_agent/cases/` (`contrast_2` = the transfer).

| Run | Candidate | Case | File (`responses/`) |
|---|---|---|---|
| L6-Z-P / L6-Z-C | [Z] Zhong 0.2-student | primary / contrast_1 | `candidate_zhong__primary`, `candidate_zhong__contrast_1` |
| L6-L-P / L6-L-C | [L] Li 0.2 | primary / contrast_1 | `candidate_li__primary`, `candidate_li__contrast_1` |
| L6-H-P / L6-H-C | [H] Huang 0.2-student | primary / contrast_1 | `candidate_huang__primary`, `candidate_huang__contrast_1` |
| L6-Y-P / L6-Y-C | [Y] Zhang 0.1-student (metadata; record says revision 02) | primary / contrast_1 | `candidate_zhang__primary`, `candidate_zhang__contrast_1` |
| L6-K-P / L6-K-C | [K] Srivastava 0.1-student | primary / contrast_1 | `candidate_srivastava__primary`, `candidate_srivastava__contrast_1` |

## Results

| Test | [Z] Zhong | [L] Li | [H] Huang | [Y] Zhang | [K] Srivastava |
|---|---|---|---|---|---|
| T-31 Validator | PASS ×2 | PASS ×2 | PASS ×2 | PASS ×2 | PASS ×2 |
| T-32 General stage (same cards) | **Late majority ×2**, from E1's 71% respondent self-report (share rule >50%). Its own text: "not representative global penetration" | Withheld ×2 ("exact stage is withheld") | Withheld ×2 (no category assigned) | Unclassified ×2 | "substantial but uneven", no category ×2 |
| T-33 General-slot stability | **Drift on identical cards:** STANDARDS Contested → None; MESSAGING SHIFT Observed → Not observed; CHANGE AGENTS McKinsey/NIST → ServiceNow | stable | stable | stable | stable |
| T-34 Application stage | Insufficient evidence ×2 (E8 undated, so BASE CASE None) | Withheld ×2; adoption defined as repeated use | Withheld; E8 = strongest direct signal | Unclassified ×2 | "early-adopter deployment", provisional, low confidence ×2 |
| T-35 Posture swap (timing) | **Urgency ×2**: the table fallback to TECHNOLOGY STAGE (Late majority) gives Urgency for both postures; the swap changes nothing | Changes: peer evidence **parallel** (fast follower) vs. **prerequisite to a proposal** (conservative) | Changes prerequisites: bounded learning vs. data-flow review, reviewer ownership and comparable evidence first | Small change: monthly reviews ×2; fortnightly learning reviews added only for fast follower | Near-identical (evaluate, then expand); contrast adds "stricter comparable-deployment evidence" |
| T-36 Source honesty | Typed evidence; packet dates kept | "supplied source-card summary" | packet dates kept; "retrieval" = packet's date | per-claim verified/unverified; "not accessed in this run" | "supplied packet summary" |
| T-37 Lane (adoption reserved) | Timing only (clean) but the timing value is rule-inflated | "first permissible step" and evidence dossier (borderline) | "Next step: prepare a bounded evaluation proposal" (borderline) | Names evaluation owner, thresholds, review cadence (Adoption / Org Readiness lane) | "run a bounded evaluation … expand only if …" (Adoption lane) |
| Words g / a / o / rec (P) | 245 / 115 / 182 / 67 | 119 / 234 / 173 / 281 | 99 / 220 / 204 / 173 | 150 / 203 / 178 / 118 | 69 / 154 / 127 / 86 |

All ten cover the five Rogers characteristics. All five reject W1 (no candidate says the application is in the early majority).

## Reading

- The recommendations converge on "gather comparable evidence; nothing is decided here". The discriminators are the general-level label rule (T-32/T-33), the timing mechanism (T-35) and lane (T-37).
- [Z]'s structure (fixed labels, the APPLICATION STAGE × POSTURE timing table with Fortino's Urgency / Patience / Continued monitoring) is the only one that states a timing value the Adoption Agent can read. But two of its rules failed on this case: the share rule accepted a respondent self-report as a population share, and the fallback to TECHNOLOGY STAGE turned that inflated label into Urgency for a conservative adopter. This is the same flaw Justin recorded in his Assignment 5 record (Late majority from a vendor survey).
- [L], [H], [Y] withhold labels honestly but give no fixed slot a downstream agent can parse. [L] and [H] show the clearest posture effect without moving the evidence.
