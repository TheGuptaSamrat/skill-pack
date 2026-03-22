Classification: training-derived-concepts
Source basis: FPSL TRAINING DOCUMENT.pdf, pages 1-20
Trust usage: product framing, architecture understanding, data model concepts
Do not use for: customer-specific implementation details, local configuration assumptions
Topics covered: FPSL scope, Universal Journal, multi-GAAP approach, subledger architecture, HANA integration

# FPSL Architecture Overview
IFPSLF
                               SAP S/4HANA for financial products subledger
                               Financial Accounting
                               Collection 01 Revision 01
                               May 2020
                               Material Number: 50152712




Duplication is prohibited.                                                                                                                                                                                                    Duplication is prohibited.
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved.

                                 No part of this publication may be reproduced or transmitted in any form or for any purpose without the express permission of SAP SE or an SAP affiliate company.

                                 The information contained herein may be changed without prior notice. Some software products marketed by SAP SE and its distributors contain proprietary software components
                                 of other software vendors. National product specifications may vary.

                                 These materials are provided by SAP SE or an SAP affiliate company for informational purposes only, without representation or warranty of any kind, and SAP or its affiliated
                                 companies shall not be liable for errors or omissions with respect to the materials. The only warranties for SAP or SAP affiliate company products and services are those that are
                                 set forth in the express warranty statements accompanying such products and services, if any. Nothing herein should be construed as constituting an additional warranty.

                                 In particular, SAP SE or its affiliated companies have no obligation to pursue any course of business outlined in this document or any related presentation, or to develop or release
                                 any functionality mentioned therein. This document, or any related presentation, and SAP SE’s or its affiliated companies’ strategy and possible future developments, products,
                                 and/or platform directions and functionality are all subject to change and may be changed by SAP SE or its affiliated companies at any time for any reason without notice. The
                                 information in this document is not a commitment, promise, or legal obligation to deliver any material, code, or functionality. All forward-looking statements are subject to various
                                 risks and uncertainties that could cause actual results to differ materially from expectations. Readers are cautioned not to place undue reliance on these forward-looking statements,
                                 and they should not be relied upon in making purchasing decisions.

                                 SAP and other SAP products and services mentioned herein as well as their respective logos are trademarks or registered trademarks of SAP SE (or an SAP affiliate company)
                                 in Germany and other countries. All other product and service names mentioned are the trademarks of their respective companies.
                                 See http://global.sap.com/corporate-en/legal/copyright/index.epx for additional trademark information and notices.




                             © SAP SE                                                                                  IFPSLF                                                                                             1

Agenda


                                 Part 1                       Introduction

                                 Part 2                       Loan Example - Processes and Process Steps

                                 Part 3                       Bond Example - Processes and Process Steps

                                                              Conclusion




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                     3




Duplication is prohibited.                                                                                                                                              Duplication is prohibited.
                                 Introduction

                                         Introduction
                                         Your training team for the upcoming three days


                                          Breaks
                                          Bio breaks
                                          Lunch break


                                           Q&A options

                                           You can ask your questions (click on the button                             in the lower part of the screen) or

                                           raise your hand to ask verbally (click the raise hand button and we will unmute your line)



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                     4




                             2                                                                                IFPSLF                                         © SAP SE

Introduction

                                            System access
                                            Please doublecheck your access to the training system




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                         5




Duplication is prohibited.                                                                                                                                  Duplication is prohibited.
                                 Objectives

                                           After completing this learning module, you will be able to:

                                           • Understand the basic functionalities of FPSL to meet banking business requirements
                                           • Understand the general architecture and data model that underpin FPSL
                                           • Understand the accounting process model
                                           • Understand the interaction of FPSL and SAP S/4HANA




                                          Underlying software version
                                          Course based on SAP SAP S/4HANA for Financial Products Subledger 1812 Feature Package 01 (available
                                          since June 2019). All screenshots have been taken on this basis.
                                          FP02 with a few enhancement for Banking Customers has been released in December 2019, but hasn’t been
                                          considered in subsequent material, except if there are relevant enhancements to described functions and
                                          features.
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                         6




                             © SAP SE                                                                         IFPSLF                                    3

