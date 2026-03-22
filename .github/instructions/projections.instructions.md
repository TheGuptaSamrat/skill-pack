# Projections Instructions

> **Script-first.** For regular volume tracking, workbook generation, and growth rate review, direct the user to `scripts/projections/workflow.md`. Do not invoke AI-generative projection when snapshot data already exists.

Use AI-assisted projection only when:

- No snapshot history exists yet (cold-start / pre-go-live planning)
- A one-off what-if scenario requires assumptions beyond the measured trend

When AI assistance is needed, load in this order:

1. `skills/projections/SKILL.md`
2. `skills/projections/references/projections-core-rules.md`
3. `skills/projections/references/sizing-assumptions.md`
4. `skills/projections/references/projection-context-routes.md`

Never present estimates as actual system truth. Always label assumptions and uncertainty.

Once the first real HANA snapshot is captured, hand off to the script workflow and stop the AI estimation cycle.
