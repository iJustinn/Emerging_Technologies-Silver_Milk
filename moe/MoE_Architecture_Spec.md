# Silver-Milk MoE Architecture and Orchestration Specification

**Team Lab 10 · Version 1.0-design · ratified 2026-11-24 (D-70 to D-79)**

Team Silver Milk: Dian Li, Justin Zhong, Karuna Srivastava, Nini Huang, Yuanxiang Zhang

> Governing question: *How should seven bounded expert agents be orchestrated, challenged, and synthesized so the result is one accountable management recommendation rather than seven disconnected answers?*

**Version history**
- **0.9-design** (`records_v0_9/`) was critiqued by ChatGPT (`critique/`) and dry-run on the robotics case (`dry_run/`).
- **1.0-design** applies the team's dispositions (`critique/disposition.md`).
- **1.0 has not been re-run end to end** since those changes (W-6). Lab 11 is its first full test.

**Rule tags**
- `[S]` team choice in the Lab 10 session, answered by Justin Zhong (D-67 to D-79)
- `[R]` carried from an earlier decision or issue
- `[CR-n]` / `[DR-n]` the critic or dry-run finding that changed the rule

This is an **application-level** mixture of experts. Seven prompt-defined specialists run in ChatGPT, joined by local scripts and one human decision owner. It is not a neural-network MoE, and **no language model routes**.

## 0. The decision, the user, and what the system is for (Lab 1 brief)

- **Decision supported:** what to do now about one emerging technology, for one application, in one organization, within one time horizon. The answer is one of the Adoption Agent's actions:

  | Action | Lab 1 wording |
  |---|---|
  | Adopt | adopt |
  | Bounded experiment | pilot |
  | Proof of concept | pilot |
  | Monitor | monitor |
  | Defer | wait |
  | Reject for now | — |
  | Withheld — more evidence | — |

- **User (decision owner):** the role the intake names, from Lab 1's map: CFO (funding/ROI), CTO (skills/systems), business-unit leader (problem fit), Strategy team (long-term fit). The system informs this person and does not decide for them (Lab 1 §5).
- **Failure modes it must resist** (Lab 1 §4): hype amplification, vendor bias, context blindness, stale evidence.
- **Simplest design that keeps** evidence, specialist boundaries, visible conflict and human control:
  - fixed routing
  - one narrow LLM prose step after the experts
  - everything else done by script from validated expert text

## 1. Architecture (diagram: `architecture_diagram.svg`)

```
INTAKE (11 frozen fields + 10 org-readiness facts + decision owner) + SOURCE PACK (dated, classed, checked, frozen)
   │
WAVE 1 (parallel): Creation · Innovation · Promethean · Diffusion · Landscape
   │   CHECK each output (hard checks → rerun once) before anything is copied downstream          [CR-6]
WAVE 2: Adoption   ← verbatim label passages from Diffusion, Promethean, Landscape
   │   CHECK
WAVE 3: Org Adoption ← verbatim passages from Adoption (action, gates) and Landscape (execution gates)
   │   CHECK
BRIEF ASSEMBLY (script): panel · action→stage readiness test · every §4.2 conflict row · gates ·
                         missing evidence (with asked_by) · triggers · flags F-1…F-11
   │
SYNTHESIZER (1 ChatGPT run, narrow): TRADEOFFS prose + conflict explanations only,
                         every sentence carrying an exact quoted expert passage                    [S, CR-4]
   │   SUPPORT CHECK (script): quotes exist verbatim · action unchanged · rows answered
   ▼
any flag F-1…F-11? ── no (only Monitor/Defer/Reject/Withheld can get here) ──► "Accepted by rule"; owner may reopen [S]
   │ yes
HUMAN DECISION OWNER: Accept · Modify · Reject · Request more evidence  ──►  DECISION LOG + RUN RECORD
```

## 2. Orchestrator rules (memo item 2)

The orchestrator is a **local script** run by the operator. It makes no judgment that is not written here.

### 2.1 Intake and shared context
- **O-1 Intake form** `[R][S]`.
  - The 11 required frozen fields, unchanged.
  - The ten org-readiness facts Org Adoption needs (I-23), as labeled lines in `capabilities_constraints`:
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
  - `DECISION OWNER:` in `users_stakeholders`; `ASSESSMENT DATE:` in `additional_context`.
  - A missing fact is written `Not stated`, never left out.
