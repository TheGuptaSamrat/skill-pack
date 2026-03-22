# Official Sources - Centralized Router

Load curated FPSL context from `docs-context/official/sap/` as needed for your skill.

---

## Shared Across All Skills

Standard FPSL terminology, process framing, and non-customer-specific documentation:

- `fpsl-product-overview.md` - FPSL architecture, Universal Journal, multi-GAAP approach
- `fpsl-client-setup.md` - Client configuration prerequisites
- `fsdm-fpsl-integration.md` - Standard FSDM and FPSL integration framing
- **`fpsl-fsdm-2023-golden-source.md`** - ⭐ **Comprehensive FPSL 2306 & FSDM 2023 technical specification** (2023 release details, core engines, data models, integration mechanics, multi-GAAP strategy, banking domain entities)

---

## Skill-Specific Official References

### AMDP Skill
- `amdp-supported-capabilities.md` - HANA AMDP and SQLScript supported patterns
- `fpsl-fsdm-2023-golden-source.md` - Section 1.4 (RAP Model), Section 4.2 (Data Loading & RFMs)

### Config Skill
- `fpsl-guided-configuration.md` - Product-standard guided configuration framing
- `fpsl-fsdm-2023-golden-source.md` - Section 3.2 (Multi-GAAP Strategy), Section 4.4 (Value Mapping Tables)

### CVPM Skill
- `fpsl-fsdm-2023-golden-source.md` - ⭐ **Comprehensive source** for Part 3 (Core Engines), accounting logic, EBA rules, multi-GAAP posting

### Mapping Skill
- `fpsl-fsdm-2023-golden-source.md` - Section 4 (FSDM-to-FPSL Integration), Section 4.3-4.4 (Mapping Views & Value Mapping), Section 5 (Banking Domain Entities)

### Quality Skill
- `fpsl-fsdm-2023-golden-source.md` - Section 2.2 (Physical Data Model, Managed Tables), Section 2.3 (Data Access Views), bitemporal versioning

### Reconciliation Skill
- `fpsl-process-run-validation.md` - Process-run verification anchors for operational checks
- `fpsl-fsdm-2023-golden-source.md` - Section 3.2 (Multi-GAAP), Section 4.5 (Universal Journal Integration), multi-period audit trail

### Partitioning Skill
- `fpsl-product-overview.md` - Baseline product framing; pair with measured growth evidence from `scripts/projections/`

### Other Skills
Other skills (abap, projections, test-data) primarily reference `fpsl-product-overview.md` for standard FPSL framing; may consult `fpsl-fsdm-2023-golden-source.md` for additional architecture context.

---

## Usage

When a skill's SKILL.md says "Read [official-sources.md]", it directs here.

- For standard FPSL concepts: Read `fpsl-product-overview.md`
- For skill-specific guidance: See section above and load the listed file for that skill first
- For official terminology precedence: Trust these sources above training-derived or marketing content
