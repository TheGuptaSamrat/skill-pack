# Test Case 14: CVPM Focused Skill

Use the `cvpm` skill only.

## Scenario

You need guidance for an FPSL calculation and valuation process design for a periodic valuation requirement. The user provides:

- target process steps such as register, defer, value, or classify
- partial method notes from business or functional design
- some implementation evidence
- no confirmed customer-specific class, worklist, or thread details yet

## Prompt

```text
Use the cvpm skill in this repo. Propose the smallest useful CVPM design note for a periodic valuation requirement. Separate confirmed setup from inferred setup. Include process-step sequence, method guidance, worklist and thread placeholders where evidence is missing, implementation handoff notes, and validation follow-up actions.
```

## Success Criteria

- does not invent class names, job names, worklist objects, or thread settings
- clearly separates confirmed and inferred setup
- gives a usable process-step and method view
- includes implementation handoff notes for follow-up in `abap` or `amdp`
- routes coding or SQL follow-up to the right companion skills
