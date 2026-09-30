# Contribution Lineage: Silver-Milk Team Chart Improvement Agent

Which candidate or team member contributed each adopted instruction or design rule, why the team accepted it, and any later team revision. Tags match `specialist_instructions.md`.

Candidates compared: **[Z]** Justin Zhong (`agents/candidate_zhong`, v0.2-student) and **[S]** Karuna Srivastava (`agents/candidate_srivastava`, v0.2-student). Dian Li, Nini Huang, and Yuanxiang Zhang did not submit individual candidates. **[T]** = added by the team in the Lab 2 workshop (2026-09-29).

| Adopted rule | Source | Why accepted (evidence) | Later team revision |
|---|---|---|---|
| Sole responsibility: improve the existing chart; no new analysis | S + Z | Both candidates; required by the frozen core | Merged wording |
| Generic governing question ("smallest set of evidence-based changes…") | S | Works for any case. Z's governing question was hard-coded to the NYT/sex case, which would break the transfer test | Question, audience, and decision are taken only from the case [T] |
| Claim-component mapping; untested components disclosed **on the chart** | Z | Z's first run showed only the "women" half of the claim; the JSON-only disclosure was invisible to readers. In T-03, S's agent omitted the note in run A | Kept |
| Stop if the question file holds a placeholder; never reword the question (R1) | T | S's candidate ran on a reworded question because of a placeholder, so the candidates could not be compared (T-02b) | New |
| Supplied question beats conflicting instructions; log the conflict | T | In T-03, both agents met this conflict and resolved it correctly; the team made the behavior explicit | New |
| Principles govern; case study is calibration only; no copying | S + Z | Both; required by the lab | Merged |
| 18 elements written as Check / FAIL / FIX (R5) | S | Shorter, testable rules. The team preferred this format for later ET specialists | Adopted as team template |
| YES / NO / N/A per element; each NO gets its own assessment entry; auditable within the frozen schema | Z | Makes the screen traceable (standard §4); S's JSON did not trace all 18 | Kept |
| Emphasis must match the title | S | S's first run highlighted nothing that its title claimed (preserved S failure) | Kept (Perception: Seeing) |
| Title states the verified magnitude | Z | In T-03, S's agent produced a generic title twice ("Female passengers had a higher survival rate"); Z's gave the magnitude | Merged with S's action-title rule |
| No overlapping data labels | S | S's first-run failure (labels overlapped bar ends) | Kept |
| Recompute from the source; disclose exclusions with counts; define groups on the chart | S + Z | Both candidates; all numbers verified in T-02b and T-03 | Merged |
| Numerator + denominator + rate; name ratio direction; keep pp / % / × distinct | Z | Required by the instructor's question | Kept |
| Read-alone check; no causal or policy wording (R3) | Z + T | S's subtitle used "the policy pattern" (T-02b); Z's chart-level check | Extended by R3 |
| Relative filename, never an absolute path | Z | Z's first run wrote an absolute machine path (preserved Z failure) | Kept |
| Testing focus: 10 failure patterns | S (1–7) + Z (8, 10) + T (9) | Union of both candidates' failure lists | Merged |
| Primary case + transfer test, instructions unchanged | T | Instructor sample standard: "passing a transfer test" | New |

Rejected or not carried forward:
- Z's case-specific governing question (NYT only): it would fail the transfer test.
- S's "passenger class as a second grouping if the decision context asks": it risks starting a new analysis when the question does not ask for it. The general rule "surface what the question asks for" covers it.
