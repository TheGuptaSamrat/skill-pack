# Test Case 16: Integration Focused Skill

Use the `integration` skill only.

## Scenario

You need guidance for an FSDM-to-FPSL data-loading flow. The user provides:

- a source object cohort such as contracts, instruments, or business transactions
- a requirement for either full load or delta load
- partial evidence about staging or extraction controls
- no confirmed customer-specific scheduler, RFC destination, or staging table names yet

## Prompt

```text
Use the integration skill in this repo. Propose the smallest useful design note for an FSDM-to-FPSL data-loading flow. Keep source, stage, and target checkpoints explicit. Include extraction sequencing, restart logic, technical validation checks, confirmed versus inferred controls, and handoff notes for mapping, coding, or reconciliation follow-up.
```

## Success Criteria

- does not invent customer-specific RFC destinations, staging tables, or scheduler objects
- clearly separates confirmed controls from inferred orchestration guidance
- explains the extract, stage, validate, and load checkpoints cleanly
- includes restart or retry notes
- routes field mapping, code, and balancing follow-up to the right companion skills
