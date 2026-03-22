# SAP Skill Pack Documentation Ingestion Pipeline & Patterns

## Executive Summary

The skill pack uses a controlled, staged ingestion system that balances trustworthiness with flexibility. Core principles: source versioning, explicit review gates, staged promotion from draft → reviewed → active, and deterministic config-driven extraction over ad-hoc copying.

---

## 1. Ingestion Script & Capabilities

### `scripts/ingest_pdf_context.py`

**Purpose:** Convert raw PDFs, `.txt`, or `.md` sources into reviewed, classified markdown documents with provenance metadata.

**Key Features:**

- **Multi-format support:** PDF (via `pdftotext` or `pypdf` library), plain text, or preconverted markdown
- **Config-driven extraction:** JSON config specifies page ranges, section titles, trust usage, and topic tags
- **Automatic fallback chain:** If `pdftotext` unavailable, falls back to `pypdf` library; fails gracefully if neither found
- **Per-section provenance:** Each output markdown includes structured header with:
  - Classification (e.g., `official-source-derived`, `training-derived-concepts`)
  - Source basis (filename + page range)
  - Trust usage constraints (what the material should be used for)
  - Do-not-use constraints (what NOT to use it for)
  - Topics covered (CSV list)

**Workflow:**

```bash
python3 scripts/ingest_pdf_context.py <source.pdf|.txt|.md> <config.json>
```

**Example Ingestion Config Structure** (`config-fpsl-training.json`):

```json
{
  "target_root": "docs-context/inbox/review-drafts/fpsl-training-extracted",
  "sections": [
    {
      "filename": "01-fpsl-architecture-overview.md",
      "title": "FPSL Architecture Overview",
      "classification": "training-derived-concepts",
      "start_page": 1,
      "end_page": 20,
      "trust_usage": "product framing, architecture understanding, data model concepts",
      "do_not_use_for": "customer-specific implementation details, local configuration assumptions",
      "topics": ["FPSL scope", "Universal Journal", "multi-GAAP approach", "subledger architecture", "HANA integration"]
    }
  ]
}
```

**Output Structure:**

```
docs-context/
  inbox/
    review-drafts/
      fpsl-training-extracted/
        01-fpsl-architecture-overview.md
        02-fpsl-process-steps-complete.md
        ... (one file per configured section)
```

**Provenance Header in Each Output File:**

```markdown
Classification: training-derived-concepts
Source basis: fpsl-training.pdf, pages 1-20
Trust usage: product framing, architecture understanding, data model concepts
Do not use for: customer-specific implementation details, local configuration assumptions
Topics covered: FPSL scope, Universal Journal, multi-GAAP approach, subledger architecture, HANA integration

# FPSL Architecture Overview

[extracted content]
```

---

## 2. External Documentation Storage & Organization

### Directory Structure

```
docs-context/
├── official/                          # Curated SAP/Fioneer official material
│   ├── sap/                           # Core official sources
│   │   ├── amdp-supported-capabilities.md
│   │   ├── fpsl-client-setup.md
│   │   ├── fpsl-guided-configuration.md
│   │   ├── fpsl-process-run-validation.md
│   │   ├── fpsl-product-overview.md
│   │   ├── fsdm-fpsl-integration.md
│   │   └── README.md
│   └── sap-fioneer/                   # Partner/derivative sources
├── training/                          # Training-derived concept materials
│   ├── fpsl/
│   │   ├── accounting-process-model.md
│   │   ├── fpsl-architecture-and-data-model.md
│   │   ├── fpsl-architecture-overview.md
│   │   ├── ifrs9-classification-framework.md
│   │   ├── mapping-specification-concepts.md
│   │   ├── projection-and-sizing-concepts.md
│   │   ├── test-data-generation-concepts.md
│   │   ├── worked-examples.md
│   │   ├── worked-examples/
│   │   └── README.md
│   ├── hana-sql/
│   └── README.md
├── shared/                            # Shared router & handoff files
│   ├── official-sources-router.md     # Centralized dispatcher for skill-specific official refs
│   ├── adt-handoff-rules.md           # Eclipse ADT paste/console rules
│   └── README.md
├── inbox/                             # Staging area for extraction
│   ├── review-drafts/
│   │   └── fpsl-training-extracted/   # Staged ingestion awaiting promotion
│   ├── config-fpsl-admin.json         # Ingestion config for admin training
│   ├── config-fpsl-training.json      # Ingestion config for main FPSL training
│   ├── fpsl-pdf-extraction-config.json
│   ├── section-config.template.json   # Template for new ingestion configs
│   └── README.md
├── indexes/                           # Metadata and indexing
│   ├── ingestion-manifest.csv         # Source version inventory & status
│   ├── topic-map.md                   # Canonical topic → file mapping
│   ├── validation-skill-pack.json     # Validation rule set
│   ├── versioning-convention.md       # Version naming scheme
│   ├── update-policy.md               # Lifecycle & promotion rules
│   ├── redundancy-audit.md
│   └── source-catalog.md
├── architecture/
│   └── skill-routing-matrix.md        # When to use which skill
└── README.md
```

