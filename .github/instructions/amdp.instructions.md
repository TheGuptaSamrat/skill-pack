# AMDP Instructions

Use this instruction set when the task is primarily about:

- AMDP implementation
- SQLScript
- CDS table functions
- reconciliation queries
- DDIC-aware data checks
- performance-sensitive set-based logic

Load in this order:

1. `skills/amdp/SKILL.md`
2. `skills/amdp/references/amdp-core-rules.md`
3. `skills/amdp/references/amdp-query-patterns.md`
4. `skills/amdp/references/sql-and-performance-rules.md`
5. `skills/amdp/references/adt-handoff-rules.md`

Routing rule:

- Use `amdp` for pushdown-heavy implementation.
- Route specialist reconciliation work to `reconciliation`.
- Route checklist-led operational walkthroughs to `config`.
