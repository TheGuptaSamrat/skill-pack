# CVPM Data Integration

**Classification:** FPSL-standard-guidance
**Usage:** Reference when designing data staging and integration for CVPM
**Do not use for:** Customer-specific table names without placeholders; route detailed mapping to `mapping` skill

---

## Data Integration Phases

```
┌──────────────────────────────────────────────────────┐
│ Phase 0: Requirement Gathering                       │
│ └─ Which FPSL products? Segments? Accounting objective?
├──────────────────────────────────────────────────────┤
│ Phase 1: Source Data Identification                  │
│ └─ Deal master, segment hierarchy, market data sources
├──────────────────────────────────────────────────────┤
│ Phase 2: Staging & Preparation                       │
│ └─ CDS views, temporary tables, data quality checks  │
├──────────────────────────────────────────────────────┤
│ Phase 3: CVPM Method Execution                       │
│ └─ Run AMDP/ABAP calculation methods (see cvpm-method-design.md)
├──────────────────────────────────────────────────────┤
│ Phase 4: Result Validation                           │
│ └─ Reconciliation queries, drill-down checks (route to reconciliation skill)
└──────────────────────────────────────────────────────┘
```

---

## Phase 1: Source Data Identification

### 1.1 Deal Master Data

**Purpose:** Primary source for contracts/instruments to process

**Typical Fields:**
| Field | Example | Usage in CVPM |
|-------|---------|--------------|
| DEAL_ID | 10001234 | Join key for all subsequent processing |
| DEAL_TYPE | LOAN, BOND, FX, DERIV | Filter; method routing |
| PRODUCT_CODE | ZFRI_LOAN_FIXED | Method determination (which valuation method?) |
| COUNTERPARTY_ID | CPTY_5678 | Risk; rating lookup |
| COUNTERPARTY_RATING | AA-, BB+, NR | IFRS 9 stage; provision; revaluation |
| PORTFOLIO_CODE | PORT_TRADING, PORT_BANKING | Segment; GL posting; threading scope |
| CURRENCY | USD, EUR, JPY | FX revaluation; data sourcing (rate lookups) |
| INSTRUMENT_AMOUNT | 1000000.00 | Calculation basis (interest = amount * rate) |
| INSTRUMENT_AMOUNT_UNIT | If applicable (e.g., shares, notional) |
| EFFECTIVE_START_DATE | 2024-01-15 | Period calculation (start of accrual period) |
| MATURITY_DATE | 2029-01-15 | Remaining term; amortization schedule |
| INTEREST_RATE_TYPE | FIXED, FLOATING | Method selection (floating = market data lookup) |
| INTEREST_BASE_RATE | 3.50% or 0bps | If fixed |
| INTEREST_SPREAD | 2.00% | If floating: BASE_RATE + SPREAD logic |
| INTEREST_RATE_INDEX | EURIBOR_3M, SOFR_3M | Market data key for rate lookup |
| INTEREST_DAY_COUNT | 30/360, ACT/360, ACT/ACT | accrual calculation |
| ACCOUNTING_TREATMENT | AMORTIZED_COST, FVPL, FVOCI | GL account, posting logic |
| EXPECTED_LOSS_RATE | 0.45% | Provision calculation |
| PRIOR_PERIOD_VALUATION | 1002500.50 | Carry-forward (for reval delta) |
| INTERNAL_NOTES | e.g., "RESTRUCTURED" | Flag for classification methods |
| STATUS | ACTIVE, MATURING, MATURED | Filter; exclusion rules |

**Source System/Table:**
- (Placeholder: Internal deal master? S/4HANA? External system?)
- Typical SAP approach: Z-table or CDS view over deal registry
- FPSL reference: Could be `/BA1/...` table (confirm from customer landscape)

**Data Quality Checks:**
```sql
-- Deal master pre-screening
check: DEAL_ID is NOT NULL
check: DEAL_TYPE in ('LOAN', 'BOND', 'FX', ...)
check: INSTRUMENT_AMOUNT > 0
check: EFFECTIVE_START_DATE ≤ MATURITY_DATE
check: PRODUCT_CODE exists in product master
check: COUNTERPARTY_ID exists in counterparty master (if applicable)
```

---

### 1.2 Segment / Organization Hierarchy

**Purpose:** Route deals to correct GL profit center, segment for analytics

