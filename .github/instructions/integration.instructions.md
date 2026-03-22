# Integration Instructions

Use this instruction set when the task is primarily about:

- FSDM-to-FPSL extraction orchestration
- change-pointer based delta loading
- RFM sequencing and control flow
- staging design and restart logic
- technical validation of extract, stage, and load checkpoints

Load in this order:

1. `skills/integration/SKILL.md`
2. `skills/integration/references/integration-core-rules.md`
3. `skills/integration/references/integration-core-patterns.md`
4. `skills/integration/references/fpsl-fsdm-integration-architecture.md`
5. `skills/integration/references/integration-validation.md`

Open `skills/integration/references/fsdm-rfm-extraction-guide.md` only when the task needs RFM mechanics or change-pointer extraction details.
Open `skills/integration/references/integration-testing.md` only when the task is specifically about test strategy or recovery simulation.

Routing rule:

- Use `integration` for movement and orchestration of data between source, stage, and target layers.
- Route field-level mapping specs to `mapping`, business balancing to `reconciliation`, schema rules to `quality`, IMG setup to `config`, CVPM-specific process design to `cvpm`, and code artifacts to `abap` or `amdp`.
