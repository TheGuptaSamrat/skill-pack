Classification: training-derived-concepts
Source basis: FPSL TRAINING DOCUMENT.pdf, pages 180-220
Trust usage: FX mechanics, OCI conceptual flow, recycling on position exit
Do not use for: specific FX calculation formulas or rates
Topics covered: FX revaluation, Monetary Asset Revaluation (MAR), OCI, recycling, multi-currency accounting

# Bond Example - FX Revaluation and OCI Recycling
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

Lunch Break




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                 361




Duplication is prohibited.                                                                                                              Duplication is prohibited.


                                 Securities Period-End Processing

                                 Business Context




                             © SAP SE                                                                              IFPSLF         181

Period-End Processing Securities – Business Problem to be solved

                                             At the end of the period the financial statement should reflect in an appropriate way all
                                             financial aspects of the business as of the last day of the period. Purpose is to disclose
                                             transparency regarding the current business situation to all stakeholders (regulators,
                                             financial markets, business partner, investors).

                                             To achieve this all components of the financial statement need to be updated to document

                                             •         All operational value flows

                                             •         All not completed income and efforts (accruals and deferral) need to be distributed for the
                                                       current period

                                             •         Risk provision need to be calculated and updated in the balance sheet

                                             •         Valuation of all assets and obligations need to be updated

                                             •         All relevant risks need to be reflected appropriately in the financial statement

                                             •         Period need to be protected against subsequent changes
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                         363




Duplication is prohibited.                                                                                                                                      Duplication is prohibited.


                                   Securities Period-End Processing

                                   Demo




                             182                                                                                IFPSLF                               © SAP SE

Bond Example 1 – Purchase and Sale – Life Cycle
                                Basic Data - Security Information                                                                                 Accounting Requirements
                                Maturity                                         30.09.2018 – 30.09.2028 (10 Years)                               •   Applying FVTPL valuation approach
                                Issue Amount                                     1.000.000 € (complete bond issued)                               •   Periodic financial statement (monthly reporting
                                Nominal Amount                                   1000 €                                                               31.01. / 28.02. / 31.03. / …)

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
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                            365
                                                                                                                                                                                * Period-End includes Day Processing




Duplication is prohibited.                                                                                                                                                                                                         Duplication is prohibited.
                                 Data Model – Key Date Values

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




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                            366




                             © SAP SE                                                                                                       IFPSLF                                                                           183

Data Model
                                                                                                                Delivery is …                                                            Delivery is …

                                                                                                                                          Amortized Valuation
                                                                             Price/ Gain                           possible                      Cost                                          possible


                                                                                Accruals                          mandatory                 Risk Adjustments                         Depends on type of risk*




                                         Target Values
                                                                                                                                                Fair Value of
                                                                       Accrued Interest                           mandatory                                                                  mandatory
                                                                                                                                                 Collateral

                                                                                Deferrals                          possible                       Free Line                                    possible


                                                                        Amortized Cost                             possible                 Maturity Grouping                                  possible


                                                                             Credit Risk
                                                                                                                   possible
                                                                             Adjustment                                                 Legend
                                                                                                                                                   Used in the bond example
                                                                              Fair Value                           possible                        Target value but not used in the example

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                 367
                                                                                                                                * Different types of risks are supported. Only some of them can be derived FPSL internally




Duplication is prohibited.                                                                                                                                                                                                              Duplication is prohibited.
                                   Key Date Values – Target Value – Accrued Interest

                                           1. Target Value – Accrued Interest




                                            2. A look into the system
                                            /BA1/HW_RESULTVIEWER - Display Results Data
                                            Result Area / Resultview: SAFI / _S_SCT_TVL



                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                 368




                             184                                                                                              IFPSLF                                                                                         © SAP SE

Data Model – Calculation Rates and Factors

                                                      Master Data                                                  Additional                  Flow Data            Key Date Values
                                                                                                                Information on
                                              Contract                                                           Master Data
                                                                                                                                          Business                  Target
                                              Security                                                                                                 Cash Flow
                                                                                                              Analytical                 Transaction                Values
                                                                                                                              Lot
                                            Securities                                                         Status
                                             Account




                                                                                Calculation Rates                            Journal Entries               Market Data
                                                                                  and Factors
                                                                                                                           Subledger Journal Entry
                                                                                             Impairment
                                                                                              Attributes




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                           369




Duplication is prohibited.                                                                                                                                                                        Duplication is prohibited.
                                 Calculation Rates and Factors – Impairment Attributes

                                         1. Upload of Attributes and Master Rating




                                          2. A look into the system
                                          /BA1/HW_RESULTVIEWER
                                          Result Area / Resultview: SAFI / _S_SCT_IMP


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                           370




                             © SAP SE                                                                                               IFPSLF                                                  185

Data Model – Market Data

                                                        Master Data                                                  Additional                  Flow Data                 Key Date Values
                                                                                                                  Information on
                                                Contract                                                           Master Data
                                                                                                                                            Business                       Target
                                                Security                                                                                                 Cash Flow
                                                                                                                Analytical                 Transaction                     Values
                                                                                                                                Lot
                                              Securities                                                         Status
                                               Account




                                                                                  Calculation Rates                            Journal Entries                Market Data
                                                                                    and Factors
                                                                                                                             Subledger Journal Entry
                                                                                               Impairment
                                                                                                Attributes
                                                                                                                                                         Prices/ Rates for Financial
                                                                                                                                                                 Instruments



                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                 371




