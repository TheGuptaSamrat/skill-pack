# SAP FPSL FSDM Skill Pack

Trimmed multi-skill repository for SAP FPSL and FSDM development.

This repo is designed for:

- Codex-style skill import
- GitLab mirroring
- VS Code with GitHub Copilot as a reference and context repo

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

## How To Use

For Codex:

- import the required skill folder or the full repo
- activate only the skill relevant to the task

For VS Code with GitHub Copilot:

- keep this repo open beside the Eclipse ADT workspace
- use the relevant skill folder as canonical context
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

## Validation

Run:

```bash
./scripts/smoke-check.sh
```
