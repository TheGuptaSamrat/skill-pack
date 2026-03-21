Classification: training-derived-concepts
Source basis: FPSL TRAINING DOCUMENT.pdf, pages 150-180
Trust usage: bond accounting concepts, fair value vs. amortized cost, IFRS 9 classification
Do not use for: production valuation models
Topics covered: bond accounting, fair value, amortized cost, IFRS 9, financial instruments

# Bond Example - Basic Valuation
Agenda Part 3 – Accounting for Securities - Bond Example

                                   1.          Introduction – Summary of previous day

                                   2.          Bond Example 1 – Purchase & Sale

                                   3.          Bond Example 2 – Foreign Currency and Other Comprehensive Income with Recycling

                                   4.          Bond Example 3 – Extended Accounting Logic

                                   5.          Summary of Part 3




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                     299




Duplication is prohibited.                                                                                                                  Duplication is prohibited.




                                   Summary Accounting for Contracts




                             150                                                                                IFPSLF           © SAP SE

Recap / Intro


                                       ¾         Processes and process steps in FPSL

                                       ¾         Loan example at amortized cost

                                       ¾         Master data / flow data / key date values

                                       ¾         Day processing (intraday /day-end) Æ posting documents

                                       ¾         Period-end processing (accrue / defer / value TC)

                                       ¾         Period close




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                           301




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




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                           302




                             © SAP SE                                                                                               IFPSLF                                                  151

Processes and Process Steps in FPSL

                                          Day Processing                                                         Intraday                                                      Security Positions

                                              Set Posting                          Register                     Register      Register                                Define         Allocate       Determine       M&T *
                                                                                                                                                     IAD
                                                 Date                                MD                           BT            AD                                     Lots            Lots         Price Gain       BT

                                                                                                                                            Impairment Attribute
                                                                                                                 Register                                                               End-of-Day Process
                                                                                                                                              Determination


                                          Day-End Processing / Period-End Processing

                                                                                                            Write                          Value       Move and       Value                         Classify
                                                    Accrue                      Defer                                       Release                                                 Classify                        Adjust
                                                                                                            Down                            TC         Transform       FX                             P&L

                                                                                                                                                                                                                    Manual
                                                                                                                            Day-End Process / Period-End Process
                                                                                                                                                                                                                    Posting



                                          Period-End                              Year-End Processing                        Across                Preparatory Processing
                                          Processing
                                                                                                                                                      Determine      Determine Amort.       Determine Adj.       Determine Fair
                                                  Close                                   Carry Forward                         Allocate
                                                                                                                                                    Amortized Cost    Valuation Cost        for Credit Risk          Value

                                          Open and Close                           Balance Carry Forward
                                          Posting Periods                            (Cross/-Contract)


                                                                                                                                                                                         *M&T abbreviation for „Move and Transform“ 303
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER




Duplication is prohibited.                                                                                                                                                                                                                   Duplication is prohibited.


                                   Bond Example 1
                                   Purchase and Sale
                                   Overview




                             152                                                                                                                   IFPSLF                                                                         © SAP SE

Bond Example 1 – Purchase and Sale – Life Cycle
                                Basic Data - Security Information                                                                                 Accounting Requirements
                                Maturity                                         30.09.2018 – 30.09.2028 (10 Years)                               •    Applying FVTPL valuation approach
                                Issue Amount                                     1.000.000 € (complete bond issued)                               •    Periodic financial statement (monthly reporting
                                Nominal Amount                                   1000 €                                                                31.01. / 28.02. / 31.03. / …)

                                Nominal Interest                                 3.6 % (30/360)
                                                                                                                                                  •    Recognition of price gain on lot level
                                                                                                                                                  •    Recognition of accrued interest
                                Interest Payment                                Half-yearly

                                Flow Data                                                    Purchase               Purchase         Sale

                                Date                                                 02.01.2019                   03.02.2019     30.06.2019
                                Nominal Amount                                       200.000 €                    300.000 €      350.000 €
                                Position Amount                                      200.000 €                    300.000 €      365.000 €
                                Accrued interest                                     1.820 €                      3.660 €        3.150 €
                                                                                                              Purchase,                     2nd Purchase,
                                     Operational                                                                                                                Interest
                                                                                                              Accrued                         Accrued                                         Sale
                                       Events                                                                                                                   Payment
                                                                                                               Interest                        Interest
                                                                            30.09.2018                        02.01.2019       31.01.2019 03.02.2019            31.03.2019                30.06.2019


                                  FPSL System                                                                  Register                        Register
                                                                                                                               Period-End*                    Period-End*                 Period-End*
                                    Activities                                                                End-of-Day                      End-of-Day
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                             305
                                                                                                                                                                                 * Period-End includes Day Processing




