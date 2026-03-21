# Quality Patterns: Common Data Quality Rules

Real-world DDIC-driven quality rule examples for FPSL/FSDM flows:

---

## Pattern 1: Simple Null Check

**Scenario:** Mandatory field must have a value

```
Field: /BA1/HFPPD.PRODUCT_ID (type varchar, length 10)
DDIC Evidence: NOTNULL = X (checked via DD04N table)

Quality Rule:
  Name: HFPPD_PRODUCT_ID_NOT_NULL
  Check: SELECT COUNT(*) FROM /BA1/HFPPD WHERE PRODUCT_ID IS NULL
  Expected: 0 rows
  Error Action: Reject or flag as quality issue
```

**Implementation (SQL):**
```sql
SELECT COUNT(*) as violation_count,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM /BA1/HFPPD), 2) as violation_pct
FROM /BA1/HFPPD
WHERE PRODUCT_ID IS NULL;
```

**When to apply:** All primary key fields, all mandatory foreign keys

---

## Pattern 2: Domain Value Check

**Scenario:** Field values must be from defined domain

```
Field: /BA1/HFPPD.ASSET_CLASS (type char, length 3)
DDIC Evidence:
  Domain: ZZ_ASSET_CLASS
  Fixed values: 010 (Stock), 020 (Bond), 030 (FX), 040 (Commodity)
  (Retrieved from DD07V table)

Quality Rule:
  Name: HFPPD_ASSET_CLASS_IN_DOMAIN
  Check: ASSET_CLASS must be IN ('010','020','030','040')
  Expected: 100% valid
  Invalid values: None (or flag where found)
```

**Implementation (SQL):**
```sql
SELECT COUNT(*) as violation_count,
       COUNT(DISTINCT ASSET_CLASS) as unique_invalid_values,
       LISTAGG(DISTINCT ASSET_CLASS, ',') WITHIN GROUP (ORDER BY ASSET_CLASS) as invalid_values
FROM /BA1/HFPPD
WHERE ASSET_CLASS NOT IN ('010','020','030','040')
  AND ASSET_CLASS IS NOT NULL;
```

**When to apply:** All fields with DDIC fixed values or domain assignments

---

## Pattern 3: Primary Key Uniqueness Check

**Scenario:** Primary key must have no duplicates

```
Table: /BA1/HFPPD
DDIC Evidence: Primary key fields (DD09L table)
  Keys: PORTFOLIO_ID + SECURITY_ID + VALUATION_DATE

Quality Rule:
  Name: HFPPD_PRIMARY_KEY_UNIQUE
  Check: GROUP BY PORTFOLIO_ID, SECURITY_ID, VALUATION_DATE; COUNT(*) must = 1
  Expected: No duplicate keys
```

**Implementation (SQL):**
```sql
SELECT COUNT(*) as duplicate_key_count
FROM (
  SELECT PORTFOLIO_ID, SECURITY_ID, VALUATION_DATE, COUNT(*) as cnt
  FROM /BA1/HFPPD
  GROUP BY PORTFOLIO_ID, SECURITY_ID, VALUATION_DATE
  HAVING COUNT(*) > 1
)
;
```

**When to apply:** All primary key combinations

---

## Pattern 4: Foreign Key Referential Integrity

**Scenario:** Foreign key must reference existing parent record

```
Table: /BA1/HFPPD
FK Field: VENDOR_ID
References: /BA1/HKTVR.VENDOR_ID

DDIC Evidence: DD08L (foreign key definition)

Quality Rule:
  Name: HFPPD_VENDOR_ID_FK_VALID
  Check: Join to HKTVR; no unmatched VENDOR_IDs
```

**Implementation (SQL):**
```sql
SELECT COUNT(*) as orphaned_fk_count
FROM /BA1/HFPPD hfppd
LEFT JOIN /BA1/HKTVR hktvr ON hfppd.VENDOR_ID = hktvr.VENDOR_ID
WHERE hfppd.VENDOR_ID IS NOT NULL
  AND hktvr.VENDOR_ID IS NULL;
```

**When to apply:** All foreign key fields; run before data integration

---

## Pattern 5: Type/Format Validation

**Scenario:** Field type must match DDIC definition

```
Field: /BA1/HFPPD.NOTIONAL_AMOUNT (DDIC type: decimal, length 19.4)
DDIC Evidence: Field definition from DD03L table

Quality Rule:
  Name: HFPPD_NOTIONAL_AMOUNT_TYPE_VALID
  Check: All values parse as numeric(19,4); no overflow/underflow
```

