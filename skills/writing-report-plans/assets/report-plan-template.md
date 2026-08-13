# Report Plan: [topic]

## Status and ownership

- Status: Draft | Ready for Confirmation | Current
- Plan owner: [person or role]
- Analysis Brief: [exact confirmed path]
- Created/updated: [YYYY-MM-DD]
- Current since: [confirmation date or not current]
- Supersedes: [prior Plan path or none]

## Goal and boundaries

- Goal: [one-sentence report outcome]
- Audience/use: [from Brief]
- Questions covered: [exact Brief questions]
- Non-goals: [inherited and Plan-specific exclusions]
- Report period parameter: [period represented]
- As-of/cutoff: [availability rule, timezone, inclusivity, late data]
- Freshness requirements: [per source/use]

## Semantic dependencies

### Source Profiles

| Source/use | Profile path | Fitness | Qualification enforced by this Plan | Reopen trigger |
|---|---|---|---|---|
| [use] | [path] | FIT / QUALIFIED | [none or exact constraint] | [semantic change] |

### Metric Definitions

| Metric/use | Definition path | Status | Qualification/confirmation condition | Reopen trigger |
|---|---|---|---|---|
| [metric] | [path] | Ready / Current | [condition] | [semantic change] |

## Report contract

- Draft path: [.evidencecraft run path]
- Final path: [reports/YYYY-MM-DD-<topic>.md]
- Required sections: [ordered headings]
- Comparison rules: [period/cohort/target and comparability]
- Required tables/figures: [content, not visual style only]
- Traceability rule: [how statements point to evidence/task results]
- Limitation rule: [where material gaps appear]

## Run output interface

- Run workspace: `.evidencecraft/runs/<plan>-<as-of>/`
- Progress ledger: `progress.md`
- Evidence log: `evidence-log.md`
- Draft report: [exact path]
- Optional delegated task files: `task-N-brief.md`, `task-N-report.md`
- Review record: [path or compact-record rule]
- Final report: [exact path]

The selected Executor must return `COMPLETE | QUALIFIED | BLOCKED`, actual output paths, verification performed, and limitations. Status never substitutes for inspecting files.

## Work Package dependency map

```text
[WP-1] -> [WP-2]
[WP-1] -> [WP-3]
[WP-2, WP-3] -> [WP-4 synthesis]
```

Replace this example with the actual dependency graph. Do not preserve artificial parallelism.

## Work Packages

### WP-[N]: [deliverable]

- Purpose/report section: [question and section]
- Start condition: [verified prerequisites]
- Frozen inputs: [exact paths, periods, definitions, qualifications]
- Upstream dependencies: [WP IDs or none]
- Procedure:
  1. [specific action]
  2. [specific action]
- Sole output: [exact path and Markdown/table/data interface]
- Evidence-log entries: [source locator/as-of/citation/hash/coverage/status/limits]
- Completion checks:
  - [observable command/inspection/reconciliation and expected result]
- Stop conditions:
  - [condition -> exact Return Route]
- Delegation: safe | unsafe — [reason and context boundary]
- Downstream consumers: [WP IDs/report/reviewer]

Repeat only for independently reviewable deliverables.

## Synthesis and claim discipline

- Verified inputs required: [WP outputs]
- Conflict handling: [how disagreements stop/qualify synthesis]
- Missing evidence handling: [what may be omitted/qualified/blocked]
- Claim traceability: [citation/evidence-log/task-result rule]
- Prohibited conclusions: [Brief/source/metric limitations]

## Executor recommendation

- Recommended: `executing-report-plans` | `subagent-driven-reporting`
- Rationale: [coupling, independence, context, risk]
- Mutual exclusion: Record the selected Executor in `progress.md`; do not start the other for this run.
- Shared completion interface: [progress, evidence log, verified outputs, draft, status, limitations]

## Fresh verification

| Scope | Check at execution time | Expected evidence | Stop/Return Route |
|---|---|---|---|
| [WP/report] | [command/inspection/reconciliation] | [fresh output] | [route] |

## Review and save

- Reviewer package: [Brief, Plan, Profiles, Definitions, progress, evidence log, outputs, draft, limitations]
- Review outcomes: `pass | qualified | blocked`
- Qualified handling: [visible qualifications and authority]
- Blocked handling: [responsible Return Route]
- Save only after: [review and verification gate]
- Preserve on same-period correction: [prior report and replacement relationship]

## Stop and recovery rules

- Global stops: [missing/changed semantics, access, invalid outputs, unresolved conflict]
- Resume from: earliest incomplete Work Package whose inputs remain current
- Trust: actual files and fresh checks, not conversation or status alone
- Invalidation: [which changes reopen which Packages]

## Confirmation record

- Confirmed by: [person or not yet confirmed]
- Confirmed at: [date or not yet confirmed]
- Confirmation: [exact statement/reference]
- Metric Definitions confirmed together: [paths or none]
- Accepted qualifications: [list or none]
- Next responsible Skill: [Executor or blocker]
