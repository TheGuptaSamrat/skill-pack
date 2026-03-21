Classification: training-derived-concepts
Source basis: FPSL TRAINING DOCUMENT.pdf, pages 50-100
Trust usage: standard FPSL process nomenclature, sequence understanding, process-step dependencies
Do not use for: customer configuration or method names
Topics covered: Register, Accrue, Defer, Value, Classify, FX revaluation, process sequence

# Complete FPSL Process Steps Reference
Accounting Process Model and Book Value Components - Register

                                  Day                                     Period-End Processing
                                  Processing




                                                                                                                                       Write
                                  Register                                         Accrue                          Defer                           Release                  Value TC
                                                                                                                                       Down


                                                                                 Accruals                      Deferrals
                                       Unpaid
                                                                                                                                   Write Down                            Hedged Fair Value
                                      Principle                                                                                                 Valuation
                                                                                                                                                Remnants     Credit Risk financial Adjustment
                                      Balance
                                                                                                                                                                            risks



                                                                                                                           Amortized
                                                                                                                                                                                                Fair Value
                                                                                                                             Cost



                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                            99




Duplication is prohibited.                                                                                                                                                                                     Duplication is prohibited.


                                  Loan Intraday Processing
                                  Register
                                  Demo




                             50                                                                                                        IFPSLF                                                       © SAP SE

Transaction                                                                    Specs            System-Example   View
                               /BA1/BR_SET_POST_DAT                                                           01.01.2018DEM
                                - Set Posting Date                                                            O01
                               SE16:                                                                                           DEMO01_LOAN_01
                               /BA1/BR_REG_MDC
                               /BA1/BR_REG_MD
                               /BA1/BR_REG_BT
                               SE16:                                                                                           DEMO01_LOAN_01
                               /BA1/BR_REG_BT
                               /BA1/BR_REGISTER                                                               DEMO01
                                - Register
                               /BA1/BR_RESLT_VIEWER                                                           DEMO01
                               - Ergebnisdaten -> Nebenbuchbelege anzeigen
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                            101




Duplication is prohibited.                                                                                                                                        Duplication is prohibited.


                                 Loan Intraday Processing
                                 Register
                                 Theory




                             © SAP SE                                                                                 IFPSLF                                 51

Register – Definition and Characteristics                                                                                                       Register


                                  Definition                                                                                        Process step
                                  In accounting you use the Register process step to                                                The Register process step is an operational
                                  document all business transactions imported since                                                 process step. It is responsible for the registration of
                                  the step was executed last, and all business                                                      • Business Transactions
                                  transactions haven't been processed completely or                                                 • Master data changes
                                  correctly in a previous register run.                                                             • Analytical decisions


                                  Business Transactions                                                                             Master Data Changes
                                  Transfer of operational flow transactions (Business                                               Master data include contracts, securities, business
                                  Transactions) to Subledger Accounting and                                                         partners.
                                  documentation as subledger Journal Entries.                                                       In case of a master data change: contract or
                                  • Posting date of BT  set posting date                                                           security positions are marked for end-of-day
                                  • Business transaction class is relevant                                                          processing (contract).


                                  SE16: table /BA1/BR_REG_BT                                                                        SE16: table /BA1/BR_REG_MD

                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                  103




Duplication is prohibited.                                                                                                                                                                          Duplication is prohibited.
                                  Processing Events Across Systems




                                                                                               Source System X                     Mapping                     FPSL Accounting
                                                             What                          •        Transaction Type       •    Information is             •    Creating subledger
                                                                                           •        Amount / Transaction        mapped on FPSL                  Journal Entries
                                                             How                                    Currency                    SDL object                 •    G/L Accounts
                                                             much                          •        Amount / Position      ÆBusiness Transaction                ÆReady for
                                                                                                    Currency                                                    Reporting
                                                            When                           •        Posting / Value Date
                                                              Who                          •        Contract ID


                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                  104




                             52                                                                                                IFPSLF                                                    © SAP SE

Exemplary Derivation of Posting Rule




                                                                                                      Based on the information of the contract referenced by the Business Transaction
                                          Product Segment



                                                                                                      Gives information on the accounts involved in the accounting record
                                           Transaction Type                                           e.g., ‘Payment distribution’ and ‘Income: Interest‘



                                                                                                      Defines which account is the Debit and Credit account
                                           Posting Direction                                          e.g. UPB (Payment distribution (D) to Income: Interest (C))




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                             105




Duplication is prohibited.                                                                                                                                                                         Duplication is prohibited.
                                 Posting Rule Derivation – IMG – Definition




                                                    1
                                                    2




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                             106




                             © SAP SE                                                                                               IFPSLF                                                    53

Posting Rule Derivation – IMG – Derivation




                                                     1
                                                     2




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                          107




Duplication is prohibited.                                                                                                                                                                      Duplication is prohibited.
                                  Data Model – Additional relevant information

                                                         Master Data                                                Additional                Flow Data            Key Date Values
                                                                                                                 Information on
                                                Contract                                                          Master Data
                                                                                 Business                                             Business                     Target
                                                                                                                                                   Cash Flow
                                                                                  Partner                      Analytical            Transaction                   Values
                                                                                                                Status
                                                                                  Portfolio




                                                                                 Calculation Rates                          Journal Entries               Market Data
                                                                                   and Factors

                                                                                              Impairment
                                                                                               Attributes




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                          108




                             54                                                                                                   IFPSLF                                             © SAP SE

Data Model                                                                                                                                   Delivery is …

                                                                                                              Specifies whether revenue (for example, interest payments
                                                                                Accrual Status                or accrual results) can be included in the profit and loss        optional
                                                                                                              statement.

                                                                                                              Specifies if a contract is written down (partially or
                                                                           Write-Down Status                                                                                   mandatory




                                      Analytical Status
                                                                                                              completely). This is an accounting write off and not a legal
                                                                                                              write off. Status at contract creation: Not Written Down.


                                                                                                              Specifies the classification that the system needs to derive
                                                                           Impairment Status
                                                                                                              the impairment calculation approach.                              optional

                                                                                                              Specifies the classification of a financial product according
                                                                                 Classification
                                                                                                              to accounting principle for balance sheet reporting purposes.     optional

                                                                                                              Determined from the debit/credit sign of the book value in
                                                                        Asset Liability Status
                                                                                                              functional currency.                                            not possible

                                                                                                              Divides the term of contracts or securities positions into
                                                                                Term Segment
                                                                                                              segments for analytical purposes.                                 optional
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                   109




Duplication is prohibited.                                                                                                                                                                               Duplication is prohibited.
                                 Configuration of Analytical Status Derivation

                                     1. Analytical Status IMG Activities / Explanation




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                   110




                             © SAP SE                                                                                           IFPSLF                                                              55

Data Model – Additional Information – Analytical Status

                                      1. Analytical Status




                                     2. A look into the system
                                     /BA1/HW_RESULTVIEWER - Display Results Data
                                     Result Area / Resultview: SAFI / _S_SC_STS

                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                            111




Duplication is prohibited.                                                                                                                                                                        Duplication is prohibited.
                                  Data Model

                                                       Master Data                                                  Additional                  Flow Data            Key Date Values
                                                                                                                 Information on
                                               Contract                                                           Master Data
                                                                               Business                                                    Business                  Target
                                                                                                                                                        Cash Flow
                                                                                Partner                        Analytical                 Transaction                Values
                                                                                                                Status
                                                                                Portfolio




                                                                                 Calculation Rates                            Journal Entries               Market Data
                                                                                   and Factors
                                                                                                                            Subledger Journal Entry
                                                                                              Impairment
                                                                                               Attributes




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                            112




                             56                                                                                                      IFPSLF                                            © SAP SE

Data Model – Posting Document – Subledger Document

                                     1. Posting Document




                                    2. A look into the system
                                    /BA1/BR_RESLT_VIEWER - Display Subledger Documents


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER            113