Introduction




Duplication is prohibited.                                                                                                                                                       Duplication is prohibited.
                                  Ready for the Future with Financial Product Subledger
                                                                                                                           Covers the accounting for financial
                                                                   Seamlessly integrated with                              instruments and insurance contracts
                                                                   Finance in SAP S/4HANA


                                                                                                                                     Simplifies
                                 Combines financial accounting                                                                       deployment and
                                 and controlling in the Universal                                                                    operation
                                 Journal



                                                                                                                                  Includes end-to-end best practice
                                       Provides embedded analytics                                                                templates and configuration for
                                       using the SAP Analytic Cloud                                                               IFRS 9, IFRS 17 and US GAAP



                                                           Can be deployed on premise,
                                                           SAP HANA Enterprise Cloud and                                Engineered for high-end
                                                           SAP S/4HANA Cloud, single                                    performance
                                                           tenant edition


                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                             8




                             4                                                                                 IFPSLF                                                 © SAP SE

SAP S/4HANA for financial products subledger
                                 Overview
                                                                                          SAP S/4HANA for financial products subledger, banking option
                                                                                                  is a dedicated multi-GAAP and multi-entity subledger
                                                                                                  includes a centralized accounting rules engine and Actual
                                                                                                                                                         specialized calculators                 Group
                                                                                                  empowers acquiring instant   financial insight at any level of detail for analytics and reporting
                                                                                                                            Plan
                                                                                                         Adjust                                                   Consolidated
                                                                                                  is shipped with pre-configuration and templates    for IFRS 9 and
                                                                                                                                               Planned               US GAAP
                                                                                                  comes with a scalable data model supporting Advanced HANA Data Volume Management features and Scale-out
                                                                                                  unburdens                  Allocate
                                                                                                       Measurethe product systems from accounting and controlling tasks
                                                                                                  provides seamless integration to Finance in SAP S/4HANA, including drill-down                 Entities


                                                                                                                                        Reporting & Analysis



                                         Subledger Accounting                                     GL Accounting                Entity Close                Intercompany               Consolidation                 Disclosure




                                                                                                                                     S/4HANA Universal Journal




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                      9




Duplication is prohibited.                                                                                                                                                                                                                Duplication is prohibited.
                                 SAP S/4HANA for financial products subledger
                                 Overview
                                                                                          SAP S/4HANA for financial products subledger, banking option
                                                                                                  is a dedicated multi-GAAP and multi-entity subledger
                                                                                                  includes a centralized accounting rules engine and Actual
                                                                                                                                                         specialized calculators                 Group
                                                                                                  empowers acquiring instant   financial insight at any level of detail for analytics and reporting
                                                                                                                            Plan
                                                                                                         Adjust                                                   Consolidated
                                                                                                  is shipped with pre-configuration and templates    for IFRS 9 and US
                                                                                                                                               Planned                    GAAP
                                                                                                  comes with a scalable data model supporting Advanced HANA Data Volume Management features and Scale-out
                                                                                                  unburdens                  Allocate
                                                                                                      Measurethe product systems   from accounting and controlling tasks
                                                                                                  provides seamless integration to Finance in SAP S/4HANA, including drill-down                 Entities


                                                                                                                                        Reporting & Analysis



                                         Subledger Accounting                                     GL Accounting                       SAP S/4HANA for financial
                                                                                                                               Entity Close                     products subledger covers
                                                                                                                                                          Intercompany                Consolidation                 Disclosure
                                                                                                                                                                 Amortized Cost
                                                                                                              Classification      Status                                           Fair Value             Cost
                                                                                                                                                 Impairment        & Effective
                                                                                                              Management        Management                                          Engine            Allocations
                                                                                                                                                                  Interest Rate

                                                                                                                                 Impacts of
                                                                                                              Multi Currency                    Accruals and                         Hedge            Financial
                                                                                                                               changed Master                    Lot Accounting
                                                                                                               Accounting                        Deferrals                         Accounting         Steering*
                                                                                                                                    Data




                                                                                                                                     S/4HANA Universal Journal




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                      10




                             © SAP SE                                                                                                         IFPSLF                                                                                  5

