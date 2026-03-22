---
name: "FPSL/FSDM 2023 Golden Source Reference"
description: "Comprehensive technical specification for SAP FPSL 2306 and FSDM 2023 banking architecture"
source: "Building SAP FPSL_FSDM Golden Source.docx"
date: 2026-03-22
trust_level: "official-product"
---

# SAP FPSL/FSDM 2023 Golden Source Reference

**Source:** Building SAP FPSL_FSDM Golden Source.docx  
**Version:** FPSL 2306, FSDM 2023  
**Date Extracted:** 2026-03-22  
**Trust Level:** Official Product Documentation

---

## Executive Overview

This document serves as the authoritative technical repository for the implementation and operation of SAP Financial Services Data Management (FSDM) 2023 and SAP Financial Products Subledger (FPSL) 2306 within the SAP S/4HANA 2023 ecosystem. It covers:

- **Architecture & Platform:** ABAP Platform 2023 (SAP_BASIS 758), RAP model, integration with S/4HANA
- **Data Models:** Conceptual (CDM), Physical (PDM), managed tables with draft/active/history lifecycle
- **Core Engines:** Accounting Hub, Valuation Engine, Cashflow Engine, Posting Engine
- **Integration:** FSDM-to-FPSL data loading (DL) process, mapping views, value mapping
- **Accounting Standards:** Multi-GAAP support (IFRS 9, US GAAP, Local GAAP)
- **Banking Domain:** Financial contracts vs. instruments, structured vs. unstructured delivery

---

## Part 1: Architectural Foundation

### 1.1 Paradigm Shift to ABAP

**Key Change:** FSDM 2023 is now fully ABAP-based, not HANA-native.

- Previous versions: SAP HANA-native structures
- Current version: Integrated into ABAP Platform 2023, aligning with SAP S/4HANA 2023
- Benefit: "Clean core" approach using RESTful ABAP Programming (RAP)

### 1.2 Technology Stack

| Component | Specification | Role in Banking |
|-----------|---------------|-----------------|
| **Core Platform** | ABAP Platform 2023 (SAP_BASIS 758) | Foundational tech for S/4HANA 2023 |
| **Database Layer** | SAP HANA (In-Memory) | Storage and high-speed processing of contracts |
| **Development Model** | ABAP Cloud / RAP | Standardized framework for OData, Fiori apps |
| **Integration Framework** | OData REST APIs (CRUD) | Connectivity for third-party tools |
| **Add-ons** | S4FPSL 300 / S4FSFND 200 | Core FPSL backend components |

### 1.3 Three-Tier Client-Server Architecture

```
┌─────────────────────────────────────┐
│   Presentation Layer (SAP Fiori)    │
│   - UI for user interactivity       │
└──────────────┬──────────────────────┘
               │
┌──────────────┴──────────────────────┐
│   Application Layer (ABAP)          │
│   - Banking logic, RAP model        │
│   - Business Objects, Events        │
└──────────────┬──────────────────────┘
               │
┌──────────────┴──────────────────────┐
│   Database Layer (SAP HANA)         │
│   - In-memory analytics             │
│   - Contract-level granularity      │
└─────────────────────────────────────┘
```

### 1.4 ABAP RESTful Application Programming (RAP)

**Purpose:** Standardized framework for building banking business objects

**2023 Enhancements:**
- Side effects modeling in behavior definitions
- Real-time UI updates in Fiori based on user input (essential for manual adjustments)
- Banking business event consumption (local or remote via SAP Event Mesh on BTP)

**Implications for Skills:**
- AMDP/ABAP: Implement business objects using RAP semantics
- Config: Configuration of side effects and event routing
- CVPM: Accounting logic enclosed in business object behavior

---

## Part 2: Data Architecture

### 2.1 Conceptual Data Model (CDM) for Banking

**Purpose:** Business-oriented view of banking entities (understandable by business experts)

**Key Banking Domains:**

