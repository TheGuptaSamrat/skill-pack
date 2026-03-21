# CVPM Information Gap Analysis

**Analysis:** Gaps between current skill-pack content and real-world CVPM implementation needs
**Scope:** SAP Financial Product Subledger (FPSL / formerly AFI - Advanced Financial Information)
**Date:** 2026-03-21
**Status:** Evidence-based findings

---

## Executive Summary

**Current State:** CVPM skill has 4 reference files (~30 lines total) with high-level framing only
**Reality:** A production CVPM job requires 20-30 distinct pieces of customer-specific evidence
**Gap Severity:** 🔴 **Critical** - skill cannot guide production implementation without significant supplementation

---

## Part 1: What's Currently in the Skill-Pack

### ✅ What We Have

**CVPM Skill Files:**
```
skills/cvpm/
├── SKILL.md (50 lines)
├── references/
│   ├── cvpm-core-rules.md (9 lines)
│   ├── cvpm-implementation-patterns.md (9 lines)
│   ├── cvpm-validation.md (8 lines)
│   └── official-sources.md (13 lines)
```

**Current Framing:**
- High-level process design thinking (register, defer, value, classify)
- Emphasis on NOT inventing class names, job names, thread settings
- Routing to companion skills (abap, amdp, mapping, reconciliation)
- Process-step sequencing concept

**Training/Official Docs Available:**
- `docs-context/training/fpsl/accounting-process-model.md` (conceptual, 12 lines)
- `docs-context/official/sap/fpsl-product-overview.md` (architectural framing only)
- `docs-context/official/sap/fpsl-process-run-validation.md` (validation concepts)

**Metadata Available:**
- Example core structures: `/BA1/HFSPD`, `/BA1/HKTVR`, `/BA1/HKTVL`
- Sample validation angles (ledger, company code, posting date, amounts)
- No CVPM-specific structures, process models, or configuration tables

---

## Part 2: What's Actually Needed for Real CVPM Development

### 🔴 Critical Gaps

**To design a functional CVPM job from scratch, you need evidence on:**

#### 1. **Business Process & Accounting Objective** (Currently missing)
```
Evidence needed:
├─ Accounting goal (e.g., periodic interest accrual, FX revaluation, fair-value adjustment)
├─ Business event trigger (e.g., month-end, quarter-end, deal maturity)
├─ Service provider or desk responsible
├─ Affected instruments (loan, bond, derivative, etc.)
├─ Regulatory or internal reporting driver
└─ Period-specific vs. deal-specific vs. ongoing cadence
```

**Why current skill doesn't cover:**
- SKILL.md says "confirm the accounting goal" but provides no templates or examples
- No structured checklist for identifying the right CVPM scope

---

#### 2. **FPSL Process Step Sequence** (Partially missing)
```
Evidence needed:
├─ Standard FPSL process steps involved:
│  ├─ Register (bring in source data)
│  ├─ Accrue (recognize contract obligations)
│  ├─ Defer (defer costs/income)
│  ├─ Classify (categorize by risk, product line, accounting treatment)
│  ├─ Value (calculate fair value, interest, FX adjustments)
│  ├─ Reconcile (match source to GL posting)
│  └─ Post (send to GL or sub-ledger)
├─ Optional FPSL steps:
│  ├─ Segment (product taxonomy)
│  ├─ Price (market data lookup)
│  ├─ Provision (loan loss provision)
│  └─ Consolidation (inter-company elimination)
└─ Dependencies & sequencing constraints
```

**Why current skill doesn't cover:**
- cvpm-implementation-patterns.md says "describe the intended process-step sequence" but gives NO examples
- No catalog of standard FPSL process steps with dependencies
- No guidance on WHICH standard steps to include vs. exclude

---

