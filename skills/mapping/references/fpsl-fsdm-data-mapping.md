---
name: "FSDM-to-FPSL Data Mapping and Integration"
description: "Data loading process, mapping views, value mapping, and field transformations"
source: "Building SAP FPSL_FSDM Golden Source.docx - Sections 4, 5"
date: 2026-03-22
applies_to: "mapping"
---

# FSDM-to-FPSL Data Mapping Reference

**Source:** Building SAP FPSL_FSDM Golden Source.docx  
**Extracted:** 2026-03-22  
**Applies To:** mapping skill (Data Integration and Mapping Specs)

---

## 1. FSDM-to-FPSL Integration Architecture

### 1.1 Integration Philosophy

- **FSDM Role:** Harmonized data provisioning layer
  - Central data hub consolidating source systems
  - Standardized banking data model (CDM)
  - "Single source of truth" for contracts, instruments, events
  
- **FPSL Role:** Consumption and accounting processor
  - Reads from FSDM via data loading (DL) process
  - Performs valuation, accounting, and subledger posting
  - Maintains contract-level granularity for auditing

- **Connection Paradigm:** Unidirectional data flow
  - FSDM → FPSL via standardized mapping views
  - No feedback loop (FPSL does not modify FSDM)
  - FSDM change pointer mechanism triggers DL extracts

### 1.2 Data Loading (DL) Process Workflow

**Sequence (Standardized for all FSDM-FPSL implementations):**

#### Step 1: Change Pointer Generation
**Purpose:** Identify new or modified objects in FSDM since last load

**Mechanism:**
- FSDM tracks change pointers on business entities
- Pointers reset after successful extract
- New/modified entities flagged with timestamp

**Extraction Parameters:**
```
Last_DL_Run_Timestamp ← Read from FPSL DL status table
Modified_After ← FSDM.change_pointer > Last_DL_Run_Timestamp
Objects_to_Extract ← FSDM entities WHERE modified_after = TRUE
```

#### Step 2: Data Extraction
**Purpose:** Retrieve modified objects from FSDM

**Mechanism:** Remote-enabled Function Modules (RFMs)

**Function Group:** /FSDL/EXTRACT

**Key RFMs:**
- `/FSDL/RFM_EXTRACT_CONTRACTS` - Fetch contract master data
- `/FSDL/RFM_EXTRACT_INSTRUMENTS` - Fetch security/instrument data
- `/FSDL/RFM_EXTRACT_TRANSACTIONS` - Fetch business transactions
- `/FSDL/RFM_EXTRACT_CASHFLOWS` - Fetch expected/actual cashflows
- `/FSDL/RFM_EXTRACT_EVENTS` - Fetch business events

**RFM Call Pattern:**
```ABAP
CALL FUNCTION '/FSDL/RFM_EXTRACT_CONTRACTS' DESTINATION 'FSDM_SYSTEM'
  IMPORTING
    iv_changed_after = last_dl_timestamp
  EXPORTING
    et_contracts = []
    ev_result_code = result.
```

#### Step 3: Transformation and Mapping
**Purpose:** Transform FSDM structure to FPSL target format

**Mechanism:** CDS Mapping Views (/FSDL/MV_*)

**Transformation Layers:**
```
Extract Layer (RFM Output)
         ↓
   [CDS Projection Layer]
         ↓
Mapping View Layer (/FSDL/MV_*)
   - Filter invalid records
   - Join auxiliary tables (CoA, rates, customer)
   - Apply value mappings (LOT_ID, accrual types, etc.)
   - Derive target FPSL fields
         ↓
   [Data Staging Tables]
         ↓
FPSL Consumption Layer
```

#### Step 4: Data Ingestion
**Purpose:** Load mapped data into FPSL tables

**Mechanism:** FPSL Data Import APIs

**Target Tables:**
- `BA_BASICDATA` - Master data (customer, contract terms)
- `BA_TRANSACTIONDATA` - Contract transactions (for loans/deposits)
- `BA_POSITION_DATA` - Security positions (for equities/bonds)
- `BA_CASHFLOWDATA` - Expected and actual cashflows
- `BA_BUSINESSEVENTS` - Event trigger records

**Ingestion Validation:**
- Primary key uniqueness
- Mandatory field completeness
- Reference integrity (customer ID, GL account exists)
- Amount validity (non-negative, within range)

---

## 2. Standard Mapping Views (/FSDL/MV_*)

### 2.1 /FSDL/MV_BUSINESSTRANSACTIONS

**Function:** Maps FSDM banking settlements to FPSL business transaction records

**Source:** FSDM transactions + business events