Duplication is prohibited.                                                                                                                                                                              Duplication is prohibited.
                                   Market Value – Prices for Financial Instruments
                                            1. Market Data




                                            2. A look into the system
                                            /BA1/F4_SEC02 - Edit Prices for Financial Instruments
                                            Market Data Area: S000


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                 372




                             186                                                                                                      IFPSLF                                                 © SAP SE

Show the period end
                                                                                                              processing in the system
                                                                                                              (Protocols)
                                                                                                              + Results




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                              373




Duplication is prohibited.                                                                                                                           Duplication is prohibited.


                                 Bond Period-End Processing
                                 Value TC
                                 Theory




                             © SAP SE                                                                                    IFPSLF                187

Accounting for Securities – Relevant Process Steps

                                          Day Processing                                                         Intraday                                                           Security Positions

                                              Set Posting                          Register                     Register        Register                                   Define         Allocate       Determine        M&T *
                                                                                                                                                        IAD
                                                 Date                                MD                           BT              AD                                        Lots            Lots         Price Gain        BT

                                                                                                                                               Impairment Attribute
                                                                                                                 Register                                                                    End-of-Day Process
                                                                                                                                                 Determination


                                          Day-End Processing / Period-End Processing

                                                                                                            Write                             Value       Move and         Value                         Classify
                                                    Accrue                      Defer                                          Release                                                   Classify                         Adjust
                                                                                                            Down                               TC         Transform         FX                             P&L

                                                                                                                                                                                                                          Manual
                                                                                                                              Day-End Process / Period-End Process
                                                                                                                                                                                                                          Posting



                                          Period-End                              Year-End Processing                           Across                Preparatory Processing
                                          Processing
                                                                                                                                                         Determine        Determine Amort.       Determine Adj.       Determine Fair
                                                  Close                                   Carry Forward                            Allocate
                                                                                                                                                       Amortized Cost      Valuation Cost        for Credit Risk          Value

                                          Open and Close                           Balance Carry Forward
                                          Posting Periods                            (Cross/-Contract)

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                                375
                                                                                                                                                                                                *M&T abbreviation for „Move and Transform“




Duplication is prohibited.                                                                                                                                                                                                                         Duplication is prohibited.
                               Accounting Process Model and Book Value Components – Value TC

                                   Day                                     Period-End Processing
                                   Processing




                                                                                                                                                      Write
                                   Register                                         Accrue                                     Defer                                       Release                          Value TC
                                                                                                                                                      Down


                                                                                  Accruals                                 Deferrals
                                        Unpaid
                                                                                                                                               Write Down                                            Hedged Fair Value
                                       Principle                                                                                                                        Valuation
                                                                                                                                                                        Remnants         Credit Risk financial Adjustment
                                       Balance
                                                                                                                                                                                                        risks



                                                                                                                                       Amortized
                                                                                                                                                                                                                                    Fair Value
                                                                                                                                         Cost



                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                                376




                             188                                                                                                                      IFPSLF                                                                            © SAP SE

Value TC – Definition and Characteristics


                                       Definition                                                                            Process step
                                       The Value TC is an analytical step which is                                           The Value TC calculates the target values or uses
                                       responsible for the documentation of changes                                          delivered target values. The journal entry is created
                                       to the valuation of a position.                                                       by determining the delta between current balance and
                                                                                                                             target value.



                                       The Value TC step tracks the following values:
                                                •      Credit Risk (Impairment)
                                                •      Financial Risks (several types)
                                                •      Fair Value
                                                •      Target Value (after economic write down)



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                          377




Duplication is prohibited.                                                                                                                                                                       Duplication is prohibited.
                                 Value TC – Fair Value


                                                                                                 Methods
                                                                                                                Import
                                                                                                              Parametric                                  Mark-to-Market
                                                                      Cash-Flow-Based Determination                                                        Mark-to-Model
                                                                                            Custom Determination


                                                                                              Exception Processing

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                          378




                             © SAP SE                                                                                      IFPSLF                                                          189

Value TC – Fair Value

                                              Parametric − Mark-to-Market                                                     Cash-Flow-based − Mark-to-Model
                                              In the mark-to-market determination of fair                                     Prerequisites are interest rates and yield
                                              value, the fair value calculator scales the                                     curves. By discounting cash flows based on
                                              market prices according to the securities                                       these interest rates of the yield curve, the full
                                              position.                                                                       fair value is determined.

                                              Prerequisite: Market data imported
                                              Option for accrued interest market price
                                              between
                                                                                                                                       ‫ ݐ ܸܨܨ‬ൌ ෍ ‫ܨܥ‬௜ ൈ ‫ܨܦ‬௜
                                              •        including (dirty)
                                                                                                                                                     ௧೔ வ௧
                                              •        excluding (clean)                                                                                               where
                                              In case of excluding, accruals need to be                                                                  ‫ܸܨܨ‬: full fair value
                                              imported separately                                                                                    ‫ܨܦ‬: discounting factor




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                      379




Duplication is prohibited.                                                                                                                                                                   Duplication is prohibited.
                                   Value TC – Account Assignment




                                                                                                     Balance Sheet                       Profit and Loss

                                                                                         Fair Value Adjustment                                Income

                                                                                                                                         Profit and Loss

                                                                                                                                             Expense

                                                                                                                                               Equity

                                                                                                                                      Other Income (OCI)


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                      380




                             190                                                                                     IFPSLF                                                       © SAP SE

Bond Period-End Processing

                                 Hands On




