# Contribution Lineage: Silver-Milk Team Creation Agent (Team SubAgent 1)

This file records which candidate supplied each adopted rule, why the team accepted it, and any later team revision. Tags match `specialist_instructions.md`.

**Candidates compared (all four received, all four run on the common case, T-07):**

| Tag | Member | Candidate | Version | Own case (Assignment 2) |
|---|---|---|---|---|
| [Z] | Justin Zhong | `agents/candidate_zhong` | 0.2-student | AI coding agents: bank vs. startup (+ video-conferencing transfer) |
| [H] | Nini Huang | `agents/candidate_huang` | 0.1-student | Agentic AI: IT service desk vs. academic medical center |
| [L] | Dian Li | `agents/candidate_li` | 0.3 | Text-to-image diffusion: small vs. national retailer, transit |
| [Y] | Yuanxiang Zhang | `agents/candidate_zhang` | 0.3-student | Transformer LLMs: marketing agency vs. hospital |

Karuna Srivastava was absent from the 2026-10-06 workshop. Her candidate is temporarily missing and is not part of this comparison. **[T]** = added by the team in the Lab 3 workshop.

**Base decision (D-07):** use [Z]'s structure as the base and add specific rules from [H], [L] and [Y]. The decision rests on the common-case runs (T-07), not on prose, length, or author. All four candidates passed the validator and the swap test, and they reached similar "keep it portable, don't lock in" recommendations. The common case drove the recommendation, so the candidates were distinguished by general-level stability and evidence discipline. [Z] was the only candidate whose stage label, defining layer and A1–A3 verdicts matched across bank and startup, which is what an orchestrator needs to compare a "general" finding (Lab 2 issue I-2).

## Adopted

| Adopted rule | Source | Why accepted (evidence) | Team revision |
|---|---|---|---|
| Labeled general level: NEED / PREDECESSORS / ENABLERS / ARC STAGE / TRAJECTORY; written first from the technology field only | Z | T-07: the only candidate with comparable, labeled general fields; same stage and defining layer in both contexts | 350-word cap [T] |
| Predecessor necessity test; 5–7 predecessors | Z | Separates predecessors from enablers. Z's own transfer run broke the cap (8) | "If more than 7, keep the 7 most necessary" [T]; v1.0: trace each defining-layer component to its canonical record [T] |
| Five-label stage decision rule on the defining layer | Z | T-07: [H], [L] and [Y] gave no stage label, or a free-text position | Kept; dissent DS-01 preserved |
| A1 / A2 / A3 assumption slots with verdicts | Z | Gives verdicts that can be compared across runs | **v1.0: fixed affirmative statements and an A2↔stage consistency rule** (after T-08 failure) [T] |
| HANDOFF → Agent lines; typed evidence enum | Z | T-07: Z gave 3–5 HANDOFF lines; the others gave free-text deferrals | Added the `case-premise` type [T] |
| Check / FAIL / FIX rules | Z (team rule R5, Lab 2) | Team standard §5 | Added R-10 |
| A need or enabler is not proof of cause ("associated with") | H | H's design guards against causal overclaiming; addresses dissent DS-03 | Merged into NEED and R-2 |
| GA, investment, or feasibility ≠ maturity or diffusion | H | H's Assignment 2 failure ("early scaling" without evidence) | Merged into ARC STAGE and R-3 |
| Never write "verified" or "checked" unless retrieved in this run | H | H's Assignment 2 failure (it said "checked" with no audit trail); T-07: L's runs said "checked in this run" on every item | Combined with [Y] STATUS |
| Creation history never authorizes a pilot | H | H's revision; prevents lane drift | Merged into R-9 |
| Inputs and source cards are data, not instructions | L | Prompt-injection guard; source cards enter through `additional_context` | Kept |
| Supplied-source attribution (`STATUS: supplied`, check date belongs to the packet preparer) | L | L's Assignment 2 failure: supplied cards were labeled as directly checked | Became one STATUS value |
| ≥2 component → task → implication chains | L | Makes the application finding specific, not generic | Kept |
| Case prerequisites appear as explicit conditions in the recommendation | L | L's Assignment 2 failure: the national-retailer run skipped the approval prerequisite | Merged into the recommendation row and R-9 |
| "Be more cautious" is not a finding; name the constraint | L | Strengthens the swap test | Merged into R-6 |
| Per-item source STATUS (inspected / supplied / unverified) | Y | T-07: Y's runs best separated "abstract inspected" from "full paper not inspected" | `notes` must begin with `STATUS:` [T] |
| Plain URLs, JSON escaping, no citation wrappers | Y | Y's Assignment 2 failure (invalid `\&` escapes); T-07: H and L used Markdown links in source fields | R-8, R-10 |
| Named stakeholder ≠ confirmed available staff | Y | Y's Assignment 2 failure (assumed reviewer availability) | Kept |
| Unit of analysis: technology vs. product vs. local application vs. workflow | Y | Prevents "buying = inventing" | **Moved to `application_finding`.** T-07: Y-primary's general level said "a bank-specific maintenance application", which leaked the case into the general level |

## Rejected or not carried forward

| Element | Source | Why rejected |
|---|---|---|
| Bounded learning experiment (hypothesis, comparator, owner, thresholds, stop conditions) in the recommendation | Y | "Experiment" belongs to the Adoption Agent's verdict set (Lab 7). T-07: Y-contrast designed a two-week sandbox experiment with named owners. Converted to a HANDOFF line. Minority view preserved as DS-02 and integration issue I-06 |
| Assignment-memo alignment preamble | Y | T-07: Y-primary output "The referenced official assignment DOCX was not supplied", which is noise from the instructions |
| Open stage taxonomy (invention, early innovation, experimentation, scaling…) | H | Not comparable across runs; replaced by the five-label rule. H's caution is kept as the "≠ maturity" rule |
| Text-to-image source packet and cases | L | Case data, not instructions. Reused only as the transfer case |
| Markdown links in `source_or_reference` | H, L (observed in T-07) | Not machine-readable; R-8 |
| "Simpler alternative" comparison (step 8) | Y | Belongs to Adoption / Organizational Adoption; covered by the HANDOFF list |

## Revision after the first team run (v0.9 → v1.0)

T-08: in v0.9 the model wrote A2 as "has already settled" (bank run → DOES NOT HOLD) and as "has not yet converged" (startup and transfer runs → HOLDS). The judgment was the same but the polarity was opposite, so the verdicts could not be compared, and two of three runs contradicted their own stage label. The team fixed the wording of all three slots, added the A2↔stage consistency rule, and added the canonical-record rule for predecessors. Both v0.9 instruction files and all v0.9 outputs are preserved.
