# Lab 5 candidate comparison (T-22 to T-28)

Five Assignment 4 "Promethean Technology Classification" candidates, all present, each run unchanged on the same three saved cases.

**File naming:** Karuna Srivastava's candidate was submitted as `team-individual-agents/MASY1800_ET_Agent_Scaffold_v1_0.zip`, which looks like a pristine scaffold. Its `records/agent_record.md` names Karuna, and its git log shows an Assignment 4 branch. The file was not renamed. The pristine scaffold for this lab came from Dian Li's `original/MASY1800_ET_Agent_Scaffold_v1_0.zip` (`FROZEN CORE INTACT`).

## Common cases (team decision, 2026-10-20)

- **Primary:** Dian Li's `primary`. A hypothetical small online homeware retailer, aggressive for reversible internal experiments, wants internal concept images and mood boards. Saved as `cases/primary.json`.
- **Context contrast (posture only):** Dian Li's `posture_only`. Identical except that the adoption posture is conservative. This isolates the memo's test: "Inspect whether broad classification remains stable across organizational posture while management implication changes appropriately." Saved as `cases/posture_only.json`.
- **Hype test:** Dian Li's `hype_pressure`. The primary, plus an "UNVERIFIED MANAGEMENT CLAIM" that investors call image AI "the next electricity" and ask for a Promethean label and immediate full deployment. Saved as `cases/hype_pressure.json`.
- All three carry the same five source cards (S3, S5, S8, S11, S12). Per the case text, the cards were checked by ChatGPT/Codex on 2026-10-18, not by Dian personally.
- **Transfer test for the team agent:** Karuna Srivastava's `primary` (generative AI foundation models at a global consulting firm). Saved as `cases/transfer_karuna_consulting.json`.
- Using a member's own cases favors that member. Dian's instructions mention "a narrower image-generation system", so these cases were partly a home ground for [L]. For the other four, they are a transfer.

## Runtime (all 15 runs, 2026-10-20)

- **ChatGPT web** (chatgpt.com) in the Ego Lite browser on Justin's signed-in account. The team asked for this runtime (Justin, 2026-10-20) after computer use was not available in the operating session. Labs 3–4 used the ChatGPT macOS app.
- **Work** mode, model **GPT-6.1 Sol**, effort **Light**. On the web, the "Power" slider runs 0–5 across models: stop 0 is "GPT-6 Luna High", and stop 1 is "GPT-6.1 Sol Light". Light is therefore the lowest GPT-6.1 Sol stop, the same setting as Labs 3–4.
- Every run is a fresh chat started inside the ChatGPT project **MASY-1800**. Project settings, re-checked on 2026-10-20: no custom instructions; Memory "Default" ("This project can access memory from outside chats, and vice versa"); Space access enabled. The project's source list was not re-opened this lab (Lab 4 recorded `1800-Textbook.pdf`). [H]'s primary run says it checked Chapter 11 locators "in the supplied textbook", so the project source was visible to at least that run.
- The packet was attached as a file through the composer's file input, with one message: `[Run L5-x-y] Run the attached MASY1800 specialist agent prompt packet exactly as written. Return JSON only, in this chat reply; do not create files.`
- Work mode on the web shows the user's connected Gmail/Drive suggestions on the home screen. No run cited them.
- Responses were copied with each reply's own Copy button and saved with `save_resp.py`. All 15 passed `validate_response.py`. No repairs were needed (0 characters removed by cleanup).
- **Handling incident:** the first send of L5-L-P lost its attachment before sending, and nothing was sent. The draft was cleared, the file attached again, and the run sent by hand. Because the Files space already held the first upload, the attachment was named `candidate_li__primary(1).txt`.
- Claude Code operated the browser for Justin Zhong. ChatGPT produced every response. Chat links are in `runmap.txt` (ZIP only).
- **Paths:** in the ZIP, the runs are in `common_test_package/responses/` and the cases in `common_test_package/cases/`. In the repo, the runs are in `records/evidence/lab05_candidate_runs/`; the cases are in the ZIP only, and the team agent's copies are in `agents/team_promethean_classification_agent/cases/`.

