# Common Executor Output Contract

Both `executing-report-plans` and `subagent-driven-reporting` must read and apply this contract before initializing or resuming a Run and again before sealing the review handoff. Orchestration may differ; the core outputs and review boundary may not.

## Required Run outputs

Produce inside the Plan-scoped workspace:

- progress that records Plan and semantic identities, Run-selected Executor, exact user selection and time, explicit parallel authorization or `none`, period/as-of, language contract, Work Package state, checks, blockers, and recovery history; a legacy Run may instead append selection source `legacy progress` and time `unavailable (legacy)` without inventing missing history;
- an evidence log with a coverage index and compact evidence cards;
- verified Work Package outputs and, for delegated work, Task Briefs, Task Reports, and task reviews;
- one reader-facing report draft at the planned draft path;
- staged reader assets and final relative-URI mappings when the Plan declares assets;
- one real Review Package manifest at the planned path.

The final report and final assets remain unwritten until `reviewing-analysis` passes the save gate.

## Evidence and reader boundary

Each consequential result needs an evidence card with the supported requirement or claim, evidence type, exact source or upstream locator, governing Profile or Definition, period/as-of, grain and coverage, durable identity, observation or derivation, verification, support status, reader handling, and limitations.

Keep paths, internal IDs, hashes, task-review state, and engineering traceability in governance artifacts. The reader draft must stand alone through prose, tables, allowed external citations, and declared report-local assets; it must not require repository access or expose current-run governance navigation.

## Fresh verification

For every completed Package and the integrated report:

1. identify the Plan check and expected result;
2. perform it against the current output;
3. read the complete result, including failures, counts, coverage, and limitations;
4. record method, time, observed result, and disposition in progress;
5. keep the Package incomplete when the result does not match.

Prior success, a status label, a worker report, or plausible output is not completion evidence.

## Seal the review handoff

After all required work passes:

1. reconcile the draft's required sections, claims, values, and limitations with verified outputs and the evidence log;
2. verify reader self-containment, governance separation, permitted citations, and every staged-to-final asset mapping;
3. confirm the planned final Markdown and assets are still unwritten;
4. freeze stable outputs in dependency order, then the evidence log, draft, and staged assets;
5. instantiate the Review Package manifest with the frozen delivery contract, current Brief, Profiles, Definitions, Plan, progress Run ID/status, evidence log, verified outputs, draft/assets, final mappings, and unresolved limitations;
6. open every member at its exact path and record a real hash or other durable identity for each stable member;
7. omit the manifest's own hash and mutable progress hash from the manifest;
8. record the completed manifest and frozen draft/assets identities once in progress;
9. set the Run to `READY FOR INDEPENDENT REVIEW`, never `APPROVED` or `FINAL`.

If any check fails or a frozen member changes, reopen the first affected Package, verify its dependents again, and repeat the seal. Do not self-review, silently repair findings as reviewer, or write the final destination.

## Handoff result

Return the Run ID, actual progress/evidence/output/draft/asset/manifest paths, fresh checks performed, limitations, and either `reviewing-analysis` or one exact blocking Return Route. The handoff is execution evidence, not an approval claim.