| Entity | Definition | Examples |
|--------|-----------|----------|
| **Business Partner** | All parties in financial transactions | Borrower, Lender, Guarantor |
| **Financial Contract** | Specific agreements between bank and customer | Loans, Deposits, Accounts |
| **Financial Instrument** | Standardized, fungible assets | Bonds, Equities, Investment funds |
| **Business Event** | Lifecycle occurrences | Signings, Disbursements, Repayments |

**Tool:** FSDM Workbench (Microsoft Visual Studio Code extension)
- Graphical modeling
- FSDMDDL (domain-specific data definition language)

### 2.2 Physical Data Model (PDM) and Managed Tables

**Implementation:** ABAP Data Dictionary (DDIC) objects

**Unique Feature:** Bitemporal Lifecycle Management

| Table Type | Technical Role | Lifecycle | Use Case |
|------------|---|---|---|
| **Draft Tables** | Initial Ingestion | Temporary storage before validation | Data staging |
| **Active Tables** | Current Reality | Valid version for reporting | Operational reporting |
| **History Tables** | Audit Trail | Archive previous versions | Compliance & audits |

**Bitemporal Versioning:**
- **Business Time:** When a transaction was valid
- **System Time:** When the record was entered/modified
- **Compliance Benefit:** Full auditability for regulatory requirements

### 2.3 Data Access: Technical vs. Business Views

**Technical Views (CDS):**
- Read from draft, active, or history tables
- Include technical metadata: LOADNO, PACKNO, RECNO
- Purpose: Administrative tasks, technical browsing

**Business Views (CDS):**
- Apply prepared filters to technical data
- System and business validity filters
- Used by apps like Business Data Browser
- Point-in-time reporting capability

**Implications for Skills:**
- Quality: Validate draft/active/history lifecycle
- Reconciliation: Leverage business views for multi-period reporting
- Mapping: Understand CDS view structure for data transformation

---

## Part 3: FPSL 2306 Core Engines

### 3.1 Integrated Engine Architecture

FPSL processes financial data through four integrated engines:

#### 3.1.1 Accounting Hub
- Centralizes posting rules management
- Chart of accounts configuration
- Multi-GAAP logic orchestration

#### 3.1.2 Valuation Engine
- **Fair Value (FV):** Market-based valuation
- **Amortized Cost (AC):** Time-value calculation using Effective Interest Rate (EIR)
- **Expected Credit Loss (ECL):** IFRS 9 compliance calculations

#### 3.1.3 Cashflow Engine (CFE)
- Stores actual and expected cashflows
- Foundation for time-value-of-money calculations
- Critical for discounting and NPV computations

#### 3.1.4 Posting Engine
- **Trigger:** Event-Based Accounting (EBA)
- **Scope:** Subledger journal entries
- **Execution:** Business events or period-end rules

### 3.2 Multi-GAAP and Multi-Currency Strategy

**Model:** "Central and Delta GAAP" Approach

```
Common Cross-GAAP Entries
         ↓
    [Posted Once]
         ↓
┌────────┴────────┬────────────┬─────────────┐
│                 │            │             │
↓                 ↓            ↓             ↓
IFRS 9       US GAAP      Local GAAP    Multi-Currency
Entries      Adjustments  Deltas        Conversions
```

**Benefits:**
- Reduced redundancy
- Simplified reconciliation
- Single source of truth for core postings

| Standard | Calculation | Templates | FPSL Support |
|----------|-------------|-----------|---|
| **IFRS 9** | Amortized Cost, Fair Value (P&L/OCI), ECL | Comprehensive | ✅ Full |
| **US GAAP** | Recognition/Measurement rules | US-specific | ✅ Specialized |
| **Local GAAP** | Statutory adjustments | Delta postings | ✅ Delta approach |

---

## Part 4: FSDM-to-FPSL Integration

### 4.1 Integration Philosophy

- **FSDM Role:** Provisioning layer (harmonized data hub)
- **FPSL Role:** Consumer layer (accounting and valuation processor)
- **Connection:** Data Loading (DL) process

### 4.2 Data Loading (DL) Process Workflow

**Standardized sequence for data replication:**

