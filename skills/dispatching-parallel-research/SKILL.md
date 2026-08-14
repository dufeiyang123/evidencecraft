---
name: dispatching-parallel-research
description: Use when an active Subagent-Driven Evidencecraft Run has explicit user authorization for parallel execution and at least two dependency-ready Work Packages may be independent.
---

# Dispatching Parallel Research

Dispatch one bounded worker per proven-independent Work Package concurrently, then return every worker claim to `subagent-driven-reporting`. This is a subordinate scheduling Skill, not a third Executor: it never owns the Run, accepts outputs, integrates evidence, reviews the report, or saves the final artifact.

## Admit only an authorized batch

Proceed only when all are true:

- a confirmed current Report Plan and active Run exist;
- Run progress freezes `subagent-driven-reporting` as its Executor;
- progress records the user's explicit parallel request for this Run;
- at least two Packages are dependency-ready and each already has a frozen Task Brief and unique Task Report/output paths;
- `subagent-driven-reporting` invoked this Skill for the named batch.

Generic requests to execute, continue, use subagents, or follow the Plan do not authorize parallelism. A Plan's parallel-candidate marker is evidence to inspect, not authorization or proof.

If any admission condition fails, dispatch nothing. Return the exact failed condition to `subagent-driven-reporting`, which continues serially unless the condition reveals a real Plan or semantic defect.

## Prove independence

Open every candidate Task Brief and the current progress ledger. A batch is parallel-safe only when every pair of Packages:

- has no dependency on the other's unfinished output;
- reads only immutable or independently versioned inputs;
- writes distinct output, Task Report, intermediate, and temporary paths;
- cannot edit progress, evidence log, draft, Review Package, final report, or another worker artifact;
- does not share a mutable extract, source session, transaction, temporary table, rate-limit budget, lock, or other constrained resource that can change either result;
- can fail or finish without changing the other's requirements or interpretation.

Unclear independence is not independence. Reject the whole proposed batch when any pair fails; do not dispatch a safe subset silently. Name the conflicting Packages and resource, then return control for serial scheduling.

## Dispatch one concurrent batch

For each accepted candidate, use the existing [report-worker prompt](../subagent-driven-reporting/prompts/report-worker.md) with that Package's frozen Task Brief and declared inputs. Do not paste the whole Plan, accumulated Run history, another worker's context, or expected conclusions. Workers may write only their unique output and Task Report and may not dispatch subagents.

Issue every worker dispatch in the same orchestration turn so the batch is genuinely concurrent. Include the batch, Packages, authorization reference, independence evidence, worker identities, and dispatch time in the returned batch record; the parent Executor writes that record to progress. Do not launch a second batch while this one is active.

## Reconcile worker claims

Wait for every worker in the batch. Preserve successful outputs when a peer fails; independence means one failure cannot invalidate another by itself. Record for each Package:

- canonical worker status: `DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED`;
- worker identity;
- output and Task Report paths and claimed identities;
- check summary;
- exact concern, missing context, or blocker.

Treat all statuses as claims. Do not inspect deeply enough to accept work, dispatch task review, correct findings, update shared evidence, or integrate results here. Those duties remain with `subagent-driven-reporting` after this Skill returns.

If a worker is missing or still active, return the batch as incomplete and name it; do not redispatch completed or unknown workers. On recovery, reconcile actual worker identities and files before any further dispatch.

## Result and Return Route

Return one concise batch result to `subagent-driven-reporting` with the authorization reference, independence decision, worker/status/path table, incomplete workers, and exact task-level blockers. A successful dispatch means only that worker claims are available. The parent Executor must verify and independently task-review each output before acceptance.

Return every outcome to `subagent-driven-reporting`, including alleged Plan, source, metric, or framing defects. The parent verifies the claim against actual artifacts and owns any later lifecycle Return Route. This scheduler never routes away from its parent on worker status alone.
