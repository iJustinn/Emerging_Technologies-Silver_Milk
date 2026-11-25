# Silver-Milk MoE Architecture and Orchestration Specification

**Team Lab 10 · Version 0.9-design (draft for critique and dry run) · 2026-11-24**
Team Silver Milk: Dian Li, Justin Zhong, Karuna Srivastava, Nini Huang, Yuanxiang Zhang

> Governing question: *How should seven bounded expert agents be orchestrated, challenged, and synthesized so the result is one accountable management recommendation rather than seven disconnected answers?*

This is an **application-level** mixture of experts: seven prompt-defined specialists run in ChatGPT, joined by local scripts and one human decision owner. It is not a neural-network MoE, and no language model routes.

Each rule carries a tag:
- `[S]` a choice made by the team in the Lab 10 session (2026-11-24, answered by Justin Zhong)
- `[R]` a rule carried from an earlier decision (D-xx) or issue (I-xx)
- `[P]` proposed by the operator for the team to accept, change or reject at ratification

## 0. The decision, the user, and what the system is for (Lab 1 brief)

- **Decision supported:** what to do now about one emerging technology, for one application, in one organization, within one time horizon. The answer is one of the Adoption Agent's six actions plus `Withheld`.

  | Management action | Lab 1 wording |
  |---|---|
  | Adopt | adopt |
  | Bounded experiment | pilot |
  | Proof of concept | pilot |
  | Monitor | monitor |
  | Defer | wait |
  | Reject for now | — |

- **User (decision owner):** the leader the intake names. Lab 1's customer map lists CFO (funding/ROI), CTO (skills/systems), business-unit leader (problem fit) and Strategy team (long-term fit). The system informs this person; it does not decide for them (Lab 1 §5 "Preserve Human Judgment").
- **Failure modes it must resist** (Lab 1 §4): hype amplification, vendor bias, context blindness, stale evidence.
- **Simplest design that keeps:** evidence, specialist boundaries, visible conflict, and human control (memo). Fixed routing, no LLM router, one bounded LLM step after the experts.

## 1. Architecture (diagram: `architecture_diagram.svg`)

```
            ┌───────────────────────── INTAKE (human + script) ─────────────────────────┐
            │ 11 frozen fields + 10 org-readiness fields (I-23) + decision owner         │
            │ + SOURCE PACK (dated cards, SOURCE CLASS, checked, frozen)  → run record   │
            └──────────────────────────────────────┬─────────────────────────────────────┘
                                                   │ same packet base for all seven
   WAVE 1 (parallel) ┌──────────┬────────────┬─────┴──────┬───────────┬────────────┐
                     │ Creation │ Innovation │ Promethean │ Diffusion │ Landscape  │
                     └────┬─────┴─────┬──────┴─────┬──────┴─────┬─────┴──────┬─────┘
                          └───────────┴──── labels copied verbatim ─────────┘
   WAVE 2                       ┌──────────── Adoption ────────────┐  ← Diffusion stage+timing,
                                └──────────────┬───────────────────┘    Promethean weight, Landscape stance
   WAVE 3                       ┌──────── Organizational Adoption ─┐  ← Adoption action + gates
                                └──────────────┬───────────────────┘
                                               ▼
                     EVIDENCE / GOVERNANCE CHECK (scripts; per expert)
                     validator · strict schema · common + per-agent checks · recomputed counts
                     · pack-only general labels · flags F-1…F-9      → FAILED? rerun once → else mark missing
                                               ▼
                     CONFLICT TABLE (script) — known pairs, side by side, never averaged
                                               ▼
                     SYNTHESIZER = fixed template (script) + 1 bounded ChatGPT run
                     then SYNTHESIS CHECK (script): action unchanged, every qualification cites an expert
                                               ▼
                 any flag? ── no ──► brief issued "accepted by rule", owner may reopen
                     │ yes
                     ▼
                 HUMAN DECISION OWNER: Accept · Modify · Reject · Request more evidence
                                               ▼
                     DECISION LOG + RUN RECORD (every packet, raw reply, check, flag, disposition)
```

## 2. Orchestrator rules (memo item 2)

