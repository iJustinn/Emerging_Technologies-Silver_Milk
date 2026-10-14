# Test Log: Team Innovation Classification Agent (Lab 4)

## Runtime (all 22 runs, 2026-10-13, 20:08–20:39 local)

- ChatGPT macOS app, **Work** mode, **GPT-6.1 Sol**, effort **Light** (the lowest stop on the effort slider), confirmed on screen before the first run. (D-14)
- Every run was a fresh chat started inside the ChatGPT project **MASY-1800**:
  - Project source: `1800-Textbook.pdf`.
  - No custom instructions.
  - Memory: "Open" (shared with chats outside the project; the app says this cannot be changed).
  - Space access: enabled.
- This differs from Lab 3 (D-08), and from Justin's Assignment 3 runs, which detached the project.
- Work mode also reads the operator's local `~/.codex/AGENTS.md`, which references `RTK.md` (shell-tooling notes, no lab content).
- Runs could search the web. The work logs show "Read files, searched the web" but do not itemize the retrievals.
- The packet was attached by paste, with one message: `[Run <ID>] Run the attached MASY1800 specialist agent prompt packet exactly as written. Return JSON only, in this chat reply; do not create files.`
- Claude Code operated the app through computer use for Justin Zhong. ChatGPT produced every response.
- Each `.raw_copy.txt` is the clipboard exactly as copied. Each `.json` is that text parsed and re-indented, with no repairs (0 `\&` escapes, 0 citation markers in all 22 runs).

## Cases

| File | Origin | Content |
|---|---|---|
| `cases/primary.json` | Nini Huang, Assignment 3 `contrast_1` | Bounded agentic AI for standard IT tickets at a hypothetical outsourced IT service company that charges mainly for staff time and service hours. Borderline: the revenue mechanism is stated; shares and contracts are not |
| `cases/contrast_1.json` | Nini Huang, Assignment 3 `primary` | The same technology, application, safeguards, posture, horizon, and source cards E1–E5, at an internal corporate IT department run as a cost center |
| `cases/contrast_2.json` | Yuanxiang Zhang, Assignment 3 `contrast_2` | Transfer test: LLM routine-reply drafting demo at the fictional PivotDesk; revenue mix unknown; supplied cards S1–S3 |

## Candidate comparison (T-11 to T-17)

See `common_test_package/lab04_candidate_comparison.md` (in the ZIP) and `records/lab04_candidate_comparison.md` (repo). Summary:

| Test | Li [L] | Zhong [Z] | Srivastava [K] | Huang [H] | Zhang [Y] |
|---|---|---|---|---|---|
| T-11 Validator | PASS ×2 | PASS ×2 | PASS ×2 | PASS ×2 | PASS ×2 |
| T-12 General stability | Stable | Stable (Breakthrough) | **Degree flips** | Stable | Stable |
| T-13 Level separation | Same | **Org class in application field** | Same | Same | **Status "unspecified"** |
| T-14 Swap (significance) | Withheld → Low | Moderate → Low | Moderate → Moderate | Withheld → Withheld | Withheld → Withheld |
| T-15 Source honesty | Honest "supplied" | "verified this run"; Markdown links | "Verified" (searched) | **Supplied cards typed "Verified"** | Attributed to the ledger |
| T-16 Lane | Experiment design (stop rule) | **"Pilot or partner"** | Clean | Clean | Clean |
| T-17 Words (total) | 1980 / 1536 | 1795 / 1697 | 2094 / 1978 | 1773 / 1737 | 1995 / 1938 |

All five see the same mechanism, and all reject Potentially Existential. The discriminators were stability, level separation, source honesty, and lane discipline.

## Team runs

