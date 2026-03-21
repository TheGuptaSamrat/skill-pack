# Quality Validation Checklist

Pre-deployment validation checklist for data quality rules:

## Before Marking Rule "Confirmed"

- [ ] DDIC evidence retrieved (FDD02L, DD03L, DD04N, DD07V, DD08L, DD09L)
- [ ] Rule tested on 1,000+ representative rows (not just happy path)
- [ ] Violation count quantified (how many violations in current data?)
- [ ] False positive rate assessed (rule doesn't flag valid data)
- [ ] Performance tested (SQL runs in <5s for 100K rows)
- [ ] Threshold documented (what violation % triggers alert?)
- [ ] Error handling specified (reject row? flag? log? escalate?)

## Deployment Readiness

- [ ] Rule is reproducible (same SQL, same result every time)
- [ ] Rule is maintainable (clear naming, commented logic)
- [ ] Rule is monitorable (can track metric over time)
- [ ] Baseline established (what's "normal" vs "abnormal"?)
- [ ] Alert frequency tuned (daily? weekly? on threshold breach only?)
- [ ] Remediation process defined (who fixes violations? how long?)

## Testing Queries

### Test 1: Does rule detect violations?
```sql
-- Manually insert/update test data with known violation
-- Re-run quality rule
-- Confirm violation is detected
```

### Test 2: False positive rate?
```sql
-- Run rule on clean dataset (all valid values)
-- Expected: 0 violations
-- If > 0, rule needs refinement
```

### Test 3: Performance acceptable?
```sql
-- EXPLAIN PLAN on quality rule query
-- Confirm: uses indexes, runs <5s
-- If >30s, may time out in production
```

## Deployment Steps

1. Deploy rule DDL (create view or stored procedure)
2. Run rule on 30 days of historical data
3. Capture baseline violations (expected rate)
4. Compare to current data (is violation rate similar?)
5. If rule is new: start in "warning" mode (log only, don't reject)
6. Monitor for 1 week; adjust threshold if needed
7. Promote to production (enforce rejections)

## Documentation Template

```markdown
# Quality Rule: GC_HFPPD_PRODUCT_ID_NOT_NULL

**Category:** Type 1 - Completeness
**Table:** /BA1/HFPPD
**Field:** PRODUCT_ID
**Source:** DDIC NOTNULL indicator (DD04N.NOTNULL='X')

**Rule:** PRODUCT_ID must not be null

**Implementation:**
```sql
SELECT COUNT(*) FROM /BA1/HFPPD WHERE PRODUCT_ID IS NULL
```

**Expected:** 0 rows

**Error Action:** Reject record; escalate to data governance

**Baseline:** 0 violations (historical)
**Alert Threshold:** >0 violations
**Monitor Frequency:** Daily
**Owner:** [Data Governance Team]
```