The orchestrator is a **local script** run by the operator. It makes no judgment that is not written below.

### 2.1 Intake
- **O-1 Intake form** `[R][S]`. The intake collects:
  - The 11 required frozen fields, unchanged.
  - The ten organizational-readiness facts Org Adoption needs (I-23), written as labeled lines inside `capabilities_constraints`:
    1. stage asked and scope
    2. sponsor and stop authority
    3. coordinator and operating owner
    4. approved environment and data permissions
    5. contracts covering this tool
    6. budget and protected hours
    7. review/fallback procedure and whether it was demonstrated
    8. governance reviews done
    9. skills evidence and training owner
    10. objections and unsanctioned use
  - `DECISION OWNER:` the role from Lab 1's map, put in `users_stakeholders`.
  - `ASSESSMENT DATE:` put in `additional_context`.

  A missing item is written `Not stated`, never left out.
- **O-2 Source pack** `[S]` (closes the mechanism question of D-63; addresses I-05, I-10, I-13, I-15, I-19):
  - **Build:** before any run, the operator builds a dated source pack, with AI retrieval allowed. Format is the Lab 6 "Fixed evidence register" (`S<n>`, URL, date, accessed date, supports, limits / forbidden inference).
  - **Check:** the evidence keeper opens each card, confirms it, and gives it one `SOURCE CLASS` from Landscape's vocabulary: `vendor-claim`, `adopter-self-report`, `industry-analyst`, `independent`, `standards-regulatory`. This closes I-26 for pack cards.
  - **Freeze:** the pack gets a Pack ID and is then frozen. It goes into `additional_context` under `# Fixed evidence register` for **all seven** experts, identical bytes.
  - **Coverage:** Promethean, Diffusion, Adoption and Org Adoption decide general labels from the pack only (their `EVIDENCE BASE` rules); Innovation does so for ENTREPRENEURSHIP. Creation and Landscape still retrieve, and their general-level stability is a known limit (W-1 below; Lab 11 decides whether to version them).
  - **Refresh:** new signals that Landscape finds are *not* added during a run. They go to the decision owner as candidates for the next pack refresh.
- **O-3 Prompt-injection guard** `[R]`. Every expert already treats case fields, cards and upstream reads as data. The orchestrator adds nothing that reads as an instruction to an expert.

### 2.2 Which experts run, and in what order
- **O-4 All seven always run** `[S]`. No expert is skipped for any question type. An expert that is not relevant says so in its own output; absence is never silent.
- **O-5 Three waves** `[S]`. The order is fixed:
  - **Wave 1**, in parallel: Creation, Innovation, Promethean, Diffusion, Landscape. Each gets the intake plus the pack, and nothing from any other expert.
  - **Wave 2:** Adoption gets the intake, the pack, and an `# Upstream expert reads` block (O-6) carrying these labels:
    - Diffusion: `APPLICATION STAGE`, `STAGE BASIS`, `TIMING`
    - Promethean: `SIGNIFICANCE CLASS`, `WEIGHT OF BROAD SIGNIFICANCE ON THIS DECISION`
    - Landscape: `STANCE`, `CONDITION STATUS`, `MOVEMENT`, `EXECUTION GATES`

    These are exactly what Adoption's `UPSTREAM READ` rule names (D-39, I-14), plus Landscape's stance, which it may cite.
  - **Wave 3:** Org Adoption gets the intake, the pack, and an upstream block with Adoption's `RECOMMENDATION`, `DEFER GATE` and `POSTURE GATE` (D-46, I-20), plus Landscape's `EXECUTION GATES`.
- **O-6 Upstream block format** `[P]`. The block is appended to `additional_context` (the path proven since Lab 6; extra top-level intake fields are allowed by the schema but untested):

  ```
  # Upstream expert reads (case-premise; produced by other Silver-Milk team specialists in MoE run <RUN ID>)
  - <Agent name> <version>: <LABEL>: <value copied verbatim from its output, up to the end of the line>
  ```

  The script copies label lines verbatim. It never paraphrases, summarizes or merges them. An upstream expert that failed is written `<Agent>: unavailable in this run (failed check)`.