Duplication is prohibited.                                                                                                        Duplication is prohibited.


                                 Loan Intraday Processing
                                 Register
                                 Hands On




                             © SAP SE                                                                         IFPSLF         57

Hands on – Day Processing 1

                                                                                             Task                           SAP Menu Location & Transaction
                                           a.       Set the posting date for your Source                         a)   /BA1/BR_SET_POST_DAT - Set Posting Date
                                                    System                                                       b)   /BA1/BR_REGISTER - Register
                                           b.       Execute the Register for your Source                         c)   /BA1/BR_DAY_END_1 - End-of-Day Processing (Contract)
                                                    System
                                           c.       Execute the End-of-Day (Contract)
                                                    Process


                                                                           To be considered
                                          The following parameters must be
                                          considered:
                                          1. Source System
                                          2. Posting Date


                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                115




Duplication is prohibited.                                                                                                                                                        Duplication is prohibited.
                                  Hands on – Results: Additional Data
                                                                                                                                                          Additional Data

                                                                                             Task                           SAP Menu Location & Transaction
                                          Check the additional information on                                    /BA1/HW_RESULTVIEWER - Display Results Data
                                          master data: Analytical Status with
                                          Result View _S_SCT_STS.




                                                                           To be considered
                                          The following parameters must be
                                          considered:
                                          1. Legal Entity
                                          2. Mind the System Date!


                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                116




                             58                                                                                IFPSLF                                                 © SAP SE

Hands on – Results: Posting Documents
                                                                                                                                                                 Journal Entries

                                                                                                     Task                                  To be considered
                                         Check the subledger Journal Entries with Result                                   The following parameters must be considered:
                                         View _S_SLPD.                                                                     1. Legal Entity


                                                                                   Selection Screen                                  SAP Menu Location & Transaction
                                                                                                                           /BA1/BR_RESLT_VIEWER - Display Subledger Documents




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                    117




Duplication is prohibited.                                                                                                                                                                Duplication is prohibited.




                               Transaction                                                                    Specs             System-Example           View
                               /BA1/BR_REGISTER                                                               DEMO_01
                                - Register
                               /BA1/BR_DAY_END_1                                                              DEMO_01
                               - End-of-Day Processing (Contract)                                             01.01.2018


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                    118




                             © SAP SE                                                                                 IFPSLF                                                         59

Q&A


                                  Questions?



                                  End of Day 1




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                    119




Duplication is prohibited.                                                                                                                Duplication is prohibited.
                                  Quiz




                                        1.          What is the use of the transaction ‘Set Posting Date‘?

                                        2.          What does the ‘Register‘ process step do?

                                        3.          What are the substeps of the ‘Register‘ process step? Where can you find
                                                    out if there are tasks for the substeps?

                                        4.          Name 3 analytical status. Is their delivery optional or mandatory?




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                    120




                             60                                                                                IFPSLF          © SAP SE

Loan Day Processing
                                 Day End Processing




Duplication is prohibited.                                                                                                                                                              Duplication is prohibited.
                                 Day End Processing - Purposes

                                           While new data coming in can be processed by registered instantly, there are some tasks
                                           which can only be applied at a day end to create a consistent status

                                           •        Fixing of operational value flows in foreign currencies
                                                          Accounting has always an End-of-Day view and therefore needs a translation into functional currency with
                                                          day end quotes. If value flows are getting registered throughout the day a translation is already happening
                                                          with FX rates available at this point in time. At day end translations need to be adopted to reflect day end end
                                                          currency quote.

                                           •        Reclassification of current positions due to code block changes
                                                          Attributes used to derive code block elements can be delivered during the day. Because accounting does not
                                                          have an intraday view / requirement for classification, all subledger documents created during the day are
                                                          using previous day code block elements.
                                                          Reclassifications will be applied only at day end to transfer End-of-Day positions to the new code block value.

                                                           To be considered
                                                           The functionality of this process will be discussed in a later chapter:
                                                           Special Topic Management of Attribute Changes

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                  122




                             © SAP SE                                                                               IFPSLF                                                         61

Agenda Part 2 – Loan Example

                                  1.          Introduction – Summary of Part 1

                                  2.          Day Processing

                                  3.          Period-End Processing

                                  4.          Additional information on Day and Period-End Processing

                                  5.          Year-End processing

                                  6.          Special Topics

                                  7.          Summary of Part 2




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                 123




Duplication is prohibited.                                                                                                                             Duplication is prohibited.
                                  Agenda Part 2 – Period-End Processing

                                                  Prerequisites
                                                                                                                        General Structure
                                                  Methods
                                                                                                                        ¾ Business
                                                  Process Steps                                                          motivation
                                           –            Accrue
                                           –            Defer                                                           ¾ Demo
                                           –            Value TC
                                                                                                                        ¾ Theory
                                                  Period-End – Close
                                                                                                                        ¾ Hands On




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                 124




                             62                                                                                IFPSLF                       © SAP SE

Example
                                                                                                                                          Accounting Requirements
                                Basic Data - Loan
                                                                                                                                          •   Periodic financial statement (monthly reporting 31.01. / 28.02. /
                                Maturity                                                        01.01.2018 – 01.01.2028 (10 Years)            31.03. / …)
                                                                                                                                          •   (optional) additional information more frequently needed for
                                Nominal                                                         1 000 000 €                                   some components

                                Discount                                                        10 000 €

                                Nominal Interest                                                1.2%

                                Interest Payment                                               Quarterly                                  Error Conflict Handler

                                Repayment                                                      Half-yearly


                                    Operational                                       Disburse-                                           Interest-
                                                                                                                            Interest-
                                      Events                                            ment                                              Payment
                                                                                                                            Payment
                                                                                                                                         Repayment

                                                                                     01.01.2018               31.01.2018   31.03.2018     30.06.2018


                                  FPSL System                                           Register
                                                                                                              Period End   Period End    Period End
                                    Activities                                      End-of-day
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                  125




Duplication is prohibited.                                                                                                                                                                                              Duplication is prohibited.
                                 Period-End Processing for Contracts – Business Motivation

                                           At the end of the period the financial statement should reflect in an appropriate way all
                                           financial aspects of the business as of the last day of the period. Purpose is to disclose
                                           transparency regarding the current business situation to all stakeholders (regulators,
                                           financial markets, business partner, investors).

                                           To achieve this all components of the financial statement need to be updated to document

                                           •        All operational value flows

                                           •        All not completed income and efforts (accruals and deferral) need to be distributed for the
                                                    current period

                                           •        Risk provision needs to be calculated and updated in the balance sheet

                                           •        Valuation of all assets and obligations needs to be updated

                                           •        All relevant risks need to be reflected appropriately in the financial statement

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                  126




                             © SAP SE                                                                                                IFPSLF                                                                        63

Loan Period-End Processing

                                  Demo




Duplication is prohibited.                                                                                                                                                                        Duplication is prohibited.
                                  Data Model

                                                       Master Data                                                  Additional                  Flow Data            Key Date Values
                                                                                                                 Information on
                                               Contract                                                           Master Data
                                                                               Business                                                    Business                  Target
                                                                                                                                                        Cash Flow
                                                                                Partner                        Analytical                 Transaction                Values
                                                                                                                Status
                                                                                Portfolio




                                                                                 Calculation Rates                            Journal Entries               Market Data
                                                                                   and Factors
                                                                                                                            Subledger Journal Entry
                                                                                              Impairment
                                                                                               Attributes




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                            128




                             64                                                                                                      IFPSLF                                            © SAP SE

Key Date Values
                                 Data Model
                                                                                                              Delivery                                   Delivery

                                                                                                                                       Price/ Gain         optional

                                                                         Accruals                             mandatory                                   mandatory




                                 Target Values
                                                                                                                                    Accrued Interest

                                                                        Deferrals                                                  Amortized Valuation     optional
                                                                                                               optional
                                                                                                                                          Cost

                                                                Amortized Cost                                                     Interest Rate Risk
                                                                                                               optional                                    optional
                                                                                                                                       Adjustment
                                                                      Credit Risk                                                     Fair Value of
                                                                                                               optional                                   mandatory
                                                                      Adjustment                                                       Collateral

                                                     Legend
                                                                                                                                       Fair Value          optional
                                                                      Used in the loan example

                                                                      Target value but not used in the loan example

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                129




