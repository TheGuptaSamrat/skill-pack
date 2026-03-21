Classification: training-derived-concepts
Source basis: FPSL TRAINING DOCUMENT.pdf, pages 75-110
Trust usage: IFRS 9 business model assessment, SPPI test, classification categories
Do not use for: regulatory interpretation or customer-specific classification
Topics covered: IFRS 9, classification, business model, SPPI test, amortized cost, fair value, accounting treatment

# IFRS 9 Classification and Measurement Framework
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