- **O-7 Specialist boundaries** `[R]`. Upstream reads are typed `case-premise` by the receiving expert. No expert re-derives another's finding (Adoption, Org Adoption rules). The orchestrator never asks an expert to answer outside its own instructions.

### 2.3 What each expert returns (contract: `expert_contract.json`)
- **O-8** `[R]`. Each expert returns one frozen-schema JSON object. The orchestrator reads only the labels listed for that agent in `expert_contract.json`, keyed by **agent + label**, because names are shared and meanings differ (I-09, I-27). Innovation is accepted under both aliases (I-28). Saved file names follow `moe_<RUNID>__<agent>.json` (closes I-29 for new runs; the loader also accepts the three older patterns).

### 2.4 Missing, failed, and abstaining experts
- **O-9 Reply timeout and relaunch** `[R]` (I-16, I-24). The launcher reads the visible model and effort labels before each send and aborts on mismatch. A run with no reply after 5 minutes is relaunched once in a fresh chat. Every empty or aborted chat is logged.
- **O-10 Failed check** `[P]`. A run that fails the evidence/governance check (§3) is rerun once in a fresh chat with the identical packet. A second failure marks the expert **FAILED**. The brief shows it as missing, with the failed check named, and flag F-1 fires. Its saved outputs are kept.
- **O-11 Failed upstream** `[P]`. If a Wave-1 expert fails, Wave 2 proceeds, and the upstream block says the expert is unavailable. If **Adoption** fails, there is no proposed action: the brief says `NO PROPOSED ACTION — Adoption expert unavailable`, and flag F-1 forces human review. If Org Adoption fails, the action is shown with `READINESS: not assessed`.
- **O-12 Abstention is an answer** `[R]`. A `Withheld`, `Indeterminate`, `Undetermined — more evidence`, `Insufficient evidence` or STANCE abstention is shown as given, with what the expert says is missing. It is never filled in from another expert. It is mapped onto one display scale (§4.4, I-33).

### 2.5 Run record
- **O-13** `[R]`. Each MoE run gets a Run ID (`MOE-<case>-<n>`). The run record lists:
  - the intake file and its SHA-256
  - the Pack ID
  - for each expert: name, version, tag, packet SHA-256, chat URL, raw reply, saved JSON, and check results
  - the runtime (mode, model, effort label, project)
  - flags, the conflict table, the synthesizer packet and reply, the synthesis check, and the human disposition with reason

## 3. Evidence and governance check (memo item 3, first half)

- **G-1 The validator is necessary, not sufficient** `[R]` (I-02). The check runs, per expert:
  - the frozen `validate_response.py`
  - a strict schema check (`additionalProperties: false`, required item fields)
  - `check_common.py` (labels present, `STATUS:` on every evidence note, the six evidence types, HANDOFF lines, word caps)
  - the agent's own lab check script (`check_*_lab0N.py`, I-07)
- **G-2 Recompute, don't trust** `[R]` (I-22). Org Adoption's `COUNTS` and verdict are recomputed from its D-lines. A mismatch is a FAIL.
- **G-3 Pack discipline** `[P]`. For the four pack-bound experts:
  - The run must state `EVIDENCE BASE: Supplied cards`.
  - Every general-level `BASIS`/card citation must name a pack card.
  - A general label that cites only `STATUS: inspected-this-run` evidence is a FAIL (their R-2 rules).
- **G-4 Unverified never decides** `[R]`. An evidence item marked `STATUS: unverified` that is cited behind a headline label is a FAIL.
- **G-5 Source class in the brief** `[P]`. Pack cards carry their `SOURCE CLASS` from intake. Non-pack items are shown as `retrieved, unclassified` (I-26), except Landscape's, which carry their own `SOURCE CLASS`. No headline in the brief may rest only on `vendor-claim` items.
- **G-6 Lane check** `[R]`. These are FAILs:
  - an adopt, pilot or defer decision outside Adoption
  - a readiness verdict outside Org Adoption
  - a selection of vendor, tool or model by anyone

  Detected by keyword plus label checks; the checks from each lab's lane review are carried over.
- **G-7 What the synthesizer may not invent** `[S][P]`. See §4.3.

