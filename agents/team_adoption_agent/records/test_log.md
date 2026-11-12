# Test log (Lab 7)

**Runtime:** ChatGPT web in Ego Lite; Work mode; composer "GPT-6.1 Sol Light"; fresh chat per run in project MASY-1800 (instructions empty; Memory Default; Space access Enabled, read 2026-11-03). Source `1800-Textbook.pdf` (read 2026-11-03). **The team chose Light on the understanding it was the lowest stop; the operator then found None and Minimal listed below it.** Light was retained pending team review (D-37). Packet attached, message `[Run <ID>] …`. Map: `common_test_package/runmap.txt` (ZIP).

**Handling incidents:** the first two collection attempts failed (empty clipboard, then the user prompt copied); the third garbled non-ASCII characters through a shell locale. These failures arose in the Claude Code collection script; the failed copies were discarded, and the same replies were re-copied under UTF-8. The team's v0.9 review was re-run on the clean copies.

| Test | Result |
|---|---|
| T-48 v0.9, 4 cases | Valid. Bounded experiment / Defer / Defer / Reject for now. Weaknesses: card types drift; transfer Severe from excluded harm; MODIFIER case |
| T-49 v1.0, 4 cases | Valid. Same recommendations. 334 mechanical checks pass, 0 fail (`final_checks_v1_0.txt`) |

**Human §4 review (v1.0):** swap test passes (posture alone moves the action, through a named gate; Step 1 and 2 labels identical). Consequence test passes (Reject for now). Prerequisites stay conditions; no readiness verdict; tool choice is routed to Landscape. Transfer passes with unchanged instructions. Weaknesses W-1 to W-5 are in `agent_record.md`.