SAP S/4HANA for financial products subledger
                                 Overview


                                                                                                                                   Reporting & Analysis




                                           Subledger                                                           General Ledger                               Group Reporting

                                         Subledger Accounting                                     GL Accounting           Entity Close               Intercompany        Consolidation             Disclosure




                                                                                                                                S/4HANA Universal Journal



                                  Result Categories                                                           ACDOCA (actual)                       ACDOCU (consolidation)


                                                                                                                  Sequence of processing
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                       11




Duplication is prohibited.                                                                                                                                                                                                 Duplication is prohibited.
                                 SAP S/4HANA for financial products subledger
                                 Seamless integration with Finance in SAP S/4HANA

                                                                                                                                                      COMPANY
                                                                                                                                                          CODE
                                                                                CONTROLLING
                                                                                         AREA                                                                                 SEGMENTS




                                                                     PROFIT
                                                                     CENTER                                                                                                                ACCOUNTING
                                                                                                                                                                                            PRINCIPLE



                                                            DOCUMENT
                                                                   TYPE                                                                                                                  TRANSACTION
                                                                                                                                                                                            TYPE



                                                                              FISCAL YEAR
                                                                                  VARIANTS                                                                              MARKET
                                                                                                                                                                         DATA
                                                                                                                       CHART OF
                                                                                                                       ACCOUNTS
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                       12




                             6                                                                                                           IFPSLF                                                                 © SAP SE

SAP S/4HANA for financial products subledger
                                 Engineered for high-end performance



                                 Outstanding and reliable solution performance
                                                                                                                                                                  HANA
                                                                                                                                                                  optimized
                                            Real-time processing                                                                                                  Data Model
                                            of operational business transactions
                                                                                                                  Central GAAP
                                            Fast period-end processes                                             Approach
                                                                                                                  Elimination of
                                            for reduced time-to-close                                             Redundancies
                                                                                                                                                                  Parallelized
                                            Efficient handling of multiple GAAPs                                                                                  Processing
                                            through Central GAAP Approach: GAAP-independent                                                                       on Application
                                            postings are stored only once.                                                                                        Server Level

                                                                                                                  Scale-Out
                                            Efficient management of high data volume
                                                                                                                  Scalability
                                            through Scale-Out: scalability on database-level for single-          on Database
                                            contract based subledger improves TCO                                 Level
                                                                                                                                                                  Advanced HANA
                                            TCO optimized storage of historical data                                                                              Data Volume
                                            through business time - dependent 2nd level partitioning                                                              Management
                                                                                                                                                                  features
                                                                                                                                                                  Data Life Cycle
                                                                                                                                                                  Management



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                             13




Duplication is prohibited.                                                                                                                                                                       Duplication is prohibited.
                                     SAP S/4HANA for financial products subledger
                                     Universal Journal

                                               Single Source of Truth                                                                Multiple Currencies

                                                                                                                                               Central GAAP Approach
                                          SAP HANA & Big Data

                                                                                                                                                 Error Correction and
                                         360r View                                                                                               Suspense Accounting

                                                                                                                                                    Finance & Controlling
                                          Extensibility
                                                                                                                                                                    Projection *

                                           Subledger Connectivity                                                                                            Planning *


                                               Parallel Accounting                                                                                   Simulation *

                                                                                                                                   *: Financial Steering: Roadmap – subject to change
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                             14




                             © SAP SE                                                                         IFPSLF                                                                         7

SAP S/4HANA for financial products subledger
                                             Universal Journal




                                     © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                             15




