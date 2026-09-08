# Evidencecraft

Evidencecraft is a skills-only plugin for evidence-first analysis and recurring reporting in Claude Code, Codex, and OpenClaw. It turns an ambiguous reporting request into a confirmed brief, reusable source and metric definitions, an executable plan, a verified run, and an independent review.

Its main audience is junior and intermediate data analysts working on metric interpretation, joins, reconciliation, ad hoc analysis, and recurring reports. Warehouse data is the primary analysis input; project rules, existing implementations, and historical reports help select the method. Deep data governance and source repair are outside the core workflow.

It bundles nine composable skills and does not require an MCP server, app connection, or external service:

- `using-evidencecraft` routes first-time setup, recurring runs, recovery, semantic rework, and new-Run execution handoffs.
- `framing-analysis` creates and confirms the Analysis Brief.
- `profiling-evidence` tests source semantics and fitness.
- `defining-metrics` freezes reusable quantitative definitions.
- `writing-report-plans` researches relevant context and bounded data readiness, then produces a strategy, report blueprint, reusable preparation, and executable Work Packages.
- `executing-report-plans` runs a Report Plan after the Run selects Inline Execution.
- `subagent-driven-reporting` runs Work Packages one fresh worker at a time with independent task review.
- `dispatching-parallel-research` handles an explicitly requested batch only after proving its ready Work Packages independent.
- `reviewing-analysis` returns an independent `PASS`, `QUALIFIED`, or `BLOCKED` verdict before final save.

## Installation

Installation differs by agent harness. Install Evidencecraft separately in each harness you use.

### Claude Code

Inside Claude Code, add this GitHub repository as a marketplace and install Evidencecraft:

```text
/plugin marketplace add dufeiyang123/evidencecraft
/plugin install evidencecraft@evidencecraft
/reload-plugins
```

Invoke the router explicitly with:

```text
/evidencecraft:using-evidencecraft
```

To pin an immutable semver release instead of tracking the default branch:

```text
/plugin marketplace add dufeiyang123/evidencecraft@v0.5.0
/plugin install evidencecraft@evidencecraft
/reload-plugins
```

### Codex

Add this GitHub repository as a Codex marketplace and install Evidencecraft:

```bash
codex plugin marketplace add dufeiyang123/evidencecraft
codex plugin add evidencecraft@evidencecraft
```

Restart the Codex app or start a new thread after installation. Begin with:

```text
Use $evidencecraft:using-evidencecraft to route this reporting task.
```

To install an immutable release instead of tracking the default branch, pin its semver tag:

```bash
codex plugin marketplace add dufeiyang123/evidencecraft --ref v0.5.0
codex plugin add evidencecraft@evidencecraft
```

### OpenClaw

Install the complete Evidencecraft bundle from ClawHub and restart the Gateway:

```bash
openclaw plugins install clawhub:@dufeiyang123/evidencecraft
openclaw gateway restart
```

OpenClaw loads every current `skills/` child as a normal Skill. Inspect the installed bundle with:

```bash
openclaw plugins inspect evidencecraft
```

To pin an immutable release instead of following `latest`:

```bash
openclaw plugins install clawhub:@dufeiyang123/evidencecraft@0.5.0
openclaw gateway restart
```

## Update

For a Claude Code installation that tracks the default branch:

```text
/plugin marketplace update evidencecraft
/plugin update evidencecraft@evidencecraft
/reload-plugins
```

For a Codex installation that tracks the default branch:

```bash
codex plugin marketplace upgrade evidencecraft
codex plugin add evidencecraft@evidencecraft
```

Then restart the Codex app or start a new thread. Release tags are immutable; move a pinned installation to a newer tag by removing the configured marketplace, adding it again with the new tag, and reinstalling Evidencecraft.

For an OpenClaw installation that follows ClawHub `latest`:

```bash
openclaw plugins update evidencecraft
openclaw gateway restart
```

You can update all tracked OpenClaw plugins with `openclaw plugins update --all`. An installation pinned to an exact ClawHub version remains pinned until you explicitly install a newer version.

## How it behaves

### Research, computation, and writing

Planning resolves the business and method decisions needed to execute; it does not precompute the report's findings. It searches relevant project material, distinguishes authoritative rules from reusable code and historical method examples, and checks only task-relevant data within known cost limits. Metadata and valid existing checks come first. Samples do not prove full coverage, unchecked prerequisites are not passes, and a historical report cannot silently supply current numbers or authorize a metric.

