---
name: integration
description: "Use for FSDM-to-FPSL integration orchestration, including change-pointer extraction flow, RFM sequencing, staging design, restart and recovery logic, and technical validation of data-loading pipelines when users need movement and control guidance without collapsing into field-level mapping specs, IMG customizing, or business reconciliation outputs."
---

# Integration

Use this skill for FSDM-to-FPSL data movement and orchestration design.

See [Skill Routing Matrix](../../docs-context/architecture/skill-routing-matrix.md) for clarification on when to use this skill vs. others.

## Load Order

1. Read this file.
2. Read [integration-core-rules.md](./references/integration-core-rules.md) for scope boundaries, trust order, and delivery rules.
3. Read [integration-core-patterns.md](./references/integration-core-patterns.md) for repeatable orchestration patterns, restart logic, and staging choices.
4. Read [fpsl-fsdm-integration-architecture.md](./references/fpsl-fsdm-integration-architecture.md) for DL flow, /FSDL/EXTRACT framing, mapping-view consumption, and runtime checkpoints.
5. Read [fsdm-rfm-extraction-guide.md](./references/fsdm-rfm-extraction-guide.md) when the task needs RFM sequencing, delta logic, or extraction controls.
6. Read [integration-validation.md](./references/integration-validation.md) when the task needs technical completeness checks for extract, stage, or load checkpoints.
7. Read [integration-testing.md](./references/integration-testing.md) when the user asks for test strategy, failure simulation, or restart verification.
8. Read [fpsl-fsdm-2023-golden-source.md](../../docs-context/official/sap/fpsl-fsdm-2023-golden-source.md) when standard SAP/FSDM integration terminology or 2023 architecture details matter.
9. Read [official-sources.md](../../docs-context/shared/official-sources-router.md) when standard product framing matters.
10. Read [adt-handoff-rules.md](../../docs-context/shared/adt-handoff-rules.md) when the output is meant for implementation handoff.

## Trust Order

1. Official SAP documentation for supported integration behavior and terminology
2. Confirmed repository metadata and curated official references
3. Active normalized metadata for actual structures, keys, and file-level evidence
4. Trusted raw metadata when normalization is missing
5. Synthetic examples only for shape

## Workflow

1. Confirm the source system, target layer, and control objective.
2. Separate extraction orchestration from field-level mapping and posting correctness.
3. Identify whether the ask is about full load, delta load, restart, or failure recovery.
4. Build the smallest useful flow first: extract, stage, validate, load, verify status.
5. Keep placeholders explicit for system-specific RFC destinations, jobs, or staging tables.
6. Route downstream coding to `abap` or `amdp`, field specs to `mapping`, and balancing to `reconciliation`.

## Non-Negotiables

- Do not invent RFC destinations, RFM names beyond confirmed SAP-standard examples, staging table names, or scheduler objects.
- Do not turn this skill into field-by-field mapping documentation.
- Do not present business reconciliation as technical flow validation.
- Keep confirmed extraction controls separate from inferred orchestration guidance.
- Make restart points, control totals, and failure boundaries explicit.

## Expected Output

- integration scope summary
- source-to-stage-to-target flow sketch
- extraction and restart controls
- technical validation checkpoints
- confirmed versus inferred implementation notes
- handoff notes for mapping, coding, or reconciliation follow-up
