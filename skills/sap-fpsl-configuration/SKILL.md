---
name: sap-fpsl-configuration
description: Analyze, document, and guide SAP FPSL configuration work including derivative rules, processing setup, posting-related configuration, master data upload flows, and validation sequences. Use for evidence-first configuration guidance, impact review, configuration handoff, and testing checklists.
---

# SAP FPSL Configuration

Use this skill for configuration-heavy FPSL tasks that still need disciplined technical guidance.

## Load Order

1. Read this file.
2. Read [configuration-core-rules.md](./references/configuration-core-rules.md).
3. Read [validation-and-tcodes.md](./references/validation-and-tcodes.md) when verification is needed.
4. Read `../../metadata-drop/configuration/` artifacts when sample navigation, validation sequence, or setup examples are available.
5. Read [official-sources.md](./references/official-sources.md) when you need official FPSL/FSDM scope anchors.
6. Use this skill for guided operational verification, checklists, and evidence-led process review; route set-based SQL and data-presence checks to `sap-fpsl-amdp`.

## Trust Order

1. Official SAP documentation for product scope and standard integration concepts
2. Confirmed repository metadata, screenshots, extracts, or setup evidence
3. Trusted raw metadata where relevant
4. Training-derived conceptual guidance for operational context
5. Synthetic samples only for checklist shape

Do not derive actual IMG node names, customizing entries, or derivative rule content from public documentation alone.

## Workflow

1. Identify the exact configuration area and expected business effect.
2. Ask for evidence if the request depends on system-specific setup.
3. Distinguish product-standard configuration from custom extensions.
4. Support guided walkthroughs when the user wants step-by-step configuration help.
5. Include process-run verification for accounting processes, register runs, period-end style checkpoints, or setup validation when relevant.
6. Return a configuration checklist, impact notes, and validation steps.

## Non-Negotiables

- Do not invent IMG paths, node names, customizing tables, or derivative rules.
- Use placeholders if screenshots, extracts, or metadata are missing.
- Make prerequisites and downstream validation explicit.
- Separate confirmed settings from assumptions.
- Prefer repository navigation examples over generic SAP boilerplate when evidence is available.
- Clearly state when a response is based on generic product knowledge rather than confirmed system setup.

## Expected Output

- configuration scope summary
- dependency and impact notes
- upload or setup checklist
- validation transactions, logs, or review points
- risks and open assumptions
- guided sequence when requested
- process-run verification checks when requested
