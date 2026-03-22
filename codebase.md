# Codebase Guide

> Quick orientation for anyone exploring this repository for the first time.

---

## What This Repository Is

**SAP FPSL/FSDM Skill Pack** — A structured context repository for AI-assisted development on
SAP Financial Products Subledger (FPSL) and Financial Supply Chain Data Model (FSDM) projects.

The repository is designed to work alongside two tools:

- **Eclipse ADT** — where SAP ABAP / AMDP code is written and activated
- **VS Code with GitHub Copilot** — where AI-assisted generation and context loading happens

The core principle:

> The repository carries durable context. The developer prompt carries only the task-specific
> delta.

This means developers write short, focused prompts instead of large ones that re-explain SAP
conventions every session. See `how-it-accelerates.md` for the value model.

---

## Key Technologies

| Layer | Technology | Role |
|---|---|---|
| AI tooling | GitHub Copilot (VS Code) | Prompt routing and code generation |
| Development IDE | Eclipse ADT | ABAP activation and transport management |
| Database | SAP HANA | Runtime for AMDP / SQLScript pushdown |
| Content format | Markdown, CSV | Skills, references, and metadata |
| Agent definitions | YAML (OpenAI format) | Skill-level agent configuration |
| Automation scripts | Python 3 | Excel normalization, link validation, PDF ingestion, redundancy audit |
| Smoke testing | Bash + Python | Filename convention and link checks |
| Task integration | VS Code `tasks.json` | One-click metadata normalization |
| Context files | JSON | PDF extraction configuration for `docs-context/inbox/` |

---

## Directory Tree

```text
skill-pack/
│
├── README.md                        # Entry point: shape, usage, design principles
├── codebase.md                      # This file — orientation guide
├── how-it-accelerates.md            # Value summary, metrics, expected outcomes
├── vs-code-ghcp-step-by-step.md     # Step-by-step workflow for Eclipse ADT + VS Code + GHCP
├── metadata-normalization.md        # Excel → CSV normalization process
├── prompt-library.md                # Starter prompts for every skill
│
├── .github/
│   ├── copilot-instructions.md      # Master routing and trust rules for GitHub Copilot
│   ├── reference-naming-standards.md
│   └── instructions/                # Skill-specific routing files (one per skill)
│       ├── abap.instructions.md
│       ├── amdp.instructions.md
│       ├── config.instructions.md
│       ├── integration.instructions.md
│       ├── quality.instructions.md
│       ├── reconciliation.instructions.md
│       ├── mapping.instructions.md
│       ├── test-data.instructions.md
│       ├── cvpm.instructions.md
│       ├── partitioning.instructions.md
│       └── projections.instructions.md
│
├── skills/                          # Canonical skill packs (11 active)
│   ├── abap/                        # OO ABAP, orchestration, exceptions, ABAP Unit
│   ├── amdp/                        # AMDP, SQLScript, CDS table functions
│   ├── config/                      # FPSL guided configuration and checklists
│   ├── integration/                 # FSDM-to-FPSL orchestration, staging, restart, validation
│   ├── quality/                     # DDIC-driven data quality rules
│   ├── reconciliation/              # Cross-process totals, counts, data-flow checks
│   ├── mapping/                     # Source-to-target mapping specs
│   ├── test-data/                   # Synthetic FPSL/FSDM test data and insert scripts
│   ├── cvpm/                        # Calculation and valuation process design
│   ├── partitioning/                # HANA partition strategy
│   └── projections/                 # Volume forecasting (script-driven; AI for cold-start only)
│
├── docs-context/                    # Knowledge corpora
│   ├── README.md
│   ├── official/sap/                # Official SAP-derived markdown
│   ├── official/sap-fioneer/        # SAP Fioneer resources
│   ├── training/fpsl/               # Training-derived FPSL conceptual notes
│   ├── training/hana-sql/           # HANA query processing and performance concepts
│   ├── architecture/                # Skill routing matrix and decision trees
│   ├── shared/                      # Cross-skill guidance (ADT handoff, official-sources router)
│   ├── indexes/                     # Topic map, versioning convention, ingestion manifest
│   └── inbox/                       # PDF intake area with extraction config files
│
├── metadata-drop/                   # Evidence repository
│   ├── README.md
│   ├── ddic/current/                # CSV templates for tables, fields, keys, domains, elements
│   ├── ddic/sql/                    # HANA SQL for DDIC extraction
│   ├── cds/                         # CDS DDL snippets
│   ├── fpsl/                        # FPSL core structure notes
│   ├── fsdm/                        # FSDM model notes
│   ├── configuration/               # Sample navigation paths and validation checklists
│   ├── samples/                     # Safe sample rows (e.g., cashflow_rows.sample.csv)
│   ├── raw-excel/                   # Trusted source Excel workbooks (input only)
│   ├── normalized/                  # Active working CSVs (output of normalization script)
│   ├── pdf-resources/               # Source PDFs for knowledge extraction
│   ├── manifest.csv                 # Source-to-normalized tracking
│   └── change-log.md                # Structural change history and reverification notes
│
├── scripts/                         # Automation and validation
│   ├── normalize_excel.py           # Converts Excel workbooks to normalized CSVs
│   ├── validate_file_naming.py      # Enforces lowercase kebab-case filename convention
│   ├── validate_skill_pack_links.py # Checks internal markdown links
│   ├── audit_skill_pack_redundancy.py  # Detects duplicated content across skill files
│   ├── ingest_pdf_context.py        # Converts PDFs to markdown for docs-context/
│   ├── smoke-check.sh               # Runs all validation scripts in sequence
│   ├── run-context-optimization.sh  # Runs redundancy audit and writes reports
│   ├── run-normalization.sh         # Wrapper for normalize_excel.py
│   └── projections/                 # Volume tracking workflow
│       ├── workflow.md              # Repeatable cadence guide
│       ├── hana_volume_snapshot.sql # Weekly snapshot query (run in HANA Studio)
│       ├── volume-snapshots.csv     # Append table-level results here
│       ├── db-size-snapshots.csv    # Append DB disk results here
│       └── generate_projection_workbook.py  # Produces 7-sheet Excel workbook
│
├── test-cases/                      # 16 structured developer trial scenarios
│   ├── README.md
│   ├── feedback-template.md
│   ├── test-case-01-amdp.md         # … through …
│   └── test-case-16-integration-focused.md
│
└── .vscode/
    └── tasks.json                   # VS Code task: run metadata normalization
```

