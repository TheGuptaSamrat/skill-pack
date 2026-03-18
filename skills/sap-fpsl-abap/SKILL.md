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

## Workflow

1. Identify the minimal ABAP artifact needed.
2. Keep methods small and responsibilities clear.
3. Use ABAP for orchestration, validations, application semantics, and framework interactions.
4. Split production code from test support cleanly.
5. Return paste-ready artifact blocks for ADT.

## Non-Negotiables

- Do not invent `Z*` object names or interfaces.
- Use neutral placeholders until repo or metadata evidence confirms exact names.
- Make type conversion and rounding behavior explicit.
- Prefer constructor injection or seam-friendly collaborators for testability.
- Use exception chaining with `previous =` when propagating technical failure context.

## Expected Output

- brief assumptions
- class and method responsibility split
- ABAP implementation
- ABAP Unit scaffold with fixtures
- validation steps
