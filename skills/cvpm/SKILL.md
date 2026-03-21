---
name: cvpm
description: Guide FPSL calculation and valuation process design using evidence-first process-step, method, worklist, and threading guidance. Use for CVPM job structure, run design, and validation planning.
---

# CVPM

Use this skill for FPSL calculation and valuation process design and review.

## Load Order

1. Read this file.
2. Read [fpsl-process-steps-reference.md](./references/fpsl-process-steps-reference.md) for authoritative FPSL standard process steps (Register, Accrue, Defer, Value FX, Classify, etc.).
3. Read [cvpm-core-rules.md](./references/cvpm-core-rules.md).
4. Read [cvpm-implementation-patterns.md](./references/cvpm-implementation-patterns.md).
5. Read [cvpm-process-design-guide.md](./references/cvpm-process-design-guide.md) for complete FPSL process-step deep dives, method mapping, and run strategy.
6. Read [cvpm-configuration-tables.md](./references/cvpm-configuration-tables.md) for configuration object hierarchy and customizing setup.
7. Read [cvpm-method-design.md](./references/cvpm-method-design.md) for method type patterns and implementation guidance.
8. Read [cvpm-data-integration.md](./references/cvpm-data-integration.md) for data staging and integration workflows.
9. Read [cvpm-validation.md](./references/cvpm-validation.md).
10. Read [fpsl-cvpm-operational-monitoring.md](./references/fpsl-cvpm-operational-monitoring.md) for FPSL CVPM Monitor guidance, periodic task verification, system setup, and troubleshooting frameworks.
11. Read [official-sources.md](./references/official-sources.md) when standard FPSL framing matters.

## Trust Order

1. Official SAP documentation and confirmed customer evidence for actual CVPM setup
2. Active normalized metadata and repository extracts for concrete structures
3. Reviewed training-derived FPSL process concepts for method and process-step framing
4. Trusted raw metadata when normalization is missing
5. Synthetic examples only for output shape

Do not derive actual customer class names, worklist IDs, thread settings, or job definitions from generic training content alone.

## Workflow

1. Confirm the accounting goal, process cadence, and affected FPSL process steps.
2. Separate standard FPSL process-step behavior from customer implementation choices.
3. Use the training-derived process model to frame methods such as register, defer, value, classify, and related valuation steps.
4. Ask for or preserve placeholders for customer-specific class, method, worklist, and threading evidence.
5. Return the smallest useful CVPM design artifact first.

## Non-Negotiables

- Do not invent CVPM job names, class names, worklist objects, or thread configuration values.
- Keep confirmed setup separate from inferred implementation guidance.
- Make process-step sequence and method dependencies explicit.
- Route mapping work to `mapping`, validation SQL to `reconciliation`, quality rules to `quality`, and code artifacts to `abap` or `amdp`.

## Expected Output

- CVPM scope summary
- process-step and method design notes
- job, worklist, and threading guidance with placeholders when needed
- confirmed versus inferred setup
- validation and follow-up actions
