# Silver-Milk Team Creation Agent (v1.0-team)

Team SubAgent 1 for MASY1-GC 1800, Team Lab 3. Created from `agents/_template` with `tools/new_agent.py`. The frozen core is unchanged.

| Path | Contents |
|---|---|
| `specialist_instructions.md` | v1.0-team instructions. Lineage tags [Z] [H] [L] [Y] [T] |
| `agent_metadata.json` | Name, specialty, `1.0-team` |
| `cases/` | `primary` (AI coding agents, bank), `contrast_1` (same technology, startup), `contrast_2` (transfer test: text-to-image diffusion, small retailer, with supplied source cards) |
| `prompts/` | Exact packets sent to ChatGPT for v0.9 and v1.0 (ZIP only; they embed the frozen core) |
| `responses/` | `*_v0.9.*` first team runs, including the preserved failure; `*_v1.0.*` final runs. `.raw_copy.txt` is the clipboard exactly as copied |
| `records/` | `agent_record.md`, `contribution_lineage.md`, `test_log.md`, `team_inventory_and_version.md`, `specialist_instructions_v0.9.md` |

Rebuild and check, from the scaffold root:

```bash
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/team_creation_agent --case agents/team_creation_agent/cases/primary.json
python3 tools/validate_response.py agents/team_creation_agent/responses/primary_response_v1.0.json
python3 common_test_package/check_team_run.py agents/team_creation_agent/responses/primary_response_v1.0.json agents/team_creation_agent/cases/primary.json
```

`check_team_run.py` covers the mechanical part of the team's §4 review: labels, word cap, case leakage, A2 wording and consistency, evidence STATUS, lane, and handoffs. It does not replace the human swap test or claim tracing.