#### 3. **CVPM Configuration Object Details** (Almost completely missing)
```
Evidence needed:
├─ CVPM Job Definition (transaction, customizing table, structure)
│  ├─ Job name (Z* naming convention?)
│  ├─ Logical database or CDS table function used
│  ├─ Source data table(s)
│  ├─ Result table(s)
│  ├─ Run frequency settings
│  └─ Batch job scheduling parameters
├─ Method Mapping (which FPSL method handles each step)
│  ├─ /BA1/HMETHOD or similar registry
│  ├─ Method class naming (pattern?)
│  ├─ Method activation / versioning
│  └─ Fallback or error-handling method
├─ Process Step Registry (if one exists)
│  ├─ Step ID / sequence
│  ├─ Step dependencies
│  ├─ Input/output table mapping
│  └─ Success/failure routing
└─ Worklist Definition (if batch preview needed)
   ├─ Worklist table name (Z* or /BA1/?)
   ├─ Field requirements (deal ID, date, amount, result, status)
   ├─ User assignment logic
   └─ Approval workflow (if any)
```

**Why current skill doesn't cover:**
- No mention of actual configuration objects or tables
- No indication of where CVPM job definition lives in SAP FPSL
- official-sources.md just says "load fpsl-product-overview.md" - which is only architectural framing

---

#### 4. **Method Implementation Details** (Missing)
```
Evidence needed:
├─ Method Types:
│  ├─ Valuation Method (e.g., amortized cost, fair value, effective rate)
│  ├─ Classification Method (e.g., IFRS 9 stage determination, SPPI test)
│  ├─ Calculation Method (e.g., interest accrual, FX revaluation)
│  └─ Reconciliation Method (deal-to-posting matching)
├─ Method Implementation:
│  ├─ Is method a SELECT+CALC? (AMDP/SQL)
│  ├─ Is method a rule tree? (Decision table)
│  ├─ Is method a formula? (Excel-like expression)
│  ├─ Is method a BADI/plugin? (Custom class)
│  └─ Supporting data tables/CDS views required
├─ Method Input Requirements:
│  ├─ Deal master data fields
│  ├─ Market data (FX rates, interest curves, credit spreads)
│  ├─ Portfolio/segment hierarchy
│  ├─ Period/reference date handling
│  └─ Previous period result carry-forward?
└─ Method Output Requirements:
   ├─ Result grain (deal, segment, GL code, all)
   ├─ Required output fields (amount, justification, audit trail)
   ├─ Posting account assignment logic
   └─ Balance or P&L vs. OCI routing
```

**Why current skill doesn't cover:**
- cvpm-implementation-patterns.md barely mentions methods
- No guidance on when to use SQL vs. rules vs. formulas
- No examples of method input/output contracts

---

#### 5. **Threading & Parallelization Strategy** (Missing specifics)
```
Evidence needed:
├─ Performance & Volume:
│  ├─ How many deals to process? (100s? Millions?)
│  ├─ How many calculations per deal?
│  ├─ Expected runtime? (Minutes? Hours?)
│  ├─ Acceptable latency?
│  └─ Peak concurrency windows?
├─ Threading Options:
│  ├─ Sequential (batch job runs 1×)
│  ├─ Batch parallel by deal ID range
│  ├─ Batch parallel by segment/desk
│  ├─ Batch parallel by method type
│  └─ Real-time calculation (not batch)
├─ Thread Configuration:
│  ├─ Number of threads (4? 8? 16?)
│  ├─ Thread scope (deal range, time period, method)
│  ├─ Thread data isolation (table partitioning? View filtering?)
│  ├─ Synchronization point (wait for all threads before posting?)
│  └─ Error handling per thread (fail one = fail all?)
└─ Operational Monitoring:
   ├─ Job logs by thread
   ├─ Per-thread result aggregation
   ├─ Failure rollback strategy (per-thread? whole job?)
   └─ Performance metrics collection
```

**Why current skill doesn't cover:**
- cvpm-implementation-patterns.md says "use thread guidance only when user provides runtime/volume evidence"
- But this effectively PREVENTS the skill from giving any Threading guidance until customer already has an implementation!
- No templates for threading decision-making

---