**Typical Structure:**
```
Hierarchy:
  COMPANY → BUSINESS_LINE → DESK → TRADER

Examples:
  ┌─ COMPCO_001 (Company Code)
  │  ├─ BANKING (Business Line)
  │  │  ├─ LOANS_DESK (Desk)
  │  │  └─ TRADING_DESK
  │  └─ TRADING (Business Line)
  │     ├─ FX_DESK
  │     └─ DERIVATIVES_DESK
  └─ COMPCO_002
```

**Key Fields for CVPM:**
```
SEGMENT_ID → SEGMENT_DESC
PROFIT_CENTER_ID → PROFIT_CENTER_DESC
COST_CENTER_ID (optional)
BUSINESS_LINE (affects GL posting rules)
MANAGER_ID (for approval routing if worklist used)
```

**Data Quality Checks:**
```sql
check: Every deal.PORTFOLIO_CODE exists in segment hierarchy
check: Segment hierarchy has no circular references
check: PROFIT_CENTER status = ACTIVE
```

---

### 1.3 Market Data (Reference Rates)

**Purpose:** Provides FX rates, interest curves, credit spreads, volatility (if needed)

**Type 1: FX Rates (For FX Revaluation)**

| Field | Example | Usage |
|-------|---------|-------|
| CURRENCY_PAIR | EUR/USD | Join key for rate lookup |
| RATE_DATE | 2024-03-20 | As-of date for valuation |
| SPOT_RATE | 1.0850 | Direct application |
| BID_RATE, ASK_RATE (optional) | 1.0848, 1.0852 | Conservative mid-rate |
| SOURCE | BLOOMBERG, ECB, INTERNAL | For audit trail |
| QUALITY_FLAG | REAL_TIME, EOD, HISTORICAL | Staleness check |

**Type 2: Interest Curves (For Bond/Loan Valuation)**

| Field | Example | Usage |
|-------|---------|-------|
| CURVE_ID | EUR_OIS, EUR_IBOR_3M | Matches floating rate index |
| TENOR | 3M, 1Y, 5Y, 10Y | Interpolation point |
| RATE_VALUE | 3.45% | Risk-free rate or index |
| CURVE_DATE | 2024-03-20 | As-of date |
| INTERPOLATION_METHOD | LINEAR, SPLINE | Calculation method for intermediate tenors |

**Type 3: Credit Spreads (For IFRS 9 / Fair Value)**

| Field | Example | Usage |
|-------|---------|-------|
| COUNTERPARTY_ID | CPTY_5678 | Join key |
| SPREAD_BPS | 250 bps | Credit margin |
| SPREAD_DATE | 2024-03-20 | As-of date |
| VERSION | 1.0, 2.0 (regulatory update) | Versioning |

**Market Data Sourcing:**
- Real-time feed (Bloomberg, Reuters, SAP Data Hub)
- EOD (end-of-day file upload)
- Manual upload (if no feed available)
- Fallback (use prior EOD if real-time unavailable)

**Data Quality Checks:**
```sql
check: No missing rates for rate_date and currencies used
check: SPOT_RATE in plausible range (not 100x prior day)
check: CURVE_DATE ≤ reporting_date (no future rates)
check: If rate older than X days, flag as STALE_WARNING
```

**Staleness Handling:**
```
IF market_data is missing for reporting_date THEN
  TRY: Use prior EOD rate + mark result as 'STALE_DATA'
  CATCH: If no prior rate exists → method fails → fallback to prior period value
ENDIF
```

---

### 1.4 Prior Period Results (Carry-Forward)

**Purpose:** Required for:
- Reval delta (current valuation - prior valuation)
- Cumulative accrual tracking
- Incremental processing
- Audit trail (version history)

**Typical Fields:**
```
DEAL_ID
PRIOR_PERIOD_DATE (e.g., 2024-02-29)
PRIOR_PERIOD_AMOUNT (the valuation/accrual from last month)
METHOD_VERSION_USED (to detect if method changed)
PRIOR_GL_POSTING_AMOUNT (if already posted)
```

**Carry-Forward Logic:**
```
IF rerun_during_OPEN_period THEN
  -- Reverse prior posting, recalculate, repost
  GL_reversal_amount = -1 * prior_gl_posting_amount
  GL_new_posting_amount = current_calculation_result

ELSIF rerun_during_CLOSED_period THEN
  -- Issue correction entry (posterior adjustment)
  GL_correction_amount = current_calculation_result - prior_calculation_result
  GL_posting_date = current_period (not prior period)
ENDIF
```

---

## Phase 2: Staging & Preparation

### 2.1 CDS View Design (Recommended)

**Why CDS instead of direct table access:**
- Encapsulation (deal logic in one place)
- Performance optimization (push predicates to DB)
- Consistency across multiple CVPM methods
- Field masking/security

