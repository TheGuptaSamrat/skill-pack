Classification: training-derived-concepts
Source basis: FPSL TRAINING DOCUMENT.pdf, pages 100-150
Trust usage: process flow illustration, method evaluation order, GL account mapping concepts
Do not use for: production data, customer-specific rules
Topics covered: loan accounting, interest accrual, amortized cost, GL posting, period-end processing

# Loan Example - Worked Process Flow
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

Example
                                                                                                                                                           Accounting Requirements
                                Basic Data - Loan
                                                                                                                                                           •   31.01./ 31.03./ … : Periodic financial statement (monthly
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
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                         201




Duplication is prohibited.                                                                                                                                                                                                                      Duplication is prohibited.
                                 Processes and Process Steps in FPSL – Classify

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

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                         202




                             © SAP SE                                                                                                             IFPSLF                                                                                  101

Loan End-of-Day
                                   Trigger
                                   Theory




Duplication is prohibited.                                                                                                          Duplication is prohibited.
                                   End-of-Day (Contract) – 3 Scenarios




                                   The following changes trigger period-end process steps in the End-of-Day
                                   Process:
                                       1. Master data change
                                       2. Analytical decision
                                       3. Updating executed period-end process steps




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER             204




                             102                                                                                IFPSLF   © SAP SE

End-of-Day (Contract)


                                     1st Scenario: Master Data Change
                                     ¾        If the master data change leads to a change in a subledger coding block dimension, the day
                                              end process (Contract) executes period-end process steps for the contract or securities
                                              position using the old subledger coding block characteristics.
                                     ¾        As a result, the system assigns the determined contributions to P&L to the subledger coding
                                              block before the master data change.
                                     ¾        Eventually the process step classify updates the position balances with the new subledger
                                              coding block characteristics.




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                  205




Duplication is prohibited.                                                                                                                               Duplication is prohibited.
                                 End-of-Day (Contract)

                                    2nd Scenario: Analytical Decision
                                    ¾        If the analytical status changes for a contract or securities position, end-of-day processing
                                             runs period-end process steps using the old subledger coding block characteristics.
                                    ¾        As a result, the system assigns the determined contributions to P&L to the subledger coding
                                             block before the analytical decision.
                                    ¾        Eventually the process step classify updates the position balances with the new subledger
                                             coding block characteristics.


                                    3rd Scenario: Updating executed Period-End Process Steps
                                    ¾        If the registered change has its origin at a time prior to already processed Period End
                                             Process or Day End Process, the process steps are re-run in the "End-of-Day processing".

                                    ¾        Therefore the relevant "period end process steps" are run using the information on the
                                             Journal Entries.
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                  206




                             © SAP SE                                                                         IFPSLF                               103

Loan End-of-Day
                                   Classify
                                   Demo




Duplication is prohibited.                                                                                                                                                     Duplication is prohibited.




                                   Transaction                                                                  Specs             System-Example     View/Variant
                                   /BA1/F1_CF_00_02                                                             Field: Org Unit   External Number:
                                    - Change Contract                                                                             DEMO01_LOAN_01
                                   /BA1/BR_REGISTER                                                             DEMO01
                                    - Register
                                   /BA1/BR_DAY_END_1                                                            DEMO01            DEMO01_LOAN_01
                                    - End-of-Day Processing (Contract)
                                                                                                                31.05.2018
                                   /BA1/BR_RESLT_VIEWER                                                                           DEMO01_LOAN_01
                                    - Nebenbuchbelege anzeigen
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                        208




                             104                                                                                        IFPSLF                                      © SAP SE

Loan End-of-Day
                                 Classify
                                 Theory




Duplication is prohibited.                                                                                                                                                                                               Duplication is prohibited.
                                 Classify Process Step
                                 If one or more subledger coding block characteristics change, the Classify process step ensures
                                 that the balances are reclassified from the old subledger coding block to the new subledger coding
                                 block.


                                                                                                                                            Subledger
                                                                                                                                           Coding Block
                                                                                                              А   Characteristic 1
                                                                                                              А   Characteristic 2
                                                                                                              А   Characteristic 3
                                                                                                              А   ……

                                                                                                                                              Derivation
                                                                                                                                               Rules


                                                                                                                                                                                                 Subledger
                                                                                                                    Subledger                                           Subledger
                                                                                                                     Account                                             Account
                                                                                                                                                                                                   level




                                                                                                                                                                                                  General
                                                                                                      GL Account                     GL Account            GL Account               GL Account    Ledger
                                                                                                                                                                                                   level



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                  210




                             © SAP SE                                                                                                             IFPSLF                                                           105

Classify Process Step - Example




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                 211




Duplication is prohibited.                                                                                                                                                                              Duplication is prohibited.
                                   Classify Process Step

                                   The Classify process step is capable to move the balance to a new subledger/general ledger
                                   account. The following cases are customizable to transfer balances between subledgers

                                                                                                                                                                 Val. Remnants: Fair Value
                                     Market Conformity Status                                                               Fair Value Adjustment
                                                                                                                                                                  Adj. Income/Expenses

                                                                                                                                                                 Val. Remn.: Income Credit
                                     Impairment Status                                                                      Credit Risk Adjustment
                                                                                                                                                                         Risk Adj.

                                                                                                                                                                 Val. Remnants: Fair Value
                                     Classification                                                                         Fair Value Adjustment
                                                                                                                                                                        Adj. Income



                                     Change in the dimension of financial statement entity:
                                     in this case the process is using a joker account because it is a cross-entity classification.
                                                                                                                Subledger             Reclassification Account          Subledger




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                 212




                             106                                                                                                IFPSLF                                                       © SAP SE

Agenda Part 2 – Additional Information on Day and Period-End Processing

                                                 Register – Suspense Accounting

                                                 Management of attribute changes

                                          –            End-of-Day Contract

                                          –            Classify

                                                 Register – Reverse BT

                                                 Period-End – Manual corrections (Adjust)




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER            213




Duplication is prohibited.                                                                                                         Duplication is prohibited.

                                 Loan Intraday Processing
                                 Register
                                 Special Topic Reverse Business Transaction
                                 Demo




                             © SAP SE                                                                         IFPSLF         107

Example
                                                                                                                                                  Accounting Requirements
                                   Basic Data - Loan
                                                                                                                                                  •   31.01./ 31.03./ … : Periodic financial statement (monthly
                                   Maturity                                                       01.01.2018 – 01.01.2028 (10 Years)                  reporting)
                                                                                                                                                  •   31.03.18: Suspense Accounting due to missing derivation rule
                                   Nominal                                                        1 000 000 €                                     •   31.05.18: Change of organizational unit

                                   Discount                                                       10 000 €                                        •   30.09.18: Closing passed posting periods
                                                                                                                                                  •   01.10.18: Reversal of interest payment, correction
                                   Nominal Interest                                               1.2%                                            •   31.12.18: Manual Adjustment, Year-End Processing

                                   Interest Payment                                              Quarterly                                        •   31.05.19: Impairment Attribute Determination

                                   Repayment                                                     Half-yearly

                                                                                                                 Suspense                                                                   Interest-
                                      Operational                                          Disburse-             Accounting
                                                                                                                                Change of       Interest-
                                                                                                                                                              Interest-                     Payment        Impairment
                                                                                                                              organizational    Payment                      Reversal
                                        Events                                               ment                 Interest-
                                                                                                                                  unit         Repayment
                                                                                                                                                              Payment                      Repayment       Write Down
                                                                                                                  Payment                                                                 Manual Adjust.


                                                                                       01.01.2018 31.03.2018 31.05.2018 30.06.2018 30.09.2018                               10.2018       31.12.2018 31.05.2019


                                    FPSL System                                           Register
                                                                                                                Period End Period End Period End Period End                                Year End Period End
                                      Activities                                       End-of-day
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                      215




Duplication is prohibited.                                                                                                                                                                                                   Duplication is prohibited.




                                   Transaction                                                                                    Specs               System-Example                            View/Variant
                                   /BA1/F2_BT_COPY                                                                                Reverse BT          BT:
                                    - Create Business Transaction by Copying                                                                          LOAN_01_INT_1803_01_DEMO
                                   /BA1/BR_REGISTER                                                                               DEMO01
                                    - Register
                                   /BA1/BR_RESLT_VIEWER                                                                                               DEMO01_LOAN_01
                                    - Nebenbuchbelege anzeigen


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                      216




                             108                                                                                                           IFPSLF                                                                 © SAP SE

Loan Intraday Processing
                                 Register
                                 Reverse Business Transaction
                                 Theory




Duplication is prohibited.                                                                                                                                                             Duplication is prohibited.
                                 Reversal of Business Transactions

                                                                  Reversal                                              Further “inversions”
                                                                  A reversal business transaction will be               Inversion
                                                                  delivered from source systems carrying the
                                                                                                                        Inversion mode revokes postings that were
                                                                  same values as a the original transaction
                                                                                                                        made earlier e.g. while reprocessing
                                                                  (reversal by value), but with a reversal




                                         Register Sub-Steps
                                                                                                                        backdated changes / business transactions.
                                                                  indicator.
                                                                  Neither the reversed journal entry nor the            Reset
                                                                  reversal journal entry can be reversed again.
                                                                                                                        Some postings as part of period end
                                                                                                                        processing will be created with the intention to
                                                                  − Follows same logic as registration of               invert them at the beginning of the next
                                                                    business transaction                                period. (open period processing)
                                                                                                                        − Manual adjustments
                                                                  − Reversal indicator and reference to
                                                                                                                        − Reset of period end postings
                                                                    reversed document are set
                                                                  − Debit/ Credit indicator remains is kept             All “inversions” are getting executed
                                                                                                                        technically in the same way (see Reversal),
                                                                  − Change sign of the amount in transaction            but flags are documenting what kind of
                                                                    currency (= *-1)                                    inversion has been applied.

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                218




                             © SAP SE                                                                          IFPSLF                                                            109

Reverse-BT – System View

                                   SAP Menu Location




                                   Selection Screen




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER             219




Duplication is prohibited.                                                                                                          Duplication is prohibited.


                                   Loan Period-End Processing
                                   Close




                             110                                                                                IFPSLF   © SAP SE

Period Close – Business Motivation




                                          •        At the end of the period a company has to have a complete representation of the business
                                                   represented in the financial statement as of period end date.

                                          •        This include the update of all book value components.

                                          •        If all numbers are completed and validated, period need to be protected against further
                                                   changes




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                   221




Duplication is prohibited.                                                                                                                                Duplication is prohibited.


                                 Loan Period-End Processing
                                 Close
                                 Demo




                             © SAP SE                                                                         IFPSLF                                111

Transaction                                                                   Specs                       System-Example       View/Variant
                                   /BA1/BR_PPER                                                                  Open Posting Periods from   DEMO01
                                   - Open and Close Posting Periods                                              10 2018 to …*
                                   /BA1/F2_BT_COPY                                                               With Dates 30.09.           LOAN_01_DISB_1801_
                                    - Create Business Transaction by Copying                                     LOAN_01_INTPAY_TEST         01
                                   /BA1/F2_BT_COPY                                                               Reverse BT
                                    - Create Business Transaction by Copying                                     LOAN_01_INTPAY_TEST_
                                                                                                                 S
                                    © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                    223




Duplication is prohibited.                                                                                                                                                                  Duplication is prohibited.


                                    Loan Period-End Processing
                                    Close
                                    Theory




                             112                                                                                          IFPSLF                                                 © SAP SE

Close – Definition and Characteristics

                                            Definition                                                               Process step
                                            After a period is closed for intraday                                    You can use the Close process step to open and
                                            processing, operational flow transactions and                            close posting periods (including special periods) for
                                            master data changes no longer affect period-                             each legal entity.
                                            end processing. Accordingly, for the period
                                            end, the adjustments made in the individual                              Transaction: /BA1/BR_PPER - Open and Close
                                            process steps in period-end processing no                                Posting Periods
                                            longer affect the manual adjustments.


                                                                                                              Open / Close




                                                                            Intraday Processing               Period-End
                                                                                                                                    Manual Adjustments
                                                                                 (Register)                   Processing

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                  225




Duplication is prohibited.                                                                                                                                                               Duplication is prohibited.
                                 Closing Process Step – System View

                                   Period opening
                                   and closing takes
                                   place on the level
                                   of the legal entity.




                                   Three different
                                   entities for
                                   closing:
                                   • Intraday
                                   • Periodic
                                   • Manual




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                  226




                             © SAP SE                                                                           IFPSLF                                                             113

Break (15min)




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                    227




Duplication is prohibited.                                                                                                                 Duplication is prohibited.
                                   Quiz




                                         1.          What is/ are the advantage/s of suspense accounting?

                                         2.          In which cases executes the End of Day Process Period end process steps?

                                         3.          What happens if a period is closed?




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                    228




                             114                                                                                     IFPSLF     © SAP SE

Agenda Part 2 – Additional Information on Day and Period-End Processing

                                                 Register – Suspense Accounting

                                                 Register – Reverse BT

                                                 Management of attribute changes

                                          –            End-of-Day Contract

                                          –            Classify

                                                 Period-End – Manual corrections (Adjust)




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER            229




Duplication is prohibited.                                                                                                         Duplication is prohibited.


                                 Loan Period-End Processing
                                 Special Topic Manual Correction - Adjust
                                 Demo




                             © SAP SE                                                                         IFPSLF         115

Example
                                                                                                                                                             Accounting Requirements
                                   Basic Data - Loan
                                                                                                                                                             •   31.01./ 31.03./ … :Periodic financial statement (monthly
                                   Maturity                                                       01.01.2018 – 01.01.2028 (10 Years)                             reporting)
                                                                                                                                                             •   31.03.18: Suspense Accounting due to missing derivation rule
                                   Nominal                                                        1 000 000 €                                                •   31.05.18: Change of organizational unit

                                   Discount                                                       10 000 €                                                   •   30.09.18: Closing passed posting periods
                                                                                                                                                             •   01.10.18: Reversal of interest payment, correction
                                   Nominal Interest                                               1.2%                                                       •   31.12.18: Manual Adjustment, Year-End Processing

                                   Interest Payment                                              Quarterly                                                   •   31.05.19: Impairment Attribute Determination

                                   Repayment                                                     Half-yearly

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
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                          231




Duplication is prohibited.                                                                                                                                                                                                                       Duplication is prohibited.
                                   Processes and Process Steps in FPSL – Adjust

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

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                          232




                             116                                                                                                                    IFPSLF                                                                            © SAP SE

Transaction                                                                    Specs            System-Example   View/Variant
                               /BA1/BR_ADJUST_MD
                                - Manual Posting (Contract)
                               /BA1/HW_RESULTVIEWER                                                           SAFI             DEMO01_LOAN_01
                                - Ergebnisdaten anzeigen
                                                                                                              _S_PSLPD
                               Sbwp
                               - SAP BUSINESS WORKSPACE

                               /BA1/BR_RESLT_VIEWER                                                                            DEMO01_LOAN_01
                               - Nebenbuchbelege anzeigen
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                    233




Duplication is prohibited.                                                                                                                                                 Duplication is prohibited.


                                 Loan Period-End Processing
                                 Manual Correction - Adjust
                                 Theory




                             © SAP SE                                                                                 IFPSLF                                         117

Adjust Process Step

                                      Definition                                                                                                    Process Step

                                      The Adjust process step is in charge of posting manual adjustment                                             In the Adjust process step, you can first
                                      entries to Manual Adjustment Subledgers (same way as in G/L).                                                 manually make preliminary entries for
                                                                                                                                                    contract-related or cross-contract value
                                      Manual postings can be required if data (e.g. for interest settlement)                                        adjustments to balances or import them, and
                                      from the feeder system is not imported in time for period-end                                                 then post them using a release workflow. You
                                      processing.                                                                                                   can reset the manual postings during period-
                                                                                                                                                    opening processing, if necessary.
                                      The process requires the approval of another employee. If the
                                      corrections are not approved, they can be reversed by using
                                      transaction /BA1/BR_ADJUST_RESET - Reset Manual Posting
                                      before the corrections are posted in the subledger.

                                                                                  Transactions:
                                                                                  /BA1/BR_ADJUST_MD - Manual Posting (Contract)
                                                                                  /BA1/BR_ADJUST - Manual Posting (Cross-Contract)
                                                                                                                                                            Adjust
                                                                                  Import:
                                                                                  Preliminary Subledger Documents (Result Category 905)

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                      235




Duplication is prohibited.                                                                                                                                                                               Duplication is prohibited.
                                   Adjust Process Step


                                   The process allows you to enter the following values:

                                                      Cross-Contract-based Characteristics                                                       Contract-based Characteristics
                                                                                        (/BA1/BR_ADJUST)                                               (/BA1/BR_ADJUST_MD)

                                                   • GL Account                                                 • Accrual Status
                                                                                                                                               • Accounting Change
                                                   • Lifecycle Segment • Impairment Status
                                                                                                                                               • Business Tranche
                                                   • Product Segment                                            • Market Conf. Status
                                                                                                                                               • Transaction Type
                                                   • Asset Liability                                            • Write Down Status
                                                     Status
                                                                                                                • Fair Value level
                                                   • Classification


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                      236




                             118                                                                                                      IFPSLF                                                 © SAP SE

Adjust Process Step - Workflow
                                                                                                                   A need for manual correction has been identified



                                                                                                              The correction has been performed (transaction or import)



                                                                                                                                 Review of the adjustments
                                                                                                                                 (SAP Business Workplace)


                                                                                                                         Release                       Rejection


                                                                                                                 Generation of a new
                                                                                                                    journal entry
                                                                                                              (with reference to the preliminary
                                                                                                                         journal entry)
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                               237




Duplication is prohibited.                                                                                                                                                            Duplication is prohibited.
                                 Agenda Part 2 – Special Topics and Summary

                                 5.          Year-End Processing

                                                 Carry Forward

                                 6.          Special Topics

                                                 Impairment Attribute Determination

                                                 Write Down

                                 7.          Summary of Part 2




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                               238




                             © SAP SE                                                                                                     IFPSLF                                119

Loan Year-End Processing

                                   Demo




Duplication is prohibited.                                                                                                                                                                                                  Duplication is prohibited.
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
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                      240




                             120                                                                                                           IFPSLF                                                                © SAP SE

Processes and Process Steps in FPSL – Carry Forward

                                        Day Processing                                                         Intraday                                                      Security Positions

                                            Set Posting                          Register                     Register      Register                                Define         Allocate       Determine         M&T
                                                                                                                                                   IAD
                                               Date                                MD                           BT            AD                                     Lots            Lots         Price Gain         BT

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
                                                                                                                                                    Determine      Determine Amort.       Determine Adj.        Determine Fair
                                                Close                                   Carry Forward                         Allocate
                                                                                                                                                  Amortized Cost    Valuation Cost        for Credit Risk           Value

                                        Open and Close                           Balance Carry Forward
                                        Posting Periods                            (Cross/-Contract)

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                      241




Duplication is prohibited.                                                                                                                                                                                                                   Duplication is prohibited.




                               Transaction                                                                                             Specs               System-Example                                   View/Variant
                               /BA1/BR_BCF_1                                                                                           DEMO01
                                - Balance Carryforward (Contract)                                                                      2019
                               /BA1/BR_RESLT_VIEWER                                                                                                        DEMO01_LOAN_01
                               - Nebenbuchbelege anzeigen

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                      242




                             © SAP SE                                                                                                            IFPSLF                                                                                121

Loan Year-End Processing
                                   Carry Forward
                                   Theory




Duplication is prohibited.                                                                                                                                                                                Duplication is prohibited.
                                   Carry Forward Process Step


                                          You use Year-End processing to open and close fiscal years.


                                                                                                       Period-End                                  Note      that   neither     the    Carry
                                                                                                        (Prerequisite)                             Forward        process       step     nor
                                                                                                                                                   the Adjust process step automatically
                                                                                                                                                   react to adjustments. Since the preceding
                                                                                                                                                   posting periods must already be closed
                                                                                                         Year-End                                  there is no need for an automated
                                                                                                                                                   adjustment function in the system here.
                                                                            Adjust                                Carry Forward                    You can use the Carry Forward process
                                                             Period-end processing                                Balance                          step to manually make a selective
                                                             for special periods                                  carryforward function            correction.




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                   244




                             122                                                                                                          IFPSLF                                               © SAP SE

Carry Forward Process Step - Example
                                                                        Period 00                                   …                                                 Period 12
                                                     Opening balances as of 2018-01-01                                                      Profit and loss statement            Closing balance as of 2018-12-31



                                   2018
                                                                                                      Equity                                                                                                     Equity
                                                             Assets                                                               Expenses                       Income            Assets
                                                                                                  Liabilities                                                                                                   Liabilities
                                                                                                                                                  Profit




                                                                                                                                  Carry Forward
                                                     Opening balances as of 2019-01-01




                                                                                                                                                                                    Carry Forward                Carry Forward
                                   2019
                                                                                                      Equity
                                                             Assets
                                                                                                  Liabilities




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                      245




Duplication is prohibited.                                                                                                                                                                                                                   Duplication is prohibited.
                                 Carry Forward Process Step – Handling of Special Features


                                          The process is moving the balances in                                                                            Note:
                                          the following order:
                                                                  Currency
                                                                                                                                                           In case of changes in the balance of the last
                                                                                                                  Currency                                 day of the old fiscal year, it is necessary to
                                                                position Profit
                                             1                                                                    position                                 run the Carry forward process again. The
                                                                  and Loss
                                                                                                                  Reserve
                                                                 Statement                                                                                 previous initial positions will be reversed,
                                                                                                                                                           and the new values will be posted.
                                                               Year-opening                                      Preliminary
                                             2                  positions in                                      Retained
                                                             foreign currency                                     Earnings                                                                            Carry
                                                                                                                                                                      Carry
                                                                                                                                                                                                     Forward
                                                                                                                                                                     Forward
                                                                                                                                                                                                     (Cross-
                                                                                                                                                                    (Contract)
                                                                                                                Carried to next                                                                     Contract)
                                                                Postings with
                                                                                                                 fiscal year in
                                             3                  value dates >
                                                                                                                  order to be
                                                                 End of Year
                                                                                                                   preserved



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                      246




                             © SAP SE                                                                                             IFPSLF                                                                                               123

Carry Forward Process Step

                                    Posting Documents
                                    The posting documents are registered in the table /BA1/HFSPD.
                                    Also available in the transaction /BA1/HW_RESULTVIEWER - Display Results Data.




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                            247




Duplication is prohibited.                                                                                                                                         Duplication is prohibited.
                                   Carry Forward – Account Assignment



                                                                                                   Profit and Loss                      Equity

                                                                                                                Income                  Equity




                                                                                                    Balance Sheet                    Balance Sheet

                                                                                         Balance Sheet Items                      Balance Sheet Items




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                            248




                             124                                                                                         IFPSLF                         © SAP SE

Agenda Part 2 – Special Topics and Summary

                                 5.          Year-End Processing

                                                 Carry Forward

                                 6.          Special Topics

                                                 Impairment Attribute Determination

                                                 Write Down

                                 7.          Summary of Part 2




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER            249




Duplication is prohibited.                                                                                                         Duplication is prohibited.


                                 Loan Intraday Processing
                                 Impairment Attribute Determination
                                 Demo




                             © SAP SE                                                                         IFPSLF         125

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
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                      251




Duplication is prohibited.                                                                                                                                                                                                  Duplication is prohibited.
                                   Data Model

                                                        Master Data                                                  Additional                        Flow Data                     Key Date Values
                                                                                                                  Information on
                                                Contract                                                           Master Data
                                                                                Business                                                         Business                            Target
                                                                                                                                                                Cash Flow
                                                                                 Partner                        Analytical                      Transaction                          Values
                                                                                                                 Status
                                                                                 Portfolio




                                                                                  Calculation Rates                               Journal Entries                     Market Data
                                                                                    and Factors
                                                                                                                              Subledger Journal Entry
                                                                                               Impairment
                                                                                                Attributes




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                      252




                             126                                                                                                           IFPSLF                                                                © SAP SE

Data Model – Calculation Rates and Factors – Impairment Attributes


                                                   1. Calculation Rates and Factors – Impairment Attributes




                                                  2. A look into the system
                                                  /BA1/HW_RESULTVIEWER
                                                  Result Area / Resultview: SAFI / _S_SCT_IMP

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                     253




Duplication is prohibited.                                                                                                                                                                                                                  Duplication is prohibited.
                                 Processes and Process Steps in FPSL – IAD

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

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                     254




                             © SAP SE                                                                                                            IFPSLF                                                                               127

Transaction                                                                   Specs            System-Example   View/Variant
                                   Hier noch das ausführen, was für das Impairment
                                   notwendig ist. Bzw. Falls RDL Uploads
                                   notwendig, können diese auch bereits im System
                                   vorgelegt werden.
                                   /BA1/HW_RESULTVIEWER                                                          SAFI             DEMO01_LOAN_01
                                    - Display Results Data
                                                                                                                 _S_SCT_IMP
                                   /BA1/BR_REGISTER                                                              DEMO01
                                    - Register
                                   /BA1/BR_IAD                                                                   31.01.2019
                                    - Determine Impairment Attributes
                                   /BA1/BR_DAY_END_1                                                             31.01.2019
                                    - End-of-Day Processing (Contract)
                                   /BA1/HW_RESULTVIEWER                                                          SAFI             DEMO01_LOAN_01
                                    - Display Results Data
                                                                                                                 _S_SC_STSS
                                   /BA1/HW_RESULTVIEWER                                                          SAFI             DEMO01_LOAN_01
                                    - Display Results Data
                                    © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER
                                                                                                                 _S_SCT_STS                                        255




Duplication is prohibited.                                                                                                                                                   Duplication is prohibited.


                                    Loan Intraday Processing
                                    Impairment Attribute Determination
                                    Theory




                             128                                                                                         IFPSLF                                   © SAP SE

Impairment Attribute Determination – Definition and Characteristics

                                            Definition                                                                   Process step
                                            The IAD is necessary if the impairment                                       The process determines the impairment status for
                                            stages are not imported. In this case, the                                   each accounting system. The criteria are the due
                                            process Impairment Attribute                                                 dates (based on threshold logic) and the master
                                            Determination (IAD) determines the                                           rating (either relative or absolute).
                                            impairment status and accrual status.




                                            Responsibilities                                                             Result
                                            The IAD determines the                                                       As a result, the IAD process writes the impairment
                                            1. Accrual Status                                                            status and accrual status if there has been a
                                            2. Impairment Stage                                                          change. It also informs the Register process of an
                                            The Accrual Status is an accounting status                                   analytical decision (through the status change) by
                                            used during the Defer process.                                               storing the underlying contract or securities position
                                            The Impairment Stage is used to document                                     in the Register worklist.
                                            credit risk in the Value TC process step.
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                        257




Duplication is prohibited.                                                                                                                                                                     Duplication is prohibited.
                                 Impairment Attribute Determination - IAD



                                                                                                                                             Determination for each accounting
                                  Delinquency Band (DB)                                                                  Accrual             system based on the DB.
                                  Days past due:                                                                         Status

                                  0           30            60           90 t [days]
                                                                                                                                             Determination for each accounting
                                                                                                                       Impairment            system based on DB and MR. If there
                                                                                                              IAD
                                  Master Rating (MR)                                                                     Status              are both, the lower quality status is
                                                                                                                                             used as the result.
                                  1.          Relative: Depends on initial
                                              rating
                                                                                                                    The IAD informs the Register process of an analytical decision
                                  2.          Absolute                                                              (through the status change) by storing the underlying contract or
                                              AAA              BB+              CCC-                D               the underlying securities position in the Register worklist.




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                        258




                             © SAP SE                                                                               IFPSLF                                                               129

Recap – Impairment stages – Value TC

                                                                                                                               Impairment Stage 1
                                                                                                                              One-year Expected Loss
                                                                                                                              ¾ At initial recognition

                                                Customer
                                               Impairment                                                                     Impairment Stage 2
                                               Calculation
                                                                                                                              Lifetime Expected Loss
                                                                                                                              ¾     If a loan’s credit risk has increased significantly since
                                                   Imported                                                                         initial recognition and is exceeding a certain threshold
                                                    Target
                                                     Value                                                                    Impairment Stage 3
                                                                                                                              Lifetime Expected Loss
                                                                                                                              Expected Cash Flow
                                                                                                                              ¾ If the loan’s credit reaches the point where it is
                                                                                                                                considered credit-impaired



                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                      259




Duplication is prohibited.                                                                                                                                                                                  Duplication is prohibited.
                                   Value TC – Credit Risk Adjustment – Calculation Base


                                                 One-year Expected Loss
                                                                                                                ܴܲ ൌ ‫ ܦܣܧ‬ൈ ܲ‫ ܦ‬ൈ ‫ܦܩܮ‬

                                                                                                                 ௡                                                       where
                                                 Lifetime Approach                                                                                                       ܴܲ Risk Provision
                                                                                                        ܴܲ ൌ ෍ ‫ܦܣܧ‬௜ ൈ ‫ܦܩܮ‬௜ ൈ ܲ‫ܦ‬௜ ൈ ݁ ିாூோ ሺ௧೔షభ ି௧ሻ                      ‫ ܦܣܧ‬Exposure At Default
                                                                                                                                                                         ܲ‫ ܦ‬Probability of Default
                                                                                                                ௜ୀଵ
                                                                                                                                                                         ‫ ܦܩܮ‬Loss Given Default
                                                                                                                         ௭                                               ݅ Number of „maturity band“
                                                                                                                ‫ܦܣܧ‬௜ ൌ ෍ ‫ܨܥ‬௞ ൈ ݁ ିாூோ ሺ௧ೖషభି௧ሻ                           ݇ Number of CF items
                                                                                                                                                                         ‫ ܲܯܫ‬Credit risk adjustment
                                                                                                                       ௞ୀଵ                                               ‫ ܥܸܤܤ‬Balance of the book value



                                                  Expected Cash Flow Approach
                                                               ‫ܲܯܫ‬ா஼ி ‫ ݐ‬ൌ ‫ܥܸܤܤ‬ூெ௉ ‫ ݐ‬െ ෍ ‫ܨܥ‬௜ ݁ ିாூோሺ௧೔ ି௧ሻ
                                                                                                                                  Present value of the ECF
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                      260




                             130                                                                                             IFPSLF                                                              © SAP SE

Non-Accruing Status


                                               Definition                                                                                   Process step
                                               If it is no longer likely that a contract                                                    Since the accrual status is set based on accounting
                                               partner will meet their contractual                                                          system, the non-accrual method cannot be applied
                                               obligations, you can identify contracts and                                                  until the first GAAP-dependent process step runs
                                               securities positions for non-accrual                                                         which is the Defer process step. The non-accrual
                                               processing. This means that value date                                                       methodology of the Defer process step offsets value
                                               income continues to be collected or                                                          date income items generated in the Register,
                                               invoiced from an operational perspective,                                                    Accrue and Defer process steps by transferring
                                               but does not need to be reported as                                                          them to the corresponding offset accounts.
                                               income.
                                               The non-accruing status is purely an
                                               accounting status, and is used solely to                                                     Methods
                                               control the profit and loss statement. From                                                  Two methods are provided
                                               an operational system perspective,                                                           1. Cost Recovery Method
                                               receivables due can continue to be                                                           2. Cash Method
                                               recognized as debit entries in spite of
                                               delinquency.

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                   261




Duplication is prohibited.                                                                                                                                                                                Duplication is prohibited.
                                 Non-Accruing Status – Provided Methods

                                 The IAD determines the accruing status which is used by the Defer process for the
                                 accounting of contracts that have been set to non-accruing status.

                                                                                                               All the income for the current fiscal year with status non-accruing is
                                           Cost Recovery                                                       transferred to the respective offset account. No value date income is
                                                                                                               recorded in the profit and loss statement, and the balance sheet asset
                                              Method
                                                                                                               is reduced.




                                                                                                              All the income for the current fiscal year (reporting period) is transferred
                                                                                                              to the offset account. The balance of the offset account is limited by the
                                             Cash Method                                                      balance of a reference account from the account group 100801
                                                                                                              (Receivables/Payables (Due)). Only value date income for which there
                                                                                                              is an outstanding receivable is transferred to the offset account, others
                                                                                                              remain in the P & L statement.

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                   262




                             © SAP SE                                                                                                 IFPSLF                                                        131

Agenda Part 2 – Special Topics and Summary

                                   5.          Year-End Processing

                                                   Carry Forward

                                   6.          Special Topics

                                                   Impairment Attribute Determination

                                                   Write Down

                                   7.          Summary of Part 2




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER             263




Duplication is prohibited.                                                                                                          Duplication is prohibited.


                                   Loan Period-End Processing
                                   Impairment - Write Down
                                   Demo




                             132                                                                                IFPSLF   © SAP SE

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




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                           265




Duplication is prohibited.                                                                                                                                                                        Duplication is prohibited.
                                 Data Model – Additional Information – Analytical Status

                                     1. Analytical Status




                                    2. A look into the system
                                    /BA1/HW_RESULTVIEWER - Display Results Data
                                    Result Area / Resultview: SAFI / _S_SC_STS

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                           266




                             © SAP SE                                                                                               IFPSLF                                                  133

Processes and Process Steps in FPSL – Write Down

                                          Day Processing                                                         Intraday                                                           Security Positions

                                              Set Posting                          Register                     Register        Register                                   Define         Allocate       Determine        M&T
                                                                                                                                                        IAD
                                                 Date                                MD                           BT              AD                                        Lots            Lots         Price Gain        BT

                                                                                                                                               Impairment Attribute
                                                                                                                 Register                                                                    End-of-Day Process
                                                                                                                                                 Determination


                                          Day-End Processing / Period-End Processing

                                                                                                            Write                             Value       Move and         Value                         Classify
                                                    Accrue                      Defer                                          Release                                                   Classify                        Adjust
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

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                             267




Duplication is prohibited.                                                                                                                                                                                                                        Duplication is prohibited.
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



                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                             268




                             134                                                                                                                      IFPSLF                                                                           © SAP SE

Transaction                                                                    Specs            System-Example   View/Variant
                               /BA1/BR_PERIOD_END_1                                                           DEMO01
                                - Period-End Processing (Contract)
                                                                                                              31.01.2019
                               /BA1/BR_RESLT_VIEWER                                                                            DEMO01_LOAN_01
                               - Nebenbuchbelege anzeigen


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                    269




Duplication is prohibited.                                                                                                                                                 Duplication is prohibited.


                                 Loan Period-End Processing
                                 Write Down
                                 Theory




                             © SAP SE                                                                                 IFPSLF                                         135

Write Down Process Step
                                              Definition                                                                       Process Step
                                              A nominal write-down is an analytical write-                                     The Write Down process step is an analytical
                                              down on the long-term receivables without                                        process step in charge of documenting the
                                              an operational waiver of debt repayments.                                        changes in the nominal write-down.


                                               Write-Down can be triggered by the following processes:
                                                   1. Day-End                                                              2. Period End
                                                   •      /BA1/BR_DAY_END_BT_1 - End-of-Day Processing                     •   /BA1/BR_PERIOD_END_1 - Period-End Processing
                                                          (Business Transaction)                                               (Contract)
                                                   •      /BA1/BR_DAY_END_1 - End-of-Day Processing                        •   /BA1/BR_PER_END_CX_1 - Period-End Processing
                                                          (Contract)                                                           (Cross-Contract)



                                              ¾        If the analytical status changes for a contract or securities position, end-of-day processing closes the period.
                                              ¾        Therefore the relevant period end process steps are run using the old subledger coding block characteristics.
                                              ¾        Eventually the process step classify updates the position balances with the new subledger coding block
                                                       characteristics.
                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                  271




Duplication is prohibited.                                                                                                                                                               Duplication is prohibited.
                                   Write Down - Methods


                                                                                                                 Methods
                                                                                                                       Import
                                                                                                                Exception Processing




                                                                                                                Custom Determination

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                  272




                             136                                                                                        IFPSLF                                                © SAP SE

Write Down – Account Assignment




                                                                                                   Balance Sheet            Profit and Loss

                                                                                      Write-Down (Nominal)                     Income




                                                                                                                              Expense




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                   273




Duplication is prohibited.                                                                                                                                Duplication is prohibited.
                                 Quiz




                                       1.          What happens if a period is closed and a business transaction is delivered
                                                   late with a posting date in the closed period?

                                       2.          What is the benefit of manual adjustments?

                                       3.          Which parameters are needed for the Impairment Attribute Determination?




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                   274




                             © SAP SE                                                                              IFPSLF                           137

Summary




Duplication is prohibited.                                                                                                                                                                                                                   Duplication is prohibited.
                                   Processes and Process Steps in FPSL – Complete

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

                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                      276




                             138                                                                                                                   IFPSLF                                                                         © SAP SE

Objectives




                                              You should now be able to:
                                              • Obtain a detailed understanding of the processes and process steps in FPSL and their
                                                connection to the according book value components
                                              • Understand the connection between the data model and the process steps
                                              • Create and upload data
                                              • Perform all steps necessary to process a LOAN
                                              • Analyze errors based on suspense accounts
                                              • Check for target values in the according tables
                                              • Analyze Journal Entries




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                            277




Duplication is prohibited.                                                                                                                         Duplication is prohibited.
                                 Q&A


                                 Questions?



                                 End of Part 2




                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                            278




                             © SAP SE                                                                         IFPSLF                         139

Agenda Part 2 – Special Topics and Summary

                                   5.          Year-End Processing

                                                   Carry Forward

                                   6.          Special Topics

                                                   Impairment Attribute Determination

                                                   Write Down

                                                   Cost Allocation

                                   7.          Summary of Part 2




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER             279




Duplication is prohibited.                                                                                                          Duplication is prohibited.


                                   Introduction Loan Example

                                   Cost Allocation




                             140                                                                                IFPSLF   © SAP SE

Loan Example 2 – Cost Allocation
                                                                                                                                                               Accounting Requirements
                                Basic Data - Loan
                                                                                                                                                               •   Periodic financial statement (monthly reporting 31.01. / 28.02. /
                                Maturity                                                        01.01.2018 – 01.01.2028 (10 Years)                                 31.03. / …)
                                                                                                                                                               •   Allocation of primary costs solu3
                                Nominal                                                         1 000 000 €

                                Discount                                                        10 000 €

                                Nominal Interest                                                1.2%

                                Interest Payment                                               Quarterly                                                       Error Conflict Handler

                                Repayment                                                      Half-yearly


                                    Operational                                       Disburse-                                                                 Interest-
                                                                                                                                         Interest-
                                      Events                                            ment                                                                    Payment
                                                                                                                                         Payment
                                                                                                                                                               Repayment

                                                                                     01.01.2018                     31.01.2018         31.03.2018              30.06.2018


                                  FPSL System                                           Register
                                                                                                                   Period End          Period End              Period End
                                    Activities                                      End-of-day
                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                       281




Duplication is prohibited.                                                                                                                                                                                                                    Duplication is prohibited.
                                       Allocate Process Step – Direct and Indirect Costs
                                                                                                                                                Costs and
                                                                                                                                                Revenue


                                                                                                              Direct Costs                                                     Indirect Costs
                                                                                                              and Revenue



                                                                          Incremental                                            Non-incremental                             Non-incremental
                                                                        (variable) Costs                                          (fixed) Costs                               (fixed) Costs
                                                                         and Revenue
                                                                                                                             Direct Secondary Costs                     Indirect Secondary Costs
                                                             Primary Costs and Revenue                                        (internal activity allocation)                   (overhead costs)


                                                         •    Income from interest                                        • Claim settlement costs                    • Overhead costs (marketing)


                                                                                                                Revenue
                                                         •    Fee and commission income                                   • Loan administration costs                 • Overhead costs (sales)
                                                         •    Premium income                                              • etc                                       • etc
                                                         •    etc
                                                                                                                                     Method 1                                    Method 2
                                                         • Interest expense
                                                                                                                                     based on                                    based on
                                                                                                                Costs
                                                         • Claim expense
                                                         • etc                                                                     Primary Costs                                time series


                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                       282




                             © SAP SE                                                                                                              IFPSLF                                                                               141

Data Model – Calculation Rates and Factors – Cost Rates

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
                                                                                   Impairment Attributes

                                                                                               Cost Rates
                                                                                                                                                         Prices/ Rates for Financial
                                                                                                                                                                 Instruments
                                                                                              Cost Vector


                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                 283




Duplication is prohibited.                                                                                                                                                                              Duplication is prohibited.
                                   Calculation Rates and Factors – Cost Rates and Cost Vectors

                                           1. Cost Rates




                                           2. A look into the system
                                           /BA1/HW_RESULTVIEWER - Display Results Data
                                           Result Area / Resultview: SAFI / _S_SCT_COR



                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                 284




                             142                                                                                                      IFPSLF                                                 © SAP SE

Loan Period-End Processing
                                 Allocate (Primary Costs)
                                 Demo




Duplication is prohibited.                                                                                                                                                                                                                  Duplication is prohibited.
                                 Processes and Process Steps in FPSL

                                        Day Processing                                                         Intraday                                                      Security Positions

                                            Set Posting                          Register                     Register      Register                                Define         Allocate       Determine        M&T
                                                                                                                                                   IAD
                                               Date                                MD                           BT            AD                                     Lots            Lots         Price Gain        BT

                                                                                                                                          Impairment Attribute
                                                                                                               Register                                                               End-of-Day Process
                                                                                                                                            Determination


                                        Day-End Processing / Period End Processing

                                                                                                          Write                          Value       Move and       Value                         Classify
                                                  Accrue                      Defer                                       Release                                                 Classify                        Adjust
                                                                                                          Down                            TC         Transform       FX                             P&L

                                                                                                                                                                                                                  Manual
                                                                                                                          Day-End Process / Period End Process
                                                                                                                                                                                                                  Posting



                                        Period End                              Year-End Processing                        Across                Preparatory Processing
                                        Processing
                                                                                                                                                    Determine      Determine Amort.       Determine Adj.       Determine Fair
                                                Close                                   Carry Forward                         Allocate
                                                                                                                                                  Amortized Cost    Valuation Cost        for Credit Risk          Value

                                        Open and Close                           Balance Carry Forward
                                        Posting Periods                            (Cross/-Contract)

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                                                     286




                             © SAP SE                                                                                                            IFPSLF                                                                               143

Interactive:
                                                         Show Postings and ask audience where to find the configuration




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER              287




Duplication is prohibited.                                                                                                           Duplication is prohibited.
                                   Allocate Process Step – Primary Costs Example




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER              288




                             144                                                                                IFPSLF    © SAP SE

Loan Period-End Processing
                                 Allocate (Primary Costs)
                                 Theory




Duplication is prohibited.                                                                                                                              Duplication is prohibited.
                                 Allocate Process Step – Primary Costs

                                        The Allocate Primary Costs process step reallocates one amount (that was posted by
                                        any process step in subledger accounting) partially or completely to further subledger
                                        accounts and further cost or revenue elements in the profit and loss statement or the
                                        balance sheet.

                                             1. Document-based Allocation

                                             Based on two factors:

                                               Calculation Base                                               Calculation
                                                                                                              Factors
                                               Amount of
                                               Recognition                                                    a.   Fixed value
                                                                                                              b.   Cost/Revenue
                                                                                                                   rate (Import)



                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                 290




                             © SAP SE                                                                                              IFPSLF         145

Allocate Process Step - Document-based Allocation: Example

                                                                               In the Register process step, EUR 10 interest income has been recognized in the profit and loss
                                                                               statement.
                                                                              Posting                           Document   Document    Subledger         Debit /        Amount in        Accounting
                                                                              date                              Number     Line Item   Account           Credit         EUR              Principle
                                                                              30.10.2018                        1          1           Receivable        D              -10              Central
                                                                                                                                                                                         GAAP
                                                                                                                           2           Interest Income   C              10




                                                                               For the accounting principle IFRS, 10% of the recognized interest income needs to be reallocated to fee
                                                                               and commission income. The system does so by adding further GAAP-dependent line items:
                                                                              Posting                           Document   Document    Subledger         Debit /        Amount in       Accounting
                                                                              date                              Number     Line Item   Account           Credit         EUR             Principle
                                                                              30.10.2018                        1          3           Interest Income   D              -1              IFRS

                                                                                                                           4           Fee &             C              1
                                                                                                                                       Commission
                                                                                                                                       Income




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                          291




Duplication is prohibited.                                                                                                                                                                                       Duplication is prohibited.
                                   Allocate Process Step – Primary Costs – Customizing
                                   Calculation Rates: a) Fixed value




                                   Postings                                                                                                                  Inspection
                                                                                                                                                               Calculation Calculation
                                                                                                                                                                 Base        Factor
                                                                                                                                                                 1000     x   0.00     = 0.00



                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                                          292




                             146                                                                                                         IFPSLF                                                       © SAP SE

