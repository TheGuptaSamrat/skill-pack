# CVPM Process Design Guide

**Source:** Extracted from FPSL Training Document
**Classification:** training-derived-concepts
**Usage:** Guide CVPM design by understanding standard FPSL process flows and methods
**Do not use for:** Customer-specific implementation details; use placeholders for actual process type names

---

## FPSL Standard Process Steps

The FPSL system defines a sequence of process steps that execute during day-end and period-end processing. These steps form the backbone of CVPM (Calculation and Valuation Process Management).

### Day Processing Phases

```
┌─────────────────────────────────────────────────────────────┐
│ INTRADAY (Operational)                                      │
├─────────────────────────────────────────────────────────────┤
│ • Register BT (Business Transaction)                        │
│ • Register MD (Master Data)                                 │
│ • Register AD (Analytical Attributes)                       │
│ • Define Lots                                               │
│ • Allocate Lots                                             │
│ • Impairment Attribute Determination                        │
└─────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────┐
│ END-OF-DAY PROCESSING                                       │
├─────────────────────────────────────────────────────────────┤
│ • Determine Amortized Cost (Preparatory)                    │
│ • Determine Fair Value (Preparatory)                        │
│ • Accrue (Interest accrual, fee accrual)                    │
│ • Defer (Deferral of income/costs)                          │
│ • Write Down (Impairment)                                   │
│ • Release (Fee/commission release)                          │
│ • Value TC (Trade Cost revaluation, if applicable)          │
│ • Move & Transform (Redelivery, cross-contract processing)  │
│ • Value FX (Foreign exchange revaluation)                   │
│ • Classify (Classification by accounting treatment)         │
│ • Classify P&L (OCI recycling on position exit)             │
│ • Manual Posting (User corrections, if needed)              │
└─────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────┐
│ PERIOD-END PROCESSING                                       │
├─────────────────────────────────────────────────────────────┤
│ • Across Allocate (Consolidation, allocation logic)         │
│ • Close (Period close, result finalization)                 │
│ • Carry Forward (Balance carry-forward to next period)      │
└─────────────────────────────────────────────────────────────┘
         ↓
┌─────────────────────────────────────────────────────────────┐
│ YEAR-END PROCESSING                                         │
├─────────────────────────────────────────────────────────────┤
│ • Balance Carry Forward (Cross-contract FY rollover)        │
│ • Open/Close Posting Periods (FY transition)                │
└─────────────────────────────────────────────────────────────┘
```

---

## CVPM-Relevant Process Steps (Deep Dive)

### Step 1: Register (Intraday)

**Purpose:** Ingest source contract/deal data into FPSL system

**Types:**
- **Register BT:** Business Transaction (deal entry, amended terms, etc.)
- **Register MD:** Master Data (deal master attributes)
- **Register AD:** Analytical Attributes (segment, desk, trader mapping)

**CVPM Role:** Input data collection for valuation

**Output Grain:** Deal level

**Prerequisites:**
- Deal master table populated
- Segment hierarchy configured
- Business transaction log with all modifications

---

### Step 2: Determine Amortized Cost (Preparatory, Period-End)

**Purpose:** Calculate amortized cost for financial instruments

**Characteristics:**
- Applicable to: Fixed-rate loans, bonds, leases with fixed economics
- Method: Effective interest rate calculation
- Amortization schedule: Contract start → maturity
- Premium/discount amortization: Linear or effective-yield method

**Formula (Simplified):**
```
Amortized Cost = Original Cost
                - Cumulative Principal Repayments
                - Cumulative Impairments
                + Cumulative Interest Accrual
```

**CVPM Role:** Primary valuation method for amortized cost financial instruments (IFRS 9 category 1)

**Data Requirements:**
- Original contract amount
- Interest rate (fixed or floating index)
- Day-count convention (30/360, ACT/360, ACT/ACT)
- Payment schedule (maturity date, coupon dates)
- Any prior impairments or write-downs

**Output Fields:**
- Amortized cost balance
- Period interest expense (accrual)
- Effective interest rate used
- Valuation date

---

### Step 3: Determine Fair Value (Preparatory, Period-End)

**Purpose:** Calculate fair value for financial instruments measured at FV

**Characteristics:**
- Applicable to: FVPL (Fair Value Through Profit/Loss), FVOCI (Fair Value Through OCI)
- Market data driven (prices, rates, curves, credit spreads)
- Valuation models: DCF, mark-to-market, mark-to-model

**Common Methods:**
1. **Mark-to-Market:** Use quoted market price (active market exists)
2. **DCF (Discounted Cash Flow):** Discount future cash flows to present value
   ```
   Fair Value = Σ [Cash Flow_t / (1 + Discount Rate)^t]
   ```