Duplication is prohibited.                                                                                                                                                                                                                           Duplication is prohibited.
                                     SAP Bank Architecture Finance-Centric Approach – Simplified View
                                                                                                                                                                                                                             Financial Reporting
                                                                        SAP Fiori                                        SAP Analytics Cloud                   BI-Tools                               …                      & Analysis



                                                                SAP S/4HANA Operating area                                              SAP S/4HANA Finance                   SAP S/4HANA for Group Reporting                General ledger &




                                     SAP Profitability &
                                                                                                                                                                                       Group Reporting                       Subledgers
                                                                     AP                      AR                                                                                                                              Operating area
                                                                                                                                      Universal          Financial
                                                                                                                                       Journal                                   SAP BPC for SAP S/4HANA                     Consolidation
                                                                     AA                       …                                                         Master Data
                                                                                                                  Subledgers                                 General ledger               BPC                                Planning




                                 Performance Management
                                                                                                                               SAP S/4HANA for Financial Products Subledger

                                                                                                                                                                                                                             Central subledger for
                                                                                                                                    Accounting Rules & Methods                                                               financial instruments
                                                                                       Source Data                                                                                  Result Data
                                                                                                                                                                                                             Subledger


                                                                                 Master and transaction data                                                                  Target values & cash flow




                                                                                                                                                                                                                             Operational master
                                                                                                     BCA/Deposit                                                                                                             and transaction data
                                                                 CML                                                                 C/4HANA                   …                 MUREX                    Calypso
                                                                                                       Mgmt.                                                                                                                 Financial instruments


                                                                                                                                                                                                            Reading access
                                     © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                             16
                                                                                                                                                                                                            Data import




                             8                                                                                                                       IFPSLF                                                                             © SAP SE

SAP Bank Architecture Finance-Platform Approach – Simplified View
                                                                                                                                                                                                                                               Finance and Risk
                                                                        SAP Fiori                                     SAP Analytics Cloud                                  BI-Tools                              …                             Reporting & Analysis



                                                                  SAP S/4HANA Operating Area                                            SAP S/4HANA Finance                                SAP S/4HANA for Group Reporting                     General ledger &
                                                                                                                                                                                                   Group Reporting                             Subledgers




                                SAP Profitability & Performance
                                                                     AP                      AR                                                                                                                                                Operating area
                                                                                                                                      Universal                   Finacial
                                                                                                                                       Journal                                                SAP BPC for SAP S/4HANA                          Consolidation
                                                                     AA                       …                                                                  Master Data
                                                                                                                  Subledgers                                              General ledger               BPC                                     Planning


                                                                                                                               SAP S/4HANA for Financial Products Subledger




                                        Management
                                                                                                                                                                                                                                               Central subledger for
                                                                                                                                    Accounting Rules & Methods                                                                                 financial instruments
                                                                                       Source data                                                                                               Result data
                                                                                                                                                                                                                               Subledger
                                                                                   Master and transaction data                                                                                Target values & cash flows

                                                                                                                                                                                                                                               Standardized Finance &
                                                                                                                      SAP Financial Service Data Management                                                                                    Risk data model incl.
                                                                                                                                              (simplified illustration)
                                                                                                                                                                                                                                               data
                                                                                                                                                                                                                      Central data storage




                                                                                                                                                                                                                                               Operational master
                                                                                                     BCA/Deposit                                                                                                                               and transaction data
                                                                  CML                                                                C/4HANA                               …                  MUREX                        Calypso
                                                                                                       Mgmt.                                                                                                                                   Financial instruments


                                                                                                                                                                                                                              Reading access
                                     © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                                               17
                                                                                                                                                                                                                              Data import




Duplication is prohibited.                                                                                                                                                                                                                                                 Duplication is prohibited.




                                    Introduction – From Business Perspective




                             © SAP SE                                                                                                                      IFPSLF                                                                                                      9

From Business Perspective to FPSL – Recap IFRS9

                                                                                                                                       No     Is the financial asset held to achieve                  No
                                         Is the objective of entity’s business
                                                                                                                                              an objective by both collecting
                                         model to hold the financial assets to
                                                                                                                                              contractual cash flows and selling
                                         collect contractual cash flows?
                                                                                                                                              financial assets?

                                                                                               Yes                                                                        Yes
                                                                                                                                                                                                      No
                                      Do contractual cash flows represent solely payments of principal and interest?                                                                                           FVPL
                                                                                                Yes                                                                       Yes
                                                                                                                                                                                                     Yes
                                      Does the company apply the fair value option to eliminate an accounting mismatch?

                                                                                              No                                                                        No

                                                                       Amortized Cost                                                                              FVOCI


                                                                      Classification and measurement categories according to IFRS9
                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                             19