#### 6. **Worklist/Preview/Analytics** (Barely mentioned)
```
Evidence needed:
├─ Is worklist preview needed before posting?
│  ├─ Who reviews results? (Risk, Finance, Compliance)
│  ├─ What fields need visibility?
│  ├─ what drill-down depth?
│  ├─ Approval sign-off flow?
│  └─ Analytics or alerting on results?
├─ Worklist Architecture (if yes):
│  ├─ Worklist table schema
│  ├─ Staging area (intermediate results)
│  ├─ Result filtering/sorting options
│  ├─ Notes/comment fields
│  ├─ Rerun decision (post or recalc?)
│  └─ Audit trail (who viewed when, approved what)
└─ Analytics Requirements:
   ├─ Sensitivities (what if rates ±10bps?)
   ├─ Tolerance breach alerting (deviation > threshold?)
   ├─ Variance reporting (current vs. prior period)
   └─ Drill-down to deal level (explain each posting line)
```

**Why current skill doesn't cover:**
- cvpm-implementation-patterns.md says "use worklist discussion only when requirement clearly depends on carried-forward positions or analytical decisions"
- This is circular: you don't know if worklist is needed until you've designed CVPM!
- No template for worklist requirements gathering

---

#### 7. **Data Integration & Staging** (Missing)
```
Evidence needed:
├─ Source Data:
│  ├─ Deal master location (FPSL, S/4HANA, external system)
│  ├─ Deal attributes to fetch (type, instrument, counterparty, rating, etc.)
│  ├─ Instrument/product mapping (internal code → FPSL product type)
│  ├─ Segment hierarchy (business line, desk, risk category)
│  └─ Effective dating (as-of contract date, as-of reporting date, as-of settlement)
├─ Market Data:
│  ├─ Reference rates (FX spots, interest curves, credit spreads, equity prices, volatility)
│  ├─ Sourcing (Bloomberg, Reuters, internal models, SAP feeds, external files)
│  ├─ Lag (real-time, EOD, T+0, T+1, historical daily, week, month)
│  ├─ Validation (stale-rate detection, outlier detection)
│  └─ Fallback logic (missing rate → use prior close? use proxy?)
├─ Historical/Carry-Forward Data:
│  ├─ Prior period results (previous month's valuation)
│  ├─ Prior period GL postings (for rerun/correction logic)
│  ├─ Amortization schedule or remaining life
│  └─ Deferred/deferred income opening balance (for accruals)
└─ Staging Process:
   ├─ ETL or direct CDS view?
   ├─ Staging table (intermediate layer?)
   ├─ Data quality checks (mandatory fields, referential integrity)
   ├─ Grain verification (deal unique? deal+tranche unique?)
   └─ Recon before calculation starts
```

**Why current skill doesn't cover:**
- Not mentioned in CVPM skill at all
- Implicitly routed to `mapping` skill, but CVPM doesn't explain what mapping data is needed

---

#### 8. **Posting Logic & GL Integration** (Missing)
```
Evidence needed:
├─ GL Posting Destination:
│  ├─ GL account rules (determined by: product type? segment? method result?)
│  ├─ Profit center or cost center rules
│  ├─ Internal order or project assignment
│  ├─ Dimension routing (if using new GL or universal GL)
│  └─ Posting method (direct FI posting? Subledger posting? Reconciliation entry?)
├─ Posting Grain:
│  ├─ Line-level (one posting per deal result)
│  ├─ Aggregated (totals by GL account, profit center, etc.)
│  ├─ Gross vs. net (show intermediate values or final only?)
│  └─ Reversals (auto-reverse prior period? Manual reversal?)
├─ Posting Timing:
│  ├─ Immediate post when calculation done?
│  ├─ Batch accumulation then post once?
│  ├─ Manual post after approval?
│  ├─ Posting period control (current open period? Prior closed period?)
│  └─ Event-driven (e.g., on deal maturity) vs. time-driven (e.g., monthly)
├─ Error Handling:
│  ├─ If posting fails, is result rolled back?
│  ├─ Partial posting recovery (some lines post, others fail)?
│  ├─ Error log or quarantine table?
│  └─ Resubmission process?
└─ Audit & Reconciliation:
   ├─ Posting reference (CVPM job ID, method version, date)
   ├─ Traceability (from deal → CVPM result → GL posting)
   ├─ Reversal audit trail
   └─ Rerun/recalculation history (versioning)
```