Duplication is prohibited.                                                                                                                                                            Duplication is prohibited.
                                 Data Model – Key Date Values – Target Values – Accruals

                                1. Target Value - Accruals




                                 2. A look into the system
                                 /BA1/HW_RESULTVIEWER - Display Results Data
                                 Result Area / Resultview: SAFI / _S_SCT_TVR



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                130




                             © SAP SE                                                                                     IFPSLF                                                 65

Data Model

                                                       Master Data                                                  Additional                  Flow Data            Key Date Values
                                                                                                                 Information on
                                               Contract                                                           Master Data
                                                                               Business                                                    Business                  Target
                                                                                                                                                        Cash Flow
                                                                                Partner                        Analytical                 Transaction                Values
                                                                                                                Status
                                                                                Portfolio




                                                                                 Calculation Rates                            Journal Entries               Market Data
                                                                                   and Factors
                                                                                                                            Subledger Journal Entry
                                                                                              Impairment
                                                                                               Attributes




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                            131




Duplication is prohibited.                                                                                                                                                                        Duplication is prohibited.
                                  Data Model – Calculation Rates and Factors – Impairment Attributes

                                                     1. Calculation Rates and Factors – Impairment Attributes




                                                   2. A look into the system
                                                   /BA1/HW_RESULTVIEWER
                                                   Result Area / Resultview: SAFI / _S_SCT_IMP

                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                            132




                             66                                                                                                      IFPSLF                                            © SAP SE

Transaction                                                                                              Specs                       System-Example                         View
                                /BA1/HW_RESULTVIEWER                                                                                     SAFI                        DEMO01_LOAN_01
                                 - Ergebnisdaten anzeigen                                                                                _S_SCT_TVR
                                /BA1/HW_RESULTVIEWER                                                                                     SAFI                        DEMO01_LOAN_01
                                 - Ergebnisdaten anzeigen                                                                                _S_SCT_IMP


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                         133




Duplication is prohibited.                                                                                                                                                                                                                     Duplication is prohibited.
                                 Processes and Process Steps in FPSL – Accrue, Defer, Value TC

                                        Day Processing                                                         Intraday                                                          Security Positions

                                            Set Posting                          Register                     Register      Register                                    Define         Allocate       Determine        M&T
                                                                                                                                                     IAD
                                               Date                                MD                           BT            AD                                         Lots            Lots         Price Gain        BT

                                                                                                                                            Impairment Attribute
                                                                                                               Register                                                                   End-of-Day Process
                                                                                                                                              Determination


                                        Day-End Processing / Period-End Processing

                                                                                                          Write                            Value       Move and         Value                         Classify
                                                  Accrue                      Defer                                       Release                                                     Classify                        Adjust
                                                                                                          Down                              TC         Transform         FX                             P&L

                                                                                                                                                                                                                      Manual
                                                                                                                          Day-End Process / Period-End Process
                                                                                                                                                                                                                      Posting



                                        Period-End                              Year-End Processing                        Across                  Preparatory Processing
                                        Processing
                                                                                                                                                      Determine        Determine Amort.       Determine Adj.       Determine Fair
                                                Close                                   Carry Forward                         Allocate
                                                                                                                                                    Amortized Cost      Valuation Cost        for Credit Risk          Value

                                        Open and Close                           Balance Carry Forward
                                        Posting Periods                            (Cross/-Contract)

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                         134




                             © SAP SE                                                                                                              IFPSLF                                                                                 67

Transaction                                                                    Specs            System-Example   View/Variant
                                  BA1/BR_PERIOD_END_1                                                            DEMO01
                                  - Period-End Processing (Contract)                                             31.01.2018
                                                                                                                 Testrun
                                  BA1/BR_PERIOD_END_1                                                            DEMO01
                                  - Period-End Processing (Contract)                                             31.01.2018
                                  /BA1/BR_RESLT_VIEWER - Display Subledger                                       DEMO01           DEMO01_LOAN_01
                                  Documents
                                  /BA1/HW_RESULTVIEWER                                                           SAFI             DEMO01_LOAN_01
                                   - Ergebnisdaten anzeigen                                                      _S_SCT_TVAL


                                    © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                     135




Duplication is prohibited.                                                                                                                                                   Duplication is prohibited.


                                    Loan Period-End Processing
                                    Common Topics
                                    Theory




                             68                                                                                          IFPSLF                                   © SAP SE

Accounting Process Model and Book Value Components – Calculation Methods

                                 Day                                     Period-End Processing
                                 Processing




                                                                                                                                       Write
                                 Register                                          Accrue                         Defer                             Release                      Value TC
                                                                                                                                       down


                                                                                       Accruals                Deferrals
                                      Unpaid
                                                                                                                                   Write Down                                       Hedged
                                     Principle                                                                                                     Valuation
                                     Balance                                                                                                       Remnants                         financial Fair Value
                                                                                                                                                               Credit Risk Financial risks Adjustment
                                                                                                                                                                             risks


                                                                                                                           Amortized
                                                                                                                                                                                                      Fair Value
                                                                                                                             Cost



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                  137




Duplication is prohibited.                                                                                                                                                                                              Duplication is prohibited.
                                 Processes and Process Steps in FPSL – Methods


                                                                                                                           Methods
                                                                                                                                        Import
                                                                                                                       Exception Processing
                                                                                                                                   Parametric
                                                                                                              Cash-Flow-Based Determination
                                                                                                                Business Transaction-Based
                                                                                                                      Custom Determination

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                  138




                             © SAP SE                                                                                                     IFPSLF                                                                   69

Processes And Process Steps in FPSL – Universal Methods
                                                                                                                      Import
                                  ¾       Importing the target value into the RDL (_S_SCT_TVL / HKTVL)

                                  ¾       Delta of target value and existing balance is recognized as a subledger journal entry

                                  ¾       .                                                                    Exception Processing
                                  ¾       No further input parameters required other than the contractual information (e.g., lifecycle
                                          segment)

                                  ¾       Currently available methods as examples (not applicable for all use cases)
                                      ¾ Realization clears the existing balance
                                        (e.g., automatically executed if lifecycle segment is 40 = Contract End)
                                      ¾ Freeze keeps the existing balance

                                                                                                               Custom Determination
                                  ¾       Using client-specific methods for the determination of target values

                                  ¾       Implementation with Business Add Ins (BAdIs)
                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                      139




Duplication is prohibited.                                                                                                                                Duplication is prohibited.
                                  Processes and Process Steps in FPSL – Derivation of Methods
                                   Calculation methods are derived based on master
                                   data related characteristics




                                                                                                                                         Method
                                                                                                                                         derivation is
                                                                                                                                         accounting
                                                                                                                                         system
                                                                                                                                         dependent.




                                    Example




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                      140




                             70                                                                                            IFPSLF              © SAP SE

Quiz




                                       1.          Name 3 target values. Is their delivery optional or mandatory?

                                       2.          Which methods do you know for determining target values?




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER            141




Duplication is prohibited.                                                                                                        Duplication is prohibited.


                                 Loan Period-End Processing
                                 Process Step – Accrue
                                 Theory




                             © SAP SE                                                                         IFPSLF         71

Accounting Process Model and Book Value Components – Calculation Methods

                                  Day                                      Period-End Processing
                                  Processing




                                                                                                                                        Write
                                   Register                                          Accrue                        Defer                                        Release                      Value TC
                                                                                                                                        down


                                                                                         Accruals               Deferrals
                                        Unpaid
                                                                                                                                    Write Down                                                  Hedged
                                       Principle                                                                                                               Valuation
                                       Balance                                                                                                                 Remnants                         financial Fair Value
                                                                                                                                                                           Credit Risk Financial risks Adjustment
                                                                                                                                                                                         risks


                                                                                                                            Amortized
                                                                                                                                                                                                                  Fair Value
                                                                                                                              Cost



                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                               143




