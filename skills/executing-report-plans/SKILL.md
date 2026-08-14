---
name: executing-report-plans
description: Use when a new Evidencecraft Run explicitly selects Inline Execution or an incomplete Run already freezes `executing-report-plans`.
---

# Executing Report Plans

Execute one confirmed Report Plan faithfully in the Main Agent's context. Own the sequential run, evidence capture, recovery, and fresh verification; do not reinterpret analysis semantics or issue the independent review verdict.

## Admit only a sequential run

Read the exact current Plan before doing analysis work. Also inspect the confirmed Analysis Brief, every referenced Source Profile and Metric Definition, the requested period/as-of, relevant prior progress, and the actual run files.

Read and apply [the shared language contract](../using-evidencecraft/references/language-and-localization-contract.md). Recover an existing Run from progress first; record inferred legacy fields there without rewriting old artifacts.

Read and apply [the common Executor output contract](references/executor-output-contract.md). This Skill adds sequential ownership and dependency-ordered execution; it does not alter the shared output, evidence, verification, or review-handoff interface.

Proceed only when all are true:

- the Plan is confirmed and still current for its Brief, source uses, metric meanings, report interface, and capabilities;
- the current execution handoff explicitly selected Inline for a new Run, or existing progress freezes `executing-report-plans` or legacy `sequential`;
- the exact user selection statement is available for a new Run; legacy progress may instead carry an appended compatibility record with selection source `legacy progress` and unavailable time;
- no Subagent-Driven Executor owns this Run and no other writer is changing its files;
- the Plan identifies the run workspace, Work Packages, outputs, reader-report contract, distinct draft/final paths, checks, stop conditions, and Review Package manifest.

Route instead when:

| Observed state | Action |
|---|---|
| This Run selected Subagent-Driven | Use `subagent-driven-reporting`; do not start an Inline writer. |
| No Run selection exists | Return to `using-evidencecraft` for the two-option execution handoff. |
| Plan is absent, unconfirmed, or has an execution-blocking interface gap | Return the exact gap to `writing-report-plans`. |
| Intended use, audience, question, or scope changed | Return to `framing-analysis`. |
| Source grain, keys, time, authority, lineage, or use-specific fitness changed | Return the exact use to `profiling-evidence`. |
| Metric population, formula, grain, time, deduplication, aggregation, missing-data rule, or source mapping changed | Return the exact metric to `defining-metrics`. |
| Only `interaction_language` changed | Continue the same lifecycle state and use the new language for user interaction. |
| `artifact_language` changed from the confirmed Plan | Stop and return to `writing-report-plans` to revise and reconfirm the report interface; do not rerun unaffected profiling, metric definition, or analysis. |
| Only current-period records or computed values changed under current semantics | Continue with this Executor. |
| The draft and evidence package are complete and need judgment | Use `reviewing-analysis`. |

Never run both Executors for the same active Run. Before any Package starts, an explicit reselection may replace the mode in that otherwise empty Run. After work starts, a mode change stops current writes and creates a new Run ID; preserve the old Run as history. Do not revise an otherwise current Plan merely to change execution mode.

## Initialize or recover the run

Use [the progress template](assets/progress-template.md), [the evidence-log template](assets/evidence-log-template.md), and, when sealing, [the Review Package manifest template](assets/review-package-template.md). Instantiate them in the Plan's run workspace; treat English headings and labels—including “Report Run Progress”, “Evidence Log”, and “Review Package Manifest”—as semantic slots, render all user-visible content and artifact-type phrases in `artifact_language`, preserve only exact Skill names and the recorded canonical or source-exact exceptions, and remove all template comments. Never edit the Skill assets in place.

For a new run:

1. Record the Plan, semantic dependency paths, period/as-of, `executing-report-plans`, the exact user selection and time, explicit parallel authorization as `none`, the frozen language contract, output paths, and every Work Package.
2. Create only the directories and empty records the Plan authorizes.
3. Mark the first dependency-ready Package `IN PROGRESS`; leave the rest `NOT STARTED` or `BLOCKED BY <id>`.

