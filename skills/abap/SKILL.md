---
name: abap
description: Build and review modular ABAP for FPSL and FSDM. Use for orchestration, validation, exception handling, ABAP Unit, wrapper classes, and supportable batch-oriented implementation.
---

# ABAP

Use this skill for ABAP-heavy work in FPSL and FSDM projects.

See [Skill Routing Matrix](../../docs-context/architecture/skill-routing-matrix.md) for clarification on when to use this skill vs. others.

## Load Order

1. Read this file.
2. Read [abap-core-rules.md](./references/abap-core-rules.md) for design and senior-developer guidance.
3. Read [abap-test-patterns.md](./references/abap-test-patterns.md) for ABAP Unit, fixtures, and scenario validation support.
4. Read [adt-handoff-rules.md](./references/adt-handoff-rules.md) when output is meant for Eclipse ADT paste or review.
5. Read [official-sources.md](./references/official-sources.md) when supported ABAP/ADT behavior or official FPSL context matters.

## Trust Order

1. Official SAP documentation for supported ABAP and FPSL capabilities
2. Active normalized repository metadata for actual names, fields, and structures
3. Trusted raw metadata when normalization is missing
4. Synthetic examples only for shape

Do not infer custom classes, interfaces, packages, or field lists from public SAP help pages.

## Workflow

1. Identify the minimal ABAP artifact needed.
2. Keep methods small and responsibilities clear.
3. Use ABAP for orchestration, validations, application semantics, and framework interactions.
4. Generate functional test data, insert scripts, or fixture builders when scenario validation is requested.
5. Split production code from test support cleanly.
6. Return one ADT-ready artifact block at a time with `Artifact`, `Paste target`, `Action`, code, and `Checks`.

## Non-Negotiables

- Do not invent `Z*` object names or interfaces.
- Use neutral placeholders until repo or metadata evidence confirms exact names.
- Make type conversion and rounding behavior explicit.
- Prefer constructor injection or seam-friendly collaborators for testability.
- Use exception chaining with `previous =` when propagating technical failure context.
- Do not assume public product documentation reflects landscape-specific implementation classes.

## Expected Output

- brief assumptions
- class and method responsibility split
- one artifact block at a time for ADT paste
- ABAP implementation
- ABAP Unit scaffold with fixtures
- validation steps
- test-data setup and insert scripts when requested
