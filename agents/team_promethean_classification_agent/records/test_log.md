# Test Log: Team Promethean Classification Agent (Lab 5)

## Runtime (all 23 runs, 2026-10-20)

- **ChatGPT web** (chatgpt.com) in the Ego Lite browser on Justin Zhong's signed-in account (D-20). This is a change from Labs 3–4, which used the ChatGPT macOS app through computer use; computer use was not available in the operating session, and Justin chose the web runtime for this and later labs.
- **Work** mode, model **GPT-6.1 Sol**, effort **Light**. On the web, the "Power" slider runs 0–5 across models: stop 0 is "GPT-6 Luna High", and stop 1 is "GPT-6.1 Sol Light". Light is the lowest GPT-6.1 Sol stop, the same setting as Labs 3–4. The model and effort were set once and confirmed on screen ("GPT-6.1 Sol Light" in the composer) before the first run; every launch also checked that the composer showed GPT-6.1 Sol.
- Every run was a fresh chat started inside the ChatGPT project **MASY-1800** (the composer read "New chat in MASY-1800", and every chat URL is under `/g/g-p-…-masy-1800/`). Project settings, re-checked on 2026-10-20 and left unchanged:
  - Instructions: empty.
  - Memory: "Default" ("This project can access memory from outside chats, and vice versa"). Lab 4 recorded this as "Open".
  - Space access: enabled.
  - The source list was not re-opened. Lab 4 recorded `1800-Textbook.pdf`, and two team runs cite "1800-Textbook.pdf, Chapter 11" (W-4).
- The packet was attached as a file through the composer's file input, with one message: `[Run <ID>] Run the attached MASY1800 specialist agent prompt packet exactly as written. Return JSON only, in this chat reply; do not create files.`
- Work mode could search the web. Runs that retrieved pages say so in `notes` (`STATUS: inspected-this-run`); the web UI does not itemize retrievals.
- Claude Code operated the browser for Justin Zhong (ego-browser scripts). ChatGPT produced every response.
- Each `.raw_copy.txt` is the clipboard exactly as produced by the reply's own Copy button. Each `.json` is that text parsed and re-indented, with no repairs (0 characters removed in all 23 runs).
- **Handling incidents** (no effect on any output): the first send of candidate run L5-L-P lost its attachment and nothing was sent, so it was relaunched by hand. The first launch of L5-T10-contrast_2 found no attachment and aborted before sending; it was relaunched. Chat links are listed in the ZIP only (see "Chat links" below).

## Cases