### Flags (each forces human review; §5)
| Flag | Fires when |
|---|---|
| F-1 | An expert is FAILED after the rerun, or Adoption or Org Adoption is unavailable |
| F-2 | An expert abstains on a **decisive** label: Adoption `RECOMMENDATION: Withheld`, Org Adoption `Undetermined — more evidence` for the stage Adoption recommends, or Landscape STANCE abstention |
| F-3 | A **material conflict** of type E or J (§4.1) |
| F-4 | A stale or hype claim sits *inside the intake or the source pack*: Landscape's `STALE/HYPE FLAG` cites a case location or a pack card, or writes `CORRECTION:`. Also fires when a pack card used for a general label is older than 18 months, or a cited standard is not its latest version |
| F-5 | Proposed action is `Adopt`, or Adoption `CONSEQUENCE: Severe`, or Promethean's irreversibility guard is written |
| F-6 | The decision asks for, or a brief implies, a vendor, tool or model selection (I-25): always the decision owner's procurement call |
| F-7 | The synthesis check fails: action category changed, a qualification without an expert citation, new evidence, or a dropped conflict |
| F-8 | `RECOMMENDATION CONFIDENCE: Low`, or any decisive label with confidence Low |
| F-9 | `INTAKE MISSING:` lists any of org fields 2, 3, 4 or 6 (sponsor, owner, environment, budget) for a stage beyond preparation |

## 4. Conflict resolution and synthesis (memo item 3)

### 4.1 Conflict types `[P]` (I-01)
The script fills one conflict-table row for each pair in §4.2 whose labels disagree. The synthesizer may propose a type; the script keeps both readings verbatim.
- **Q, different questions:** the labels answer different questions and both can be true. Example: Adoption `Bounded experiment` vs. Org Adoption `Not ready (Bounded evaluation)`: Adoption says what to prepare, Org Adoption says what must close first (I-21). Shown and explained; flag only if the human must choose between them.
- **E, evidence conflict:** the same question, read from different evidence. Example: Creation's retrieved markers vs. the pack. Shown; F-3 fires; the brief names the evidence that would settle it.
- **J, judgment conflict:** the same evidence, read differently. Example: Innovation `DEGREE: Breakthrough` vs. Promethean `SIGNIFICANCE CLASS: Incremental` on the same cards (I-11). Shown with each expert's reason; F-3 fires; never resolved by the system.

### 4.2 Known conflict pairs (from Labs 3–9 records and saved runs)
| Pair | Labels compared | Default type | Source |
|---|---|---|---|
| Adoption ↔ Org Adoption | `RECOMMENDATION` vs. `READINESS VERDICT (stage)` | Q (E/J if Org Adoption is Not ready for a stage *beyond* what Adoption recommends) | I-21; Lab 8 runs: Bounded experiment vs. Not ready on the same retailer |
| Innovation ↔ Promethean | `DEGREE` vs. `SIGNIFICANCE CLASS` | J if they point opposite ways; Q otherwise (performance vs. barrier) | D-24, I-11 |
| Adoption ↔ Diffusion | `MATURITY ZONE` / `Leading edge` vs. `APPLICATION STAGE` | Q | I-17 |
| Landscape ↔ Diffusion ↔ Adoption | `STANCE` (cadence) vs. `TIMING` (urgency) vs. `Monitor` (action) | Q: never merged | I-31 |
| Creation ↔ Innovation | `ARC STAGE` vs. `LIFECYCLE` | Q (labels kept distinct, I-09) | I-09 |
| Promethean ↔ Adoption | `WEIGHT` vs. action size | J if WEIGHT is High while the action is Reject/Monitor, or Low while the action is Adopt | I-12 (weight sets attention, never direction) |
| Any expert ↔ pack | a general label resting on non-pack evidence | E | I-05 family |
| Lab 1 example | "disruption high/near-term" (Innovation `DEGREE` / Promethean class) vs. readiness `Not ready` | Q: shown to leadership side by side | I-01 |

### 4.3 What the synthesizer may and may not do `[S]`
Adoption's `RECOMMENDATION` is the **proposed action**. The synthesizer qualifies it and never replaces it.