For a legacy Run whose progress says `Executor: sequential`, treat it as this Executor without reprompting. Append, without rewriting history: canonical Executor `executing-report-plans`, selection source `legacy progress`, selection time `unavailable (legacy)`, and parallel authorization `none` unless exact prior evidence says otherwise.

For a resumed run, treat the filesystem and fresh checks as authoritative, not status prose:

1. Read progress, evidence log, Package outputs, draft, and review-package files.
2. Match every claimed completed output to its exact path, expected interface, provenance, and current content hash or other durable identity.
3. Rerun the Plan's completion check when its result can become stale.
4. Downgrade missing, changed, partial, or unverifiable outputs. Record the discrepancy; do not erase history.
5. Resume from the earliest invalid or incomplete dependency. Preserve upstream work only when it still passes fresh verification.

If the records disagree and cannot be reconciled safely, stop with status `BLOCKED` and identify the Plan interface or recovery decision needed.

## Execute one Work Package at a time

Work in the Plan's dependency order. The Main Agent is the sole writer and verifier for this Executor.

For each Package:

### 1. Preflight

- reread the Package's frozen inputs, qualifications, start condition, sole output, and Return Routes;
- confirm each input exists and still has the semantic identity the Plan names;
- distinguish an access or calculation problem under current semantics from a semantic change;
- mark the Package `IN PROGRESS` with time/as-of and the exact inputs used.

Do not silently substitute a convenient source, invent a join, change an eligibility rule, average a non-additive metric, widen scope, or redesign an output.

### 2. Produce the output

Follow the Package procedure exactly. Write the sole output at its planned path in `artifact_language` and keep intermediate material inside the run workspace unless the Plan says otherwise. Localize headings, labels, table headers, placeholders, and narrative; do not translate canonical codes/identifiers or source-exact exceptions recorded by the Plan.

Record every consequential result through the common Executor contract's coverage index and evidence-card interface. Distinguish observations, calculations, interpretations, and unsupported possibilities.

### 3. Verify freshly

Apply the common Executor contract's fresh-verification procedure to the just-written output. If the observed result does not match the Plan, report it and keep the Package incomplete.

### 4. Advance deliberately

Mark a Package `COMPLETE` only after all checks pass and its evidence entries are present. Record its output identity and unblock only direct dependents. Re-read the next Package rather than extrapolating from memory.

## Stop without improvising

Stop the run immediately when a Package cannot be completed faithfully. Preserve partial files and mark them clearly; do not make later Packages consume them.

Classify the blocker and use the narrowest Return Route:

- access, unavailable capability, malformed current-period record, or failed calculation under unchanged semantics: remain with this Executor and request the missing access/input or repair the execution;
- unclear or impossible Package interface, dependency, check, output, or recovery rule: `writing-report-plans`;
- changed source semantics or fitness: `profiling-evidence`;
- changed reusable metric meaning or mapping: `defining-metrics`;
- changed audience, intended use, question, or scope: `framing-analysis`.
- changed artifact language only: `writing-report-plans` for a presentation-interface revision and reconfirmation.

Write `BLOCKED` in progress with the first failing Package, observed evidence, affected downstream Packages, preserved valid work, requested decision, and exact Return Route. Do not call an incomplete or qualified run complete.

## Assemble the review handoff

After every Package passes, apply the common Executor contract's full reconciliation and seal sequence. As the sole writer, verify all current files directly; do not infer a complete package from ledger state.

When a same-period report is rerendered only because `artifact_language` changed, use the reconfirmed replacement Plan, preserve the prior report, record the existing replacement/supersession relationship, generate a new version, and send that new version through independent review. Do not overwrite the prior report or treat translation as already reviewed.

If review later requests execution-only corrections and semantics remain current, resume this Run from the affected Package, verify its dependents, and reseal through the common contract.

## Result

Return the common Executor handoff result, naming every verified Package output and either `reviewing-analysis` or the precise blocker. Use `interaction_language` for the user-facing handoff and `artifact_language` inside referenced artifacts.
