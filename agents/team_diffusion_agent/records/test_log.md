# Test Log: Team Diffusion Agent (Lab 6)

## Runtime (all runs, 2026-10-27)

- **ChatGPT web** (chatgpt.com) in the Ego Lite browser on Justin Zhong's signed-in account (D-29, continuing D-20).
- **Work** mode; the composer read **"GPT-6.1 Sol Light"** before every launch (model set "Default", Power slider stop 1 of 0–5, the same setting as Lab 5); "More usage" (fast mode) off.
- Every run was a fresh chat started inside the ChatGPT project **MASY-1800** (every chat URL is under `/g/g-p-…-masy-1800/`). Project settings, re-checked on 2026-10-27 and left unchanged: instructions empty; Memory "Default"; Space access enabled; one source, `1800-Textbook.pdf`.
- The packet was attached as a file through the composer's file input, with one message: `[Run <ID>] Run the attached MASY1800 specialist agent prompt packet exactly as written. Return JSON only, in this chat reply; do not create files.`
- Work mode could search the web. The transfer runs (no cards) retrieved pages and marked them `STATUS: inspected-this-run`; the web UI does not itemize retrievals.
- Justin Zhong coordinated the runs, with Claude Code assisting through browser automation (ego-browser scripts). ChatGPT produced every response.
- Each `.raw_copy.txt` is the clipboard exactly as produced by the reply's own Copy button. Each `.json` is that text parsed and re-indented, with no repairs.
- **Handling incidents** (no effect on any saved output):
  - The first launch scripts stalled before sending; nothing was sent. `L6-Z-P` was then sent step by step.
  - Four launches were accepted by ChatGPT but never produced a reply (no "Worked for", no Stop control after several minutes): `L6-L-C`, `L6-T09-C2`, and `L6-T10-P` twice. Each was relaunched in a fresh chat with the same Run ID; the empty chats are kept and listed in `chat_links.md`. The fourth relaunch waited 10 s after the upload before sending and succeeded (W-4, I-16).
  - Attachment names carry "(1)"/"(2)" suffixes because the Files space already held files of the same name.
- **Run count:** 16 completed runs (10 candidate, 3 v0.9, 3 v1.0) and 4 empty launches, within the approved budget of 22.

## Cases

| File | Origin | Content |
|---|---|---|
| `cases/primary.json` | Nini Huang, Assignment 5 `primary` | GenAI incident summaries and resolution notes in internal enterprise IT service desks; hypothetical mid-to-large enterprise; **fast follower**; fixed packet E1–E8 and the pre-flagged claim W1 |
| `cases/contrast_1.json` | Nini Huang, Assignment 5 `contrast_1` | Identical except **conservative** posture and stricter governance text (posture test) |
| `cases/contrast_2.json` | Justin Zhong, Assignment 5 `primary` | **Transfer test:** AI coding agents at an illustrative U.S. regional bank (conservative); **no source cards** |

## Candidate comparison (T-31 to T-37)

Full table: `common_test_package/lab06_candidate_comparison.md` (ZIP) and `records/lab06_candidate_comparison.md` (repo).

| Test | [Z] Zhong | [L] Li | [H] Huang | [Y] Zhang | [K] Srivastava |
|---|---|---|---|---|---|
| T-31 Validator | PASS ×2 | PASS ×2 | PASS ×2 | PASS ×2 | PASS ×2 |
| T-32 General stage | **Late majority ×2** (E1 self-report) | Withheld ×2 | Withheld ×2 | Unclassified ×2 | no category ×2 |
| T-33 Slot stability | STANDARDS, MESSAGING SHIFT, CHANGE AGENTS drift | stable | stable | stable | stable |
| T-35 Posture swap | **Urgency ×2** (no change) | parallel → prerequisite | prerequisites change | small change | near-identical |
| T-37 Lane | clean | borderline | borderline | owner / thresholds / cadence | evaluate / expand |

## Team runs

| Run | Version | Case | File (`responses/`) |
|---|---|---|---|
| L6-T09-P / C1 / C2 | 0.9-team | primary / contrast_1 / contrast_2 | `team_v0_9__primary`, `team_v0_9__contrast_1`, `team_v0_9__contrast_2` |
| L6-T10-P / C1 / C2 | 1.0-team | primary / contrast_1 / contrast_2 | `team_v1_0__primary`, `team_v1_0__contrast_1`, `team_v1_0__contrast_2` |

### T-38: team v0.9 (preserved failure)

- All three valid; stages Withheld / Withheld / Withheld (ITSM) and Early adopters / Withheld / Withheld (transfer); STANDARDS and MESSAGING SHIFT now stable; timing Patience (fast follower), Continued monitoring (conservative), Continued monitoring (transfer).
- **Failure:** `check_diffusion_lab06.py --pair` FAIL: on identical cards, RELATIVE ADVANTAGE `Neutral · Speculative` vs. `Favors · Speculative`; TRIALABILITY and OBSERVABILITY `Favors · Observed` (E6 prototype; E3/E5 vendor documentation) vs. `Favors · Speculative`. `records/checks_v0_9.txt`.
- **Fix (team choice, D-32):** factor rule: Observed only from dated adopter evidence per factor; every Speculative factor is Neutral. Chosen over "tighten Observed only" and "accept as limitation".

### T-39: team v1.0 (final)

- All three valid. `records/final_checks_v1_0.txt`: **280 PASS, 0 FAIL**; FLAGs read by hand:
  - "case"/"context" in the general level come from `STAGE BASIS` wording and the `case-premise` type, not from case content.
  - "verified" appears only as "not verified organizational observations".
  - Transfer: Early adopters without a share → confirmed a dated base case (OpenAI, 2026-01-14).
- `--pair --posture-pair` (primary vs. contrast_1): identical Step 1 and Step 2 labels; TIMING Patience → Continued monitoring; POSTURE EFFECT differs.

## Human §4 review (v1.0)

| Check | Result |
|---|---|
| Swap test (posture only) | Evidence labels unchanged; timing and POSTURE EFFECT change. Pass |
| Stage rule | No stage above Early adopters; E1 treated as context; E8 refused as a base case because it is undated. Pass |
| Three-way read | Each level has its own basis. Pass |
| Factor rule | ITSM: all five Neutral · Speculative with the likely direction; transfer: four Observed from adopter evidence. Pass |
| Lane | Timing, watch-list and reassessment only; six HANDOFF lines. Pass |
| Transfer (unchanged instructions, no cards) | `EVIDENCE BASE: Retrieved this run`; Early adopters by dated base case; application and peer Withheld; Continued monitoring. Pass |
| Claims | E-29 to E-39 retrieved and matched on 2026-10-27, except E-35 (ServiceNow docs did not render; no label rests on them); E-31's date is from the URL path |

## Weaknesses (W-x)

- **W-1:** `USE LEVEL OBSERVED` for GenAI: Scaled ×2 (v0.9) vs. Piloted ×2 (v1.0) on identical cards; no fixed rule for the rung.
- **W-2:** transfer base case follows retrieval (Rakuten in v0.9, OpenAI's own use in v1.0).
- **W-3:** opt-in developer surveys are context under the stage rule, so a technology like coding agents cannot reach the early majority from Stack Overflow data (DS-08).
- **W-4:** four empty launches (I-16).
- **W-5:** both postures returned `PEER EVIDENCE ROLE: Prerequisite` (fast follower and conservative), so the slot did not separate this pair; the posture pair passed on TIMING and POSTURE EFFECT alone. A limitation, not a failure.
