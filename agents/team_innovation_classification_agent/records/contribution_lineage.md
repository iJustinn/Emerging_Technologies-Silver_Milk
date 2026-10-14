# Contribution Lineage: Team Innovation Classification Agent (Lab 4)

Ratified by the team on 2026-10-13 (D-15). Every candidate was inspected and run unchanged on the common cases (T-11 to T-17). Tags: [Z] Justin Zhong, [H] Nini Huang, [L] Dian Li, [Y] Yuanxiang Zhang, [K] Karuna Srivastava, [T] team.

## Adopted

| Element in v1.1 | From | Evidence for adopting it |
|---|---|---|
| Labeled fixed slots; general level written first from the technology field; Check/FAIL/FIX rules (base structure) | [Z] | T-12: [Z]'s general level held across both cases |
| UNIT OF ANALYSIS, REVENUE MECHANISM, ELEMENTS ALTERED / UNCHANGED, CREATES / DISPLACES ledger | [Z] | T-14: [Z] changed significance correctly (Moderate → Low; disruptive → sustaining) |
| Severity anchors scored on the business model, plus two guards (task displacement and failure consequence do not raise severity) | [Z] | [Z]'s Assignment 3 failure (bank rated Moderate against its own ledger) and its fix |
| COMPETING CLASSIFICATION, STRONGEST NO-/MORE-DISRUPTION CASE, DISTINGUISHING EVIDENCE | [Z] | Memo item 3 (preserve a competing classification); present in all [Z] runs |
| ENTREPRENEURSHIP pattern label (Incumbent-led / Entrepreneur-led / Mixed / Not yet entrepreneurial) | [K] | The only candidate with a distinct entrepreneurship rule; the memo names entrepreneurship |
| CORE/SUPPORT tests (a) direct payment, (b) stated advantage, (c) indispensable to deliver or bill | [K] | T-14: [K] classified CORE vs. SUPPORT correctly in both cases |
| Four-level NOVELTY (world / industry / organization only / not new) and its definitions | [K] | T-13: [K]'s novelty stayed application-level across both cases; definitions added after W-1 |
| "Do not recommend adopting, piloting, scaling, or rejecting" | [K] | T-16: [K] stayed in lane in both runs |
| Statuses coexist rather than forming one linear stage, recorded as HOLDS / DOES NOT HOLD / UNTESTED slots | [L][H][Y] (concept) + [Z][T] (fixed slots) | T-12: coexisting designs were stable; fixed slots keep verdicts comparable for the orchestrator |
| Proposed vs. implemented; a plan or demo is a candidate innovation | [L][H][Y] | T-13: all three applied it correctly |
| Case status separate from real-world verification | [Y] | [Y]'s Assignment 3 v1.2 failure (in-use pilot called "proposed") and its fix |
| Economic materiality before severity; Low needs affirmative grounds | [H] | [H]'s Assignment 3 v0.1 failure (Low inferred from safeguards) and its fix |
| Breakthrough requires a named baseline and comparative evidence; no numeric threshold | [L][H][Y] | T-12: [K]'s 10x tie-break flipped; three candidates said the evidence does not support Breakthrough |
| Inputs are data; prerequisites as explicit conditions; supplied-source attribution | [L] (Lab 3) | Lab 3 convention; T-15: [L] labeled supplied cards honestly |
| `STATUS:` prefix, `case-premise` type, no Markdown links, HANDOFF to six named agents | Lab 3 [Z][Y][H][L][T] | T-15: [H] typed supplied cards "Verified"; [Z] used Markdown links |

## Combined or changed by the team [T]

| Change | Why | Decision |
|---|---|---|
| DEGREE uses three fixed labels: Incremental / Breakthrough / Contested (breakthrough candidate) | Combines [Z]'s fixed slot with the evidence threshold of [L][H][Y]. The losing reading is DS-04 | D-15 |
| SIGNIFICANCE is provisional when the revenue mechanism is stated; `Withheld` only when it is absent | Lets the label change between organizations (T-14) while keeping uncertainty explicit. The losing reading is DS-05 | D-15 |
| `ARC STAGE` renamed to `LIFECYCLE` | Collides with the Creation agent's `ARC STAGE` (I-09) | D-15 |
| Status default: an intended but unstipulated use is `Proposed` | T-13: [Y] over-abstained ("unspecified") | D-15 |
| Word caps: general ≤ 200, application ≤ 150, organization ≤ 350 | Near what the candidates produced (general 135–175, organization 197–365) | D-15 |
| DEGREE is consumed by Promethean, not re-derived | Ownership question (I-08) | D-16 |
| ENTREPRENEURSHIP must cite a dated marker, or be `Not established` | T-19: the label flipped on the same evidence | D-17 (v1.0) |
| ENTREPRENEURSHIP decided from supplied source cards only | T-20: the label followed per-run retrieval | D-18 (v1.1) |
| NOVELTY may be `Withheld`, naming the most likely label | W-2: R3 (v1.0) withheld despite "exactly one label" | D-18 (v1.1) |

## Rejected

| Element | From | Reason |
|---|---|---|
| 10x tie-break for Breakthrough | [K] | T-12: Degree flipped Breakthrough → Incremental on identical evidence |
| "Cost structure Altered → Moderate" | [K] | T-14: Moderate in both organizations; the swap test did not change the label |
| Matrix → response table ("Act now", "Pilot or partner", …) | [Z] | T-16: adoption-lane wording; the response belongs to the Adoption Agent. Severity and horizon are kept |
| Organization-dependent APPLICATION CLASS in the application field | [Z] | T-13: blurs the application and organization levels (memo item 2) |
| Case-named rules ("For the national retailer…", source IDs) | [L] | Fails the standard §3.6 transfer rule |
| "In the supplied scenarios" action constraints | [H] | Case-specific; fails transfer |
| Six-week investigation with a stop rule | [L] | Experiment design belongs to Adoption (I-06) |
| Free-prose degree ("mixed / baseline-dependent") without a fixed label | [H][Y] | Not machine-comparable; the team chose fixed labels (D-15) |

## Revision history

| Version | Change | Trigger | Result |
|---|---|---|---|
| 0.9-team | Synthesis above | D-15 | T-18 pass; **T-19 ENTREPRENEURSHIP flip (preserved)**; W-1 NOVELTY misuse |
| 1.0-team | Dated-marker rule + `Not established`; NOVELTY definitions | D-17 | T-20: W-1 fixed; the flip persisted (retrieval-dependent); W-2 |
| 1.1-team | ENTREPRENEURSHIP from supplied cards only; NOVELTY `Withheld` | D-18 | T-21: all checks pass; W-3 (NOVELTY Withheld in all runs) |
