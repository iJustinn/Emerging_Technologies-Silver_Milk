# Integration Issue Log

| ID | Raised | Issue | Affects | Status | Resolution / owner |
|---|---|---|---|---|---|
| I-01 | Lab 1 | How the system reconciles conflicting specialist findings (e.g., high disruption vs. low readiness): weighted merge, escalate to humans, or show the disagreement to leadership | MoE synthesis, confidence reporting | Open (deliberately), for Lab 10 | Collect real disagreements from Labs 3–9 |
| I-02 | Lab 2 | Validator passes structurally valid but empty or invalid outputs (T-02). The MoE layer cannot trust `VALIDATION PASSED` alone | All specialists → MoE | Mitigated by human review (standard §4) | Lab 10: decide whether the integration layer adds its own checks |
| I-03 | Lab 2 | ET scaffold not yet in team workspace | All | Blocker | See `scaffold/README.md` |
| I-04 | Lab 2 | Repo is public, but promotion requires committing the scaffold (instructor material) | Promotion procedure | **Still open after Lab 3.** Workaround: the scaffold and prompt packets are kept out of the repo; the full package is the Brightspace ZIP | Make the repo private or get instructor approval (owner: Justin) |
| I-05 | Lab 3 | The general level of one technology still varies between runs (economic-enabler evidence, predecessor dates; W-1, W-2), even after v1.0 | All specialists → MoE | Open, for Lab 10 | Hold one reconciled general record per technology (Justin's I-2 recommendation from Assignment 2); specialists read it rather than re-deriving it |
| I-06 | Lab 3 | Experiment design ([Y]) was removed from Creation and sent to the Adoption Agent; nothing owns it until Lab 7 | Adoption (Lab 7), MoE routing | Open | Lab 7: Adoption Agent owns experiment design (hypothesis, comparator, owner, stop conditions) |
| I-07 | Lab 3 | `check_team_run.py` automates the mechanical §4 checks for the Creation format; other specialists will need their own | All specialists, Lab 10 | Open | Reuse the pattern in Labs 4–9; decide in Lab 10 whether the integration layer runs it |