**Why current skill doesn't cover:**
- cvpm-validation.md mentions "include validation points for process-step sequencing" but posting logic is never discussed
- Implicitly routed to `reconciliation`, but CVPM doesn't explain what posting-validation queries are needed

---

#### 9. **SAP FPSL Metadata & Customizing** (Mostly missing)
```
Evidence needed:
├─ FPSL Tables/Structures:
│  ├─ Deal master (e.g., /BA1/... table or CDS view)
│  ├─ Product catalog (e.g., /FIPSL/... or custom Z* product definition)
│  ├─ Method registry (e.g., /BA1/HMETHOD or custom)
│  ├─ Result store (e.g., /BA1/HKTVR or custom Z* result table)
│  ├─ GL posting table (e.g., /BA1/HFSPD or standard GL posting)
│  └─ Segment hierarchy (e.g., standard CCTR/PRCTR or custom Z* hierarchy)
├─ Customizing Tables:
│  ├─ Process type master (IMG customizing for CVPM type registration)
│  ├─ Method assignment (which method per product/segment?)
│  ├─ GL account determination (product → accounting key → GL account)
│  ├─ Valuation date rules (deal date vs. reporting date vs. settlement date)
│  └─ Regulatory/IAS 39/IFRS 9 mapping tables
└─ Configuration Transactions:
   ├─ IMG path for CVPM setup
   ├─ Customizing sequence (what to configure first/second/last?)
   ├─ Configuration verification steps
   └─ Transport/promotion sequence
```

**Why current skill doesn't cover:**
- SKILL.md mentions "load official sources" but official sources are just architectural framing
- No table names, no IMG path guidance, no DDIC structures provided

---

#### 10. **Rerun Safety & Idempotency** (Mentioned but not detailed)
```
Evidence needed:
├─ Rerun Scenarios:
│  ├─ Full rerun (recalculate all deals afresh, overwrite prior)
│  ├─ Incremental rerun (recalc subset of deals)
│  ├─ Correction run (apply one-time manual adjustment)
│  ├─ Reversal run (undo prior period posting)
│  └─ Rerun during open period vs. closed period
├─ Deduplication:
│  ├─ Is deduplication key (deal_id + reporting_date + method_version)?
│  ├─ If duplicate found, update or error?
│  ├─ Merge logic if method produces variable row counts?
│  └─ Grain validation (no cartesian product surprises)
├─ Balance Preservation:
│  ├─ Posting reversal (automatic offset for prior result)?
│  ├─ Audit trail (trace movement from old posting → new posting)
│  ├─ Reversals in separate transaction or same?
│  └─ Reversal approval needed?
└─ Previous Period Carry-Forward:
   ├─ Is carry-forward automatic or manual?
   ├─ If carry-forward missing, fail run or assume zero?
   ├─ Validation of carry-over (opening balance reconciliation)
   └─ Versioning (method version X → version Y, recalc all prior periods?)
```

**Why current skill doesn't cover:**
- amdp-query-patterns.md has rerun content but is routed to amdp, not cvpm
- cvpm skill doesn't guide rerun requirements at CVPM job design level

---