**Template CDS View: Deal Master for CVPM**

```abap
@AbapCatalog.sqlViewName: 'ZCVPM_DEAL_STAGING_V'
@AbapCatalog.compiler.compareFilter: true
@AccessControl.authorizationCheck: #CHECK
@EndUserText.label: 'CVPM Deal Staging'

define view ZCVPM_DEAL_STAGING
  as select from zdeal_master as d
    inner join zsegment_hierarchy as s on d.portfolio_code = s.segment_id
    inner join zproduct_master as p on d.product_code = p.product_code
    left outer join zprior_valuation as pv on d.deal_id = pv.deal_id
                                           and pv.valuation_date = :lv_prior_period_date
{
  d.deal_id,
  d.deal_type,
  d.product_code,
  p.product_desc,
  d.counterparty_id,
  d.instrument_amount,
  d.currency,
  d.interest_rate_type,
  d.interest_rate_index,
  d.effective_start_date,
  d.maturity_date,
  d.accounting_treatment,
  s.segment_id,
  s.profit_center_id,
  s.business_line,
  pv.prior_valuation_amount,
  cast(pv.valuation_date as nvarchar(10)) as prior_valuation_date,
  cast(:lv_reporting_date as nvarchar(10)) as reporting_date,
  'd' as view_type  // for debugging
}
where d.status = 'ACTIVE'
  and d.company_code = $param1.company_code
  and d.effective_start_date ≤ $param1.reporting_date
  and d.maturity_date ≥ $param1.reporting_date
```

---

### 2.2 Data Quality Checks (SQL)

Before CVPM methods run:

```sql
-- Check 1: Data completeness
SELECT COUNT(*) as incomplete_deals
FROM cvpm_staging
WHERE deal_id IS NULL
   OR instrument_amount IS NULL
   OR accounting_treatment IS NULL
HAVING COUNT(*) > 0;
-- ✓ PASS: 0 rows
-- ✗ FAIL: > 0 → investigate, fix, retry

-- Check 2: Referential integrity
SELECT deal_id, portfolio_code
FROM cvpm_staging
WHERE portfolio_code NOT IN (SELECT segment_id FROM segment_hierarchy)
-- ✓ PASS: 0 rows
-- ✗ FAIL: > 0 → investigate, remove from staging, retry

-- Check 3: Date logic
SELECT deal_id, effective_start_date, maturity_date
FROM cvpm_staging
WHERE effective_start_date > maturity_date
-- ✓ PASS: 0 rows
-- ✗ FAIL: > 0 → data source issue, escalate

-- Check 4: Amount reasonableness
SELECT deal_id, instrument_amount
FROM cvpm_staging
WHERE instrument_amount < 0
   OR instrument_amount > 1000000000000  // 1 trillion threshold
-- ✓ PASS: 0 rows
-- ✗ FAIL: > 0 → data validation rule breach
```

**Data Quality Report Template:**
```
CVPM Staging Data Quality Report
═════════════════════════════════════════
Run Date: 2024-03-20
Reporting Period: Mar 2024
CVPM Job: INTEREST_ACCRUAL_v2.1

Total Deals in Source: 15,234
After ACTIVE filter: 15,123
After Date Range filter: 14,987
Passed ALL Quality Checks: 14,987 ✓

Issues Found:
├─ Incomplete records (missing amount): 2 [Escalate]
├─ Missing market data (FX rate): 45 [Use fallback rate]
└─ Invalid accounting treatment: 3 [Exclude; manual review]

Ready to proceed: YES (14,987 of 15,234 = 98.4%)
```

---

### 2.3 Market Data Lookup / Enrichment

**Process:**
```
For each deal in staging:
  1. Identify which market data needed (based on product + interest type)
  2. Lookup rate as of reporting_date
  3. If missing: use fallback (prior EOD? static rate? fail?)
  4. Add market rate to staging row
```

**Template Query: Fetch Market Data for Floating-Rate Loan**