| File | Origin | Content |
|---|---|---|
| `cases/primary.json` | Dian Li, Assignment 4 `primary` | Text-to-image diffusion (latent diffusion as reference) for internal concept images and mood boards at a hypothetical small online homeware retailer; **aggressive** for reversible internal experiments; five supplied source cards S3, S5, S8, S11, S12 (checked by ChatGPT/Codex on 2026-10-18 per the case) |
| `cases/contrast_1.json` | Dian Li, Assignment 4 `posture_only` | Identical except the posture is **conservative** (the memo's posture test) |
| `cases/contrast_2.json` | Karuna Srivastava, Assignment 4 `primary` | **Transfer test:** generative AI foundation models for consultant research, synthesis and drafting at a hypothetical global consulting firm; moderate/fast-follower; **no source cards** |
| `cases/hype.json` | Dian Li, Assignment 4 `hype_pressure` | The primary plus an "UNVERIFIED MANAGEMENT CLAIM": investors call image AI "the next electricity" and ask for a Promethean label and immediate full deployment |

## Candidate comparison (T-22 to T-28)

All five candidates ran unchanged on primary, posture_only and hype (15 runs). Full table: `common_test_package/lab05_candidate_comparison.md` (ZIP) and `records/lab05_candidate_comparison.md` (repo).

| Test | [Z] Zhong | [L] Li | [H] Huang | [Y] Zhang | [K] Srivastava |
|---|---|---|---|---|---|
| T-22 Validator | PASS ×3 | PASS ×3 | PASS ×3 | PASS ×3 | PASS ×3 |
| T-23 General level | Breakthrough ×3 (slot drift on TIERS) | qualified breakthrough ×3 | **Withheld ×3**: requires the agentic-AI packet EP-A4-0.1 | **Incremental ×3** (B1 Unknown) | Breakthrough ×3 |
| T-24 Hype | held | held | held (0 evidence items) | held | held |
| T-25 Posture swap | organization level identical (weight Low ×3) | small change | withheld both | small change | clearest change |
| T-26 Source honesty | "independently opened" | "supplied source card" | case premises only | "consulted abstract, lines …" | "supplied source card" |
| T-27 Lane | clean (adoption → Adoption Agent) | designs the comparison | defers and sets expansion conditions | continue/hold rules | "proceed with a bounded internal evaluation" |
| T-28 Words (general) | 177–195 | 231–237 | 255–343 | 392–454 (over 350) | 113–134 |

## Team runs

| Run | Version | Case | Validator | Class · dissolution · earliest gate | Confidence (at least / not higher) | Core · window · weight | Result |
|---|---|---|---|---|---|---|---|
| L5-T09-primary | 0.9 | primary | PASS | **Breakthrough** · Reduced · Suppression | Moderate / Moderate | No · None · Low | Mechanical checks pass |
| L5-T09-contrast_1 | 0.9 | posture | PASS | Breakthrough · Reduced · Suppression | Moderate / Moderate | No · None · Low | Posture pair passes (same labels and weight, different POSTURE EFFECT) |
| L5-T09-contrast_2 | 0.9 | transfer | PASS | Breakthrough · Reduced · Suppression | Moderate / Moderate | Yes · None · **Moderate** | W-1: handoffs omit Creation and Diffusion |
| L5-T09-hype | 0.9 | hype | PASS | **Incremental** · Reduced · **Barrier** | Moderate / Moderate | No · None · Low | **T-29 preserved failure** (below) |
| L5-T10-primary | 1.0 | primary | PASS | **Indeterminate (Incremental \| Breakthrough)** · Reduced · Suppression; reassess 2027-04-20 | Moderate / Moderate | No · None · Low | All checks pass |
| L5-T10-contrast_1 | 1.0 | posture | PASS | same | Moderate / Moderate | No · None · Low | Posture pair passes |
| L5-T10-contrast_2 | 1.0 | transfer | PASS | **Breakthrough** · Reduced · Suppression | Moderate / Moderate | Yes · None · Moderate | All checks pass; six handoffs |
| L5-T10-hype | 1.0 | hype | PASS | Indeterminate (Incremental \| Breakthrough) · Reduced · Suppression; reassess 2027-04-20 | Moderate / Moderate | No · None · Low | Same Step 1 labels as primary; hype rejected |

Mechanical checks: `records/checks_v0_9.txt` (3 FAIL: the T-29 pair ×2 and W-1) and `records/final_checks_v1_0.txt` (293 PASS, 0 FAIL, 2 FLAG; both FLAGs are the case's own phrase "separately authored and checked"). The checks themselves were shown to fail on the outputs they target (`common_test_package/check_proof_on_candidates.txt`).

## T-29 Preserved failure (v0.9): the class flipped on identical cards

- **What happened.** Primary and posture runs: `SIGNIFICANCE CLASS: Breakthrough`, with `WHY NOT LOWER` resting on S3's comparison of latent diffusion against **pixel-space diffusion**. Hype run, same five cards: `BARRIER STATEMENT … This candidate statement is not convincing from the cards: they do not establish the historical constraint or exclude earlier generative alternatives` → `EARLIEST UNRESOLVED GATE: Barrier` → `SIGNIFICANCE CLASS: Incremental`.
- **Why.** v0.9 never said what the baseline is, or what follows when a barrier is real but its reduction is unmeasured. One run read an intra-family comparison (one diffusion architecture against another) as a substantial reduction. The other treated a barrier qualified by earlier alternatives as unconvincing. This is the same Breakthrough-vs-Incremental split as the candidates ([Z][L][K] vs. [Y]), now inside one agent.
- **Not hype.** The hype claim did not raise anything. If anything, the hype run was more skeptical, so the failure is about baseline ambiguity, not hype susceptibility.
- **Fix (D-25, chosen by the team).**
  - The baseline is the **pre-technology workflow**. Intra-family comparisons never decide the class.
  - Earlier alternatives qualify a barrier; they never make it unconvincing.
  - Breakthrough needs a dated item that **measures** the reduction against that workflow.
  - When the reduction is real but unmeasured, the class is `Indeterminate (Incremental | Breakthrough)`, with the deciding evidence and a reassessment date ≤ 12 months, weighted as Incremental.
  - Also W-1: one HANDOFF line for each of the six agents.
- **Retest (T-30).**
  - All three same-card runs: `Indeterminate (Incremental | Breakthrough)`, identical Step 1 labels and confidence lines, deciding evidence "a dated measurement against the pre-technology workflow", and reassessment 2027-04-20.
  - The transfer stays `Breakthrough`: it cites a measured comparison against working without AI (HBS "Navigating the Jagged Technological Frontier", 758 BCG consultants).

## Human §4 review (v1.0)

- **Swap test (posture).**
  - Class, weight (Low) and application significance (Incremental) are identical between aggressive and conservative, as intended.
  - `POSTURE EFFECT` differs. Aggressive: "greater tolerance of uncertainty … proportionate review rather than high-confidence reliance". Conservative: "less tolerance for unresolved reliability and attribution … more demanding review".
- **Swap test (organization).** The retailer (core No) gets weight **Low**. The consulting firm (core Yes: "producing adaptable analysis and explanatory content is central to its paid work") gets **Moderate**.
- **Hype.** The class and weight match the primary exactly. The recommendation says "neither investor enthusiasm nor a civilization-scale analogy changes that result". The management claim is typed `case-premise` and excluded from scoring.
- **Prerequisites as conditions.** The irreversibility guard is present in the transfer ("cannot justify any irreversible commitments").
- **Lane.** No adopt, pilot, proceed, or evaluation design in any recommendation. Every run hands adoption to the Adoption Agent.
- **Level separation.** No case words in any `general_et_finding` (check_common leak test passes).

## Weaknesses (open)

- **W-1 (fixed in v1.0).** v0.9 transfer handoffs omitted Creation and Diffusion.
- **W-2.** Evidence typing still drifts: the transfer types `1800-Textbook.pdf` as `primary-technical`, and `inference` items carry `STATUS: supplied` (hype) or `STATUS: inspected-this-run` (transfer). No label depends on this.
- **W-3.** The transfer has no supplied cards, so its evidence base is per-run retrieval.
  - v0.9 cited Noy & Zhang (2023) and Dell'Acqua et al. (dated 2026-03-11 in that run).
  - v1.0 cited the GPT-4 Technical Report and the HBS "Jagged Frontier" page (2023-09-21).
  - The label held (Breakthrough), but its support differs run to run. This extends I-10.
- **W-4.** Runs can read the MASY-1800 project's `1800-Textbook.pdf`. The transfer v1.0 cites it, and candidate [H] said it checked Chapter 11 locators "in the supplied textbook". The project source is part of the runtime and is not in the packet.
- **W-5.** `Indeterminate (Incremental | Breakthrough)` is weighted as Incremental, so for the retailer the weight is Low whichever way the class resolves. The fix made the general level honest without changing any organization-level result.
- **W-6.** One run per case and version. Stability rests on three same-card runs with different organization fields, not on reruns of identical input.

## Chat links

The chat links for every run are in `records/chat_links.md` and `common_test_package/runmap.txt`, in the ZIP only. They are not published in the public repo because the URLs expose the ChatGPT project id.