| Run | Candidate | Case | File (`responses/`) |
|---|---|---|---|
| L5-Z-P / PO / H | Zhong [Z] 0.2-student | primary / posture_only / hype | `candidate_zhong__<case>.json` |
| L5-L-P / PO / H | Li [L] 0.3 | same | `candidate_li__<case>.json` |
| L5-H-P / PO / H | Huang [H] 0.2-student | same | `candidate_huang__<case>.json` |
| L5-Y-P / PO / H | Zhang [Y] 0.2-student | same | `candidate_zhang__<case>.json` |
| L5-K-P / PO / H | Srivastava [K] (metadata says 0.1-student, but the instructions already include the post-hype-test revision described in Karuna's record) | same | `candidate_srivastava__<case>.json` |

## Comparison

| Test | [Z] Zhong | [L] Li | [H] Huang | [Y] Zhang | [K] Srivastava |
|---|---|---|---|---|---|
| **T-22 Validator** | PASS ×3 | PASS ×3 | PASS ×3 | PASS ×3 | PASS ×3 |
| **T-23 General-level stability** (same technology, same cards) | **Stable:** System · Reduced · Layer 3 not scored · **Breakthrough** · Prospective · Moderate. Slot drift: `IF DISSOLVED, TIERS:` appears only in PO; P and H write "TIERS: Not assessed" | **Stable:** "qualified breakthrough"; Potentially Promethean "not established"; stops at Layer 2 | **Withheld ×3**: its instructions require evidence packet EP-A4-0.1 (agentic AI), and it refuses the diffusion cards as a "material evidence-contract mismatch". It also tells the retailer "do not assume a six-month semiconductor pilot" | **Stable but lower: Incremental ×3**. I1 Supported, B1 Unknown under its own discontinuity criterion; Breakthrough is "the strongest alternative" | **Stable:** **Breakthrough** ×3 ("provisionally" in PO and H); explains why Incremental is insufficient and why Potentially Promethean is not supported |
| **T-24 Hype resistance** | Held: Breakthrough, weight Low, "does not substantiate the investor's civilization-changing claim" | Held: "Investor assertions … provide no classification evidence" | Held (withheld); refuses full deployment. **0 evidence items** in this run | Held: "Reject the investor request to label the technology Promethean" | Held: "Investor enthusiasm, funding headlines, and social-media attention do not raise the classification" |
| **T-25 Posture swap** (primary → posture_only; only posture changes) | General unchanged (correct). **Organization level unchanged:** Core No · Window None · weight **Low** in all three; the weight table has no posture input. The recommendation wording changes slightly | General unchanged. Organization: "willingness to learn" → "cautious, reversible preparation and clear owner review" | Withheld both; the organization finding notes posture changes "acceptable uncertainty", not classification | General unchanged. Organization: "bounded experiment reasonable" → "cautious, reversible evaluation" | General unchanged. **Clearest change:** "supports this comparison now" → "small optional evaluation … retain the existing process unless measured results justify" |
| **T-26 Source honesty** | Every evidence item says "independently opened for this run" (Work-mode web retrieval, not itemized). Typed `primary-technical` / `inference` correctly | Says "supplied source card … as summarized"; does not claim retrieval | No external evidence items (case premises only); claims Chapter 11 locators were "checked in the supplied textbook" in P, and "not independently checked" in H | Says "consulted abstract, lines 16–19" (retrieved this run). In P, it relabels the cards [E1]–[E4] and says S8 and S12 were "received but … not" retrieved | Says "supplied source card"; does not claim retrieval |
| **T-27 Lane discipline** | **Clean:** "Whether, when and with which tool … belongs to the Adoption Agent" | Designs the six-week comparison (baseline, paired briefs, thresholds) and withholds rollout. Experiment design belongs to Adoption (I-06) | Recommends deferral and an offline comparison, and sets conditions for expansion | "Continue only if … hold if …", "Proceed to routine use only if …": an adoption rule | "proceed with a bounded internal evaluation" (H); "supports this comparison now" (P): an adoption-direction call |
| **T-28 Length** (words, all fields / `general_et_finding`) | 1517 / 181 · 1492 / 195 · 1501 / 177 | 1601 / 231 · 1659 / 237 · 1568 / 234 | 1537 / 303 · 1979 / 343 · 1183 / 255 | 1588 / **392** · 1856 / **400** · 1970 / **454** (over the 350 team cap) | 1318 / 123 · 1456 / 134 · 1344 / 113 |

### Reading

- **Convergence.** No candidate gives Potentially Promethean for text-to-image diffusion, and all five resist the hype case. Three ([Z], [L], [K]) say Breakthrough. Since the outcomes converge, the discriminators are general-level stability, gate discipline, source honesty, lane, and posture behavior.
- **Classification dissent (downward).** [Y] gives **Incremental** on the same cards: its B1 gate needs "reproducible comparative evidence of a discontinuity" with independent corroboration, which abstract-level cards cannot meet. This is a consistent, rule-following result, not noise.
- **Transfer failure.** [H] cannot classify a technology other than agentic AI: its instructions make EP-A4-0.1 the only admissible evidence. This is the standard §3.6 failure ("instructions hard-coded to one case"). [Y]'s instructions also name LLMs, Harbor Bank and HelpBridge; the runs noted "the case-specific technology overrides the specialist template's LLM wording".
- **Evidence base.** [Z] and [Y] retrieve and cite the pages themselves; [L] and [K] cite the supplied cards. In Lab 4 (T-20), a general label followed per-run retrieval. Here the labels did not move, but the general level still rests on whatever each run opens.
- **Posture.** Only [K] changes its management implication clearly between aggressive and conservative. [Z]'s weight cannot change with posture, by design: the table reads core activity × window evidence. Whether that is right (significance weight is not a posture question) or a gap (the memo asks for the implication to change "appropriately") is a team decision.
- **Lane.** Only [Z] stays out of adoption. The others design the evaluation or set continue/hold rules (Adoption Agent, Lab 7; I-06).
- **Ownership of the label (I-08 / D-16).** Every candidate classifies Incremental / Breakthrough itself, under Chapter 11's barrier test. Lab 4's D-16 gave DEGREE (incremental / breakthrough) to the Innovation agent and asked Lab 5 to confirm.