Duplication is prohibited.                                                                                                                                                                                                        Duplication is prohibited.
                                   Accrue – Definition and Example
                                           Definition                                                                                            Process step
                                           Accrual is the assignment of future expense or                                                        The Accrue process step is an operational process step in
                                           income to the appropriate period in which it is                                                       charge of documenting the changes in the value of the
                                           recognized.                                                                                           accrual for a specified posting date. To update the
                                                                                                                                                 accounting balance of an accrual, the system determines
                                                                                                                                                 the balance from the subledger Journal Entries on the
                                                                                                                                                 relevant subledger accounts (actual value) and compares
                                                                                                                                                 this to the imported target balance (target value). The
                                          Explanation
                                                                                                                                                 difference is documented as a subledger journal entry.
                                          The interest is recognized monthly throughout the
                                          life cycle of the time deposit. At the maturity date,
                                          the accruals are cleared by the payment of the total                                                  102
                                          interest amount by the counterpart.
                                                                                                                                                                                                  Accruals       Interest
                                                                                                                                                101
                                                                                                                                                                                                                 earned
                                                                                                                                                                                            Interest paid
                                                                                                                                                                           Accruals
                                                                                                                                                100
                                            Example – Time Deposit

                                                                                                                                                  Money Unit
                                            • Interest payment at maturity                                                                                                                                       Long Term
                                            • Term: 1 year                                                                                                                                                       Receivables
                                            • 100 MU paid into time deposit
                                            • Interest rate 12 % p.a.
                                            • Accruals = 1% p.m. = 1 MU per month
                                                                                                                                                                       1 month                 1 month          Value Date
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                               144




                             72                                                                                                            IFPSLF                                                                      © SAP SE

Accrue – Methods


                                                                                                                      Methods
                                                                                                                            Import
                                                                                                                     Exception Processing




                                                                                                                     Custom Determination

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                              145




Duplication is prohibited.                                                                                                                                          Duplication is prohibited.
                                 Accruals – Account Assignment




                                                                                                  Balance Sheet                        Profit and Loss

                                                                                                          Accruals                          Income



                                                                                                                                         Expenses




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                              146




                             © SAP SE                                                                                        IFPSLF                            73

Break (15min)




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                             147




Duplication is prohibited.                                                                                                                         Duplication is prohibited.
                                  Period-End Processing for Contracts – Remember Bus Motiv. Deferral

                                            At the end of the period the financial statement should reflect all financial
                                            aspects of the business as of the last day of the period. Purpose is to disclose
                                            transparency regarding the current business situation to all stakeholders (regulators,
                                            financial markets, business partner, investors).

                                            To achieve this, all components of the financial statement need to be updated to document

                                            •        All operational value flows

                                            •        All not completed income and efforts (accruals and deferral) need to
                                                     be distributed for the current period
                                            •        Risk provision needs to be calculated and updated in the balance sheet

                                            •        Valuation of all assets and obligations needs to be updated

                                            •        All relevant risks need to be reflected appropriately in the financial statement


                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                             148




                             74                                                                                     IFPSLF              © SAP SE

Loan Period-End Processing
                                 Process Step - Defer
                                 Theory




Duplication is prohibited.                                                                                                                                                                                             Duplication is prohibited.
                               Accounting Process Model and Book Value Components – Defer

                                 Day                                     Period-End Processing
                                 Processing




                                                                                                                                      Write
                                 Register                                          Accrue                        Defer                             Release                      Value TC
                                                                                                                                      down


                                                                                       Accruals               Deferrals
                                      Unpaid
                                                                                                                                  Write Down                                       Hedged
                                     Principle                                                                                                    Valuation
                                     Balance                                                                                                      Remnants                         financial Fair Value
                                                                                                                                                              Credit Risk Financial risks Adjustment
                                                                                                                                                                            risks


                                                                                                                          Amortized
                                                                                                                                                                                                     Fair Value
                                                                                                                            Cost



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                 150




                             © SAP SE                                                                                                    IFPSLF                                                                   75

Defer – Definition and Characteristics

                                             Definition                                                                        Process step
                                             Deferral is the assignment of already                                             The Defer process step is an analytical process step
                                             received expense or income to the                                                 with GAAP-dependent results that are documented
                                             appropriate period which is one of the key                                        as delta GAAP documents. Deferrals are calculated
                                             tasks of accounting.                                                              by the deferral calculator. The deferral calculator
                                             For this the Defer process step is crucial.                                       determines the deferral method based on the
                                                                                                                               accounting system.



                                             Responsibilities
                                             The Defer process step covers:
                                             1. Deferrals
                                             2. Non-Accrual Processing




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                     151




Duplication is prohibited.                                                                                                                                                                Duplication is prohibited.
                                  Defer – Methods


                                                                                                                    Methods
                                                                                                                          Import
                                                                                                                   Exception Processing


                                                                                                               Cash-Flow-Based Determination
                                                                                                                Business Transaction-Based
                                                                                                                   Custom Determination

                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                     152




                             76                                                                                            IFPSLF                                              © SAP SE

Deferral Methods – Cash-Flow-Based

                                      For Cash-Flow-Based deferrals, the deferral calculator applies the effective interest rate method to
                                      calculate the target value of the deferral based on the amortized cost. Three cash flow categories are
                                      supported:
                                      • Contract-related cash flow
                                      • Behavioral cash flow
                                      • Credit-risk-adjusted cash flow
                                      In this method, the deferral is the adjustment needed in the book value component in order to represent
                                      the amortized cost at a given period-end.

                                                    DEF =                                   AC                –        UPB              –         AI
                                                    Target                         Calculated by                   Determined by              Delivered to
                                                    Value                        deferral calculator              deferral calculator             RDL
                                                                                using the subledger                   using the
                                                                                  balances and/or                     subledger
                                                                                    cash flows                        balances


                                          DEF = amount of the Cash-Flow-Based Deferral item
                                          AC = Amortized Cost
                                          UPB = Unpaid Principal Balance
                                          AI = Accrued Interest
                                                                                                                   Result                   Book Value Component   UPB   Accrual   Deferral    Amortized
                                                                                                                                                                                                 Cost
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                153




Duplication is prohibited.                                                                                                                                                                                            Duplication is prohibited.
                                 Deferral Methods – Cash-Flow-Based                                                                                                                Deferral Calculator


                                     Key Figure Determination:
                                     During the Defer Process, the system determines the following key figures:

                                     1. Calculation of the Effective Interest Rate (EIR)

                                     2. Calculation of the Net Present Value (NPV): The value of the cash flow discounting by the EIR (reff) to
                                        the evaluation key date (t)

                                     3. Total amount of one-time effect (catch-up adjustment, minor modification), and the time effects for
                                        each accounting change

                                     4. The defer step considers total effects from payments with a value date that is before the evaluation key
                                        date but a due date that is after the evaluation key date




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                154




                             © SAP SE                                                                                                             IFPSLF                                                         77

Deferral Methods – Cash-Flow-Based                                                                                                  Deferral Calculator


                                      Effective Interest Rate (EIR)
                                      The initial EIR is calculated using the following conditional equation at time point t0 of the first payment:

                                                                                                               ܸܰܲ ‫ݐ‬଴ ൌ 0
                                      Net Present Value (NPV)
                                      The net present value (NPV) of a cash flow is determined by discounting the cash flow with the effective
                                      interest rate (reff) to the evaluation key date (t). For the determination of the net present value in End-of-
                                      Day and Period-End Processing, the evaluation key date is included in the calculation.
                                                                        Discrete Compounding                                               Continuous Compounding


                                                          ܸܰܲ ‫ ݐ‬ൌ ‫ ܸܣ‬ሺ1 ൅ ‫ݎ‬௘௙௙ ሻ௧                                                ܸܰܲ ‫ ݐ‬ൌ σ௧೔ஹ௧ ‫ܨܥ‬௜ ݁ ି௥೐೑೑ሺ௧೔ି௧ሻ
                                                                   where AV = Acquisition Value / Outstanding Principal
                                                                   reff = Effective Interest Rate
                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                             155




