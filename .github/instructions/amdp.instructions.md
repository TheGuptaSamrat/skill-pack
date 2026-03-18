# AMDP Instructions

Use this instruction set when the task is primarily about:

- AMDP implementation
- SQLScript
- CDS table functions
- reconciliation queries
- DDIC-aware data checks
- performance-sensitive set-based logic

Load in this order:

1. `skills/sap-fpsl-amdp/SKILL.md`
2. `skills/sap-fpsl-amdp/references/amdp-delivery-rules.md`
3. `skills/sap-fpsl-amdp/references/sql-and-performance-rules.md`
4. `skills/sap-fpsl-amdp/references/reconciliation-query-patterns.md` when the task is investigative
5. `skills/sap-fpsl-amdp/references/ddic-aware-query-construction.md` when metadata exists

Routing rule:

- Use `sap-fpsl-amdp` for set-based SQL, reconciliation, and data-presence verification.
- Route checklist-led operational walkthroughs to `sap-fpsl-configuration`.