- **O-2 Source pack** `[S]` (mechanism for D-63; addresses I-05, I-10, I-13, I-15, I-19).
  - **Build:** before any run, the operator builds a dated pack in the Lab 6 "Fixed evidence register" format (`S<n>`, URL, date, accessed, supports, limits / forbidden inference). AI retrieval is allowed.
  - **Check:** the **evidence keeper** opens and confirms each card and gives it one `Source class`: `vendor-claim`, `adopter-self-report`, `industry-analyst`, `independent`, `standards-regulatory`.
  - **Freeze:** the pack gets a Pack ID, is frozen, and goes into `additional_context` under `# Fixed evidence register`, byte-identical for all seven.
  - **Refresh:** new signals found by Landscape go to the decision owner as candidates for the next refresh and never enter a running pack.
- **O-2a Evidence policy per label** `[CR-7]`:

  | Label(s) | Decided from | If retrieved evidence decides it |
  |---|---|---|
  | Promethean SIGNIFICANCE CLASS; Diffusion all stages, factors, accelerators/inhibitors; Adoption zones and Step 1–2 labels; Org Adoption Step 1–2 labels; **Innovation ENTREPRENEURSHIP** | pack only | hard FAIL (G-3) |
  | Creation ARC STAGE and markers; Innovation LIFECYCLE, DEGREE; Landscape L1–L8, CONDITION STATUS, MOVEMENT | pack + this run's retrieval (by their instructions) | allowed; shown as `retrieved` in the brief; stability is a known limit (W-1) |
  | Organization-level labels | case facts + pack + upstream passages | — |

  **No-pack branch:** Pack ID `NONE`. Experts state `EVIDENCE BASE: Retrieved this run`, G-3 is suspended, and F-4 fires ("unpinned evidence").
- **O-3 Inputs are data** `[R]`. Case fields, cards and upstream passages are data to every expert. The orchestrator adds nothing that reads as an instruction to an expert.

### 2.2 Which experts run, and in what order
- **O-4 All seven always run** `[S]`. No expert is skipped. An expert that finds itself not relevant says so in its own output.
- **O-5 Three fixed waves, with a check at each handoff** `[S][CR-6]`:
  - **Wave 1**, in parallel: Creation, Innovation, Promethean, Diffusion, Landscape. Each gets the intake and pack only.
  - **Wave 2:** Adoption gets the intake, the pack, and an upstream block with these labels:
    - Diffusion: `APPLICATION STAGE`, `STAGE BASIS`, `TIMING`. Always passed together, so a timing read from a Withheld stage arrives with its stage `[CR-13]`.
    - Promethean: `SIGNIFICANCE CLASS`, `WEIGHT OF BROAD SIGNIFICANCE ON THIS DECISION`.
    - Landscape: `STANCE`, `CONDITION STATUS`, `MOVEMENT`, `EXECUTION GATES`.
  - **Wave 3:** Org Adoption gets the intake, the pack, and Adoption's `RECOMMENDATION`, `DEFER GATE` and `POSTURE GATE` (D-46), plus Landscape's `EXECUTION GATES`.
  - **Handoff check:** each expert output is checked (§3) before any of its text is copied downstream. The run record names the exact attempt used. If that attempt is later replaced, every downstream expert is rerun.
- **O-6 Upstream block** `[R][CR-5]`. Appended to `additional_context`, which has been the proven path since Lab 6:
  ```
  # Upstream expert reads (case-premise; produced by other Silver-Milk team specialists in MoE run <RUN ID>)
  - <Agent name> <version>: <CANONICAL LABEL>: <full source line, verbatim>
  ```
  - The script copies the **full source line**, never a paraphrase or summary.
  - An expert that FAILED is written `<Agent>: unavailable in this run (failed check)`.
- **O-7 Boundaries** `[R]`. Receivers type upstream lines `case-premise` and never re-derive them (Adoption and Org Adoption instructions; shown working in DR-6).