Duplication is prohibited.                                                                                                                                                            Duplication is prohibited.
                                 Hands On – Data: Creating Your Own Data 6

                                                                                                                                                                  Market Data
                                                                                            Task                           Application Menu & Transaction
                                         Create the Market Data for your Security by                            /BA1/F4_SEC02 - Edit Prices for Financial Instruments
                                         copying the market data from the table in the
                                         market data table.


                                                                           Selection Screen
                                        1. Enter Market Data Area: S000
                                        2. Enter the External Number of your Security




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                              382




                             © SAP SE                                                                         IFPSLF                                                            191

Hands On – Data: Creating Your Own Data 7

                                                                                                                                                                                     Market Data
                                        Exemplary entry for the relevant market data attributes




                                                               Date                                         Rate Category Exchange             Unit                Price
                                                              31.01.2019                                   XETRA          SCLS                EUR                            0.95
                                                              02.01.2019                                   XETRA          SCLS                EUR                            0.99

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                    383




Duplication is prohibited.                                                                                                                                                                               Duplication is prohibited.
                                   Hands On – Data: Creating Your Own Data / Uploads
                                                                                                                                                                                    Key Date Values

                                                                                                            Task                                               Transaction          Calculation Rates
                                                                                                                                                                                        & Factors
                                          Create your uploads by copying the data from:
                                                                                                                                              SE38: /BA1/R_AL_HW_EXCEL_EXECUTE
                                          <test data directory>/Bond01 test data/ ACC_Bond_01.csv
                                          <test data directory>/Bond01 test data/ RP_Bond_01.csv
                                          a. Accruals
                                          b. Risk Parameters

                                                                                         To be considered
                                         The following parameters need to be changed accordingly:                                             a) Accruals
                                         1. External Number of your Security (a./b.)
                                         2. Source System (a.)                                                                                b) Risk parameters


                                                                                                                     Choose path as shown to
                                                                                                                     select your adapted .csv files




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                    384




                             192                                                                                                   IFPSLF                                                     © SAP SE

Hands On – Results: Check Uploads

                                                                                                                                                          Key Date Values
                                                                                                                                                          Calculation Rates
                                                                                                                                                              & Factors
                                                                                                 Task                     Application Menu & Transaction
                                          Check the uploaded data in the following                              /BA1/HW_RESULTVIEWER - Display Results Data
                                          Result Views:
                                          a. Accruals: _S_SCT_TVR
                                          b. Risk Data: _S_SCT_IMP




                                                                              To be considered
                                        The following parameters must be considered:
                                        1. External Number of your Security (a./b.)
                                        2. Source System (a.)

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                             385




Duplication is prohibited.                                                                                                                                                          Duplication is prohibited.
                                 Hands On – Period-End Processing (Contract)

                                                                                            Task                          Application Menu & Transaction
                                         As a preliminary for Period End                                        /BA1/BR_SET_POST_DAT – Set Posting Date
                                         Processing execute complete Day                                        /BA1/BR_REGISTER – Register
                                         Processing for 31.01.2019
                                                                                                                /BA1/BR_DAY_END_BT_1 – End-of-Day Processing
                                         Execute the “Period End (Contract)”                                    /BA1/BR_DAY_END_1 – End-of-Day Processing (Contract)
                                         process.
                                                                                                                /BA1/BR_PERIOD_END_1 - Period End Processing (Contract)




                                                                          To be considered
                                         The following parameters must be
                                         considered:
                                         1. Source System
                                         2. Legal Entity
                                         3. Posting Date

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                             386




                             © SAP SE                                                                         IFPSLF                                                          193

Hands On – Results: Journal Entries

                                                                                                                                                           Journal Entries

                                                                                                       Task                         To be considered
                                          Check the subledger documents.                                            The following parameters must be considered:
                                                                                                                    1. Legal Entity

                                                                                     Selection Screen                          Application Menu & Transaction
                                                                                                                    /BA1/BR_RESLT_VIEWER - Display Subledger Documents




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                            387




Duplication is prohibited.                                                                                                                                                       Duplication is prohibited.

                                   Bond End-of-Day Processing
                                   Interest Payment
                                   Demo




                             194                                                                                IFPSLF                                                © SAP SE

Bond Example 1 – Purchase and Sale – Life Cycle
                                Basic Data - Security Information                                                                                 Accounting Requirements
                                Maturity                                         30.09.2018 – 30.09.2028 (10 Years)                               •   Applying FVTPL valuation approach
                                Issue Amount                                     1.000.000 € (complete bond issued)                               •   Periodic financial statement (monthly reporting
                                Nominal Amount                                   1000 €                                                               31.01. / 28.02. / 31.03. / …)

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
                                                                                                                               Period-End*                   Period-End*                 Period-End*
                                    Activities                                                                End-of-Day                      End-of-Day
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                            389
                                                                                                                                                                                * Period-End includes Day Processing




Duplication is prohibited.                                                                                                                                                                                                         Duplication is prohibited.
                                   Interest Payment – Distribution to Lots




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                            390




                             © SAP SE                                                                                                       IFPSLF                                                                           195

Bond End-of-Day Processing
                                   Determine Price Gain
                                   Business Context




