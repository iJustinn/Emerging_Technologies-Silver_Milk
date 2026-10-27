# Silver-Milk Team Diffusion Agent (v1.0-team)

Team SubAgent 4 for MASY1-GC 1800, Team Lab 6. Created from `agents/_template` with `tools/new_agent.py`. The frozen core is unchanged.

| Path | Contents |
|---|---|
| `specialist_instructions.md` | v1.0-team instructions. Lineage tags [Z] [H] [L] [Y] [K] [T] |
| `agent_metadata.json` | Name, specialty, `1.0-team` |
| `cases/` | `primary`: GenAI incident summaries and resolution notes in internal IT service desks, fast follower, fixed packet E1–E8 (Nini Huang). `contrast_1`: identical but conservative (posture test). `contrast_2`: transfer test, AI coding agents at a U.S. regional bank, conservative, no cards (Justin Zhong) |
| `prompts/` | The exact packets sent to ChatGPT for v0.9 and v1.0. ZIP only, because they embed the frozen core |
| `responses/` | `team_v0_9__*` first team runs, including the preserved failure (T-38: `team_v0_9__primary` vs. `team_v0_9__contrast_1`). `team_v1_0__*` final runs. Each `.raw_copy.txt` is the clipboard exactly as copied |
| `records/` | `agent_record.md`, `contribution_lineage.md`, `test_log.md`, `team_inventory_and_version.md`, `specialist_instructions_v0.9.md`, `agent_metadata_v0.9.json`, `checks_v0_9.txt`, `final_checks_v1_0.txt`, `final_frozen_core_check.txt`, `chat_links.md` (ZIP only) |

Rebuild and check, from the scaffold root:

```bash
python3 tools/check_frozen_core.py
python3 tools/build_prompt.py --agent agents/team_diffusion_agent --case agents/team_diffusion_agent/cases/primary.json
python3 tools/validate_response.py agents/team_diffusion_agent/responses/team_v1_0__primary.json
python3 common_test_package/check_common.py agents/team_diffusion_agent/responses/team_v1_0__primary.json agents/team_diffusion_agent/cases/primary.json
python3 common_test_package/check_diffusion_lab06.py agents/team_diffusion_agent/responses/team_v1_0__primary.json --pair agents/team_diffusion_agent/responses/team_v1_0__contrast_1.json --posture-pair
```

`check_diffusion_lab06.py` covers the mechanical part of the team's §4 review:
- fixed labels and word caps at all three levels
- the stage rule (a stage above Early adopters needs a share; self-report wording fails; Early adopters without a share is flagged for a dated base case)
- the factor rule (Speculative is Neutral)
- the timing table (input = APPLICATION STAGE, Withheld → Early adopters row) and the matching `TIMING:` line
- POSTURE EFFECT without direction; the four Step 4 labels; one confidence value per level
- lane discipline and six handoffs
- `--pair`: identical Step 1 and Step 2 labels on the same technology, application and cards (never pair with the transfer case)
- `--posture-pair`: TIMING or PEER EVIDENCE ROLE differs, and POSTURE EFFECT differs

It does not replace the human swap test or claim tracing. Lane hits need a human read: a sentence that hands a decision to the Adoption Agent can contain a flagged verb.
