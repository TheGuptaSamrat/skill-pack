# Building SAP FPSL/FSDM Golden Source

*Extracted from: Building SAP FPSL_FSDM Golden Source.docx*

# Technical Specification and Unified Knowledge Database for SAP FPSL and FSDM 2023 ABAP-Based Banking Architecture

The modernization of financial data management within the banking sector has necessitated a transition from fragmented, siloed architectures to unified, standardized environments capable of providing a "single source of truth." The integration of SAP Financial Services Data Management (FSDM) 2023 and SAP Financial Products Subledger (FPSL) 2306 represents the current pinnacle of this architectural evolution. This report serves as an exhaustive technical repository for the implementation and operation of these systems, specifically tailored for banking instruments, contracts, and securities within the SAP S/4HANA 2023 ecosystem.1

## Architectural Paradigm Shift: The ABAP-Based Foundation

The most significant development in the 2023 release cycle is the definitive shift of FSDM to an ABAP-based architecture. While previous iterations leveraged SAP HANA-native structures, the 2023 version is fully integrated into the ABAP Platform 2023, which underlies SAP S/4HANA 2023.4 This transition aligns the data management layer with the core ERP technology stack, enabling a "clean core" approach that utilizes the RESTful ABAP Programming (RAP) model for building transactional and analytical services.4

## Technology Stack and Platform Compatibility

The ABAP Platform 2023, corresponding to SAP_BASIS 758, provides the technical infrastructure required for the high-performance demands of bank management. This platform is not a standalone product but is delivered as part of SAP S/4HANA 2023 or the SAP S/4HANA Foundation 2023 for HANA-only add-ons.4 For banking institutions, this architecture facilitates a seamless upgrade path from earlier S/4HANA versions (1610 through 2022) directly to the 2023 environment.4

The architecture utilizes a three-tier client-server model, ensuring a clear separation between the presentation, application, and database layers. In this model, the SAP HANA database handles intensive data processing and in-memory analytics, while the application layer manages complex banking logic, and the presentation layer provides the user interface through SAP Fiori.4

Platform Component

Specification/Version

Role in Banking Architecture

Core Platform

ABAP Platform 2023 (SAP_BASIS 758)

Foundational technology for S/4HANA 2023.

Database Layer

SAP HANA (In-Memory)

Storage and high-speed processing of granular contracts.

Development Model

ABAP Cloud / RAP

Standardized framework for OData and Fiori apps.

Integration Framework

OData REST APIs (CRUD)

Connectivity for third-party tools and Fiori UIs.

Add-on Support

S4FPSL 300 / S4FSFND 200

Core FPSL backend components.

2

## The RAP Model and Banking Business Objects

The integration of the ABAP RESTful Application Programming (RAP) model is critical for the 2023 banking stack. RAP enables the development of Business Objects (BOs) that represent banking entities such as financial contracts and instruments. Enhancements in 2023 allow for the modeling of side effects in behavior definitions, which triggers real-time UI updates in SAP Fiori elements based on user input—a vital feature for complex manual adjustments in subledger accounting.4 Furthermore, banking business events can now be consumed locally within the S/4HANA system or remotely via SAP Event Mesh on the SAP Business Technology Platform (BTP).4

## FSDM 2023: The Harmonization and Data Integration Layer

FSDM 2023 acts as the central data hub for banking organizations, consolidating data from various source systems into a harmonized format. This layer eliminates the need for redundant data silos and provides a consistent basis for finance, risk, and regulatory reporting.1

## Conceptual Data Model (CDM) for Banking

The Conceptual Data Model (CDM) provides a business-oriented view of banking entities and their relationships. It is designed to be understood by business experts and analysts without requiring deep technical knowledge of the underlying database structures.8 The CDM covers several key banking domains:

Business Partner: Captures all parties involved in financial transactions, including roles such as borrower, lender, and guarantor.9

Financial Contract: Represents specific agreements between the bank and its customers, such as loans, deposits, and accounts.9

Financial Instrument: Defines standardized, fungible assets such as bonds, equities, and investment fund shares.11

Business Event: Records lifecycle occurrences such as contract signings, disbursements, and repayments.8

The CDM is managed at design time using the FSDM Workbench, an extension for Microsoft Visual Studio Code, which allows for graphical modeling and the definition of entities using FSDMDDL (a domain-specific data definition language).9