#### 11. **Operator Runbook & Support** (Completely missing)
```
Evidence needed:
├─ Operational Playbook:
│  ├─ Pre-run checklist (data loads complete? Market data loaded? Prior period finalized?)
│  ├─ Run execution steps (which transaction? Parameter entry?)
│  ├─ Expected runtime (5 min? 2 hours?)
│  ├─ Success criteria (all deals processed? Tolerance breaches acceptable?)
│  └─ Post-run verification (reconciliation, audit, posting confirmation)
├─ Troubleshooting:
│  ├─ Common failure scenarios | → Recovery steps
│  ├─ Log analysis (where to find results? Error codes?)
│  ├─ Data quality issues → How to fix?
│  ├─ Performance tuning (if slow, where to optimize?)
│  └─ Support escalation (when to call SAP? When to call customer Finance?)
├─ Monitoring & Alerting:
│  ├─ Tolerance breach detection (e.g., daily P&L > ±$1M)
│  ├─ Missing market data alert
│  ├─ Stale result detection (recent rerun missing?)
│  ├─ GL posting confirmation
│  └─ End-to-end execution time trending
└─ Change Management:
   ├─ When to rerun (after method change, after data correction, after rate feed update?)
   ├─ Promotion process (DEV→QA→PROD)
   ├─ Regression testing (prior period results replicated?)
   └─ Version rollback plan
```

**Why current skill doesn't cover:**
- Not mentioned anywhere in CVPM skill or references
- This is operational knowledge, not design knowledge, but it's critical to implementation success

---

## Part 3: AFI → FPSL Transition Context

### What Changed?

**AFI (Advanced Financial Information):**
- Older SAP financial products framework
- Limited to specific instrument types
- Configuration-heavy, limited analytics

**FPSL (Financial Product Subledger) / SAP S/4HANA for Financial Products:**
- Modern replacement for AFI (and legacy FSCM components)
- Broader instrument coverage (loans, bonds, derivatives, FX contracts, commodities, etc.)
- HANA-native, emphasis on analytics and reporting
- CVPM naming replaced older "Calculation Process" naming
- CDS views and AMDP-ready (not just traditional ABAP batch jobs)

**Key Implication for CVPM Skill:**
- The skill assumes "FPSL" (new terminology), but many existing landscapes may still run AFI or hybrid
- No guidance on AFI→FPSL CVPM migrationpath or coexistence
- No mention of whether CVPM design is version-dependent

---

## Part 4: What Would Make CVPM Skill Complete?

### 🟡 Recommended New Reference Files

```
skills/cvpm/references/
├── cvpm-core-rules.md (current: 9 lines)
│   └─→ ADD: Standard FPSL process steps, worklist/threading decision tree, method types
├── cvpm-implementation-patterns.md (current: 9 lines)
│   └─→ ADD: Common CVPM architectures, data integration patterns, posting patterns
├── cvpm-configuration-tables.md (NEW: ~50 lines needed)
│   ├─ FPSL configuration object overview
│   ├─ Customizing table references (with IMG path if known)
│   ├─ Method registry structure
│   ├─ Process step registry (if exists)
│   ├─ Worklist, job, and batch setup tables
│   └─ Example configuration checklist
├── cvpm-method-design.md (NEW: ~40 lines needed)
│   ├─ Method types (valuation, classification, calculation, reconciliation)
│   ├─ Method implementation options (SQL, rule tree, formula, BADI)
│   ├─ Input/output contract definition
│   ├─ Method versioning and fallback
│   └─ Common method patterns (amortized cost, fair value, FX reval, interest accrual)
├── cvpm-data-integration.md (NEW: ~45 lines needed)
│   ├─ Source data requirements (deal master, market data, hierarchies)
│   ├─ Staging and data quality
│   ├─ Carry-forward / prior period logic
│   ├─ Reference data management
│   └─ Integration with config skill (mapping + staging)
├── cvpm-posting-and-gl.md (NEW: ~35 lines needed)
│   ├─ GL posting decision logic
│   ├─ Posting grain options
│   ├─ Posting timing (immediate, batch, manual approved)
│   ├─ Error handling and audit trail
│   └─ Rerun/reversal strategy
├── cvpm-operational-design.md (NEW: ~40 lines needed)
│   ├─ Threading and parallelization (now with decision templates)
│   ├─ Worklist preview and analytics
│   ├─ Rerun safety and idempotency
│   ├─ Operator runbook outline
│   ├─ Support and troubleshooting
│   └─ Change management
├── cvpm-metadata-sources.md (NEW: ~25 lines needed)
│   ├─ FPSL tables and structures directory
│   ├─ DDIC references for /BA1/... tables
│   ├─ CDS views for dealing, accounting, master data
│   ├─ SAP Note references for CVPM setup
│   └─ IMG transaction references
└── official-sources.md (current: 13 lines)
    └─→ EXPAND: Link to SAP Help FPSL CVPM guide, SAP Fioneer guidance, Release Notes
```

