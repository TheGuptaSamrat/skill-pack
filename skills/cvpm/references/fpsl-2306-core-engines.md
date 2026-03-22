---
name: "FPSL 2306 Core Engines and Valuation"
description: "Core engines, valuation methods, and accounting logic for CVPM implementations"
source: "Building SAP FPSL_FSDM Golden Source.docx - Section 3.1"
date: 2026-03-22
applies_to: "cvpm"
---

# FPSL 2306 Core Engines Reference for CVPM

**Source:** Building SAP FPSL_FSDM Golden Source.docx  
**Extracted:** 2026-03-22  
**Applies To:** cvpm skill (Core Valuation and Process Modeling)

---

## 1. Integrated Engine Architecture

FPSL 2306 employs four integrated engines for financial data processing in banking:

### 1.1 Accounting Hub
**Function:** Centralizes accounting rule orchestration

- Posting rules management
- Chart of accounts (CoA) configuration
- Multi-GAAP logic deployment
- Standard posting template definitions

**Skillwise Application:**
- Configuration of posting rules per GAAP standard
- Template mapping for recurring transactions
- CoA analysis for reporting structure

### 1.2 Valuation Engine
**Function:** Computes financial metrics per accounting standards

**Key Metrics:**
- **Fair Value (FV):** Market-based valuation, observable inputs
- **Amortized Cost (AC):** Time-value calculation using Effective Interest Rate (EIR)
- **Expected Credit Loss (ECL):** IFRS 9-specific credit risk provisioning

**IFRS 9 Framework:**
- Classification: FVTPL, FVOCI, AC (Financial Instruments classification)
- Measurement: Applies appropriate valuation model per classification
- ECL Staging: Stage 1 (12-month PD), Stage 2 (lifetime PD, increased risk), Stage 3 (default)

**Amortized Cost Calculation Method:**
```
AC(t) = Original Cost - Principal Paid + Interest Accrued - Cumulative Impairment
         where Interest Accrued uses EIR discount curve
```

**Effective Interest Rate (EIR) Methodology:**
- TIR (Time-Weighted Internal Rate of Return)
- Incorporates all contractual future cashflows
- Fixed for instrument lifetime (except stage 3 transitions)
- Basis for interest income recognition

**CVPM Integration:**
- Valuation method selection per product template
- EIR curve calibration and maintenance
- ECL model parameter adjustment
- Valuation trigger rules (origin of contract, covenant breach, etc.)

### 1.3 Cashflow Engine (CFE)
**Function:** Stores and processes actual and expected cashflows

**Components:**
- **Actual Cashflows:** Historical/current disbursements and repayments
- **Expected Cashflows:** Forward-looking payment schedules
- **Scenario Cashflows:** Stress-test and what-if scenarios

**Uses:**
- Foundation for time-value-of-money calculations (discounting)
- NPV computation for valuation
- Liquidity and interest rate risk analysis
- Hedge accounting effectiveness testing

**Granularity:**
- Contract-level detail (not aggregated)
- Time-bucketed periods (daily, monthly, quarterly, annual)
- Currency-specific (multi-currency workflows)

**CVPM Implications:**
- Cashflow schedule attachment to contract
- Embedded option modeling (prepayment, conversion, callable bonds)
- Scenario branching for probabilistic outcomes (ECL)
- Scenario weighting for expected value calculations

### 1.4 Posting Engine
**Function:** Generates subledger journal entries

**Methodology:** Event-Based Accounting (EBA)

**Trigger Types:**
1. **Business Event Triggers:** Contract origination, disbursement, repayment, event-based covenant breach
2. **Period-End Requirements:** Accrual generation, valuation changes, reserves/provisions
3. **Lifecycle Transitions:** Stage changes, reclassifications, prepayments, defaults

**Posting Generation:**
```
Business Event / Period Requirement
         ↓
   EBA Rule Matching
         ↓
Document Derivation (GL Account, Amount, GAAP)
         ↓
Subledger Entry Generation
         ↓
GL Aggregation & Transfer to ACDOCA
```

**GAAP-Specific Rules:**
- IFRS 9: FV changes OCI vs. P&L per classification
- US GAAP: ASC 326 ECL with alternative frameworks
- Local GAAP: Statutory adjustments and regulatory reserves

**CVPM Process Design:**
- Define posting rules per accounting standard
- Map business events to posting triggers
- Validate posting derivation logic for all scenarios
- Review multi-GAAP posting consistency

---

## 2. Multi-GAAP Posting Strategy

### 2.1 "Central and Delta GAAP" Approach

**Principle:** Post common entries once; GAAP-specific entries separately.

**Architecture:**
```
┌─────────────────────────────────────┐
│   Core/Central Entries              │
│   (Common to all GAAP standards)    │
│   - Interest income                 │
│   - Principal collections           │
│   - Fees and commissions            │
└────────────┬────────────────────────┘
             │
        ┌────┴────┬──────────┬──────────┐
        │          │          │          │
        ↓          ↓          ↓          ↓
   IFRS 9 Δ   US GAAP Δ  Local GAAP Δ  FX Δ
   - FV chg   - ASC 326  - Stat Adj.   - Revaluation
   - ECL     - Specific - Reserves    - Gains/Losses
   - OCI Rsrv  Templates - Tax Impact
```

### 2.2 Multi-GAAP Support Matrix

