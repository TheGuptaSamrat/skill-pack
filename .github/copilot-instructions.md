# Copilot Instructions

This repository is a compact SAP FPSL/FSDM skill pack.

When responding:

- load only one skill area unless the task clearly spans multiple skills
- use `.github/instructions/*.instructions.md` as the primary GHCP routing layer in standard VS Code workflows
- use `skills/<skill-name>/SKILL.md` as the deeper canonical guidance behind each instruction set
- load references from that same skill only when needed
- prefer official SAP references for supported product behavior and repository metadata for actual landscape structure
- prefer `docs-context/official/` and `docs-context/training/` for public-repo document context
- do not invent SAP object names, package names, CDS names, DDIC fields, or `Z*` artifacts
- use placeholders when exact objects are not confirmed by repository metadata or user input
- keep outputs compact, modular, and paste-friendly for Eclipse ADT

Routing note:

- GHCP should usually route correctly from task intent, but pilot users should name the skill explicitly in the prompt when they want the most reliable behavior.

Recommended mapping:

- `amdp` for HANA pushdown, SQLScript, AMDP wrappers, and CDS table functions
- `abap` for OO ABAP, orchestration, validations, exceptions, and ABAP Unit
- `config` for FPSL configuration flows, derivative rules, setup guidance, and validation checklists
- `quality` for structural data conformance validation: DDIC-driven rules such as completeness, consistency, key, null, and domain checks
- `projections` — script-driven; run `scripts/projections/workflow.md` for all regular volume tracking; invoke AI only for cold-start planning when no snapshot data exists
- `reconciliation` for business data verification: SQL checks, data-flow validation, totals, cross-process key integrity, and process-run verification from data
- `mapping` for source-to-target mapping specs with confirmed, inferred, and unresolved sections
- `test-data` for synthetic scenario data, insert scripts, fixture builders, and batch-style functional test preparation
- `cvpm` for FPSL calculation and valuation process design, method framing, worklist guidance, and thread-aware implementation review
- `partitioning` for HANA partitioning strategy, table-growth review, and SAP-aligned operational partition guidance

VS Code routing files:

- `.github/instructions/amdp.instructions.md`
- `.github/instructions/abap.instructions.md`
- `.github/instructions/config.instructions.md`
- `.github/instructions/quality.instructions.md`
- `.github/instructions/projections.instructions.md`
- `.github/instructions/reconciliation.instructions.md`
- `.github/instructions/mapping.instructions.md`
- `.github/instructions/test-data.instructions.md`
- `.github/instructions/cvpm.instructions.md`
- `.github/instructions/partitioning.instructions.md`
