---
name: test-data
description: Generate synthetic FPSL and FSDM test data, insert scripts, and fixture builders for batch-oriented functional scenarios using repository metadata and sample evidence.
---

# Test Data

Use this skill for synthetic scenario data and functional test preparation.

## Load Order

1. Read this file.
2. Read [test-data-rules.md](./references/test-data-rules.md).
3. Read [adt-handoff-rules.md](./references/adt-handoff-rules.md).
4. Read [official-sources.md](./references/official-sources.md).

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