## Physical Data Model (PDM) and Managed Tables

The Physical Data Model (PDM) is the technical implementation of the CDM within the SAP S/4HANA system. In the ABAP-based version of FSDM 2023, the PDM is represented as ABAP Data Dictionary (DDIC) objects.8 A unique feature of the FSDM PDM is the concept of "Managed Tables," which handle the lifecycle of data records through various statuses.14

Table Status

Technical Role

Lifecycle Detail

Draft Tables

Initial Ingestion

Temporary storage for data before it is validated and activated.

Active Tables

Current Reality

Stores the currently valid version of banking records used for reporting.

History Tables

Audit Trail

Archives previous versions to support bitemporal historization and audits.

14

This bitemporal versioning is essential for banking compliance, as it allows the system to produce reports based on "Business Time" (when a transaction was valid) and "System Time" (when the record was entered or modified), ensuring full auditability.8

## Data Access through Technical and Business Views

Data records stored in managed tables are accessed through specialized Core Data Services (CDS) views. These views provide different perspectives on the data depending on the requirement:

Technical Views: These views read directly from draft, active, or history tables. They include technical metadata fields such as Load Number (LOADNO), Package Number (PACKNO), and Record Number (RECNO), which are primarily used for administrative tasks and technical data browsing.14

Business Views: These views apply prepared filters to the technical data, presenting a business-oriented view that accounts for system and business validity. They are used by Fiori apps like the Business Data Browser to display data as it appears at a specific point in time.14

## SAP FPSL 2306: The Financial Products Subledger for Banking

SAP FPSL is a high-performance subledger solution designed to manage the complexity of banking products at a granular contract level. It integrates with the S/4HANA Universal Journal (ACDOCA) while maintaining the detail necessary for multi-GAAP reporting and regulatory compliance.3

## Core Engines and Accounting Logic

FPSL architecture is built around several integrated engines that process financial data according to defined accounting standards:

Accounting Hub: Centralizes the management of posting rules, the chart of accounts, and multi-GAAP logic.17

Valuation Engine: Calculates key metrics such as Fair Value, Amortized Cost using the Effective Interest Rate (EIR) method, and Expected Credit Loss (ECL) for IFRS 9 compliance.17

Cashflow Engine (CFE): Stores and processes all actual and expected cash flows, which serve as the foundation for time-value-of-money calculations.17

Posting Engine: Utilizes Event-Based Accounting (EBA) to generate subledger journal entries triggered by business events or period-end requirements.17

## Multi-GAAP and Multi-Currency Support

Banking institutions operating internationally must comply with multiple accounting frameworks (e.g., IFRS 9, US GAAP, and various local GAAPs). FPSL 2306 utilizes a "central and delta GAAP" approach. This methodology ensures that cross-GAAP entries—those common to all standards—are posted only once, while GAAP-specific adjustments are posted separately for each accounting principle. This significantly reduces data redundancy and reconciliation efforts.7

Accounting Standard

Requirement

FPSL 2306 Banking Template

IFRS 9

Financial Instruments

Amortized Cost, Fair Value (P&L/OCI), ECL calculation.

US GAAP

Recognition/Measurement

Specialized templates for US-specific classifications.

Local GAAP

Statutory Reporting

Delta postings relative to the central GAAP approach.

3

## Universal Journal Integration and Aggregation

While FPSL maintains millions of granular contract-level documents, the General Ledger (GL) in S/4HANA typically requires a summarized view. FPSL aggregates subledger journal entries into GL documents, which are then transferred to the Universal Journal (ACDOCA). This ensures that GL reporting remains performant while the subledger provides the "drill-down" capability to individual contracts for auditing purposes.17

## Integration Mechanics: FSDM 2023 to FPSL 2306

The seamless integration between FSDM and FPSL is achieved through the Data Loading (DL) process. FSDM serves as the "provisioning layer," and FPSL acts as the consumer.11

## The Data Loading (DL) Process Workflow

The DL process is a standardized sequence of steps that replicates data from FSDM to the FPSL internal data model:

Change Pointer Generation: The system identifies new or modified objects in FSDM since the last data load.11

Data Extraction: FPSL triggers extraction from FSDM via remote-enabled function modules (RFMs) located in the /FSDL/EXTRACT function group.11

Transformation and Mapping: The FSDM consumption layer uses mapping views to transform the data into the target FPSL structure.11