Allocate Process Step – Primary Costs – Customizing
                                  Calculation Rates: b) Cost / Revenue rate


                                 SAP Menu Location




                                 Postings




                                  © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                293




Duplication is prohibited.                                                                                                              Duplication is prohibited.



                                                                                                               -Internal-



                               SAP S/4HANA for Financial Product Subledger
                               (banking edition)
                               Bond Example - Processes and Process Steps – part 3
                               April 2020


                               SAP SE




                             © SAP SE                                                                          IFPSLF             147

Agenda


                                   Part 1                       Introduction

                                   Part 2                       Loan Example - Processes and Process Steps

                                   Part 3                       Bond Example - Processes and Process Steps

                                                                Conclusion




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                  295




Duplication is prohibited.                                                                                                               Duplication is prohibited.
                                   Objectives




                                               After completing this learning module, you will be able to:
                                               • Obtain a holistic understanding of the processes and process steps in FPSL
                                               • Understand the connection between the data model and the process steps
                                               • Create and upload test data
                                               • Perform all steps necessary to process a security
                                               • Check for target values in FPSL result category storage
                                               • Analyze subledger postings in FPSL result category storage




                                   © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                  296




                             148                                                                                IFPSLF        © SAP SE

Contracts vs. Security – What is different?


                                                     Item                                                     Contract                       Security

                                                     Issue                                                    Individual contract            Standardized financial Instrument
                                                                                                              Start contract with            Multiple purchases possible,
                                                     Acquisition
                                                                                                              counterpart                    usually traded at exchange
                                                                                                                                             Held to maturity, trading or to be
                                                     Purpose                                                  Held to maturity
                                                                                                                                             used as collateral
                                                     Valuation                                                Discount cash flows            Alternatively market price / quote
                                                                                                                                             Position based (purpose or lot
                                                     Management                                               Single contract
                                                                                                                                             based)
                                                                                                              Contract management            Market data provider (standardized
                                                     Data sources
                                                                                                              system                         information), trading systems

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                       297




Duplication is prohibited.                                                                                                                                                                    Duplication is prohibited.
                                 Purchase or Sale of a Security – Business Problem to be solved

                                           Accounting requirements are the same as for a contract
                                                •        Documentation of all operational value flows
                                                •        Completeness of all book value components and income statement at period end

                                           Additional challenges while handling securities
                                                •        Managing income statement, because positions are build up by single purchases with individual
                                                         prices. Prices (acquisition value) need to be considered while calculating P/L
                                                          •        Unrealized P/L at period end by calculating current value
                                                          •        Realized P/L if a position / parts of a position are getting sold
                                                •        Operations and data for securities are highly standardized (all data is referring to a normalized
                                                         value or a piece and need to be scaled to current positions)
                                                •        Multiple positions can be build for the same security (different purpose of position)
                                                •        Positions on lots are maintained in accounting
                                                •        Non position changing events (e.g. interest payment) are triggering a distribution of value across
                                                         different positions

                                 © 2020 SAP SE or an SAP affiliate company. All rights reserved. ‫ ۄ‬CUSTOMER                                                                       298




                             © SAP SE                                                                                               IFPSLF                                              149

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
