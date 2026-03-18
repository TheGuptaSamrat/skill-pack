# AMDP Query Patterns

Treat all object names, types, and tables below as placeholders unless they are confirmed by repository or DDIC metadata.

- use DDIC-aware query shapes when metadata is available
- generate reconciliation or data-flow-check queries when the task is investigative
- use `MERGE` when reruns must be idempotent
- match on the true business key, not row order
- include result category or accounting dimension when it defines uniqueness
- push selective filters early
- filter on legal entity, posting date, result category, source system, and scenario where relevant
- prefer explicit filter parameters over generic free-text filtering
- preserve the root cause with `previous =`
- use deterministic fixture helpers for ABAP Unit around wrapper code
- convert early into the correct numeric type
- round once at the correct business boundary
- validate currency consistency before aggregation
- commit by package or document group, not by row
- keep commit frequency configurable
- use `JOIN` when the relationship naturally belongs in the database
- use `FOR ALL ENTRIES` only with deduplicated, non-initial driving keys
- compare row explosion risk before choosing the pattern
