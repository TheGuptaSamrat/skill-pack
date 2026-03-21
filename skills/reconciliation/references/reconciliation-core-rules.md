# Reconciliation Core Rules

Foundational guardrails for business data verification through DDIC-aware SQL:

## Reconciliation Rule Types

1. **Totals Balancing** - SUM by group matches control totals
2. **Row Count Verification** - Record counts match between source/target
3. **Key Integrity** - Primary/foreign keys valid across joined tables
4. **Data Flow Validation** - Records flowthrough from source → staging → target
5. **Cross-System Reconciliation** - Balances across multiple systems/modules

## Core Principles

- Prefer row-level reconciliation over aggregate-only checks (catches ~30% more issues)
- Document baseline beforehand (what's "normal" vs "abnormal"?)
- Include both positive (valid) and negative (invalid) reconciliation paths
- Separate reconciliation from quality (reconciliation is process-level, quality is field-level)
- Keep joins explicit with clear cardinality documentation
