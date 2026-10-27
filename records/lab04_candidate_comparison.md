# Lab 4 candidate comparison (T-11 to T-17)

Five Assignment 3 "Innovation and Disruption" candidates, all present, each run unchanged on the same two saved cases.

## Common cases (team decision, 2026-10-13)

- **Primary (borderline):** Nini Huang's `contrast_1`, a hypothetical outsourced IT service company that charges mainly for staff time and service hours. Saved as `cases/common_primary_hourbilled.json`.
- **Context contrast:** Nini Huang's `primary`, a hypothetical internal corporate IT department run as a cost center. Saved as `cases/common_contrast_costcenter.json`.
- The technology, application, safeguards, posture, horizon, and five source cards (E1–E5, accessed 2026-10-10) are identical in both cases. Only the organization and its revenue logic change.
- **Transfer test for the team agent:** Yuanxiang Zhang's `contrast_2`, the PivotDesk demo-only case. Saved as `cases/transfer_pivotdesk_demo.json`.
- Using a member's own cases favors that member. Nini's instructions were tuned on this pair, and her instructions mention "the supplied scenarios". For the other four candidates, this pair is a transfer test.

## Runtime (all 10 runs, 2026-10-13)

- ChatGPT macOS app, **Work** mode, **GPT-6.1 Sol**, effort **Light** (the lowest stop on the slider).
- Every run is a fresh chat started inside the ChatGPT project **MASY-1800**:
  - Project source: `1800-Textbook.pdf`.
  - No custom instructions.
  - Memory: "Open" (shared with chats outside the project; the app says this cannot be changed).
  - Space access: enabled.
- Work mode also reads the operator's local `~/.codex/AGENTS.md`, which references `RTK.md` (shell-tooling notes, no lab content). This was seen in the C10 work log.
- C03's work log shows "Read files, searched the web". Runs could browse, but the log does not itemize which sources were retrieved.
- The packet was attached by paste, with one message: `[Run Cxx] Run the attached MASY1800 specialist agent prompt packet exactly as written. Return JSON only, in this chat reply; do not create files.`
- Justin Zhong coordinated the runs, with Claude Code assisting through computer-use automation. ChatGPT produced every response.
- Responses were saved with `save_resp.py`. All 10 passed `validate_response.py`. No repairs were needed: there were 0 `\&` escapes and 0 citation markers.

| Run | Candidate | Case | File |
|---|---|---|---|
| C01 | Li [L] v0.2 | hour-billed | `records/evidence/lab04_candidate_runs/C01_candidate_li__common_primary_hourbilled.json` |
| C02 | Li [L] | cost center | `records/evidence/lab04_candidate_runs/C02_candidate_li__common_contrast_costcenter.json` |
| C03 | Zhong [Z] v0.2-student | hour-billed | `records/evidence/lab04_candidate_runs/C03_candidate_zhong__common_primary_hourbilled.json` |
| C04 | Zhong [Z] | cost center | `records/evidence/lab04_candidate_runs/C04_candidate_zhong__common_contrast_costcenter.json` |
| C05 | Srivastava [K] v0.2-student | hour-billed | `records/evidence/lab04_candidate_runs/C05_candidate_srivastava__common_primary_hourbilled.json` |
| C06 | Srivastava [K] | cost center | `records/evidence/lab04_candidate_runs/C06_candidate_srivastava__common_contrast_costcenter.json` |
| C07 | Huang [H] v0.2-student | hour-billed | `records/evidence/lab04_candidate_runs/C07_candidate_huang__common_primary_hourbilled.json` |
| C08 | Huang [H] | cost center | `records/evidence/lab04_candidate_runs/C08_candidate_huang__common_contrast_costcenter.json` |
| C09 | Zhang [Y] v1.2-student | hour-billed | `records/evidence/lab04_candidate_runs/C09_candidate_zhang__common_primary_hourbilled.json` |
| C10 | Zhang [Y] | cost center | `records/evidence/lab04_candidate_runs/C10_candidate_zhang__common_contrast_costcenter.json` |

