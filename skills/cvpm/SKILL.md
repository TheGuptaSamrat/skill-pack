---
name: cvpm
description: "Use for FPSL CVPM design and review, including process-step sequencing, method selection, worklist and threading decisions, run-structure planning, and validation framing based on confirmed evidence, when users need practical calculation and valuation job guidance without fabricating implementation-specific customer objects."
---

# CVPM

Use this skill for FPSL calculation and valuation process design and review.

See [Skill Routing Matrix](../../docs-context/architecture/skill-routing-matrix.md) for clarification on when to use this skill vs. others.

## Load Order

1. Read this file.
2. Read [fpsl-process-steps-reference.md](./references/fpsl-process-steps-reference.md) for authoritative FPSL standard process steps (Register, Accrue, Defer, Value FX, Classify, etc.).
3. Read [cvpm-core-rules.md](./references/cvpm-core-rules.md).
4. Read [cvpm-implementation-patterns.md](./references/cvpm-implementation-patterns.md).
5. Read [cvpm-process-design-guide.md](./references/cvpm-process-design-guide.md) for complete FPSL process-step deep dives, method mapping, and run strategy.
6. Read [cvpm-configuration-tables.md](./references/cvpm-configuration-tables.md) for configuration object hierarchy and customizing setup.
7. Read [cvpm-method-design.md](./references/cvpm-method-design.md) for method type patterns and implementation guidance.
8. Read [cvpm-balance-snapshot-implementation.md](./references/cvpm-balance-snapshot-implementation.md) for image-derived implementation order, sequence design, and monitor evidence patterns.
9. Read [cvpm-data-integration.md](./references/cvpm-data-integration.md) for data staging and integration workflows.
10. Read [cvpm-validation.md](./references/cvpm-validation.md).
11. Read [fpsl-cvpm-operational-monitoring.md](./references/fpsl-cvpm-operational-monitoring.md) for FPSL CVPM Monitor guidance, periodic task verification, system setup, and troubleshooting frameworks.
12. Read [official-sources.md](../../docs-context/shared/official-sources-router.md) when standard FPSL framing matters.

## Progressive Reading Paths

**Choose your path based on your goal:**

### ⚡ Fast Path (25% of content, ~30 min)
*Goal: Understand CVPM job structure and design basics*

**Read Steps:**
1. This file
2. fpsl-process-steps-reference.md → **[Fast Path only](./references/fpsl-process-steps-reference.md)** (pages 1-50: Register only)
3. cvpm-core-rules.md
4. cvpm-implementation-patterns.md (skim patterns only, don't memorize)
5. cvpm-process-design-guide.md → Introduction section only
6. cvpm-configuration-tables.md → Process Type Master section only

**Skip:** validation, data-integration details, operational monitoring (for now)

**Output:** Job structure sketch, threading decision, basic pattern selection

---

### 📖 Full Path (100% of content, ~2 hours)
*Goal: Production-ready CVPM design and implementation*

**Read Steps:** All 12 steps in Load Order sequence

**Depth:** Read all sections, reference sections, code examples

**Output:** Complete CVPM design document, implementation roadmap, method specifications

---

### 🔧 Troubleshooting Path (30% of content, ~40 min)
*Goal: Debug failing CVPM job or periodic task*

**Read Steps:**
1. This file
2. cvpm-core-rules.md (rules section only)
3. cvpm-validation.md (all)
4. fpsl-cvpm-operational-monitoring.md (all)
5. fpsl-process-steps-reference.md → **[Troubleshooting Path](./references/fpsl-process-steps-reference.md)** (operations sections only)

**Skip:** method design, configuration hierarchy (unless config issue)

**Output:** Debugging checklist, error resolution, operational guidance

---

## Trust Order

1. Official SAP documentation and confirmed customer evidence for actual CVPM setup
2. Active normalized metadata and repository extracts for concrete structures
3. Reviewed training-derived FPSL process concepts for method and process-step framing
4. Trusted raw metadata when normalization is missing
5. Synthetic examples only for output shape

Do not derive actual customer class names, worklist IDs, thread settings, or job definitions from generic training content alone.

## Workflow

1. Confirm the accounting goal, process cadence, and affected FPSL process steps.
2. Separate standard FPSL process-step behavior from customer implementation choices.
3. Use the training-derived process model to frame methods such as register, defer, value, classify, and related valuation steps.
4. Ask for or preserve placeholders for customer-specific class, method, worklist, and threading evidence.
5. Return the smallest useful CVPM design artifact first.

## Image-Derived Implementation Guidance

Use the OCR-derived CVPM evidence for practical implementation asks:

1. server/worklist class
2. CVPM execution class
3. server entry for primary data source
4. primary data source (PDS)
5. analytical process
6. custom step sequence
7. run + monitor

When the user asks for "where to configure", provide navigation as:

- `Financial Products Subledger -> Data Loading Process -> Data Sources for Worklists`
- `Financial Products Subledger -> Calculation and Valuation Process Manager (CVPM) -> General Settings for Custom Processes -> Edit Analytical Processes`
- `Financial Products Subledger -> Calculation and Valuation Process Manager (CVPM) -> General Settings for Custom Processes -> Edit Custom Step Sequences for Analytical Processes`
- `Financial Products Subledger -> Calculation and Valuation Process Manager (CVPM) -> /BAL/PW_PROCMON`

Use these observed sample controls when shaping checklists (as placeholders, not defaults):

- process parameters: `/BA1/C11SRCSY`, `/BA1/C55LGENT`, `/BA1/C55POSTD`, `/BA1/CROTSTMP`
- step sequence pattern: `15 Enrich Parameters`, `20 Worklist Creation`, `30 Data Enrichment`
- monitor evidence style: run start/end, step sequence, source-data timestamp, package and record counts

Treat screenshot metrics (for example, package/record volumes) as scale indicators only.

## Non-Negotiables

- Do not invent CVPM job names, class names, worklist objects, or thread configuration values.
- Do not reuse screenshot-specific `Z*` object names as customer defaults.
- Keep confirmed setup separate from inferred implementation guidance.
- Make process-step sequence and method dependencies explicit.
- Route mapping work to `mapping`, validation SQL to `reconciliation`, quality rules to `quality`, and code artifacts to `abap` or `amdp`.

## Expected Output

- CVPM scope summary
- process-step and method design notes
- job, worklist, and threading guidance with placeholders when needed
- confirmed versus inferred setup
- validation and follow-up actions

## Local Evidence Pack

- [extracted-ocr.md](../../metadata-drop/OtherDocs/CVPM/extracted-ocr.md)
- [cvpm-balance-snapshot-implementation.md](./references/cvpm-balance-snapshot-implementation.md)