Duplication is prohibited.                                                                                                                                                                                                          Duplication is prohibited.
                                 Example – Cash Flow

                                       CF Item
                                                                                Key Date                          Cal Fr.            Cal To           Nom. Amount            Amount             Currency
                                       Category

                                            Issued                           30.09.2018                                                                1 000 000.00 -1 000 000.00                  EUR

                                  Interest Value 31.03.2019                                                     01.10.2018         31.03.2019          1 000 000.00           18 000.00            EUR

                                  Interest Value 30.09.2019                                                     01.04.2019         30.09.2019          1 000 000.00           18 000.00            EUR

                                  Interest Value 31.03.2020                                                     01.10.2019         31.03.2020          1 000 000.00           18 000.00            EUR

                                  Interest Value 30.09.2020                                                     01.04.2020         30.09.2020          1 000 000.00           18 000.00            EUR

                                  Interest Value                                          …                          …                  …                   …                 18 000.00            EUR

                                     Repayment                               30.09.2028                                                                1 000 000.00        1 000 000.00            EUR

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                             306




                             © SAP SE                                                                                                       IFPSLF                                                                            153

Accounting for Securities – Relevant Process Steps

                                          Day Processing                                                         Intraday                                                      Security Positions

                                              Set Posting                          Register                     Register      Register                                Define         Allocate       Determine        M&T *
                                                                                                                                                     IAD
                                                 Date                                MD                           BT            AD                                     Lots            Lots         Price Gain        BT

                                                                                                                                            Impairment Attribute
                                                                                                                 Register                                                               End-of-Day Process
                                                                                                                                              Determination


                                          Day-End Processing / Period-End Processing

                                                                                                            Write                          Value       Move and       Value                         Classify
                                                    Accrue                      Defer                                       Release                                                 Classify                         Adjust
                                                                                                            Down                            TC         Transform       FX                             P&L

                                                                                                                                                                                                                     Manual
                                                                                                                            Day-End Process / Period-End Process
                                                                                                                                                                                                                     Posting



                                          Period-End                              Year-End Processing                        Across                Preparatory Processing
                                          Processing
                                                                                                                                                      Determine      Determine Amort.       Determine Adj.       Determine Fair
                                                  Close                                   Carry Forward                         Allocate
                                                                                                                                                    Amortized Cost    Valuation Cost        for Credit Risk          Value

                                          Open and Close                           Balance Carry Forward
                                          Posting Periods                            (Cross/-Contract)

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                           307
                                                                                                                                                                                           *M&T abbreviation for „Move and Transform“




Duplication is prohibited.                                                                                                                                                                                                                    Duplication is prohibited.


                                   Bond Data Creation

                                   Demo




                             154                                                                                                                   IFPSLF                                                                         © SAP SE

Bond Example 1 – Purchase and Sale – Life Cycle
                                Basic Data - Security Information                                                                                 Accounting Requirements
                                Maturity                                         30.09.2018 – 30.09.2028 (10 Years)                               •   Applying FVTPL valuation approach
                                Issue Amount                                     1.000.000 € (complete bond issued)                               •   Periodic financial statement (monthly reporting 31.01.
                                Nominal Amount                                   1000 €                                                               / 28.02. / 31.03. / …)

                                Nominal Interest                                 3.6 % (30/360)
                                                                                                                                                  •   Recognition of price gain on lot level
                                                                                                                                                  •   Recognition of accrued interest
                                Interest Payment                                Half-yearly

                                Flow Data                                                    Purchase               Purchase         Sale

                                Date                                                 02.01.2019                   03.02.2019     30.06.2019
                                Nominal Amount                                       200.000 €                    300.000 €      350.000 €
                                Position Amount                                      200.000 €                    300.000 €      365.000 €
                                Accrued interest                                     1.820 €                      3.660 €        3.150 €
                                                                                                              Purchase,                     2nd Purchase,
                                     Operational                                                                                                               Interest
                                                                                                              Accrued                         Accrued                                        Sale
                                       Events                                                                                                                  Payment
                                                                                                               Interest                        Interest
                                                                            30.09.2018                        02.01.2019       31.01.2019 03.02.2019          31.03.2019                 30.06.2019


                                  FPSL System                                                                  Register                        Register
                                                                                                                               Period-End*                    Period-End*                Period-End*
                                    Activities                                                                End-of-Day                      End-of-Day
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                            309
                                                                                                                                                                                * Period-End includes Day Processing




Duplication is prohibited.                                                                                                                                                                                                         Duplication is prohibited.
                                 Data Model – Master Data (Securities)

                                                      Master Data                                                    Additional                        Flow Data                  Key Date Values
                                                                                                                  Information on
                                              Contract                                                             Master Data
                                                                              Business                                                           Business                         Target
                                              Security                                                                                                         Cash Flow
                                                                               Partner                          Analytical                      Transaction                       Values
                                            Securities                                                           Status
                                                                               Portfolio
                                             Account




                                                                                Calculation Rates                                 Journal Entries                   Market Data
                                                                                  and Factors
                                                                                                                                Subledger Journal Entry
                                                                                             Impairment
                                                                                              Attributes




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                            310




                             © SAP SE                                                                                                       IFPSLF                                                                           155

Master Data – Security

                                                       1. Security – Basic Data




                                                      2. A look into the system
                                                      /BA1/F1_CF_01_03 - Display Securities

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER             311




Duplication is prohibited.                                                                                                          Duplication is prohibited.
                                   Master Data – Security

                                                       1. Security – Instrument Data




                                                      2. A look into the system
                                                      /BA1/F1_CF_01_03 - Display Securities

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER             312




                             156                                                                                IFPSLF   © SAP SE

Flow Data – Cash Flow

                                       1. Flow Data – Cash Flow




                                      2. A look into the system
                                      /BA1/HW_RESULTVIEWER - Display Results Data
                                      Result Area / Result View: SAFI / S_CF
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                         313