Duplication is prohibited.                                                                                                                                                                                       Duplication is prohibited.
                                  Deferral Method – Cash-Flow-Based

                                  Cash Flow Change

                                  If the cash flow changes at time t1, the system either calculates the one-time effect (CUA) or the
                                  EIR is recalculated (depending on Customizing).
                                          One-Time Effect (Catch-Up Adjustment, CUA)                                      Recalculation of EIR
                                          The one-time effect is calculated as the difference in
                                                                                                                                               ܸܰܲ௡௘௪ ‫ݐ‬ଵ ൌ ܸܰܲ௢௟ௗ ‫ݐ‬ଵ
                                          the present values of the old cash flow and the new
                                          cash flow while retaining the effective interest rate.
                                                                                                                          Cash Flow Change              Modification Type                 Optional

                                                                                                                           Valid-from and valid-to
                                                                                                                                                                   Rollover
                                                                                                                            date have changed
                                                               ‫ݐ ܣܷܥ‬ଵ ൌ ܸܰܲ௡௘௪ ‫ݐ‬ଵ െ ܸܰܲ௢௟ௗ ‫ݐ‬ଵ
                                                                                                                               Valid-from only               Condition change                 X

                                                                                                                              Date information          Another cash flow change
                                                                                                                                                                                              X
                                                                                                                                unchanged               (e.g. special repayment,...)



                                                                                                                          Remark: Classification if change is minor or major needs to be delivered to FPSL

                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                             156




                             78                                                                                      IFPSLF                                                                           © SAP SE

Deferral Methods – Cash-Flow-Based                                                                                                                        Deferral Calculator


                                       Distributing Deferrals to Subledger Accounts in proportion to the balances
                                       The calculator considers the distribution of the balances of the previous valuation, t1:
                                                                                                                                         where

                                                   ‫ܦ‬ଵ ൌ ‫ܣ‬ଵ ൅ ‫ܤ‬ଵ                                                D1: Balance of the Deferral at t1
                                                                                                              A1: Balance of the Account A at t1
                                                                                                              B1: Balance of the Account B at t1


                                       and determines the new account balances:
                                                                                                                                                                                                              where

                                                     ‫ܣ‬ଶ ൌ ‫ܣ‬ଵ ൅ ܽ ‫ܦ‬ଶ െ‫ܦ‬ଵ                                                                             D2 is the same definition of D1 in t2, the actual is ‫ܦ‬ଶ ൌ ‫ܣ‬ଶ ൅ ‫ܤ‬ଶ

                                                     ‫ܤ‬ଶ ൌ ‫ܤ‬ଵ ൅ 1 െ ܽ ‫ܦ‬ଶ െ‫ܦ‬ଵ                                                                                                         and             ܽൌ
                                                                                                                                                                                                            |‫ܣ‬ଵ |
                                                                                                                                                                                                          ‫ܣ‬ଵ ൅ |‫ܣ‬ଶ |

                                                 In order to ensure that the individual balances                                                                  ‫ݐ ݉݋ݎ݂ ݁݉݅ݐ‬ଶ ‫݀݋݅ݎ݁݌ ݀݁ݔ݂݅ ݂݋ ݀݊݁ ݈݅ݐ݊ݑ‬
                                                 approach zero at the end of the fixed period,                                                               ߬ൌ                                          ൏1
                                                                                                                                                                  ‫ݐ ݉݋ݎ݂ ݁݉݅ݐ‬ଵ ‫݀݋݅ݎ݁݌ ݀݁ݔ݂݅ ݂݋ ݀݊݁ ݈݅ݐ݊ݑ‬
                                                 they are multiplied by Ĳ.



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                             157




Duplication is prohibited.                                                                                                                                                                                                         Duplication is prohibited.
                                 Defer – Methods


                                                                                                                             Methods
                                                                                                                                            Import
                                                                                                                           Exception Processing


                                                                                                              Cash-Flow-Based Determination
                                                                                                                   Business Transaction-Based
                                                                                                                          Custom Determination

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                             158




                             © SAP SE                                                                                                          IFPSLF                                                                         79

Deferral Methods – Business Transaction-Based                                                                               Deferral Calculator


                                        Business Transaction-Based Deferrals
                                        The target value is calculated with the straight-line method at the granularity level of the individual
                                        business transaction. The deferral calculator aggregates the target value at contract level and transfers
                                        the aggregated target value to the defer process step.

                                                                                                                                                         where

                                                                                                                          ݇െ1            DEF = Deferral amount

                                                                                                               ‫ܨܧܦ‬௞ ൌ 1 െ     ‫ܨܧܦ כ‬௦              k = key date
                                                                                                                          ݁െ‫ݏ‬                     s = start date
                                                                                                                                                  e = end date


                                        The deferral period is determined by customizing:
                                                      • From the business transaction (imported from an external system): Value date as the start date and
                                                        the date from the calculate to characteristic (/BA1/C11CALCT) as the end date
                                                      • From the contract master data: Start and end of the fixed interest period or the contract term
                                                      • Accounting-based: Individually specifying a length and time unit

                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                         159




Duplication is prohibited.                                                                                                                                                                     Duplication is prohibited.
                                  Deferrals – Account Assignment




                                                                                                   Balance Sheet                       Profit and Loss

                                                                                                          Deferrals                        Income


                                                                                                                                         Expenses




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                         160




                             80                                                                                             IFPSLF                                                  © SAP SE

Loan Period-End Processing
                                 Process Step - Value TC (transaction currency)
                                 Theory




Duplication is prohibited.                                                                                                                                                                                             Duplication is prohibited.
                               Accounting Process Model and Book Value Components – Defer

                                 Day                                     Period-End Processing
                                 Processing




                                                                                                                                      Write
                                 Register                                          Accrue                        Defer                             Release                      Value TC
                                                                                                                                      down


                                                                                       Accruals               Deferrals
                                      Unpaid
                                                                                                                                  Write Down                                       Hedged
                                     Principle                                                                                                    Valuation
                                     Balance                                                                                                      Remnants                         financial Fair Value
                                                                                                                                                              Credit Risk Financial risks Adjustment
                                                                                                                                                                            risks


                                                                                                                          Amortized
                                                                                                                                                                                                     Fair Value
                                                                                                                            Cost



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                 162




                             © SAP SE                                                                                                    IFPSLF                                                                   81

Value TC – Definition and Characteristics


                                        Definition                                                                           Process step
                                        Value TC is an analytical step which is                                              Value TC calculates the target values or uses
                                        responsible for the documentation of changes                                         delivered target values. The Journal Entries are
                                        to the valuation of a position.                                                      created by determining the delta between current
                                                                                                                             balance and target value.



                                        The Value TC step tracks the following values:
                                                 •      Credit risk (Impairment)
                                                 •      Interest rate risk
                                                 •      Fair Value
                                                 •      Target value (after economic write down)



                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                     163




Duplication is prohibited.                                                                                                                                                                 Duplication is prohibited.
                                  Value TC – Methods


                                                                                                                    Methods
                                                                                                                          Import
                                                                                                                   Exception Processing
                                                                                                                        Parametric
                                                                                                               Cash-Flow-Based Determination


                                                                                                                   Custom Determination

                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                     164




                             82                                                                                            IFPSLF                                               © SAP SE