| May | May not |
|---|---|
| Copy the proposed action verbatim, with Adoption's confidence | Change the action category, or propose a more aggressive one |
| Attach **conditions** from named experts, each citing agent + label. Example: "prepare only; do not start the trial until Org Adoption D1 and D8 close" | Average, merge or re-score labels; compute a combined score |
| Add a `CAUTION SIGNAL:` when an expert's label points to a more cautious category, which triggers F-3 so the human can change the category | Add evidence, sources, numbers or dates that are not in an expert output or the pack |
| Propose a conflict type for each table row, with both readings quoted | Resolve a type-J conflict, or delete any conflict row |
| Explain tradeoffs in plain language for the decision owner | Select a vendor, tool or model (F-6) |
| List at most five `MOST VALUABLE MISSING EVIDENCE` items, deduplicated across experts, each tagged with the experts that asked | Report confidence higher than the lowest contributing decisive label |
| Restate each expert's reassessment triggers, grouped, each with its owner expert | Drop an expert's abstention or dissent |

- **S-1 Template first** `[S]`. The script fills the fixed brief (§5.1) from the extracted labels. One ChatGPT run (synthesizer instructions: `synthesizer_instructions.md`) writes only the `TRADEOFFS`, `CONDITIONS` and `CONFLICT EXPLANATION` text and proposes conflict types.
- **S-2 Synthesis check** `[S]`. The script compares the synthesizer reply against the template:
  - The action string is unchanged.
  - Every condition or caution names an agent and a label that exist in the expert outputs.
  - No URL or date appears that is absent from the outputs and the pack.
  - Every conflict row is present.

  Any failure is F-7, and the template-only brief is issued with the synthesizer text attached as *unchecked*.

### 4.4 One uncertainty display scale (I-33) `[P]`
The brief shows each expert's own confidence words, plus a mapped display value. Values are never averaged.

| Display | Creation | Innovation | Promethean | Diffusion | Adoption | Org Adoption | Landscape |
|---|---|---|---|---|---|---|---|
| **Firm** | — (no fixed label: shown as text) | — (text) | `CONFIDENCE AT LEAST … High` | `STAGE CONFIDENCE` application High | `RECOMMENDATION CONFIDENCE: High` | `VERDICT CONFIDENCE: High` | `CONFIDENCE: High` |
| **Qualified** | | | Moderate | Moderate | Moderate | Moderate | Moderate |
| **Weak** | | | Low | Low | Low | Low | Low |
| **Abstained** | "abstain/qualify" wording | `Withheld` | `Indeterminate (…)` (weighted as lower label) / `Withheld` | `Withheld` stage | `Withheld — more evidence` | `Undetermined — more evidence` | STANCE abstention / `Insufficient evidence` |

## 5. Final output and human authority (memo item 4)

### 5.1 Management decision brief (one page; template filled by script; text by synthesizer)
```
MOE DECISION BRIEF — <technology> for <application> at <organization>  · Run <ID> · Pack <ID> · <date>
DECISION OWNER: <role>          HORIZON: <time horizon>          STATUS: Draft | Accepted by rule | Decided by owner
1 PROPOSED ACTION (Adoption Agent): <category> — <one line>      CONFIDENCE: <Adoption's> (<display>)
2 CONDITIONS BEFORE ACTING: readiness verdict for the stage (Org Adoption) · execution gates (Landscape/Org Adoption) · defer/posture gates (Adoption)
  CAUTION SIGNALS (if any): <agent+label> → <more cautious reading>
3 THREE LEVELS: ET generally (Creation stage, Innovation lifecycle/degree, Promethean class+weight, Diffusion technology stage, Landscape position)
                · for this application · in this organization — one line each, attributed
4 EXPERT PANEL (7 rows): agent · version · headline label(s) · confidence (own words + display) · abstentions · status (OK / FAILED / unavailable)
5 CONFLICTS (never averaged): pair · reading A · reading B · type Q/E/J · what would settle it
6 TRADEOFFS: value vs. risk/governance, in plain language (synthesizer, checked)
7 MOST VALUABLE MISSING EVIDENCE (≤5) · REASSESSMENT TRIGGERS (owner expert, grouped)
8 EVIDENCE: pack cards cited (with SOURCE CLASS) · retrieved items cited · stale/hype flag
9 FLAGS FIRED: F-n … → human review required? yes/no
10 HUMAN DISPOSITION: Accept | Modify (new action/conditions + reason) | Reject (reason) | Request more evidence (what) — name, date
```