### Default Load Order

From `docs-context/README.md`:

```
1. official/          (SAP/Fioneer official sources)
2. metadata-drop/normalized/  (normalized workbook artifacts)
3. training/          (training-derived concepts)
```

### Key Locations by Purpose

| Location | Purpose | Audience | Format |
|----------|---------|----------|--------|
| `docs-context/official/sap/` | Canonical SAP product guidance | All skills | Curated `.md` |
| `docs-context/training/fpsl/` | Concept tutorials & worked examples | Learning & framing | `.md` + `/worked-examples/` |
| `docs-context/shared/official-sources-router.md` | Skill→official-ref dispatcher | Skills loading refs | Router `.md` |
| `docs-context/inbox/review-drafts/` | Staged extractions awaiting review | Tech reviewers | Numbered `.md` |
| `metadata-drop/normalized/` | Normalized workbook CSVs | Skills consuming data | `.csv` |
| `docs-context/indexes/ingestion-manifest.csv` | Source version inventory | Pipeline managers | `.csv` |

---

## 3. How Skills Consume External References

### Universal Load Order Pattern

All skill `SKILL.md` files follow a consistent load-order sequence:

**Example from `skills/config/SKILL.md`:**

```markdown
## Load Order

1. Read this file.
2. Read [configuration-core-rules.md](./references/configuration-core-rules.md).
3. Read [fpsl-installation-configuration.md](./references/fpsl-installation-configuration.md) for FPSL system installation...
4. Read [validation-and-tcodes.md](./references/validation-and-tcodes.md) when verification is needed.
5. Read `../../metadata-drop/configuration/` artifacts when sample navigation, validation sequence, or setup examples are available.
6. Read [official-sources.md](../../docs-context/shared/official-sources-router.md) when you need official FPSL/FSDM scope anchors.
7. Use this skill for guided... [operational context]
```

### Navigation Pattern: Official Sources Router

**File:** `docs-context/shared/official-sources-router.md`

**Purpose:** Centralized dispatcher that maps skills to their specific official references.

**Content Pattern:**

```markdown
# Official Sources - Centralized Router

## Shared Across All Skills
- `fpsl-product-overview.md` - FPSL architecture, Universal Journal, multi-GAAP approach
- `fpsl-client-setup.md` - Client configuration prerequisites
- `fsdm-fpsl-integration.md` - Standard FSDM and FPSL integration framing

## Skill-Specific Official References

### AMDP Skill
- `amdp-supported-capabilities.md` - HANA AMDP and SQLScript supported patterns

### Config Skill
- `fpsl-guided-configuration.md` - Product-standard guided configuration framing

### Reconciliation Skill
- `fpsl-process-run-validation.md` - Process-run verification anchors for operational checks

[... more skills ...]

## Usage
When a skill's SKILL.md says "Read [official-sources.md]", it directs here.
```

### Link Pattern in Skills

Skills consistently link to docs-context using **relative paths** from their `SKILL.md`:

```markdown
See [Skill Routing Matrix](../../docs-context/architecture/skill-routing-matrix.md)
Read [official-sources.md](../../docs-context/shared/official-sources-router.md)
Read [adt-handoff-rules.md](../../docs-context/shared/adt-handoff-rules.md)
```

### Trust Order Pattern

All skill `SKILL.md` files declare a **Trust Order** section:

**Example from `skills/config/SKILL.md`:**

```markdown
## Trust Order

1. Official SAP documentation for product scope and standard integration concepts
2. Confirmed repository metadata, screenshots, extracts, or setup evidence
3. Trusted raw metadata where relevant
4. Training-derived conceptual guidance for operational context
5. Synthetic samples only for checklist shape
```

This ensures consistent evidence prioritization across skills.