**Selection Logic:**
```
Source FSDM Data:
  - Transaction_ID (primary key)
  - Transaction_Type (DISBURSEMENT, REPAYMENT, FEE, etc.)
  - Contract_ID (links to contract master)
  - Amount, Currency, Booking Date
  - PCI (Product Catalog Item)
  - Event_Queue (triggered by business events)

Mapping Logic:
  - Validate transaction type against permitted values
  - Link to contract via Contract_ID
  - Apply accrual mapping rules
  - Derive FPSL posting account from CoA + transaction type
  - Calculate posting amount (incl. sign conventions)

Output to FPSL:
  - BA1_TRANID (Transaction ID, unique)
  - BA1_CONTRACTID (Reference to BA_BASICDATA)
  - BA1_C55TTYPE (Mapped transaction type)
  - BA1_AMOUNT (Posted amount)
  - BA1_POSTING_ACCOUNT (GL Account from CoA)
```

**2023 Performance Enhancement:**
- **Mirror Contract Identifiers:** Added two new fields
  - `BA1_C55R5CNID` - Contract ID for loan/deposit contracts
  - `BA1_C55R6CNID` - Contract ID for securities positions
- **Purpose:** Enables faster join logic without full cross-system lookup
- **Benefit:** Reduces extraction time by ~40% for large portfolios

### 2.2 /FSDL/MV_BASICDATA

**Function:** Provisions master data for financial contracts

**Source:** FSDM Contract Master + Customer Master

**Selection Logic:**
```
Source FSDM Data:
  - Contract_ID, Customer_ID
  - Contract_Type (LOAN, DEPOSIT, etc.)
  - Start_Date, Maturity_Date
  - Principal_Amount, Current_Balance
  - Interest_Rate_Type (FIXED, FLOATING)
  - Credit_Facility_ID (for structured products)

Mapping Logic:
  - Validate contract type (route to correct FPSL table)
  - Classify contract vs. security
  - Determine template (standard vs. structured)
  - Look up customer credit rating (for ECL staging)
  - Apply initial fair value (market rates at origination)

Output to FPSL:
  - BA1_CONTRACTID, BA1_CUSTOMERID
  - BA1_CONTRACTTYPE, BA1C/HDRTEMPL
  - BA1_START_DATE, BA1_MATURITY_DATE
  - BA1_PRINCIPAL_AMOUNT
  - BA1_CLASSIFICATION (AC, FVTPL, FVOCI per IFRS 9)
  - BA1_INITIAL_FV (Fair value at origination)
```

**2023 Enhancement:**
- **New View:** `/FSDL/CV_FINANCIALCONTRACT_UN` (Unstructured Contracts)
- **Optimization:** Pre-joins complex join logic (customer, facility, rates)
- **Benefit:** Extractions of unstructured contracts +30% faster

### 2.3 /FSDL/MV_SECURITIESBASICDATA

**Function:** Handles master data for financial instruments (securities)

**Source:** FSDM Instrument Master + Pricing Data

**Selection Logic:**
```
Source FSDM Data:
  - Instrument_ID, Instrument_Class (EQUITY, BOND, DERIVATIVE)
  - Issuer_ID, Maturity_Date
  - Nominal_Amount, Current_Price, Currency
  - Coupon_Rate (for bonds), Dividend_Yield (for equities)

Mapping Logic (with 2023 Updates):
  - For equities & funds: SUPPRESS contract start/end dates
    (Reason: equity/fund positions are perpetual, no maturity)
  - For bonds: Keep maturity date (fixed term)
  - Look up issuer credit rating (for ECL staging)
  - Retrieve current market price for FV calculation
  - Validate currency matching portfolio currency

Output to FPSL:
  - BA1C_INSTID, BA1C_ISSUERID
  - BA1C_FITYPE (Mapped instrument class)
  - BA1C_MATURITY_DATE (bonds only; NULL for equities/funds)
  - BA1C_NOMINAL_AMOUNT
  - BA1C_CURRENT_PRICE (market value)
  - BA1C_CLASSIFICATION (typically FVTPL for securities)
  - BA1C_FV (Fair value = Current_Price × Nominal_Amount)
```

**2023 Specific Handling:**
| Instrument Class | Start/End Date | Maturity Date | FPSL Treatment |
|---|---|---|---|
| EQUITY | SUPPRESS | NULL | Perpetual position |
| BOND | SUPPRESS | RETAIN | Fixed maturity, interest-bearing |
| DERIVATIVE | SUPPRESS | RETAIN | Term-limited contingent claim |
| FUND | SUPPRESS | NULL | Perpetual fund units |

### 2.4 /FSDL/MV_INTERESTACCRUALS_COND

