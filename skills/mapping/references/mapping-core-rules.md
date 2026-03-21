# Mapping Core Rules

Foundational guardrails for source-to-target mapping specifications:

## Evidence Requirements

- Inventory source AND target structures first (don't map from memory)
- Use DDIC exports and table definitions as primary evidence
- For CDS sources, include DDL and table function definitions
- Document metadata quality issues (missing keys, orphaned fields, etc.)

## Section Discipline

Keep these sections explicit and separate:

1. **Confirmed mappings** - field-by-field joins backed by DDIC evidence
2. **Inferred mappings** - reasonable transforms based on naming/type patterns (flag as inferred)
3. **Unresolved gaps** - missing source/target fields requiring business clarification

## Artifact Clarity

- Use field-level precision (ZZ_FIELD → TARGET_TABLE.FIELD, not "sales data → ledger")
- Include join conditions for complex mappings (FK constraints, cardinality)
- Label synthetic or assumed mappings explicitly
- Include implementation notes only after mapping is locked

## Non-Negotiables

- Do not fabricate fields or joins when evidence is incomplete
- Do not guess join logic from naming alone
- Keep "confirmed vs inferred" explicit in every spec
- State what evidence is still required for open gaps