```
1. Change Pointer Generation
   └─→ Identify new/modified objects in FSDM since last load

2. Data Extraction
   └─→ Trigger extraction from FSDM via RFMs (/FSDL/EXTRACT function group)

3. Transformation & Mapping
   └─→ FSDM consumption layer uses mapping views
   └─→ Transform into target FPSL structure

4. Data Ingestion
   └─→ Load mapped data into FPSL tables
   └─→ Ready for accounting/valuation processes
```

### 4.3 Standard Mapping Views (/FSDL/MV_*)

**Performance-Enhanced Mapping (2023 FP03, FP05):**

| View | Purpose | Recent Enhancement |
|------|---------|------------------|
| **/FSDL/MV_BUSINESSTRANSACTIONS** | Maps bank settlements to FPSL transactions | Mirror contract IDs (BA1_C55R5CNID for contracts, BA1_C55R6CNID for securities) |
| **/FSDL/MV_BASICDATA** | Provision master data for contracts | /FSDL/CV_FINANCIALCONTRACT_UN offloads complex joins |
| **/FSDL/MV_SECURITIESBASICDATA** | Master data for instruments | Correctly suppresses contract dates for equities/funds |
| **/FSDL/MV_INTERESTACCRUALS_COND** | Aggregates accrual types | NEW: Prevents key-conflict errors during processing |

### 4.4 Value Mapping and Customization Tables

**Tool:** Custom Business Configurations Fiori app

| Mapping Table | Input (FSDM) | Output (FPSL) | Purpose |
|---------------|---|---|---|
| **/FSDL/MAP_ACLTYP** | Accrual Type, Interest Type | BA1/C55ACCAT | Accrual category derivation |
| **/FSDL/MAP_TTYPE** | Transaction Type, PCI | BA1/C55TTYPE | Business transaction classification |
| **/FSDL/MAP_SECTYP** | Instrument Class | BA1C_FITYPE | Security type mapping |
| **/FSDL/MAP_PCI** | Product Catalog Item | BA1C/HDRTEMPL | Template derivation (Structured vs Unstructured) |

**Critical Nuance (2023):** LOT_ID Field Length Mismatch
- FSDM: 128 characters
- FPSL: 15 characters
- **Requirement:** Strict source validation to prevent truncation errors

### 4.5 Universal Journal Integration

**Flow:**
```
FPSL Subledger (Millions of contracts)
         ↓
   [Aggregation]
         ↓
GL Documents (Summarized)
         ↓
Universal Journal (ACDOCA)
         ↓
General Ledger Reporting (Performant)
```

**Benefit:** Maintains contract granularity in subledger while keeping GL reports fast

---

## Part 5: Banking Domain Entities

### 5.1 Financial Contracts vs. Financial Instruments

**Distinction:** Determines target table in FPSL and valuation logic

#### Contracts
- Specific agreements between bank and customer
- Examples: Loans, current accounts, fixed-term deposits
- Delivery: Often "unstructured" unless complex (embedded derivatives)
- FPSL Table: BA_TRANSACTIONDATA or similar

#### Instruments (Securities)
- Fungible, standardized assets
- Examples: Bonds, equities, derivatives
- FSDM Mapping: /FSDL/MV_SECURITIESBASICDATA
- FPSL Table: Position management (securities-specific)

### 5.2 Structured vs. Unstructured Delivery

**Structured Products:**
- Interest rate swaps
- Structured notes with embedded options
- Delivery: Component-level detail
- FPSL: Full derivative valuation

**Unstructured Products:**
- Simple loans
- Vanilla deposits
- Delivery: Aggregate level
- FPSL: Standard valuation templates

---

## Part 6: Practical Implications for Skill Development

### 6.1 Configuration (Config Skill)

**Relevant Sections:**
- Multi-GAAP setup (IFRS 9, US GAAP, Local GAAP)
- Value mapping tables (/FSDL/MAP_*)
- Customization via Fiori apps
- Chart of accounts and posting rule templates

**Actions:**
- Document multi-GAAP workflow in SKILL.md Load Order (Step 3-4)
- Reference value mapping tables in config guidance
- Include template derivation logic (structured vs. unstructured)