**Function:** Aggregates fine-granular FSDM accrual types into broader FPSL accrual categories

**Purpose:** Prevent key-conflict errors during processing (NEW in 2023)

**Source:** FSDM Accrual Transactions + Accrual Type Master

**Selection Logic:**
```
Source FSDM Data:
  - Accrual_Type (granular, e.g., REGULAR_FIXED, STRUCTURED_FLOAT, DEFERRED_CONV)
  - Interest_Type (FIXED, FLOATING, VARIABLE)
  - Contract_ID, Accrual_Amount, Accrual_Date

Aggregation Logic (NEW - prevents key conflicts):
  - FSDM has 50+ accrual type granularities
  - FPSL expects 5-7 broad accrual categories
  - View maps: FSDM fine-grained → FPSL categories
  - Aggregate amounts for duplicate keys

Mapping:
  FSDM_ACCRUAL_TYPE          → FPSL_ACCRUAL_CATEGORY
  REGULAR_FIXED              → AC-STD
  REGULAR_FLOATING           → AC-FLT
  STRUCTURED_FIXED           → AC-SUB
  STRUCTURED_FLOAT           → AC-SUB
  DEFERRED_FIXED             → AC-DEF
  DEFERRED_VARIABLE          → AC-DEF

Output to FPSL:
  - BA1_CONTRACTID
  - BA1/C55ACCAT (Aggregated accrual category)
  - BA1_ACCRUAL_AMOUNT (summed across FSDM granularities)
  - BA1_ACCRUAL_DATE
```

**Key Benefit:** Eliminates "duplicate key" errors when loading aggregated accruals

---

## 3. Value Mapping Tables (Part 2: Field Transformation Detail)

### 3.1 Field-Level Transformation Examples

#### LOT_ID (Lot Identifier) - CRITICAL NUANCE

**Issue:** Character length mismatch
- FSDM Field: LOT_ID (128 char)
- FPSL Field: LOT_ID (15 char)

**Mapping Strategy:**

**Option A: Truncate (Lossy)**
```
FSDM_LOT_ID = "PORTFOLIO_2024_TERM_LOAN_BATCH_001_ABC123"  (40 chars)
FPSL_LOT_ID = "PORTFOLIO_2024_"                            (15 chars, truncated)
Risk: Loss of batch specificity; potential collisions
```

**Option B: Hash (Deterministic)**
```
FSDM_LOT_ID = "PORTFOLIO_2024_TERM_LOAN_BATCH_001_ABC123"
Hash(LOT_ID) = "7A9F2E3C1B"                                  (10 char hash)
FPSL_LOT_ID = "LOT_7A9F2E3"                                  (15 chars, prefix + hash)
Benefit: Deterministic, collision-resistant, preserves batch attribution
```

**Recommended Configuration:**
```sql
FUNCTION LOT_ID_TRANSFORM (p_fsdm_lot_id IN VARCHAR2(128))
RETURN VARCHAR2(15) AS
BEGIN
  IF LENGTH(p_fsdm_lot_id) <= 15 THEN
    RETURN p_fsdm_lot_id;  -- Passthrough if ≤ 15
  ELSE
    -- Hash approach: deterministic mapping
    RETURN 'LOT_' || SUBSTR(DBMS_OBFUSCATION.MD5(p_fsdm_lot_id), 1, 11);
  END IF;
END;
```

#### Contract ID / Instrument ID Mapping

**Scenario:** FSDM contract IDs may be longer or use different naming convention than FPSL

**Mapping Logic:**
```
FSDM_CONTRACT_ID = "FSDM-2024-001-TERM_LOAN-ABC"  (27 chars)
             ↓
  [Lookup in Mapping Table]
             ↓
FPSL_CONTRACT_ID = "C00012345"  (9 chars, normalized alphanumeric)
```

**Mapping Table Structure:**
| FSDM_ID | FSDM_ID_TYPE | FPSL_ID | MAPPING_STATUS | SYNC_DATE |
|---|---|---|---|---|
| FSDM-2024-001-TERM_LOAN-ABC | CONTRACT | C00012345 | ACTIVE | 2026-03-22 |
| FSDM-2024-002-FIXED_DEPOSIT-DEF | CONTRACT | C00012346 | ACTIVE | 2026-03-22 |

---

## 4. Contract vs. Security Routing Logic

### 4.1 Classification Decision Tree

**Question 1:** Is this a standard banking product (loan, deposit, account)?

**Yes → Question 2:** Does it contain embedded derivatives?
  - **No:** Route to BA_TRANSACTIONDATA (Contract Table)
  - **Yes → Question 3:** Is the embedded derivative material?
    - **No:** Simplify; route to BA_TRANSACTIONDATA
    - **Yes:** Route to BA_POSITION_DATA (Security Table); treat components separately

