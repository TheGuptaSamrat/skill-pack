---
name: "FPSL Multi-GAAP Configuration Guidance"
description: "Multi-GAAP setup, value mapping tables, and customization for config skill"
source: "Building SAP FPSL_FSDM Golden Source.docx - Sections 3.2, 4.4"
date: 2026-03-22
applies_to: "config"
---

# FPSL Multi-GAAP Configuration Reference

**Source:** Building SAP FPSL_FSDM Golden Source.docx  
**Extracted:** 2026-03-22  
**Applies To:** config skill (Configuration and Setup)

---

## 1. Multi-GAAP Setup Strategy

### 1.1 "Central and Delta GAAP" Approach

**Configuration Principle:** Post core entries once; GAAP-specific adjustments separately.

**Setup Workflow:**
```
Define Core Chart of Accounts
         ↓
Configure Central (Common) Posting Rules
         ↓
For Each GAAP Standard:
  - Configure GAAP-specific posting rules
  - Set up differential accounts (GAAP-specific GL lines)
  - Configure reserve/provisioning logic
         ↓
Validate Multi-GAAP Mapping
         ↓
Test Reconciliation (Central Entries match across GAAP)
```

### 1.2 Chart of Accounts (CoA) Design

**Layers:**
- **Core CoA:** Common GL accounts (interest income, principal, fees, etc.)
- **GAAP-Specific CoA:** Additional accounts for IFRS 9 OCI reserves, US GAAP-specific provisions, local regulatory adjustments
- **Analytical CoA:** Optional cost centers or profit centers for managerial reporting

**Configuration Tool:** T-code OB51 (Define Posts Keys / CoA Structure)

### 1.3 GAAP Posting Rule Configuration

#### IFRS 9 Setup
**Key Configuration Objects:**

| Config Object | Purpose | Setup Details |
|---|---|---|
| **Ledger Group** | Multi-GAAP container | Create separate ledger (e.g., IFRS-9-LEDGER) |
| **Accounting Method** | Valuation approach | Select AC (Amortized Cost) or FV (Fair Value) per classification |
| **Posting Rules** | EBA rule configuration | Interest accrual, FV changes (P&L vs. OCI), ECL reserves |
| **OCI Reserve Accounts** | Fair Value changes | Map to specific GL accounts per classification (FVOCI instruments) |

**IFRS 9 Posting Derivation Rules:**
- **Interest Income:** EIR-based accrual per contract
- **FV Change - FVTPL:** P&L posting (debit/credit Asset, P&L Account)
- **FV Change - FVOCI:** OCI posting (debit/credit Asset, OCI Reserve)
- **ECL Reserve:** Stage-based ECL calculation (Stage 1 → Stage 2 → Stage 3)
- **Reclassification:** When business model or SICR triggered

#### US GAAP Setup (ASC 326 CECL)
**Key Configuration Objects:**

| Config Object | Purpose | Setup Details |
|---|---|---|
| **Ledger Group** | Multi-GAAP container | Create separate ledger (e.g., US-GAAP-LEDGER) |
| **ECL Model** | Allowance calculation | CECL (Collective/Collective Life), not 3-stage |
| **Vintage Data** | Historical loss rates | Configure aging buckets (historical cohorts) |
| **Posting Rules** | EBA rules for US GAAP | Allowance reserve posting, write-offs |

**US GAAP Posting Derivation Rules:**
- **Interest Income:** Same as IFRS 9 (EIR-based)
- **Allowance Reserve:** CECL reserve posting (single-stage, no SICR logic)
- **Charge-offs:** Policy-driven (e.g., 180 days past due)

#### Local GAAP Setup (Statutory Reporting)
**Key Configuration Objects:**

| Config Object | Purpose | Setup Details |
|---|---|---|
| **Ledger Group** | Multi-GAAP container | Create separate ledger per country necessity |
| **Posting Rules** | Delta-based adjustments | Differences from central GAAP |
| **Reserve Accounts** | Regulatory requirements | Tax-driven, compliance-driven reserves |

**Local GAAP Posting Derivation Rules:**
- **Delta Postings:** Only IFRS-to-Local differences
- **Regulatory Reserves:** Country-specific loan loss provisioning rules
- **Tax Impact:** Deferred tax accounts if applicable

---

## 2. Value Mapping and Customization Tables

### 2.1 Value Mapping Architecture

**Purpose:** Transform FSDM attribute codes to FPSL target codes