Duplication is prohibited.                                                                                                                                                   Duplication is prohibited.
                                     Sale of a Security Position – Business Problem to be solved


                                             If a position is sold the following information is available:
                                                      •         What?       Reference to security
                                                      •         How much? Quantity /nominal value
                                                      •         From where? Sold from which securities account
                                                      •         Price paid? Price of the position
                                                      •         When?       Trade date and settlement date

                                             Besides this operational information about the trade, financial accounting needs to reflect the
                                             trade with additional information
                                                      •         Which fine granular position (lot) is affected? There is the need to update quantity, status,
                                                                current values of the affected lots
                                                      •         What is the realized profit or loss for the trade to be recognized in the period of the trade
                                                                (depends on the affected lots)
                                                      •         Update of financial statement regarding position change to other components like risk provision
                                                                (is happening at period-end)


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                      392




                             196                                                                                IFPSLF                                            © SAP SE

Bond End-of-Day Processing
                                 Determine Price Gain
                                 Demo




Duplication is prohibited.                                                                                                                                                                                                         Duplication is prohibited.
                                 Bond Example 1 – Purchase and Sale – Life Cycle
                                Basic Data - Security Information                                                                                 Accounting Requirements
                                Maturity                                         30.09.2018 – 30.09.2028 (10 Years)                               •   Applying FVTPL valuation approach
                                Issue Amount                                     1.000.000 € (complete bond issued)                               •   Periodic financial statement (monthly reporting
                                Nominal Amount                                   1000 €                                                               31.01. / 28.02. / 31.03. / …)

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
                                                                                                                               Period-End*                   Period-End*                 Period-End*
                                    Activities                                                                End-of-Day                      End-of-Day
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                            394
                                                                                                                                                                                * Period-End includes Day Processing




                             © SAP SE                                                                                                       IFPSLF                                                                           197

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

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                           395
                                                                                                                                                                                           *M&T abbreviation for „Move and Transform“




Duplication is prohibited.                                                                                                                                                                                                                    Duplication is prohibited.




                                                                                                                                 Show the period end
                                                                                                                                 processing in the system
                                                                                                                                 (Protocols)
                                                                                                                                 + Results RDL result +
                                                                                                                                 Journal entries




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                           396




                             198                                                                                                                   IFPSLF                                                                         © SAP SE

Bond End-of-Day Processing
                                 Determine Price Gain
                                 Theory




Duplication is prohibited.                                                                                                                                                       Duplication is prohibited.
                                 End-of-Day Processing (BT) – Determine Price Gain

                                 Definition                                                                       Process Step
                                 The Determine Price Gain process step                                            The price gain calculator determines the type of
                                 documents the nominal price gain for a securities                                price gain determination to be applied from
                                 position resulting from a position change.                                       Customizing, depending on the accounting system.
                                 The price gain calculator determines the nominal                                 You can use these methodologies for this:
                                 price gain.
                                                                                                                  • Price Gain Determination based on the
                                                                                                                    Average Cost Method
                                 Results
                                                                                                                  • Price Gain Determination based on Lot
                                 •        Price gain results, which include the position                            Selection Method
                                          outflow factor
                                                                                                                  • External import of Price Gain
                                 •        Lot results for collective position
                                 •        Profit or loss recognition in income statement




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                          398




                             © SAP SE                                                                         IFPSLF                                                       199

End-of-Day Processing (BT) – Determine Price Gain


                                         Average Cost Method
                                         When there is a position change, the lot result of the collective position is updated as follows:
                                         ¾         The adjustment of the quantity/nominal value of the lot (collective position) is calculated by adding the
                                                   quantity/ nominal value of the position change (taking the plus/minus sign of the business transaction
                                                   into account)
                                         ¾         The adjustment of the lot acquisition value is calculated as follows:
                                             o         For an inflow: By adding the position amount of the position change (taking the plus/minus sign of the business
                                                       transaction into account)
                                             o         For an outflow: By multiplying the quantity/nominal after the change with the existing price per unit

                                         ¾         The price per unit of the lot (collective position) is calculated by scaling the acquisition value of the lot
                                                   to the unit in the lot




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                   399




Duplication is prohibited.                                                                                                                                                                                Duplication is prohibited.
                                   End-of-Day Processing (BT) – Determine Price Gain


                                          Average Cost Method
                                          Price gain with position inflow and position outflow
                                          ¾      For an outflow, the system determines the price gain and position outflow factor:

                                               o                  Price gain = price of position change – (quantity of position change * (nominal value of position / quantity of position))

                                                      more simplified: Price gain = (selling price – acquisition price) * quantity




                                               o                                                                Position outflow factor= quantity pf position change / quantity of position

                                                      more simplified: factor by which the position is changing


                                          ¾      For an inflow, the price gain and the position outflow factor are zero




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                   400




                             200                                                                                                                   IFPSLF                                      © SAP SE

End-of-Day Processing (BT) – Determine Price Gain


                                   Lot Selection Method
                                   The positions considered for the determination of price gain are the lots (defined by securities account,
                                   security, position currency and lot ID).

                                   Every inflow generates a new lot.

                                   Every outflow reduces one or more lots.

                                   The reference value is the price per unit for the lot. This is determined from the acquisition value and the
                                   nominal value or the quantity of the lot.

                                   Results for the individual lots for the securities position are determined according to one out of six possible
                                   provided methods.




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                401