Duplication is prohibited.                                                                                                                                                      Duplication is prohibited.
                                 Master Data – Securities Account

                                                     1. Securities Account – General Data
                                                                                                                                   Account Status
                                                                                                                                         Active
                                                                                                                                        Inactive

                                                                                                                                 Organizational Unit


                                                                                                                            Securities Account Category
                                                                                                                       1.    Proprietary trading securities
                                                                                                                             account
                                                                                                                       2.    Issuance securities account
                                                                                                                       3.    Lending securities account
                                                                                                                       4.    Investment securities account
                                                                                                                       5.    Assets held for sale
                                                                                                                       Initial classification can be derived from
                                                   2. A look into the system                                           category depending on accounting system
                                                   /BA1/F1_ACC_03 - Display Securities Account

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                         314




                             © SAP SE                                                                         IFPSLF                                                      157

Data Model – Flow Data

                                                        Master Data                                                  Additional                  Flow Data              Key Date Values
                                                                                                                  Information on
                                                Contract                                                           Master Data
                                                                                Business                                                    Business                    Target
                                                Security                                                                                                 Cash Flow
                                                                                 Partner                        Analytical                 Transaction                  Values
                                              Securities                                                         Status
                                                                                 Portfolio
                                               Account




                                                                                  Calculation Rates                            Journal Entries               Market Data
                                                                                    and Factors
                                                                                                                             Subledger Journal Entry
                                                                                               Impairment
                                                                                                Attributes




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                  315




Duplication is prohibited.                                                                                                                                                                             Duplication is prohibited.
                                   Flow Data – Business Transaction
                                             1. Flow Data – Business Transaction - Header Data




                                                                                                                                                                           Trade Date
                                                                                                                                                                Represented by posting date of the
                                                                                                                                                                          transaction

                                                                                                                                                                        Settlement Date
                                                                                                                                                                 Represented by value date of the
                                                                                                                                                                           transaction


                                             2. A look into the system
                                             /BA1/F2_BT_SHOW - Display Business Transaction

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                  316




                             158                                                                                                      IFPSLF                                                © SAP SE

Flow Data – Business Transaction
                                           1. Flow Data – Business Transaction - Item Data




                                                                                                                                   Purchase:
                                                                                                                          Transaction type "SC1000"
                                                                                                                              Posting direction "D"




                                           2. A look into the system
                                           /BA1/F2_BT_SHOW - Display Business Transaction

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                           317




Duplication is prohibited.                                                                                                                                        Duplication is prohibited.
                                 Flow Data – Business Transaction
                                           1. Flow Data – Business Transaction - Item Data




                                                                                                                           Accrued Interest:
                                                                                                                       Transaction type "SC8702"
                                                                                                                          Posting direction "C"




                                           2. A look into the system
                                           /BA1/F2_BT_SHOW - Display Business Transaction

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                           318




                             © SAP SE                                                                         IFPSLF                                        159

Data Creation and Upload
                                                        Check FI
                                                        Check Account
                                                        Check SDL (BT)


                                                        Check the uploaded data in
                                                        SAFI ->
                                                        S_CF (Cash Flow)


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER             319




Duplication is prohibited.                                                                                                          Duplication is prohibited.


                                   Bond Data Creation

                                   Hands On




                             160                                                                                IFPSLF   © SAP SE

Hands On – Data: Creating Your Own Data 1
                                                                                                                                                       Master Data


                                                                                            Task                           Application Menu & Transaction
                                         a. Create your own Security by copying the                             a. /BA1/F1_CF_01_04 - Create Securities by Copying
                                            data from
                                             DEMO_04_BOND_01_FV
                                         b. Create your own Securities Account by
                                            copying the data from
                                            DEMO_04_BOND_01_SECACC

                                                                                                                b. /BA1/F1_ACC_04 - Create Securities Account by Copying

                                                                          To be considered
                                         The following parameters need to be changed
                                         accordingly:
                                         1. Source System (a./b.)
                                         2. Legal Entity (b.)



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                            321




Duplication is prohibited.                                                                                                                                                         Duplication is prohibited.
                                 Hands On – Data: Creating Your Own Data 2
                                                                                                                                                        Master Data


                                       1. Security: Source System                                                2. Securities Account: Source System / Legal Entity




                                    External Number is the individual number that you have
                                    assigned to your Security and your Securities Account.


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                            322




                             © SAP SE                                                                         IFPSLF                                                         161

Hands On – Data: Creating Your Own Data 3
                                                                                                                                                       Flow Data


                                                                                              Task                          Application Menu & Transaction
                                           Create your own Business Transaction by
                                           copying the data from
                                           DEMO_04_BOND_01_PUR_1901




                                                                              To be considered
                                           The following parameters need to be changed
                                           accordingly:
                                           1. Source System (BT)
                                           2. External Number of your Security and your
                                              Securities Account


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                       323




Duplication is prohibited.                                                                                                                                                    Duplication is prohibited.
                                   Hands On – Data: Creating Your Own Data 4                                                                           Flow Data

                                           1. Source System on Header                                                2. Account Number and External Number




                                          External Number is the individual number that you
                                          have assigned to your Security.
                                          The Account Number is the individual number that
                                          you have assigned to your Securities Account.


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                       324




                             162                                                                                IFPSLF                                             © SAP SE