### Skill-Specific Reference Examples

| Skill | Preferred Official File | Training File | Metadata |
|-------|------------------------|----|----------|
| **amdp** | `amdp-supported-capabilities.md` | (performance reasoning only) | `metadata-drop/normalized/` |
| **abap** | `fpsl-product-overview.md` | (conceptual only) | ADT handoff rules |
| **config** | `fpsl-guided-configuration.md` | (operational context) | Sample navigation, validation checklists |
| **quality** | `fpsl-product-overview.md` | (terminology) | DDIC extracts from normalized metadata |
| **cvpm** | `fpsl-product-overview.md` | `accounting-process-model.md` | Confirmed customer evidence preferred |
| **reconciliation** | `fpsl-process-run-validation.md` | Process framing | `metadata-drop/reconciliation/` |
| **partitioning** | `fpsl-product-overview.md` | (baseline framing) | Actual system evidence from `scripts/projections/` |

---

## 4. Reference Material Load Patterns

### Staged Promotion Workflow

```
Raw PDF/Source
    ↓
scripts/ingest_pdf_context.py (config-driven extraction)
    ↓
docs-context/inbox/review-drafts/<topic>/ (staged for review)
    │
    ├─ Classification: training-derived-concepts or official-source-derived
    ├─ Source basis: <file> pages X-Y
    ├─ Trust usage: [explicit constraints]
    └─ Do-not-use-for: [explicit constraints]
    ↓
[Tech review against current curated content]
    ↓
docs-context/{official|training}/ (promoted after review)
    ↓
docs-context/indexes/ingestion-manifest.csv (status → "active")
    ↓
Skill SKILL.md load-order updated (if new skill-specific reference)
```

### Version Management via `ingestion-manifest.csv`

**Example manifest:**

```csv
source_id,source_label,origin_type,classification,target_area,source_version,status,replaces_source_id,review_state,notes
official-source-01,operational-reference,official,official-source-derived,docs-context/official/sap,2306-sp04,active,,reviewed,Curated from reviewed operational reference material
training-source-01,query-concepts-week-1,training,training-derived-concepts,docs-context/training/hana-sql,week-1,active,,reviewed,Concept extraction from reviewed training source
training-source-02,query-concepts-week-3,training,training-derived-concepts,docs-context/training/hana-sql,week-3,active,,reviewed,Concept extraction from reviewed training source
training-source-03,fpsl-concepts,training,training-derived-concepts,docs-context/training/fpsl,rev-01,active,,reviewed,Concept extraction from reviewed training source
```

**Status Values:**

- `active` — current preferred source for curated context
- `superseded` — older source retained for traceability
- `candidate` — newly ingested source awaiting review

**Review States:**

- `reviewed`
- `pending-review`
- `promoted`
- `rejected`

### Update Policy Rules

From `docs-context/indexes/update-policy.md`:

**Core Rule:** Newer source PDFs do NOT automatically change active curated context.

**Promotion Checklist:**

- [ ] Source has been reviewed outside public repo if raw extraction needed
- [ ] Extracted material reviewed against current curated files
- [ ] Update applicable curated markdown if content invalidated
- [ ] Check `topic-map.md` still points to preferred files
- [ ] Mark prior source `superseded` if replaced
- [ ] Update `ingestion-manifest.csv` to `active`
- [ ] Update skill SKILL.md load-order if new skill-specific reference

**Tech Head Review Questions:**

- Does this change product scope or terminology?
- Does this change operational setup guidance?
- Does this change integration framing?
- Does this invalidate older curated notes?
- Do any skill-routing files need updating?

---

## 5. Office Format (.docx, .xlsx) Handling

### Current State: `.xlsx` Workbook Normalization Only

**Supported:** `.xlsx` (Excel workbooks) — **NOT .docx**

**Unsupported:** `.docx` (Word documents), other Office formats

### XLSX Processing Script

**File:** `scripts/normalize_excel.py`

**Purpose:** Convert trusted metadata workbooks into normalized CSV outputs.

**Capabilities:**

- Uses **Python standard library only** (no external package dependencies for core extraction)
- Parses XLSX XML structure (ECMA-376 format)
- Extracts shared strings (deduplicated text pool in modern Excel)
- Preserves column/row structure as-is
- Outputs one CSV per worksheet
- Updates `metadata-drop/manifest.csv` with artifact metadata

**Workflow:**