### 2.3 What each expert returns and how it is read (`expert_contract.json`)
- **O-8 Extraction rule per label** `[CR-5][DR-4]`. Each contracted label is read by these rules:
  - Keyed on **agent + label**, because names are shared and meanings differ (I-09, I-27).
  - Read from its **named field first**, then from anywhere in the output. A label can occur twice: Landscape's `MOVEMENT` appears in both L3 and Step 3.
  - Accepts the listed **aliases**: Diffusion `TIMING IMPLICATION`/`TIMING`; Promethean `WEIGHT`; Innovation "Innovation Agent"/"Innovation Classification Agent" (I-28).
  - Matches values **case-insensitively**: Org Adoption wrote `(bounded evaluation)`.
  - Keeps parenthesized values whole: `Indeterminate (Incremental | Breakthrough)`.
  - Reads Promethean's confidence as `CONFIDENCE AT LEAST <class>:`.
  - Keeps the full line beside the canonical label.
  - Live runs use only `moe_<RUNID>__<agent>.json`. Older patterns are read only by the replay/baseline loader `[CR-11]` (closes I-29).

### 2.4 Missing, failed and abstaining experts
- **O-9 Runner** `[R][DR-10]` (I-16, I-24):
  - Before every send, the runner reads the visible model and effort labels and aborts on a mismatch.
  - **Every launch is written to the run log before the next one.**
  - A run with no reply after 5 minutes may be relaunched once, and only after the project chat list shows no chat with that Run ID.
  - Empty, aborted and duplicate chats are all logged and kept.
- **O-10 Hard vs. soft checks** `[DR-5]`:
  - **Hard checks:** frozen validator, strict schema, pack discipline (O-2a), recomputed COUNTS, `unverified` behind a headline, lane. A hard FAIL means one rerun in a fresh chat with the identical packet; a second hard FAIL marks the expert **FAILED** and fires F-1.
  - **Soft checks:** word caps, label format, wording FLAGs. A soft FAIL is shown in the panel as a warning, with no rerun.
- **O-11 Failed upstream** `[P→S]`:
  - A failed Wave-1 expert: the downstream waves proceed and the upstream line says `unavailable`.
  - **Adoption FAILED:** the brief says `NO PROPOSED ACTION — Adoption expert unavailable` (F-1).
  - **Org Adoption FAILED:** `READINESS: not assessed` (F-1).
- **O-12 Abstention is an answer** `[R][CR-12]`. `Withheld`, `Indeterminate (…)`, `Undetermined — more evidence`, `Insufficient evidence` and a STANCE abstention are shown in the expert's own words, with a separate status `ABSTAINED` and what the expert says is missing. They are never filled in from another expert. **There is no translated confidence scale:** each expert's own confidence words are shown (§4.4).

### 2.5 Run record
- **O-13** `[R]`. Each MoE run gets a Run ID (`MOE-<case>-<n>`). The record lists:
  - intake file + SHA-256, Pack ID
  - per expert: version and tag, packet SHA-256, chat URL, raw reply, saved JSON, hard and soft check results, and which attempt was used downstream
  - runtime (mode, model, effort, project)
  - flags, the conflict table, the synthesizer packet and reply, the support check, and the human disposition with reason

## 3. Evidence and governance check (memo item 3, first half)

- **G-1** `[R]` (I-02, I-07). Per expert, run:
  - the frozen `validate_response.py`
  - a strict schema check
  - `check_common.py` (soft except the STATUS prefix)
  - the agent's own lab check script
- **G-2** `[R]` (I-22). Org Adoption COUNTS and verdict are recomputed from the D-lines. A mismatch is a hard FAIL.
- **G-3** `[CR-7]`. Pack discipline per O-2a: a pack-bound label resting only on `inspected-this-run` items is a hard FAIL. Suspended in the no-pack branch.
- **G-4** `[R]`. An `unverified` external item cited behind a headline label is a hard FAIL. `case-premise` and `inference` items marked unverified are allowed: they are not external evidence (DR-11).
- **G-5** `[CR-15]`. **Each decisive headline names its supporting passage and source class.** Decisive headlines: Adoption RECOMMENDATION, Org Adoption READINESS VERDICT, Landscape STANCE.
  - Pack cards carry their class.
  - Retrieved items are `retrieved, unclassified`, except Landscape's, which carry their own `SOURCE CLASS` (I-26).
  - No decisive headline may rest only on `vendor-claim` support.
- **G-6** `[R]`. Lane check. Each of these is a hard FAIL:
  - an action outside Adoption
  - a readiness verdict outside Org Adoption
  - any vendor, tool or model selection