Data Ingestion: The mapped data is loaded into FPSL tables, where it becomes available for accounting and valuation processes.11

## Key Integration Views and Performance Enhancements

The FSDM consumption layer provides several standard mapping views (/FSDL/MV_*) that are critical for the GHCP-based Skill to understand the data flow. Recent enhancements in the 2023/FP03 and FP05 releases have focused on improving performance for high-volume banking data.25

/FSDL/MV_BUSINESSTRANSACTIONS: Maps banking settlements to FPSL business transactions. It has been enhanced to include mirror contract identifiers (BA1_C55R5CNID for contracts and BA1_C55R6CNID for securities).27

/FSDL/MV_BASICDATA: Provisioning of master data for financial contracts. The introduction of /FSDL/CV_FINANCIALCONTRACT_UN offloads complex join logic to improve extraction speed.25

/FSDL/MV_SECURITIESBASICDATA: Handles the master data for financial instruments. For equity instruments and investment fund shares, the system now correctly suppresses contract start and end dates, reflecting the nature of these products.25

/FSDL/MV_INTERESTACCRUALS_COND: A new view that aggregates fine-granular FSDM accrual types into the broader accrual categories expected by FPSL, preventing key-conflict errors during processing.27

## Value Mapping and Customization Tables

Many banking attributes require a transformation of codes between FSDM and FPSL. This is handled through specialized value mapping tables maintained in the "Custom Business Configurations" Fiori app.28

Mapping Table

Input Fields (FSDM)

Output Field (FPSL)

Purpose

/FSDL/MAP_ACLTYP

Accrual Type, Interest Type

BA1/C55ACCAT

Accrual category derivation.

/FSDL/MAP_TTYPE

Transaction Type, PCI

BA1/C55TTYPE

Business transaction classification.

/FSDL/MAP_SECTYP

Instrument Class

BA1C_FITYPE

Security type mapping.

/FSDL/MAP_PCI

Product Catalog Item

BA1C/HDRTEMPL

Template derivation (Structured vs Unstructured).

26

A critical technical nuance in the 2023 integration is the handling of the LOT_ID field. In FSDM, this field is 128 characters, while FPSL only supports 15 characters. This discrepancy necessitates strict validation at the source to prevent data truncation errors during the DL process.25

## Banking Domain Entities: Detailed Mapping and Field Analysis

For the "golden source" to be effective, it must accurately represent banking-specific instruments and their associated financial flows.

## Financial Contracts vs. Financial Instruments

The banking model distinguishes between contracts (specific agreements) and instruments (fungible securities). This distinction determines the target table in FPSL and the valuation logic applied.9

Financial Contracts: Includes loans, current accounts, and fixed-term deposits. These are often processed as "unstructured" unless they involve complex components like embedded derivatives.25

Financial Instruments: Includes bonds, equities, and derivatives. In FSDM, these are mapped via the /FSDL/MV_SECURITIESBASICDATA view to the FPSL securities position management.11

## Structured vs. Unstructured Delivery

Banks often deal with complex products like interest rate swaps or structured notes. FSDM 2023 allows these to be delivered as either structured or unstructured objects.25

If a contract is marked with StructuredDeliveryFlag = TRUE, the mapping must derive the correct template (e.g., S40_505 via the /FSDL/MAP_PCI table). If delivered as unstructured, a standard template like S40_500 is used. This flag determines whether FPSL treats the contract as a single unit or as a hierarchy of components.25

## Settlements and Cash Flows

The movement of cash is the lifeblood of banking finance. FSDM captures this through the "Settlement" (actual flows) and "Repayment Schedule" (expected flows) entities.11

Settlements: Mapped to FPSL Business Transactions. These trigger Event-Based Accounting entries.11

Cash Flows: Provided as input to the FPSL Valuation Engine. They are essential for calculating Amortized Cost and the Fair Value of debt instruments.17

FSDM Cash Flow Item Type

FPSL Category (BA1_CRCCFITCG)

Business Description

PrincipalChanges

01

Repayments or disbursements.

InterestPayments

02

Standard interest payments.

FeePayments

03

Associated transaction fees.

PrincipalBalance

04

Remaining principal amount.

27

## Advanced Scenarios: Hedge Accounting and Credit Risk

