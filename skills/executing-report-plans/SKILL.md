---
name: executing-report-plans
description: Use when a confirmed current Report Plan selects the sequential Executor, or when resuming that sequential run; execute its Work Packages in dependency order, verify fresh outputs, maintain progress and evidence records, and prepare a review package without redefining scope, sources, metrics, or the Plan.
---

# Executing Report Plans

Execute one confirmed Report Plan faithfully in the Main Agent's context. Own the sequential run, evidence capture, recovery, and fresh verification; do not reinterpret analysis semantics or issue the independent review verdict.

## Admit only a sequential run

Read the exact current Plan before doing analysis work. Also inspect the confirmed Analysis Brief, every referenced Source Profile and Metric Definition, the requested period/as-of, relevant prior progress, and the actual run files.

Recover the language contract independently. Apply a current explicit field-scoped requirement first; otherwise, for an existing Run, use the contract recorded in `progress.md`, then the current Plan and Brief, then the primary language of the current substantive request. If legacy artifacts lack the fields, record `interaction_language`, `artifact_language`, and terminology/source-title handling in this Run without rewriting them. Use `interaction_language` for questions, status, route, and confirmation messages. Use `artifact_language` for progress, evidence logs, Package outputs, Review Package text, draft, and final-report content. Preserve canonical codes and identifiers, paths, hashes, citations, code, formulas, and original source titles; English source material, templates, prompts, Profiles, or Definitions never switch the contract.

Proceed only when all are true:

- the Plan is confirmed and still current for its Brief, source uses, metric meanings, report interface, and capabilities;
- the Plan recommends or the user has selected the sequential Executor;
- no multi-agent Executor owns this run and no other writer is changing its files;
- the Plan identifies the run workspace, Work Packages, outputs, reader-report contract, distinct draft/final paths, checks, stop conditions, and Review Package manifest.

Route instead when:

| Observed state | Action |
|---|---|
| Multi-agent Executor was selected | Use `subagent-driven-reporting`; do not start a parallel sequential run. |
| Plan is absent, unconfirmed, or has an execution-blocking interface gap | Return the exact gap to `writing-report-plans`. |
| Intended use, audience, question, or scope changed | Return to `framing-analysis`. |
| Source grain, keys, time, authority, lineage, or use-specific fitness changed | Return the exact use to `profiling-evidence`. |
| Metric population, formula, grain, time, deduplication, aggregation, missing-data rule, or source mapping changed | Return the exact metric to `defining-metrics`. |
| Only `interaction_language` changed | Continue the same lifecycle state and use the new language for user interaction. |
| `artifact_language` changed from the confirmed Plan | Stop and return to `writing-report-plans` to revise and reconfirm the report interface; do not rerun unaffected profiling, metric definition, or analysis. |
| Only current-period records or computed values changed under current semantics | Continue with this Executor. |
| The draft and evidence package are complete and need judgment | Use `reviewing-analysis`. |

Never run both Executors for the same scenario. An Executor switch requires stopping the current owner, reconciling actual files, recording the handoff in progress, and obtaining user authority when it changes the confirmed Plan.

## Initialize or recover the run

Use [the progress template](assets/progress-template.md), [the evidence-log template](assets/evidence-log-template.md), and, when sealing, [the Review Package manifest template](assets/review-package-template.md). Instantiate them in the Plan's run workspace; treat English headings and labels—including “Report Run Progress”, “Evidence Log”, and “Review Package Manifest”—as semantic slots, render all user-visible content and artifact-type phrases in `artifact_language`, preserve only exact Skill names and the recorded canonical or source-exact exceptions, and remove all template comments. Never edit the Skill assets in place.

For a new run:

1. Record the Plan, semantic dependency paths, period/as-of, selected Executor, frozen language contract, output paths, and every Work Package.
2. Create only the directories and empty records the Plan authorizes.
3. Mark the first dependency-ready Package `IN PROGRESS`; leave the rest `NOT STARTED` or `BLOCKED BY <id>`.

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

For every consequential result, add a compact evidence card containing the supported requirement/claim, evidence type, exact source or upstream artifact and locator, governing Profile/Definition, period/as-of, grain/coverage, identity, observation or derivation, verification, status, and limitations. Update the coverage index that maps report requirements/claims to Evidence IDs and reader-report handling. Keep precise paths, Evidence IDs, hashes, and verification detail in governance artifacts; do not paste them into the reader draft. Distinguish observations, calculations, interpretations, and unsupported possibilities.

### 3. Verify freshly

Before calling the Package complete:

1. identify the Plan check that proves each completion claim;
2. run or perform the full check against the just-written output;
3. read the complete result, including failures, counts, coverage, and limitations;
4. compare it with the observable expected result;
5. record the command or method, time, outcome, and evidence in progress.

An old check, a plausible output, a prior status, or another actor's success statement is not proof. If verification fails, report the actual state and keep the Package incomplete.

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

After every Package passes fresh verification:

1. confirm the draft contains every Plan-required section and no unsupported completion markers;
2. reconcile claims, tables, and limitations with the evidence log;
3. verify the reader draft against the Plan's publication contract: it stands alone, carries key values in prose/tables, preserves allowed reader-facing citations, and does not use current-run governance paths/IDs/statuses, hashes, engineering traceability, `...`, globs, brace expansions, or path-only figures as reader references;
4. resolve every Markdown image to the declared staged asset and final relative URI, or confirm that the asset contract is `none`; a filename that is substantive report content may remain, but it cannot be required navigation or the sole support for a claim;
5. verify the planned final report and final asset destinations are still unwritten;
6. rerun the Plan's final completeness and internal traceability checks;
7. freeze the evidence log, verified Package outputs, draft, and staged reader assets, then instantiate the Plan-defined Review Package manifest with the frozen delivery contract, current Brief, Source Profiles, Metric Definitions, Plan, progress by Run ID/status, evidence log, verified Package outputs, draft/assets, final URI mapping, and unresolved limitations;
8. inspect every manifest member at its exact path and record a real hash or other durable identity for every stable member; do not record a manifest self-hash inside the manifest and do not hash mutable progress;
9. after the manifest is complete, record the frozen draft/assets and manifest identities in progress once; do not rewrite frozen files merely to update a self-referential identity;
10. mark run status `READY FOR INDEPENDENT REVIEW`, never `APPROVED` or `FINAL`.

Formal external citations, paper URLs, and file or code identifiers that are themselves report subject matter are not governance leakage. They still cannot make repository access a prerequisite for understanding the report.

When a same-period report is rerendered only because `artifact_language` changed, use the reconfirmed replacement Plan, preserve the prior report, record the existing replacement/supersession relationship, generate a new version, and send that new version through independent review. Do not overwrite the prior report or treat translation as already reviewed.

If a final check reveals a substantive mismatch, reopen the affected Package or record, correct it, and repeat the freeze sequence. Do not churn timestamps or hashes after a passing freeze just to make mutable records hash each other.

Do not review your own work, silently repair it as a reviewer, or save the report to its final destination. Return the Review Package to `reviewing-analysis`. If review later requests execution-only corrections and semantics remain current, resume this run from the affected Package and verify all dependents again.

## Result

Return exact paths for:

- progress and evidence log;
- every verified Package output;
- report draft;
- staged reader assets, when any;
- Review Package manifest;
- the next skill or precise blocking Return Route.

State what was freshly verified and what remains limited, using `interaction_language` for the user-facing handoff and `artifact_language` inside referenced artifacts. The result is execution evidence, not a claim that the analysis is approved or saved.
