# Lab 9 candidate comparison (Landscape), T-61 to T-68

**Cases (D-54):** Dian Li's concept-board pair. Primary: a two-marketer homeware retailer with no AI sponsor, preparing disposable internal mood boards. Contrast: a nine-staff retailer with a creative operations lead, photo repository, evaluation budget and procurement review. Same technology and application strings; the organization changes. Assessment date in the cases: 2026-11-13. Runs: 2026-11-17, GPT-6.2 Sol Light (D-55).

**Caveat:** [L] has home field, and its instructions are written for image generation. [H] is written for wafer-fab scheduling and [Y] for banking; both still ran on the image case. [Z] and [K] are case-agnostic. Dian's primary names a source-ledger file path that no packet contains.

**Versions:** [Z] 0.2-student, [L] 0.2, [H] 0.2-student, [Y] 0.2-student, [K] 0.1-student (its instructions were revised in Assignment 8 but the metadata version was not bumped; its agent record is the blank template). Run files `candidate_<surname>__primary|contrast_1`; run map `runmap.txt`.

| Test | [Z] | [H] | [L] | [Y] | [K] |
|---|---|---|---|---|---|
| T-61 Validator | PASS ×2 | PASS ×2 | PASS ×2 | PASS ×2 | PASS ×2 |
| T-62 General level across the pair | L1, L2, L4–L7 labels identical. **L3 differs:** Thoughtworks 2022-10 "Stable Diffusion — Assess" vs. "Not covered by IEEE (2026-01)" | Prose stable | Prose stable | Prose stable | Prose stable |
| T-63 Organization level (swap test) | Gating condition and unit change; **stance identical** (Partly met × Toward → Active watch ×2) | Priorities reworded; same order | Ranks reworded; same order | Changes (feasibility, integration, procurement) | Changes |
| T-64 Execution gate vs. landscape signal | Terms sit inside the gating condition and RELEVANT SIGNALS (R-8 scan flags "permission", "terms") but are not ranked first | **Permissions ranked first ×2** | **Permissions ranked first ×2** (the weakness [L]'s own Assignment 8 review named) | **Rights ranked first ×2** | **Privacy/rights ranked first ×2** |
| T-65 Stale/hype flag | **Present ×2**, a dated claim with REFRESH BY (BFL speed claim; FLUX pricing) | None | None | None | None |
| T-66 Currency | Cites a **2022** radar placement as the L3 entry | — | **C2PA v2.2 cited again** (2.5 published October 2026) | — | C2PA "2.4" |
| T-67 Evidence typing | The memo's classes (vendor-claim, industry-analyst, independent, standards-regulatory, inference) | Free-text types | Free-text types ("VERIFIED — …") | Free-text types | Free-text types |
| T-68 Thresholds and lane | **Invents numeric thresholds** ("at least 9 of 10 boards", "20 or more matched briefs") | No pilot advice | No pilot advice | No pilot advice | "who can approve a trial" appears only as a question; no pilot advice |
| HANDOFF lines | 2 per run | 0 | 0 | 0 | 0 |
| Words g/a/o/rec (primary) | 267/115/275/66 | 82/149/150/68 | 101/109/100/61 | 93/261/101/101 | 154/169/132/99 |

**Reading:** the recommendations converge. Every candidate says prepare a vendor-neutral comparison, keep manual boards from existing photography as the baseline, and authorize no trial. So the discriminators are:
1. The stale/hype control, which only [Z] produced (memo item 4).
2. Whether permissions are mistaken for the landscape signal: four of five ranked them first, which [L]'s own review had already called a conflation.
3. Currency: [L]'s C2PA 2.2 error recurred on a new runtime, and [Z] reported a four-year-old radar placement as current.
4. Stability of fixed labels ([Z]'s L1–L7 held; its L3 did not).
5. [Z]'s invented thresholds, which [Y]'s "pending owner approval" rule fixes.

Ratified synthesis: D-59.