Duplication is prohibited.                                                                                                                                                                                                        Duplication is prohibited.
                                  From Business Perspective to FPSL - structure of book value components

                                                     Operational                                                                                     Analytical

                                                             Value-date dependent                                                                     Value-date independent

                                         Event-
                                                                                                                       Deterministic                                          Stochastic
                                         driven
                                        Quantity                                                                                             Valuation
                                                                              Accruals                                 Deferrals                                              Valuations
                                        changes                                                                                              Remnants
                                                                                                                                                                  Credit       Hedged All other
                                                                                                                                                                   risk           risk       risks




                                                                                 Accruals                      Deferrals   Amortized    Write Down    Valuation     Risk          Hedge          FV        Full Fair
                                        Unpaid Principle
                                                                                                                             Cost                     Remnants    Provision     Accounting   Adjustment     Value
                                           Balance
                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                             20




                             10                                                                                                              IFPSLF                                                                    © SAP SE

Accounting Process Model implemented in FPSL

                                 The accounting process model can be classified in three different dimensions:
                                 Operational vs Analytical:



                                      Operational                                                                    Analytical
                                        Day                                    Period-End Processing
                                        Processing                                                                                                                                                                 Inflation
                                                                                                                                                                                                                   Credit


                                                                                                                                                                                                           RISKS
                                                                                                                                                                                                                   Interest
                                          Register                                Accrue                        Defer                 Write     Release          Value TC                                          Equity
                                                                                                                                                                                                                   FX
                                          ….                                                                                          Down                                                                         Commodity
                                                                                                                                                                                                                   Liquidity
                                                                                                                                                                       Hedge
                                                                                   Accruals                   Deferrals                                      Risk    Accounting
                                        Unpaid Principle                                                                          Write Down   Valuation   Provision
                                           Balance                                                                                             Remnants
                                                                                                                                                                                  Fair Value
                                                                                                                                                                                  Adjustment
                                                                                                                          Amortized                                                            Full Fair
                                                                                                                            Cost                                                                Value




                                Operational sources system                                                                                     Position changes – Accounting principals dependent
                                flows transactions – Cross all
                                accounting principals
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                    21




Duplication is prohibited.                                                                                                                                                                                                               Duplication is prohibited.
                                 Accounting Process Model in FPSL
                                 Dependent vs Independent of value date:



                                 Operational                                                                    Analytical


                                        Day                                    Period-End Processing
                                        Processing
                                          Register                                Accrue                        Defer                 Write     Release          Value TC
                                          ….                                                                                          Down
                                                                                                                                                                       Hedge
                                                                                   Accruals                   Deferrals                                      Risk    Accounting
                                        Unpaid Principle                                                                          Write Down   Valuation   Provision
                                           Balance                                                                                             Remnants
                                                                                                                                                                                  Fair Value
                                                                                                                                                                                  Adjustment
                                                                                                                          Amortized                                                            Full Fair
                                                                                                                            Cost                                                                Value




                                   Dependent of value Date                                                                            Independent of value Date


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                    22




                             © SAP SE                                                                                                                  IFPSLF                                                                       11

Accounting Process Model in FPSL

                                  Event-driven vs Deterministic vs Stochastic:


                                  Operational                                                                    Analytical

                                  Dependent of value Date                                                                                Independent of value Date


                                          Day                                    Period-End Processing
                                          Processing
                                            Register                                Accrue                        Defer                 Write        Release         Value TC
                                            ….                                                                                          Down
                                                                                                                                                                           Hedge
                                                                                     Accruals                   Deferrals                                        Risk    Accounting
                                          Unpaid Principle                                                                          Write Down     Valuation   Provision
                                             Balance                                                                                               Remnants
                                                                                                                                                                                      Fair Value
                                                                                                                                                                                      Adjustment
                                                                                                                            Amortized                                                              Full Fair
                                                                                                                              Cost                                                                  Value




                                  Event-Driven                                                                  Deterministic                                                          Stochastic


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                    23




