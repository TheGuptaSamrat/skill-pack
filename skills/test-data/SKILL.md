---
name: test-data
description: Generate synthetic FPSL and FSDM test data, insert scripts, and fixture builders for batch-oriented functional scenarios using repository metadata and sample evidence.
---

# Test Data

Use this skill for synthetic scenario data and functional test preparation.

See [Skill Routing Matrix](../../docs-context/architecture/skill-routing-matrix.md) for clarification on when to use this skill vs. others.

## Load Order

1. Read this file.
2. Read [test-data-core-rules.md](./references/test-data-core-rules.md).
3. Read [test-data-builders.md](./references/test-data-builders.md) for fixture builder patterns and parametrized dataset generation.
4. Read [test-data-scenarios.md](./references/test-data-scenarios.md) for scenario-based test design (happy path, boundary, error cases, volume).
5. Read [adt-handoff-rules.md](./references/adt-handoff-rules.md).
6. Read [official-sources.md](./references/official-sources.md).

## Trust Order

1. Official SAP documentation for product terminology only
2. Active normalized metadata for actual field shape
3. Trusted raw metadata when normalization is missing
4. Synthetic examples only for shape and defaults

## Workflow

1. Confirm the test scenario and checkpoint being validated.
2. Identify mandatory attributes and likely batch-driving fields.
3. Generate the smallest useful data set for the scenario.
4. Keep synthetic assumptions visible.

## Non-Negotiables

- Keep synthetic values clearly labeled.
- Do not invent confirmed structures when metadata is incomplete.
- Include validation expectations with the generated data.

## Expected Output

- scenario assumptions
- insert scripts or fixture builders
- required attributes list
- validation expectations
- unresolved placeholders if needed