Hands On – Data: Creating Your Own Data 5                                                                                          Flow Data


                                                                                                     Task                                         Calling upload report
                                                                                                                            SE38: /BA1/R_AL_HW_EXCEL_EXECUTE
                                         Create your Cash Flow by copying the data from:
                                         <test data directory>/bond01 test data/ CF_BOND01.csv
                                                                                                                            -   Call transaction SE38


                                         Check uploaded CF in RDL                                                           -   Start report
                                                                                                                                /BA1/R_AL_HW_EXCEL_EXECUTE
                                         /BA1/HW_RESULTVIEWER - Display Results Data
                                         Result Area / Result View: SAFI / S_CF

                                                                                                                            -   Choose option “Create
                                                                                                                                Results”
                                                                                  To be considered
                                        The following parameters need to be changed
                                        accordingly:                                                                        -   Choose path as shown to
                                        1. External Number of your security (1)                                                 select your adapted .csv
                                                                                                                                files




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                     325




Duplication is prohibited.                                                                                                                                                                  Duplication is prohibited.



                                                                                                              Break (15min)




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                     326




                             © SAP SE                                                                              IFPSLF                                                             163

Securities Intraday Processing
                                   Set Posting Date & Register
                                   Business Context




Duplication is prohibited.                                                                                                                                                    Duplication is prohibited.
                                   Intraday Processing – Business Problem to be solved



                                            Step: Set Posting Date
                                                 •        Not different from contract scenario, just ensuring that data is processed only to a specific point in
                                                          time

                                            Step: Register
                                                 •        Recognizing the value flows attached to purchase and selling of securities
                                                 •        Long and short positions need to be build (on security account level)
                                                 •        Reclassification of positions due to master data changes since security data is not provided from
                                                          trading systems, but by financial markets and is not changing frequently
                                                 •        Managing the situation of potential accrued interest which is included in the paid price (dirty price
                                                          = clean price + interest), when purchasing a bond




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                       328




                             164                                                                                IFPSLF                                             © SAP SE

Bond Example 1 – Purchase and Sale – Life Cycle
                                Basic Data - Security Information                                                                                            Accounting Requirements
                                Maturity                                         30.09.2018 – 30.09.2028 (10 Years)                                          •   Applying FVTPL valuation approach
                                Issue Amount                                     1.000.000 € (complete bond issued)                                          •   Periodic financial statement (monthly reporting
                                Nominal Amount                                   1000 €                                                                          31.01. / 28.02. / 31.03. / …)

                                Nominal Interest                                 3.6 % (30/360)
                                                                                                                                                             •   Recognition of price gain on lot level
                                                                                                                                                             •   Recognition of accrued interest
                                Interest Payment                                Half-yearly

                                Flow Data                                                    Purchase                     Purchase          Sale

                                Date                                                 02.01.2019                          03.02.2019      30.06.2019
                                Nominal Amount                                       200.000 €                           300.000 €       350.000 €
                                Position Amount                                      200.000 €                           300.000 €       365.000 €
                                Accrued interest                                     1.820 €                             3.660 €         3.150 €
                                                                                                                Purchase,                           2nd Purchase,
                                     Operational                                                                                                                          Interest
                                                                                                                Accrued                               Accrued                                                     Sale
                                       Events                                                                                                                             Payment
                                                                                                                 Interest                              Interest
                                                                            30.09.2018                         02.01.2019             31.01.2019 03.02.2019              31.03.2019                        30.06.2019


                                  FPSL System                                                                    Register                              Register
                                                                                                                                      Period-End*                       Period-End*                        Period-End*
                                    Activities                                                                 End-of-Day                             End-of-Day
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                               329
                                                                                                                                                                                                  * Period-End includes Day Processing




Duplication is prohibited.                                                                                                                                                                                                                            Duplication is prohibited.
                                 Accounting for Securities – Relevant Process Steps

                                        Day Processing                                                         Intraday                                                          Security Positions

                                            Set Posting                          Register                     Register        Register                                  Define         Allocate       Determine          M&T *
                                                                                                                                                      IAD
                                               Date                                MD                           BT              AD                                       Lots            Lots         Price Gain          BT

                                                                                                                                             Impairment Attribute
                                                                                                               Register                                                                   End-of-Day Process
                                                                                                                                               Determination


                                        Day-End Processing / Period-End Processing

                                                                                                          Write                             Value        Move and       Value                          Classify
                                                  Accrue                      Defer                                         Release                                                   Classify                           Adjust
                                                                                                          Down                               TC          Transform       FX                              P&L

                                                                                                                                                                                                                         Manual
                                                                                                                            Day-End Process / Period-End Process
                                                                                                                                                                                                                         Posting



                                        Period-End                              Year-End Processing                          Across                 Preparatory Processing
                                        Processing
                                                                                                                                                        Determine      Determine Amort.       Determine Adj.        Determine Fair
                                                Close                                   Carry Forward                           Allocate
                                                                                                                                                      Amortized Cost    Valuation Cost        for Credit Risk           Value

                                        Open and Close                           Balance Carry Forward
                                        Posting Periods                            (Cross/-Contract)

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                               330
                                                                                                                                                                                             *M&T abbreviation for „Move and Transform“




                             © SAP SE                                                                                                               IFPSLF                                                                                      165