### Flags (any flag keeps the brief Draft until the owner decides; §5)
Thresholds drafted by the operator and accepted by the team (D-78): 18-month card age (F-4), 5-minute reply timeout and one relaunch (O-9), one rerun on a hard FAIL (O-10), 120-word TRADEOFFS (§4.3). O-11 and the §5.3 fallback table are also operator-drafted and team-accepted.
| Flag | Fires when |
|---|---|
| F-1 | An expert is FAILED after the rerun, or Adoption or Org Adoption is unavailable |
| F-2 | An abstention on a decisive label: Adoption `RECOMMENDATION: Withheld — more evidence`, Org Adoption `Undetermined — more evidence`, or a Landscape STANCE abstention `[CR-8]` |
| F-3 | A **material disagreement**: two experts give incompatible readings of the *same question at the same scope* (§4.2 rows marked "same question"), or the synthesizer annotates a row E or J `[CR-2]` |
| F-4 | A stale or hype claim sits inside the intake or the pack (Landscape's `STALE/HYPE FLAG` cites a case location or a pack card, or writes `CORRECTION:`); a market, capability or adoption card older than 18 months behind a general label; a cited standard that is not its latest version (standards are exempt from the age rule `[DR-9]`); or Pack ID `NONE` |
| F-5 | The action is `Adopt`, or Adoption `CONSEQUENCE: Severe`, or Promethean writes its irreversibility guard |
| F-6 | The decision asks for, or the action requires, a vendor, tool or model choice. That choice is always the owner's procurement call (I-25) |
| F-7 | The support check fails (§4.3 S-2) |
| F-8 | Adoption `RECOMMENDATION CONFIDENCE: Low`, or Org Adoption `VERDICT CONFIDENCE: Low` |
| F-9 | **Computed from the intake, not from an expert's list:** when the stage the action executes (§4.5) is **beyond preparation**, any of org facts 2, 3, 4 or 6 (sponsor, coordinator/owner, environment, budget) is `Not stated` `[CR-14]`. (The 0.9 scope "beyond preparation" is kept; whether F-9 should also fire for no-start actions is an open question for Lab 11, W-L13.) |
| F-10 | **Same-stage readiness block** `[S]`: for an action that starts work (Adopt, Bounded experiment, Proof of concept), Org Adoption reads `Not ready` or `Undetermined — more evidence` (verdict), or `Blocked` or `Undetermined` (stage ladder), for the stage the action executes (§4.5). `Partially ready`, `Conditional` and `Not assessed` are shown in §2 of the brief without a flag (D-79) |
| F-11 | **Action starts work** `[S]`: the proposed action is Adopt, Bounded experiment or Proof of concept. Such a brief always goes to the owner, so only Monitor, Defer, Reject for now and Withheld briefs with no other flag are auto-accepted (D-79) |

## 4. Conflict resolution and synthesis (memo item 3)

### 4.1 Conflict annotations `[CR-2]`
Every row keeps both readings verbatim. Q/E/J are **annotations that explain a row, not verdicts**:
- `Q`: different questions; both can be true.
- `E`: the same question, read from different evidence.
- `J`: the same evidence, read differently.

What reaches the owner is decided by the flags (F-3, F-10, F-11), not by the annotation. The system never resolves a row.

### 4.2 Conflict rows the script always builds (all rows, every run) `[DR-12][CR-3]`
| Row | Readings placed side by side | Same question? | Source |
|---|---|---|---|
| Adoption ↔ Org Adoption | `RECOMMENDATION` vs. `READINESS VERDICT` *for the stage the action executes* | handled by **F-10** | I-21; dry run MOE-C-1 |
| Innovation ↔ Promethean | `DEGREE` (performance vs. baseline) vs. `SIGNIFICANCE CLASS` (barrier) | **No**: unlike measures, shown side by side | D-24, I-11 |
| Adoption ↔ Diffusion | `MATURITY ZONE` vs. `APPLICATION STAGE` | No | I-17 |
| Landscape ↔ Diffusion ↔ Adoption | `STANCE` (cadence) vs. `TIMING` (urgency) vs. action | No: never merged | I-31 |
| Creation ↔ Innovation | `ARC STAGE` vs. `LIFECYCLE` | No (distinct labels) | I-09 |
| Promethean ↔ Adoption | `WEIGHT` vs. action | No: weight sets attention, never direction (I-12) | I-12 |
| Any pack-bound label ↔ pack | the label vs. a retrieved basis | **Yes**: a hard FAIL already (G-3) | I-05 family |
| Lab 1 example | "disruption high/near-term" (Innovation DEGREE / Promethean class) vs. readiness `Not ready` | No: shown to leadership side by side | I-01 |

A row is marked "same question" (and fires F-3) only when two experts' passages answer one question at one scope. The script marks the pack row; the synthesizer may *propose* E/J for any row, which also fires F-3.

### 4.3 The synthesizer (narrowed) `[S][CR-4][CR-10][DR-7]`
- **S-1 What the script builds.** Copied or computed from validated outputs:
  - proposed action
  - readiness test and `PREPARE ONLY` wording (§4.5)
  - the panel, each expert's own confidence words and abstention status
  - all conflict rows
  - conditions and gates, quoted
  - **missing evidence, with `asked_by` computed from each expert's own `abstention_or_more_information_needed`**
  - reassessment triggers grouped by expert
  - flags
- **S-1a What ChatGPT writes, in one run** (`synthesizer_instructions.md`):
  - (a) `TRADEOFFS`, at most 120 words, plain language for the decision owner
  - (b) a one-sentence explanation and an optional E/J annotation for each conflict row

  **Every sentence carries a `support` field holding an exact passage copied from one named expert output.** Nothing else is generated.
- **S-2 Support check (script).** Any failure fires F-7, and the brief is issued script-only with the synthesizer text attached as *unchecked*. The checks:
  - every `support` passage occurs verbatim (whitespace-normalized) in the named expert's output
  - no date, URL or number that is absent from the outputs and the pack
  - every conflict row answered
  - the action echoed unchanged
- **May not:**
  - change the action
  - average, merge or score labels
  - give any overall confidence
  - add evidence
  - resolve a row
  - select a vendor
  - drop an abstention or dissent

  These are kept from 0.9.

### 4.4 Uncertainty display `[CR-12]`
Each expert's confidence is shown in its own words and on its own question:
- Promethean `CONFIDENCE AT LEAST` / `NOT HIGHER`
- Diffusion `STAGE CONFIDENCE` per level
- Adoption `RECOMMENDATION CONFIDENCE`
- Org Adoption `VERDICT CONFIDENCE`
- Landscape `CONFIDENCE`
- Creation and Innovation: text only

There is a separate status column: `OK`, `ABSTAINED`, `FAILED` or `unavailable`. There is **no overall confidence anywhere in the brief** (AC-S3).

### 4.5 Action-to-stage map and same-stage readiness `[S]`
| Adoption action | Stage the action executes | If Org Adoption is `Not ready` / `Undetermined` for that stage |
|---|---|---|
| Adopt | Routine operation | Headline: `<action> — PREPARE ONLY: do not start until <gap(s)> close (Org Adoption)`; F-10 (and F-11 always) |
| Bounded experiment · Proof of concept | Bounded evaluation | same |
| Monitor · Defer · Reject for now · Withheld | Preparation | No `PREPARE ONLY` (nothing starts); readiness is shown in §2 of the brief; no F-10 |

- The action category stays Adoption's (the qualify-only rule).
- The owner chooses: prepare only, start anyway (Modify, with a reason), or request more evidence.
- **Readiness is compared at the stage the action executes, not at the stage Org Adoption happened to be asked about.** If the two differ, the brief shows both, and the script reads Org Adoption's `STAGE LADDER` entry for the executed stage.

## 5. Final output and human authority (memo item 4)

### 5.1 Management decision brief (one page)
```
MOE DECISION BRIEF — <technology> for <application> at <organization> · Run <ID> · Pack <ID> · <date>
DECISION OWNER: <role>   HORIZON: <horizon>   STATUS: Draft (flags) | Accepted by rule (no flags) | Decided by owner
1 PROPOSED ACTION (Adoption, verbatim) [+ " — PREPARE ONLY: do not start until … (Org Adoption)" if F-10]
  Adoption's own confidence, in its words
2 BEFORE ACTING: readiness for the executed stage (Org Adoption) · execution gates (Landscape, Org Adoption) · defer/posture gates (Adoption) — quoted
3 THREE LEVELS, one attributed line each: ET generally · for this application · in this organization
4 EXPERT PANEL (7 rows): agent · version · headline labels · own confidence words · status · soft-check warnings
5 CONFLICT ROWS (all §4.2 rows): readings A/B verbatim · same question? · annotation · one-line explanation (with support)
6 TRADEOFFS (synthesizer, each sentence with its support passage)
7 MOST VALUABLE MISSING EVIDENCE (asked_by computed) · REASSESSMENT TRIGGERS by expert
8 EVIDENCE: pack cards cited with Source class · retrieved items cited · decisive headlines' supporting passages · stale/hype flag
9 FLAGS FIRED → owner review required? yes/no
10 HUMAN DISPOSITION: Accept | Modify (new action/conditions + reason) | Reject (reason) | Request more evidence (what) — name, date
```

### 5.2 Human authority
- **H-1 Review when flagged** `[S]`. If no flag F-1 to F-11 fires, the brief is issued `Accepted by rule`; the owner is notified and may reopen it at any time. Otherwise it stays `Draft` until the owner records a disposition.
  - **Team reason** (critic CR-1 rejected, D-74): flags catch everything that matters. F-11 (added in D-79 after review found a ready, unflagged trial would otherwise be auto-accepted) sends every action that starts work to the owner; F-5 and F-6 cover Adopt/Severe and vendor choice. Only no-start briefs (Monitor, Defer, Reject for now, Withheld) with no flag are auto-accepted, saving owner time.
  - W-2 measures this in Lab 11.
- **H-2 Dispositions.** The owner can:
  - **Accept** the action and conditions.
  - **Modify:** choose any action or change conditions. A reason is required, and the expert reading stays beside the human one.
  - **Reject** the brief as unusable, with a reason, which leads to a rerun or redesign.
  - **Request more evidence:** name the cards or facts wanted, which leads to a pack refresh and a new run.
- **H-3 Only the owner** `[R][S]`:
  - resolves material disagreements (F-3)
  - starts an action despite a readiness block (F-10)
  - changes the action category
  - selects a vendor, tool or model (F-6)
  - authorizes spending or anything hard to reverse
  - adds pack cards (with the evidence keeper's check)
- **H-4** The owner never edits an expert output or the synthesizer text. Disagreement goes in the disposition.

### 5.3 Fallback
| Failure | Behavior |
|---|---|
| Runtime unavailable, or model/effort label mismatch | No run; logged; nothing issued |
| Wave-1 expert FAILED | Downstream proceeds with `unavailable`; panel row `FAILED`; F-1 |
| Adoption FAILED | `NO PROPOSED ACTION`; panel and rows shown; F-1; owner decides |
| Org Adoption FAILED | `READINESS: not assessed`; F-1 |
| No pack possible | Pack ID `NONE`; experts retrieve; G-3 suspended; F-4 |
| Support check fails (F-7) | Script-only brief; synthesizer text attached as unchecked |
| Owner unavailable while flags are open | Draft; nothing proceeds by default |

### 5.4 Logs `[R]`
- The run record (O-13) goes to `records/moe_runs/`.
- Each disposition becomes one line in a decision ledger: run, owner, disposition, reason, date.
- Test failures go to `records/test_failure_log.md`; interface issues to `records/integration_issue_log.md`.

## 6. Team decision: who may decide what

| Question | Script | Synthesizer (ChatGPT) | Human decision owner |
|---|---|---|---|
| Which experts run, in what order | Fixed by O-4/O-5 | — | Changed only by a decision-log entry |
| Proposed action category | Copies Adoption's | Echoes it, cannot change it | Accepts or changes it (Modify, with a reason) |
| Readiness block for the executed stage | Adds `PREPARE ONLY` + F-10 (start actions only) | — | Prepare only / start anyway / more evidence |
| Conditions, gates, missing evidence, triggers | Quotes or computes them from experts | — | Accepts or edits them in the disposition |
| Conflicts | Builds every row; marks same-question rows | Explains each row; may annotate E/J (with support) | Resolves material disagreements |
| Evidence base | Freezes the pack | Adds nothing | Approves cards (evidence keeper checks them) |
| Vendor/tool selection | Never | Never | Always |
| Issue without review | Only a no-start action with no flag (H-1, F-11) | — | May reopen any time |

## 7. Known limits (tested, not hidden)
- **W-1 Rerun instability of general labels** `[DR-1][DR-2]`.
  - On a byte-identical packet, these flipped: Innovation `ENTREPRENEURSHIP` (pack-bound: Not established vs. Incumbent-led); Promethean `WEIGHT` (routed to Adoption: Moderate vs. Low) and its confidence; Landscape L1 (Developing vs. Emerging).
  - **A single MoE run cannot see this.** D-18's reopen condition is met.
  - Lab 11 adds a rerun-stability check (work list W-L6), and the team decides there whether to version Promethean or Innovation.
- **W-2** "Review when flagged" fired on the only dry-run case (F-4, F-6, F-9; F-10 and F-11 would also fire under 1.0). Lab 11 records the flag rate on all three cases.
- **W-3** The dry run was the first GPT-6.2 Sol run of the six older agents. They passed on single runs apart from two soft-format items (DR-5, DR-11).
- **W-4** Runs inside the MASY-1800 project can read the textbook PDF (I-13). Kept, for consistency with Labs 4–9.
- **W-5** Comparison across cases (I-32) sits outside a single run. Lab 11 compares briefs across the three cases by hand.
- **W-6** 1.0-design changed after the dry run (dispositions). **It has not been re-run end to end.** Lab 11's first run is its first test.
- **W-7** The robotics pack was retrieved and summarized by a Claude Code subagent on 2026-11-24. It is **pending the evidence keeper's (Karuna Srivastava's) check** before Lab 11 freezes case C.

## 8. Integration issues: disposition in this design
| Issue | Disposition |
|---|---|
| I-01 reconcile conflicting findings | **Closed (D-72):** never merged; all §4.2 rows shown; F-3/F-10 send material disagreements and readiness blocks to the owner; the Lab 1 example is a side-by-side row |
| I-02 validator passes empty/invalid output | **Closed (D-75):** hard/soft check layer G-1 to G-6 |
| I-03 scaffold not in workspace | **Closed (D-79):** the full scaffold ships in every package; the public repo keeps the `FROZEN CORE INTACT` output (D-12) |
| I-05, I-10, I-13, I-15, I-19 per-run retrieval drives general labels | **Mitigated (D-71):** frozen pack + evidence policy per label; residual W-1 (DR-1/DR-2) → Lab 11 |
| I-07 per-agent mechanical checks | **Closed (D-75):** the integration layer runs each agent's lab check (G-1) |
| I-09, I-27 shared label names | **Closed (D-75):** key on agent + label with per-label extraction rules (O-8) |
| I-11 DEGREE vs. SIGNIFICANCE CLASS | **Closed (D-72):** unlike measures side by side; never reconciled |
| I-12 route on WEIGHT, not class | **Closed (D-70):** only WEIGHT and class pass upstream, as case-premise; weight never sets direction (row) |
| I-13 project textbook access | The dry run used project MASY-1800 (D-68; the team declined the outside-project option). Kept for Lab 11 unless the team changes it (W-4) |
| I-16, I-24 runner timeouts and label checks | **Closed in design (O-9);** implementation → Lab 11 |
| I-17, I-31 Leading edge vs. stage; watch/timing/monitor words | **Closed (D-72):** side-by-side rows, never merged |
| I-18 Defer may resolve to Monitor | Open; the brief quotes Adoption's own gate text; Lab 11 test |
| I-21 Adoption vs. Org Adoption | **Closed (D-73):** action-to-stage map + `PREPARE ONLY` + F-10 |
| I-22 COUNTS recomputed | **Closed (D-75):** G-2 |
| I-23 org intake fields | **Closed (D-75):** O-1 intake form; F-9 computed from the intake |
| I-25 vendor selection has no owner | **Closed (D-72):** always the owner's procurement call (F-6) |
| I-26 two evidence taxonomies | **Closed for pack cards (D-71):** the evidence keeper assigns a Source class; retrieved non-Landscape items shown `retrieved, unclassified` |
| I-28 Innovation alias | **Closed (D-75):** both aliases accepted |
| I-29 run-file naming | **Closed (D-75):** one live pattern; the loader handles legacy patterns for baselines |
| I-30 PR reviews not recorded | Open; standard §6 unchanged; the Lab 10 PR asks the reviewer to approve on GitHub |
| I-32 comparison across cases | Open → Lab 11 by hand (W-5) |
| I-33 confidence/abstention formats | **Closed (D-75):** own words + separate abstention status; no translated scale |