**Tool:** Custom Business Configurations (CBC) Fiori App

**Configuration Flow:**
```
FSDM Source Codes (Accrual Type, Transaction Type, Instrument Class, PCI)
         ↓
     Mapping Rules (IF-THEN logic in CBC)
         ↓
FPSL Target Codes (BA1/C55ACCAT, BA1/C55TTYPE, BA1C_FITYPE, BA1C/HDRTEMPL)
```

### 2.2 Mapping Table Specifications

#### /FSDL/MAP_ACLTYP - Accrual Type Mapping

**Input Fields (FSDM):**
- Accrual Type (e.g., REGULAR, DEFERRED, STRUCTURED)
- Interest Type (e.g., FIXED, FLOATING, VARIABLE)

**Output Field (FPSL):**
- BA1/C55ACCAT (Accrual Category) - e.g., AC-STD, AC-DEF, AC-SUB

**Derivation Logic:**
```
IF Accrual Type = "REGULAR" AND Interest Type = "FIXED"
   THEN BA1/C55ACCAT = "AC-STD"

IF Accrual Type = "STRUCTURED" AND embedded option detected
   THEN BA1/C55ACCAT = "AC-SUB"  // Requires component breakdown
```

**Configuration Example:**
| ACCRUAL_TYPE | INTEREST_TYPE | BA1/C55ACCAT | Notes |
|---|---|---|---|
| REGULAR | FIXED | AC-STD | Standard fixed-rate products |
| REGULAR | FLOATING | AC-FLT | Index-linked products |
| STRUCTURED | FIXED | AC-SUB | Component-level detail required |
| DEFERRED | FIXED | AC-DEF | Non-accruing, deferred recognition |

#### /FSDL/MAP_TTYPE - Transaction Type Mapping

**Input Fields (FSDM):**
- Transaction Type (DISBURSEMENT, REPAYMENT, FEE, WRITEOFF, etc.)
- Product Catalog Item (PCI) - optional, for refinement

**Output Field (FPSL):**
- BA1/C55TTYPE (Business Transaction Type) - e.g., DISB, PMNT, FEE, WROF

**Derivation Logic:**
```
IF Transaction Type = "DISBURSEMENT"
   THEN BA1/C55TTYPE = "DISB"  // Initial funding

IF Transaction Type = "REPAYMENT"
   THEN BA1/C55TTYPE = "PMNT"  // Principal/interest collection

IF Transaction Type = "WRITEOFF"
   THEN BA1/C55TTYPE = "WROF"  // Charge-off recognition
```

#### /FSDL/MAP_SECTYP - Security Type Mapping

**Input Field (FSDM):**
- Instrument Class (EQUITY, BOND, DERIVATIVE, FUND, etc.)

**Output Field (FPSL):**
- BA1C_FITYPE (Financial Instrument Type) - e.g., EQ, BD, DRV, FND

**Derivation Logic:**
```
IF Instrument Class = "EQUITY"
   THEN BA1C_FITYPE = "EQ"  // Stock, share

IF Instrument Class = "BOND"
   THEN BA1C_FITYPE = "BD"  // Fixed income, subordinated debt

IF Instrument Class = "DERIVATIVE"
   THEN BA1C_FITYPE = "DRV"  // Option, swap, forward
```

#### /FSDL/MAP_PCI - Product Catalog Item & Template Derivation

**Input Field (FSDM):**
- Product Catalog Item (PCI) - e.g., PCI_TERM_LOAN, PCI_FIXED_DEP, etc.

**Output Field (FPSL):**
- BA1C/HDRTEMPL (FPSL Header Template) - e.g., LOAN-STD, LOAN-STRUCT, DEP-TERM

**Derivation Logic (Structured vs. Unstructured):**
```
IF PCI = "PCI_TERM_LOAN" AND no embedded derivatives
   THEN BA1C/HDRTEMPL = "LOAN-STD"  // Unstructured

IF PCI = "PCI_TERM_LOAN" AND embedded interest rate cap
   THEN BA1C/HDRTEMPL = "LOAN-STRUCT"  // Structured; needs component breakdown

IF PCI = "PCI_FIXED_DEP"
   THEN BA1C/HDRTEMPL = "DEP-TERM"  // Fixed maturity deposit
```

### 2.3 Custom Business Configurations (CBC) Setup

**Navigation:** Fiori App "Custom Business Configurations"