Modern banking requires sophisticated handling of risk mitigation and impairment calculations, both of which are deeply integrated into the FSDM-FPSL 2023 landscape.

## Hedge Accounting Implementation

Hedge accounting involves the designation of hedging instruments to offset changes in the fair value or cash flows of hedged items. In FSDM 2023, these are managed using the Collection and CollectionAssignment entities.25

New views introduced for this purpose include:

/FSDL/MV_HEDGE_PORTF_DEF: Defines the "Hedge Portfolio" in FPSL, derived from the FSDM Collection entity.25

/FSDL/MV_HEDGE_PORTF_ASSIGNM: Maps the assignment of specific contracts or instruments to the hedge. A key field here is the HedgeRatio, which identifies the portion of the instrument's volume that is part of the hedge relationship.25

/FSDL/MV_INTERESTRATERISKADJST: Provisions adjustments for interest rate risk, which are frequently used in fair value hedges. This view now supports multiple hedge assignments per instrument by including the Hedge Relationship ID.25

## Credit Risk Adjustments and IFRS 9 Staging

The calculation of the Expected Credit Loss (ECL) is a core requirement for banking subledgers under IFRS 9. The FPSL Valuation Engine performs these calculations based on risk parameters provisioned from FSDM.17

The system tracks several key analytical statuses and key date values:

Impairment Status and Staging: Determines if an instrument is in Stage 1, 2, or 3 based on credit quality changes since inception.11

Probability of Default (PD) and Loss Given Default (LGD): These risk parameters are provided by FSDM's analytical layer and used in the ECL formula.11

Days Past Due: A primary indicator used for the automated "staging" of financial contracts.11

The integrated calculation engine in FPSL allows for real-time, event-driven recalculations. For example, a change in a borrower's credit rating in FSDM can immediately trigger a recalculation of the ECL provision in FPSL, ensuring that the bank's financial statements reflect current risk profiles.20

## Technical Implementation and Operational Governance

Deploying and maintaining the FSDM 2023 and FPSL 2306 ecosystem requires adherence to specific technical prerequisites and governance standards.

## Installation Prerequisites and SAP Notes

The installation of the 2023 stack is a multi-step process. FSDM 2023 is installed as an ABAP add-on to S/4HANA 2023. Several critical SAP Notes must be applied to the FPSL 2306 environment to ensure the stability of the Data Loading (DL) process.7

SAP Note

Purpose

Criticality

3366144

Fixes for DL Process on HANA source.

Mandatory

3388094

Prevents false RFC errors during DL process chains.

Mandatory

3409757

Corrects delta approach logic in data loads.

Mandatory

3411743

Prevents DL jobs from aborting with shortdumps.

Mandatory

3409757

Handling of missing authorizations during data load.

Mandatory

3330659

Installation of FPSL business content via ASU task list.

Mandatory

24

## Authorization and Security Framework

Security in the unified database is managed through the ABAP authorization concept. Access to FSDM's business data browser is controlled via specific objects for each entity class 10:

/FSDC/BP: Business Partner data access.

/FSDC/FC: Financial Contract data access.

/FSDC/FI: Financial Instrument data access.

For the integration between the two systems, the user executing the extraction must have the authorization object /FSDL/FPSL with activity 33 (Read).24 Additionally, a new authorization object /FSDM/FILE has been introduced in 2023 to restrict access to individual files within the FSDM file store—a critical feature for managing custom mapping uploads.10

## Data Anonymization for Testing

To comply with data privacy regulations (like GDPR) while still enabling realistic testing, FSDM 2023 introduces a data anonymization feature.10 This allows developers and testers to replace sensitive customer values with substitute data during the load and activation process. This capability is controlled by the ANONYMIZE activity on the /FSDM/LOAD authorization object, ensuring that only authorized personnel can mask data.10

## Operational Monitoring and Performance Optimization

High-volume banking environments require rigorous monitoring and performance tuning to meet tight period-end closing windows.

## Monitoring Fiori Apps

The 2023 release introduces several Fiori apps for operational oversight:

FSDM Loads: Provides a list of all data ingestion events. Statuses are color-coded: ACTIVE is green, while ACTIVATING or ERROR are shown in red to facilitate quick intervention.10

FSDM Logs: Centralizes all application and technical logs associated with data processing and integration.10

FSDM Managed Views: This app allows administrators to display metadata, result sets, and graphical data lineage for both standard mapping views and custom customer views.10

