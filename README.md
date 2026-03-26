# SAP FPSL FSDM Skill Pack

Structured skill-pack and context repository for AI-assisted SAP FPSL and FSDM development.

This repo is designed for:

- structured skill-pack import
- GitLab mirroring
- VS Code with GitHub Copilot as a reference and context repo

It is designed for teams developing in Eclipse ADT while using VS Code with GitHub Copilot as the AI interaction and context workspace.

For a quick orientation to the codebase structure and key technologies, read:

- `codebase.md`

For the developer-value summary, read:

- `how-it-accelerates.md`
- `vs-code-ghcp-step-by-step.md`
- `metadata-normalization.md`
- `prompt-library.md`
- `docs-context/README.md`
- `docs-context/indexes/update-policy.md`
- `docs-context/indexes/versioning-convention.md`

## Repository Shape

Each skill lives under `skills/<skill-name>/` and follows the standard skill layout:

- `SKILL.md`
- `agents/`
- `references/`

For standard VS Code + GitHub Copilot use, the repo also includes:

- `.github/copilot-instructions.md`
- `.github/instructions/*.instructions.md`

These instruction files provide a GHCP-friendly routing layer while keeping the `skills/` directory as the canonical design structure.

Core skills:

- `amdp`
- `abap`
- `config`
- `integration`

Focused skills:

- `quality`
- `reconciliation`
- `mapping`
- `test-data`
- `cvpm`
- `partitioning`

Script-driven (no AI invocation):

- `projections` — use `scripts/projections/` workflow; AI only for cold-start planning

## Metadata Drop

Use `metadata-drop/` for reusable evidence that improves output quality without expanding prompts.
Treat it as shared golden context, not as the place for requirement-specific working notes.

Operating rule:

- raw Excel is treated as trusted source metadata
- normalized metadata is the active working format used by skills by default
- when new source metadata changes the active model materially, impacted outputs should be reverified
- requirement-specific logic should move into `implementation/`, not shared metadata

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
- `change-log.md`
  - summary of structural changes and reverification needs
- `test-cases/`
  - developer trial cases and feedback pack

## Implementation Packs

Use `implementation/` as the shared memory for project-specific work.

Each implementation pack should hold:

- requirement summary and intent
- confirmed metadata references
- requirement-specific logic
- curated examples
- implementation notes
- validation, debugging, and enhancement history

Operating rule:

- raw Excel, PDF, DOCX, screenshots, and temporary extraction outputs may stay local
- commit only curated outputs that help future delivery
- if something proves reusable across multiple requirements, it can later be promoted into `metadata-drop/`

## Docs Context

Use `docs-context/` for markdown-derived document corpora.

- `official/`
  - crisp, trusted markdown for direct skill loading
- `training/`
  - compact conceptual notes from training material
- `indexes/`
  - source and topic navigation
- `inbox/`
  - new PDF intake

Tech-head governance:

- newer documents should enter as candidates, not automatically replace curated context
- versioned source history should remain visible
- curated topic files should stay stable even as source versions change

## How To Use

For skill-pack consumers:

- import the required skill folder or the full repo
- activate only the skill relevant to the task

For VS Code with GitHub Copilot:

- keep this repo open beside the Eclipse ADT workspace
- let GitHub Copilot pick up `.github/copilot-instructions.md` and the relevant `.github/instructions/*.instructions.md` file first
- treat `.github/instructions/` as the primary GHCP activation and routing layer for day-to-day use
- use `skills/` as the deeper canonical design layer when the task needs stricter delivery rules or more context
- load `metadata-drop/` evidence only for the current task
- prefer task-first prompts that reference an implementation pack when one exists
- name the skill explicitly only when the task is ambiguous or you want to override routing
- keep prompts short and task-specific

Example:

```text
Build from the implementation pack for this requirement. Use approved metadata first and keep placeholders explicit where object names are not confirmed.
```

Use-case mapping:

- `config` for setup and navigation guidance
- `integration` for FSDM-to-FPSL extraction orchestration, staging flow, restart control design, and technical load validation
- `quality` for SDL/RDL-style data quality rules
- `mapping` for source-to-target mapping specs
- `reconciliation` for SQL checks, counts, totals, and data-flow validation
- `test-data` for synthetic FPSL/FSDM test data
- `projections` — script-driven; use `scripts/projections/workflow.md` for all regular tracking; AI only for cold-start planning without snapshot data

Additional focused engineering skills:

- `cvpm` for FPSL calculation and valuation process job design, method framing, worklists, and thread configuration guidance
- `partitioning` for HANA partition strategy and SAP-aligned partition recommendations for FPSL-relevant tables

## Design Principles

- each skill is narrow and reusable
- prompts should carry only the task delta
- references should ground output in FPSL, FSDM, CDS, and metadata evidence
- placeholder names must remain placeholders unless repo or DDIC evidence confirms exact SAP objects
- user-provided training material should be integrated as derived conceptual guidance, not as the top trust source for object names or active metadata
- keep durable guidance in skill references and indexed docs; avoid session or review-style summary files in the root workflow
- requirement-specific logic should accumulate in implementation packs, not shared metadata

## Validation

Run:

```bash
./scripts/smoke-check.sh
```

Smoke check now includes filename-convention validation (`scripts/validate_file_naming.py`) so non-special files remain lowercase kebab-style.
This convention applies to filenames only. SAP technical identifiers inside content and outputs must preserve SAP casing (for example `/BA1/C55POSTD`, `/BA1/HFSPD`).

For redundancy and context-efficiency auditing, run:

```bash
./scripts/run-context-optimization.sh
```