3. **OAS (Option-Adjusted Spread):** Adjust for embedded options

**CVPM Role:** Primary valuation method for financial instruments measured at fair value

**Data Requirements:**
- Quoted prices (if available)
- Yield curves (discount rates by tenor)
- Credit spreads (by counterparty rating)
- Volatility (for embedded options, derivatives)
- FX rates (for foreign currency instruments)

**Output Fields:**
- Fair value amount
- Valuation input source (market price, model, pricing service)
- Confidence level (active market vs. model-dependent)
- Valuation date

---

### Step 4: Accrue (End-of-Day, Period-End)

**Purpose:** Recognize periodic interest, fees, or income earned

**Characteristics:**
- Interest accrual: Daily, monthly, or per-period basis
- Fee accrual: Origination fees, management fees, commitment fees
- Day-count logic: ACT/360, 30/360, ACT/ACT
- Source: Fixed rate or floating rate index

**Formula (Interest Accrual):**
```
Accrued Interest = Outstanding Principal
                 × (Interest Rate / Year Fraction)
                 × (Days Accrued / Days in Period)
```

**CVPM Role:** Mandatory for all interest-bearing instruments

**Data Requirements:**
- Outstanding principal balance (from prior period or deal register)
- Interest rate (fixed or floating index + spread)
- Period start and end dates
- Day-count convention

**Output Fields:**
- Accrual amount
- GL posting destination (P&L interest expense account)
- Accrual reference (deal-level traceability)

---

### Step 5: Value FX (End-of-Day, Period-End)

**Purpose:** Revalue foreign currency positions to functional currency

**Characteristics:**
- Applicable to: Positions in currency ≠ functional currency
- Methods:
  - **Fixing of Postings:** Translate all transactions at transaction-date FX rate
  - **Monetary Asset Revaluation (MAR):** Revalue outstanding balance at period-end FX rate

**FX Gain/Loss Calculation:**
```
FX Unrealized Gain/Loss = Position Balance (TC) × (Rate_EOD – Rate_Prior)
```

**CVPM Role:** Mandatory for all FX-exposed positions

**Data Requirements:**
- Outstanding position in foreign currency
- FX spot rates: transaction date, prior period-end, current period-end
- Exchange rate category (daily vs. period-end vs. realised/unrealised)
- Multi-currency accounting setting (on/off)

**Output Fields:**
- FX gain/loss amount
- GL posting destination (P&L FX result account)
- FX fixing rate used (for audit trail)
- OCI FX reserve (if FVOCI treatment)

---

### Step 6: Classify (Period-End)

**Purpose:** Determine accounting classification for each instrument (IFRS 9 or local GAAP)

**IFRS 9 Classification Matrix:**

| Business Model | SPPI Test | Result |
|---|---|---|
| Hold to Collect | Pass | Amortized Cost (AC) |
| Hold to Collect | Fail | FVPL |
| Hold to Collect & Sell | Pass | FVOCI |
| Hold to Collect & Sell | Fail | FVPL |
| Other (Trading, Held for Sale) | — | FVPL |

**CVPM Role:** Drives which valuation method (Amortized Cost vs. Fair Value) to apply

**Data Requirements:**
- Original instrument classification
- Changes indicating remeasurement needed (business model shift, market conditions)
- Hedge accounting designation (if applicable)

**Output Fields:**
- Classification code (e.g., AC, FVPL, FVOCI)
- Effective date of classification
- Triggering event (if change from prior period)
- Justification (for audit trail)

---

### Step 7: Classify P&L (Period-End)

**Purpose:** Recycle OCI reserves to P&L upon partial/full position exit

**Mechanics:**
- When a FVOCI or FVOCI-with-recycling position is sold/matured:
  - Reclassify cumulative OCI reserve proportionally to P&L
  - Create matched gain/loss entry (removal from OCI, entry to P&L)

**Example:**
```
Position: 100 securities, cumulative OCI gain = 500
Action: Sell 50 securities
Recycling Entry:
  Dr. OCI Reserve (450)  [50/100 × 500]
  Cr. P&L Recycling Income (450)
```

**CVPM Role:** Mandatory for FVOCI-with-recycling instruments

**Data Requirements:**
- Prior period OCI reserve (by deal or position)
- Position exit detail (quantity/amount exiting)
- Original acquisition date and classification

**Output Fields:**
- OCI recycling amount
- GL posting destination (P&L recycling account)
- Reclassification date

---

### Step 8: Defer (End-of-Day, Period-End)