Duplication is prohibited.                                                                                                                                                                                                Duplication is prohibited.
                                   Accounting Process Model in FPSL


                                   Operational                                                                    Analytical

                                   Dependent of value Date                                                                               Independent of value Date

                                  Event-driven                               Deterministic                                                                       Stochastic


                                          Day                                    Period-End Processing
                                          Processing
                                            Register                                Accrue                        Defer                 Write        Release         Value TC
                                            ….                                                                                          Down
                                                                                                                                                                           Hedge
                                                                                     Accruals                   Deferrals                                        Risk    Accounting
                                          Unpaid Principle                                                                          Write Down     Valuation   Provision
                                             Balance                                                                                               Remnants
                                                                                                                                                                                      Fair Value
                                                                                                                                                                                      Adjustment
                                                                                                                            Amortized                                                              Full Fair
                                                                                                                              Cost                                                                  Value



                                                                                                                                     Classification Management
                                                                                                                                         Status Management
                                                                                                                            Impacts of Changed Master Data
                                                                                                                              Multi-Currency Accounting
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                    24




                             12                                                                                                                            IFPSLF                                              © SAP SE

Realization in the System




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER            25




Duplication is prohibited.                                                                                                       Duplication is prohibited.
                                 Quiz




                                       1. Name the three dimensions of the process model.

                                       2. Can you give examples of process steps for each dimension?

                                       3. Can you name the accompanying processes?




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER            26




                             © SAP SE                                                                         IFPSLF        13

Q&A


                                  Questions?




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER              27




Duplication is prohibited.                                                                                                         Duplication is prohibited.




                                  Subledger Coding Block




                             14                                                                                IFPSLF   © SAP SE

What is the Subledger Coding Block?

                                      Defines the granularity of accounting and is relevant for creating posting documents / journal entries:

                                                                                                                               Subledger Coding Block
                                                                                      General Ledger                            Additional Dimensions of the Subledger Coding
                                                                                       Coding Block                                                 Block
                                                                          General                    Additional               Subledger           Contract   P & L relevant    If neccessary.
                                                                          Ledger                     dimensions of the        account             ID         characteristics   additional dimensions
                                                                          Account                    general ledger                                                            of the subledger coding
                                                                                                     coding block                                                              block



                                                                                                               For the creation of the link to                        Documentation of change of
                                                                                                                the master data                                         a in P & L relevant
                                                                                                               Thus mandatory                                          characteristic (pro rata
                                                                                                               Represents additional, not                              temporis)
                                                                                                                explicitly existing dimensions                         Examples: Change in
                                                                                                                of the subledger coding block                           organisational unit, holding
                                                                                                                                                                        category, etc.



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                              29




Duplication is prohibited.                                                                                                                                                                                         Duplication is prohibited.
                                 Guiding Principles for multi-dimensional Accounting


                                     Only characteristics that meet one of the following requirements shall be included in the SL
                                     coding block:

                                     •        The characteristics are part of the general ledger coding block

                                     •        The characteristics are relevant for the profit and loss statement (pro rata temporis)

                                     •        Contract ID of the corresponding Contract (proxy to other characteristics)

                                     •      Securities ID of the corresponding security (proxy to other characteristics)

                                     •      Portfolio ID (proxy to other characteristics)



                                     For reporting purposes additional characteristics can be used which do not meet the above
                                     requirements … but which can be read from referenced objects

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                              30




                             © SAP SE                                                                                                       IFPSLF                                                            15

