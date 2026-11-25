# Disposition of critic findings (L10-CR1) and dry-run findings (DR-x): 0.9-design → 1.0-design

The operator proposed each disposition; the team decided them (see the "Decided" column and decision-log entries D-74 to D-76).
- **Q1–Q3**: asked as separate team questions.
- **Bundle**: accepted together in one team answer.
- **Lab 11**: goes to the integration work list, not into 1.0-design.

| ID | Finding (short) | Proposed disposition | Decided |
|---|---|---|---|
| CR-1 | Unflagged brief "Accepted by rule" without an owner disposition (high) | **Q1** | see Q1 |
| CR-2 | Who confirms conflict type; caution vs. F-3 | Accept: Q/E/J become explanatory annotations; any unresolved material disagreement or execution blocker goes to the owner whatever its type | Bundle |
| CR-3 | Default conflict rules compare unlike measures; readiness stage logic inverted | Accept: unlike measures are shown side by side with no default J (Innovation↔Promethean, Promethean↔Adoption); readiness is checked against the stage the action executes (**Q2**) | Bundle + Q2 |
| CR-4 | A valid cite does not prove the condition follows from it | **Q3** | see Q3 |
| CR-5 | One extraction rule per label (aliases, field precedence, duplicates, multiline) | Accept: matches DR-4. Contract gets per-label field precedence, aliases, case-insensitive values, parenthesized values kept whole, full source passage kept with a canonical label | Bundle |
| CR-6 | Validate before copying upstream | Accept: check each routed output before its wave hands off; record the attempt used; if it is replaced, rerun the downstream experts | Bundle |
| CR-7 | Evidence policy per label; ENTREPRENEURSHIP missing from G-3; no-pack branch contradicts G-3 | Accept: one evidence-policy table per label, with an explicit no-pack branch (G-3 suspended, F-4 fires) | Bundle |
| CR-8 | F-2/F-8 value mismatches; no action→stage map; AC-S3 reads as an overall confidence | Accept: canonical status values; action→stage map (**Q2**); AC-S3 becomes "no overall confidence claim; original confidences kept" | Bundle + Q2 |
| CR-9 | Inputs used but not contracted (Org EXECUTION GATES, DEMAND set, Promethean irreversibility) | Accept: add them to the contract | Bundle |
| CR-10 | Each brief field needs one owner; synthesizer schema too wide | Accept, shaped by **Q3**: gates, missing evidence (with `asked_by` computed by script) and triggers come from expert outputs by script | Bundle + Q3 |
| CR-11 | Legacy filename discovery in live routing | Accept: live runs use only `moe_<RUNID>__<agent>.json`; AC-C1 names exact baseline files | Bundle |
| CR-12 | Firm/Qualified/Weak display scale misleads | Accept: remove it; show each expert's own confidence words plus a separate abstention status (removes machinery) | Bundle |
| CR-13 | Timing forwarded when its stage is Withheld | Accept as already handled (Adoption reads stage, basis and timing together, and its rule says a timing from a Withheld stage is not stage evidence; DR-6 shows it worked); fixture to Lab 11 | Bundle |
| CR-14 | F-9 depends on the expert listing missing intake | Accept: the script checks the required intake fields for the stage directly; `Undetermined` stays distinct from `Not ready` | Bundle |
| CR-15 | Vendor-only support can hide behind an irrelevant independent cite | Accept in part: AC-E2 requires each decisive headline to name its supporting passage and source class; the fixture goes to Lab 11 | Bundle |
| CR-16 | AC-C1 baselines not frozen; missing labels | Accept: name exact baseline files and Pack ID; add Diffusion TECHNOLOGY STAGE and Innovation ENTREPRENEURSHIP | Bundle |
| CR-17 | AC-F1 must use a routed expert; AC-F4 end-to-end | Accept | Bundle |
| DR-1 | Pack-bound ENTREPRENEURSHIP and routed Promethean WEIGHT flip on an identical packet | **Q4**: limitation W-1 extended, a Lab 11 rerun-stability check, versioned fixes considered in Lab 11; D-18 formally reopened | see Q4 |
| DR-2 | Landscape L1 drifts across reruns | Limitation W-1; Lab 11 | Q4 |
| DR-3 | Stable labels | Evidence only | — |
| DR-4 | Extraction defects | → CR-5 | Bundle |
| DR-5 | Format-only FAILs would force reruns | Accept: hard checks (validator, strict schema, pack discipline, recomputed COUNTS, unverified behind a headline, lane) trigger a rerun; caps and format are warnings shown in the brief | Bundle |
| DR-6 | Upstream reads worked | Evidence only | — |
| DR-7 | Synthesizer `asked_by` inflated; caution signals misused; S-2 is blind to meaning | **Q3** | see Q3 |
| DR-8 | Flags fired on the first case | **Q1** | see Q1 |
| DR-9 | F-4 age rule wrongly hits current standards | Accept: the age rule applies to market, capability and adoption cards; standards use a latest-version check | Bundle |
| DR-10 | Launch loop printed nothing, so duplicates were launched | Accept: the runner logs every launch to a file and checks the chat list before any relaunch; Lab 11 work list (I-16) | Bundle |
| DR-11 | G-3, G-4 and G-6 have no script | Lab 11 work list | Bundle |
| DR-12 | Conflict table built 5 of 8 pairs | Accept: the script builds every §4.2 row | Bundle |
| DR-13 | D-18 reopened; D-53 and D-65 not triggered | Records | — |
