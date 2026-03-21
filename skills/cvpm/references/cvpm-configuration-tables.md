# CVPM Configuration Tables and Customizing

**Classification:** FPSL-standard-guidance-with-placeholders
**Usage:** Reference when designing CVPM job configuration structure
**Do not use for:** Customer-specific table names or custom Z* naming; use placeholders instead

---

## Configuration Object Hierarchy

### Level 1: Process Type Master

**Purpose:** Register a CVPM job type in the FPSL framework

**Table/Customizing Location:** (Placeholder: confirm SAP table or IMG path)
- Possible names: `/BA1/HCVPMTYPE`, `/FIPSL/CVPM_TYPE`, or IMG customizing table
- IMG path: (Placeholder: likely under FPSL → Customizing → CVPM or Calculation)

**Key Fields** (example structure):
```
┌─────────────────────────────────────────────────────────┐
│ CVPM Process Type Master                                │
├─────────────────────────────────────────────────────────┤
│ CVPM_TYPE_ID          (e.g., "INTEREST_ACR", "FXR")    │
│ CVPM_TYPE_DESC        (e.g., "Monthly Interest Accrual")│
│ BUSINESS_EVENT        (e.g., "PERIOD_END", "DEAL_EVENT")│
│ PROCESS_CADENCE       (e.g., "MONTHLY", "QUARTERLY")   │
│ AFFECTED_PRODUCT_TYPE (e.g., "LOAN", "BOND", "FX")     │
│ SEGMENT_SCOPE         (e.g., "ALL", "BY_DESK", "BY_LOB")│
│ ACCOUNTING_OBJECTIVE  (e.g., "INTEREST_ACCRUAL")       │
│ MANDATORY_FIELDS      (e.g., "ACCOUNT", "PROFIT_CENTER")│
│ ACTIVE_FLAG           (X or blank)                      │
│ CREATED_BY, CREATED_DATE, CHANGED_BY, CHANGED_DATE     │
└─────────────────────────────────────────────────────────┘
```

**Design Decisions:**
- One CVPM_TYPE_ID per distinct accounting objective
- Do NOT combine unrelated objectives (e.g., accrual + FX in one type)
- Include PROCESS_CADENCE to guide job scheduling

---

### Level 2: Process Step Registry

**Purpose:** Define the sequence of FPSL steps within a CVPM process type

**Table/Customizing Location:** (Placeholder: `/BA1/HCVPM_STEP` or IMG under CVPM_TYPE_ID)

**Key Fields** (example structure):
```
┌─────────────────────────────────────────────────────────┐
│ CVPM Process Step Registry                              │
├─────────────────────────────────────────────────────────┤
│ CVPM_TYPE_ID          (FK to Process Type Master)       │
│ STEP_SEQ              (1, 2, 3, ... ordering)           │
│ STEP_ID               (e.g., "REGISTER", "VALUE", ...)  │
│ STEP_DESC             (e.g., "Fetch source deals")      │
│ METHOD_CLASS_NAME     (placeholder; actual later)       │
│ INPUT_TABLE           (source data table or CDS view)   │
│ OUTPUT_TABLE          (result or staging table)         │
│ MANDATORY_FLAG        (X = must run; blank = optional)  │
│ SKIP_ON_ERROR_FLAG    (X = continue; blank = fail fast) │
│ THREAD_CAPABLE        (X = can parallelize)             │
│ DEPENDENCY_ON_STEP    (e.g., "REGISTER")                │
│ EXPECTED_DURATION_EST (estimated runtime in seconds)    │
│ ACTIVE_FLAG           (X or blank)                      │
└─────────────────────────────────────────────────────────┘
```

**Standard FPSL Process Steps:**
| Step ID | Description | Typical Method | Output Grain | Can Parallel |
|---------|-------------|-----------------|--------------|--------------|
| REGISTER | Fetch source deal data | SQL/CDS Select | Deal | Yes (by range) |
| ENRICH | Add supplementary data (rates, hierarchy) | Join + lookup | Deal | Yes |
| VALUE | Run valuation/calculation method | AMDP/ABAP | Deal or Result | Yes (by segment) |
| CLASSIFY | Apply accounting classification logic | Rule tree or SQL | Deal | Yes |
| RECONCILE | Validation & reconciliation checks | SQL queries | Deal + GL | No (after VALUE) |
| STAGE | Intermediate result storage | Insert/update | Result table | Sequential |
| POST | Generate GL posting lines | SQL/AMDP | Posting line | No (last step) |

---

### Level 3: Method Master Registry

**Purpose:** Register calculation/valuation methods and link them to process steps

**Table/Customizing Location:** (Placeholder: `/BA1/HMETHOD`, or IMG under CVPM_TYPE_ID)

