# Reconciliation Patterns: Common Cross-Process Validation

Real-world reconciliation patterns for FPSL/FSDM process runs:

## Pattern 1: Daily Run Totals

```sql
SELECT run_date, COUNT(*) as record_count, SUM(amount) as total_amount
FROM landing_table
GROUP BY run_date
ORDER BY run_date DESC;

-- Compare vs previous day: is volume within expected band?
```

## Pattern 2: Source-to-Target Completeness

```sql
WITH source_counts AS (
  SELECT source_id, COUNT(*) as source_cnt FROM source_system GROUP BY source_id
),
target_counts AS (
  SELECT source_id, COUNT(*) as target_cnt FROM target_table GROUP BY source_id
)
SELECT s.source_id, s.source_cnt, t.target_cnt, s.source_cnt - t.target_cnt as delta
FROM source_counts s
LEFT JOIN target_counts t ON s.source_id = t.source_id
WHERE s.source_cnt != COALESCE(t.target_cnt, 0);
```

## Pattern 3: Foreign Key Orphans

```sql
SELECT COUNT(*) as orphaned_records
FROM target_table t
LEFT JOIN reference_table r ON t.ref_id = r.ref_id
WHERE t.ref_id IS NOT NULL AND r.ref_id IS NULL;
```

## Pattern 4: Amount Reconciliation with Tolerance

```sql
SELECT SUM(amount) as target_total,
       (SELECT SUM(amount) FROM source) as source_total,
       ABS(SUM(amount) - (SELECT SUM(amount) FROM source)) as variance,
       CASE WHEN ABS(SUM(amount) - (SELECT SUM(amount) FROM source)) < 0.01 THEN 'PASS' ELSE 'FAIL' END as status
FROM target_table;
```