## Performance Optimization Strategies

For large banks with millions of contracts, extraction performance is paramount. Several technical mechanisms are employed in 2023 to optimize the data flow:

Buffered Views: The use of views like /FSDL/CV_FINANCIALCONTRACT_BUF helps reduce the load on the primary HANA tables during repeated extractions.26

Delta Loading Approach: By using change pointers, the system ensures that only modified records are processed, significantly reducing the volume of data transferred between FSDM and FPSL after the initial load.11

Parallelization: The system can be configured for implicit or explicit parallelization during data container creation and orchestration, leveraging the multi-core processing capabilities of the SAP HANA database.30

## Analytical Power and Regulatory Readiness

The unified database serves not only as an accounting engine but also as a powerful analytical platform, ready for future regulatory changes such as IReF and BIRD.1

## Transparency and Auditability

The bitemporal historization in FSDM, combined with the granular contract-level documents in FPSL, provides unparalleled transparency. Any consolidated figure on a balance sheet can be traced back to the specific contract, the business event that triggered the posting, and the original master data as it existed at that time.1

## Cross-Product and Real-Time Insights

Because FSDM harmonizes data across all banking verticals—from retail loans to complex OTC derivatives—banks can perform holistic analytics. This includes cross-product customer profitability, real-time exposure monitoring, and advanced risk simulations.1 The integration with SAP Analytics Cloud (SAC) further enhances this by providing powerful visualization and planning capabilities directly on top of the subledger results.7

## Strategic Value of the Unified Banking Architecture

The implementation of FSDM 2023 and FPSL 2306 is not merely a technical upgrade; it is a strategic repositioning of the bank's financial core.

## Reduction in Total Cost of Ownership (TCO)

By utilizing a single, standardized platform (S/4HANA) for both data management and subledger accounting, banks can significantly reduce their TCO. This is achieved through:

Simplified Integration: Predefined content and mapping views eliminate the need for custom-built ETL layers.1

Skill Set Reuse: Leveraging existing ABAP and Fiori expertise across the entire finance and risk landscape.1

Consolidation of Silos: Retiring legacy standalone risk and accounting subledgers.1

## Agility and the "Continuous Close"

The move toward "Event-Based Accounting" and automated data flows brings banks closer to the "Continuous Close." Instead of waiting for a month-end batch process, accounting entries are generated throughout the period as business events occur. This allows management to have an up-to-date view of the bank's financial position at any given time, rather than just once a month.19

## Conclusion: The "Golden Source" for Banking Finance

The SAP FPSL 2306 and FSDM 2023 (ABAP-based) ecosystem provides the definitive "golden source" for modern banking. By establishing a unified, granular, and bitemporal data foundation, banking institutions can meet the most stringent regulatory requirements while simultaneously unlocking strategic insights and operational efficiencies. The transition to the ABAP platform in 2023 ensures that this architecture is future-proof, scalable, and fully integrated with the broader SAP S/4HANA banking strategy.1

Works cited

Financial Services Data Management | SAP Fioneer, accessed on March 22, 2026, https://www.sapfioneer.com/finance-esg/financial-services-data-management/

Financial Services Data Management 2023, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/

SAP S/4HANA Financial Product Sub-Ledger (SAP S/4HANA FPSL) for Financial and Insurance institutions - Scheer, accessed on March 22, 2026, https://www.scheer-ids.com/company/blog/sap-s/4hana-financial-product-sub-ledger-sap-s/4hana-fpsl-for-financial-and-insurance-institutions

ABAP Platform for SAP S/4HANA 2023 - SAP Community, accessed on March 22, 2026, https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/abap-platform-for-sap-s-4hana-2023/ba-p/13573791

ABAP Platform, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/latest/en/4-ABAPCloud/README

SAP Architecture, ABAP, Companies | PDF | Databases - Scribd, accessed on March 22, 2026, https://www.scribd.com/document/893993446/SAP-Architecture-ABAP-Companies

Getting Started Guide for SAP S/4HANA for ... - SAP Help Portal, accessed on March 22, 2026, https://help.sap.com/doc/fd83cd845c4b43a09cb5462d1759d61a/2306.003/en-US/loioe272dc8471c242fe900bedb72c0e824e_00031109.pdf

Data Model - Financial Services Data Management 2023 - SAP Fioneer, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/v2023_130/en/5-DataModel/Readme