Duplication is prohibited.                                                                                                                                             Duplication is prohibited.
                                   End-of-Day Processing (BT) – Determine Price Gain – Lot Selection Method
                                                                                                               FIFO – First in First Out
                                                                 Selection of lots in the sequence they were created.




                                          Lot Selection Method
                                                                                                               LIFO - Last In First Out
                                                                 Selection of lots in reverse order – those created last are selected first.

                                                                                                              HIFO - Highest In First Out
                                                                 Selection of the lots according to the price per unit, the highest selected first.

                                                                                                              LOFO - Lowest In First Out
                                                                 Selection of the lots according to the price per unit, the lowest selected first.

                                                                                                                   Maximum Profit
                                                                 Selection of the lots according to the book value per unit, the lowest selected first.

                                                                                                                   Minimum Profit
                                                                 Selection of the lots according to the book value per unit, the highest selected first.
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                402




                             © SAP SE                                                                               IFPSLF                                       201

End-of-Day Processing (BT) – Determine Price Gain

                                                                                                                                     Permanent
                                     The system determines the potential price gain for each position change.
                                     The acquisition value that the price gain calculator uses as the basis for settling a business transaction is
                                     only taken from position changes that were processed earlier (from an operational perspective) than the
                                     business transaction to be settled (date and time in operational system).


                                                                                                                                  Life-To-Date (LTD)
                                     To determine the price gain, the system always reverts to the last status of the lot since the creation of the
                                     collective position.
                                     The acquisition value of a position is updated from its creation onwards. There is no periodic balancing.




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                               403




Duplication is prohibited.                                                                                                                                                            Duplication is prohibited.
                                     End-of-Day Processing (BT) – Determine Price Gain
                                               160

                                               140                                                                                                       T0: Purchase
                                               120
                                                                                                                                                         T2: First Sale
                                               100

                                       Price    80                                                                                                       T3: Second Sale
                                                60

                                                40

                                                20

                                                 0
                                                     0                                   1                             2             3               4
                                                                                                                  Point in Time


                                                                             Permanent                                               Life-to-Date
                                                 T2:                         Profit                        + 20                      Profit       + 20
                                                 T3:                         + Loss                        - 10                      Profit       + 10


                                                                             = Profit:                     +10                        Profit      + 10


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                               404




                             202                                                                                                         IFPSLF                            © SAP SE

Price Gain Determination – Lot and Price Gain Results


                                                          Lot Result
                                                          •        Date of creation of lot resp. of security position
                                                          •        Acquisition value resp. average acquisition value of lot resp. of
                                                                   security position
                                                          •        Nominal or quantity of lot resp. of security position



                                                              Price Gain Result
                                                              • Price gain amount
                                                              • Reference to (portion of) position change (leading to the price gain amount)



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                      405




Duplication is prohibited.                                                                                                                                   Duplication is prohibited.
                                 Price Gain Determination – Account Assignment




                                                                                                   Balance Sheet              Profit and Loss
                                                                                       Acquisition Value
                                                                                                                                 Income
                                                                                     (Securities) Adjustment

                                                                                                                              Profit and Loss

                                                                                                                                 Expense

                                                                                                                                   Equity

                                                                                                                            Other Income (OCI)


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                      406




                             © SAP SE                                                                              IFPSLF                              203

Break (15min)




Duplication is prohibited.                                                                                                                 Duplication is prohibited.
                                   Quiz




                                         1.          What‘s the difference between a contract and a security?

                                         2.          Why do you need Lot Accounting?

                                         3.          Which methods can you use for the Price Gain Determination?




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                    408




                             204                                                                                     IFPSLF     © SAP SE

Introduction Bond Example 2

                                 Foreign Currency and OCI with Recycling




Duplication is prohibited.                                                                                                                                                                                                   Duplication is prohibited.
                                 Bond Example 2 – Foreign Currency and OCI with Recycling
                                Basic Data - Security Information                                                                            Accounting Requirements
                                Maturity                                         30.09.2018 – 30.09.2028 (10 Years)                          •   Applying Fair Value through OCI with Recycling
                                Issue Amount                                     1.000.000 $ (complete bond issued)                              approach
                                Nominal Amount                                   1000 $                                                      •   Periodic financial statement (monthly reporting
                                                                                                                                                 31.01. / 28.02. / 31.03. / …)
                                Nominal Interest                                 3.6 % (30/360)
                                                                                                                                             •   FX Evaluation
                                Interest Payment                                Half-yearly

                                Flow Data                                                                     Purchase          Sale

                                Date                                                               02.01.2019              30.06.2019
                                Nominal Amount                                                     200.000 $               200.000 $
                                Position Amount                                                    200.000 $               200.000 $
                                Accrued interest                                                   1.820 $
                                                                                                              Purchase,
                                     Operational                                                                                                     Interest
                                                                                                              Accrued                                                                      Sale
                                       Events                                                                                                        Payment
                                                                                                               Interest
                                                                            30.09.2018                        02.01.2019   31.01.2019 28.02.2019 31.03.2019                           30.06.2019


                                  FPSL System                                                                  Register
                                                                                                                                                 Period-End*                          Period-End*
                                    Activities                                                                End-of-Day
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                      410
                                                                                                                                                                          * Period-End includes Day Processing




                             © SAP SE                                                                                                   IFPSLF                                                                         205

From Business Perspective to FPSL – Recap Introduction IFRS9

                                                                                                                No   Is the financial asset held to achieve   No
                                          Is the objective of entity’s business
                                                                                                                     an objective by both collecting
                                          model to hold the financial assets to
                                                                                                                     contractual cash flows and selling
                                          collect contractual cash flows?
                                                                                                                     financial assets?

                                                                                                Yes                                       Yes
                                                                                                                                                              No
                                       Do contractual cash flows represent solely payments of principal and interest?                                               FVPL
                                                                                                 Yes                                      Yes
                                                                                                                                                              Yes
                                       Does the company apply the fair value option to eliminate an accounting mismatch?

                                                                                               No                                        No

                                                                        Amortized Cost                                                FVOCI


                                                                       Classification and measurement categories according to IFRS9
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                              411




