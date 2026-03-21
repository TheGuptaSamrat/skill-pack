# Mapping Edge Cases & Validation Guidance

Complex scenarios and validation patterns for mapping specifications:

---

## Edge Case 1: Nullable Fields in Mappings

**Scenario:** Source allows NULL but target doesn't (or vice versa)

```
SOURCE: ZZ_PRODUCTS.EFFECTIVE_DATE (nullable)
TARGET: /BA1/HFPPD.VALUE_START_DATE (non-null, key component)
```

**Resolution options:**
1. Default value: Use system date or hardcoded date
2. Filter source: Only map non-null rows
3. Two-path mapping: Separate logic for NULL vs non-NULL cases
4. Business rule: Ask if NULL source is valid at all

**Validation:**
- Count NULL occurrences in source (sample 1,000 rows)
- Determine business impact of chosen resolution
- Document in mapping spec which option applies

---

## Edge Case 2: Duplicate Keys in Source

**Scenario:** Source has multiple rows for what appears to be same entity

```
SOURCE: ZZ_CUSTOMER (multiple rows per customer)
├── CUSTOMER_ID=123, UPDATED_DATE=2025-01-01
├── CUSTOMER_ID=123, UPDATED_DATE=2025-01-15 ← Duplicate key!
├── CUSTOMER_ID=123, UPDATED_DATE=2025-03-10

TARGET: /BA1/HFPPD (expects 1 row per customer)
```

**Resolution options:**
1. Latest record: Use MAX(UPDATED_DATE) deduplication
2. Aggregate: SUM/AVG/DISTINCT values
3. Error: Flag as data quality issue, don't map
4. Grain change: Accept multiple rows, map to detail table instead

**Validation:**
- Count duplicates per CUSTOMER_ID
- Verify all duplicates have same non-key fields (yes/no?)
- Choose deduplication strategy based on business semantics

---

## Edge Case 3: Type Incompatibility

**Scenario:** Source and target data types don't match

```
SOURCE: ZZ_GL_CODE (string "411000")
TARGET: /BA1/HFPPD.GL_ACCOUNT (numeric, 10 digits)
```

**Resolution:**
- Direct cast: String → Numeric (works if all strings are numeric)
- Safe cast: Use function to validate (CAST with error handling)
- Transform: Clean/validate before casting (trim spaces, remove leading zeros)

**Validation required:**
- Sample 100 source values; test cast on all
- Identify cast failures (non-numeric strings, overflow, underflow)
- Document expected cast behavior (trim zeros? pad? round?)

---

## Edge Case 4: Cardinality Mismatch (1:N when expecting 1:1)

**Scenario:** What you thought was 1:1 join actually produces multiple rows

```
SOURCE: ZZ_PURCHASE_ORDERS (key: PO_NUMBER)
TARGET: /BA1/HFPPD (also keyed on PO_NUMBER)

PROBLEM: One PO has multiple line items
SOURCE: PO_NUMBER=123, LINE=1, AMOUNT=1000
SOURCE: PO_NUMBER=123, LINE=2, AMOUNT=500

Result: Target gets 2 rows instead of 1!
```

**Resolution options:**
1. Aggregate: SUM amounts by PO_NUMBER
2. Filter: Map only first line item
3. Explode: Allow multiple detail rows in target (grain change)
4. Wrong target: Use detail table, not header

**Validation:**
- Count distinct values: COUNT(DISTINCT PO_NUMBER) vs COUNT(*)
- If ratio > 1, cardinality is N:1, not 1:1
- Reconsider which target table to use

---

## Edge Case 5: Temporal/Historical Changes

**Scenario:** Source value changes over time; target expects single value

```
SOURCE: ZZ_CUSTOMER_MASTER (slowly changing dimension)
├── CUSTOMER_ID=123, EFFECTIVE_DATE=2024-01-01, REGION="APAC"
├── CUSTOMER_ID=123, EFFECTIVE_DATE=2025-01-01, REGION="EMEA" ← Changed!

TARGET: /BA1/HFPPD (effective on valuation date, e.g., 2025-02-15)
```

**Resolution:**
1. Latest as-of date: Use MAX(EFFECTIVE_DATE) ≤ valuation date
2. Historical snapshot: Keep mapping valid as-of specific date
3. Current: Always use latest value (ignoring history)

**Validation:**
- Track which values change over time
- Document effective date semantics (SCD Type 1 vs Type 2?)
- Ensure mapping applies to target's valuation date, not today

---

## Edge Case 6: Missing Source Evidence

**Scenario:** Source field doesn't exist yet or is undocumented

```
TARGET: /BA1/HFPPD.RATING_CODE (required field)
SOURCE: ??? Not documented, not visible in current data
```

**Resolution:**
1. Placeholder: Mark as "UNRESOLVED" in mapping spec
2. Derived: Can this be computed from other fields?
3. Default: Use business default (if acceptable)
4. Block: Refuse to map until source evidence found

**Validation:**
- Documentation: Is source field planned but not yet deployed?
- Workaround: Can existing fields substitute?
- Timeline: When will source field be available?

---

## Validation Checklist: Before Marking Mapping "Confirmed"

- [ ] Source field exists and is accessible (confirmed via DDIC or SELECT)
- [ ] Target field exists and is in correct table (crossed with DDIC)
- [ ] Data types tested with 5+ sample rows (casts work, no errors)
- [ ] Cardinality verified (1:1 join produces expected row count)
- [ ] NULL handling explicit (what do we do if source is NULL?)
- [ ] Duplicates handled (if source has dups, how do we resolve?)
- [ ] Temporal semantics clear (current vs historical as-of date)
- [ ] Edge cases documented (special values, exceptions, error cases)
- [ ] Performance tested (if joining large tables, does it run in <5s for 100K rows?)
- [ ] Variance documented (which values change over time? flagged for retesting)

---

## Common Validation Queries

### Test 1: Count source vs target cardinality
```sql
-- Source grain
SELECT COUNT(DISTINCT PO_NUMBER) as unique_pos,
       COUNT(*) as total_rows
FROM ZZ_PURCHASE_ORDERS;

-- If total > unique, then 1:N cardinality (need aggregation in mapping)
```

### Test 2: Find unmatched keys in JOIN
```sql
-- Source records without corresponding target
SELECT s.PO_NUMBER
FROM ZZ_PURCHASE_ORDERS s
LEFT JOIN /BA1/HFPPD t ON s.PO_NUMBER = t.PO_NUMBER
WHERE t.PO_NUMBER IS NULL
LIMIT 10;

-- If any rows found, mapping gap exists (document in "Unresolved")
```

### Test 3: Verify lookups are complete
```sql
-- Source values not in lookup table
SELECT DISTINCT source_code
FROM ZZ_GL_CODES s
LEFT JOIN ZZ_GL_MAPPING m ON s.GL_CODE = m.GL_CODE
WHERE m.GL_CODE IS NULL
LIMIT 20;

-- If any rows found, lookup incomplete (error case in production)
```

### Test 4: Identify NULL patterns
```sql
-- Count NULLs by field
SELECT 'EFFECTIVE_DATE' as field,
       COUNT(*) as total,
       SUM(CASE WHEN EFFECTIVE_DATE IS NULL THEN 1 ELSE 0 END) as null_count,
       ROUND(100.0 * SUM(CASE WHEN EFFECTIVE_DATE IS NULL THEN 1 ELSE 0 END) / COUNT(*), 2) as null_pct
FROM ZZ_PRODUCTS;

-- If null_pct > 5%, likely needs default or filter logic in mapping
```