```bash
# Explicit invocation
python3 scripts/normalize_excel.py metadata-drop/raw-excel/<workbook>.xlsx

# With optional artifact ID
python3 scripts/normalize_excel.py metadata-drop/raw-excel/<workbook>.xlsx --artifact-id fpsl-fsdm-2023-drop-01

# Via wrapper script
./scripts/run-normalization.sh <workbook>.xlsx

# Or latest workbook (auto-detect)
./scripts/run-normalization.sh

# Or via VS Code task (Metadata: Normalize latest workbook)
```

**Input Location:**

```
metadata-drop/raw-excel/
```

**Output Location:**

```
metadata-drop/normalized/<artifact-id>/
  ├── sheet-1.csv
  ├── sheet-2.csv
  └── ...
```

**Manifest Update:**

`metadata-drop/manifest.csv` is automatically updated with:
- `artifact_id` (system-generated or user-provided)
- `source_type`: `raw-excel`
- `source_name`: workbook filename
- `normalized_type`: `normalized`
- Ingestion date and output directory path

### Why PDF (not Word/DOCX)

The pipeline prioritizes:

1. **PDFs** → Deterministic, config-driven extraction via `ingest_pdf_context.py`
2. **Text/Markdown** → Direct ingestion (pre-converted)
3. **.xlsx** → Deterministic, structure-preserving normalization via `normalize_excel.py`

**NOT .docx because:**

- `.docx` is complex (ZIP of XML + binary + embedded content)
- Requires heavy dependencies (e.g., `python-docx`, `pandoc`)
- Inconsistent formatting preservation
- Policy: "Provide preconverted `.txt` or `.md` instead" (per `ingest_pdf_context.py` docstring)

### Fallback for Word Documents

If Word source material is crucial:

1. **Manual conversion outside repo**
   - User exports Word to PDF or Markdown manually
   - Then uses `ingest_pdf_context.py` or direct text ingestion
   
2. **Via external tool**
   - User can use `pandoc`, `libreoffice`, or Word to convert `.docx` → `.md` or `.pdf`
   - Then ingest via standard pipeline

**Recommended Pattern (if .docx is needed):**

```bash
# User pre-converts outside skill pack
pandoc source.docx -t markdown -o source.md

# Then ingest into pipeline
python3 scripts/ingest_pdf_context.py source.md docs-context/inbox/config-example.json
```

---

## 6. Ingestion Command Reference

### PDF + Config-Driven Extraction

```bash
# Standard extraction
python3 scripts/ingest_pdf_context.py docs-context/inbox/fpsl-training.pdf \
  docs-context/inbox/config-fpsl-training.json

# Output: docs-context/inbox/review-drafts/fpsl-training-extracted/*.md
```

### .xlsx Workbook Normalization

```bash
# Standard normalization
python3 scripts/normalize_excel.py metadata-drop/raw-excel/fpsl-metadata-2023.xlsx

# With explicit artifact ID
python3 scripts/normalize_excel.py metadata-drop/raw-excel/fpsl-metadata-2023.xlsx \
  --artifact-id fpsl-fsdm-2023-drop-01

# Auto-detect latest + wrapper
./scripts/run-normalization.sh

# Output: metadata-drop/normalized/<artifact-id>/*.csv
# Updates: metadata-drop/manifest.csv
```

### Pre-Converted Text/Markdown

```bash
# Direct markdown ingestion
python3 scripts/ingest_pdf_context.py training-notes.md \
  docs-context/inbox/config-training.json

# Output: docs-context/inbox/review-drafts/extracted-notes/*.md
```

---

## 7. Key Patterns & Best Practices

### Pattern: Config-Driven Ingestion

**Why:** Deterministic, reviewable, repeatable extraction without manual copy-paste.

**Implementation:**

1. Source doc is placed in `docs-context/inbox/` or external location
2. JSON config specifies page ranges and section metadata
3. `ingest_pdf_context.py` reads config and extracts sections with provenance metadata
4. Output staged in `docs-context/inbox/review-drafts/<topic>/`
5. Reviewer checks output quality and promotes to `official/` or `training/` after approval
6. `ingestion-manifest.csv` updated with status `active`

**Benefits:**

- Extracting repeated pages? Re-run with updated config.
- New source version? Update config page ranges, re-run, compare with prior output.
- Provenance is automatic and machine-readable.

### Pattern: Trust Layering

**Official > Evidence > Training > Synthetic**

