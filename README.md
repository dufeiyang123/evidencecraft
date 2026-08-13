# Evidencecraft

Evidencecraft is a skills-only Codex plugin for evidence-first analysis and recurring reporting. It turns an ambiguous reporting request into a confirmed brief, reusable source and metric definitions, an executable plan, a verified run, and an independent review.

It bundles eight composable skills and does not require an MCP server, app connection, or external service:

- `using-evidencecraft` routes first-time setup, recurring runs, recovery, and semantic rework.
- `framing-analysis` creates and confirms the Analysis Brief.
- `profiling-evidence` tests source semantics and fitness.
- `defining-metrics` freezes reusable quantitative definitions.
- `writing-report-plans` turns confirmed analysis intent into executable Work Packages.
- `executing-report-plans` runs a confirmed plan sequentially with evidence and progress records.
- `subagent-driven-reporting` runs eligible Work Packages through isolated workers and independent task review.
- `reviewing-analysis` returns an independent `pass`, `qualified`, or `blocked` verdict before final save.

## Install

Add this GitHub repository as a Codex marketplace, then install the plugin:

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
codex plugin marketplace add dufeiyang123/evidencecraft --ref v0.1.0
codex plugin add evidencecraft@evidencecraft
```

## Update

For an installation that tracks the default branch, refresh the marketplace snapshot and reinstall the current plugin version:

```bash
codex plugin marketplace upgrade evidencecraft
codex plugin add evidencecraft@evidencecraft
```

Then restart the Codex app or start a new thread. Release tags are immutable; move a pinned installation to a newer tag by removing the configured marketplace, adding it again with the new `--ref`, and reinstalling Evidencecraft.

## How it behaves

Evidencecraft uses Markdown artifacts as durable handoffs. The router selects the next responsible skill but does not perform downstream work. Profiling and metric definition run only when their semantics are missing or stale. A single run uses either the sequential executor or the multi-agent executor, never both, and final save remains gated on independent review.

The plugin contributes instructions, templates, references, and role prompts only. It inherits the tools and data access already available in the current Codex environment.
