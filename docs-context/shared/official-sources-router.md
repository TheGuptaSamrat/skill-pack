# Official Sources - Centralized Router

Load curated FPSL context from `docs-context/official/sap/` as needed for your skill.

---

## Shared Across All Skills

Standard FPSL terminology, process framing, and non-customer-specific documentation:

- `fpsl-product-overview.md` - FPSL architecture, Universal Journal, multi-GAAP approach
- `fpsl-client-setup.md` - Client configuration prerequisites
- `fsdm-fpsl-integration.md` - Standard FSDM and FPSL integration framing

---

## Skill-Specific Official References

### AMDP Skill
- `amdp-supported-capabilities.md` - HANA AMDP and SQLScript supported patterns

### Config Skill
- `fpsl-guided-configuration.md` - Product-standard guided configuration framing

### Reconciliation Skill
- `fpsl-process-run-validation.md` - Process-run verification anchors for operational checks

### Partitioning Skill
- `fpsl-product-overview.md` - Baseline product framing; pair with measured growth evidence from `scripts/projections/`

### Other Skills
Other skills (abap, cvpm, docs, mapping, projections, quality, test-data) primarily reference `fpsl-product-overview.md` for standard FPSL framing.

---

## Usage

When a skill's SKILL.md says "Read [official-sources.md]", it directs here.

- For standard FPSL concepts: Read `fpsl-product-overview.md`
- For skill-specific guidance: See section above and load the listed file for that skill first
- For official terminology precedence: Trust these sources above training-derived or marketing content