---

### 🟡 Recommended Additional Training Material

```
docs-context/training/fpsl/
├── cvpm-process-design-guide.md (NEW: ~80 lines)
│   ├─ End-to-end CVPM design workflow
│   ├─ Business requirements → CVPM job structure
│   ├─ Common FPSL processes (interest accrual, revaluation, classification)
│   ├─ Threading and performance considerations
│   ├─ Worked example: Quarterly FX revaluation process
│   └─ Worked example: Monthly interest accrual for floating-rate loans
├── cvpm-method-patterns.md (NEW: ~60 lines)
│   ├─ Method implementation options matrix
│   ├─ When to use SQL (AMDP) vs. rule tree vs. formula
│   ├─ Example method: Amortized cost calculation
│   ├─ Example method: IFRS 9 stage determination
│   ├─ Example method: FX revaluation by reference rate
│   └─ Method testing and validation
└── cvpm-data-flows.md (NEW: ~70 lines)
    ├─ Deal master data requirements
    ├─ Market data orchestration
    ├─ From method result → GL posting flow
    ├─ Reconciliation checkpoints
    ├─ Data quality rules
    └─ Worked example: Loan deal through full CVPM flow
```

---

### 🟡 Recommended Metadata Additions

```
metadata-drop/fpsl/
├── cvpm-structures.md (NEW)
│   ├─ Process type registry structure
│   ├─ Method registry structure
│   ├─ Result table structure (grain, cardinality)
│   ├─ Worklist structure (if used)
│   └─ Segment hierarchy structure
├── cvpm-configuration-checklist.md (NEW)
│   ├─ Pre-implementation decisions
│   ├─ Configuration sequence
│   ├─ Testing/validation gates
│   └─ Go-live checklist
└── cvpm-example-designs.md (NEW - 3-5 realistic scenarios)
    ├─ Simple scenario: Monthly interest accrual (single method, no worklist)
    ├─ Medium scenario: Quarterly FX revaluation (multiple segments, worklist needed)
    ├─ Complex scenario: Deal classification for regulatory reporting (multi-method, multi-thread)
    └─ Each with: Business driver, process steps, methods, data needs, threading strategy
```

---

## Part 5: Real-World Evidence Gaps

### From Customer Engagement Perspective

**To actually help a customer design a CVPM job, you'd need to gather:**

| Topic | Current Skill Help? | Reality |
|-------|-------------------|---------|
| Business objective | ❌ "Confirm it" | Needs structured discovery questionnaire |
| Process steps to include | 🟡 "Use register, defer, value..." | Needs decision tree: which steps apply to THIS product/objective? |
| Method implementation | ❌ Not covered | Need method type selector + template per type |
| Threading strategy | ❌ "Only with evidence" | Need decision tree: volume analysis → threading recommendation |
| Data sources | ❌ "Implicit in mapping" | Need explicit checklist: deal master, market data, hierarchies |
| GL posting rules | ❌ Not covered | Need posting account determination logic template |
| Worklist needs | ❌ "Only if clear" | Need questionnaire: review needed? approval? analytics? |
| Rerun scenarios | 🟡 Mentioned in AMDP | Not connected to CVPM job design decisions |
| Go-live readiness | ❌ Not covered | Need pre-go-live checklist |

---

## Part 6: Real-World CVPM Development Checklist

**What a complete CVPM skill would help you generate:**

