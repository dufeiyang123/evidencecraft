---
name: using-evidencecraft
description: Use when an Evidencecraft analysis or recurring report starts or resumes and no isolated Task Brief or review package already fixes the role.
---

# Using Evidencecraft

Choose the next responsibility; the routed Skill owns the work. An isolated worker or reviewer follows its supplied package and does not reopen this lifecycle.

## Inspect the smallest useful state

Start with the request and current Run progress, otherwise the current Plan and Brief. Verify the existence and identity of artifacts needed for the next transition. Open a Profile, Definition, evidence entry, or prior review only when a dependency, change, or finding makes it relevant. A status label or polished draft alone is not proof of completion.

Resolve missing or changed language fields using [the language contract](references/language-and-localization-contract.md). Reuse a resolved contract; do not reload unchanged guidance at every handoff.

If host planning restrictions left authorized Brief/Plan content in the conversation, route to its producer to persist that exact content and preparation references once writes are permitted. Recheck changed facts, not the entire research process; do not fabricate file identities or run against an unsaved contract.

## Classify once

Use the first matching state:

| Observed state | Next responsibility |
|---|---|
| Audience, intended use, business scope, or acceptable risk changed, or no authorized Brief exists | `framing-analysis` |
| Explicit source investigation or a recorded, exact source semantic/fitness gap | `profiling-evidence`, then planning |
| Explicit metric definition or a recorded, exact reusable metric gap | `defining-metrics`, then planning |
| No usable Current Plan, a Draft has unresolved planning prerequisites, or package/check/save interfaces changed | `writing-report-plans` |
| Sealed Run is `READY FOR INDEPENDENT REVIEW`, including a resealed correction | `reviewing-analysis` |
| Review is `BLOCKED` | Its earliest exact Return Route and affected Package |
| Incomplete Run has a frozen Executor | Resume that Executor at the first affected Package |
| Current Plan and no incomplete Run | Resolve execution below, then invoke that Executor |

A merely suspected or unclassified source/metric gap goes to planning for preflight, not a broad router investigation. A new period or new source values alone is an execution input. Reuse unchanged business and semantic decisions.

Planning owns bounded preparation and a useful Draft when critical checks are unavailable; a Draft cannot start formal execution. A Current legacy Plan merely missing preparation fields goes to its Executor for bounded readiness checks, not automatic replanning.

An interaction-language change takes effect immediately. A requested translation or presentation change under the same meaning stays with the current producer; record the revised delivery setting and review the new report bytes. Return to planning only if it changes a binding delivery interface, and to framing only if audience or intended use changes.

## Resolve a new Run without a routine approval stop

Check execution and independent whole-report review capability before costly work. Inline execution still requires an independent reviewer. If that capability is unavailable, state the limitation before execution; never promise an audited final or invent independence. If the user explicitly changes the request to an unreviewed draft, record that scope change and leave the audited-final workflow; do not mark it review-ready or save it as a reviewed final.

Resolve the mode in order:

1. Current explicit choice, including “use the recommendation.”
2. An applicable prior user preference or project instruction.
3. A feasible Plan recommendation within the user's authorization and resource constraints.
4. Inline, when feasible and no unresolved material cost or capability trade-off remains.

Honor a request to approve the mode. Otherwise “execute,” “continue,” or “follow the Plan” authorizes the feasible default; explain the choice briefly and proceed. Ask only when a missing choice materially affects cost, isolation, timing, or capability. Explain that trade-off in business terms. If an explicitly selected mode is unavailable, disclose that and obtain a replacement choice; do not silently override it.

Subagent-Driven means fresh workers per Package, serial by default. Parallel execution requires explicit authorization for this Run and eligibility checks in `dispatching-parallel-research`; it is not a third Executor. An explicit parallel request selects Subagent-Driven. A recommendation alone never authorizes parallelism or overrides environment restrictions on delegation.

The chosen Executor records the mode, basis (explicit choice / standing preference / authorized default), source statement or reference, resolution time, and parallel authorization or `none`. Do not fabricate a user quote for an inferred default.

## Preserve ownership and recovery

One Run has one Executor. Before any Package starts, an explicit reselection may update an empty Run. After work starts, stop writes and use a new Run ID for a mode change, preserving the old Run. A resumed Run does not repeat mode selection.

Legacy progress `Executor: sequential` means `executing-report-plans`. Preserve its choice, record basis `legacy progress` and unknown selection time honestly. A legacy Plan selection with no existing Run is advisory. Do not rewrite history just to normalize fields.

Reconcile actual outputs with progress at the affected boundary:

- execution, verification, ordinary access or period-data defect → current Executor;
- package, dependency, output, check, review input, or save-rule defect → planning;
- source grain, keys, time, authority, mapping, or use-specific fitness defect → profiling, then planning;
- metric meaning, population, formula, time, aggregation, or missing-data rule defect → metric definition, then planning;
- business meaning or risk authority change → framing, then planning.

Redo only dependent work. Preserve valid accepted artifacts and prior reports.

## Hand off

Tell the user the next action and its reason in one or two natural sentences. Include a decision or blocker only when one exists; keep internal state codes, Skill names, IDs, and hashes in the handoff record unless useful to the user.

Pass the resolved contract, relevant artifact references/identities, exact affected scope, execution basis, and any blocking evidence to the next Skill. Do not paste the entire lifecycle or all source files. If asked only to classify or recommend, stop here. Otherwise invoke the routed Skill and continue.
