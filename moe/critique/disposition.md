# Disposition of critic findings (L10-CR1) and dry-run findings (DR-x): 0.9-design → 1.0-design

The operator proposed each disposition; the team decided them in session (Justin Zhong's answers; decision-log entries D-73 to D-79).
- **Q1–Q3**: asked as separate team questions.
- **Bundle**: accepted together in one team answer.
- **Lab 11**: goes to the integration work list, not into 1.0-design.

| ID | Finding (short) | Proposed disposition | Decided |
|---|---|---|---|
| CR-1 | Unflagged brief "Accepted by rule" without an owner disposition (high) | **Q1** | **Rejected** (D-74). Team reason: flags cover what matters; F-11 (D-79) sends every action that starts work to the owner |
| CR-2 | Who confirms conflict type; caution vs. F-3 | Accept: Q/E/J become explanatory annotations; any unresolved material disagreement or execution blocker goes to the owner whatever its type | **Accepted** (D-75) |
| CR-3 | Default conflict rules compare unlike measures; readiness stage logic inverted | Accept: unlike measures are shown side by side with no default J (Innovation↔Promethean, Promethean↔Adoption); readiness is checked against the stage the action executes (**Q2**) | **Accepted** (D-75); readiness rule D-73, values D-79 |
| CR-4 | A valid cite does not prove the condition follows from it | **Q3** | **Accepted** via Q3: narrowed synthesizer with verbatim support (D-76) |
| CR-5 | One extraction rule per label (aliases, field precedence, duplicates, multiline) | Accept: matches DR-4. Contract gets per-label field precedence, aliases, case-insensitive values, parenthesized values kept whole, full source passage kept with a canonical label | **Accepted** (D-75) |
| CR-6 | Validate before copying upstream | Accept: check each routed output before its wave hands off; record the attempt used; if it is replaced, rerun the downstream experts | **Accepted** (D-75) |
| CR-7 | Evidence policy per label; ENTREPRENEURSHIP missing from G-3; no-pack branch contradicts G-3 | Accept: one evidence-policy table per label, with an explicit no-pack branch (G-3 suspended, F-4 fires) | **Accepted** (D-75) |
| CR-8 | F-2/F-8 value mismatches; no action→stage map; AC-S3 reads as an overall confidence | Accept: canonical status values; action→stage map (**Q2**); AC-S3 becomes "no overall confidence claim; original confidences kept" | **Accepted** (D-75); stage map D-73 |
| CR-9 | Inputs used but not contracted (Org EXECUTION GATES, DEMAND set, Promethean irreversibility) | Accept: add them to the contract | **Accepted** (D-75) |
| CR-10 | Each brief field needs one owner; synthesizer schema too wide | Accept, shaped by **Q3**: gates, missing evidence (with `asked_by` computed by script) and triggers come from expert outputs by script | **Accepted** (D-75, D-76) |
| CR-11 | Legacy filename discovery in live routing | Accept: live runs use only `moe_<RUNID>__<agent>.json`; AC-C1 names exact baseline files | **Accepted** (D-75) |
| CR-12 | Firm/Qualified/Weak display scale misleads | Accept: remove it; show each expert's own confidence words plus a separate abstention status (removes machinery) | **Accepted** (D-75) |
| CR-13 | Timing forwarded when its stage is Withheld | Accept as already handled (Adoption reads stage, basis and timing together, and its rule says a timing from a Withheld stage is not stage evidence; DR-6 shows it worked); fixture to Lab 11 | **Accepted** (D-75) |
| CR-14 | F-9 depends on the expert listing missing intake | Accept: the script checks the required intake fields for the stage directly; `Undetermined` stays distinct from `Not ready` | **Accepted** (D-75) |
| CR-15 | Vendor-only support can hide behind an irrelevant independent cite | Accept in part: AC-E2 requires each decisive headline to name its supporting passage and source class; the fixture goes to Lab 11 | **Accepted in part** (D-75) |
| CR-16 | AC-C1 baselines not frozen; missing labels | Accept: name exact baseline files and Pack ID; add Diffusion TECHNOLOGY STAGE and Innovation ENTREPRENEURSHIP | **Accepted** (D-75) |
| CR-17 | AC-F1 must use a routed expert; AC-F4 end-to-end | Accept | **Accepted** (D-75) |
| DR-1 | Pack-bound ENTREPRENEURSHIP and routed Promethean WEIGHT flip on an identical packet | **Q4**: limitation W-1 extended, a Lab 11 rerun-stability check, versioned fixes considered in Lab 11; D-18 formally reopened | **Accepted** as proposed: W-1, AC-C4, D-18 reopened (D-77) |
| DR-2 | Landscape L1 drifts across reruns | Limitation W-1; Lab 11 | **Accepted**: W-1 (D-75) |
| DR-3 | Stable labels | Evidence only | No change (evidence/records) |
| DR-4 | Extraction defects | → CR-5 | **Accepted** (D-75) |
| DR-5 | Format-only FAILs would force reruns | Accept: hard checks (validator, strict schema, pack discipline, recomputed COUNTS, unverified behind a headline, lane) trigger a rerun; caps and format are warnings shown in the brief | **Accepted** (D-75) |
| DR-6 | Upstream reads worked | Evidence only | No change (evidence/records) |
| DR-7 | Synthesizer `asked_by` inflated; caution signals misused; S-2 is blind to meaning | **Q3** | **Accepted** via Q3 (D-76) |
| DR-8 | Flags fired on the first case | **Q1** | Q1: keep review-when-flagged (D-74); F-11 added after review (D-79) |
| DR-9 | F-4 age rule wrongly hits current standards | Accept: the age rule applies to market, capability and adoption cards; standards use a latest-version check | **Accepted** (D-75) |
| DR-10 | Launch loop printed nothing, so duplicates were launched | Accept: the runner logs every launch to a file and checks the chat list before any relaunch; Lab 11 work list (I-16) | **Accepted** (D-75) |
| DR-11 | G-3, G-4 and G-6 have no script | Lab 11 work list | **Accepted** (D-75) |
| DR-12 | Conflict table built 5 of 8 pairs | Accept: the script builds every §4.2 row | **Accepted** (D-75) |
| DR-13 | D-18 reopened; D-53 and D-65 not triggered | Records | No change (evidence/records) |