| Accounting Standard | Key Requirements | FPSL 2306 Support | CVPM Design Impact |
|-----------|---|---|---|
| **IFRS 9: Financial Instruments** | Amortized Cost, Fair Value (P&L/OCI), ECL | ✅ Comprehensive templates | Valuation engine selection, ECL model parameters, classification logic, OCI reserve management |
| **US GAAP: ASC 326 CECL** | Recognition/Measurement per classification | ✅ Specialized templates | Alt. ECL models, vintage aging, probability weighting |
| **Local GAAP** | Statutory reporting, regulatory reserves | ✅ Delta posting approach | Local adjustments, regulatory capital impact, tax implications |

### 2.3 GAAP-Specific Calculation Examples

#### IFRS 9 ECL (3-Stage Model)
```
Stage 1 (12M ECL): PD(12M) × LGD × EAD
Stage 2 (Lifetime ECL): PD(Lifetime) × LGD × EAD, if SICR
Stage 3 (Default): Loss already incurred, specific reserves
```

#### US GAAP CECL (Single-Stage Expected Loss)
```
CECL Reserve = Lifetime PD × LGD × EAD
(No staging; forward-looking historical vintage data)
```

---

## 3. Event-Based Accounting (EBA) Rules

### 3.1 Rule Structure

**Template:**
```
WHEN [Business Event / Period Trigger]
AND [Condition 1: Account Classification]
AND [Condition 2: GAAP Standard]
AND [Condition 3: Business Rules]
THEN [Post Journal Entry]
     - GL Account: [CoA Code]
     - Amount: [Calculation Formula]
     - GAAP Tag: [Standard]
```

### 3.2 Common Business Events

| Event | Trigger | Posting Logic | GAAP Handling |
|-------|---------|---|---|
| **Contract Origination** | Deal approval → active status | Debit Loan, Credit Cash | Single entry; derivative rules apply |
| **Disbursement** | Fund transfer | Asset increase | Single entry; timing per GAAP |
| **Interest Accrual (Period-End)** | Daily calculation or period-end | Debit Receivable, Credit Interest Income | EIR-based; FV changes separately |
| **ECL Reserve Adjustment** | Model recalculation or stage change | Debit Expense, Credit Reserve (contra-asset) | IFRS 9 vs. US GAAP differences |
| **Fair Value Revaluation** | Period-end for FV portfolio | Debit/Credit Asset, Credit/Debit OCI or P&L | Per classification (FVTPL via P&L; FVOCI via OCI) |
| **Prepayment** | Early repayment transaction | Debit Cash (gain/loss), Credit Loan | Potential acceleration of unamortized fees/costs |
| **Stage Transition** | Covenant breach or SICR event | Reclassify ECL, adjust interest calc | Impact on postings (rate, reserve) |
| **Default** | Arrears threshold / legal event | Move to Stage 3, specific provision | May trigger restructuring or charge-off logic |

---

## 4. Reconciliation within CVPM

### 4.1 Sub-Systems Integration

**Reconciliation Points:**
1. **Valuation Engine ↔ Posting Engine:** Ensure FV changes drive EBA posting
2. **Cashflow Engine ↔ Valuation Engine:** ECL scenario weights based on CF paths
3. **Posting Engine ↔ GL:** Subledger aggregation to GL without loss
4. **Multi-GAAP Posting Consistency:** Central entries same across GAAP; deltas isolated

### 4.2 Audit Trail for CVPM

**Required Logging:**
- Valuation method applied (FV, AC, ECL model)
- Key assumptions (EIR, PD curve, LGD)
- Posting derivation trace (rule matched, GL account, amount)
- GAAP-specific adjustments applied
- Timestamp and user responsible

---

## 5. Practical CVPM Workflow

### 5.1 Process Steps

1. **Setup Phase:**
   - Define product templates (contract structure, classification rules)
   - Configure valuation methods (FV vs. AC vs. ECL model selection)
   - Set up EBA posting rules per GAAP standard

2. **Origination & Capture:**
   - Contract terms entered into FSDM
   - Replicated to FPSL via data loading (DL) process
   - Initial classification and valuation assigned

3. **Regular Processing:**
   - Interest accrual calculation (daily or period-end)
   - Cashflow processing (payments, prepayments)
   - ECL recalculation (monthly or quarterly)
   - Posting generation via EBA rules

4. **Period-End Procedures:**
   - Valuation updates (FV market repricing, ECL model runs)
   - Multi-GAAP reserve reconciliation
   - Posting validation and GL transfer
   - Audit trail review

### 5.2 Key Decision Points

| Decision | Impact | Configuration |
|----------|--------|---|
| **Classification (AC vs. FV)** | Valuation method, posting destination (P&L vs. OCI) | Product template → FSDM classification rule |
| **ECL Model (IFRS 9 vs. US GAAP)** | Reserve calculation, staging logic | Master data → FPSL allocation |
| **EIR Curve Maintenance** | Interest income recognition; AC amortization | Standing data → quarterly updates |
| **FV Pricing Source** | Fair value inputs; observable vs. unobservable | Market data feed → ECL curve calibration |
| **Derivative Accounting** | Embedded option treatment; hedge effectiveness | Product template → special rules |

---

## 6. Cross-Skill References

- **Config Skill:** Multi-GAAP template setup, CoA configuration, EBA rule customization
- **Quality Skill:** Valuation data completeness, FV input validation, ECL model parameter QA
- **Mapping Skill:** FSDM-to-FPSL field mapping for classification, valuation attributes
- **Reconciliation Skill:** Multi-GAAP posting reconciliation, GL aggregation, FV reserve verification

---

**Document Version:** 1.0  
**Last Updated:** 2026-03-22  
**Classification:** Official Reference Material

