# Lab 7 candidate comparison (Adoption), T-40 to T-47

**Cases (D-36):** Dian Li's text-to-image concept boards, aggressive vs. conservative; only `adoption_posture` differs; cards D1–D4, G1. Caveat: [L] has home field; [H] is hard-coded to wafer-fab scheduling. Candidate versions: [Z] 0.2-student, [L] 0.2, [H] 0.5-student, [Y] and [K] 0.1-student. Run files: `candidate_<surname>__primary|contrast_1`.

| Test | [Z] | [L] | [H] | [Y] | [K] |
|---|---|---|---|---|---|
| T-40 Validator | PASS ×2 | PASS ×2 | PASS ×2 | PASS ×2 | PASS ×2 |
| T-41 Recommendation (aggressive → conservative) | Bounded experiment → Monitor | Bounded experiment → Defer | Bounded experiment → same | Experiment → Defer | **Defer → Defer** |
| T-42 Label stability | **FIT Strong → Partial; RELATIVE ADVANTAGE Unclear → Claimed; different retrieved evidence** | Stable (no labels) | Stable | Stable | Stable |
| T-43 Case in general level | Clean | Case and posture words | Case words; "scheduling instructions" leak | Case words; posture in contrast | Case and posture words |
| T-44 Posture effect | Table cell | Trial threshold | Timing only | Concrete peer gate | No vendor selected forces Defer for both |
| T-45 Source labelling | Searched past cards; card typed `inference` | Free-text types | Cards typed `VERIFIED SOURCE` | "Supplied" types | Free-text types; says nothing retrieved |
| T-46 Lane | Three clean handoffs | Org Adoption named | Org Adoption named | Org Adoption named | **No Org Adoption mention** |
| T-47 Bias and reversal | Slots; names one bias | Partial | All four | Partial | None explicit |
| Words g/a/o/rec (primary) | 167/132/226/103 | 89/94/89/353 | 75/119/98/196 | 100/120/129/299 | 64/76/90/228 |

**Reading:** all ten runs say "prepare now, no tool use yet". The labels hide the same action, so label meaning, stability and lane are the discriminators.