### 5.2 Human authority `[S]`
- **H-1 Review when flagged.** If no flag F-1 to F-9 fires, the brief is issued as `Accepted by rule`. The decision owner is notified and may reopen it at any time. If any flag fires, the brief stays `Draft` until the decision owner records a disposition.
- **H-2 The human's choices.** The decision owner can:
  - **Accept** the proposed action and conditions.
  - **Modify** them: choose any management action (Adopt, Bounded experiment, Proof of concept, Monitor, Defer, Reject for now) or change conditions. A reason is required, and the brief keeps the expert reading beside the human one.
  - **Reject** the brief as unusable: a reason is required, and it triggers a rerun or redesign.
  - **Request more evidence:** name the cards or intake facts wanted. This leads to a pack refresh and a new MoE run with a new Run ID.
- **H-3 Only the human** `[R][S]`:
  - resolves type-J conflicts
  - chooses a different action category
  - selects a vendor, tool or model (I-25, F-6)
  - authorizes spending, a trial start, or anything hard to reverse
  - adds a card to the pack
- **H-4 What the human may not do in the record:** edit an expert output or the synthesizer text. A disagreement is written in the disposition, not by changing what an expert said.

### 5.3 Fallback `[P]`
| Failure | System behavior |
|---|---|
| Runtime unavailable, or model/effort label mismatch | No run; logged; nothing issued |
| One Wave-1 expert FAILED | Brief issued with that row `FAILED`; F-1 |
| Adoption FAILED | `NO PROPOSED ACTION`; panel and conflicts shown; F-1, owner decides |
| Org Adoption FAILED | Action shown with `READINESS: not assessed`; F-1 |
| No source pack possible | Pack ID `NONE`; experts state `EVIDENCE BASE: Retrieved this run`; F-4 fires (unpinned evidence); brief says general labels may vary across reruns |
| Synthesizer fails or F-7 | Template-only brief; synthesizer text attached as unchecked |
| Owner unavailable while flags are open | Brief stays Draft; no action proceeds by default |

### 5.4 What is logged `[R]`
The run record (O-13) goes into `records/moe_runs/`. Each disposition becomes one line in a decision ledger: run, owner, disposition, reason, date. Lab 11 failures go to `records/test_failure_log.md`, and interface issues to `records/integration_issue_log.md`.

## 6. Team decision: who may decide what

| Question | Synthesizer | Human decision owner |
|---|---|---|
| Which experts run, in what order | Neither: fixed by O-4/O-5 | Neither: changed only by a team decision-log entry |
| Proposed action category | Copies Adoption's verbatim | Accepts or changes it (Modify) |
| Conditions and cautions | Attaches them, each citing an expert | Accepts, edits or removes them, with a reason |
| Conflicts | Proposes a type; may not resolve or delete | Resolves type J; may accept type-Q explanations |
| Evidence base | May not add anything | Approves pack cards and refreshes |
| Vendor/tool selection | Never | Always (procurement) |
| Issue without review | — | Only when no flag fires (H-1) |

## 7. Known limits of this design (to test, not hide)
- **W-1** Creation and Landscape still retrieve per run, so their general labels can vary (I-05). The pack fixes the other four, plus ENTREPRENEURSHIP.
- **W-2** "Review when flagged" is only as good as the flags. If flags fire on almost every case, it collapses into always-review. The dry run measures how often they fire.
- **W-3** Six of the seven agents were promoted on GPT-6.1 Sol or GPT-6. The dry run is their first run on GPT-6.2 Sol (D-55, audit "Not checked").
- **W-4** Runs inside the MASY-1800 project can read the textbook PDF (I-13). It is kept, for consistency with Labs 4–9.
- **W-5** One cross-case comparison (I-32) is outside a single MoE run. Lab 11 compares briefs across the three test cases by hand.
