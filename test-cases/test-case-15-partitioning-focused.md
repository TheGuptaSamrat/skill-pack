# Test Case 15: Partitioning Focused Skill

Use the `partitioning` skill only.

## Scenario

You need a HANA partitioning recommendation for a high-volume FPSL-relevant table. The user provides table identity, growth context, and workload concerns, but not a full approved DB design.

## Prompt

```text
Use the partitioning skill in this repo. Review whether partitioning is justified for the provided FPSL-relevant table. Base the answer on table volume, growth, access pattern, and operational implications. Include assumptions, a recommendation or no-go view, and validation steps.
```

## Success Criteria

- does not present partitioning as a default
- does not invent DB settings or approved partition layout
- explains the operational trade-offs
- includes validation and Basis/HANA coordination points
