---
name: "FPSL Data Models and Lifecycle Management"
description: "CDM, PDM, managed tables, bitemporal versioning, and data validation for quality"
source: "Building SAP FPSL_FSDM Golden Source.docx - Section 2"
date: 2026-03-22
applies_to: "quality"
---

# FPSL Data Models and Lifecycle Reference

**Source:** Building SAP FPSL_FSDM Golden Source.docx  
**Extracted:** 2026-03-22  
**Applies To:** quality skill (Data Conformance and Quality Validation)

---

## 1. Physical Data Model (PDM) and Managed Tables

### 1.1 Managed Table Lifecycle

**Unique Feature of FSDM 2023 (ABAP-based):** Bitemporal versioning through managed table statuses

| Table Type | Technical Role | Lifecycle Meaning | Data State | Query Pattern |
|---|---|---|---|---|
| **Draft Tables** | Initial staging | Temporary storage before validation | Unvalidated input | SELECT * FROM DRAFT WHERE valid_state = 'DRAFT' |
| **Active Tables** | Current reality | Single valid version used for reporting | Validated, current | SELECT * FROM ACTIVE WHERE valid_flag = 'X' |
| **History Tables** | Audit trail | Archive of previous versions | Superseded records | SELECT * FROM HISTORY WHERE is_archived = 'X' |

### 1.2 Bitemporal Versioning Mechanics

**Two Time Dimensions:**

1. **Business Time (Valid_From, Valid_To)**
   - When was this record valid in the business domain?
   - Example: Loan interest rate changed on 2024-01-15 → Valid_From = 2024-01-15
   - Supports "as-of" reporting for any historical date
   
2. **System Time (Created_Date, Modified_Date)**
   - When was the record entered/modified in the system?
   - Example: Rate change discovered and corrected on 2024-02-01 → Modified_Date = 2024-02-01
   - Supports audit trail of who changed what and when

### 1.3 Bitemporal Query Examples

**Scenario 1: Current State Report**
```sql
-- What is the current loan balance?
SELECT contract_id, balance
FROM BA_BASICDATA_ACTIVE
WHERE valid_to IS NULL  -- Still valid
  AND system_time = CURRENT_TIMESTAMP;  -- Latest version
```

**Scenario 2: Point-in-Time Report (June 30, 2024)**
```sql
-- What was the loan balance on June 30, 2024?
SELECT contract_id, balance
FROM BA_BASICDATA_HISTORY
WHERE valid_from <= '2024-06-30'
  AND (valid_to > '2024-06-30' OR valid_to IS NULL)
  AND business_time = (SELECT MAX(business_time) 
                       FROM BA_BASICDATA_HISTORY 
                       WHERE valid_from <= '2024-06-30');
```

**Scenario 3: Audit Trail (What changed?)**
```sql
-- Who changed the interest rate and when?
SELECT contract_id, old_rate, new_rate, changed_by, changed_date
FROM BA_BASICDATA_HISTORY
WHERE contract_id = 'C00012345'
  AND field_changed = 'INTEREST_RATE'
ORDER BY changed_date DESC;
```

### 1.4 Data Lifecycle Validations (Quality Checks)

**Conformance Rules:**

| Check | Rule | Severity |
|---|---|---|
| **Draft Completeness** | All mandatory fields populated before activation | ERROR |
| **Draft-to-Active Transition** | Exactly one record transitions from DRAFT to ACTIVE per load | ERROR |
| **Valid_From ≤ Valid_To** | Business time ranges must be valid (or Valid_To IS NULL) | ERROR |
| **Created_Date ≤ Modified_Date** | System time must be chronological | ERROR |
| **No Active Overlap** | No two ACTIVE records with overlapping business time | ERROR |
| **History Archival** | HISTORY records must have Valid_To < CURRENT_DATE | WARNING |
| **Audit Trail Completeness** | Every HISTORY record must cite source transaction | WARNING |

---

##  2. Conceptual Data Model (CDM) vs. Physical Data Model (PDM)

### 2.1 CDM (Business-Oriented View)

**Purpose:** Understood by business experts without technical database knowledge

**Key CDM Entities:**

| Entity | Definition | Business Purpose |
|---|---|---|
| **Business Partner** | Parties in financial transactions (borrower, lender, guarantor, investor) | Customer relationship management, credit authority |
| **Financial Contract** | Specific agreements (loans, deposits, accounts) | Core banking product tracking |
| **Financial Instrument** | Standardized, fungible assets (bonds, equities, funds) | Investment portfolio management |
| **Business Event** | Lifecycle occurrences (signings, disbursements, repayments, prepayments) | Transaction audit trail |

### 2.2 PDM (Technical Implementation in ABAP DDIC)

**Mapping: CDM → PDM**

| CDM Concept | DDIC Object Type | FPSL Table/View |
|---|---|---|
| Business Partner | Database table | BA_PARTNER_MASTER |
| Financial Contract | Database table (managed) | BA_BASICDATA (active), BA_BASICDATA_H (history) |
| Financial Instrument | Database table (managed) | BA_POSITION_DATA (active), BA_POSITION_DATA_H (history) |
| Business Event | Database table | BA_BUSINESS_EVENTS |

### 2.3 CDS (Core Data Services) Implementation

**Role of CDS Views:** Decouple physical storage from logical queries

#### Technical Views (Direct Table Access)

```abap
DEFINE VIEW /FSDL/V_BASICDATA_TECH AS
  SELECT FROM ba_basicdata_active AS active
    INNER JOIN ba_basicdata_history AS history
      ON active.contract_id = history.contract_id
    {
      active.contract_id,
      active.load_number,      -- Technical: LOADNO
      active.pack_number,      -- Technical: PACKNO
      active.record_number,    -- Technical: RECNO
      active.balance,
      history.valid_from,
      history.valid_to
    }
  WHERE active.valid_flag = 'X'
```

