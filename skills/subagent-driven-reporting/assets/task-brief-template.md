<!-- Template use: render every heading, label, table header, placeholder replacement, and narrative passage in the confirmed artifact language. The sample title's “Work Package Task Brief” phrase is a translatable artifact-type label, not a canonical identifier. Preserve canonical codes and IDs, exact Skill names, paths, hashes, citations, code, formulas, and original source titles. Remove this and every Template instruction comment from the instantiated artifact. -->

# Evidencecraft Work Package Task Brief

## Identity

- Report Plan path / identity:
- Run ID:
- Work Package ID / title:
- Brief status: `FROZEN FOR DISPATCH`
- Interaction language: [frozen; workers do not contact the user]
- Artifact language: [required for output, Task Report, and task review]
- Terminology and source-title handling: [frozen translation and preservation rules]
- Prepared at:
- Decision use / report section served:

## Goal and boundary

- Exact task goal:
- In scope:
- Out of scope:
- Dependencies that must already be accepted:
- Downstream consumers:

## Governed inputs

| Role | Exact path / locator | Identity | Required use |
|---|---|---|---|
| Analysis Brief |  |  |  |
| Source Profile(s) |  |  |  |
| Metric Definition(s) |  |  |  |
| Accepted upstream output(s) |  |  |  |
| Raw or qualified source evidence |  |  |  |

## Binding semantic rules

- Population / eligibility:
- Grain / keys / deduplication:
- Period / time basis / timezone:
- Categories / mappings:
- Formula / numerator / denominator:
- Aggregation / comparison:
- Missing, pending, or invalid data:
- Qualifications that must propagate:

## Read and write scope

- Allowed reads:
- Unique worker output path:
- Task Report path:
- Other allowed writes, if any:
- Forbidden shared writes: progress, evidence log, report draft, Review Package, other worker artifacts, final report.

## Required output

- Output format and fields:
- Required intermediate calculations / extracts:
- Precise evidence paths, locators, and Evidence IDs to retain for governance:
- Identity method:
- Audience boundary: this output and its Task Report are internal governance inputs; do not write or save the reader report.

## Acceptance checks

| Check ID | Method / command | Expected result | Evidence to record |
|---|---|---|---|
|  |  |  |  |

## Stop conditions and Return Routes

- Missing access or source fitness → `profiling-evidence`.
- Reusable metric ambiguity or mapping defect → `defining-metrics`.
- Work Package, dependency, output, or check defect → `writing-report-plans`.
- Audience, use, question, or scope change → `framing-analysis`.
- Execution defect under unchanged semantics → this Work Package in `subagent-driven-reporting`.

Do not guess, redesign semantics, contact the user, integrate other packages, or save the final report.
