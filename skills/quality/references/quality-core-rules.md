# Quality Core Rules

Foundational guardrails for structural data quality rule generation:

## Rule Generation Hierarchy

1. **Confirmed rules** - Generated directly from DDIC evidence (keys, domains, types, nullability)
2. **Inferred rules** - Based on naming patterns, business context, or sample data analysis
3. **Unresolved gaps** - Incomplete metadata; placeholder rules pending evidence

## Rule Categories

### Type 1: Null/Completeness Checks
- Non-nullable fields must have values
- Evidence: DDIC NOTNULL indicator (table DD04N)
- Example: "GL_ACCOUNT must not be null"

### Type 2: Domain Checks
- Field values must match defined domain or fixed value set
- Evidence: DDIC domain assignment (table DD04L)
- Example: "ASSET_CLASS must be in domain ZZ_ASSET_CLASS (010, 020, 030, etc.)"

### Type 3: Key/Uniqueness Checks
- Primary key fields must be unique
- Foreign key fields must reference existing parent keys
- Evidence: DDIC key definitions (DD09L, DD08L)
- Example: "PO_NUMBER must be unique (primary key)"

### Type 4: Type/Format Checks
- Field data types must match DDIC definition
- Example: "AMOUNT must be numeric(13,2); no strings"

### Type 5: Cross-Field Consistency Checks
- Relationships between fields must hold
- Example: "If SETTLEMENT_TYPE='CASH', then SETTLEMENT_DATE ≤ TODAY()"
- Evidence: Business rules documentation, sample data

### Type 6: Referential Integrity Checks
- Foreign keys must reference valid parent record
- Example: "VENDOR_ID must exist in table ZZ_VENDOR"
- Evidence: Transaction logs, sample joins

## Rule Documentation Template

```
Rule ID: QC_001
Name: [table]_[field]_NOT_NULL
Category: Type 1 (Completeness)
Field: [table_name].[field_name]
Condition: field_value IS NOT NULL
DDIC Evidence: NOTNULL indicator from DD04N
Confirmed/Inferred: Confirmed
Layer/Checkpoint: Landing Zone (raw inbound)
Error Action: Reject row (terminate processing)
Sample Query:
  SELECT COUNT(*) FROM [table] WHERE [field] IS NULL
Expected: 0 rows
```

## Non-Negotiables

- Tie each rule to DDIC evidence or documented business logic
- Do not invent domains or domains values
- Keep unresolved gaps visible (don't guess when evidence is incomplete)
- Make sure rule is generated from metadata, not manual inspection