**Purpose:**
- Administrative browsing
- Troubleshooting data issues
- Include technical metadata (LOADNO, PACKNO, RECNO)

#### Business Views (Filtered, Business Semantics)

```abap
DEFINE VIEW /FSDL/V_BASICDATA_BIZ AS
  SELECT FROM /FSDL/V_BASICDATA_TECH AS tech
    {
      tech.contract_id,
      tech.balance,
      CASE
        WHEN tech.valid_to IS NULL THEN 'CURRENT'
        WHEN tech.valid_to < :current_date THEN 'EXPIRED'
        WHEN tech.valid_from > :current_date THEN 'FUTURE'
        ELSE 'VALID'
      END as contract_status
    }
  WHERE tech.valid_from <= :as_of_date
    AND (tech.valid_to > :as_of_date OR tech.valid_to IS NULL)
```

**Purpose:**
- Business reports and dashboards
- Fiori apps (Business Data Browser)
- Point-in-time reporting capability
- Hide technical metadata

---

## 3. Data Access Patterns (Technical vs. Business)

### 3.1 Technical View Access Patterns

**Use Case:** Data administrator inspecting raw data

```sql
-- Show all records (including history) with technical metadata
SELECT *
FROM /FSDL/V_BASICDATA_TECH
WHERE load_number = '20240315'
  AND pack_number = '001'
ORDER BY record_number;
```

**Output Includes:**
- LOADNO (Load Number)
- PACKNO (Package Number)
- RECNO (Record Number)
- All historical versions
- Draft, Active, and History states

### 3.2 Business View Access Patterns

**Use Case:** Business report extracting current balances

```sql
-- Show current balances as of quarter-end (2024-Q1)
SELECT contract_id, balance, contract_status
FROM /FSDL/V_BASICDATA_BIZ
WHERE contract_status = 'CURRENT'
  AND as_of_date = '2024-03-31';
```

**Output:**
- Only ACTIVE records valid on Q1 end-date
- Technical metadata hidden
- Contract status derived (CURRENT, EXPIRED, FUTURE)

---

## 4. Quality Validation Checklist

### 4.1 Draft Data Validation (Before Activation)

- [ ] **Mandatory Fields:** All required fields (contract ID, customer ID, principal, rate) populated
- [ ] **Field Format:** Numbers numeric, dates in YYYYMMDD or DATE format, amounts ≥ 0
- [ ] **Reference Integrity:** Customer ID exists in BA_PARTNER_MASTER, GL Account exists in CoA
- [ ] **Business Logic:** Maturity_Date > Start_Date, Interest_Rate in valid range (0-50%)
- [ ] **Uniqueness:** Contract_ID is unique within draft batch (no duplicates)
- [ ] **Completeness:** No NULL values in mandatory fields
- [ ] **Cross-Field Consistency:** Principal = Sum(Tranches) if multi-tranche

### 4.2 Active Data Validation (Post-Ingestion)

- [ ] **State Consistency:** Exactly one ACTIVE record per contract with Valid_To IS NULL
- [ ] **Balance Reconciliation:** ACTIVE balance matches latest transaction posted amount
- [ ] **Temporal Integrity:** Valid_From ≤ Valid_To; Created_Date ≤ Modified_Date
- [ ] **Audit Trail:** Every ACTIVE record has trace to source FSDM load
- [ ] **GL Posting Validation:** Subledger postings match master data (contract amount, rate)

### 4.3 Historical Data Validation (Archive Integrity)

- [ ] **Archive Completeness:** All superseded records moved to HISTORY
- [ ] **Non-Overlapping Versions:** No two HISTORY records with overlapping Valid_From/Valid_To
- [ ] **Change Attribution:** Every HISTORY record cites who changed it and why
- [ ] **Chronological Ordering:** HISTORY records ordered by Valid_From, then Modified_Date
- [ ] **Link to Current:** ACTIVE record linked to latest HISTORY version

---

## 5. Data Conformance Rules (Banking Domain)

### 5.1 Contract-Specific Rules

| Rule | Purpose | Check |
|---|---|---|
| **Contract Balance** | Ensure balance accuracy | Balance ≥ 0; Balance ≤ Original Principal |
| **Accrued Interest** | Ensure interest calculation consistency | Interest_Accrued ≤ (Principal × Rate × Days_Elapsed) |
| **ECL Reserve** | Ensure loan loss provisioning validity | ECL_Reserve ≤ Principal; Stage matches days_past_due |
| **Maturity Validation** | Ensure contract closure readiness | Days_to_Maturity ≥ 0 or = 0 if mature |

### 5.2 Instrument-Specific Rules

| Rule | Purpose | Check |
|---|---|---|
| **Equity Position** | Validate stock holdings | Position > 0; Market_Price > 0; Valuation =Position × Price |
| **Bond Position** | Validate bond holdings | Position > 0; Coupon_Rate ≥ 0; Accrued_Interest calculated |
| **Derivative Position** | Validate derivative exposure | Mark-to-Market value within ±(notional × volatility×sqrt(time)) |
| **Securities Maturity** | Validate fixed-income maturity | Maturity_Date populated (bonds); suppressed for equities/funds |

---

## 6. Cross-Skill References

- **Mapping Skill:** Understanding CDM entities and their mapping to PDM
- **CVPM Skill:** Valuation data conformance (FV, ECL, accrued interest)
- **Reconciliation Skill:** Bitemporal query patterns for audit trail and compliance reporting

---

**Document Version:** 1.0  
**Last Updated:** 2026-03-22  
**Classification:** Official Quality Reference