Duplication is prohibited.                                                                                                                                                        Duplication is prohibited.
                                   Foreign Currency – Business Problem to be solved



                                           Each entity has a reporting currency and all amounts in other currencies need to be
                                           translated into this currency. All business need to be reflected in reporting currency of the
                                           company in the financial statement.

                                           Doing business in foreign currencies is ending up with positions (assets, liabilities, cash) in
                                           those currencies.

                                           For all operational value flows in foreign currency, amounts need to be translated into
                                           reporting (and maybe more currencies) with the FX rate valid at this date.

                                           While FX rates are fluctuating a revaluation of all FX positions is necessary at the end of the
                                           period (monetary asset revaluation) to reflect the situation for this key date in the financial
                                           statement.



                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                              412




                             206                                                                                     IFPSLF                                            © SAP SE

OCI with Recycling – Business Problem to be solved




                                          In accounting some of the value adjustments are not getting recognized in income statement,
                                          but on equity as other comprehensive income (OCI). OCI is used for not realized profit or loss
                                          due to value adjustments (calculated).

                                          If an asset is sold (partially or completely) the changed value, previously recognized in OCI,
                                          becomes a realized profit or loss.

                                          Therefore value adjustment need to be reclassified from OCI to P/L to document the
                                          realization of a previously calculated profit or loss.




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                              413




Duplication is prohibited.                                                                                                                                           Duplication is prohibited.
                                 What kind of risks do contracts in foreign currency bear?
                                                                           Quantity Risk / Credit Risk: Contract/Business
                                                                                              Partner                               All-day Business
                                                                         Risk is existing as long as a payment is expected.              Activity



                                                                                 Value Risk: Exchange Rate Risk                        Operational
                                                                            Æ always if two currencies are exchanged                Currency Risk that
                                                                        (e.g. deposit of USD into an EUR current account)              needs to be
                                                                                                                                        managed



                                                                            Transactional Currency <> Functional Currency



                                                                                                               Currency of the
                                                                                 Contract
                                                                                                              published financial
                                                                                 Currency
                                                                                                                  statement

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                              414




                             © SAP SE                                                                              IFPSLF                                      207

Bond 2 Period-End Processing

                                   Demo




Duplication is prohibited.                                                                                                                                                                              Duplication is prohibited.
                                   Data Model – Market Data FX

                                                        Master Data                                                  Additional                  Flow Data                 Key Date Values
                                                                                                                  Information on
                                                Contract                                                           Master Data
                                                                                Business                                                    Business                       Target
                                                Security                                                                                                 Cash Flow
                                                                                 Partner                        Analytical                 Transaction                     Values
                                              Securities                                                         Status
                                                                                 Portfolio
                                               Account




                                                                                  Calculation Rates                            Journal Entries                Market Data
                                                                                    and Factors
                                                                                                                             Subledger Journal Entry
                                                                                               Impairment
                                                                                                Attributes
                                                                                                                                                         Prices/ Rates for Financial
                                                                                                                                                                 Instruments



                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                 416




                             208                                                                                                      IFPSLF                                                 © SAP SE

Market Data – Exchange Rates

                                                     1. Exchange Rates




                                                    2. A look into the system
                                                    /BA1/F4_FX_03 - Display Exchange Rates

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER            417




Duplication is prohibited.                                                                                                         Duplication is prohibited.




                                                       Value FX Example
                                                       Security: DEMO_06*




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER            418




                             © SAP SE                                                                         IFPSLF         209

Processes and Process Steps in FPSL - Value FX

                                          Day Processing                                                         Intraday                                                      Security Positions

                                              Set Posting                          Register                     Register      Register                                Define         Allocate       Determine        M&T
                                                                                                                                                     IAD
                                                 Date                                MD                           BT            AD                                     Lots            Lots         Price Gain        BT

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

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                      419




Duplication is prohibited.                                                                                                                                                                                                                   Duplication is prohibited.


                                   Bond 2 Period-End Processing
                                   Value FX
                                   Theory




                             210                                                                                                                   IFPSLF                                                                         © SAP SE

Value FX – Definition and Characteristics

                                 Definition                                                                     Process Step
                                 Translating amounts from foreign currencies into                               The Value FX process step carries out the following
                                 currencies relevant for accounting to represent                                steps:
                                 current business.
                                                                                                                • Fixing of postings in foreign currency
                                 Determining value changes due to FX rate
                                 changes, by comparing against previous results                                 • Monetary Asset Revaluation (MAR)
                                                                                                                Which method is used depends on the following
                                 Characteristics                                                                settings:

                                 The Value FX process step is available:                                        1. Multicurrency accounting:
                                                                                                                       a. activated
                                 •        at the contract granularity level: it is run in
                                          end-of-day processing and period-end                                         b. deactivated
                                          processing                                                            2. Exchange rate category for currency fixing:

                                 •        at the cross-contract granularity level: it is                               1. specified or
                                          run in end-of-day processing and period-                                     2. not specified
                                          end processing
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                           421




