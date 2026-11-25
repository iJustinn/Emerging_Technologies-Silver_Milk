# Integration work list for Team Lab 11 (from 1.0-design)

The memo's post-class rule: "prepare the integration work list … do not begin an unlimited hidden coding sprint." Nothing below is built in Lab 10. The Lab 10 dry-run helpers (`moe_labels.py`, `moe_upstream.py`, `moe_brief.py`, `moe_synth_check.py`) were written to run the approved dry run against 0.9-design. They are a starting point, **not** the 1.0 orchestrator.

Owners are named only where the team already assigned the role. Everything else is assigned at the start of Lab 11.

| ID | Item | Spec rule / AC | Before or in Lab 11 | Owner |
|---|---|---|---|---|
| W-L1 | Assemble the case A and case B intakes and packs from existing, already-checked material only; fix the Pack IDs | Test plan §1 | Before (posting window) | Nini Huang (test-plan owner) with the evidence keeper |
| W-L2 | Check robotics pack cards S1–S12 against their pages; confirm or correct each Source class | O-2, W-7 | Before | Karuna Srivastava (evidence keeper) |
| W-L3 | Orchestrator script: three waves, hard/soft checks at each handoff, verbatim upstream lines from the attempt used, rerun of downstream experts if an attempt is replaced, run record | O-4 to O-13 | In | Lab 11 integrator |
| W-L4 | Runner: write every launch to the log before the next one; check the project chat list for the Run ID before any relaunch; configurable upload wait; 5-minute reply timeout; abort on a model/effort label mismatch | O-9, DR-10, I-16, I-24 | In | Lab 11 integrator |
| W-L5 | Brief builder: action-to-stage map and F-10 with `PREPARE ONLY`; all §4.2 rows; `asked_by` computed from abstention lists; flags F-1 to F-10 (F-9 from the intake); no overall confidence | §3, §4.2, §4.5, §5.1 | In | Lab 11 integrator |
| W-L6 | **Rerun-stability check (AC-C4)** on case A. Then the team decides whether to version Promethean (WEIGHT) and/or Innovation (ENTREPRENEURSHIP), since D-18 is reopened | W-1, DR-1, D-77 | In | Team decision |
| W-L7 | Support check for the 1.0 synthesizer schema: verbatim passage match, no new dates, numbers or URLs, rows answered, action echo | S-2, AC-E3 | In | Lab 11 integrator |
| W-L8 | Offline fixtures: AC-F1 (routed Diffusion FAILED), AC-F2, AC-F3 (passage altered so a condition is reversed), AC-H4 (dry-run outputs), CR-15 (vendor claim plus an irrelevant independent cite) | Test plan | In | Test lead |
| W-L9 | Scripts for G-3 (pack discipline per label), G-4 (external `unverified` behind a headline), G-5 (supporting passage and class for decisive headlines), G-6 (lane) | §3, DR-11 | In | Lab 11 integrator |
| W-L10 | `team_tools/check_org_adoption_lab08.py`: match the stage case-insensitively. This is a tool fix, not an agent change; the agent is unchanged | DR-4(d) | In | Lab 11 integrator |
| W-L11 | `records/moe_runs/` and the disposition ledger | §5.4 | In | Evidence keeper |
| W-L12 | Re-confirm the MASY-1800 project settings (sources, instructions, memory) before the frozen runs | Runtime, I-13 | In | Operator |

**Open issues carried into Lab 11:** I-18 (Defer may resolve to Monitor), I-30 (PR reviews not recorded), I-32 (comparison across cases, done by hand), and W-1 to W-7 in the spec.