Data Model - Financial Services Data Management 2023 - SAP Fioneer, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/latest/en/5-DataModel/Readme

ABAP Enhancements - Financial Services Data Management 2023 - SAP Fioneer, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/latest/en/01-GetStarted/News/23_150/23_150_ABAP

Integration with FPSL - Financial Services Data Management 2023 - SAP Fioneer, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/latest/en/5-Integration/20-Integrate-Product/FPSL

Fioneer Financial Services Data Management - SAP, accessed on March 22, 2026, https://www.sap.com/products/erp/partners/sap-fioneer-gmbh-fioneer-financial-services-data-management.html

Good to Know about FSDM - Financial Services Data Management 2023 - SAP Fioneer, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/latest/en/1-G2K/G2K_FSDM

Good to Know about Data Tables and Views, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/v2023_130/en/4-ABAPCloud/G2K_ABAP

Good to Know about Data Tables and Views, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/latest/en/4-ABAPCloud/G2K_ABAP

Business Data Browser - Financial Services Data Management 2023, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/latest/en/4-ABAPCloud/30-FioriApps/Bus_Dat_Brws/Bus_Dat_Brws

SAP FPSL | PDF | Fair Value | International Financial Reporting Standards - Scribd, accessed on March 22, 2026, https://www.scribd.com/document/979504001/SAP-FPSL

Feature Scope Description for SAP S/4HANA for ... - SAP Help Portal, accessed on March 22, 2026, https://help.sap.com/doc/dd16d015d84e4ced8e6df21e940ad498/2306.004/en-US/FSD_FPSL_EN.pdf

Financial Products Subledger | SAP Fioneer, accessed on March 22, 2026, https://www.sapfioneer.com/finance-esg/financial-products-subledger/

Why SAP FPSL is a Capital Optimizer | by Ferran Frances-Gil - Medium, accessed on March 22, 2026, https://medium.com/@ferran.frances/why-sap-fpsl-is-a-capital-optimizer-caba90fdd85d

What is... SAP S/4HANA for Financial Products Subledger? | ADWEKO | IT-Lösungen für Banken & Versicherungen, accessed on March 22, 2026, https://www.adweko.com/project/what-is-sap-s-4hana-for-financial-products-subledger/?lang=en

SAP FPSL (Financial Products Subledger) Training Course - Multisoft Virtual Academy, accessed on March 22, 2026, https://www.multisoftvirtualacademy.com/erp/sap-financial-products-subledger-training

SAP Financial Products Subledger | DYCSI | SAP Fioneer, accessed on March 22, 2026, https://dycsi.net/sap-fpsl/

Prepare Your Integration - Financial Services Data Management 2023 - SAP Fioneer, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/latest/en/5-Integration/20-Integrate-Product/Prep_Integration

Enhancements for the FPSL Integration - Financial Services Data Management 2023, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/v2023_130/en/01-GetStarted/News/23_130/23_130_FPSL

Enhancements for the FPSL Integration - Financial Services Data Management 2023, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/latest/en/01-GetStarted/News/23_150/23_150_FPSL

Enhancements for the FPSL Integration - Financial Services Data Management 2023, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/v2023_120/en/01-GetStarted/News/23_120/23_120_FPSL

Value Mapping - Financial Services Data Management 2023 - SAP Fioneer, accessed on March 22, 2026, https://fsdm.docs.fioneer.com/latest/en/5-Integration/20-Integrate-Product/ValueMapping

Integration Between Different Financial Services Products - SAP Help Portal, accessed on March 22, 2026, https://help.sap.com/doc/16d9b896d5fa49a797a4d995a2dd4cba/1.26/en-US/Integration_Guide_FSDM_FPSL.pdf

Installation and Upgrade - Finance Data Suite - SAP Fioneer, accessed on March 22, 2026, https://fds.docs.fioneer.com/v2025-001.1/en/fds/Installation/Installation

Let's Integrate SAP FPSL Full Video by Prasad Sri Koribilli - YouTube, accessed on March 22, 2026, https://www.youtube.com/watch?v=Q5tUkJuPdZ0

SAP for Banking Management | FSDP, FPSL | BearingPoint USA, accessed on March 22, 2026, https://www.bearingpoint.com/en-us/industries/banking-and-capital-markets/sap-oriented-bank-management/