### 6.2 CVPM (Core Valuation & Process Modeling)

**Relevant Sections:**
- Core Engines (Valuation, Cashflow, Posting, Accounting Hub)
- Effective Interest Rate (EIR) calculations
- Expected Credit Loss (ECL) - IFRS 9
- Event-Based Accounting (EBA) logic
- Multi-GAAP posting strategy

**Actions:**
- Add "Core Engines" section to CVPM SKILL.md
- Include EIR/ECL calculation workflows
- Document EBA posting derivation
- Reference Valuation Engine methodology

### 6.3 AMDP & ABAP (Development Skills)

**Relevant Sections:**
- RAP model and business objects
- Side effects in behavior definitions
- Banking business events
- Remote function modules (/FSDL/EXTRACT)
- Event-based triggers

**Actions:**
- Add RAP banking business object patterns to AMDP SKILL.md
- Include side effects example for manual adjustments
- Document RFM extraction pattern
- Add event consumption (local vs. BTP Event Mesh)

### 6.4 Mapping (Data Integration)

**Relevant Sections:**
- FSDM-to-FPSL mapping views (/FSDL/MV_*)
- Value mapping tables
- Field transformations (LOT_ID, contract/security IDs, accrual types)
- Contract vs. instrument routing
- Structured vs. unstructured logic

**Actions:**
- Create section on "Financial Data Mapping" in mapping SKILL.md
- Include decision tree: Contract vs. Instrument
- Document field-level transformations with examples
- Reference value mapping table structure

### 6.5 Quality (Data Conformance)

**Relevant Sections:**
- Draft/Active/History table lifecycle
- Bitemporal versioning (Business Time vs. System Time)
- Data models (CDM, PDM)
- Technical vs. Business CDS views
- Audit trail requirements

**Actions:**
- Add section on "Bitemporal Data Lifecycle" to quality SKILL.md
- Document conformance checks for draft → active → history
- Include CDS view validation patterns
- Reference audit trail completeness requirements

### 6.6 Reconciliation (Business Verification)

**Relevant Sections:**
- Multi-GAAP reconciliation
- GL aggregation from subledger
- Contract-level drill-down capability
- Universal Journal (ACDOCA) posting verification
- Historical reporting (point-in-time)

**Actions:**
- Add "Multi-GAAP Reconciliation" section to reconciliation SKILL.md
- Document GL ↔ subledger reconciliation workflow
- Include ACDOCA posting verification logic
- Add point-in-time query patterns for audit

---

## Integration Timeline

**Phase 1 (Immediate):** Create this reference document ✅  
**Phase 2:** Extract skill-specific sections and update SKILL.md files  
**Phase 3:** Update official-sources-router.md with new reference  
**Phase 4:** Validate all cross-references and commit  

---

## Skillwise Reference Index

### Config Skill
- Section 3.2: Multi-GAAP Strategy
- Section 4.4: Value Mapping & Customization

### CVPM Skill
- Section 3.1: Integrated Engine Architecture
- Section 3.2: Multi-GAAP and Multi-Currency

### Mapping Skill
- Section 4.2: Data Loading Workflow
- Section 4.3: Standard Mapping Views
- Section 4.4: Value Mapping Tables
- Section 5: Banking Domain Entities

### Quality Skill
- Section 2.2: Physical Data Model & Managed Tables
- Section 2.3: Data Access Views

### Reconciliation Skill
- Section 3.2: Multi-GAAP Strategy
- Section 4.5: Universal Journal Integration

### AMDP/ABAP Skills
- Section 1.4: RAP Model
- Section 4.2: RFM Extraction Pattern

---

## Document Change History

| Date | Change | Version |
|------|--------|---------|
| 2026-03-22 | Initial extraction from Building SAP FPSL_FSDM Golden Source.docx | 1.0 |

---

**Trust Level:** Official Product Documentation  
**Source Confidence:** High (Official SAP reference material)  
**Last Reviewed:** 2026-03-22  
**Next Review:** Quarterly or upon FPSL/FSDM release updates
