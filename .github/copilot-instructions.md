# Copilot Instructions

This repository is a compact SAP FPSL/FSDM skill pack.

When responding:

- load only one skill folder unless the task clearly spans multiple skills
- prefer `.github/instructions/*.instructions.md` in standard VS Code + GitHub Copilot workflows
- use `skills/<skill-name>/SKILL.md` as the canonical detailed guidance behind each instruction set
- treat `skills/<skill-name>/SKILL.md` as the primary instruction file
- load references from that same skill only when needed
- prefer official SAP references for supported product behavior and repository metadata for actual landscape structure
- prefer `docs-context/official/` and `docs-context/training/` over `docs-context/full-source-md/` unless a deeper lookup is required
- do not invent SAP object names, package names, CDS names, DDIC fields, or `Z*` artifacts
- use placeholders when exact objects are not confirmed by repository metadata or user input
- keep outputs compact, modular, and paste-friendly for Eclipse ADT

Recommended mapping:

- `sap-fpsl-amdp` for HANA pushdown, SQLScript, AMDP wrappers, CDS table functions, and set-based transformations
- `sap-fpsl-abap` for OO ABAP, orchestration, validations, exceptions, ABAP Unit, and clean modular implementation
- `sap-fpsl-configuration` for FPSL configuration flows, derivative rules, CVPM-style setup, master data upload guidance, and validation checklists
- `sap-fpsl-tech-docs` for technical documentation, metadata-driven descriptions, handoff docs, and code-generation context from DDIC, CDS, and FSDM metadata
- `sap-fpsl-projections` for yearly or monthly volume growth, DB-size estimation, and trend projections with explicit assumptions

VS Code routing files:

- `.github/instructions/amdp.instructions.md`
- `.github/instructions/abap.instructions.md`
- `.github/instructions/configuration.instructions.md`
- `.github/instructions/tech-docs.instructions.md`
- `.github/instructions/projections.instructions.md`
