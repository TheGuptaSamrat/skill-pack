---
name: sap-fpsl-abap
description: Design, implement, review, and refactor modular ABAP for SAP FPSL and FSDM delivery. Use for orchestration logic, validations, exception handling, ABAP Unit, clean OO design, wrapper classes, batch flows, and supportable code generation around FPSL and FSDM processing.
---

# SAP FPSL ABAP

Use this skill for ABAP-heavy work in FPSL and FSDM projects.

## Load Order

1. Read this file.
2. Read [abap-delivery-rules.md](./references/abap-delivery-rules.md) for design and code patterns.
3. Read [test-and-exception-patterns.md](./references/test-and-exception-patterns.md) for ABAP Unit and exception handling.
4. Read [official-sources.md](./references/official-sources.md) when supported ABAP/ADT behavior or official FPSL context matters.

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
6. Return paste-ready artifact blocks for ADT.

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
- ABAP implementation
- ABAP Unit scaffold with fixtures
- validation steps
- test-data setup and insert scripts when requested