**Key Fields** (example structure):
```
┌──────────────────────────────────────────────────────────┐
│ CVPM Method Master                                       │
├──────────────────────────────────────────────────────────┤
│ CVPM_TYPE_ID              (FK to Process Type Master)    │
│ METHOD_ID                 (e.g., "AMORT_COST", "IFRS9")  │
│ METHOD_NAME               (e.g., "Amortized Cost")       │
│ METHOD_TYPE               (e.g., "VALUATION", "CLASSIFICATION") │
│ IMPLEMENTATION_TYPE       (e.g., "AMDP", "ABAP", "RULE_TREE")   │
│ AMDP_CLASS_NAME           (placeholder: Z_XXXXX_METHOD)  │
│ AMDP_METHOD_NAME          (placeholder method name)      │
│ SOURCE_TABLE              (input for method)             │
│ OUTPUT_TABLE              (result storage)               │
│ APPLICABLE_PRODUCTS       (e.g., "LOAN,BOND")            │
│ APPLICABLE_SEGMENTS       (e.g., "DESK_1,DESK_2" or "*") │
│ METHOD_VERSION            (e.g., "1.0", "2.1")           │
│ FALLBACK_METHOD_ID        (if method fails, use this)    │
│ PARAMETERS                (JSON or XML config string)    │
│ ACTIVE_FLAG               (X or blank)                   │
│ EFFECTIVE_FROM_DATE       (version control)              │
│ EFFECTIVE_TO_DATE         (version control)              │
└──────────────────────────────────────────────────────────┘
```

**Design Guidance:**
- One METHOD_ID per unique calculation (do not mix interest + FX in same method)
- IMPLEMENTATION_TYPE sets expectations: SQL (AMDP) vs. procedural (ABAP) vs. rules (decision table)
- VERSION field enables rolling back or A/B testing methods
- FALLBACK_METHOD_ID is critical for business continuity (missing data = use prior method)

---

### Level 4: GL Account Determination

**Purpose:** Map CVPM result characteristics to GL posting accounts

**Table/Customizing Location:** (Placeholder: IMG under FPSL → GL Posting or custom Z* table)

**Key Fields** (example structure):
```
┌──────────────────────────────────────────────────────────┐
│ GL Account Determination                                 │
├──────────────────────────────────────────────────────────┤
│ CVPM_TYPE_ID              (FK to Process Type Master)    │
│ PRODUCT_TYPE              (e.g., "LOAN", "BOND")         │
│ ACCOUNTING_TREATMENT      (e.g., "AMORTIZED_COST", "FVPL") │
│ RESULT_TYPE               (e.g., "INTEREST", "FX_GAIN", "FX_LOSS") │
│ GL_ACCOUNT                (e.g., "400100")                │
│ PROFIT_CENTER_RULE        (e.g., "@SEGMENT" → use from deal) │
│ COST_CENTER_RULE          (e.g., "FIXED_CC_001" or rule) │
│ POSTING_TYPE              (e.g., "DEBIT", "CREDIT")      │
│ AMOUNT_SIGN_ADJUST        (e.g., 1 or -1 multiplier)    │
│ ACTIVE_FLAG               (X or blank)                   │
└──────────────────────────────────────────────────────────┘
```

**Design Guidance:**
- Avoid single catch-all GL account (precision matters for audit)
- Use rules (@SEGMENT, @PRODUCT) where possible to avoid cartesian explosion
- Sign adjustment prevents posting line sign flips downstream

---

### Level 5: Worklist Master (If Preview Needed)

**Purpose:** Control analytical display and approval workflow for CVPM results

**Table/Customizing Location:** (Placeholder: `/BA1/HCVPM_WORKLIST` or custom)

**Key Fields** (example structure):
```
┌──────────────────────────────────────────────────────────┐
│ CVPM Worklist Master                                     │
├──────────────────────────────────────────────────────────┤
│ CVPM_TYPE_ID              (FK to Process Type Master)    │
│ WORKLIST_ID               (e.g., "INTEREST_ACR_REVIEW")  │
│ WORKLIST_TITLE            (e.g., "Interest Accrual Review") │
│ APPROVAL_REQUIRED         (X = yes, blank = view-only)   │
│ APPROVER_ROLE             (e.g., "FUND_MANAGER")         │
│ SORTBY_FIELDS             (e.g., "SEGMENT,DEAL_ID")      │
│ FILTER_CONDITIONS         (e.g., "AMOUNT > 100000")      │
│ ANALYTICS_FIELDS          (e.g., "AMOUNT,METHOD_VER")    │
│ ALERT_THRESHOLD_TYPE      (e.g., "TOLERANCE_BREACH")     │
│ ALERT_THRESHOLD_VALUE     (e.g., "1000000")              │
│ AUTO_POST_ON_APPROVAL     (X = post automatically)       │
│ ACTIVE_FLAG               (X or blank)                   │
└──────────────────────────────────────────────────────────┘
```

**Design Guidance:**
- Worklist is optional; use only if regulatory/operational preview is required
- APPROVAL_REQUIRED gates posting; make explicit when needed vs. batch posting