Break out session IFRS9                                                                                   Expected Credit Loss
                                                                                                                                             (IFRS9)
                                                                                                                                                                        5% or 0.05         Propability of Default (PD)
                                                                                                                                             Lifetime expected Credit                      provides an estimate of the
                                                                                                                                             Loss                                          likelihood that a borrower will
                                                                                                                                                                                           be unable to meet its debt
                                                                                                                             Incurred Loss
                                                                                                                                                                                           obligations (Default).
                              Amount
                              Expected
                              Credit
                              Loss
                                                                                                                                                                        100.000€           Exposure at Default (EAD)
                                                                                                                                                                                           Is an estimation of the extent
                                                                                                                                                                                           to which a bank may be
                                                                 Significant
                                                                 deterioration                                                                                                             exposed to a counterparty in
                                                                                                                                                                                           the event of, and at the time
                                                Stage 1                                                           Stage 2                    Stage 3                                       of, that counterparty’s
                                                „Performing“                                                      „Underperforming
                                                                                                                  “
                                                                                                                                             „Impaired“                                    default.

                                                                                                                                                                        10% or 0.1         Loss given Default (LGD)
                                                                                                                                                                                           is the share of an asset that is
                                                                                                                                                                                           lost if a borrower defaults.


                                                                                                                                                                        0.05x100.000       Expected Loss (EL)
                                                                                                                                                              Time t    x0.1 = 500€        is the sum of the values of all
                                                                                                                                                                                           possible losses, each
                                         1 yr parameter                              Lifetime parameter                              Lifetime parameter                                    multiplied by the probability of
                                                                                                                                                                                           that loss occurring.
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                            165




Duplication is prohibited.                                                                                                                                                                                                          Duplication is prohibited.
                                   Value TC – Credit Risk Adjustment



                                                                                                        Methods
                                                                                                                  Import                                                     One-year expected loss

                                                                                                                                                                             Lifetime expected loss
                                                                                               Exception Processing

                                                                                                                Parametric

                                                                                                                                                                             Expected Cash Flow
                                                                                Cash-Flow-Based Determination




                                                                                              Custom Determination


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                            166




                             © SAP SE                                                                                                                     IFPSLF                                                               83

Value TC – Credit Risk Adjustment
                                                                                                               Credit risk from …                               Own credit
                                                                                                                                                                 risk from…
                                                                                                                                         Short-Term
                                                                              Book Value                           Free Line                                    Book Value
                                                                                                                                         Receivables
                                                                                Imported target
                                                                                    value                          Imported target            Imported target
                                                                                                                       value                      value          Imported target
                                                                                                                                                                     value
                                                                                    One-year
                                                                                  expected loss
                                                                                                                     One-year                   One-year
                                                                                    Lifetime                       expected loss              expected loss
                                                                                  expected loss                                                                     Custom
                                                                                Expected cash                                                                    determination
                                                                                    flow                              Custom                     Custom
                                                                                                                   determination              determination
                                                                                     Custom
                                                                                  determination
                                                                                                                                                                   Exception
                                                                                                                     Exception                  Exception          processing
                                                                                     Exception                       processing                 processing
                                                                                     processing

                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                        167




Duplication is prohibited.                                                                                                                                                                    Duplication is prohibited.
                                  Value TC – Credit Risk Adjustment
                                                                                                               Credit risk from …                               Own credit
                                                                                                                                                                 risk from…
                                                                                                                                         Short-Term
                                                                              Book Value                           Free Line                                    Book Value
                                                                                                                                         Receivables
                                                                                Imported target
                                                                                    value                          Imported target            Imported target
                                                                                                                       value                      value          Imported target
                                                                                                                                                                     value
                                                                                    One-year
                                                                                  expected loss
                                                                                                                     One-year                   One-year
                                                                                    Lifetime                       expected loss              expected loss
                                                                                  expected loss                                                                     Custom
                                                                                Expected cash                                                                    determination
                                                                                    flow                              Custom                     Custom
                                                                                                                   determination              determination
                                                                                     Custom
                                                                                  determination
                                                                                                                                                                   Exception
                                                                                                                     Exception                  Exception          processing
                                                                                     Exception                       processing                 processing
                                                                                     processing

                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                        168




                             84                                                                                                      IFPSLF                                        © SAP SE

Value TC – Credit Risk Adjustment
                                                                                                              Credit risk from …                               Own credit
                                                                                                                                                                risk from…
                                                                                                                                        Short-Term
                                                                             Book Value                           Free Line                                    Book Value
                                                                                                                                        Receivables
                                                                               Imported target
                                                                                   value                          Imported target            Imported target
                                                                                                                      value                      value          Imported target
                                                                                                                                                                    value
                                                                                   One-year
                                                                                 expected loss
                                                                                                                    One-year                   One-year
                                                                                   Lifetime                       expected loss              expected loss
                                                                                 expected loss                                                                     Custom
                                                                               Expected cash                                                                    determination
                                                                                   flow                              Custom                     Custom
                                                                                                                  determination              determination
                                                                                    Custom
                                                                                 determination
                                                                                                                                                                  Exception
                                                                                                                    Exception                  Exception          processing
                                                                                    Exception                       processing                 processing
                                                                                    processing

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                       169




Duplication is prohibited.                                                                                                                                                                   Duplication is prohibited.
                                 Value TC – Credit Risk Adjustment
                                                                                                              Credit risk from …                               Own credit
                                                                                                                                                                risk from…
                                                                                                                                        Short-Term
                                                                             Book Value                           Free Line                                    Book Value
                                                                                                                                        Receivables
                                                                               Imported target
                                                                                   value                          Imported target            Imported target
                                                                                                                      value                      value          Imported target
                                                                                                                                                                    value
                                                                                   One-year
                                                                                 expected loss
                                                                                                                    One-year                   One-year
                                                                                   Lifetime                       expected loss              expected loss
                                                                                 expected loss                                                                     Custom
                                                                               Expected cash                                                                    determination
                                                                                   flow                              Custom                     Custom
                                                                                                                  determination              determination
                                                                                    Custom
                                                                                 determination
                                                                                                                                                                  Exception
                                                                                                                    Exception                  Exception          processing
                                                                                    Exception                       processing                 processing
                                                                                    processing

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                       170




                             © SAP SE                                                                                               IFPSLF                                              85

Value TC – Account Assignment




                                                                                                   Balance Sheet             Profit and Loss

                                                                                     Credit Risk Adjustment                     Income




                                                                                                                               Expense




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                    171




Duplication is prohibited.                                                                                                                                Duplication is prohibited.



                                                                                                               Break (15min)




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                    172




                             86                                                                                     IFPSLF                     © SAP SE

Loan Period-End Processing

                                 Hands On




Duplication is prohibited.                                                                                                                                                                     Duplication is prohibited.
                                                                                                                                                                Key Date Values
                                 Hands on – Data: Creating Your Own Data / Uploads                                                                              Calculation Rates
                                                                                                                                                                    & Factors
                                                                                                     Task                                               Transaction
                                         Create your Accruals and Risk Parameters by copying                                           SE38: /BA1/R_AL_HW_EXCEL_EXECUTE
                                         the data from:
                                         <test data directory>/LOAN01 test data/ ACC_LOAN01.csv
                                         <test data directory>/LOAN01 test data/ RP_LOAN01.csv


                                                                                  To be considered
                                        The following parameters need to be changed
                                        accordingly:                                                                                   a) Accruals
                                        1. External Number of your FT (1)
                                                                                                                                       b) Risk Parameters


                                                                                                              Choose path as shown to
                                                                                                              select your adapted .csv files




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                         174




                             © SAP SE                                                                                       IFPSLF                                                        87

Hands on – Data: Creating Your Own Data / Uploads
                                                                                                                                                                           Flow Data
                                                                                                        Task                                           Transaction
                                           Create your Cash Flow by copying the data from:
                                                                                                                                       SE38: /BA1/R_AL_HW_EXCEL_EXECUTE
                                           <test data directory>/LOAN01 test data/ CF_LOAN01.csv



                                                                                     To be considered
                                           The following parameters need to be changed
                                           accordingly:
                                           1. External Number of your FT (1)



                                                                                                                 Choose path as shown to
                                                                                                                 select your adapted .csv files




                                    © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                          175