Bond Intraday Processing
                                   Set Posting Date & Register
                                   Demo




Duplication is prohibited.                                                                                                                                                                         Duplication is prohibited.
                                   Data Model – Journal Entries

                                                        Master Data                                                  Additional                  Flow Data            Key Date Values
                                                                                                                  Information on
                                                Contract                                                           Master Data
                                                                                Business                                                    Business                  Target
                                                Security                                                                                                 Cash Flow
                                                                                 Partner                        Analytical                 Transaction                Values
                                              Securities                                                         Status
                                                                                 Portfolio
                                               Account




                                                                                  Calculation Rates                            Journal Entries               Market Data
                                                                                    and Factors
                                                                                                                             Subledger Journal Entry
                                                                                               Impairment
                                                                                                Attributes




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                            332




                             166                                                                                                      IFPSLF                                            © SAP SE

Show the intraday processing in the
                                                                                                              system
                                                                                                              + Results
                                                                                                              -> Postings
                                                                                                                   • Posting of price
                                                                                                                   • Posting interest accrued
                                                                                                                   • Posting of the bond nominal
                                                                                                              • Analytical status
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                         333




Duplication is prohibited.                                                                                                                                      Duplication is prohibited.


                                 Bond Intraday Processing
                                 Set Posting Date & Register
                                 Hands On




                             © SAP SE                                                                                    IFPSLF                           167

Hands On – Register: Day Processing

                                                                                              Task                          Application Menu & Transaction
                                            a. Set Posting Date for your Source                                   a) /BA1/BR_SET_POST_DAT - Set Posting Date
                                               System                                                             b) /BA1/BR_REGISTER - Register
                                            b. Execute the Register for your Source
                                               System




                                                                            To be considered
                                           The following parameters must be
                                           considered:
                                           1. Source System (a./b.)
                                           2. Posting Date (a.)


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                         335




Duplication is prohibited.                                                                                                                                                      Duplication is prohibited.
                                   Hands On – Results: Journal Entries
                                                                                                                                                   Journal Entries


                                                                                                       Task                     Application Menu & Transaction

                                           Check the subledger documents                                             /BA1/BR_RESLT_VIEWER - Display Subledger Documents




                                                                                    To be considered                                  Selection screen
                                          The following parameters must be considered:
                                          1. Legal Entity




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                         336




                             168                                                                                IFPSLF                                               © SAP SE

Hands On – Results: Additional Data
                                                                                                                                               Additional Data


                                                                                            Task                          Application Menu & Transaction
                                       Check the additional information on master                               /BA1/HW_RESULTVIEWER - Display Results Data
                                       data: Analytical Status
                                       with the result view _S_SCT_STS
                                       (Classification, Impairment Status, Write
                                       Down Status, Accrual Status, Fair Value
                                       Level)


                                                                          To be considered                                        Selection screen
                                       The following parameters must be
                                       considered:
                                       1. Legal Entity
                                       2. Mind the System Date!
                                       3. Two-dimensional versioning

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                      337




Duplication is prohibited.                                                                                                                                                   Duplication is prohibited.


                                 End-of-Day Processing for Securities
                                 Business Transaction
                                 Business Context




                             © SAP SE                                                                         IFPSLF                                                   169

End-of-Day (BT) Processing – Business Problem to be solved



                                            While new incoming data can be processed by registering instantly, there are some tasks
                                            which can only be applied on a day-end basis to create a consistent status:

                                            •         Fixing of operational value flows in foreign currencies (same as for loans)

                                            Specific challenge for securities:
                                                 •        Depending on chosen price gain determination method (no price gain calculation, average price
                                                          gain,…) an additional granularity for positions needs to be used.
                                                          If each single price of position change needs to be documented, granularity needs to be each
                                                          single transaction building up a position (long or short position). This is called lot accounting.
                                                 •        Lots are defined and maintained in accounting while buying a long position or selling a short
                                                          position. Price gain depend on defined lot account selection order (consumption order).
                                                          Depending on defined method, the decision can only be taken at the end of the day.



                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                   339




Duplication is prohibited.                                                                                                                                                Duplication is prohibited.


                                   End-of-Day Processing for Securities
                                   Business Transaction
                                   Demo




                             170                                                                                IFPSLF                                         © SAP SE

Bond Example 1 – Purchase and Sale – Life Cycle
                                Basic Data - Security Information                                                                                            Accounting Requirements
                                Maturity                                         30.09.2018 – 30.09.2028 (10 Years)                                          •   Applying FVTPL valuation approach
                                Issue Amount                                     1.000.000 € (complete bond issued)                                          •   Periodic financial statement (monthly reporting
                                Nominal Amount                                   1000 €                                                                          31.01. / 28.02. / 31.03. / …)

                                Nominal Interest                                 3.6 % (30/360)
                                                                                                                                                             •   Recognition of price gain on lot level
                                                                                                                                                             •   Recognition of accrued interest
                                Interest Payment                                Half-yearly

                                Flow Data                                                    Purchase                     Purchase          Sale

                                Date                                                 02.01.2019                          03.02.2019      30.06.2019
                                Nominal Amount                                       200.000 €                           300.000 €       350.000 €
                                Position Amount                                      200.000 €                           300.000 €       365.000 €
                                Accrued interest                                     1.820 €                             3.660 €         3.150 €
                                                                                                                Purchase,                           2nd Purchase,
                                     Operational                                                                                                                          Interest
                                                                                                                Accrued                               Accrued                                                     Sale
                                       Events                                                                                                                             Payment
                                                                                                                 Interest                              Interest
                                                                            30.09.2018                         02.01.2019             31.01.2019 03.02.2019              31.03.2019                        30.06.2019


                                  FPSL System                                                                    Register                              Register
                                                                                                                                      Period-End*                       Period-End*                        Period-End*
                                    Activities                                                                 End-of-Day                             End-of-Day
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                               341
                                                                                                                                                                                                  * Period-End includes Day Processing