```sql
SELECT
  s.deal_id,
  s.interest_rate_index,
  m.rate_value AS market_rate,
  m.rate_date,
  CASE
    WHEN m.rate_date < CURRENT_DATE - 3 THEN 'STALE'
    WHEN m.rate_date = CURRENT_DATE THEN 'REAL_TIME'
    ELSE 'EOD'
  END AS rate_quality,
  COALESCE(m.rate_value, lag_m.rate_value, fallback_m.rate_value) AS effective_rate,
  COALESCE(m.rate_date, lag_m.rate_date, fallback_m.rate_date) AS effective_rate_date
FROM cvpm_staging s
LEFT OUTER JOIN market_rates m
  ON s.interest_rate_index = m.curve_id
  AND m.rate_date = s.reporting_date
LEFT OUTER JOIN market_rates lag_m
  ON s.interest_rate_index = lag_m.curve_id
  AND lag_m.rate_date = s.reporting_date - 1  // prior day if missing
LEFT OUTER JOIN market_rates fallback_m
  ON s.interest_rate_index = fallback_m.curve_id
  AND fallback_m.rate_date = LAST_DAY(s.reporting_date - 30)  // last available
```

---

## Phase 3: CVPM Method Execution

(See `cvpm-method-design.md` for detailed method patterns)

Once staging is complete:

1. **Initialize method** with correct version
2. **Pass staging data** + parameters (reporting_date, method_version)
3. **Execute method** (AMDP valuation, classification rule, accrual calculation)
4. **Capture result** (valuation amount, status, audit trail)
5. **Handle errors** (log, fallback, or fail)

**Orchestration Template (ABAP):**

```abap
METHOD orchestrate_cvpm_run.

  " Step 1: Validate staging complete
  PERFORM validate_staging.

  " Step 2: Initialize result table
  CLEAR gt_cvpm_results.

  " Step 3: Call method
  TRY.

    CALL METHOD z_cvpm_interest_acr_amdp=>calculate_valuation
      EXPORTING
        iv_reporting_date = lv_reporting_date
        iv_method_version = '2.1'
      IMPORTING
        et_results = gt_cvpm_results
        ev_status = lv_method_status.

    IF lv_method_status ≠ 'SUCCESS'.
      WRITE: 'Primary method failed; attempting fallback'.
      PERFORM call_fallback_method.
    ENDIF.

  CATCH cx_method_error INTO lcx_error.
    WRITE: 'Method exception: ' lcx_error->get_text().
    PERFORM call_fallback_method.

  ENDTRY.

  " Step 4: Result validation (route to reconciliation skill)
  PERFORM validate_results.

  " Step 5: Staging for GL posting (route to abap skill for posting logic)
  PERFORM stage_for_posting.

ENDMETHOD.
```

---

## Phase 4: Result Validation

(Route detailed SQL queries to `reconciliation` skill)

**High-Level Validation Checks:**

```sql
-- Completeness check
SELECT 'Missing results for X% of deals' AS check_name
WHERE (SELECT COUNT(*) FROM cvpm_results)
      < (SELECT COUNT(*) FROM cvpm_staging) * 0.95;

-- Reasonableness check
SELECT deal_id, valuation_amount
WHERE valuation_amount < -1000000000 OR valuation_amount > 10000000000;

-- Reconciliation check
SELECT 'Sum of results vs. expected range'
WHERE SUM(valuation_amount) NOT BETWEEN X AND Y;
```

---

## Integration Points

| Phase | Output | Consumed By | Skill |
|-------|--------|-------------|-------|
| Staging | CDS view + temp table | CVPM methods | cvpm |
| Quality checks | Validation report | CVPM operator | (operational) |
| Method execution | Result table | GL posting logic + reconciliation | abap + reconciliation |
| Result validation | Reconciliation report | CVPM operator | reconciliation |

---

## Common Data Integration Pitfalls

| Pitfall | Risk | Prevention |
|---------|------|-----------|
| Staging joins on deal_id without row dedup | Cartesian product; wrong deal counts | Add DISTINCT or GROUP BY |
| Market data sourced without staleness check | Calculations based on old rates | Flag stale data; use fallback |
| No prior period carry-forward | Reval calcs incomplete | Fetch prior_period result; handle missing |
| Deal filter too restrictive | Critical deals excluded | Verify filter logic with business |
| Segment hierarchy not up-to-date | Deals with wrong profit center | Validate hierarchy before run |
| CDS view without appropriate indexes | Staging query slow; timeout | Index on deal_id, reporting_date |

---

## Data Integration Checklist

**Pre-CVPM Execution:**

- [ ] Deal master sourced and counted against source system
- [ ] Segment hierarchy verified (all deals map to valid segment)
- [ ] Market data available as-of reporting date (or fallback identified)
- [ ] Prior period results available (if carry-forward needed)
- [ ] CDS views / staging tables ready
- [ ] Data quality checks run; issues resolved
- [ ] Staging row count = expected deal count ± acceptable variance
- [ ] Sample of 10 deals spot-checked manually
- [ ] All required fields non-null
- [ ] Test run completed successfully
