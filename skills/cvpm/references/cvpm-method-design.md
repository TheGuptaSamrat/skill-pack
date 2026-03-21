# CVPM Method Design

**Classification:** FPSL-standard-guidance
**Usage:** Reference when designing and categorizing CVPM methods
**Do not use for:** Inventing method implementation details; use as decision framework only

---

## Method Types in CVPM

**Four core method categories:**

| Category | Purpose | Typical Output | Technology | Rerun Behavior |
|----------|---------|-----------------|-----------|---|
| **Valuation** | Calculate fair value, amortized cost, effective rate | Monetary amount + basis | AMDP (SQL) or ABAP | Rerunnable (overwrite) |
| **Classification** | Determine accounting treatment (IFRS 9 stage, hedge, etc.) | Classification code + rationale | Rule tree or SQL | Rerunnable (overwrite) |
| **Calculation** | Interest accrual, FX revaluation, provision | Accrual or adjustment amount | AMDP (SQL) | Rerunnable; may need reversal |
| **Reconciliation** | Match source deal to posting results | Match status + variance | SQL queries | Rerunnable (validation only) |

---

## Method Implementation Patterns

### Pattern 1: Valuation via AMDP (SQL-Based)

**When to use:**
- High-volume deals (1000+)
- Method logic is deterministic (same inputs → same output)
- Formula-driven (e.g., amortized cost = outstanding * effective rate)
- Result must be traceable to fields (audit trail requirements)

**Template Method Signature:**
```abap
CLASS z_cvpm_<method_id>_amdp DEFINITION PUBLIC CREATE PUBLIC.

  PUBLIC SECTION.
    INTERFACES: if_amdp_marker_hdb.

    METHODS:
      calculate_valuation
        IMPORTING iv_deal_id      TYPE ...
                  iv_as_of_date   TYPE d
                  iv_method_ver   TYPE ...
        EXPORTING et_results      TYPE TABLE OF z<cvpm_result_s>
                  ev_row_count    TYPE i
                  ev_status       TYPE string.

ENDCLASS.

CLASS z_cvpm_<method_id>_amdp IMPLEMENTATION.

  METHOD calculate_valuation
    BY DATABASE PROCEDURE FOR HDB
    LANGUAGE SQLSCRIPT.

    -- Step 1: Fetch deal master data
    -- Step 2: Fetch market/reference data (rates, curves, etc.)
    -- Step 3: Apply calculation formula
    -- Step 4: Build result table with audit trail
    -- Step 5: Return results + status

  ENDMETHOD.

ENDCLASS.
```

**Input Requirements:**
- Deal ID, instrument type, product code
- Amount outstanding, counterparty rating
- Effective date, reporting date, settlement date
- Reference rates (FX spot, interest curves, credit spreads)
- Prior period opening valuation (if carry-forward needed)

**Output Requirements:**
- Valuation amount (currency, precision)
- Basis/method used (for audit)
- Market data version used
- Calculation date and version
- Status (success, error, warning)

**Rerun Behavior:**
- Full rerun: Delete old results, recalculate all deals
- Incremental rerun: Update only changed deals
- Reversal: Auto-reverse prior GL posting before repost

---

### Pattern 2: Classification via Rule Tree / Decision Table

**When to use:**
- Classification logic is rule-based (IF...THEN...)
- Few rules; high complexity in conditions
- Examples: IFRS 9 stage determination, hedge accounting yes/no, SPPI test pass/fail
- Result is a categorical code, not a number

**Template Decision Table:**
```
IFRS 9 Stage Classification Rules:
┌────────────────────────────────────────────────────────────┐
│ Condition                      → Stage │ Risk Increase? → 1B │
├────────────────────────────────────────────────────────────┤
│ Default Status IN (0,1,2)          → 1 │ Otherwise     → 3  │
│ Days Past Due > 30                 → 3 │
│ Restructured Loan                  → 1 (or 2)
│ Covenant breach detected           → 2 (or 3)
│ No activity in 90+ days            → 2
│ Payment received on time            → Stage down by 1
└────────────────────────────────────────────────────────────┘

Implementation: BADI, rule tree (IMG transaction), or SQL CASE statement
```

**Implementation Options:**
- **Option A: BADI (Plugin)**
  Pros: Flexible, customer can extend
  Cons: Complex for business users

- **Option B: IMG Rule Tree (CMOD)**
  Pros: No coding, business user configurable
  Cons: Limited by tool, may need ABAP for complex logic

- **Option C: SQL CASE / WHERE-IN (AMDP)**
  Pros: Fast, deterministic, traceable
  Cons: Not easy to change without code release

**Output Requirements:**
- Classification code (e.g., "STAGE_1", "STAGE_3")
- Rationale/triggering condition (for audit)
- Confidence level (if probabilistic)
- Effective date (when classification applies)
- Prior classification (for change tracking)

