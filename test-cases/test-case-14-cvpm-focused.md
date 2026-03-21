# Test Case 14: CVPM Focused Skill

Use the `cvpm` skill only.

## Scenario

You need guidance for an FPSL calculation and valuation process design for a periodic valuation requirement. The user provides some process evidence, target process steps, and partial implementation notes, but not all customer-specific class or worklist details.

## Prompt

```text
Use the cvpm skill in this repo. Propose the smallest useful CVPM design note for a periodic valuation process. Separate confirmed setup from inferred setup. Include process-step sequence, method guidance, worklist/thread placeholders where evidence is missing, and validation follow-up actions.
```

## Success Criteria

- does not invent class names, job names, worklist objects, or thread settings
- clearly separates confirmed and inferred setup
- gives a usable process-step and method view
- routes coding or SQL follow-up to the right companion skills