Duplication is prohibited.                                                                                                                                                                                                                            Duplication is prohibited.
                                 Accounting for Securities – Relevant Process Steps

                                        Day Processing                                                         Intraday                                                          Security Positions

                                            Set Posting                          Register                     Register        Register                                  Define         Allocate       Determine          M&T *
                                                                                                                                                      IAD
                                               Date                                MD                           BT              AD                                       Lots            Lots         Price Gain          BT

                                                                                                                                             Impairment Attribute
                                                                                                               Register                                                                   End-of-Day Process
                                                                                                                                               Determination


                                        Day-End Processing / Period-End Processing

                                                                                                          Write                             Value        Move and       Value                          Classify
                                                  Accrue                      Defer                                         Release                                                   Classify                           Adjust
                                                                                                          Down                               TC          Transform       FX                              P&L

                                                                                                                                                                                                                         Manual
                                                                                                                            Day-End Process / Period-End Process
                                                                                                                                                                                                                         Posting



                                        Period-End                              Year-End Processing                          Across                 Preparatory Processing
                                        Processing
                                                                                                                                                        Determine      Determine Amort.       Determine Adj.        Determine Fair
                                                Close                                   Carry Forward                           Allocate
                                                                                                                                                      Amortized Cost    Valuation Cost        for Credit Risk           Value

                                        Open and Close                           Balance Carry Forward
                                        Posting Periods                            (Cross/-Contract)

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                               342
                                                                                                                                                                                             *M&T abbreviation for „Move and Transform“




                             © SAP SE                                                                                                               IFPSLF                                                                                      171

Show the day end bt
                                                                                                                             processing in the system
                                                                                                                             + Results
                                                                                                                             Allokationsbelege für Lots




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                               343




Duplication is prohibited.                                                                                                                                                                            Duplication is prohibited.
                                   Data Model – Lot

                                                        Master Data                                                   Additional                    Flow Data            Key Date Values
                                                                                                                   Information on
                                                Contract                                                            Master Data
                                                                                Business                                                      Business                   Target
                                                Security                                                                                                   Cash Flow
                                                                                 Partner                        Analytical                   Transaction                 Values
                                                                                                                                   Lot
                                              Securities                                                         Status
                                                                                 Portfolio
                                               Account




                                                                                  Calculation Rates                               Journal Entries               Market Data
                                                                                    and Factors
                                                                                                                               Subledger Journal Entry
                                                                                               Impairment
                                                                                                Attributes




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                               344




                             172                                                                                                         IFPSLF                                            © SAP SE

End-of-Day Processing for Securities
                                 Business Transaction
                                 Theory




Duplication is prohibited.                                                                                                                               Duplication is prohibited.
                                 Lot Accounting – Business Problem adressed



                                          Lot accounting applies to accounting for security positions

                                          Accounting in general is a record keeping technique that traces the dates of purchase and
                                          sale, cost basis, and transaction size for each security in a portfolio which is required by law

                                          Lots are introduced if the granularity for recording events for securities need to be more finer
                                          to allow price gain determination on basis of each single position change and NOT using an
                                          average price

                                          Target of lot accounting: Provide financial statement (balance sheet and P&L) on granularity
                                          lot (for security positions subject to lot accounting)

                                          Different price gain determination methods possible – differences apply while reducing
                                          positions (long or short)


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                  346




                             © SAP SE                                                                         IFPSLF                               173

End-of-Day Processing (Business Transaction)

                                   Definition                                                                                      Process Step
                                   End-of-Day                             Processing                            (BT)   generates   • Define Lots: Definition and update of lots as a result of
                                   business transaction-based postings on the                                                       position changes. Position changes are all transactions
                                   basis of the business transactions registered                                                    which are
                                   for a posting date, for all accounting systems                                                       • increasing a position (by purchasing securities)
                                   in a legal entity.                                                                                   • decreasing a position (by selling securities)
                                                                                                                                   • Allocate Register Postings: Allocation of register
                                                                                                                                    postings to lots
                                                                                                                                   • Determine Price Gain: Documentation of price gains
                                                                                                                                    in case of decreasing a position
                                                                                                                                   • Move and Transform (BT): Fixing of foreign currency
                                                                                                                                    amounts as a result of the registration of business
                                                                                                                                    transactions
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                     347




