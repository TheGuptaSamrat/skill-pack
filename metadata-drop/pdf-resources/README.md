# PDF Resources

**Purpose:** Store source PDFs (training materials, vendor documentation, etc.) for knowledge extraction

**Classification:** reference-derived
**Usage:** Extract key concepts, examples, data models, and process flows to create structured reference materials
**Do not use for:** Customer-specific confidential information; sanitize before committing

---

## Available PDFs

### FPSL_TRAINING DOCUMENT.pdf (23MB)
- **Status:** ✅ Uploaded and extracted
- **Source:** SAP S/4HANA for Financial Products Subledger Training (Collection 01, Revision 01, May 2020, Material #50152712)
- **Coverage:** Comprehensive FPSL training with worked examples
- **Key Topics:**
  - ✅ FPSL architecture and data model
  - ✅ Standard process steps (Register, Accrue, Value FX, Classify, etc.)
  - ✅ CVPM (Calculation and Valuation Process Management) concepts
  - ✅ Loan and bond accounting examples
  - ✅ IFRS 9 classification logic
  - ✅ Fair value vs. amortized cost methods
  - ✅ OCI and recycling mechanics
  - ✅ FX revaluation (MAR - Monetary Asset Revaluation)

**Extracted Reference Files:**
- ✅ cvpm-process-design-guide.md (FPSL standard process steps, CVPM methods, run strategy)

### FPSL_ADMINGUIDE_EN.pdf (789KB)
- **Status:** ✅ Uploaded
- **Source:** SAP S/4HANA for Financial Products Subledger 2306 Administration Guide (Version 1.0, June 2023)
- **Coverage:** System administration, installation, security, operations
- **Key Topics:**
  - ✅ System architecture and deployment options
  - ✅ Security and authorization
  - ✅ Required SAP Notes and dependencies
  - ✅ Installation and upgrade procedures
  - ✅ Monitoring and troubleshooting
  - ✅ Periodic tasks and year-end processing

**Extracted Reference Files:**
- ⏳ (Will create operational guidance file)

---

## Operating Standards

- PDFs are source materials; do NOT commit confidential customer data
- Extract knowledge into markdown reference files in `skills/*/references/`
- Link PDF sections in reference files for traceability
- Mark all extracted content with source and classification
- Update this README with extracted content status

---

## Extraction Workflow

1. **Upload PDF** to this directory
2. **Extract key sections** → Create markdown reference files
3. **Update README** with extracted topics
4. **Cross-reference** in related skill reference files
5. **Commit** both PDF and extracted references together

---

## Current Extraction Status

| PDF | Status | Extracted Into | Date |
|-----|--------|-----------------|------|
| fpsl-training.pdf | Pending upload | — | — |