Skills trust order:

1. **Official SAP sources** (`docs-context/official/sap/`) — canonically correct
2. **Confirmed repo metadata** (screenshots, extracts, verified setup) — proven in context
3. **Training-derived concepts** (`docs-context/training/`) — pedagogical framing
4. **Synthetic samples** — checklist structure only, not production

### Pattern: Staged Promotion

```
Staged (inbox/)
    ↓ [Review: does this change scope, terminology, integration framing?]
    ↓
Active (official/ or training/)
    ↓ [Skill SKILL.md updated if skill-specific]
    ↓
Manifests Updated (ingestion-manifest.csv)
```

### Pattern: Explicit Non-Use Constraints

Every ingested section carries metadata saying when **NOT** to use it:

```markdown
Do not use for: customer-specific implementation details, local configuration assumptions
```

This prevents misapplication (e.g., using training examples as production config templates).

### Pattern: .xlsx as Metadata Source

`.xlsx` workbooks are normalized to CSV for:

- DDIC extracts (table structures, fields, domains)
- Configuration sample navigation
- Mapping specifications
- Test data fixtures
- Volume/sizing projections

Skills consume via `metadata-drop/normalized/<artifact-id>/<sheet-name>.csv`

---

## 8. Integration Points for New Reference Materials

### Adding New PDF/Training Source

1. **Create ingestion config** in `docs-context/inbox/config-<source>.json`
   - Specify target_root, sections, page ranges, topics, trust/do-not-use constraints
   
2. **Run extraction**
   ```bash
   python3 scripts/ingest_pdf_context.py <source.pdf> docs-context/inbox/config-<source>.json
   ```

3. **Review staged output** in `docs-context/inbox/review-drafts/<topic>/`
   - Check provenance headers are correct
   - Verify extracted content matches intent
   - Flag if do-not-use constraints are insufficient

4. **Promote after review**
   - Move `.md` files to `docs-context/official/sap/` or `docs-context/training/fpsl/`
   - Add entry to `ingestion-manifest.csv` with status `active`
   
5. **Update downstream references** if needed
   - Add to `docs-context/shared/official-sources-router.md` if official
   - Update affected skill `SKILL.md` load-order if skill-specific
   - Update `docs-context/indexes/topic-map.md` if canonical topic reference

### Adding New .xlsx Metadata

1. **Place workbook** in `metadata-drop/raw-excel/`

2. **Run normalization**
   ```bash
   python3 scripts/normalize_excel.py metadata-drop/raw-excel/<workbook>.xlsx
   ```

3. **Review normalized CSVs** in `metadata-drop/normalized/<artifact-id>/`
   - Check sheet column/row structure preserved
   - Verify no data loss or encoding issues

4. **Skills consume immediately** — no extra review steps
   - Manifests auto-updated
   - CSV is production-ready

---

## 9. Current Ingestion Sources (Active)

| Source ID | Type | Version | Target | Status | Topics |
|-----------|------|---------|--------|--------|--------|
| `official-source-01` | SAP Official | 2306-sp04 | `docs-context/official/sap/` | **active** | FPSL product, reference architecture |
| `training-source-01` | Training | week-1 | `docs-context/training/hana-sql/` | **active** | Query concepts, SQL basics |
| `training-source-02` | Training | week-3 | `docs-context/training/hana-sql/` | **active** | Query concepts, advanced SQL |
| `training-source-03` | Training | rev-01 | `docs-context/training/fpsl/` | **active** | FPSL architecture, process model |

See `docs-context/indexes/ingestion-manifest.csv` for complete version inventory.

---

## 10. Key Files for Pipeline Administration

| File | Purpose |
|------|---------|
| `scripts/ingest_pdf_context.py` | PDF/text extraction engine |
| `scripts/normalize_excel.py` | XLSX workbook normalization engine |
| `scripts/run-normalization.sh` | Wrapper for latest `.xlsx` auto-detection |
| `docs-context/inbox/config-*.json` | Ingestion config templates |
| `docs-context/indexes/ingestion-manifest.csv` | Source version inventory & lifecycle status |
| `docs-context/indexes/update-policy.md` | Promotion rules & review checklist |
| `docs-context/shared/official-sources-router.md` | Skill → official reference dispatcher |
| `skills/*/SKILL.md` | Per-skill load-order & trust framing |
| `.github/instructions/*.md` | Skill-agnostic vs. skill-specific routing |