**Rerun Behavior:**
- Classification is non-monetary; no GL posting impact directly
- May trigger GL posting rule changes → posting recalc needed downstream

---

### Pattern 3: Calculation via SQL (AMDP - Formula-Driven)

**When to use:**
- Calculation is straightforward formula (e.g., interest = outstanding * rate * period)
- Result is numerical (accrual, reval delta, provision)
- High volume, deterministic, no branching

**Example: Interest Accrual Calculation**

```sql
PROCEDURE p_calc_interest_accrual(
  iv_as_of_date DATE,
  iv_method_ver STRING,
  OUT et_results TABLE OF z_accrual_result_s
) LANGUAGE SQLSCRIPT AS

  v_period_start := FIRST_DAY_OF_MONTH(LAST_DAY_OF_MONTH(ADD_MONTHS(iv_as_of_date, -1)) + 1);
  v_period_end := LAST_DAY(iv_as_of_date);
  v_period_days := DAYSSBETWEEN(v_period_start, v_period_end);

  et_results = SELECT
    deal_id,
    iv_as_of_date AS reporting_date,
    outstanding_amount,
    effective_rate,
    outstanding_amount * effective_rate * v_period_days / 360 AS accrued_amount,
    'INTEREST_CALC_v' || iv_method_ver AS method_used,
    NOW() AS calc_timestamp
  FROM deals
  WHERE deal_type = 'LOAN'
    AND active_flag = 'X'
    AND reporting_date <= iv_as_of_date;

ENDPROCEDURE;
```

**Input Requirements:**
- Deal data (outstanding, rate, product type)
- Period dates (from, to, day-count convention)
- Method version
- Any prior-period carryover (opening balance, prior accrual)

**Output Requirements:**
- Accrual/adjustment amount
- Basis (day-count method, rounding)
- Calculation date, method version
- Deal-to-GL mapping (if needed)

**Rerun Behavior:**
- Typically rerunnable: same date + same method version = same accrual
- If rerun during open period: reverse prior posting + repost new accrual
- If rerun after period closed: correction entry (GL document dated in current period)

---

### Pattern 4: Reconciliation via SQL Queries (Validation-Only)

**When to use:**
- Method is SQL-based data quality check
- No calculation; just validation
- Examples: deal-count reconciliation, total-amount validation, key completeness

**Template Reconciliation Query:**

```sql
-- Reconciliation: Deal Count by Product Type
PROCEDURE p_recon_deal_counts(
  iv_cvpm_run_id STRING,
  OUT et_recon_results TABLE OF z_recon_s
) LANGUAGE SQLSCRIPT AS

  et_recon_results = SELECT
    'DEAL_COUNT_BY_PRODUCT' AS check_name,
    product_type,
    COUNT(*) AS source_count,
    ( SELECT COUNT(*) FROM cvpm_results
      WHERE run_id = iv_cvpm_run_id
        AND product_type = t.product_type ) AS result_count,
    CASE
      WHEN COUNT(*) = ( SELECT COUNT(*) FROM cvpm_results ... ) THEN 'PASS'
      ELSE 'FAIL'
    END AS recon_status,
    NOW() AS check_timestamp
  FROM deals t
  GROUP BY product_type;

ENDPROCEDURE;
```

**Rerun Behavior:**
- Reconciliation is non-destructive; always rerunnable
- Typically run AFTER valuation/calculation methods complete

---

## Method Input/Output Contract

### Universal Input Contract (All Methods)

```
MANDATORY INPUTS:
├─ Reference/As-Of Date (reporting_date, valuation_date, period_end)
├─ Method Version (z_method_version)
├─ Deal Selection Criteria (filter: product type, segment, company code, etc.)
└─ Execution Context (batch job run ID, user, timestamp)

OPTIONAL INPUTS (Method-Specific):
├─ Prior Period Results (for carry-forward or comparison)
├─ Market Data Version (reference date for rates, curves, FX)
├─ Calculation Options (e.g., rounding decimals, day-count convention)
├─ Override Parameters (e.g., use fixed rate instead of market rate)
└─ Test/Debug Flags (limited output, explicit logging)
```

### Universal Output Contract (All Methods)

```
MANDATORY OUTPUTS:
├─ Result Table
│  ├─ Deal ID (or result key)
│  ├─ Calculation Result (valuation amount, classification code, accrual amount)
│  ├─ Calculation Date & Method Version
│  └─ Status (SUCCESS, WARNING, ERROR, INCOMPLETE)
├─ Error/Warning Log
│  ├─ Error Description (human-readable)
│  ├─ Affected Deals (count + sample)
│  ├─ Recommendation (skip deal? retry? escalate?)
│  └─ Timestamp & Severity
└─ Summary Metrics
   ├─ Total Deals Input
   ├─ Successfully Calculated
   ├─ Errors/Warnings
   ├─ Total Amount (if applicable)
   └─ Execution Time (seconds)
```