**Purpose:** Defer income/costs matching future periods

**Common Scenarios:**
- Loan origination fees → defer, amortize over loan life
- Prepaid interest → defer, recognize per accrual schedule
- Upfront discounts → defer, amortize over maturity

**Formula:**
```
Deferred Expense = Upfront Cost × (Remaining Term / Total Term)
Deferred Amort = Linear: Upfront Cost / Remaining Periods
```

**CVPM Role:** Required for instruments with non-standard fee arrangements

**Data Requirements:**
- Upfront income/cost amount
- Deferral schedule (maturity, term profile)
- Amortization method (linear or yield-based)

**Output Fields:**
- Period deferral/amortization amount
- GL posting destination (Deferral balance sheet + P&L amortization)

---

### Step 9: Write Down / Impairment (End-of-Day, Period-End)

**Purpose:** Record credit losses (Expected Credit Loss for IFRS 9, Incurred Loss for other GAAP)

**IFRS 9 Model:**
```
ECL = Probability of Default (PD) × Loss Given Default (LGD) × Exposure at Default (EAD)
```

**Characteristics:**
- Stage 1 (Inception - 12M ECL): No credit deterioration
- Stage 2 (Credit deterioration): Lifetime ECL
- Stage 3 (Default): Specific provision

**CVPM Role:** Required for credit-loss-exposed instruments (loans, bonds, etc.)

**Data Requirements:**
- Instrument rating or PD model
- LGD assumptions (recovery rate, collateral value)
- EAD (outstanding + undrawn commitments)
- Prior impairment balance (for stage transitions)

**Output Fields:**
- Impairment provision amount
- GL posting destination (P&L credit loss expense)
- Stage classification (1/2/3)
- Impairment reference (deal, model, date applied)

---

## CVPM Method Mapping to Process Steps

| Process Step | Method Type | Implementation | Rerunnable |
|---|---|---|---|
| Register | Data Load | ETL or manual entry | Yes |
| Determine Amortized Cost | Valuation | AMDP SQL or ABAP | Yes |
| Determine Fair Value | Valuation | AMDP SQL (DCF, models) | Yes |
| Accrue | Calculation | AMDP SQL (interest formula) | Yes |
| Value FX | Revaluation | AMDP SQL (FX spot rate lookup) | Yes |
| Classify | Classification | Rule tree or SQL CASE | Yes |
| Classify P&L | Recycling | ABAP (complex GL logic) | Rerunnable if no posting yet |
| Defer | Amortization | AMDP SQL (schedule-based) | Yes (overwrites) |
| Write Down | Impairment | AMDP SQL (ECL models) | Yes (full recalc) |

---

## CVPM Run Strategy: Which Steps to Execute?

**Decision Points:**

```
START: Determine CVPM Scope
│
├─ "Is this a periodic valuation run (month/quarter end)?"
│  ├─ YES → Execute full cycle (Register → Accrue → FX → Classify → Close)
│  └─ NO → Go to next question
│
├─ "Is this an intra-period update (deal amendment, rate change)?"
│  ├─ YES → Re-run Register + impacted methods only
│  └─ NO → Go to next question
│
└─ "Is this a correction/rerun after period-close?"
   ├─ YES → Reverse prior posting + re-run full cycle
   └─ NO → One-time manual adjustment (rare)
```

---

## Integration with GL (General Ledger) Posting

**After Each CVPM Step:**
```
Method produces result (e.g., 1M accrual)
  ↓
CVPM Result staging table updated
  ↓
GL posting logic: Result → Posting line items
  ↓
GL Document created (posting date = period end)
  ↓
Audit trail: Deal → CVPM result → GL posting
```

---

## Pre-CVPM Run Checklist

- [ ] All required process steps identified (which of the 9 steps applies?)
- [ ] Deal master loaded and validated (Register complete)
- [ ] Market data as-of-date available (rates, curves, FX, spreads)
- [ ] Prior period results available (carry-forward, prior balances)
- [ ] GL posting account rules configured
- [ ] Worklist preview configured (if user approval needed)
- [ ] Threading strategy finalized (parallelization, batch size)
- [ ] Rerun protocol clear (full recalc or incremental?)
- [ ] Error handling defined (fail fast or continue?)

---

## Next Steps: From Process Design to Implementation

Once CVPM process steps are identified:

1. **Route to `mapping` skill** → Define source-to-CVPM-staging data flow
2. **Route to `amdp` skill** → Design SQL-based valuation/calculation methods
3. **Route to `abap` skill** → Wrapper class, orchestration, error handling
4. **Route to `reconciliation` skill** → Validation queries, data quality checks