**Configuration Steps:**
1. Navigate to "Configurations" → "FSDM Integration"
2. Select the mapping table (/FSDL/MAP_*)
3. Create a new configuration object (e.g., "Standard Accrual Mapping")
4. Define IF-THEN rules for each mapping scenario
5. Assign to a business configuration scope (e.g., PROD-BANK, TEST-BANK)
6. Test with sample FSDM data
7. Promote to productive scope

**Mapping Table Maintenance Example:**

| Table | IF Conditions | THEN Output | Active |
|---|---|---|---|
| /FSDL/MAP_ACLTYP | ACCRUAL_TYPE=REGULAR, INTEREST_TYPE=FIXED | BA1/C55ACCAT=AC-STD | ✓ |
| /FSDL/MAP_ACLTYP | ACCRUAL_TYPE=STRUCTURED, EMB_DERIVATIVE=TRUE | BA1/C55ACCAT=AC-SUB | ✓ |
| /FSDL/MAP_TTYPE | TRANSACTION_TYPE=DISBURSEMENT | BA1/C55TTYPE=DISB | ✓ |
| /FSDL/MAP_PCI | PCI=PCI_TERM_LOAN, STRUCT_FLAG=FALSE | BA1C/HDRTEMPL=LOAN-STD | ✓ |

---

## 3. Critical Configuration Nuances (2023)

### 3.1 LOT_ID Field Length Mismatch

**Issue:** FSDM LOT_ID = 128 characters; FPSL = 15 characters

**Configuration Mitigation:**
1. **Source Validation Rule:** Validate LOT_ID length ≤ 15 in FSDM staging
2. **Mapping View Logic:** Truncate or hash LOT_ID in /FSDL/MV_* views
3. **Error Handling:** Reject records with LOT_ID > 15; report in DL error log

**CBC Configuration:**
```
IF LENGTH(LOT_ID) > 15
   THEN REJECT and LOG error: "LOT_ID exceeds FPSL field length (15 chars)"
   ELSE PASS through mapping views
```

### 3.2 Contract vs. Security Classification Rule

**Configuration Goal:** Route FSDM records to correct FPSL table (contracts vs. securities)

**Decision Rule in Customization:**
```
IF Financial_Contract_Type = "LOAN" OR "DEPOSIT" OR "ACCOUNT"
   AND NOT exists Embedded_Derivative_Flag
   THEN Route to BA_TRANSACTIONDATA (Contract table)

IF Financial_Instrument_Type = "EQUITY" OR "BOND" OR "DERIVATIVE"
   OR (Financial_Contract_Type = "LOAN" AND Embedded_Derivative_Flag = TRUE)
   THEN Route to BA_POSITION_DATA (Security/Instrument table)
```

**CBC Configuration Object Name:** CONTRACT_VS_SECURITY_CLASSIFIER

---

## 4. Configuration Checklist

### Pre-Go-Live Configuration Validation

- [ ] **CoA Structure:** Core + GAAP-specific accounts defined and linked
- [ ] **Ledger Setup:** Separate ledger created for each GAAP standard (IFRS-LEDGER, US-GAAP-LEDGER, LOCAL-LEDGER)
- [ ] **Posting Rules:** EBA rules configured for all business events  (disbursement, accrual, FV change, ECL adjustment, writeoff)
- [ ] **Mapping Tables:** All 4 mapping tables (/FSDL/MAP_*) populated with representative scenarios
- [ ] **GAAP Validation:** Multi-GAAP reconciliation tested (central entries identical across GAAP)
- [ ] **Value Mapping Testing:** Sample FSDM data transformed correctly to FPSL via CBC
- [ ] **LOT_ID Validation:** Error handling for LOT_ID > 15 characters configured
- [ ] **Contract vs. Security Routing:** Classification logic tested with mixed portfolio
- [ ] **DL Process:** Data loading workflow tested end-to-end (extraction, transformation, load)

---

## 5. Cross-Skill References

- **CVPM Skill:** Multi-GAAP posting strategy (Section 2 in fpsl-2306-core-engines.md)
- **Mapping Skill:** Value mapping tables and FSDM-to-FPSL field transformation
- **Quality Skill:** Validation of mapping table completeness and contract vs. security classification accuracy
- **Reconciliation Skill:** Multi-GAAP posting reconciliation (central vs. GAAP-specific amounts)

---

**Document Version:** 1.0  
**Last Updated:** 2026-03-22  
**Classification:** Official Configuration Reference

