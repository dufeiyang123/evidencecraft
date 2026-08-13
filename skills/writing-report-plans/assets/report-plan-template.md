<!-- Template use: render every heading, label, table header, placeholder replacement, and narrative passage in the confirmed artifact language. The sample title's “Report Plan” phrase is a translatable artifact-type label, not a canonical identifier. Preserve canonical codes and IDs, exact Skill names, paths, hashes, citations, code, formulas, and original source titles. Remove this and every Template instruction comment from the instantiated artifact. -->

# Report Plan: [topic]

## Identity and outcome

- Status: Draft | Ready for Confirmation | Current
- Plan owner: [person or role]
- Analysis Brief: [exact confirmed path]
- Created/updated: [YYYY-MM-DD]
- Current since: [confirmation date or not current]
- Supersedes: [prior Plan path or none]
- Goal: [one-sentence report outcome]
- Audience/use: [from Brief]
- Questions covered: [exact Brief questions]
- Boundaries inherited from Brief: [exact sections plus any Plan-specific exclusion]
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

- Delivery profile: `standalone reader report` unless the user explicitly requests another audience artifact
- Interaction language: [language for questions, status, routes, and confirmation messages]
- Artifact language: [language for this Plan and all persistent run/report artifacts]
- Terminology and source-title handling: [translation, first-use explanation, and original-title rules]
- Localization rule: [localize headings, labels, table headers, placeholders, and narrative; list preserved canonical/source-exact exceptions]
- Reader self-containment: [context, methods, key values, and limitations that must appear in the report]
- Governance separation: [exact internal artifact paths and Run/Work Package/Evidence IDs/statuses excluded from the reader report]
- Reader citation policy: [formal external/reader-accessible citations retained; internal paths never substitute for support]
- Figure policy: [tables/prose first; figures only when materially useful]
- Asset contract: [none, or exact staging path, final asset root, and Markdown relative-URI mapping]
- Export interface: [reviewed Markdown plus declared report-local assets only]
- Draft path: [.evidencecraft run path]
- Final path: [different final destination; written only by `reviewing-analysis` after a passing gate]
- Required sections: [ordered headings]
- Comparison rules: [period/cohort/target and comparability]
- Required tables/figures: [reader-facing content; no path-only figure references]
- Internal traceability rule: [how governance artifacts map statements to evidence without leaking those links into the report]
- Limitation rule: [where material gaps appear]
- Companion dossier: [none by default, or separate path when explicitly requested]

## Run output interface

- Run workspace: `.evidencecraft/runs/<plan>-<as-of>/`
- Progress ledger: `progress.md`
- Progress language record: [repeat interaction language, artifact language, and terminology/source-title handling]
- Evidence log: `evidence-log.md`
- Draft report: [exact path]
- Staged reader assets: [none or exact paths and identities]
- Optional delegated task files: `task-N-brief.md`, `task-N-report.md`
- Review Package manifest: [exact Run-workspace Markdown file path]
- Review record: [path or compact-record rule]
- Final report: [exact path]

The selected Executor must return actual progress/evidence/output/draft/asset/manifest paths, fresh verification performed, unresolved limitations, and either the route to `reviewing-analysis` or an exact blocking Return Route. It does not issue the whole-report verdict, and status never substitutes for inspecting files.

## Work Package dependency map

```text
[WP-1] -> [WP-2]
[WP-1] -> [WP-3]
[WP-2, WP-3] -> [WP-4 synthesis]
```

<!-- Template instruction: replace the example with the actual dependency graph; do not preserve artificial parallelism. -->

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
- Evidence-log entries: [coverage-index claim mapping and compact evidence cards with exact source/upstream locator, as-of, identity, observation/derivation, verification, status, reader handling, and limitations]
- Completion checks:
  - [observable command/inspection/reconciliation and expected result]
- Stop conditions:
  - [condition -> exact Return Route]
- Delegation: safe | unsafe — [reason and context boundary]
- Downstream consumers: [WP IDs/report/reviewer]

<!-- Template instruction: repeat only for independently reviewable deliverables. -->

## Synthesis and claim discipline

- Verified inputs required: [WP outputs]
- Conflict handling: [how disagreements stop/qualify synthesis]
- Missing evidence handling: [what may be omitted/qualified/blocked]
- Governance traceability: [claim-to-evidence/task-result rule kept outside the reader artifact]
- Reader-report rule: [self-contained prose/tables, allowed reader citations, prohibited current-run governance references]
- Prohibited conclusions: [Brief/source/metric limitations]

## Executor recommendation

- Recommended: `executing-report-plans` | `subagent-driven-reporting`
- Rationale: [coupling, independence, context, risk]
- Mutual exclusion: Record the selected Executor in `progress.md`; do not start the other for this run.
- Shared completion interface: [progress, coverage-index/evidence-card log, verified outputs, draft, staged assets/mappings, real manifest, status, limitations]

## Fresh verification

| Scope | Check at execution time | Expected evidence | Stop/Return Route |
|---|---|---|---|
| [WP/report] | [command/inspection/reconciliation] | [fresh output] | [route] |
| Reader draft | Inspect self-containment, exact current-run governance strings, path-only references, and Markdown assets | No governance leakage; key content stands alone; every asset mapping resolves | First affected synthesis Package |
| Review Package | Inspect every manifest member and identity; confirm final path is still unwritten | Real sealed manifest; no placeholder identity; draft/final remain separate | Selected Executor |

## Review and save

- Reviewer package: [manifest containing frozen delivery contract, Brief, Plan, Profiles, Definitions, progress Run ID/status, evidence log, outputs, draft, assets/mappings, limitations, and stable identities]
- Review outcomes: `PASS | QUALIFIED | BLOCKED`
- Qualified handling: [visible qualifications and authority]
- Blocked handling: [responsible Return Route]
- Save only after: [independent whole-report review and unchanged-identity verification; self-review never substitutes]
- Save mapping: [record reviewed draft/assets identities to final path/identities in governance artifacts only]
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