Duplication is prohibited.                                                                                                                                                                              Duplication is prohibited.
                                   End-of-Day Processing (BT) – Lot Accounting

                                   Definition                                                                                           Process step
                                   Lot Accounting is used to document securities                                                        For lot accounting, security positions are divided
                                   positions in accounting.                                                                             into single positions or lots. These lots are built up
                                   It’s a necessary tool to keep track of the acquisition                                               by inflows and reduced by outflows, according to a
                                   value of a single purchase. This information is used                                                 defined lot selection method.
                                   to determine price gains according to one out of
                                   six possible methods, impairment changes etc.
                                                                                                                                         Consequences
                                   Characteristics                                                                                       If lot accounting is applied to a security position,
                                                                                                                                         the postings generated by End-of-Day Processing
                                   •        Accounting data (subledger journal entries,                                                  (Contract), Period-End Processing (Contract) and
                                            notes to balance sheet, calculator results) are                                              Period-Opening Processing (Contract) also refer
                                            created on lot level                                                                         to lots for the security position.
                                   •        Impairment status on lot level is supported                                                  This also means that the calculators called by the
                                   •        If a security position is subject to lot accounting                                          process steps calculate at lot level and, if required,
                                            it can be defined for each accounting standard                                               save their results at lot level on the database.
                                            separately
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                     348




                             174                                                                                                   IFPSLF                                                    © SAP SE

Lot Accounting – Lot Life Cycle

                                                                  01 Active                                                                                   04 Not reversed completely




                                                 02 Used completely
                                                                                                              Lots with a nominal value/             Lots where the inflow has been reversed but
                                                                                                              quantity of 0 where the inflow         that contain outflows that have not yet been
                                                                                                              is not reversed. Lots that are         reversed. Lots that are not completely
                                                                                                              used completely are only used          reversed are only considered for the
                                                                                                              for the processing of reversals.       processing of reversals.

                                                             03 Reversed                                                                                                  05 Inactive
                                                                                                              Lots for which all business            Lots that have become
                                                                                                              transactions are reversed.             obsolete as a result of a
                                                                                                              Reversed lots are no longer            rollback (corrections). Inactive
                                                                                                              considered by the Price Gain           lots are no longer considered
                                                                                                              Calculator.                            by the Price Gain Calculator.
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                         349




Duplication is prohibited.                                                                                                                                                                                      Duplication is prohibited.
                                 End-of-Day Processing (BT) – Allocate Register Postings

                                 Definition                                                                                     Process Step
                                 The Allocate Register Postings step                                                            The context defined by the business transaction determines
                                 allocates register postings for a security                                                     which allocation algorithm is applied to a register posting. A
                                 position to the lot for the security                                                           distinction is made between the following situations:
                                 position.                                                                                      1. Position-changing BT: The business transaction contains an
                                 Cross-contract register postings are not                                                          item that changes the acquisition value of the securities
                                 allocated to lots. An allocation document                                                         position
                                 is created for each register document for
                                                                                                                                2. Non-position-changing BT
                                 each relevant accounting system.
                                                                                                                                    a. The register posting to be allocated reduces a short-term
                                                                                                                                       receivable
                                                                                                                                    b. The register posting to be allocated does not reduce a
                                                                                                                                       short-term receivable
                                Non-position-changing events are e.g. interest                                                  3. Reversal BT: The business transaction is the reversal of a
                                payments, dividends. They are getting paid on                                                     business transaction described in 1 or 2
                                level of the complete position and will need to
                                be distributed across the active lots.


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                         350




                             © SAP SE                                                                                                 IFPSLF                                                              175

Example for Lot Processing

                                                Day 1                    Purchase: 10 SAP shares                                      Price: 121 EUR (each)

                                                Day 2                    Purchase: 15 SAP shares                                      Price: 125 EUR (each)

                                                Day 3                    Dividend payment 1,50 EUR per share                          37,50 EUR

                                                Day 4                    Sale: 5 SAP shares                                           Price: 123 EUR                        Profit: 10 EUR = (123 EUR -121 EUR) * 5 shares

                                                Day 5                    Sale: 6 SAP shares                                           Price: 124 EUR                        Profit: 14 EUR = (124 EUR -121 EUR) * 5 shares +
                                                                                                                                                                                             (124 EUR -125 EUR) * 1 share




                                       Lot 1                                                                                                            Lot 2
                                          10 SAP shares                   Price: 121 EUR                    Value: 1210 EUR                              15 SAP shares        Price: 125 EUR       Value: 1875 EUR
                                          10 SAP shares                   Div: 1,50 EUR                                       Profit: 15 EUR             15 SAP shares        Div: 1,50 EUR                            Profit: 22,50 EUR
                                          -5 SAP shares                   Price 123 EUR                     615 EUR           Profit: 10 EUR             -1 SAP share        Price: 124 EUR        Value: 124 EUR      Loss: 1 EUR
                                          5 SAP shares                    Price: 121 EUR                    Value: 605 EUR                               14 SAP shares       Price: 125 EUR        Value: 1750 EUR
                                          -5 SAP shares                   Price: 124 EUR                    Value: 620 EUR    Profit: 15 EUR




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                             351




