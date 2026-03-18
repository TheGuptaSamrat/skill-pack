# SAP FPSL FSDM Skill Pack

Trimmed multi-skill repository for SAP FPSL and FSDM development.

This repo is designed for:

- Codex-style skill import
- GitLab mirroring
- VS Code with GitHub Copilot as a reference and context repo

For the developer-value summary, read:

- `HOW-IT-ACCELERATES.md`
- `VS_CODE_GHCP_STEP_BY_STEP.md`
- `METADATA_NORMALIZATION.md`
- `docs-context/README.md`

## Repository Shape

Each skill lives under `skills/<skill-name>/` and follows the standard skill layout:

- `SKILL.md`
- `agents/openai.yaml`
- `references/`

Included skills:

- `sap-fpsl-amdp`
- `sap-fpsl-abap`
- `sap-fpsl-configuration`
- `sap-fpsl-tech-docs`

## Metadata Drop

Use `metadata-drop/` for reusable evidence that improves output quality without expanding prompts.

Operating rule:

- raw Excel is treated as trusted source metadata
- normalized metadata is the active working format used by skills by default
- when new source metadata changes the active model materially, impacted outputs should be reverified

- `fpsl/`
  - core structure notes and sample table references
- `fsdm/`
  - model notes and extension metadata
- `cds/`
  - CDS definitions or exported DDL snippets
- `configuration/`
  - sample navigation paths, setup examples, and validation references
- `ddic/`
  - CSV exports for tables, fields, keys, domains, and data elements
- `samples/`
  - safe sample rows and source-to-target examples
- `raw-excel/`
  - trusted source Excel metadata
- `normalized/`
  - active working metadata used by skills by default
- `manifest.csv`
  - source-to-normalized tracking
- `change-review.md`
  - summary of structural changes and reverification needs
- `test-cases/`
  - developer trial cases and feedback pack

## Docs Context

Use `docs-context/` for markdown-derived document corpora.

- `official/`
  - crisp, trusted markdown for direct skill loading
- `training/`
  - compact conceptual notes from training material
- `full-source-md/`
  - section-split markdown for deeper lookup only
- `indexes/`
  - source and topic navigation
- `inbox/`
  - new PDF intake

## How To Use

For Codex:

- import the required skill folder or the full repo
- activate only the skill relevant to the task

For VS Code with GitHub Copilot:

- keep this repo open beside the Eclipse ADT workspace
- use the relevant skill folder as canonical context
- load `metadata-drop/` evidence only for the current task
- keep prompts short and task-specific

Example:

```text
Use the sap-fpsl-amdp skill in this repo. Design the smallest AMDP plus ABAP wrapper for transforming FSDM contract cashflow rows into FPSL posting input. Include tests and validation.
```

## Design Principles

- each skill is narrow and reusable
- prompts should carry only the task delta
- references should ground output in FPSL, FSDM, CDS, and metadata evidence
- placeholder names must remain placeholders unless repo or DDIC evidence confirms exact SAP objects
- user-provided training material should be integrated as derived conceptual guidance, not as the top trust source for object names or active metadata

## Validation

Run:

```bash
./scripts/smoke-check.sh
```