**Implementation (SQL):**
```sql
SELECT COUNT(*) as type_violation_count,
       LISTAGG(DISTINCT NOTIONAL_AMOUNT, ';') WITHIN GROUP (ORDER BY 1) as sample_invalid_values
FROM /BA1/HFPPD
WHERE NOTIONAL_AMOUNT IS NOT NULL
  -- Catch non-numeric, overflow, or formatting issues
  AND (TRY_CAST(NOTIONAL_AMOUNT AS DECIMAL(19,4)) IS NULL
       OR ABS(NOTIONAL_AMOUNT) > 9999999999999.9999);
```

**When to apply:** Numeric, date, and currency fields

---

## Pattern 6: Cross-Field Business Logic Check

**Scenario:** Relationship between two fields must hold

```
Table: /BA1/HFPPD
Fields: SETTLEMENT_TYPE, SETTLEMENT_DATE

Business Rule:
  IF SETTLEMENT_TYPE = 'T+0' THEN SETTLEMENT_DATE ≤ TODAY()
  IF SETTLEMENT_TYPE = 'T+2' THEN SETTLEMENT_DATE BETWEEN TODAY() AND TODAY()+2 days

Quality Rule:
  Name: HFPPD_SETTLEMENT_DATE_LOGIC_VALID
```

**Implementation (SQL):**
```sql
WITH violations AS (
  SELECT SETTLEMENT_TYPE, COUNT(*) as cnt
  FROM /BA1/HFPPD
  WHERE (
    (SETTLEMENT_TYPE = 'T+0' AND SETTLEMENT_DATE > TODAY())
    OR (SETTLEMENT_TYPE = 'T+2' AND SETTLEMENT_DATE > TODAY() + 2 DAYS)
  )
  GROUP BY SETTLEMENT_TYPE
)
SELECT SUM(cnt) as total_violations FROM violations;
```

**When to apply:**Rules tied to business process logic; coordinate with business team

---

## Pattern 7: Completeness/Coverage Check

**Scenario:** Table must have minimum record count or row coverage

```
Table: /BA1/HFPPD
Expected: Minimum 1 record per portfolio per day

Quality Rule:
  Name: HFPPD_PORTFOLIO_COVERAGE
  Check: COUNT(DISTINCT PORTFOLIO_ID) where VALUATION_DATE = TODAY()
  Expected: ≥ baseline (e.g., 500 portfolios)
```

**Implementation (SQL):**
```sql
SELECT VALUATION_DATE,
       COUNT(DISTINCT PORTFOLIO_ID) as portfolio_count,
       COUNT(*) as total_records,
       ROUND(100.0 * COUNT(*) / LAG(COUNT(*)) OVER (ORDER BY VALUATION_DATE), 1) as vs_prev_day_pct
FROM /BA1/HFPPD
WHERE VALUATION_DATE >= CURRENT_DATE - 10 DAYS
GROUP BY VALUATION_DATE
ORDER BY VALUATION_DATE DESC;
```

**When to apply:** End-of-day/end-of-period reconciliation checks

---

## Quality Rule Hierarchy

```
LEVEL 1: Structural Conformance (SQL checks)
├─ Type 1: Null/Completeness (Row-level)
├─ Type 2: Domain/Enum (Field-level)
└─ Type 3: Key/Uniqueness (Table-level)

LEVEL 2: Logical Consistency (Cross-field)
├─ Type 4: Type/Format (Data type validation)
├─ Type 5: Business Logic (Relationships)
└─ Type 6: Referential Integrity (FK checks)

LEVEL 3: Operational Validation (Process-level)
└─ Type 7: Coverage/Completeness (Volume checks)
```

---

## Validation Query Template

Every quality rule should include:

```sql
-- Measure quality rule violations
SELECT 'RULE_NAME' as quality_rule,
       CURRENT_DATE as check_date,
       COUNT(*) as violation_count,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM [table]), 2) as violation_pct,
       CASE WHEN COUNT(*) > [threshold] THEN 'FAILED' ELSE 'PASSED' END as status
FROM [table]
WHERE [condition] -- rule condition
GROUP BY 1, 2;
```

---

## Common Quality Metrics

| Metric | Formula | Interpretation |
|--------|---------|---|
| Completeness | NOT_NULL_COUNT / TOTAL_COUNT | % of records with required field populated |
| Validity | VALID_COUNT / TOTAL_COUNT | % of records with valid domain/type values |
| Uniqueness | UNIQUE_COUNT / TOTAL_COUNT | % of records with unique key values |
| Consistency | MATCHING_COUNT / TOTAL_COUNT | % of records where cross-field logic holds |
| Referential Integrity | MATCHED_FK / TOTAL_FK | % of FK references that exist in parent |
|Timeliness | RECORDS_LT_SLA / TOTAL | % of data arriving within SLA window |