Duplication is prohibited.                                                                                                                                                                                                                          Duplication is prohibited.
                                   End-of-Day Processing (BT) – Allocate Register Postings

                                          1. Position-changing Business Transaction
                                          In the Define Lots step, the position-changing business transaction item is distributed to the
                                          lots based on the lot selection method for the price gain determination. Amount B in position
                                          currency for the position-changing business transaction item is partitioned into amounts Bi per
                                          lot Li.
                                                                                                                                  If a position is sold, the total amount is distributed to the lots (defined by lot selection method)
                                                                                                           ௜ ௜                    If a position is bought, a new lot is crated, but the formula is still correct


                                          The amount in transaction currency A in the register posting allocated to Lot Li is given by

                                                                                                                                  All changes in transaction currency is distributed proportionally according to position changes
                                                                            ௜                                   ௜                 (relevant for price gain determination)




                                          (following the partition above).


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                             352




                             176                                                                                                               IFPSLF                                                                                    © SAP SE

End-of-Day Processing (BT) – Allocate Register Postings

                                 2. Non-position-changing Business Transaction
                                 a. Register Posting reduces short-term receivable

                                 In this case the register posting is made to a subledger account from the subledger account group 100801
                                 (Receivables/Payables (Due)) and the related business transaction item has the posting direction credit.

                                 The amount in transaction currency A in the register posting is allocated to the lots in proportion to balance BALi per lot Li
                                 in relation to the total balance BAL of the subledger account for the register posting. Therefore, the following applies to
                                 amount Ai allocated to lot L௜i: Ai ௜= A* BALi / BAL.

                                 When an overpayment is made (the payment amount is larger than the short-term receivable to be cleared) the
                                 overpayment amount is allocated to the lots in the same way as in the following case.
                                 Example: Interest or dividend payment that is due and get paid.

                                 b. Register Posting does not reduce short-term receivable

                                 Amount in transaction currency A in the register posting is allocated to the lots in proportion to quantity (nominal or
                                 number of units) Qi per lot Li in relation to the total quantity Q of the securities position. Therefore, the following applies to
                                 amount Ai allocated to lot i: Ai = A*Qi / Q.


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                           353




Duplication is prohibited.                                                                                                                                                        Duplication is prohibited.
                                 End-of-Day Processing (BT) – Allocate Register Postings

                                        3. Reversal Business Transaction
                                        In this case there is a register posting for the reversed business transaction that corresponds
                                        to the register posting for the reversal business transaction.

                                        The allocation journal entry for the register posting for the reversal business transaction is
                                        created when the allocation journal entry for the register journal entry of the reversed
                                        business transaction is reset, while retaining the lot assignment. The following information is
                                        transferred from the allocation journal entry for the corresponding register posting for the
                                        reversed business transaction to the new allocation journal entry:
                                        •         The amounts in transaction currency allocated to the lots multiplied by -1
                                        •         The debit/credit indicator of the relevant line item
                                        •         The assignment of the allocated amount to the respective lot
                                        •         The reversal indicator is set in the newly created allocation journal entry

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                           354




                             © SAP SE                                                                         IFPSLF                                                        177

End-of-Day Processing (BT) – Allocate Register Postings

                                          3. Reversal Business Transaction
                                          •         The amounts in transaction currency allocated to the lots multiplied by -1
                                          •         The debit/credit indicator of the relevant line item
                                          •         The assignment of the allocated amount to the respective lot
                                          •         The reversal indicator is set in the newly created allocation journal entry




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                       355




Duplication is prohibited.                                                                                                                                    Duplication is prohibited.
                                   Lot Accounting – Account Assignment




                                                                                                     Balance Sheet              Profit and Loss

                                                                                        Receivables/Payables                       Income

                                                                                                                                Profit and Loss

                                                                                                                                   Expense

                                                                                                                                    Equity

                                                                                                                              Other Income (OCI)


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                       356




                             178                                                                                     IFPSLF                        © SAP SE

Bond End-of-Day Processing
                                 Business Transaction
                                 Hands On




Duplication is prohibited.                                                                                                                                                      Duplication is prohibited.
                                Hands On – End-of-Day Processing (Business Transaction): Day Processing 2

                                                                                            Task                          Application Menu & Transaction
                                         Execute the “End-of-Day Processing                                     /BA1/BR_DAY_END_BT_1 - End-of-Day Processing (Business
                                         (Business Transaction)” process                                        Transaction)




                                                                          To be considered
                                         The following parameters must be
                                         considered:
                                         1. Legal Entity
                                         2. Posting Date


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                         358




                             © SAP SE                                                                         IFPSLF                                                      179

Hands On – Results: Journal Entries

                                                                                                                                                         Journal Entries

                                                                                                     Task                           To be considered
                                        Check the subledger documents.                                             The following parameters must be considered:
                                                                                                                   1. Legal Entity


                                                                                   Selection Screen                          SAP Menu Location & Transaction
                                                                                                                   /BA1/BR_RESLT_VIEWER - Display Subledger Documents




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                              359




Duplication is prohibited.                                                                                                                                                       Duplication is prohibited.
                                   Hands On – Results: Additional Data

                                                                                                                                                          Additional Data

                                                                                              Task                          Application Menu & Transaction
                                           Check the additional information on                                    /BA1/HW_RESULTVIEWER - Display Results Data
                                           master data: Lot
                                           with the result view _S_SCT_PGD




                                                                            To be considered
                                           The following parameters must be
                                           considered:
                                           1. Legal Entity
                                           2. Mind the System Date!


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                              360




                             180                                                                                IFPSLF                                               © SAP SE
