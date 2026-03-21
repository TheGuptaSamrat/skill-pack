# Mapping Patterns: Common Source-to-Target Scenarios

Real-world mapping patterns for FPSL/FSDM flows:

---

## Pattern 1: Direct Field Mapping (1:1)

**Scenario:** Source has matching field name and type in target

```
SOURCE TABLE: ZZ_PURCHASE_ORDERS
├── PO_NUMBER → TARGET: /BA1/HKTVR.PRODUCT_ID (varchar, key)
├── VENDOR_ID → TARGET: /BA1/HKTVR.VENDOR_ID (varchar, FK)
└── AMOUNT → TARGET: /BA1/HKTVR.NOTIONAL_VALUE (decimal)
```

**Evidence required:**
- PO_NUMBER type matches PRODUCT_ID (or safe cast exists)
- VENDOR_ID is foreign key in target (check DD09S/DD08L)
- AMOUNT currency defined (check WAERS field)

**Mapping notes:**
- Confirmed: Direct passthrough
- Validation: Ensure no null PO_NUMBER (is it key in source?)
- Handoff: Implement in mapping CDS or direct table insert

---

## Pattern 2: Derived/Calculated Mapping

**Scenario:** Target field requires transformation or calculation

```
SOURCE: ZZ_TRANSACTIONS.TRADE_DATE (date, format YYYYMMDD)
TARGET: /BA1/HFPPD.VALUE_DATE (date, format YYYYMM01)
Transform: YYYYMMDD → Month-start date
```

**Evidence required:**
- Source format confirmed (check sample data)
- Target expects month-start (check table description in DDIC)
- Fiscal/calendar month alignment documented

**Mapping notes:**
- Inferred: Month-start convention (confirm with business)
- Edge case: Month-end transactions round to next month?
- Handoff: CDS expression or SQLScript function

---

## Pattern 3: Multi-Table Join Mapping

**Scenario:** Single source field maps across multiple target tables

```
SOURCE: ZZ_CUSTOMER.CUSTOMER_ID → TARGET tables
├── /BA1/HFPPD.COUNTERPARTY_ID (transaction header)
├── /BA1/HKAPD.PARTY_ID (account position detail)
└── /BA1/HKTVR.CUSTOMER_REF (valuation reference)

Join logic: All three use customer_id as PK join on CUSTOMER_ID
```

**Evidence required:**
- CUSTOMER_ID is unique key in source (check uniqueness)
- All three target tables share same customer semantics
- No cross-validation conflicts (e.g., customer A maps to both party 1 and party 2)

**Mapping notes:**
- Confirmed: FK relationships verified
- Inferred: Cardinality 1:1 across tables (validate against data samples)
- Unresolved: Does HKTVR.CUSTOMER_REF allow null? (if join optional)

---

## Pattern 4: Conditional/Rule-Based Mapping

**Scenario:** Target field value depends on source conditions

```
SOURCE: ZZ_PRODUCTS.PRODUCT_TYPE
├── IF PRODUCT_TYPE = 'EQUITY' → TARGET: /BA1/HFPPD.ASSET_CLASS = '010' (Stock)
├── IF PRODUCT_TYPE = 'BOND' → TARGET: /BA1/HFPPD.ASSET_CLASS = '020' (Bond)
└── IF PRODUCT_TYPE = 'FX' → TARGET: /BA1/HFPPD.ASSET_CLASS = '030' (Currency Pair)
```

**Evidence required:**
- PRODUCT_TYPE domain/values fully enumerated (no "other" category)
- Asset class values locked in DDIC domain ZZ_ASSET_CLASS
- No ambiguous product types

**Mapping notes:**
- Confirmed: Values enumerated from source documentation
- Inferred: ELSE → DEFAULT case? (specify behavior)
- Validation: Sample 100 rows; verify 100% coverage

---

## Pattern 5: Code/Lookup Table Mapping

**Scenario:** Source code must translate to target via lookup table

```
SOURCE: ZZ_GL_CODES.GL_CODE (e.g., "4100-Sales")
LOOKUP: ZZ_GL_MAPPING
├── GL_CODE → SAP_GL_ACCOUNT (e.g., 411000)

TARGET: /BA1/HFPPD.GL_ACCOUNT = SAP_GL_ACCOUNT
```

**Evidence required:**
- ZZ_GL_MAPPING is complete (no missing GL_CODE values in source)
- SAP_GL_ACCOUNT is valid (check chart of accounts in DDIC)
- Lookup table maintained over time (is it static or does it change?)

**Mapping notes:**
- Confirmed: Lookup table exists and is complete
- Inferred: GL maps 1:1 (no GL_CODE → multiple SAP accounts)
- Unresolved: What if source GL_CODE not in lookup? (error, default, skip?)

---

## Pattern 6: Field Aggregation/Rollup

**Scenario:** Multiple source rows roll up to single target

```
SOURCE: ZZ_DAILY_TRADES (multiple rows per day)
├── DAY_1: Qty=100, Price=50 → Amount=5000
├── DAY_2: Qty=50, Price=51 → Amount=2550
└── DAY_3: Qty=75, Price=49 → Amount=3675

TARGET: /BA1/HFPPD (single row per position)
├── TOTAL_AMOUNT = SUM(Amount) = 11,225
├── AVG_PRICE = WEIGHTED_AVG = 50.05
└── END_OF_MONTH_POSITION = 225 units
```

**Evidence required:**
- Source grain: "daily trades" (multiple per day, multiple days per position)
- Target grain: "end-of-month position" (single row)
- Aggregation logic: SUM for amounts, WEIGHTED_AVG for prices
- Tie-breaker for conflicting dates (use latest date or average?)

**Mapping notes:**
- Confirmed: Aggregation keys clearly defined
- Inferred: Aggregation method (SUM vs AVG) based on field semantics
- Validation: Reconcile source totals to target after aggregation

---

## When to Use Each Pattern

| Pattern | Use Case | Complexity | Risk |
|---------|----------|-----------|------|
| Direct (1:1) | Matching fields, types | Low | Low |
| Derived | Transforms, calculations | Medium | Medium (if formula wrong) |
| Multi-join | Multiple targets from one source | Medium | Medium (join logic errors) |
| Conditional | Business rules, enumerations | Medium-High | High (missing conditions) |
| Lookup | Code translation | Medium | High (incomplete lookup) |
| Aggregation | Grain changes | High | High (aggregation errors) |

---

## Validation Checklist for Each Mapping

- [ ] Source field exists in source system (DDIC check or data sample)
- [ ] Target field exists in target system (DDIC check)
- [ ] Data types compatible (or safe cast documented)
- [ ] For JOINs: cardinality verified (1:1, 1:N, N:M documented)
- [ ] For LOOKUPs: lookup table complete (no unmatched source values)
- [ ] For CONDITIONALs: all source values enumerated (no "other")
- [ ] For AGGREGATIONS: grain change explicitly documented
- [ ] Null handling specified (are NULLs allowed in target?)
- [ ] Historical behavior documented (does mapping change over time?)