## Comparison

| Test | [L] Li | [Z] Zhong | [K] Srivastava | [H] Huang | [Y] Zhang |
|---|---|---|---|---|---|
| **T-11 Validator** | PASS ×2 | PASS ×2 | PASS ×2 | PASS ×2 | PASS ×2 |
| **T-12 General-level stability** (same technology, same evidence) | Stable: commercial offering; incremental/recombinative, breakthrough unsupported | Stable: Commercialization · **Breakthrough** · depends on business model | **FAIL: Degree flips** Breakthrough (C05) → Incremental (C06) on identical evidence; the 10x tie-break decided the label | Stable: statuses separately evidenced; degree "mixed and baseline-dependent" | Stable: "breakthrough candidate", incremental still credible |
| **T-13 Level separation** (the application is identical in both cases, so the application finding should match) | Same: candidate process innovation, incremental/recombinative | **Differs:** APPLICATION CLASS Breakthrough → Incremental, organizational novelty High → Moderate. Organization judgments sit in the application field | Same: Adaptive application; New to the organization only | Same: proposed process innovation | Same, but both runs **withhold lifecycle status as "unspecified"** (the case describes an intended application, which means proposed) |
| **T-14 Swap test** (organization finding) | Withheld (conditional L/M/H) → **Low** (provisional) | **Moderate** · near-term → **Low** · Disruptive → Sustaining | CORE → SUPPORT, but **Moderate → Moderate**: its rule "cost structure Altered → Moderate" fires for both | Withheld → Withheld; the mechanisms change (billable hours vs. funding) | Withheld → Withheld; the mechanisms change |
| **T-15 Source honesty** | Says "supplied source card" (honest) | "verified during this run" on each source (log shows web search; not itemized); **Markdown links** in sources; adds E6 (Infosys annual report) | "Verified during this assessment" (web search; new Moveworks/ServiceNow sources) | **Types supplied cards "Verified original…"**: copies the case's "VERIFIED" heading; not retrieved by the run | "summarized in the supplied verified source ledger" (attributes the check to the ledger) |
| **T-16 Lane discipline** | Designs a six-week investigation with a stop rule (experiment design belongs to Adoption, I-06) | **RESPONSE: Pilot or partner** (adoption wording from the matrix); otherwise hands off | Clean: "Do NOT recommend adopting" rule held | Clean | Clean |
| **T-17 Length** (total words) | 1980 / 1536 | 1795 / 1697 | 2094 / 1978 | 1773 / 1737 | 1995 / 1938 |

### Reading

- **Convergence.** All five see the same mechanism: hourly billing exposes value capture, while the cost center only changes cost and capacity. All five reject Potentially Existential. The recommendations converge, so the discriminators are general-level stability, level separation, source honesty, and lane discipline.
- **Forced label vs. evidence threshold.** [Z] holds a stable Breakthrough label but rests it on analytical inference (I1). [L], [H], and [Y] each say the supplied evidence does not support Breakthrough. [K]'s forced label flips. This is the main classification dissent.
- **Borderline case.** On the hour-billed outsourcer, [Z] and [K] give Moderate (provisional). [L], [H], and [Y] withhold, giving conditional Low/Moderate/High. In Assignment 3, Nini's supplementary case (with explicit 60% revenue exposure) gave conditional High.
- **Context sensitivity of the label.** Only [L] and [Z] change the disruption label between the two organizations. [H] and [Y] change the mechanisms but keep "withheld" for both. [K] keeps Moderate for both.
- **Hard-coding.** [L]'s instructions name its own cases and source IDs ("For the national retailer…", "Do not apply S11"). [H]'s mention "the supplied scenarios". Both still ran sensibly on this pair, but such rules fail standard §3.6 for a team agent.
- **Naming collision.** [Z] uses `ARC STAGE` with Invention/Innovation/Commercialization. The team Creation agent already uses `ARC STAGE` with Emerging/Developing/Mature. Two different meanings under one label would confuse the orchestrator.
