# Silver-Milk Team Innovation Classification Agent (v1.1-team)

Team SubAgent 2 for MASY1-GC 1800, Team Lab 4. Created from `agents/_template` with `tools/new_agent.py`. The frozen core is unchanged.

| Path | Contents |
|---|---|
| `specialist_instructions.md` | v1.1-team instructions. Lineage tags [Z] [H] [L] [Y] [K] [T] |
| `agent_metadata.json` | Name, specialty, `1.1-team` |
| `cases/` | `primary`: bounded agentic AI for IT tickets at an hour-billed outsourced IT service company (the borderline case). `contrast_1`: the same technology and application at an internal cost-center IT department. `contrast_2`: transfer test, an LLM reply-drafting demo at PivotDesk, revenue mix unknown, with supplied source cards |
| `prompts/` | The exact packets sent to ChatGPT for v0.9, v1.0, and v1.1. ZIP only, because they embed the frozen core |
| `responses/` | `*_v0_9.*` first team runs, including the preserved failure (T-19). `*_v1_0.*` the first revision, where the failure persisted (T-20). `*_v1_1.*` final runs. Each `.raw_copy.txt` is the clipboard exactly as copied |
| `records/` | `agent_record.md`, `contribution_lineage.md`, `test_log.md`, `team_inventory_and_version.md`, `specialist_instructions_v0.9.md`, `specialist_instructions_v1.0.md`, earlier metadata, `final_checks_v1_1.txt`, `final_frozen_core_check.txt` |

Rebuild and check, from the scaffold root:

```bash
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/team_innovation_classification_agent --case agents/team_innovation_classification_agent/cases/primary.json
python3 tools/validate_response.py agents/team_innovation_classification_agent/responses/primary_response_v1_1.json
python3 common_test_package/check_common.py agents/team_innovation_classification_agent/responses/primary_response_v1_1.json agents/team_innovation_classification_agent/cases/primary.json --cap 200
python3 common_test_package/check_innovation_lab04.py agents/team_innovation_classification_agent/responses/contrast_1_response_v1_1.json --pair agents/team_innovation_classification_agent/responses/primary_response_v1_1.json --same-application
```

`check_innovation_lab04.py` covers the mechanical part of the team's §4 review:
- fixed labels and word caps
- general-level stability across a pair on the same technology
- application-level stability across a pair with the same application
- the provisional/withheld rule
- source STATUS honesty
- lane discipline
- handoffs

It does not replace the human swap test or claim tracing.
