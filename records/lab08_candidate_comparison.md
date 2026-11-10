# Lab 8 candidate comparison (Organizational Adoption), T-50 to T-57

**Cases (D-43):** Dian Li's text-to-image concept boards. Primary: a two-person marketing team with no AI sponsor, lead or operating owner. Contrast: a 14-person marketing and content team with a designated sponsor, a two-person evaluation allocation, a named reviewer, a budget owner, reference-data ownership and a fallback. Same technology and application strings; the organization changes. Cards D2, D3 and G1 are carried in the case (checked in Lab 7 as E-40, E-41 and E-43).

**Caveat:** [L] has home field. [H] is hard-coded to wafer-fab drills and [Y] to banking customer service; both runs say so in their own text. [Z] and [K] are case-agnostic. Dian's `readiness_framework.md` is not in the packet, because `build_prompt.py` reads only `specialist_instructions.md`.

**Versions:** [Z] 0.2-student, [L] 0.2, [H] 0.3, [Y] 0.1-student, [K] 0.1-student. [K]'s metadata `specialty` is the template placeholder; each run wrote its own specialty string. Run files are `candidate_<surname>__primary|contrast_1`; the run map is `runmap.txt`.

| Test | [Z] | [L] | [H] | [Y] | [K] |
|---|---|---|---|---|---|
| T-50 Validator / strict schema | PASS ×2 / PASS ×2 | PASS ×2 / PASS ×2 | PASS ×2 / PASS ×2 | PASS ×2 / PASS ×2 | PASS ×2 / PASS ×2 |
| T-51 Headline (small → staffed) | **Abstained** → Build readiness first | PREPARATION_ONLY → CONDITIONALLY_READY_FOR_BOUNDED_EVALUATION | Withhold trial authorization → **Withhold** (same headline) | Preparation "Insufficient information" → "Conditionally ready … for preparation only"; launch Insufficient ×2 | "Planning yes; trial conditional, withheld" → "Planning yes; bounded evaluation conditional" (near-identical) |
| T-52 Verdict logic | **Preserved failure:** abstains under its 5-unknowns rule even though its own VERDICT SENSITIVITY gives Do not scale yet either way (3 Not ready). It rates routine production, which the case does not ask about | Status by named prerequisites | Gate logic built for drills; reads "documented ≠ demonstrated" correctly | Stage ladder; Insufficient for launch in both | Stage ladder |
| T-53 General and application stability | FIT Partial ×2, FIT GAP stable; **DEMAND [D4] Moderate → High**, following per-run retrieval (Stability AI docs vs. Black Forest Labs pricing) | Stable prose | Stable prose | Stable in substance; says the banking instructions do not apply | Stable prose |
| T-54 Case in general level | Clean structure; leak check flags "accountable", "creative" | Clean | Clean | **Case words ("retailer") and its own banking scope** | Flags "accountable", "evaluation" |
| T-55 Dominant gap (staffed case) | D6 = unresolved vendor/input terms | Making existing roles and hours explicit for the evaluation | Vendor permissions first | Authority and permissions first | **Vendor/input-use authorization** as the single missing factor |
| T-56 Missing-information behavior | MORE INFO → lines, ordered by verdict impact | One concrete owner/hours question | Specific charter and roles request | Exact authority questions | "Single most consequential missing factor" plus one question |
| T-57 Source labelling and lane | Retrieves vendor docs and pricing each run (types correct; sources differ by run); only candidate with HANDOFF lines | Cards marked "not independently reverified" | Cards marked "not inspected" | Retrieved and "rechecked" Rombach and NIST in this run | Cards marked as inherited, not verified |
| Words g/a/o/rec (primary) | 155/88/375/153 | 69/102/260/324 | 48/106/419/223 | 127/124/**725**/409 | 51/64/210/261 |

**Reading:** every candidate agrees on the substance. The small team should prepare but not run a trial, because sponsorship, an accountable lead and protected hours are missing. The staffed team can organize a bounded evaluation but has no trial permission. The discriminators are:
1. Whether the headline changes with the organization ([L], [Y] and [Z] change it; [H] and [K] barely do).
2. Whether "ready" names the stage it means ([Z] judges routine production only).
3. Whether an external permission gate is mistaken for the organization's main readiness gap. [Z], [H] and [K] rank vendor terms first in the staffed case; [L] does not.
4. Label stability. [Z]'s Step 1 DEMAND labels move with retrieval.