| ID | Version | Run IDs | Result |
|---|---|---|---|
| T-18 | 0.9-team | T1 primary, T2 contrast_1, T3 transfer | All valid. Swap: Moderate (provisional, CORE a) → Low (provisional, SUPPORT). Application labels identical (Proposed; New to the organization only). Degree and lifecycle identical (Contested; HOLDS/UNTESTED/HOLDS). Transfer: Demonstration; Withheld (revenue absent). Lane clean; six HANDOFFs |
| **T-19** | 0.9-team | T1 vs. T2 | **Preserved failure: ENTREPRENEURSHIP Incumbent-led (T1) vs. Mixed (T2)** on the same technology and evidence. The v0.9 rule "choose the best-supported label" let the model pick arbitrarily. `check_innovation_lab04.py` fails it |
| T-20 | 1.0-team | R1, R2, R3 | W-1 fixed. Dated markers are now cited, but **ENTREPRENEURSHIP still differs: Mixed (R1, cites a retrieved 2021 Moveworks Series C marker) vs. Incumbent-led (R2, no such retrieval).** INNOVATION HOLDS in both. W-2: R3 withheld NOVELTY although the rule said "exactly one label" |
| T-21 | **1.1-team** | V1, V2, V3 | All valid. **100 mechanical checks pass** (`final_checks_v1_1.txt`); 2 FLAGs are generic words ("supplied", "practical-cost"). ENTREPRENEURSHIP Incumbent-led in both, from supplied E3. Degree, lifecycle, and application labels identical. Swap Moderate → Low (both provisional, with competing labels). Transfer: Demonstration; ENTREPRENEURSHIP Not established; SIGNIFICANCE Withheld |

## Human §4 review of v1.1

- **Swap test.** Passes. The hour-billed outsourcer is CORE (a) and Moderate, with High as the competing label. The cost center is SUPPORT and Low, with Moderate as the competing label. The strategic risk flips (failing to respond vs. adopting too early).
- **Rerun test (same technology).** Passes for lifecycle, entrepreneurship, and degree.
- **Level test.** Passes. The application finding is the same in both cases.
- **Borderline test.** The hour-billed case gives a provisional label with the competing label and the evidence that would move it.
- **Prerequisites as conditions.** Authorization, auditability, and escalation are carried as conditions.
- **Lane.** No adopt, pilot, partner, or experiment design. Six HANDOFF lines, including Promethean consuming DEGREE.
- **Transfer test.** Unchanged instructions on a different technology. The management claim "revolutionary" is not treated as evidence.
- **Evidence test.** The two most consequential claims trace to retrieved sources:
  - COMMERCIALIZATION HOLDS ← ServiceNow GA, 2025-03-12 (E-16).
  - DEGREE Contested ← ReAct benchmark gains, 2022-10-06 (E-14), with ITBench showing unresolved tasks (E-17).

## Checker notes

`check_innovation_lab04.py` was proven against the outputs it targets:
- degree flip: C05/C06
- organization class in the application field, lane, and Markdown links: C03/C04
- "verified" on supplied cards: C07/C08
- "unspecified" status: C09/C10
- entrepreneurship flip: T1/T2 v0.9

Four false positives were found and fixed during the lab. All are logged, and none changed a verdict on a team run:
- label extraction captured trailing text
- transfer runs were paired although they use a different technology
- "not … verified" negations
- a status line without line breaks

## Weaknesses

| ID | Weakness | Status |
|---|---|---|
| W-1 | v0.9 transfer used NOVELTY "Not new" for "the generation function isn't novel" (no definitions) | Fixed in v1.0 (D-17) |
| W-2 | v1.0 transfer withheld NOVELTY despite "exactly one label" | Addressed in v1.1 (`Withheld` allowed, D-18) |
| W-3 | v1.1 NOVELTY is "Withheld (most likely New to the organization only)" in all three runs, so it no longer discriminates | Open; accepted limitation |
| W-4 | `inference` evidence items carry `STATUS: supplied` | Open; minor |
| W-5 | A 24-month horizon falls on the near/mid boundary; the transfer chose mid-term | Open; minor |
| W-6 | General verdicts other than ENTREPRENEURSHIP depend on per-run retrieval (INNOVATION UNTESTED in v0.9/v1.1, HOLDS in v1.0) | Open → I-10 |
| W-7 | `STATUS: inspected-this-run` is self-reported by the run; the team verified the sources, not each run's retrieval | Open |