Duplication is prohibited.                                                                                                                                                                        Duplication is prohibited.
                             DW17

                                                                                                                                                                 Key Date Values
                                    Hands on – Results: Check Uploads                                                                                            Calculation Rates
                                                                                                                                                                     & Factors


                                                                                               Task                                         SAP Menu Location & Transaction
                                             Check the uploaded data in the following                                           /BA1/HW_RESULTVIEWER - Display Results Data
                                             Result Views:
                                             a. Accruals: _S_SCT_TVR
                                             b. Risk Data: _S_SCT_IMP




                                                                             To be considered
                                            The following parameters must be
                                            considered:
                                            1. Legal Entity



                                    © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                          176




                             88                                                                                              IFPSLF                                                    © SAP SE

Hands on – Results: Journal Entries


                                                                                                    Task                              SAP Menu Location & Transaction
                                                                                                                     /BA1/BR_PERIOD_END_1 - Period-End Processing
                                          a.        Set the posting date for your Source
                                                                                                                     (Contract)
                                                    System
                                          b.        Execute the Register for your Source
                                                    System
                                          c.        Execute the End-of-Day (Contract) Process
                                          d.        Execute the Period-End (Contract) Process



                                                                                  To be considered
                                        The following parameters must be considered:
                                        1. Legal Entity
                                        2. Source System
                                        3. Posting Date
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                             177




Duplication is prohibited.                                                                                                                                                         Duplication is prohibited.
                                 Hands on – Period-End Processing (Contract)

                                                                               Enter parameters as requested




                                                                                                                  Your legal entity


                                                                                                                Your Source System
                                                                                                                    31.01.2019
                                                                                                                   31.01.2018




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                             178




                             © SAP SE                                                                          IFPSLF                                                         89

Hands on – Results: Journal Entries
                                                                                                                                                             Journal Entries

                                                                                                           Task                          To be considered
                                          Check the subledger Journal Entries with Result                                  The following parameters must be considered:
                                          View _S_SLPD.                                                                    1. Legal Entity (a.)


                                                                                    Selection Screen                             SAP Menu Location & Transaction
                                                                                                                      /BA1/BR_RESLT_VIEWER - Display Subledger Journal
                                                                                                                      Entries




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                               179




Duplication is prohibited.                                                                                                                                                         Duplication is prohibited.
                                  Hands on – Results: Additional Data
                                                                                                                                                            Additional Data

                                                                                                  Task                       SAP Menu Location & Transaction
                                           Check the additional information on master                               /BA1/HW_RESULTVIEWER - Display Results Data
                                           data: Analytical Status with Result View
                                           _S_SCT_STS.




                                                                               To be considered
                                          The following parameters must be
                                          considered:
                                          1. Legal Entity
                                          2. Mind the System Date (31.01.2018)!



                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                               180




                             90                                                                                   IFPSLF                                                © SAP SE

Lunch Break




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                 181




Duplication is prohibited.                                                                                                             Duplication is prohibited.
                                 Quiz




                                       1.          What is the responsibility of the ‘Accrue‘ step?

                                       2.          Which methods can you use for this step?

                                       3.          What is the responsibility of the ‘Defer‘ step?

                                       4.          Which methods can you use for this step?




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                 182




                             © SAP SE                                                                              IFPSLF         91

Agenda Part 2 – Loan Example

                                  1.          Introduction – Summary of part 1

                                  2.          Day Processing

                                  3.          Period-End Processing

                                  4.          Additional information on Day and Period-End Processing

                                  5.          Year End processing

                                  6.          Special Topics

                                  7.          Summary of Part 2




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                      183




Duplication is prohibited.                                                                                                                                                                                                 Duplication is prohibited.
                                  Example
                                                                                                                                                 Accounting Requirements
                                  Basic Data - Loan
                                                                                                                                                 •   31.01./ 31.03./ … :Periodic financial statement (monthly
                                  Maturity                                                       01.01.2018 – 01.01.2028 (10 Years)                  reporting)
                                                                                                                                                 •   31.03.18: Suspense Accounting due to missing derivation rule
                                  Nominal                                                        1 000 000 €                                     •   31.05.18: Change of organizational unit

                                  Discount                                                       10 000 €                                        •   30.09.18: Closing passed posting periods
                                                                                                                                                 •   01.10.18: Reversal of interest payment, correction
                                  Nominal Interest                                               1.2%                                            •   31.12.18: Manual Adjustment, Year-End Processing

                                  Interest Payment                                              Quarterly                                        •   31.05.19: Impairment Attribute Determination

                                  Repayment                                                     Half-yearly

                                                                                                                Suspense                                                                  Interest-
                                     Operational                                          Disburse-             Accounting
                                                                                                                               Change of       Interest-
                                                                                                                                                             Interest-                    Payment         Impairment
                                                                                                                             organizational    Payment                      Reversal
                                       Events                                               ment                 Interest-
                                                                                                                                 unit         Repayment
                                                                                                                                                             Payment                     Repayment        Write Down
                                                                                                                 Payment                                                                Manual Adjust.


                                                                                      01.01.2018 31.03.2018 31.05.2018 30.06.2018 30.09.2018                               10.2018       31.12.2018 31.05.2019


                                   FPSL System                                           Register
                                                                                                               Period End Period End Period End Period End                                Year End Period End
                                     Activities                                       End-of-day
                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                      184




                             92                                                                                                           IFPSLF                                                                © SAP SE

Agenda Part 2 – Additional Information on Day and Period-End Processing

                                                 Register – Suspense Accounting

                                                 Register – Reverse BT

                                                 Management of attribute changes

                                          –            End-of-Day Contract

                                          –            Classify

                                                 Period-End – Manual corrections (Adjust)




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                               185




Duplication is prohibited.                                                                                                                           Duplication is prohibited.
                                 Register Suspense Accounting – Business Motivation

                                           There will be always situations that input data can’t be completely processed for various
                                           reasons, but accounting needs …

                                           •        a complete balance sheet even if not all accounting logic can be derived / executed

                                           •        all amounts and operational flows represented completely in financial statement

                                           •        Restart capability to reprocess data that was handled by suspense accounting

                                           •        Complete transparency about amounts currently posted into suspense accounts,
                                                    indicating not correct data, to determine relevancy.

                                           Suspense accounting is using

                                           •        Suspense accounts and default values to ensure transparency

                                           •        Status on register tables and process controller for reprocessing


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                               186




                             © SAP SE                                                                         IFPSLF                            93

© 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER             187




Duplication is prohibited.                                                                                                         Duplication is prohibited.

                                  Loan Intraday Processing
                                  Register
                                  Special Topic Suspense Accounting
                                  Demo




                             94                                                                                IFPSLF   © SAP SE

Example
                                                                                                                                                           Accounting Requirements
                                Basic Data - Loan
                                                                                                                                                           •   31.01./ 31.03./ … :Periodic financial statement (monthly
                                Maturity                                                        01.01.2018 – 01.01.2028 (10 Years)                             reporting)
                                                                                                                                                           •   31.03.18: Suspense Accounting due to missing derivation rule
                                Nominal                                                         1 000 000 €                                                •   31.05.18: Change of organizational unit

                                Discount                                                        10 000 €                                                   •   30.09.18: Closing passed posting periods
                                                                                                                                                           •   01.10.18: Reversal of interest payment, correction
                                Nominal Interest                                                1.2%                                                       •   31.12.18: Manual Adjustment, Year-End Processing

                                Interest Payment                                               Quarterly                                                   •   31.05.19: Impairment Attribute Determination

                                Repayment                                                      Half-yearly

                                                                                                                    Suspense                                                                              Interest-
                                    Operational                                          Disburse-                  Accounting
                                                                                                                                      Change of         Interest-
                                                                                                                                                                       Interest-                          Payment          Impairment
                                                                                                                                    organizational      Payment                          Reversal
                                      Events                                               ment                      Interest-
                                                                                                                                        unit           Repayment
                                                                                                                                                                       Payment                           Repayment         Write Down
                                                                                                                     Payment                                                                            Manual Adjust.


                                                                                     01.01.2018 31.03.2018 31.05.2018 30.06.2018 30.09.2018                                              10.2018         31.12.2018 31.05.2019


                                  FPSL System                                           Register
                                                                                                                   Period End Period End Period End Period End                                            Year End Period End
                                    Activities                                       End-of-day
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                         189




