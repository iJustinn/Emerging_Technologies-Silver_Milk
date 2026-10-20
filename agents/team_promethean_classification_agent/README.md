# Silver-Milk Team Promethean Classification Agent (v1.0-team)

Team SubAgent 3 for MASY1-GC 1800, Team Lab 5. Created from `agents/_template` with `tools/new_agent.py`. The frozen core is unchanged.

| Path | Contents |
|---|---|
| `specialist_instructions.md` | v1.0-team instructions. Lineage tags [Z] [H] [L] [Y] [K] [T] |
| `agent_metadata.json` | Name, specialty, `1.0-team` |
| `cases/` | `primary`: text-to-image diffusion for internal concept images at an aggressive small homeware retailer, with five supplied source cards. `contrast_1`: identical but conservative (posture test). `contrast_2`: transfer test, generative AI foundation models at a global consulting firm, no cards. `hype`: the primary plus an investor "next electricity" claim |
| `prompts/` | The exact packets sent to ChatGPT for v0.9 and v1.0. ZIP only, because they embed the frozen core |
| `responses/` | `*_v0_9.*` first team runs, including the preserved failure (T-29: `hype_response_v0_9` vs. `primary_response_v0_9`). `*_v1_0.*` final runs. Each `.raw_copy.txt` is the clipboard exactly as copied |
| `records/` | `agent_record.md`, `contribution_lineage.md`, `test_log.md`, `team_inventory_and_version.md`, `specialist_instructions_v0.9.md`, `agent_metadata_v0.9.json`, `checks_v0_9.txt`, `final_checks_v1_0.txt`, `final_frozen_core_check.txt`, `chat_links.md` (ZIP only) |

Rebuild and check, from the scaffold root:

```bash
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/team_promethean_classification_agent --case agents/team_promethean_classification_agent/cases/primary.json
python3 tools/validate_response.py agents/team_promethean_classification_agent/responses/primary_response_v1_0.json
python3 common_test_package/check_common.py agents/team_promethean_classification_agent/responses/primary_response_v1_0.json agents/team_promethean_classification_agent/cases/primary.json
python3 common_test_package/check_promethean_lab05.py agents/team_promethean_classification_agent/responses/primary_response_v1_0.json --pair agents/team_promethean_classification_agent/responses/contrast_1_response_v1_0.json --posture-pair
```

`check_promethean_lab05.py` covers the mechanical part of the team's §4 review:
- fixed labels and word caps
- the gate and ceiling self-check
- two-direction confidence
- the weight table
- POSTURE EFFECT without direction
- the four competing-view labels
- lane discipline and six handoffs
- `--pair`: identical Step 1 labels on the same technology and cards (never pair with the transfer case)
- `--posture-pair`: same weight, different POSTURE EFFECT

It does not replace the human swap test or claim tracing.
