# Evidencecraft

Evidencecraft is a skills-only plugin for evidence-first analysis and recurring reporting in Claude Code, Codex, and OpenClaw. It turns an ambiguous reporting request into a confirmed brief, reusable source and metric definitions, an executable plan, a verified run, and an independent review.

It bundles nine composable skills and does not require an MCP server, app connection, or external service:

- `using-evidencecraft` routes first-time setup, recurring runs, recovery, semantic rework, and new-Run execution handoffs.
- `framing-analysis` creates and confirms the Analysis Brief.
- `profiling-evidence` tests source semantics and fitness.
- `defining-metrics` freezes reusable quantitative definitions.
- `writing-report-plans` turns confirmed analysis intent into executable Work Packages and a non-binding execution recommendation.
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
/plugin marketplace add dufeiyang123/evidencecraft@v0.4.0
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
codex plugin marketplace add dufeiyang123/evidencecraft --ref v0.4.0
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
openclaw plugins install clawhub:@dufeiyang123/evidencecraft@0.4.0
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

Evidencecraft uses Markdown artifacts as durable handoffs. The router selects the next responsibility and asks the user to choose Subagent-Driven or Inline before each new Run; the Report Plan only recommends. A Run freezes one Executor and resumes it without asking again. Subagent-Driven means fresh-context workers in strict sequence by default. True parallel dispatch is a separate, explicitly requested subordinate Skill, not a third normal mode. Profiling and metric definition run only when their semantics are missing or stale, and final save remains gated on independent review.

The reviewed final Markdown is a standalone reader artifact, optionally accompanied only by declared report-local assets. By default it contains no Brief, Plan, Evidence log, Review Package, Run/Work Package/Evidence IDs, review status, hashes, or engineering traceability appendix. Formal external citations and file or code names that are substantive report subject matter remain reader-facing when useful. The governance chain stays in the run package and points forward to the reviewed report and its identity; downstream PDF conversion therefore consumes only the final Markdown and declared assets and does not need to understand Evidencecraft.

Inside the governance layer, the Evidence log combines a coverage index with compact evidence cards, while the Review Package is a real sealed manifest whose members and identities can be inspected. Tables are the default way to carry important values into the report. Figures are used only when they materially improve understanding and every Markdown image has an explicit staged-to-final report-local asset mapping.

Evidencecraft keeps two language settings throughout the lifecycle. `interaction_language` controls questions, status, routing, and confirmation messages; it follows an explicit interaction preference or otherwise the primary language of the current substantive request. `artifact_language` controls the Brief, Plan, Profiles, Definitions, run records, delegated task artifacts, reviews, and final report; it follows an explicit deliverable requirement, then a confirmed audience delivery requirement, and otherwise inherits the interaction language. Thus a Chinese request produces Chinese interaction and artifacts by default, while a user may request Chinese interaction with English deliverables.

Templates remain single-source English maintenance assets, but their headings, labels, table headers, placeholders, and narrative are localized when instantiated. Canonical status and verdict codes such as `PASS` and `BLOCKED`, Work Package IDs such as `WP-1`, exact paths, hashes, citations, code, formulas, and original source titles remain unchanged. A language-only delivery change updates and reconfirms the report interface without reopening otherwise current source profiles, metric definitions, or language-independent analysis.

The plugin contributes instructions, templates, references, and role prompts only. It inherits the tools and data access already available in the current agent environment.