Duplication is prohibited.                                                                                                                                                        Duplication is prohibited.
                                 Value FX Process Step - Methods


                                       Monetary Asset Revaluation (MAR): Revalues the balance in functional currency and all other
                                       local currencies using the valid exchange rate on the balance sheet key date. It also collects the
                                       delta for the existing balance in the foreign exchange result.


                                       Fixing of Postings in Foreign Currency and MAR:

                                       Æ        MCA turned off: Periodical fixing of posting in foreign currency for balance sheet accounts, P&L
                                                accounts and OCI accounts with the exchange rate B of the current key date. MAR follows the
                                                same logic as described before using the exchange rate A.

                                       Æ        MCA turned on: Periodical and daily fixing of posting in foreign currency for balance sheet
                                                accounts with the according exchange rates B (daily and periodend rates). MAR follows the
                                                same logic as described before using the exchange rate A.


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                           422




                             © SAP SE                                                                         IFPSLF                                                        211

Customizing of Legal Entity




                                   1


                                   2

                                                                                                                        1




                                              2



                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                    423




Duplication is prohibited.                                                                                                                                 Duplication is prohibited.
                                   Value FX – Account Assignment




                                                                                                     Balance Sheet            Profit and Loss

                                                                                                                                 Income

                                                                                                                              Profit and Loss

                                                                                                                              Other Income




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                    424




                             212                                                                                     IFPSLF                     © SAP SE

Bond 2 Period-End Processing
                                 Classify P&L
                                 Demo




Duplication is prohibited.                                                                                                                                                                                                   Duplication is prohibited.
                                 Bond Example 2 – Foreign Currency and OCI with Recycling
                                Basic Data - Security Information                                                                            Accounting Requirements
                                Maturity                                         30.09.2018 – 30.09.2028 (10 Years)                          •   Applying Fair Value through OCI with Recycling
                                Issue Amount                                     1.000.000 $ (complete bond issued)                              approach
                                Nominal Amount                                   1000 $                                                      •   Periodic financial statement (monthly reporting
                                                                                                                                                 31.01. / 28.02. / 31.03. / …)
                                Nominal Interest                                 3.6 % (30/360)
                                                                                                                                             •   FX Evaluation
                                Interest Payment                                Half-yearly
                                                                                                                                             •   Recycling
                                Flow Data                                                                     Purchase          Sale

                                Date                                                               02.01.2019              30.06.2019
                                Nominal Amount                                                     200.000 $               200.000 $
                                Position Amount                                                    200.000 $               200.000 $
                                Accrued interest                                                   1.820 $
                                                                                                              Purchase,
                                     Operational                                                                                                     Interest
                                                                                                              Accrued                                                                      Sale
                                       Events                                                                                                        Payment
                                                                                                               Interest
                                                                            30.09.2018                        02.01.2019   31.01.2019 28.02.2019 31.03.2019                           30.06.2019


                                  FPSL System                                                                  Register
                                                                                                                                                 Period-End*                          Period-End*
                                    Activities                                                                End-of-Day
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                      426
                                                                                                                                                                          * Period-End includes Day Processing




                             © SAP SE                                                                                                   IFPSLF                                                                         213

Processes and Process Steps in FPSL - Classify P&L

                                          Day Processing                                                         Intraday                                                      Security Positions

                                              Set Posting                          Register                     Register      Register                                Define         Allocate       Determine        M&T
                                                                                                                                                     IAD
                                                 Date                                MD                           BT            AD                                     Lots            Lots         Price Gain        BT

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

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                      427




Duplication is prohibited.                                                                                                                                                                                                                   Duplication is prohibited.


                                   Bond 2 Period-End Processing
                                   Classify P&L
                                   Theory




                             214                                                                                                                   IFPSLF                                                                         © SAP SE

Recycling of OCI Postings

                                      Changes in the evaluation of value of the security are posted in other comprehensive income positions.
                                      If the value of the security is lowered or the security is (partially) sold, the valuation remnants are (partially)
                                      reversed or the valuation remnants are posted in profit and loss accounts accordingly, which is referred to
                                      as recycling.

                                                                                                                                                               Business Model Criteria


                                                                                                                                             Hold to Collect     Hold to Collect & Sell   HFT or other




                                                                                             Soleily Payments of Principle
                                                                                                                             Fulfilled
                                                                                                                                                  AC                    FVOCI               FVTPL




                                                                                                   and Interest (SPPI)       Not fulfilled
                                                                                                                                                FVTPL                   FVTPL               FVTPL




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                    429




Duplication is prohibited.                                                                                                                                                                                                                 Duplication is prohibited.
                                 Classify P & L – Definition and Characteristics


                                    Definition                                                                                                                    Process Step
                                    In the Classify P&L process step, changes                                                                                     For position outflows within a given calculation interval,
                                    in value that were previously recognized in                                                                                   income and expense from value changes in the fair
                                    other      comprehensive       income     are                                                                                 value or in the lower of cost and market recognized in
                                    reclassified to the profit and loss statement                                                                                 OCI are proportionately reclassified to profit and loss by
                                    proportionately when a position outflow                                                                                       the Classify P&L process step.
                                    occurs.                                                                                                                       For a securities position in foreign currency, the
                                    It is relevant if you use the following                                                                                       currency income and expenses recognized in OCI are
                                    valuation approaches:                                                                                                         also proportionately reclassified to P&L.
                                    • Fair Value Through OCI with Recycling
                                    • LCM Through OCI with Recycling
                                    • Fair Value Through OCI with Recycling
                                       (Investment)




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                    430




                             © SAP SE                                                                                                                            IFPSLF                                                              215

Recycling – Account Assignment




                                                                                                     Profit and Loss                      Equity
                                                                                                                                   Other Comprehensive
                                                                                                                Income
                                                                                                                                          Income
                                                                                                                                          Equity

                                                                                                                Expense               Expense - OCI




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                             431