The Plan starts with a readable proposal: task, data readiness, recommended strategy and rationale, report blueprint, and material limits. Execution interfaces follow. When critical observations or capabilities are unavailable, planning delivers a limited Draft with affected work and release conditions; formal execution requires a Current Plan. Passing checks adds no approval step. Host planning restrictions are respected: conversation-only artifacts are saved when writes become permitted, without repeating the whole investigation.

One optional preparation record preserves useful references, probes, strategy decisions, reuse conditions, and remaining work. A Run references that evidence after verifying identities, parameters, coverage, method and freshness. It does not duplicate the preparation tables or inherit last period's health verdict. Legacy Plans need bounded missing checks, not bulk migration.

Both Executors compute and validate results before synthesis. They reuse versioned SQL/models/scripts under the same metric semantics; new or changed implementations require independent expected-case and fixed-input repeatability checks. Calculation records bind complete data inputs, parameters, semantic/code versions, relevant execution settings, and keyed results with units and precision. Writing organizes accepted results and evidence; new numerical derivations return to computation. Corrections preserve previous versions. These are responsibilities within the existing Executors, not new skills or mandatory agents.

These instructions define the workflow, not a warehouse engine or a guarantee established by static validation. Production repeatability, reader usability, workload coverage, and actual token savings require separate evidence from permitted use or evaluation.

### Routing and review

Evidencecraft uses Markdown artifacts as durable handoffs. The router selects the next responsibility and resolves a new Run from explicit choices, applicable preferences, or feasible defaults within authorization; the Report Plan only recommends. It asks about material scope, cost, or capability choices and honors requested approval checkpoints. Briefs and Plans record the actual authority for business decisions without asking the user to approve the same meaning repeatedly. A Run freezes one Executor and resumes it without asking again. Subagent-Driven means fresh-context workers in strict sequence by default. True parallel dispatch is a separate, explicitly requested subordinate Skill, not a third normal mode. Profiling and metric definition run only when their semantics are missing or stale, and final save remains gated on independent review.

The reviewed final Markdown is a standalone reader artifact, optionally accompanied only by declared report-local assets. By default it contains no Brief, Plan, Evidence log, Review Package, Run/Work Package/Evidence IDs, review status, hashes, or engineering traceability appendix. Formal external citations and file or code names that are substantive report subject matter remain reader-facing when useful. The governance chain stays in the run package and points forward to the reviewed report and its identity; downstream PDF conversion therefore consumes only the final Markdown and declared assets and does not need to understand Evidencecraft.

Inside the governance layer, the Evidence log combines a coverage index with compact evidence cards, while the Review Package is a real sealed manifest whose members and identities can be inspected. Reports lead with the requested answer, key evidence, and material limits. Compact tables or figures serve the reader question; exhaustive calculation rows stay in evidence unless explicitly required as a reviewed reader companion. Every Markdown image has an explicit staged-to-final asset mapping. Re-review follows actual changes and affected claims, expanding to full review when impact is uncertain. Deterministic checks may be reused only while input/output/checker identities and freshness remain valid; independent task and whole-report judgments remain required.

Evidencecraft keeps two language settings throughout the lifecycle. `interaction_language` controls questions, status, routing, and confirmation messages; it follows an explicit interaction preference or otherwise the primary language of the current substantive request. `artifact_language` controls the Brief, Plan, Profiles, Definitions, run records, delegated task artifacts, reviews, and final report; it follows an explicit deliverable requirement, then a confirmed audience delivery requirement, and otherwise inherits the interaction language. Thus a Chinese request produces Chinese interaction and artifacts by default, while a user may request Chinese interaction with English deliverables.

Templates remain single-source English maintenance assets, but their headings, labels, table headers, placeholders, and narrative are localized when instantiated. Canonical status and verdict codes such as `PASS` and `BLOCKED`, Work Package IDs such as `WP-1`, exact paths, hashes, citations, code, formulas, and original source titles remain unchanged. An explicit language-only delivery request authorizes the producer to rerender under unchanged meaning; new report bytes are reviewed without reopening current source profiles, metric definitions, or language-independent analysis.

The plugin contributes instructions, templates, references, role prompts, and a read-only Python 3 helper for local manifest identities. The helper does not run analysis or authorize a save; an equivalent hashing tool can be used where Python is unavailable. Evidencecraft inherits the environment's tools and data access, and checks independent-review capability before costly execution.