---

## Skill System

Every skill under `skills/<skill-name>/` follows the same three-part layout:

```text
skills/<skill-name>/
├── SKILL.md            # Load order, trust order, workflow, non-negotiables
├── agents/openai.yaml  # OpenAI-format agent definition
└── references/         # Supporting guidance files (2–10 per skill)
```

**`SKILL.md`** is the canonical entry point for each skill. It specifies:

1. Which reference files to load and in what order
2. Trust order (official SAP docs → normalized metadata → raw metadata → synthetic)
3. Workflow steps
4. Non-negotiables (what the skill must never do, e.g. invent Z* object names)

### Skill Categories

| Category | Skills | Notes |
|---|---|---|
| Core | `abap`, `amdp`, `config`, `integration` | Always-relevant engineering disciplines |
| Focused | `quality`, `reconciliation`, `mapping`, `test-data`, `cvpm`, `partitioning` | Task-specific |
| Script-driven | `projections` | AI only for cold-start; use scripts for regular cadence |


### Skill Boundary Quick Reference

| Task | Use |
|---|---|
| DDIC field-level null/domain checks | `quality` |
| Cross-process totals balancing | `reconciliation` |
| FSDM → FPSL mapping spec | `mapping` |
| FSDM → FPSL extract/stage/load orchestration | `integration` |
| ABAP class, method, ABAP Unit | `abap` |
| AMDP / SQLScript / CDS table function | `amdp` |
| FPSL configuration walkthrough | `config` |
| Calculation/valuation process design | `cvpm` |
| HANA partition strategy | `partitioning` |
| Volume and storage forecasting | `projections` |
| Synthetic insert scripts and fixtures | `test-data` |

Full decision trees are in `docs-context/architecture/skill-routing-matrix.md`.

---

## Routing Architecture

GitHub Copilot picks up routing from two layers:

```
.github/copilot-instructions.md          ← master rules (always active)
    └── .github/instructions/<skill>.instructions.md  ← one file per skill (activated by task intent)
            └── skills/<skill>/SKILL.md               ← canonical design layer (loaded on demand)
```

- **`.github/copilot-instructions.md`** — enforces global rules: load one skill only, trust order,
  no invented SAP object names, keep outputs compact.
- **`.github/instructions/`** — 11 skill-specific files, each declaring load order and routing
  rules. These are the primary activation layer for day-to-day VS Code + GitHub Copilot work.
- **`skills/<skill>/SKILL.md`** — the deeper canonical layer, loaded when stricter delivery rules
  or more context are needed.

---

## Metadata Flow

```
metadata-drop/raw-excel/          ← trusted source input (Excel workbooks)
        ↓  scripts/normalize_excel.py
metadata-drop/normalized/         ← active working CSVs (default context for skills)
        ↓  referenced by skills during generation
        →  improved AI output quality
```

DDIC evidence (tables, fields, keys, domains) lives in `metadata-drop/ddic/current/` as CSV
template files. Real DDIC exports replace the templates once available from the SAP system.

---

## Validation and Scripts

Run the full validation suite from the repository root:

```bash
./scripts/smoke-check.sh
```

This checks:

- Filename conventions (lowercase kebab-case for all non-special files)
- Internal markdown link integrity

For content redundancy auditing:

```bash
./scripts/run-context-optimization.sh
```

For Excel → CSV normalization:

```bash
python3 scripts/normalize_excel.py metadata-drop/raw-excel/<workbook>.xlsx
```

---

## Where to Start

| Goal | Read |
|---|---|
| Understand the value proposition | `how-it-accelerates.md` |
| Set up the VS Code + GHCP workflow | `vs-code-ghcp-step-by-step.md` |
| Pick the right skill for a task | `docs-context/architecture/skill-routing-matrix.md` |
| Find ready-made prompts | `prompt-library.md` |
| Add or refresh DDIC metadata | `metadata-drop/ddic/README.md` |
| Understand doc corpus governance | `docs-context/README.md` |
| Run validation | `scripts/smoke-check.sh` |
| Try a structured scenario | `test-cases/README.md` |