Duplication is prohibited.                                                                                                                                                                                                                     Duplication is prohibited.
                                 Processes and Process Steps in FPSL – Close

                                        Day Processing                                                         Intraday                                                          Security Positions

                                            Set Posting                          Register                     Register      Register                                    Define         Allocate       Determine        M&T
                                                                                                                                                     IAD
                                               Date                                MD                           BT            AD                                         Lots            Lots         Price Gain        BT

                                                                                                                                            Impairment Attribute
                                                                                                               Register                                                                  End-of-Day Process
                                                                                                                                              Determination


                                        Day-End Processing / Period-End Processing

                                                                                                          Write                           Value         Move and       Value                          Classify
                                                  Accrue                      Defer                                       Release                                                     Classify                        Adjust
                                                                                                          Down                             TC           Transform       FX                              P&L

                                                                                                                                                                                                                      Manual
                                                                                                                          Day-End Process / Period-End Process
                                                                                                                                                                                                                      Posting



                                        Period-End                              Year-End Processing                        Across                 Preparatory Processing
                                        Processing
                                                                                                                                                       Determine      Determine Amort.        Determine Adj.       Determine Fair
                                                Close                                   Carry Forward                         Allocate
                                                                                                                                                     Amortized Cost    Valuation Cost         for Credit Risk          Value

                                        Open and Close                           Balance Carry Forward
                                        Posting Periods                            (Cross/-Contract)

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                         190




                             © SAP SE                                                                                                             IFPSLF                                                                                  95

Transaction                                                                    Specs             System-Example        View/Variant
                                  /BA1/F2_BT_COPY                                                                BT:               BT:
                                   - Create Business Transaction by Copying                                      Demo_01_LOAN_01   LOAN_01_INT_1803_01
                                                                                                                 _INT_1803_01
                                  /BA1/BR_SET_POST_DAT                                                           DEMO01
                                   - Set Posting Date
                                                                                                                 31.03.2018
                                  /BA1/BR_REGISTER                                                               DEMO01
                                   - Register
                                  /BA1/BR_RESLT_VIEWER                                                                             DEMO01_LOAN_01
                                   - Nebenbuchbelege anzeigen
                                  Fix deleted rules in customizing
                                  /BA1/BR_REGISTER                                                               DEMO01
                                   - Register
                                  /BA1/BR_RESLT_VIEWER                                                                             DEMO01_LOAN_01
                                   - Nebenbuchbelege anzeigen
                                    © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                           191




Duplication is prohibited.                                                                                                                                                         Duplication is prohibited.




                                    © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                           192




                             96                                                                                          IFPSLF                                         © SAP SE

© 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER            193




Duplication is prohibited.                                                                                                        Duplication is prohibited.

                                 Loan Intraday Processing
                                 Register
                                 Special Topic Suspense Accounting
                                 Theory




                             © SAP SE                                                                         IFPSLF         97

Suspense Accounting Functionality


                                  FPSL provides the functionality of Suspense Accounting. In this way inaccurate input data and
                                  subledger configuration can be managed in order to ensure the principle of completeness.
                                      Possible scenarios
                                      It’s not possible to determine
                                      1. the subledger accounts
                                      2. other dimensions of the subledger
                                           coding block
                                                                                                               Subledger
                                                                                                                Account
                                                                                                                                                                    SUSPENSE
                                                                                                                      Subledger
                                                                                                                       Account
                                                                                                                                                                    ACCOUNTS
                                                                                     Subledger
                                                                                    Coding Block
                                                                                                               Subledger
                                                                                                                Account




                                                                                 Determination of the subledger account
                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                     195




Duplication is prohibited.                                                                                                                                                                               Duplication is prohibited.
                                  Suspense Accounting in FPSL – Subledger Account Derivation
                                                                                                                                                                          For the complete
                                                                                                                                                                          documentation of the
                                    Scenario 1:                                                                                                                           imported flow transactions
                                    It is not possible to determine one or                                                                                                a temporary journal entry
                                    both Subledger Account(s).                                                             Register       End-of-day   Period end         (defined as an error value)
                                                                                                                                          processing   processing         is assigned.


                                                     Journal                                                         Operational Data
                                                     Entries
                                                                                                                                                                        The process will display a
                                                                                                                                                                        warning message for the
                                                 Subledger                                                                                                    Suspense
                                                                                                                                                                        Suspense Accounting
                                                 Account 1                                                                                                    Account 1


                                                                                      Derivation                        Subledger
                                                   Subledger                                                           Coding Block                           Suspense
                                                   Account 2                                                                                                  Account 2
                                                                                                                     (Subledger Account
                                                                                                                        Assignment)



                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                     196




                             98                                                                                                       IFPSLF                                                  © SAP SE

Suspense Accounting in FPSL – Subledger Coding Block Dimension


                                   Scenario 2:
                                   It is not possible to determine a
                                   Subledger Coding Block Dimension.                                                        Register         End-of-day        Period end       For all characteristics in the
                                                                                                                                             processing        processing       Subledger Coding Block, you
                                                                                                                                                                                can also define error values.
                                   For the complete
                                                                                                               Journal                           Operational Data
                                   documentation of the
                                                                                                               Entries
                                   imported flow transactions
                                   a temporary journal entry
                                   (defined as an error value)                                                Subledger                                                                          Suspense
                                   is assigned.                                                               Account 1                                                                          Account 1


                                                                                                                           Derivation                 Subledger
                                                                                                              Subledger                              Coding Block                                 Suspense
                                 The process will display a                                                   Account 2                                                                           Account 2
                                 warning message for the                                                                                         (Subledger Account
                                 Suspense Accounting                                                                                                Assignment)



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                      197




Duplication is prohibited.                                                                                                                                                                                                  Duplication is prohibited.
                                 Suspense Accounting in FPSL – The Solution
                                                                                                                                          Register          End-of-day      Period end
                                  Once the configuration is fixed, the intraday                                                                             processing      processing
                                  process will detect automatically the change,
                                  reverse the Journal Entries of the Suspense
                                  Account and post the records in the correct                                                           Worklist with
                                  subledger account.                                                                                     Suspense
                                                                                                                                         Accounting
                                                                                                                                        Transactions

                                                                              1. Create Journal Entries                                                               2. Reversal of Suspense
                                                                                                                                                                      Account Journal Entries
                                                                                     Subledger                                                                                       Suspense
                                                                                     Account 1                                                                                       Account 1

                                                                                                                                         Subledger
                                                                                                                   Derivation           Coding Block
                                                                                       Subledger                                                                                         Suspense
                                                                                       Account 2                                       (Subledger Account                                Account 2
                                                                                                                                          Assignment)



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                      198




                             © SAP SE                                                                                                   IFPSLF                                                                         99

Agenda Part 2 – Additional Information on Day and Period-End Processing

                                                   Register – Suspense Accounting

                                                   Management of attribute changes

                                            –            End-of-Day Processing (Contract)

                                            –            Classify

                                                   Register – Reverse BT

                                                   Period-End – Manual corrections (Adjust)




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER             199




Duplication is prohibited.                                                                                                          Duplication is prohibited.

                                   Loan End-of-Day
                                   End-of-Day Processing (Contract)
                                   Special Topic Management of Attribute Changes
                                   Demo




                             100                                                                                IFPSLF   © SAP SE
