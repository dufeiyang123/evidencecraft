---
name: executing-report-plans
description: Use when a new Evidencecraft Run resolves to Inline Execution or an incomplete Run already freezes `executing-report-plans`.
---

# Executing Report Plans

Execute one confirmed Report Plan faithfully in the Main Agent's context. Own the sequential run, evidence capture, recovery, and fresh verification; do not reinterpret analysis semantics or issue the independent review verdict.

## Admit only a sequential run

Read the exact current Plan before doing analysis work. Resolve the authorized Brief, semantic dependencies, requested period/as-of, and relevant Run state. Read each binding semantic section when its Package needs it; do not load every source and prior output before starting.

Read and apply [the shared language contract](../using-evidencecraft/references/language-and-localization-contract.md). Recover an existing Run from progress first; record inferred legacy fields there without rewriting old artifacts.

Read and apply [the common Executor output contract](references/executor-output-contract.md). This Skill adds sequential ownership and dependency-ordered execution; it does not alter the shared output, evidence, verification, or review-handoff interface.

Proceed only when all are true:

- the Plan is confirmed and still current for its Brief, source uses, metric meanings, report interface, and capabilities;
- the router resolved Inline within authorization for a new Run, or existing progress freezes `executing-report-plans` or legacy `sequential`;
- the resolution basis and source are available for a new Run, and independent whole-report review is feasible; legacy progress may record its actual source and unavailable time;
- no Subagent-Driven Executor owns this Run and no other writer is changing its files;
- the Plan identifies the run workspace, Work Packages, outputs, reader-report contract, distinct draft/final paths, checks, stop conditions, and Review Package manifest.

Route instead when:

| Observed state | Action |
|---|---|
| This Run selected Subagent-Driven | Use `subagent-driven-reporting`; do not start an Inline writer. |
| No Run selection exists | Return to `using-evidencecraft` to resolve execution within authorization. |
| Plan is absent, unconfirmed, or has an execution-blocking interface gap | Return the exact gap to `writing-report-plans`. |
| Intended use, audience, question, or scope changed | Return to `framing-analysis`. |
| Source grain, keys, time, authority, lineage, or use-specific fitness changed | Return the exact use to `profiling-evidence`. |
| Metric population, formula, grain, time, deduplication, aggregation, missing-data rule, or source mapping changed | Return the exact metric to `defining-metrics`. |
| Only `interaction_language` changed | Continue the same lifecycle state and use the new language for user interaction. |
| `artifact_language` changed from the confirmed Plan | Apply the shared language contract; rerender within authorized meaning, preserving prior reports and reviewing new bytes. |
| Only current-period records or computed values changed under current semantics | Continue with this Executor. |
| The draft and evidence package are complete and need judgment | Use `reviewing-analysis`. |

Never run both Executors for the same active Run. Before any Package starts, an explicit reselection may replace the mode in that otherwise empty Run. After work starts, a mode change stops current writes and creates a new Run ID; preserve the old Run as history. Do not revise an otherwise current Plan merely to change execution mode.

## Initialize or recover the run

Use [the progress template](assets/progress-template.md), [the evidence-log template](assets/evidence-log-template.md), and, when sealing, [the Review Package manifest template](assets/review-package-template.md). Instantiate them in the Plan's run workspace and apply the shared language contract. Never edit the Skill assets in place.

For a new run:

1. Record the Plan, semantic dependency paths, period/as-of, `executing-report-plans`, the resolution basis/source and time, explicit parallel authorization as `none`, the frozen language contract, output paths, and every Work Package.
2. Create only the directories and empty records the Plan authorizes.
3. Apply the common preparation handoff: link valid existing work, identify remaining readiness checks, and block affected computation until critical prerequisites pass.
4. Mark the first dependency-ready Package `IN PROGRESS`; leave the rest `NOT STARTED` or `BLOCKED BY <id>`.

For a legacy Run whose progress says `Executor: sequential`, treat it as this Executor without reprompting. Append, without rewriting history: canonical Executor `executing-report-plans`, selection source `legacy progress`, selection time `unavailable (legacy)`, and parallel authorization `none` unless exact prior evidence says otherwise.

For a resumed run, treat the filesystem and fresh checks as authoritative, not status prose:

1. Read progress and the references needed to verify claimed completed outputs; inspect evidence and content at affected boundaries.
2. Match every claimed completed output to its exact path, expected interface, provenance, and current content hash or other durable identity.
3. Apply the common verification-reuse rule; rerun when identities, checker, or freshness are invalid or unknown.
4. Downgrade missing, changed, partial, or unverifiable outputs. Record the discrepancy; do not erase history.
5. Resume from the earliest invalid or incomplete dependency. Preserve upstream work only when its verification bindings and freshness remain valid.

If the records disagree and cannot be reconciled safely, stop with status `BLOCKED` and identify the Plan interface or recovery decision needed.

## Execute one Work Package at a time

Work in the Plan's dependency order. The Main Agent is the sole writer and verifier for this Executor.

For each Package:

### 1. Preflight

- reread the Package's frozen inputs, qualifications, start condition, sole output, and Return Routes;
- confirm each input exists and still has the semantic identity the Plan names;
- consume valid preparation and implementation references; perform only remaining or invalidated checks;
- distinguish an access or calculation problem under current semantics from a semantic change;
- mark the Package `IN PROGRESS` with time/as-of and the exact inputs used.

Do not silently substitute a convenient source, invent a join, change an eligibility rule, average a non-additive metric, widen scope, or redesign an output.

### 2. Produce the output

Follow the Package's remaining procedure and the common computation/synthesis contract. Reuse or establish the versioned calculation implementation, then write from verified results. Write owned outputs at planned paths, apply the language contract, and keep intermediate material in the Run workspace unless the Plan says otherwise.

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

Write `BLOCKED` in progress with the first failing Package, observed evidence, affected downstream Packages, preserved valid work, requested decision, and exact Return Route. Do not call an incomplete or qualified run complete.

## Assemble the review handoff

After every Package passes, apply the common Executor contract's full reconciliation and seal sequence. As the sole writer, verify all current files directly; do not infer a complete package from ledger state.

When a same-period report is rerendered only because `artifact_language` changed, record the authorized delivery change, preserve the prior report, record the existing replacement/supersession relationship, generate a new version, and send that new version through independent review. Do not overwrite the prior report or treat translation as already reviewed.

If review later requests execution-only corrections and semantics remain current, resume this Run from the affected Package, verify its dependents, and reseal through the common contract.

## Result

Return the common Executor handoff result, linking the authoritative manifest and either `reviewing-analysis` or the precise blocker. Use `interaction_language` for the user-facing handoff and `artifact_language` inside referenced artifacts.