Subledger Coding Block

                                                                                                                                         Subledger Coding Block

                                                                    Master data                                                          Flow                                                                                                                                   Accounting
                                                                                                                                                                                               Analytical
                                                                                                                                         data

                                   Contractual

                                                                                                           Derived from   Derived from
                                   Master Data


                                                                                                                                          Transaction
                                                                                                                                                                                                      Analytical                                                                                Chart of
                                    Business
                                  Partner Master
                                       Data
                                                                                                                                                                                                      statuses                                                                                  accounts
                                                                                                             BPMD            OMD
                                  Organizational
                                   Master Data
                                   Derived from
                                       CMD




                                                                                                                                                             Classification                                                                                                       G/L Account
                                                                                                                                                                                                      Write-Down                Market conformity


                                                                                                                                                                                                                                                    Fair Value Levels
                                                                                                                                                                                         Impairment                                                                                                   Subledger
                                                                                                                                                                                                                   A/L Status
                                                                                                                                                                              Accrual
                                      What         Whom        Where          Who            What         Whom    Where      Who          What
                                                                                                                                                                              Status
                                                                                                                                                                                           Status       Status                       status
                                                                                                                                                                                                                                                                                                       Account


                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                                                                                                  31




Duplication is prohibited.                                                                                                                                                                                                                                                                                            Duplication is prohibited.
                                  Subledger Coding Block
                                  The set of all journal entry characteristics is the Subledger Coding Block and structured the following way:


                                                                                                                                          Subledger
                                                                                                                                         Coding Block


                                             Master Data                                                        Flow Data                               Analytical Status                                Calculation method                                                 Accounting Dimensions
                                          Analytical (derived)                                                   derived                                                                                 characteristics (der.)                                               Analytical (derived)
                                                                                                                                              •    Accrual Status                                                                                                       •      Posting Date
                                  •         Product Segment
                                                                                                                                              •    Write-Down Status                                                                                                    •      Subledger Account
                                  •         Contract Category                                      •           Posting Record                 •    Impairment StatusCalculation method                                                                                  •      Debit/Credit Indicator
                                  •         Company Code                                                                                                                      •   Calculation Method
                                                                                                                                          Analytical
                                                                                                                                              •      Status
                                                                                                                                                   A/L Status
                                                                                                                                                                                          characteristics                                                               •      Period/Fiscal Year
                                                                                                                                         Analytical (derived)                           Analytical (derived)


                                               Master Data                                                      Flow Data
                                               Operational                                                      operational
                                      •        Contract ID
                                                                                                    •          BT ID
                                      •        Source System
                                                                                                    •          Source System BT
                                      •        Contract Status
                                                                                                    •          Value Date
                                      •        Legal Entity


                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                                                                                                  32




                             16                                                                                                                             IFPSLF                                                                                                                                         © SAP SE

Realization in the system




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                   33




Duplication is prohibited.                                                                                                              Duplication is prohibited.



                                                                                                              Break (15min)




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                   34




                             © SAP SE                                                                              IFPSLF          17

Quiz




                                        1. What is the subledger coding block?

                                        2. Roughly – how is the subledger coding block structured?

                                        3. What is used for the basic structure of the subledger accounts?




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER              35




Duplication is prohibited.                                                                                                         Duplication is prohibited.
                                  Q&A


                                  Questions?




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER              36




                             18                                                                                IFPSLF   © SAP SE

Chart of accounts




Duplication is prohibited.                                                                                                       Duplication is prohibited.
                                 Chart of accounts - structure


                                 Accounting reporting structure is defined by
                                 financial statement segment and subsegment

                                 Subledger and general ledger accounts are
                                 assigned to subsegment, but representing a
                                 different granularity.




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER            38




                             © SAP SE                                                                         IFPSLF        19

Chart of accounts: Subledger chart of accounts - Example

                                  Subledger chart of accounts                                                                Subledger Account Group
                                                                                                                          100201 Accruals: Income
                                           • Purpose: Directory of
                                             all subledger
                                                                                                               10020101    Accruals: Interest Income (Requested)
                                             accounts for the
                                             production of                                                     10020102    Accruals: Fee Income (Requested)
                                             information and for
                                                                                                               10020105    Accruals: Premium Income (Requested)
                                             balance sheet
                                             reporting                                                         10020108    Accruals: Claim Income (Requested)
                                                                                                               10020109    Accruals: Acquis. Costs Income (Requested)
                                                                                                               10020110    Accruals: Profit Sharing Income (Requested)




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                               39




Duplication is prohibited.                                                                                                                                                          Duplication is prohibited.




                                  Data Model




                             20                                                                                           IFPSLF                                         © SAP SE
