# Team Inventory and Version Record — Silver-Milk (Team Lab 2)

## Current approved agent

| Field | Value |
|---|---|
| Agent | Silver-Milk Team Chart Improvement Agent |
| Folder | `agents/team_chart_improvement_agent/` |
| Version | **1.0-team** (approved 2026-09-29) |
| Specialist instructions SHA-256 (v1.0) | `7a59a4368a0897ec1f3b7d74ee63e650b0325ad229cc1fb44617c28f31931e0f` |
| Previous version | 0.9-team, preserved as `records/specialist_instructions_v0.9.md` (SHA-256 `dcc9faf2…e3282`) |
| Frozen core | `FROZEN CORE INTACT` (`records/final_frozen_core_check.txt`) |
| Commit | Instructions committed at `ab4463a` (SHA-256 matches) |
| Sources merged | `agents/candidate_zhong` (0.2-student), `agents/candidate_srivastava` (0.2-student); see `records/contribution_lineage.md` |

## Outputs

| Run | Version | Case | Files | Result |
|---|---|---|---|---|
| Run 1 (preserved failure) | 0.9-team | Primary: NYT editor, sex vs. survival | `responses/run1_v0.9_preserved_failure/` | Validator passed; report falsely listed "transfer test incomplete" → instructions revised |
| Run 2 (final primary) | 1.0-team | Primary (same case) | `responses/run2_v1.0/`, copied to `responses/improved_chart.png` and `responses/primary_response.json` | Validator passed; all numbers correct; weakness fixed |
| Context contrast | 1.0-team | Same question, safety-board audience (`cases/contrast.json`) | `responses/contrast_v1.0/` | Validator passed; numbers correct; little change from primary (D-05); run at Light effort |
| Transfer test | 1.0-team (instructions unchanged) | Museum exhibit, class vs. survival (`cases/transfer_test.json`) | `responses/transfer_v1.0/` | Validator passed; all numbers correct; no carry-over from the primary case |
| Prompt packets | — | — | `records/run_messages/` | Exact text sent to ChatGPT Work for each run |

## Records in this folder

- `records/agent_record.md`: the Agent Record (template fields).
- `records/contribution_lineage.md`: which candidate or member supplied each adopted rule, why it was accepted, and later team revisions.
- `records/team_inventory_and_version.md`: this file.
- The team-wide records are in `team_records/` at the package root: the standard, the candidate comparison, the test and decision logs, and contributions.

## Remaining limitations

1. The children component of the "women and children first" claim is untested. This is by design: the agent does not start new analyses.
2. The swap test shows that output changes little when only the audience changes (decision D-05). Later ET specialists must show organization-level change.
3. The 18-element screen is qualitative. No reader or print-size test was run (the transfer chart kept a dark background).
4. ChatGPT Work file-write permission varies by session. In the transfer run, outputs were written to a fallback folder and copied in by the team; the JSON records this as a delivery `fail`.
5. The team selected Justin Zhong’s and Karuna Srivastava’s individual candidates as the two stronger candidates for this exercise and decided not to include the other three candidates.

## Semester agent inventory (for the final MoE system)

| # | Specialist | Lab | Status |
|---|---|---|---|
| — | Chart Improvement (practice) | 2 | **1.0-team approved** (this package) |
| 1 | Technology Creation | 3 | Not started |
| 2 | Innovation Classification | 4 | Not started |
| 3 | Promethean Classification | 5 | Not started |
| 4 | Diffusion | 6 | Not started |
| 5 | Adoption | 7 | Not started |
| 6 | Organizational Adoption | 8 | Not started |
| 7 | Technology Landscape | 9 | Not started |
