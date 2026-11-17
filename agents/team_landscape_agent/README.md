# Silver-Milk Team Landscape Agent (Team SubAgent 7), 1.1-team

The team's current-intelligence expert. It places a technology in a dated landscape (L1–L8, each with a basis), separates the few signals that matter to one organization from the broad market, keeps execution gates apart from landscape signals, sets a monitoring stance by table, and names typed, owned triggers and one dated stale/hype claim. It never recommends adoption and never selects a vendor.

- `specialist_instructions.md`, `agent_metadata.json` — the team version (1.1-team).
- `cases/` — primary and contrast_1 (Dian Li's concept-board pair), contrast_2 (transfer: Yuanxiang Zhang's bank information support), contrast_3 (hype: Justin Zhong's bank plus board memo).
- `responses/` — all twelve team runs (v0.9, v1.0, v1.1), raw copies and JSON, unedited.
- `records/` — agent record, test log, contribution lineage, seven-agent integration audit, inventory and version, checks, preserved v0.9 and v1.0 instructions, frozen-core check.

Build a packet: `python3 tools/build_prompt.py --agent agents/team_landscape_agent --case agents/team_landscape_agent/cases/primary.json --out <packet>.txt`.
