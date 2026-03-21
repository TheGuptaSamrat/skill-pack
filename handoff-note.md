# Handoff Note

Use this note to resume work in GitHub Copilot from the current repo state.

## Current State

- repo is modularized into core and focused skills
- current focused additions include `quality`, `reconciliation`, `mapping`, `test-data`, `cvpm`, and `partitioning`
- public repo is sanitized for sharing and keeps only curated docs-context material
- metadata normalization and PDF-ingestion support are present

## Best Resume Flow In GHCP

1. Open this repo beside the Eclipse ADT workspace.
2. Let GHCP load:
   - `.github/copilot-instructions.md`
   - the relevant `.github/instructions/*.instructions.md` file
3. Name the skill explicitly in the prompt for the most reliable routing.
4. Load only the task-specific metadata from `metadata-drop/`.
5. Start from `prompt-library.md` if the user needs a ready-made prompt shape.

## Recommended Prompt Pattern

```text
Use the <skill-name> skill in this repo. Work only from confirmed repository metadata and keep placeholders explicit where customer-specific evidence is missing.
```

## Current Skill Map

- `config` for FPSL configuration guidance
- `quality` for data quality rule generation
- `mapping` for mapping specification generation
- `reconciliation` for investigative SQL and query-based validation
- `test-data` for synthetic test-data generation
- `projections` for trend and size estimation
- `cvpm` for calculation and valuation process design guidance
- `partitioning` for HANA partitioning strategy and review
- `abap` and `amdp` for implementation artifacts

## Practical Watchpoints

- use normalized metadata before prompting when available
- keep CVPM responses evidence-first because customer-specific class, worklist, and thread details may still be missing
- CVPM image-derived implementation evidence is maintained in `skills/cvpm/references/cvpm-balance-snapshot-implementation.md` with raw OCR in `metadata-drop/OtherDocs/CVPM/extracted-ocr.md`
- keep partitioning recommendations tied to table volume, growth, access pattern, and operational evidence
- use `reconciliation` for SQL validation even when the broader topic is CVPM or partitioning

## Recommended Next Work Items

- validate `cvpm` on one real customer scenario with known process-step and job evidence
- validate `partitioning` on one real high-volume FPSL table with runtime and growth evidence
- observe whether GHCP naturally routes well enough or still needs explicit skill naming in practice
