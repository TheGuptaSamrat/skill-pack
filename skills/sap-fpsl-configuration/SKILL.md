---
name: sap-fpsl-configuration
description: Analyze, document, and guide SAP FPSL configuration work including derivative rules, processing setup, posting-related configuration, master data upload flows, and validation sequences. Use for evidence-first configuration guidance, impact review, configuration handoff, and testing checklists.
---

# SAP FPSL Configuration

Use this skill for configuration-heavy FPSL tasks that still need disciplined technical guidance.

## Load Order

1. Read this file.
2. Read [configuration-delivery-rules.md](./references/configuration-delivery-rules.md).
3. Read [validation-and-tcodes.md](./references/validation-and-tcodes.md) when verification is needed.
4. Read `../../metadata-drop/configuration/` artifacts when sample navigation, validation sequence, or setup examples are available.

## Workflow

1. Identify the exact configuration area and expected business effect.
2. Ask for evidence if the request depends on system-specific setup.
3. Distinguish product-standard configuration from custom extensions.
4. Return a configuration checklist, impact notes, and validation steps.

## Non-Negotiables

- Do not invent IMG paths, node names, customizing tables, or derivative rules.
- Use placeholders if screenshots, extracts, or metadata are missing.
- Make prerequisites and downstream validation explicit.
- Separate confirmed settings from assumptions.
- Prefer repository navigation examples over generic SAP boilerplate when evidence is available.

## Expected Output

- configuration scope summary
- dependency and impact notes
- upload or setup checklist
- validation transactions, logs, or review points
- risks and open assumptions