```
CVPM Implementation Artifact Checklist:
├─ CVPM Design Document
│  ├─ Business objective & success criteria
│  ├─ FPSL process steps (register → accrue → defer → value → classify → post)
│  ├─ Method inventory (name, type, input/output, versioning)
│  ├─ Data flow diagram (source system → FPSL → worklist → GL)
│  ├─ Worklist / analytics / preview design (if needed)
│  ├─ Threading & parallelization strategy (with volume evidence)
│  ├─ GL posting rules (account determination logic)
│  ├─ Rerun/correction protocol
│  └─ Success & failure criteria
│
├─ CVPM Configuration Artifacts
│  ├─ Process type master customizing (IMG path, table)
│  ├─ Method master customizing (registry entries, class names)
│  ├─ GL posting account determination (rules, transact
ion)
│  ├─ Job scheduling parameters (frequency, time window)
│  └─ Batch process mode (sequential? parallel? hybrid?)
│
├─ Data Integration Artifacts (route to config skill)
│  ├─ Deal master CDS view (or table → view wrapper)
│  ├─ Market data load process (with staleness check)
│  ├─ Segment hierarchy table/view
│  ├─ Prior period carry-forward query
│  └─ Data quality checks (SQL)
│
├─ Method Implementation Artifacts (route to amdp/abap skill)
│  ├─ Method 1: [Name] (AMDP or ABAP?)
│  ├─ Method 2: [Name]
│  ├─ Method N: [Name]
│  └─ Each with: input spec, calc logic, output spec, testing plan
│
├─ Result & Posting Artifacts
│  ├─ Result staging query (or table definition)
│  ├─ Result validation/reconciliation queries (route to reconciliation skill)
│  ├─ GL posting generator (AMDP or ABAP? route to abap/amdp skill)
│  ├─ Worklist preview queries (if applicable)
│  └─ Analytics/drill-down queries
│
└─ Operational Artifacts
   ├─ Pre-run checklist
   ├─ Operator runbook (step-by-step execution)
   ├─ Monitoring & alerting setup
   ├─ Troubleshooting guide
   ├─ Change management process
   └─ Go-live verification plan
```

---

## Conclusion

### Current CVPM Skill Assessment

| Dimension | Rating | Evidence |
|-----------|--------|----------|
| Conceptual framing | 🟡 Good | Covers high-level thinking |
| Guardrails (don't invent names) | 🟢 Excellent | Clear about placeholders |
| Practical implementation guidance | 🔴 Insufficient | ~30 lines total, no configuration details |
| Metadata/structure references | 🔴 Missing | No table names, IMG paths, structures |
| Method design patterns | 🔴 Missing | No method types or decision trees |
| Data integration guidance | 🔴 Missing | Routed elsewhere, not integrated |
| Threading/performance guidance | ⚠️ Blocked | "Only with evidence" prevents proactive guidance |
| Operational/support guidance | 🔴 Missing | Not covered at all |
| Real-world examples | 🟡 Minimal | Test case exists but sparse |

### Why Current Skill Fails for Real Customers

1. **It's purely defensive**: "Don't invent X" but offers nothing to replace invention
2. **It sprinkles responsibility**: CVPM can't guide design because "routing logic is in companion skills"
3. **It's catch-22 on threading**: "Tell me volume/runtime evidence first" but customer doesn't have that until design is done
4. **It lacks specific evidence**: No table names, IMG paths, configuration sequences
5. **It's conceptual, not operational**: Great for thinking, useless for doing

### What's Needed to Make CVPM Production-Ready

✅ 3-4 new reference files (~150-200 lines total)
✅ 2-3 new training docs with worked examples
✅ Metadata samples: configuration tables, CDS structures, method templates, data models
✅ Decision trees: when to include worklist? when to thread? how many methods?
✅ Integration blueprints: how CVPM design → config → abap → amdp → reconciliation
✅ Operational playbook: pre-run, execution, post-run, troubleshooting

---

**Recommendation:** The CVPM skill is a **proof of concept**, not a **production guide**. To make it viable for real customer engagements, invest in the supplementary materials above.