---

### Level 6: Job Scheduling Master (Batch Schedule)

**Purpose:** Define when and how often CVPM runs

**Table/Customizing Location:** (SAP standard: SM36/SM37 batch job parameters, or IMG)

**Key Fields** (example structure):
```
┌──────────────────────────────────────────────────────────┐
│ CVPM Job Schedule                                        │
├──────────────────────────────────────────────────────────┤
│ JOB_NAME                  (e.g., "ZFPSL_INTEREST_ACR")   │
│ CVPM_TYPE_ID              (FK to Process Type Master)    │
│ RUN_FREQUENCY             (e.g., "MONTHLY", "DAILY")     │
│ SCHEDULED_DAY             (e.g., 28 = 28th of month)     │
│ SCHEDULED_TIME            (e.g., "08:00:00")             │
│ EARLIEST_START            (e.g., "05:00:00" UTC)         │
│ EARLIEST_END              (e.g., "10:00:00" UTC)         │
│ TIMEOUT_MINUTES           (e.g., 120 minutes max)        │
│ ON_SUCCESS_ACTION         (e.g., "POST" or "HOLD")       │
│ ON_FAILURE_ACTION         (e.g., "NOTIFY_ADMIN")         │
│ NOTIFY_ADMIN_EMAIL        (placeholder: admin@corp)      │
│ PARALLEL_THREADS          (e.g., 4 threads)              │
│ ACTIVE_FLAG               (X or blank)                   │
└──────────────────────────────────────────────────────────┘
```

---

## Configuration Sequence (Recommended Order)

1. **Create CVPM_TYPE_ID** in Process Type Master
2. **Define Process Steps** (register → value → post)
3. **Register Methods** for each step
4. **Set up GL posting rules** (product/result → GL account)
5. **Define Job Schedule** (when to run)
6. **(Optional) Create Worklist** (if preview/approval needed)

---

## Pre-Implementation Verification Checklist

### Before Configuring, Confirm:

- [ ] Business objective is clear (interest accrual? FX reval? Classification?)
- [ ] Affected FPSL products identified (loans, bonds, FX, etc.)
- [ ] Process steps match FPSL standard (register, value, post)
- [ ] Methods will be AMDP or ABAP? (not formulas or external)
- [ ] GL account routing rules are finalized (product + segment + result → account)
- [ ] Threading strategy confirmed (volume, runtime, parallelization feasible?)
- [ ] Worklist/preview needed? (regulatory requirement? Financial review? Operational risk?)
- [ ] Rerun protocol: full recalc or incremental? Posting reversal strategy?
- [ ] Data availability: deal master, market data, prior period results ready?
- [ ] Integration points: which FPSL tables as source? Which as destination?

---

## Common Configuration Pitfalls

| Pitfall | Risk | Prevention |
|---------|------|-----------|
| Single method handles multiple products | Method logic becomes unmaintainable | Create separate methods per product type |
| GL account rule is too generic | Posting accuracy issues, audit failures | Be specific: product+segment+result→account |
| No fallback method defined | Single method failure stops entire run | Always define FALLBACK_METHOD_ID |
| Worklist added without approval workflow | Manual approval becomes bottleneck, posting delayed | Define APPROVAL_REQUIRED + APPROVER_ROLE upfront |
| Job schedule doesn't align with GL posting window | Postings occur outside allowed period | Coordinate with GL closing calendar |
| Threading added without volume analysis | Performance gains unclear, operational risk | Validate thread count with actual data volume first |

---

## Integration with Other Tables

**Data Dependencies:**
- Process Type Master ← Product Master (which products applicable?)
- Process Step Registry ← Deal Master (source data table)
- Method Master ← AMDP Class Registry (method implementation)
- GL Account Rules ← Chart of Accounts Customizing
- Job Schedule ← Batch Job Scheduling (IMG: SM36)

**Validation Queries** (route to `reconciliation` skill):
```sql
-- Verify no orphan methods (method_id in registry but class not found)
-- Verify GL accounts exist and are posting-capable
-- Verify product types in config match deal master product types
-- Verify process steps have no circular dependencies
```

---

## Transport & Deployment

**Configuration Transport Sequence:**
1. Process Type Master (CVPM_TYPE_ID must exist first)
2. Process Step Registry (references CVPM_TYPE_ID)
3. Method Master (references CVPM_TYPE_ID)
4. GL Account Rules (references CVPM_TYPE_ID)
5. Job Schedule (references CVPM_TYPE_ID + method + GL rules)
6. Worklist (optional; latest)

**Go-Live Verification:**
- [ ] All configuration records transported to PROD
- [ ] No placeholder method class names or GL accounts remain
- [ ] Test run completes without errors
- [ ] Test run results reconcile to deal master
- [ ] GL postings hit correct accounts
- [ ] Rerun works (idempotent or reversal+repost?)