---

## Method Versioning & Fallback Strategy

### Why Versioning?

```
Scenario 1: Regulatory requirement changes (e.g., new IFRS 9 guidance)
→ Deploy new method version 2.0 in PROD
→ Keep version 1.0 available for audit trail / rerun capability

Scenario 2: Bug discovered in method version 1.0
→ Create version 1.1 (patch)
→ Rerun using 1.1 for all affected prior periods
→ Document which periods used which version

Scenario 3: Performance optimization
→ Version 2.0 is faster version 1.0, same output
→ Gradual rollout: test PROD with 10% of deals first
```

### Fallback Strategy

**Why:** If primary method fails (missing data, calculation error), run fallback to maintain continuity

```
FALLBACK_CHAIN Example:
Primary Method (Valuation v2.1: AMDP, complex formula)
  ↓ [On failure: missing market data, timeout, etc.]
Fallback 1 (Valuation v2.0: Simplified AMDP, fewer inputs)
  ↓ [On failure: unable to connect to data source]
Fallback 2 (Prior Period Method: Use last month's valuation, mark as stale)
  ↓ [On failure: no prior period exists]
Fallback 3 (Default: Mark deal as INCOMPLETE, manual override needed)
```

**Fallback Implementation:**
```abap
IF method_v2_1_status = 'ERROR' THEN
  -- Log error, attempt fallback
  method_v2_0_status = call_method( 'v2.0' );
  IF method_v2_0_status = 'SUCCESS' THEN
    result_used = 'FALLBACK_v2_0';
  ELSE
    -- Try prior period
    CALL prior_period_lookup( );
  ENDIF;
ENDIF;
```

---

## Common Method Implementation Pitfalls

| Pitfall | Risk | Prevention |
|---------|------|-----------|
| Method assumes all required fields exist | Calculation fails on missing data | Add data quality checks; use fallback |
| No version tracking of method used | Audit trail lost; can't explain prior results | Always store method_version in result |
| Single method handles too many products | Logic becomes unmaintainable | Split: method per product type |
| No timeout | Method runs forever, job hangs | Set max_runtime_sec; implement timeout logic |
| Calculation is non-deterministic | Reruns produce different results | Avoid RAND(), external API calls, current time functions |
| No error logging | Debugging production issues difficult | Log every step; include deal_id in every error message |
| Rounding inconsistent with GL | Posted amount ≠ sum of calculation results | Define rounding rule upfront in design |
| No prior-period carry-forward | Month-over-month accumulation inaccurate | If needed, fetch prior_period balance and add to current |

---

## Method Selection Decision Tree

```
START: You need a CVPM method
│
├─ "Is result NUMERIC (amount)?"
│  ├─ YES → "Is logic deterministic & formula-driven?"
│  │   ├─ YES → Use AMDP/SQL (Pattern 3)
│  │   └─ NO → Use ABAP with complex business rules (hybrid pattern)
│  └─ NO → "Is result CLASSIFICATION (code/category)?"
│      ├─ YES → "Can it be rule-based (IF...THEN...)?
│      │   ├─ YES → Use Rule Tree or CASE-based SQL (Pattern 2)
│      │   └─ NO → Use BADI/ABAP bridge (complex classification)
│      └─ NO → "Is this VALIDATION (no calc, just check)?"
│          ├─ YES → Use SQL reconciliation queries (Pattern 4)
│          └─ NO → Re-frame the requirement
│
└─ END: You have a method pattern
```

---

## Routing to Implementation Skills

Once method is designed:

| Method Category | Route To | Why |
|-----------------|----------|-----|
| **Valuation AMDP** | `amdp` skill | HANA pushdown, SQLScript expertise |
| **Classification BADI** | `abap` skill | OO design, interface implementation |
| **Calculation SQL** | `amdp` skill | Set-based SQL, performance optimization |
| **Reconciliation Query** | `reconciliation` skill | Query validation, data quality checks |
| **Wrapper / Job Control** | `abap` skill | Orchestration, error handling, batch integration |

---

## Pre-Method-Implementation Checklist

- [ ] Business requirement is clear (accrual? Valuation? Classification?)
- [ ] Method formula (or rules) finalized and documented
- [ ] Input data sources identified and available
- [ ] Output requirements defined (grain, precision, audit trail)
- [ ] Version strategy decided (v1.0 only? or versioning plan?)
- [ ] Fallback method identified (if primary fails)
- [ ] Error handling approach defined
- [ ] Rerun behavior specified (full? Incremental? Reversible?)
- [ ] Performance expectations documented (volume, runtime target)
- [ ] Testing strategy outlined (unit tests, integration tests, production validation)
