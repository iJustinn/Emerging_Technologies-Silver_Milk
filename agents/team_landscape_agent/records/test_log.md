# Test log (Lab 9)

**Runtime (D-55):**
- ChatGPT web in Ego Lite (task space 12), Work mode, **GPT-6.2 Sol** at **Light** (Power slider stop 0 of 0–4, the lowest stop for this model). The model changed from GPT-6.1 Sol (Labs 4–8) on Justin's instruction; effort and project unchanged.
- A fresh chat per run inside project MASY-1800. Project settings read 2026-11-17: instructions empty; Memory Default; Space access Enabled; source `1800-Textbook.pdf`. Nothing changed.
- Packet attached; message `[Run <ID>] Run the attached MASY1800 specialist agent prompt packet exactly as written. Return JSON only, in this chat reply; do not create files.`
- `launch.sh` read the visible labels before every send; every one of the 22 runs printed `GPT-6.2 Sol | Light`. No aborts, no relaunches, no empty chats. ChatGPT appended "(n)" to some attachment names (duplicate file names in the project space); the packet name prefix matched every time.
- Collection: real pointer click on the reply's copy button; `save_resp.py` saved raw copy and JSON. All 22 replies: zero characters removed, no repairs.
- Run map: `common_test_package/runmap.txt` (ZIP). Budget 22, used 22 (10 candidate, 4 v0.9, 4 v1.0, 4 v1.1).

**Cases (D-54):** primary and contrast_1 = Dian Li's concept-board pair (two-marketer retailer vs. nine-staff retailer with procurement; same technology and application); contrast_2 (transfer) = Yuanxiang Zhang's multinational-bank information-support case (agentic AI); contrast_3 (hype) = Justin Zhong's regional bank plus the board memo citing a "90% of code" prediction and "peer banks have already moved to agent-first engineering". Cases were run as saved; no source cards added. Dian's primary names a source-ledger file path that is not in the packet; the v1.1 primary run said the ledger was unavailable and did not use it.

| Test | Result |
|---|---|
| T-61 to T-68, candidates | 10 runs valid. See `lab09_candidate_comparison.md` |
| T-69 v0.9, 4 cases | Valid. Stance Active watch in all four. **Preserved failures:** W-1 L6 written "Unclassified" (contrast_1) and "No supported rating" (contrast_2), outside the label set, splitting the pair (R-3 FAIL); W-2 MOVEMENT `Toward` resting only on vendor releases (contrast_1, contrast_2), and in the hype case a vendor's own customer report as MOST CONSEQUENTIAL DEVELOPMENT. Contrast_1 organization finding 325/320 words. What worked: C2PA cited at 2.5; memo's 90% traced to Amodei 2025-03-10; execution gates separated. `checks_v0_9.txt` |
| T-70 v1.0, 4 cases (F1 Insufficient evidence value, F2 vendor items cannot move stance, F3 tracker list + SAME STANCE BECAUSE) | Valid. Scheduled / Scheduled / Scheduled / Active watch. W-2 gone (hype case `Toward` rests on NIST). **Preserved failure:** `Insufficient evidence` overused (4 of 6 labels in the primary) and the pair split on L7 (R-3 FAIL); `SAME STANCE BECAUSE: None`. `final_checks_v1_0.txt` |
| T-71 check proof | Every new check in `check_landscape_lab09.py` fails or flags on the real output it targets (v0.9, v1.0, candidates [Z] and [L]). `common_test_package/check_proof_on_targets.txt` |
| T-72 v1.1, 4 cases (tightened `Insufficient evidence`; SAME STANCE BECAUSE must cite a case fact) | Valid. **Scheduled watch in all four.** Zero mechanical FAILs. Pair Step 1 and Step 2 labels identical (Developing / Use cases emerging / Consolidating / Emerging / Mixed / Mixed; Thin; manual boards). Hype case: memo claims traced and excluded. `SAME STANCE BECAUSE: None` persists (W-3). `final_checks_v1_1.txt` |

**Human §4 review (v1.1):**
- **Swap test (two-marketer vs. nine-staff):** the stance is the same (Scheduled watch) and Step 1–2 labels are identical, as the rules require. Step 3 changes through case facts: UNIT OF ANALYSIS (two marketers and owner vs. creative operations lead with procurement and security), EXECUTION GATES (owner not stated vs. security/procurement review function), MOST CONSEQUENTIAL DEVELOPMENT (an independent July 2026 reference-conditioning comparison vs. human-rated editing-failure diagnostics), OPTIONS DOCUMENTED and triggers. The stance does not change because neither organization's gating condition is met by external evidence; the difference between them is readiness, which is Org Adoption's question. **The swap test passes on Step 3 content, not on the stance.**
- **Execution gates stay gates:** terms, upload rights, retention, security and procurement appear only under EXECUTION GATES in all four runs. The R-8 word scan passes on all four v1.1 runs (it flagged "procurement" and "authorization" in two v1.0 runs, where the "authorization" was NIST's identity-and-authorization work). Read by eye, the v1.1 RELEVANT SIGNALS name only external developments: contrast_1 cites L1 fidelity variation, L4 integrated and downloadable routes, L6 metering; contrast_3 cites a regression-carryover study, one large-bank deployment and NIST standards work.
- **Hype control (contrast_3):** CONDITION STATUS Partly met, MOVEMENT None ("the reported bank expansion concerns a single large, non-comparable bank"), STANCE Scheduled watch. STALE/HYPE FLAG names the memo's peer claim (no traceable dated source) and Amodei's 2025-03-10 forecast (window elapsed); CONTROL: neither counts toward peer use.
- **Transfer (agentic AI, bank information support)** passes with unchanged instructions: own labels, Scheduled watch, HKMA discussion paper as the most consequential development (L5).
- **Lane is clean:** no adopt, pilot or vendor choice; OPTIONS DOCUMENTED ends NO SELECTION; six HANDOFF lines per run.

**Version-to-version stance movement:** on the same unchanged cases the stance went Active (v0.9) → Scheduled (v1.0/v1.1) on the pair and transfer, and Active → Active → Scheduled on the hype case. Retrieval differs in every run, so the movement cannot be credited to the rule changes alone (W-4).

**Weaknesses:** W-1 to W-6 in `agent_record.md`.