Duplication is prohibited.                                                                                                                                          Duplication is prohibited.




                                                         Classify Example
                                                         Security: DEMO_06*




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                             432




                             216                                                                                          IFPSLF                         © SAP SE

Introduction Bond Example 3

                                 Multi Currency Accounting Posting Logic




Duplication is prohibited.                                                                                                                                                                                                   Duplication is prohibited.
                                 Bond Example 3 – Multi Currency Accounting
                                Basic Data - Security Information                                                                            Accounting Requirements
                                Maturity                                         30.09.2018 – 30.09.2028 (10 Years)                          •   Applying FVTPL valuation approach
                                Issue Amount                                     1.000.000 $ (complete bond issued)                          •   Periodic financial statement (monthly reporting
                                Nominal Amount                                   1000 $                                                          31.01. / 28.02. / 31.03. / …)

                                Nominal Interest                                 3.6 % (30/360)
                                                                                                                                             •   FX Evaluation
                                                                                                                                             •   Multi Currency Accounting
                                Interest Payment                                Half-yearly

                                Flow Data                                                                     Purchase          Sale

                                Date                                                               02.01.2019              30.06.2019
                                Nominal Amount                                                     200.000 $               200.000 $
                                Position Amount                                                    200.000 $               200.000 $
                                Accrued interest                                                   1.820 $
                                                                                                              Purchase,
                                     Operational                                                                                                     Interest
                                                                                                              Accrued                                                                      Sale
                                       Events                                                                                                        Payment
                                                                                                               Interest
                                                                            30.09.2018                        02.01.2019   31.01.2019 28.02.2019 31.03.2019                           30.06.2019


                                  FPSL System                                                                  Register
                                                                                                                           Period-End*                  Period-End*                   Period-End*
                                    Activities                                                                End-of-Day
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                      434
                                                                                                                                                                          * Period-End includes Day Processing




                             © SAP SE                                                                                                   IFPSLF                                                                         217

Multi Currency Accounting – Business Problem to be solved



                                            What is the information that is needed to manage foreign currencies?

                                            The information need is actually the current FX position in the balance sheet as a basis

                                            -       To understand the current FX exposure

                                            -       To determine the FX gain or loss due to changes in FX rates.

                                            Both information needs are already covered with the standard FX handling in FPSL.
                                            Multi currency accounting is only providing an explicitly posted FX position, resulting in more
                                            postings and more complex accounting logic.




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                 435




Duplication is prohibited.                                                                                                                                                              Duplication is prohibited.
                                   What is Multi Currency Accounting?

                                        •        You can use Multi Currency Accounting (MCA) to manage all accounts in their original
                                                 currency.
                                        •        You can make valuations in central foreign currency (FX) position accounts rather than in
                                                 individual balance sheet accounts.
                                        •        The FX positions document the currency risk and show currency fluctuations separately from
                                                 operational profits and losses.


                                                                                                  What are the information needs for foreign currency accounting?


                                                                What is the quantity and nature of my FX                               What is the value of my exposure in
                                                                               exposure?                                                      functional currency?


                                                                                                Currency Position                           Equivalent Value Position

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                 436




                             218                                                                                             IFPSLF                                          © SAP SE

Example MCA – ATM Withdrawal of 100 USD from EUR Account


                                                                                                                                        MAR                                 MCA
                                                                                                                                 FX valuation of FX                                Corresponding
                                                                           Single                                                                      FX valuation of FX
                                                                          contract               Position     Starting Balance     balance sheet                                    update of the
                                                                                                                                                       currency position*
                                                                            level                 level                              positions*                                   equivalent value*

                                                                                                                TC          FC     TC          FC        TC        FC               TC        FC
                                                                                                                     MOVE

                                                                      USD cash                                $ - 100   € - 80     $0         € - 10

                                                                      Corresponding
                                                                                                                                   $0       € + 10
                                                                      currency gain

                                                                      USD B/S position                        $ + 100   € + 80                           $0       € - 10

                                                                      Corresponding
                                                                                                                                                         $0       € + 10
                                                                      currency gain                            TRANSFORM

                                                                      USD equiv. value                        € - 80    € - 80                                                    € - 10     € - 10
                                                                                                                                                                                      FX Result
                                                                      Corresponding
                                                                                                                                                                                  € + 10    € + 10
                                                                      currency gain

                                                                      EUR cash                                € + 80    € + 80

                                                                                                                                                                                    * at period end
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                           437




Duplication is prohibited.                                                                                                                                                                                        Duplication is prohibited.


                                 Bond 3 Intraday Processing
                                 Move and Transform BT
                                 Demo




                             © SAP SE                                                                                                 IFPSLF                                                                219

Processes and Process Steps in FPSL - Move & Transform BT

                                          Day Processing                                                         Intraday                                                      Security Positions

                                              Set Posting                          Register                     Register      Register                                Define         Allocate       Determine        M&T
                                                                                                                                                     IAD
                                                 Date                                MD                           BT            AD                                     Lots            Lots         Price Gain        BT

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

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                      439




Duplication is prohibited.                                                                                                                                                                                                                   Duplication is prohibited.




                                                         Register 02.01.2019
                                                         Show BTs: Move and Transform
                                                         Legal Entity: DEMO_07
                                                         Posting Date 31.03.2019




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                      440




                             220                                                                                                                   IFPSLF                                                                         © SAP SE