**No → Question 2:** Is this a standalone investable instrument?
  - **Yes:** Route to BA_POSITION_DATA (Security Table)
  - **No:** Route to BA_TRANSACTIONDATA (default handling)

### 4.2 Mapping View Implementation

**Pseudocode (in CDS Mapping View):**

```abap
DEFINE VIEW /FSDL/V_CONTRACT_CLASSIFICATION AS
SELECT FROM dbt_fsdm_contracts
  INNER JOIN dbt_fsdm_instruments ON contracts.instr_id = instruments.instr_id
  {
    contracts.contract_id,
    contracts.contract_type,  // LOAN, DEPOSIT, ACCOUNT, etc.
    instruments.instr_class,  // EQUITY, BOND, DERIVATIVE, FUND
    instruments.embedded_derivative_flag,
    
    CASE
      WHEN contracts.contract_type IN ('LOAN', 'DEPOSIT', 'ACCOUNT')
           AND instruments.embedded_derivative_flag = 'FALSE'
        THEN 'CONTRACT'  // Route to BA_TRANSACTIONDATA
      WHEN contracts.contract_type IN ('LOAN', 'DEPOSIT', 'ACCOUNT')
           AND instruments.embedded_derivative_flag = 'TRUE'
           AND instruments.derivative_materiality = 'HIGH'
        THEN 'SECURITY'  // Route to BA_POSITION_DATA
      WHEN instruments.instr_class IN ('EQUITY', 'BOND', 'FUND')
        THEN 'SECURITY'  // Route to BA_POSITION_DATA
      ELSE 'CONTRACT'    // Default
    END as target_routing
  }
```

---

## 5. Structured vs. Unstructured Product Logic

### 5.1 Product Classification Rules

**Structured Products:** Contain embedded derivatives or non-linear payoff structure

**Examples:**
- Interest rate swap (embedded in floating-rate loan)
- Convertible bond (embedded equity option)
- Structured note (embedded FX or commodity option)
- Callable bond (embedded issuer call option)

**Unstructured Products:** Vanilla, linear payoff

**Examples:**
- Fixed-rate loan
- Fixed-rate deposit
- Vanilla bond
- Simple equity position

### 5.2 Derivation in Mapping View

```sql
-- Determine if product is structured
SELECT
  contract_id,
  CASE
    WHEN embedded_derivative_flag = 'Y' THEN 'STRUCTURED'
    WHEN cashflow_type = 'NON-LINEAR' THEN 'STRUCTURED'
    WHEN option_feature_count > 0 THEN 'STRUCTURED'
    ELSE 'UNSTRUCTURED'
  END as product_structure_type,
  CASE
    WHEN product_structure_type = 'STRUCTURED' THEN 'LOAN-STRUCT'
    WHEN product_structure_type = 'UNSTRUCTURED' THEN 'LOAN-UNSTR'
  END as fpsl_template_code
FROM /FSDL/MV_BASICDATA
```

---

## 6. Practical DL Workflow Example

### 6.1 End-to-End Scenario

**Scenario:** Bank loads 1000 new loan contracts from FSDM to FPSL (monthly batch)

**Timeline:**
1. **T-0 (Start):` Flag 1000 modified contracts in FSDM change pointer
2. **T+5 min:** FPSL DL process triggers RFM extraction
3. **T+15 min:** RFM returns 1000 contract records + metadata
4. **T+20 min:** Mapping views join with CoA, rates, customer; apply value mappings
5. **T+30 min:** Data staging: 995 contracts pass validation; 5 flagged for data issues
6. **T+40 min:** FPSL API ingests 995 records into BA_BASICDATA
7. **T+50 min:** DL status updated; 5 error records queued for manual review
8. **T+60 min:** Next day, error records corrected in FSDM; DL re-triggered

**Reconciliation Check:**
- Count records in FSDM before DL: 1000
- Count records ingested in FPSL: 995
- Count records in error: 5
- Expected: 1000 = 995 + 5 ✓

---

## 7. Cross-Skill References

- **Config Skill:** Value mapping tables and customization (fpsl-multi-gaap-configuration.md)
- **Quality Skill:** Validation of mapping view outputs, field completeness checks
- **CVPM Skill:** Understanding how mappedinstruments flow to valuation engines
- **Reconciliation Skill:** Reconciling FSDM source counts to FPSL loaded counts

---

**Document Version:** 1.0  
**Last Updated:** 2026-03-22  
**Classification:** Official Mapping Reference

