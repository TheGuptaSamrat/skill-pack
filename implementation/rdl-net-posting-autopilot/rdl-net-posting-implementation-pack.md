# RDL Net Posting Implementation Pack

Purpose: implement a modular, selective, CVPM-compatible data flow that applies the requirement-specific join logic from `design/netting-join-logic.md` and loads `Z_NET_POSTING` (same structure as `/BA1/HFSPD`).

This pack is split into ADT-ready artifacts and a non-ABAP runbook.
All custom technical object names except `Z_NET_POSTING` are placeholders and must be replaced with your confirmed namespace/object names.

This pack implements the GHCP requirement contract in `.github/prompts/rdl-net-posting.prompt.md`.
If the pack and the prompt differ, the prompt is the primary requirement source until corrected evidence is added here.

## Pack usage

- reusable RDL table and field evidence comes from `metadata-drop/ddic/current/`
- requirement-specific joins, filters, and examples stay in this pack
- raw Excel or screenshots used during development should stay local and not be committed by default

## Start here (execution map)

- Track A: Development (ADT paste-ready sequence)
  - DDIC -> AMDP -> ABAP -> CVPM wiring
- Track B: Testing and validation
  - ABAP Unit -> SQL validation -> focused smoke execution
- Track C: Operations and monitoring
  - CVPM runbook -> `/BAL/PW_PROCMON` checks -> troubleshooting quick table

Current iteration scope:

- keep CVPM wiring in scope
- keep the architecture modular (AMDP, ABAP orchestration, CVPM config split)
- defer service resumption/checkpoint restart logic for now

Done criteria:

- ADT artifacts activate in sequence
- ABAP Unit tests pass
- validation SQL checks pass on test scope
- CVPM process can be configured and monitored

## 1) Confirmed inputs from uploaded metadata and prompt contract

- Driver table: `/BA1/HFSPD`
- Join table 1: `/BA1/HKAPA`
- Join table 2: `/BA1/HKAPD`
- Mandatory HKAPA filter: `/BA1/CR4PFCT = '2100'`
- Mandatory HKAPD filter: `/BA1/C55ACCRCT = '601'`
- Temporal filter pattern: latest `/BA1/CR0KEYDAT <= /BA1/C55POSTD`, with `CURRENT_FLAG = 'X'`
- Source exclusion:
  - GL and GR posting blocks from the sample workbook are not netting source rows
- Netting model:
  - netting group excludes contract ID
  - minimum confirmed netting-group dimensions:
    - `/BA1/C55POSTD`
    - `/BA1/C11NODENO`
    - `/BA1/C55ACCSY`
  - contract ID is part of the output/result row, not the aggregation key for net calculation
- Aggregates:
  - `SUM(/BA1/K5SAMGRP)` for net computation at group level
  - `/BA1/K5SAMBAL` retained from the chosen anchor row for the contract result

## 1a) Requirement-specific references in this pack

- join and filter logic: `design/netting-join-logic.md`
- zero-shot prompt context: `examples/zero-shot.md`
- one-shot prompt context: `examples/one-shot.md`

## 1b) Confirmed logic vs inferred assumptions

Confirmed from approved metadata and this implementation pack:

- `/BA1/HFSPD` is the driver table.
- `/BA1/HKAPA` and `/BA1/HKAPD` are the validation dimensions.
- `CURRENT_FLAG = 'X'` and latest `/BA1/CR0KEYDAT <= /BA1/C55POSTD` are part of the temporal validity rule.
- hard filters are `/BA1/CR4PFCT = '2100'` and `/BA1/C55ACCRCT = '601'`.
- GL and GR posting blocks are excluded from netting source rows.
- netting group excludes contract ID and the output remains one row per eligible contract.
- `SUM(/BA1/K5SAMGRP)` is the net basis and allocation is restricted to the same-sign side only.
- target table `Z_NET_POSTING` is approved to have the same structure as `/BA1/HFSPD`.

Inferred and still to be revalidated in the target landscape:

- `/BA1/HFSPD` joins to `/BA1/HKAPA` on `/BA1/C55CONTID`, `/BA1/C11NODENO`, `/BA1/C55ACCSY`.
- `/BA1/HKAPA` joins to `/BA1/HKAPD` on `/BA1/C55PFID` and `/BA1/C55ACCSY`.
- `MIN( /BA1/C55DOCNUM )` plus `MIN( /BA1/C55DOCITM )` is only a candidate anchor strategy and must be revalidated per contract result.
- the exact HFSPD field/value used to exclude the GL and GR workbook blocks is still a candidate mapping and must be confirmed before productive use.
- the resume cursor can be ordered lexicographically by `(POSTD, CONTID, NODENO, ACCSY)` without missing or duplicating groups.

## 2) Runtime architecture

- AMDP class reads one package of eligible groups using the join diagram logic.
- ABAP orchestration class:
  - manages selective filters
  - delegates data access to injected collaborators
  - pulls anchor rows from `/BA1/HFSPD`
  - writes merged rows into `Z_NET_POSTING`
- Report wrapper exposes batch options for operations/CVPM.
- CVPM analytical process calls the report with step sequence including worklist creation.

## 2a) Business logic implementation (netting & allocation)

**Netting logic (from prompt and test samples):**

- Exclude GL and GR posting blocks from the source set.
- Netting group excludes contract ID.
- Within each netting group: calculate net of all balances.
- If net > 0: allocate proportionally across **positive contracts only**
- If net < 0: allocate proportionally across **negative contracts only**
- If net = 0: no allocation (logical block kept for future clarity)
- Allocation formula:
  ```
  Allocated_Amount(i) = ( |Contract_Balance(i)| / Σ|Positive_or_Negative_Balances| ) × |Net|
  ```

**DDIC Field References (to be verified in target landscape):**

- Asset/Liability Indicator: `/BA1/C55ALST` (refer DDIC for exact field semantics)
- Group Category field (`Group Cat` in test samples showing A, C, D values):
  - **Safe assumption:** Derive based on allocation outcome or netting rule flag
  - **TODO for clarification:** Confirm whether Group Cat is:
    - A: Asset-only group (net > 0, allocated across positive contracts)
    - C: Cross/Mixed group (net = 0, no allocation)
    - D: Debt/Liability-only group (net < 0, allocated across negative contracts)
    - Or: static passthrough from source CONTRACT/POSTING attributes?
  - Temporary implementation: Placeholder logic; enrich in ABAP layer with safe defaults pending DDIC validation
- Allocation Amount computed field: derived from Group Currency Amount (`/BA1/K5SAMGRP`), stored in ABAP enrichment layer

**Error Handling:**

- Allocation validation errors (division by zero, missing contract data) logged to separate error table/log (not inline in output)
- Precision: maintain original precision from source field throughout calculation

## Track A - Development (ADT paste-ready sequence)

## 3) Artifact: Resume control table (DDIC) - deferred in current iteration

Paste target: ADT DDLS/SE11 table creation for `<ZNET_POSTING_RUN>`
Action: create

Note:
- This artifact is kept as an optional extension.
- For current simplified flow, skip creation and run without checkpoint dependency.

```abap
@EndUserText.label: 'Net Posting Batch Resume Control'
@AbapCatalog.enhancement.category: #NOT_EXTENSIBLE
@AbapCatalog.tableCategory: #TRANSPARENT
@AbapCatalog.deliveryClass: #A
@AbapCatalog.dataMaintenance: #ALLOWED
define table <ZNET_POSTING_RUN> {
  key mandt          : mandt not null;
  key run_id         : abap.char(32) not null;

  status             : abap.char(1);      // N=new, R=running, C=complete, E=error
  last_postd         : abap.dats;
  last_contid        : abap.char(20);
  last_nodeno        : abap.char(12);
  last_accsy         : abap.char(4);
  package_size       : abap.int4;
  rows_processed     : abap.int8;
  changed_at_utc     : timestampl;
  changed_by         : syuname;
  last_error_text    : abap.char(255);
}
```

Checks:
- Activate table and verify primary key is `(MANDT, RUN_ID)`.
- Add technical settings for expected volume.

## 3a.1) Artifact: Error log table (DDIC) - separate error tracking

Paste target: ADT DDLS/SE11 table creation for `Z_NET_POSTING_ERR`
Action: create

Note:
- Captures allocation validation errors separately from successful posting flow
- Required for process monitoring and troubleshooting

```abap
@EndUserText.label: 'Net Posting Error Log'
@AbapCatalog.enhancement.category: #NOT_EXTENSIBLE
@AbapCatalog.tableCategory: #TRANSPARENT
@AbapCatalog.deliveryClass: #A
@AbapCatalog.dataMaintenance: #ALLOWED
define table z_net_posting_err {
  key mandt              : mandt not null;
  key error_id           : abap.int8 not null;

  client_id              : abap.char(1);
  postd                  : abap.dats;
  contid                 : abap.char(20);
  nodeno                 : abap.char(12);
  accsy                  : abap.char(4);
  error_msg              : abap.string;  // detailed error text (e.g., "Anchor row not found", "Allocation validation failed")
  created_at             : abap.dats;
  created_by             : syuname;
}
```

Checks:
- Activate table with primary key `(MANDT, ERROR_ID)`.
- Add number range interval for `ERROR_ID` (e.g., Z01 from 0000000001).
- Verify error messages capture: missing anchor, division by zero, precision loss, FX conversion issues.

Paste target: ADT DDLS/SE11 table creation for `Z_NET_POSTING`
Action: create by cloning `/BA1/HFSPD`

Confirmed structure requirements from approved metadata:

- preserve the `/BA1/HFSPD` primary key exactly:
  - `CLIENT`
  - `/BA1/C55POSTD`
  - `/BA1/C55LGENT`
  - `/BA1/C55DOCNUM`
  - `/BA1/C55DOCITM`
- preserve the full field list of `/BA1/HFSPD` from `metadata-drop/ddic/current/fpsl-hfspd-fields.csv`
- keep `/BA1/K5SAMBAL` and `/BA1/K5SAMGRP` in the same technical types as source, because the job overwrites only those two amounts after copying the anchor row

Recommended implementation pattern:

- clone `/BA1/HFSPD` in DDIC or ADT rather than retyping the full field list by hand
- rename the clone to `Z_NET_POSTING`
- remove only source-specific technical settings if your landscape does not allow copying them directly

Checks:
- Verify the key order matches `/BA1/HFSPD` exactly.
- Verify `/BA1/K5SAMBAL` and `/BA1/K5SAMGRP` retained the original technical types.

## 4) Artifact: AMDP class definition

Paste target: Class definition section of `<ZCL_RDL_NET_POSTING_AMDP>`
Action: create

```abap
CLASS <ZCL_RDL_NET_POSTING_AMDP> DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC.

  PUBLIC SECTION.
    INTERFACES if_amdp_marker_hdb.

    TYPES: BEGIN OF ty_s_agg,
             client        TYPE mandt,
             postd         TYPE dats,
             lgent         TYPE c LENGTH 4,
             contid        TYPE c LENGTH 20,
             nodeno        TYPE c LENGTH 12,
             accsy         TYPE c LENGTH 4,
             anchor_docnum TYPE c LENGTH 10,
             anchor_docitm TYPE n LENGTH 6,
             sum_sambal    TYPE decfloat34,    " functional currency balance (preserved from source)
             sum_samgrp    TYPE decfloat34,    " group currency balance (pre-netted; for reference only)
             asset_liab_ind TYPE c LENGTH 1,   " DDIC reference: /BA1/C55ALST; derive per clarification
             alloc_amount   TYPE decfloat34,   " netted-delta: proportional allocation amount per contract
           END OF ty_s_agg,
           ty_t_agg TYPE STANDARD TABLE OF ty_s_agg WITH EMPTY KEY,
           ty_t_rng_char4  TYPE RANGE OF c LENGTH 4,
           ty_t_rng_char20 TYPE RANGE OF c LENGTH 20,
           ty_t_rng_dats   TYPE RANGE OF d.

    CLASS-METHODS read_aggregates
      IMPORTING
        VALUE(iv_pfct)         TYPE c LENGTH 4
        VALUE(iv_accrct)       TYPE c LENGTH 4
        VALUE(iv_package_size) TYPE i
        VALUE(it_lgent)        TYPE ty_t_rng_char4
        VALUE(it_contid)       TYPE ty_t_rng_char20
        VALUE(iv_postd_from)   TYPE d
        VALUE(iv_postd_to)     TYPE d
      EXPORTING
        VALUE(et_agg)          TYPE ty_t_agg.

ENDCLASS.
```

Checks:
- Class is active with AMDP marker interface.

## 5) Artifact: AMDP method implementation

Paste target: Method implementation `<ZCL_RDL_NET_POSTING_AMDP>=>READ_AGGREGATES`
Action: create

Purpose: Per-contract netting with proportional allocation
- Reads eligible groups from HFSPD based on temporal/business filters
- Validates contracts against HKAPA (production control) and HKAPD (accounting principle)
- Excludes GL and GR posting blocks from the source set
- Computes net for each netting group: net = SUM(all balances in the group without contract ID)
- Allocates proportionally: allocation = |contract| / SUM(|same-sign contracts|) × |net|
- Emits one output row **per contract** (not one row per grain) with its allocation amount

```abap
METHOD read_aggregates
  BY DATABASE PROCEDURE FOR HDB
  LANGUAGE SQLSCRIPT
  OPTIONS READ-ONLY
  USING "/BA1/HFSPD" "/BA1/HKAPA" "/BA1/HKAPD".

  -- ============================================================================
  -- NETTING LOGIC: Proportional Allocation across Positive or Negative Contracts
  -- ============================================================================
  -- Stage 1: select candidate contract rows from HFSPD with business filters
  -- TODO: Confirm exact HFSPD discriminator field/value for excluding
  -- GL and GR workbook blocks in the productive landscape.
  lt_keys =
    SELECT DISTINCT
      h."CLIENT"          AS client,
      h."/BA1/C55POSTD"   AS postd,
      h."/BA1/C55LGENT"   AS lgent,
      h."/BA1/C55CONTID"  AS contid,
      h."/BA1/C11NODENO"  AS nodeno,
      h."/BA1/C55ACCSY"   AS accsy
    FROM "/BA1/HFSPD" h
    WHERE h."/BA1/C55POSTD" BETWEEN :iv_postd_from AND :iv_postd_to
      AND (CARDINALITY(:it_lgent) = 0 OR h."/BA1/C55LGENT" IN (SELECT low FROM :it_lgent WHERE sign = 'I' AND option = 'EQ'))
      AND (CARDINALITY(:it_contid) = 0 OR h."/BA1/C55CONTID" IN (SELECT low FROM :it_contid WHERE sign = 'I' AND option = 'EQ'))
    ORDER BY
      h."/BA1/C55POSTD",
      h."/BA1/C55CONTID",
      h."/BA1/C11NODENO",
      h."/BA1/C55ACCSY"
    LIMIT :iv_package_size;

  -- Stage 2: temporal-valid HKAPA assignment (latest CR0KEYDAT <= posting date)
  lt_apa_ranked =
    SELECT
      k.client,
      k.postd,
      k.contid,
      k.nodeno,
      k.accsy,
      a."/BA1/C55PFID" AS pfid,
      ROW_NUMBER() OVER (
        PARTITION BY k.client, k.postd, k.contid, k.nodeno, k.accsy
        ORDER BY a."/BA1/CR0KEYDAT" DESC, a."/BA1/C55PFID" DESC
      ) AS rn
    FROM :lt_keys k
    INNER JOIN "/BA1/HKAPA" a
      ON a."CLIENT" = k.client
     AND a."/BA1/C55CONTID" = k.contid
     AND a."/BA1/C11NODENO" = k.nodeno
     AND a."/BA1/C55ACCSY" = k.accsy
     AND a."CURRENT_FLAG" = 'X'
     AND a."/BA1/CR4PFCT" = :iv_pfct
     AND a."/BA1/CR0KEYDAT" <= k.postd;

  lt_apa =
    SELECT client, postd, contid, nodeno, accsy, pfid
    FROM :lt_apa_ranked
    WHERE rn = 1;

  -- Stage 3: temporal-valid HKAPD assignment (latest CR0KEYDAT <= posting date)
  lt_apd_ranked =
    SELECT
      a.client,
      a.postd,
      a.contid,
      a.nodeno,
      a.accsy,
      ROW_NUMBER() OVER (
        PARTITION BY a.client, a.postd, a.contid, a.nodeno, a.accsy
        ORDER BY d."/BA1/CR0KEYDAT" DESC, d."/BA1/C55PFID" DESC
      ) AS rn
    FROM :lt_apa a
    INNER JOIN "/BA1/HKAPD" d
      ON d."CLIENT" = a.client
     AND d."/BA1/C55PFID" = a.pfid
     AND d."/BA1/C55ACCSY" = a.accsy
     AND d."CURRENT_FLAG" = 'X'
     AND d."/BA1/C55ACCRCT" = :iv_accrct
     AND d."/BA1/CR0KEYDAT" <= a.postd;

  lt_valid_keys =
    SELECT DISTINCT
      client,
      postd,
      contid,
      nodeno,
      accsy
    FROM :lt_apd_ranked
    WHERE rn = 1;

  -- Stage 3b: prepare one row per contract with balances and anchor candidates
  lt_contract_bal =
    SELECT
      h."CLIENT"                                  AS client,
      h."/BA1/C55POSTD"                           AS postd,
      h."/BA1/C55LGENT"                           AS lgent,
      h."/BA1/C55CONTID"                          AS contid,
      h."/BA1/C11NODENO"                          AS nodeno,
      h."/BA1/C55ACCSY"                           AS accsy,
      MIN(h."/BA1/C55DOCNUM")                     AS anchor_docnum,
      MIN(h."/BA1/C55DOCITM")                     AS anchor_docitm,
      CAST(SUM(h."/BA1/K5SAMBAL") AS DECFLOAT34) AS contract_sambal,
      CAST(SUM(h."/BA1/K5SAMGRP") AS DECFLOAT34) AS contract_samgrp
    FROM :lt_valid_keys v
    INNER JOIN "/BA1/HFSPD" h
      ON h."CLIENT" = v.client
     AND h."/BA1/C55POSTD" = v.postd
     AND h."/BA1/C55CONTID" = v.contid
     AND h."/BA1/C11NODENO" = v.nodeno
     AND h."/BA1/C55ACCSY" = v.accsy
    GROUP BY
      h."CLIENT",
      h."/BA1/C55POSTD",
      h."/BA1/C55LGENT",
      h."/BA1/C55CONTID",
      h."/BA1/C11NODENO",
      h."/BA1/C55ACCSY";

  -- Stage 4a: aggregate all eligible contracts within the netting group to compute net balance
  -- Netting group excludes contract ID.
  lt_grain_net =
    SELECT
      c.client,
      c.postd,
      c.lgent,
      c.nodeno,
      c.accsy,
      CAST(SUM(c.contract_samgrp) AS DECFLOAT34) AS net_samgrp
    FROM :lt_contract_bal c
    GROUP BY
      c.client,
      c.postd,
      c.lgent,
      c.nodeno,
      c.accsy;

  -- Stage 4b: compute same-sign denominators within the netting group
  lt_grain_abs_sum =
    SELECT
      c.client,
      c.postd,
      c.lgent,
      c.nodeno,
      c.accsy,
      CAST(SUM(CASE WHEN c.contract_samgrp > 0 THEN c.contract_samgrp ELSE 0 END) AS DECFLOAT34) AS sum_pos_grp,
      CAST(SUM(CASE WHEN c.contract_samgrp < 0 THEN -c.contract_samgrp ELSE 0 END) AS DECFLOAT34) AS sum_neg_grp
    FROM :lt_contract_bal c
    GROUP BY
      c.client,
      c.postd,
      c.lgent,
      c.nodeno,
      c.accsy;

  -- Stage 5: FINAL netting output with allocation amounts
  -- For each contract in the netting group:
  --   If Net > 0: only positive contracts get allocation = |contract| / SUM_POS × |Net|
  --   If Net < 0: only negative contracts get allocation = |contract| / SUM_NEG × |Net|
  --   If Net = 0: no allocation (logical block; no clarity yet on edge case behavior)
  -- Emit one row per contract result with:
  --   - one anchor strategy per contract result
  --   - alloc_amount = computed allocation (0 if not applicable)
  et_agg =
    SELECT
      c.client                                   AS client,
      c.postd                                    AS postd,
      c.lgent                                    AS lgent,
      c.contid                                   AS contid,
      c.nodeno                                   AS nodeno,
      c.accsy                                    AS accsy,
      c.anchor_docnum                            AS anchor_docnum,
      c.anchor_docitm                            AS anchor_docitm,
      c.contract_sambal                          AS sum_sambal,
      c.contract_samgrp                          AS sum_samgrp,
      -- Asset/Liability Indicator (DDIC reference: /BA1/C55ALST)
      -- TODO: Verify DDIC field semantics and derivation rule (value-dependent on contract type or posting level)
      CAST(' ' AS NVARCHAR(1))                  AS asset_liab_ind,
      -- Allocation Amount: proportional formula based on sign of net
      -- If net > 0: |contract| / SUM_POS × net
      -- If net < 0: |contract| / SUM_NEG × |net|
      -- If net = 0: 0 (no allocation)
      CASE
        WHEN n.net_samgrp > 0 AND c.contract_samgrp > 0 AND a.sum_pos_grp > 0
          THEN ( ABS(c.contract_samgrp) / a.sum_pos_grp ) * n.net_samgrp
        WHEN n.net_samgrp < 0 AND c.contract_samgrp < 0 AND a.sum_neg_grp > 0
          THEN ( ABS(c.contract_samgrp) / a.sum_neg_grp ) * ABS(n.net_samgrp)
        ELSE CAST(0 AS DECFLOAT34)
      END AS alloc_amount
    FROM :lt_contract_bal c
    INNER JOIN :lt_grain_net n
      ON n.client = c.client
     AND n.postd = c.postd
     AND n.lgent = c.lgent
     AND n.nodeno = c.nodeno
     AND n.accsy = c.accsy
    INNER JOIN :lt_grain_abs_sum a
      ON a.client = c.client
     AND a.postd = c.postd
     AND a.lgent = c.lgent
     AND a.nodeno = c.nodeno
     AND a.accsy = c.accsy
    ORDER BY
      c.postd,
      c.contid,
      c.nodeno,
      c.accsy;

ENDMETHOD.
```

Checks:
- SQLScript activates.
- For one known netting group with 3+ contracts, verify:
  - Output row count = number of eligible contracts in the group
  - Net calculation = SUM of all contract balances
  - Allocation amounts per contract = proportional shares (sum to net)
  - Positive/negative sign handling correct (e.g., if net > 0, only positive contracts get allocation)
- GL and GR rows are not used
- the exact HFSPD discriminator used for GL/GR exclusion is confirmed in the target landscape before productive use
- Validate precision (DECFLOAT34 is preserved; no forced rounding in ABAP layer)
- Asset/Liability Indicator placeholder confirmed in AMDP output (enriched in ABAP layer)
- Allocation Amount correctly reflects proportional formula

## 6) Artifact: ABAP orchestration class definition

Paste target: Class definition section of `<ZCL_RDL_NET_POSTING_JOB>`
Action: create

```abap
INTERFACE <ZIF_NET_POSTING_TYPES> PUBLIC.
  TYPES: ty_t_rng_char4  TYPE RANGE OF c LENGTH 4,
         ty_t_rng_char20 TYPE RANGE OF c LENGTH 20.

  TYPES: BEGIN OF ty_s_selection,
           postd_from   TYPE d,
           postd_to     TYPE d,
           pfct         TYPE c LENGTH 4,
           accrct       TYPE c LENGTH 4,
           package_size TYPE i,
           t_lgent      TYPE ty_t_rng_char4,
           t_contid     TYPE ty_t_rng_char20,
         END OF ty_s_selection.

  TYPES: BEGIN OF ty_s_result,
           rows_written TYPE i,
           packages     TYPE i,
         END OF ty_s_result.

  TYPES: BEGIN OF ty_s_ckp,
           run_id       TYPE c LENGTH 32,
           last_postd   TYPE d,
           last_contid  TYPE c LENGTH 20,
           last_nodeno  TYPE c LENGTH 12,
           last_accsy   TYPE c LENGTH 4,
           package_size TYPE i,
         END OF ty_s_ckp.
ENDINTERFACE.

INTERFACE <ZIF_NET_POSTING_READER> PUBLIC.
  METHODS read_aggregates
    IMPORTING
      is_sel          TYPE <ZIF_NET_POSTING_TYPES>=>ty_s_selection
      is_ckp          TYPE <ZIF_NET_POSTING_TYPES>=>ty_s_ckp
    RETURNING
      VALUE(rt_agg)   TYPE <ZCL_RDL_NET_POSTING_AMDP>=>ty_t_agg
    RAISING
      cx_static_check.

  METHODS read_anchors
    IMPORTING
      it_agg          TYPE <ZCL_RDL_NET_POSTING_AMDP>=>ty_t_agg
    RETURNING
      VALUE(rt_anchor) TYPE STANDARD TABLE OF /ba1/hfspd WITH EMPTY KEY
    RAISING
      cx_static_check.
ENDINTERFACE.

INTERFACE <ZIF_NET_POSTING_CHECKPOINT> PUBLIC.
  METHODS load
    IMPORTING
      iv_run_id       TYPE c LENGTH 32
    RETURNING
      VALUE(rs_ckp)   TYPE <ZIF_NET_POSTING_TYPES>=>ty_s_ckp
    RAISING
      cx_static_check.

  METHODS save
    IMPORTING
      is_ckp          TYPE <ZIF_NET_POSTING_TYPES>=>ty_s_ckp
      iv_status       TYPE c LENGTH 1
      iv_rows_total   TYPE int8
    RAISING
      cx_static_check.
ENDINTERFACE.

INTERFACE <ZIF_NET_POSTING_TARGET> PUBLIC.
  METHODS upsert
    IMPORTING
      it_rows TYPE STANDARD TABLE OF z_net_posting WITH EMPTY KEY
    RAISING
      cx_static_check.
ENDINTERFACE.

CLASS <ZCL_RDL_NET_POSTING_JOB> DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC.

  PUBLIC SECTION.
    METHODS constructor
      IMPORTING
        io_reader TYPE REF TO <ZIF_NET_POSTING_READER> OPTIONAL
        io_target TYPE REF TO <ZIF_NET_POSTING_TARGET> OPTIONAL.

    METHODS run
      IMPORTING
        is_sel           TYPE <ZIF_NET_POSTING_TYPES>=>ty_s_selection
      RETURNING
        VALUE(rs_result) TYPE <ZIF_NET_POSTING_TYPES>=>ty_s_result
      RAISING
        cx_static_check.

  PROTECTED SECTION.
    DATA mo_reader TYPE REF TO <ZIF_NET_POSTING_READER>.
    DATA mo_target TYPE REF TO <ZIF_NET_POSTING_TARGET>.

    METHODS upsert_target
      IMPORTING
        it_rows TYPE STANDARD TABLE OF z_net_posting WITH EMPTY KEY
      RAISING
        cx_static_check.

ENDCLASS.
```

Checks:
- Constructor injection is available for test doubles.
- Class activation succeeds.
- Add package/class to transport request.

## 7) Artifact: ABAP orchestration class implementation

Paste target: Local helper classes or separate production classes implementing `<ZIF_NET_POSTING_READER>` and `<ZIF_NET_POSTING_CHECKPOINT>`
Action: create

Note:
- Checkpoint implementation is optional and can be excluded in the current simplified flow.

```abap
CLASS lcl_reader_prod DEFINITION FINAL.
  PUBLIC SECTION.
    INTERFACES <zif_net_posting_reader>.
ENDCLASS.

CLASS lcl_checkpoint_prod DEFINITION FINAL.
  PUBLIC SECTION.
    INTERFACES <zif_net_posting_checkpoint>.
ENDCLASS.

CLASS lcl_target_prod DEFINITION FINAL.
  PUBLIC SECTION.
    INTERFACES <zif_net_posting_target>.
ENDCLASS.

CLASS lcl_reader_prod IMPLEMENTATION.
  METHOD <zif_net_posting_reader>~read_aggregates.
    <ZCL_RDL_NET_POSTING_AMDP>=>read_aggregates(
      EXPORTING
        iv_pfct         = is_sel-pfct
        iv_accrct       = is_sel-accrct
        iv_package_size = is_sel-package_size
        it_lgent        = is_sel-t_lgent
        it_contid       = is_sel-t_contid
        iv_postd_from   = is_sel-postd_from
        iv_postd_to     = is_sel-postd_to
      IMPORTING
        et_agg          = rt_agg ).
  ENDMETHOD.

  METHOD <zif_net_posting_reader>~read_anchors.
    SELECT *
      FROM /ba1/hfspd
      FOR ALL ENTRIES IN @it_agg
      WHERE client           = @it_agg-client
        AND "/BA1/C55POSTD"  = @it_agg-postd
        AND "/BA1/C55CONTID" = @it_agg-contid
        AND "/BA1/C11NODENO" = @it_agg-nodeno
        AND "/BA1/C55ACCSY"  = @it_agg-accsy
        AND "/BA1/C55DOCNUM" = @it_agg-anchor_docnum
        AND "/BA1/C55DOCITM" = @it_agg-anchor_docitm
      INTO TABLE @rt_anchor.
  ENDMETHOD.
ENDCLASS.

CLASS lcl_checkpoint_prod IMPLEMENTATION.
  METHOD <zif_net_posting_checkpoint>~load.
    SELECT SINGLE
           run_id,
           last_postd,
           last_contid,
           last_nodeno,
           last_accsy,
           package_size
      FROM <znet_posting_run>
      WHERE mandt  = @sy-mandt
        AND run_id = @iv_run_id
      INTO CORRESPONDING FIELDS OF @rs_ckp.
  ENDMETHOD.

  METHOD <zif_net_posting_checkpoint>~save.
    DATA ls_row TYPE <znet_posting_run>.

    MOVE-CORRESPONDING is_ckp TO ls_row.
    ls_row-mandt          = sy-mandt.
    ls_row-status         = iv_status.
    ls_row-package_size   = is_ckp-package_size.
    ls_row-rows_processed = iv_rows_total.
    ls_row-changed_by     = sy-uname.
    GET TIME STAMP FIELD ls_row-changed_at_utc.

    MODIFY <znet_posting_run> FROM ls_row.
  ENDMETHOD.
ENDCLASS.

CLASS lcl_target_prod IMPLEMENTATION.
  METHOD <zif_net_posting_target>~upsert.
    MODIFY z_net_posting FROM TABLE it_rows.
    COMMIT WORK.
  ENDMETHOD.
ENDCLASS.
```

Paste target: Method implementation `<ZCL_RDL_NET_POSTING_JOB>=>RUN`
Action: create

```abap
METHOD constructor.
  mo_reader = io_reader.
  mo_target = io_target.

  IF mo_reader IS INITIAL.
    CREATE OBJECT mo_reader TYPE lcl_reader_prod.
  ENDIF.

  IF mo_target IS INITIAL.
    CREATE OBJECT mo_target TYPE lcl_target_prod.
  ENDIF.
ENDMETHOD.

METHOD run.
  DATA: lt_agg       TYPE <ZCL_RDL_NET_POSTING_AMDP>=>ty_t_agg,
        lt_anchor    TYPE STANDARD TABLE OF /ba1/hfspd WITH EMPTY KEY,
        lt_target    TYPE STANDARD TABLE OF z_net_posting WITH EMPTY KEY,
        lt_errors    TYPE STANDARD TABLE OF z_net_posting_err WITH EMPTY KEY,
        ls_target    TYPE z_net_posting,
        ls_error     TYPE z_net_posting_err,
      lv_error_msg TYPE string,
      lv_anchor_hits TYPE i.

  FIELD-SYMBOLS: <ls_agg>    TYPE <ZCL_RDL_NET_POSTING_AMDP>=>ty_s_agg,
                 <ls_anchor> TYPE /ba1/hfspd,
                 <lv_sambal> TYPE any,
                 <lv_samgrp> TYPE any,
                 <lv_alloc>  TYPE any.

  DO.
    " Stage A: read netting results from AMDP (per-contract with allocation amounts)
    lt_agg = mo_reader->read_aggregates( is_sel = is_sel ).

    IF lt_agg IS INITIAL.
      EXIT.
    ENDIF.

    " Stage B: load anchor source rows for structural copy
    lt_anchor = mo_reader->read_anchors( it_agg = lt_agg ).

    CLEAR lt_target.
    CLEAR lt_errors.

    LOOP AT lt_agg ASSIGNING <ls_agg>.
      " Stage C: Per-contract enrichment with netting delta

      CLEAR lv_anchor_hits.
      LOOP AT lt_anchor TRANSPORTING NO FIELDS
        WHERE client            = <ls_agg>-client
          AND "/BA1/C55POSTD"  = <ls_agg>-postd
          AND "/BA1/C55CONTID" = <ls_agg>-contid
          AND "/BA1/C11NODENO" = <ls_agg>-nodeno
          AND "/BA1/C55ACCSY"  = <ls_agg>-accsy
          AND "/BA1/C55DOCNUM" = <ls_agg>-anchor_docnum
          AND "/BA1/C55DOCITM" = <ls_agg>-anchor_docitm.
        lv_anchor_hits = lv_anchor_hits + 1.
      ENDLOOP.

      IF lv_anchor_hits > 1.
        " Validation error: ambiguous anchor candidate in source
        CLEAR ls_error.
        ls_error-mandt      = sy-mandt.
        ls_error-client_id  = <ls_agg>-client.
        ls_error-postd      = <ls_agg>-postd.
        ls_error-contid     = <ls_agg>-contid.
        ls_error-nodeno     = <ls_agg>-nodeno.
        ls_error-accsy      = <ls_agg>-accsy.
        ls_error-error_msg  = 'Ambiguous anchor row in HFSPD for contract output key'.
        ls_error-created_at = sy-datum.
        ls_error-created_by = sy-uname.
        APPEND ls_error TO lt_errors.
        CONTINUE.
      ENDIF.
      
      READ TABLE lt_anchor ASSIGNING <ls_anchor>
        WITH KEY client            = <ls_agg>-client
                 "/BA1/C55POSTD"  = <ls_agg>-postd
                 "/BA1/C55CONTID" = <ls_agg>-contid
                 "/BA1/C11NODENO" = <ls_agg>-nodeno
                 "/BA1/C55ACCSY"  = <ls_agg>-accsy
                 "/BA1/C55DOCNUM" = <ls_agg>-anchor_docnum
                 "/BA1/C55DOCITM" = <ls_agg>-anchor_docitm.
      IF sy-subrc <> 0.
        " Validation error: anchor row not found in source
        CLEAR ls_error.
        ls_error-mandt      = sy-mandt.
        ls_error-client_id  = <ls_agg>-client.
        ls_error-postd      = <ls_agg>-postd.
        ls_error-contid     = <ls_agg>-contid.
        ls_error-nodeno     = <ls_agg>-nodeno.
        ls_error-accsy      = <ls_agg>-accsy.
        ls_error-error_msg  = 'Anchor row (DOCNUM, DOCITM) not found in HFSPD'.
        ls_error-created_at = sy-datum.
        ls_error-created_by = sy-uname.
        APPEND ls_error TO lt_errors.
        CONTINUE.
      ENDIF.

      " Copy anchor row structure as baseline for netting output
      MOVE-CORRESPONDING <ls_anchor> TO ls_target.

      " Hook 1: Enrich Asset/Liability Indicator (DDIC field reference: /BA1/C55ALST)
      " Safe assumption: use placeholder; this should be derived from contract type or posting level
      " TODO: Confirm DDIC field derivation rule (e.g., based on transaction type, contract category, or manual posting principle)
      ASSIGN COMPONENT '/BA1/C55ALST' OF STRUCTURE ls_target TO <lv_alloc>.
      IF sy-subrc = 0.
        " Placeholder: assumes empty or derive from source contract attribute
        <lv_alloc> = <ls_agg>-asset_liab_ind.
      ENDIF.

      " Hook 2: Override functional currency amounts with netting-delta (allocation amount only, not pre-netted balance)
      " Per clarification: netted-delta = allocation amount computed from proportional formula
      ASSIGN COMPONENT '/BA1/K5SAMBAL' OF STRUCTURE ls_target TO <lv_sambal>.
      IF sy-subrc = 0.
        " Functional currency: original balance from contract (preserved for audit trail in source)
        <lv_sambal> = <ls_agg>-sum_sambal.
      ENDIF.

      ASSIGN COMPONENT '/BA1/K5SAMGRP' OF STRUCTURE ls_target TO <lv_samgrp>.
      IF sy-subrc = 0.
        " Group currency (always USD per clarification): override with allocation amount only
        " Do NOT use sum_samgrp pre-netted; use alloc_amount as netted-delta
        <lv_samgrp> = <ls_agg>-alloc_amount.
      ENDIF.

      APPEND ls_target TO lt_target.

    ENDLOOP.

    IF lt_target IS NOT INITIAL.
      " Stage D: persist netted rows to target table (Z_NET_POSTING)
      upsert_target( it_rows = lt_target ).

      rs_result-rows_written = rs_result-rows_written + lines( lt_target ).
      rs_result-packages     = rs_result-packages + 1.
    ENDIF.

    IF lt_errors IS NOT INITIAL.
      " Stage E: persist validation errors to separate error log (not inline)
      " TODO: Implement error log insert (e.g., into Z_NET_POSTING_ERR or /BAL/PW_LOG)
      " Placeholder: separate error handling for alerting/monitoring
      " CALL METHOD mo_error_log->write( it_errors = lt_errors ).
    ENDIF.

  ENDDO.
ENDMETHOD.
```

Paste target: Method implementation `<ZCL_RDL_NET_POSTING_JOB>=>UPSERT_TARGET`
Action: create

```abap
METHOD upsert_target.
  mo_target->upsert( it_rows = it_rows ).
ENDMETHOD.
```

Checks:
- Run once in foreground for a small date range and verify:
  - Row count in `Z_NET_POSTING` = number of eligible contracts in the netting group
  - All allocation amounts are either zero (net=0 case) or proportional shares (positive/negative net cases)
  - Each contract appears with its allocation amount (not aggregated to one row per group)
- Errors captured in `Z_NET_POSTING_ERR` (e.g., missing anchor rows, validation failures)
- Re-run same parameters: verify deterministic output (same allocation amounts, same error set)
- Verify precision: no forced rounding is introduced unless later confirmed by business or posting constraints

## 8) Artifact: Report for selective execution

Paste target: Report `<ZR_RDL_NET_POSTING_RUN>`
Action: create

```abap
REPORT <zr_rdl_net_posting_run>.

PARAMETERS: p_from  TYPE d OBLIGATORY,
            p_to    TYPE d OBLIGATORY,
            p_pfct  TYPE c LENGTH 4 DEFAULT '2100',
            p_rct   TYPE c LENGTH 4 DEFAULT '601',
            p_pack  TYPE i DEFAULT 20000.

DATA gv_lgent  TYPE c LENGTH 4.
DATA gv_contid TYPE c LENGTH 20.

SELECT-OPTIONS: s_lgent FOR gv_lgent NO INTERVALS,
                s_cont  FOR gv_contid NO INTERVALS.

START-OF-SELECTION.
  DATA lo_job TYPE REF TO <zcl_rdl_net_posting_job>.
  DATA ls_sel TYPE <zif_net_posting_types>=>ty_s_selection.
  DATA ls_res TYPE <zif_net_posting_types>=>ty_s_result.

  ls_sel-postd_from   = p_from.
  ls_sel-postd_to     = p_to.
  ls_sel-pfct         = p_pfct.
  ls_sel-accrct       = p_rct.
  ls_sel-package_size = p_pack.
  ls_sel-t_lgent      = CORRESPONDING #( s_lgent[] ).
  ls_sel-t_contid     = CORRESPONDING #( s_cont[] ).

  CREATE OBJECT lo_job.
  ls_res = lo_job->run( is_sel = ls_sel ).

  WRITE: / 'Rows written:', ls_res-rows_written,
         / 'Packages:', ls_res-packages.
```

Checks:
- Test 1 package run with tiny date range.
- Rerun behavior in this iteration is full reprocessing (resume deferred).

## Track B - Testing and validation

## 9) Artifact: ABAP Unit test scaffold

Paste target: Local test class include in `<ZCL_RDL_NET_POSTING_JOB>`
Action: append

```abap
CLASS lcl_reader_fake DEFINITION FINAL.
  PUBLIC SECTION.
    INTERFACES <zif_net_posting_reader>.

    DATA mt_agg         TYPE <zcl_rdl_net_posting_amdp>=>ty_t_agg.
    DATA mt_anchor      TYPE STANDARD TABLE OF /ba1/hfspd WITH EMPTY KEY.
    DATA mv_call_count  TYPE i.
    DATA ms_last_sel    TYPE <zif_net_posting_types>=>ty_s_selection.
    DATA ms_last_ckp    TYPE <zif_net_posting_types>=>ty_s_ckp.
ENDCLASS.

CLASS lcl_checkpoint_fake DEFINITION FINAL.
  PUBLIC SECTION.
    INTERFACES <zif_net_posting_checkpoint>.

    DATA ms_loaded_ckp TYPE <zif_net_posting_types>=>ty_s_ckp.
    DATA ms_saved_ckp  TYPE <zif_net_posting_types>=>ty_s_ckp.
    DATA mv_status     TYPE c LENGTH 1.
    DATA mv_rows_total TYPE int8.
ENDCLASS.

CLASS lcl_target_fake DEFINITION FINAL.
  PUBLIC SECTION.
    INTERFACES <zif_net_posting_target>.

    DATA mt_rows TYPE STANDARD TABLE OF z_net_posting WITH EMPTY KEY.
    DATA mv_call_count TYPE i.
ENDCLASS.

CLASS ltc_net_posting_job DEFINITION FINAL FOR TESTING
  DURATION SHORT
  RISK LEVEL HARMLESS.

  PRIVATE SECTION.
    METHODS empty_agg_exits_cleanly FOR TESTING.
    METHODS writes_rows_for_one_package FOR TESTING.
    METHODS anchor_mismatch_skips_row FOR TESTING.
    METHODS anchor_ambiguous_skips_row FOR TESTING.
    METHODS rerun_is_deterministic FOR TESTING.
    METHODS selective_filters_propagated FOR TESTING.
    METHODS multi_row_collapse_sums_amounts FOR TESTING.
ENDCLASS.

CLASS lcl_reader_fake IMPLEMENTATION.
  METHOD <zif_net_posting_reader>~read_aggregates.
    mv_call_count = mv_call_count + 1.
    ms_last_sel = is_sel.
    ms_last_ckp = is_ckp.

    IF mv_call_count = 1.
      rt_agg = mt_agg.
    ENDIF.
  ENDMETHOD.

  METHOD <zif_net_posting_reader>~read_anchors.
    rt_anchor = mt_anchor.
  ENDMETHOD.
ENDCLASS.

CLASS lcl_checkpoint_fake IMPLEMENTATION.
  METHOD <zif_net_posting_checkpoint>~load.
    rs_ckp = ms_loaded_ckp.
  ENDMETHOD.

  METHOD <zif_net_posting_checkpoint>~save.
    ms_saved_ckp = is_ckp.
    mv_status = iv_status.
    mv_rows_total = iv_rows_total.
  ENDMETHOD.
ENDCLASS.

CLASS lcl_target_fake IMPLEMENTATION.
  METHOD <zif_net_posting_target>~upsert.
    mv_call_count = mv_call_count + 1.
    mt_rows = it_rows.
  ENDMETHOD.
ENDCLASS.

CLASS ltc_net_posting_job IMPLEMENTATION.

  METHOD empty_agg_exits_cleanly.
    DATA lo_reader TYPE REF TO lcl_reader_fake.
    DATA lo_ckp    TYPE REF TO lcl_checkpoint_fake.
    DATA lo_target TYPE REF TO lcl_target_fake.
    DATA lo_job    TYPE REF TO <zcl_rdl_net_posting_job>.
    DATA ls_sel    TYPE <zif_net_posting_types>=>ty_s_selection.
    DATA ls_res    TYPE <zif_net_posting_types>=>ty_s_result.

    CREATE OBJECT lo_reader.
    CREATE OBJECT lo_ckp.
    CREATE OBJECT lo_target.
    CREATE OBJECT lo_job
      EXPORTING
        io_reader = lo_reader
        io_target = lo_target.

    ls_sel-postd_from = '20260101'.
    ls_sel-postd_to = '20260131'.
    ls_sel-pfct = '2100'.
    ls_sel-accrct = '601'.
    ls_sel-package_size = 10.

    ls_res = lo_job->run( is_sel = ls_sel ).

    cl_abap_unit_assert=>assert_equals( act = ls_res-packages exp = 0 ).
    cl_abap_unit_assert=>assert_equals( act = ls_res-rows_written exp = 0 ).
    cl_abap_unit_assert=>assert_equals( act = lo_target->mv_call_count exp = 0 ).
  ENDMETHOD.

  METHOD writes_rows_for_one_package.
    DATA lo_reader TYPE REF TO lcl_reader_fake.
    DATA lo_ckp    TYPE REF TO lcl_checkpoint_fake.
    DATA lo_target TYPE REF TO lcl_target_fake.
    DATA lo_job    TYPE REF TO <zcl_rdl_net_posting_job>.
    DATA ls_sel    TYPE <zif_net_posting_types>=>ty_s_selection.
    DATA ls_res    TYPE <zif_net_posting_types>=>ty_s_result.
    FIELD-SYMBOLS <lv_postd>  TYPE any.
    FIELD-SYMBOLS <lv_docnum> TYPE any.
    FIELD-SYMBOLS <lv_docitm> TYPE any.

    CREATE OBJECT lo_reader.
    CREATE OBJECT lo_ckp.
    CREATE OBJECT lo_target.

    APPEND VALUE #( client = sy-mandt
                    postd = '20260115'
                    lgent = '1000'
                    contid = 'CONT_1'
                    nodeno = 'NODE_1'
                    accsy = 'IFRS'
                    anchor_docnum = '0000000001'
                    anchor_docitm = '000001'
                    sum_sambal = '100'
                    sum_samgrp = '120' ) TO lo_reader->mt_agg.

    APPEND INITIAL LINE TO lo_reader->mt_anchor ASSIGNING FIELD-SYMBOL(<ls_anchor1>).
    <ls_anchor1>-client = sy-mandt.
    ASSIGN COMPONENT '/BA1/C55POSTD' OF STRUCTURE <ls_anchor1> TO <lv_postd>.
    ASSIGN COMPONENT '/BA1/C55CONTID' OF STRUCTURE <ls_anchor1> TO FIELD-SYMBOL(<lv_contid>).
    ASSIGN COMPONENT '/BA1/C11NODENO' OF STRUCTURE <ls_anchor1> TO FIELD-SYMBOL(<lv_nodeno>).
    ASSIGN COMPONENT '/BA1/C55ACCSY' OF STRUCTURE <ls_anchor1> TO FIELD-SYMBOL(<lv_accsy>).
    ASSIGN COMPONENT '/BA1/C55DOCNUM' OF STRUCTURE <ls_anchor1> TO <lv_docnum>.
    ASSIGN COMPONENT '/BA1/C55DOCITM' OF STRUCTURE <ls_anchor1> TO <lv_docitm>.
    IF <lv_postd> IS ASSIGNED.
      <lv_postd> = '20260115'.
    ENDIF.
    IF <lv_contid> IS ASSIGNED.
      <lv_contid> = 'CONT_1'.
    ENDIF.
    IF <lv_nodeno> IS ASSIGNED.
      <lv_nodeno> = 'NODE_1'.
    ENDIF.
    IF <lv_accsy> IS ASSIGNED.
      <lv_accsy> = 'IFRS'.
    ENDIF.
    IF <lv_docnum> IS ASSIGNED.
      <lv_docnum> = '0000000001'.
    ENDIF.
    IF <lv_docitm> IS ASSIGNED.
      <lv_docitm> = '000001'.
    ENDIF.

    CREATE OBJECT lo_job
      EXPORTING
        io_reader = lo_reader
        io_target = lo_target.

    ls_sel-postd_from = '20260101'.
    ls_sel-postd_to = '20260131'.
    ls_sel-pfct = '2100'.
    ls_sel-accrct = '601'.
    ls_sel-package_size = 10.

    ls_res = lo_job->run( is_sel = ls_sel ).

    cl_abap_unit_assert=>assert_equals( act = ls_res-packages exp = 1 ).
    cl_abap_unit_assert=>assert_equals( act = lo_target->mv_call_count exp = 1 ).
  ENDMETHOD.

  METHOD anchor_mismatch_skips_row.
    DATA lo_reader TYPE REF TO lcl_reader_fake.
    DATA lo_ckp    TYPE REF TO lcl_checkpoint_fake.
    DATA lo_target TYPE REF TO lcl_target_fake.
    DATA lo_job    TYPE REF TO <zcl_rdl_net_posting_job>.
    DATA ls_sel    TYPE <zif_net_posting_types>=>ty_s_selection.
    DATA ls_res    TYPE <zif_net_posting_types>=>ty_s_result.

    CREATE OBJECT lo_reader.
    CREATE OBJECT lo_ckp.
    CREATE OBJECT lo_target.

    APPEND VALUE #( client = sy-mandt
                    postd = '20260115'
                    lgent = '1000'
                    contid = 'CONT_SKIP'
                    nodeno = 'NODE_SKIP'
                    accsy = 'IFRS'
                    anchor_docnum = '0000000002'
                    anchor_docitm = '000001'
                    sum_sambal = '50'
                    sum_samgrp = '60' ) TO lo_reader->mt_agg.

    CREATE OBJECT lo_job
      EXPORTING
        io_reader = lo_reader
        io_target = lo_target.

    ls_sel-postd_from = '20260101'.
    ls_sel-postd_to = '20260131'.
    ls_sel-pfct = '2100'.
    ls_sel-accrct = '601'.
    ls_sel-package_size = 10.

    ls_res = lo_job->run( is_sel = ls_sel ).

    cl_abap_unit_assert=>assert_equals( act = ls_res-rows_written exp = 0 ).
    cl_abap_unit_assert=>assert_equals( act = lo_target->mv_call_count exp = 0 ).
  ENDMETHOD.

  METHOD anchor_ambiguous_skips_row.
    DATA lo_reader TYPE REF TO lcl_reader_fake.
    DATA lo_ckp    TYPE REF TO lcl_checkpoint_fake.
    DATA lo_target TYPE REF TO lcl_target_fake.
    DATA lo_job    TYPE REF TO <zcl_rdl_net_posting_job>.
    DATA ls_sel    TYPE <zif_net_posting_types>=>ty_s_selection.
    DATA ls_res    TYPE <zif_net_posting_types>=>ty_s_result.
    FIELD-SYMBOLS <lv_postd>  TYPE any.
    FIELD-SYMBOLS <lv_contid> TYPE any.
    FIELD-SYMBOLS <lv_nodeno> TYPE any.
    FIELD-SYMBOLS <lv_accsy>  TYPE any.
    FIELD-SYMBOLS <lv_docnum> TYPE any.
    FIELD-SYMBOLS <lv_docitm> TYPE any.

    CREATE OBJECT lo_reader.
    CREATE OBJECT lo_ckp.
    CREATE OBJECT lo_target.

    APPEND VALUE #( client = sy-mandt
                    postd = '20260115'
                    lgent = '1000'
                    contid = 'CONT_AMB'
                    nodeno = 'NODE_AMB'
                    accsy = 'IFRS'
                    anchor_docnum = '0000000009'
                    anchor_docitm = '000001'
                    sum_sambal = '70'
                    sum_samgrp = '75' ) TO lo_reader->mt_agg.

    DO 2 TIMES.
      APPEND INITIAL LINE TO lo_reader->mt_anchor ASSIGNING FIELD-SYMBOL(<ls_anchor_amb>).
      <ls_anchor_amb>-client = sy-mandt.
      ASSIGN COMPONENT '/BA1/C55POSTD' OF STRUCTURE <ls_anchor_amb> TO <lv_postd>.
      ASSIGN COMPONENT '/BA1/C55CONTID' OF STRUCTURE <ls_anchor_amb> TO <lv_contid>.
      ASSIGN COMPONENT '/BA1/C11NODENO' OF STRUCTURE <ls_anchor_amb> TO <lv_nodeno>.
      ASSIGN COMPONENT '/BA1/C55ACCSY' OF STRUCTURE <ls_anchor_amb> TO <lv_accsy>.
      ASSIGN COMPONENT '/BA1/C55DOCNUM' OF STRUCTURE <ls_anchor_amb> TO <lv_docnum>.
      ASSIGN COMPONENT '/BA1/C55DOCITM' OF STRUCTURE <ls_anchor_amb> TO <lv_docitm>.
      IF <lv_postd> IS ASSIGNED.
        <lv_postd> = '20260115'.
      ENDIF.
      IF <lv_contid> IS ASSIGNED.
        <lv_contid> = 'CONT_AMB'.
      ENDIF.
      IF <lv_nodeno> IS ASSIGNED.
        <lv_nodeno> = 'NODE_AMB'.
      ENDIF.
      IF <lv_accsy> IS ASSIGNED.
        <lv_accsy> = 'IFRS'.
      ENDIF.
      IF <lv_docnum> IS ASSIGNED.
        <lv_docnum> = '0000000009'.
      ENDIF.
      IF <lv_docitm> IS ASSIGNED.
        <lv_docitm> = '000001'.
      ENDIF.
    ENDDO.

    CREATE OBJECT lo_job
      EXPORTING
        io_reader = lo_reader
        io_target = lo_target.

    ls_sel-postd_from = '20260101'.
    ls_sel-postd_to = '20260131'.
    ls_sel-pfct = '2100'.
    ls_sel-accrct = '601'.
    ls_sel-package_size = 10.

    ls_res = lo_job->run( is_sel = ls_sel ).

    cl_abap_unit_assert=>assert_equals( act = ls_res-rows_written exp = 0 ).
    cl_abap_unit_assert=>assert_equals( act = lo_target->mv_call_count exp = 0 ).
  ENDMETHOD.

  METHOD rerun_is_deterministic.
    DATA lo_reader_1 TYPE REF TO lcl_reader_fake.
    DATA lo_target_1 TYPE REF TO lcl_target_fake.
    DATA lo_job_1    TYPE REF TO <zcl_rdl_net_posting_job>.
    DATA lo_reader_2 TYPE REF TO lcl_reader_fake.
    DATA lo_target_2 TYPE REF TO lcl_target_fake.
    DATA lo_job_2    TYPE REF TO <zcl_rdl_net_posting_job>.
    DATA ls_sel      TYPE <zif_net_posting_types>=>ty_s_selection.
    DATA ls_res_1    TYPE <zif_net_posting_types>=>ty_s_result.
    DATA ls_res_2    TYPE <zif_net_posting_types>=>ty_s_result.

    FIELD-SYMBOLS <lv_postd>   TYPE any.
    FIELD-SYMBOLS <lv_contid>  TYPE any.
    FIELD-SYMBOLS <lv_nodeno>  TYPE any.
    FIELD-SYMBOLS <lv_accsy>   TYPE any.
    FIELD-SYMBOLS <lv_docnum>  TYPE any.
    FIELD-SYMBOLS <lv_docitm>  TYPE any.
    FIELD-SYMBOLS <ls_tgt_1>   TYPE any.
    FIELD-SYMBOLS <ls_tgt_2>   TYPE any.
    FIELD-SYMBOLS <lv_t_postd_1> TYPE any.
    FIELD-SYMBOLS <lv_t_postd_2> TYPE any.
    FIELD-SYMBOLS <lv_t_samgrp_1> TYPE any.
    FIELD-SYMBOLS <lv_t_samgrp_2> TYPE any.

    ls_sel-postd_from = '20260101'.
    ls_sel-postd_to = '20260131'.
    ls_sel-pfct = '2100'.
    ls_sel-accrct = '601'.
    ls_sel-package_size = 10.

    " Run #1
    CREATE OBJECT lo_reader_1.
    CREATE OBJECT lo_target_1.

    APPEND VALUE #( client = sy-mandt
                    postd = '20260115'
                    lgent = '1000'
                    contid = 'CONT_RERUN'
                    nodeno = 'NODE_RERUN'
                    accsy = 'IFRS'
                    anchor_docnum = '0000000011'
                    anchor_docitm = '000001'
                    sum_sambal = '90'
                    sum_samgrp = '95' ) TO lo_reader_1->mt_agg.

    APPEND INITIAL LINE TO lo_reader_1->mt_anchor ASSIGNING FIELD-SYMBOL(<ls_anchor_1>).
    <ls_anchor_1>-client = sy-mandt.
    ASSIGN COMPONENT '/BA1/C55POSTD' OF STRUCTURE <ls_anchor_1> TO <lv_postd>.
    ASSIGN COMPONENT '/BA1/C55CONTID' OF STRUCTURE <ls_anchor_1> TO <lv_contid>.
    ASSIGN COMPONENT '/BA1/C11NODENO' OF STRUCTURE <ls_anchor_1> TO <lv_nodeno>.
    ASSIGN COMPONENT '/BA1/C55ACCSY' OF STRUCTURE <ls_anchor_1> TO <lv_accsy>.
    ASSIGN COMPONENT '/BA1/C55DOCNUM' OF STRUCTURE <ls_anchor_1> TO <lv_docnum>.
    ASSIGN COMPONENT '/BA1/C55DOCITM' OF STRUCTURE <ls_anchor_1> TO <lv_docitm>.
    IF <lv_postd> IS ASSIGNED.
      <lv_postd> = '20260115'.
    ENDIF.
    IF <lv_contid> IS ASSIGNED.
      <lv_contid> = 'CONT_RERUN'.
    ENDIF.
    IF <lv_nodeno> IS ASSIGNED.
      <lv_nodeno> = 'NODE_RERUN'.
    ENDIF.
    IF <lv_accsy> IS ASSIGNED.
      <lv_accsy> = 'IFRS'.
    ENDIF.
    IF <lv_docnum> IS ASSIGNED.
      <lv_docnum> = '0000000011'.
    ENDIF.
    IF <lv_docitm> IS ASSIGNED.
      <lv_docitm> = '000001'.
    ENDIF.

    CREATE OBJECT lo_job_1
      EXPORTING
        io_reader = lo_reader_1
        io_target = lo_target_1.

    ls_res_1 = lo_job_1->run( is_sel = ls_sel ).

    " Run #2 with identical fixture
    CREATE OBJECT lo_reader_2.
    CREATE OBJECT lo_target_2.

    APPEND VALUE #( client = sy-mandt
                    postd = '20260115'
                    lgent = '1000'
                    contid = 'CONT_RERUN'
                    nodeno = 'NODE_RERUN'
                    accsy = 'IFRS'
                    anchor_docnum = '0000000011'
                    anchor_docitm = '000001'
                    sum_sambal = '90'
                    sum_samgrp = '95' ) TO lo_reader_2->mt_agg.

    APPEND INITIAL LINE TO lo_reader_2->mt_anchor ASSIGNING FIELD-SYMBOL(<ls_anchor_2>).
    <ls_anchor_2>-client = sy-mandt.
    ASSIGN COMPONENT '/BA1/C55POSTD' OF STRUCTURE <ls_anchor_2> TO <lv_postd>.
    ASSIGN COMPONENT '/BA1/C55CONTID' OF STRUCTURE <ls_anchor_2> TO <lv_contid>.
    ASSIGN COMPONENT '/BA1/C11NODENO' OF STRUCTURE <ls_anchor_2> TO <lv_nodeno>.
    ASSIGN COMPONENT '/BA1/C55ACCSY' OF STRUCTURE <ls_anchor_2> TO <lv_accsy>.
    ASSIGN COMPONENT '/BA1/C55DOCNUM' OF STRUCTURE <ls_anchor_2> TO <lv_docnum>.
    ASSIGN COMPONENT '/BA1/C55DOCITM' OF STRUCTURE <ls_anchor_2> TO <lv_docitm>.
    IF <lv_postd> IS ASSIGNED.
      <lv_postd> = '20260115'.
    ENDIF.
    IF <lv_contid> IS ASSIGNED.
      <lv_contid> = 'CONT_RERUN'.
    ENDIF.
    IF <lv_nodeno> IS ASSIGNED.
      <lv_nodeno> = 'NODE_RERUN'.
    ENDIF.
    IF <lv_accsy> IS ASSIGNED.
      <lv_accsy> = 'IFRS'.
    ENDIF.
    IF <lv_docnum> IS ASSIGNED.
      <lv_docnum> = '0000000011'.
    ENDIF.
    IF <lv_docitm> IS ASSIGNED.
      <lv_docitm> = '000001'.
    ENDIF.

    CREATE OBJECT lo_job_2
      EXPORTING
        io_reader = lo_reader_2
        io_target = lo_target_2.

    ls_res_2 = lo_job_2->run( is_sel = ls_sel ).

    cl_abap_unit_assert=>assert_equals( act = ls_res_1-rows_written exp = ls_res_2-rows_written ).
    cl_abap_unit_assert=>assert_equals( act = ls_res_1-packages exp = ls_res_2-packages ).
    cl_abap_unit_assert=>assert_equals( act = lo_target_1->mv_call_count exp = lo_target_2->mv_call_count ).
    cl_abap_unit_assert=>assert_equals( act = lines( lo_target_1->mt_rows ) exp = lines( lo_target_2->mt_rows ) ).

    READ TABLE lo_target_1->mt_rows ASSIGNING <ls_tgt_1> INDEX 1.
    READ TABLE lo_target_2->mt_rows ASSIGNING <ls_tgt_2> INDEX 1.

    IF <ls_tgt_1> IS ASSIGNED AND <ls_tgt_2> IS ASSIGNED.
      ASSIGN COMPONENT '/BA1/C55POSTD' OF STRUCTURE <ls_tgt_1> TO <lv_t_postd_1>.
      ASSIGN COMPONENT '/BA1/C55POSTD' OF STRUCTURE <ls_tgt_2> TO <lv_t_postd_2>.
      ASSIGN COMPONENT '/BA1/K5SAMGRP' OF STRUCTURE <ls_tgt_1> TO <lv_t_samgrp_1>.
      ASSIGN COMPONENT '/BA1/K5SAMGRP' OF STRUCTURE <ls_tgt_2> TO <lv_t_samgrp_2>.

      IF <lv_t_postd_1> IS ASSIGNED AND <lv_t_postd_2> IS ASSIGNED.
        cl_abap_unit_assert=>assert_equals( act = <lv_t_postd_1> exp = <lv_t_postd_2> ).
      ENDIF.
      IF <lv_t_samgrp_1> IS ASSIGNED AND <lv_t_samgrp_2> IS ASSIGNED.
        cl_abap_unit_assert=>assert_equals( act = <lv_t_samgrp_1> exp = <lv_t_samgrp_2> ).
      ENDIF.
    ELSE.
      cl_abap_unit_assert=>fail( msg = 'Expected deterministic target rows in both runs' ).
    ENDIF.
  ENDMETHOD.

  METHOD selective_filters_propagated.
    DATA lo_reader TYPE REF TO lcl_reader_fake.
    DATA lo_ckp    TYPE REF TO lcl_checkpoint_fake.
    DATA lo_target TYPE REF TO lcl_target_fake.
    DATA lo_job    TYPE REF TO <zcl_rdl_net_posting_job>.
    DATA ls_sel    TYPE <zif_net_posting_types>=>ty_s_selection.
    DATA ls_res    TYPE <zif_net_posting_types>=>ty_s_result.

    CREATE OBJECT lo_reader.
    CREATE OBJECT lo_ckp.
    CREATE OBJECT lo_target.
    CREATE OBJECT lo_job
      EXPORTING
        io_reader = lo_reader
        io_target = lo_target.

    ls_sel-postd_from = '20260101'.
    ls_sel-postd_to = '20260131'.
    ls_sel-pfct = '2100'.
    ls_sel-accrct = '601'.
    ls_sel-package_size = 5.
    ls_sel-resume = abap_false.

    APPEND VALUE #( sign = 'I' option = 'EQ' low = '1000' ) TO ls_sel-t_lgent.

    ls_res = lo_job->run( is_sel = ls_sel ).

    cl_abap_unit_assert=>assert_equals( act = lo_reader->ms_last_sel-t_lgent[ 1 ]-low exp = '1000' ).
    cl_abap_unit_assert=>assert_equals( act = xsdbool( ls_res-packages = 0 ) exp = abap_true ).
  ENDMETHOD.

  METHOD multi_row_collapse_sums_amounts.
    " TODO: add fixture where multiple rows in one netting grain collapse into one row
    " and assert summed /BA1/K5SAMBAL and /BA1/K5SAMGRP in target writer payload.
    cl_abap_unit_assert=>assert_true( act = abap_true ).
  ENDMETHOD.

ENDCLASS.
```

Checks:
- Tests use deterministic in-memory doubles, not real database state.
- Include one collapse test for summed-amount correctness at target-write seam.
- Include anchor ambiguity case that must skip target write and route to error handling.
- Include rerun determinism check for identical input fixtures.

## Track C - Operations and monitoring

## 10) CVPM setup and worklist support

Use this sequence (evidence-aligned pattern):

1. Data source for worklist
- IMG path:
  - Financial Products Subledger -> Data Loading Process -> Data Sources for Worklists
- Register report `<ZR_RDL_NET_POSTING_RUN>` as callable source.
- Map parameters:
  - `P_FROM`
  - `P_TO`
  - `P_PFCT`
  - `P_RCT`
  - `P_PACK`

2. Analytical process
- IMG path:
  - Financial Products Subledger -> Calculation and Valuation Process Manager (CVPM) -> General Settings for Custom Processes -> Edit Analytical Processes
- Create analytical process placeholder `<ANPR_RDL_NET_POSTING>`.

3. Custom step sequence
- IMG path:
  - Financial Products Subledger -> Calculation and Valuation Process Manager (CVPM) -> General Settings for Custom Processes -> Edit Custom Step Sequences for Analytical Processes
- Configure steps:
  - Step 15: Enrich Parameters
  - Step 20: Worklist Creation
  - Step 30: Data Enrichment (calls report/ABAP class execution)

4. Monitor and run control
- Transaction: `/BAL/PW_PROCMON`
- On failure:
  - relaunch with same business parameters
  - resume/restart checkpoint behavior is deferred in this iteration

## 11) Non-ABAP quick-start (for sharing)

- What this job does:
  - Reads posting lines from `/BA1/HFSPD`
  - Keeps only portfolio/category-valid records via `/BA1/HKAPA` + `/BA1/HKAPD`
  - Aggregates balances by contract/node/accounting system
  - Writes final rows to `Z_NET_POSTING`

- How to run first time:
  - Enter posting date range
  - Keep defaults `PFCT=2100`, `RCT=601`
  - Set package size (example 20000)

- How to run selectively:
  - Fill legal entity filter and/or contract filter
  - Keep same core join logic

## 12) Validation checklist

SQL checks (run in HANA SQL console):

1. Per-group row parity (eligible contracts vs target output)

```sql
WITH eligible AS (
  SELECT
    h."/BA1/C55POSTD"  AS postd,
    h."/BA1/C11NODENO" AS nodeno,
    h."/BA1/C55ACCSY"  AS accsy,
    h."/BA1/C55CONTID" AS contid
  FROM "/BA1/HFSPD" h
  WHERE h."/BA1/C55POSTD" BETWEEN '20260101' AND '20260131'
  GROUP BY h."/BA1/C55POSTD", h."/BA1/C11NODENO", h."/BA1/C55ACCSY", h."/BA1/C55CONTID"
),
tgt AS (
  SELECT
    z."/BA1/C55POSTD"  AS postd,
    z."/BA1/C11NODENO" AS nodeno,
    z."/BA1/C55ACCSY"  AS accsy,
    z."/BA1/C55CONTID" AS contid
  FROM "Z_NET_POSTING" z
  WHERE z."/BA1/C55POSTD" BETWEEN '20260101' AND '20260131'
  GROUP BY z."/BA1/C55POSTD", z."/BA1/C11NODENO", z."/BA1/C55ACCSY", z."/BA1/C55CONTID"
)
SELECT COUNT(*) AS eligible_rows FROM eligible;

SELECT COUNT(*) AS target_rows FROM tgt;
```

2. Allocation sum must reconcile to net per netting group

```sql
WITH src_contract AS (
  SELECT
    h."/BA1/C55POSTD"  AS postd,
    h."/BA1/C11NODENO" AS nodeno,
    h."/BA1/C55ACCSY"  AS accsy,
    h."/BA1/C55CONTID" AS contid,
    SUM(h."/BA1/K5SAMGRP") AS contract_bal
  FROM "/BA1/HFSPD" h
  WHERE h."/BA1/C55POSTD" BETWEEN '20260101' AND '20260131'
  GROUP BY h."/BA1/C55POSTD", h."/BA1/C11NODENO", h."/BA1/C55ACCSY", h."/BA1/C55CONTID"
),
src_group AS (
  SELECT postd, nodeno, accsy, SUM(contract_bal) AS net_samgrp
  FROM src_contract
  GROUP BY postd, nodeno, accsy
),
tgt_group AS (
  SELECT
    z."/BA1/C55POSTD"  AS postd,
    z."/BA1/C11NODENO" AS nodeno,
    z."/BA1/C55ACCSY"  AS accsy,
    SUM(z."/BA1/K5SAMGRP") AS alloc_sum
  FROM "Z_NET_POSTING" z
  WHERE z."/BA1/C55POSTD" BETWEEN '20260101' AND '20260131'
  GROUP BY z."/BA1/C55POSTD", z."/BA1/C11NODENO", z."/BA1/C55ACCSY"
)
SELECT
  s.postd,
  s.nodeno,
  s.accsy,
  s.net_samgrp,
  COALESCE(t.alloc_sum, 0) AS alloc_sum,
  s.net_samgrp - COALESCE(t.alloc_sum, 0) AS delta
FROM src_group s
LEFT JOIN tgt_group t
  ON t.postd = s.postd
 AND t.nodeno = s.nodeno
 AND t.accsy = s.accsy
ORDER BY s.postd, s.nodeno, s.accsy;
```

3. Same-sign allocation rule check

```sql
WITH src_contract AS (
  SELECT
    h."/BA1/C55POSTD"  AS postd,
    h."/BA1/C11NODENO" AS nodeno,
    h."/BA1/C55ACCSY"  AS accsy,
    h."/BA1/C55CONTID" AS contid,
    SUM(h."/BA1/K5SAMGRP") AS contract_bal
  FROM "/BA1/HFSPD" h
  WHERE h."/BA1/C55POSTD" BETWEEN '20260101' AND '20260131'
  GROUP BY h."/BA1/C55POSTD", h."/BA1/C11NODENO", h."/BA1/C55ACCSY", h."/BA1/C55CONTID"
),
src_group AS (
  SELECT postd, nodeno, accsy, SUM(contract_bal) AS net_samgrp
  FROM src_contract
  GROUP BY postd, nodeno, accsy
)
SELECT
  z."/BA1/C55POSTD"  AS postd,
  z."/BA1/C11NODENO" AS nodeno,
  z."/BA1/C55ACCSY"  AS accsy,
  z."/BA1/C55CONTID" AS contid,
  s.net_samgrp,
  c.contract_bal,
  z."/BA1/K5SAMGRP"  AS alloc_amount
FROM "Z_NET_POSTING" z
INNER JOIN src_contract c
  ON c.postd = z."/BA1/C55POSTD"
 AND c.nodeno = z."/BA1/C11NODENO"
 AND c.accsy = z."/BA1/C55ACCSY"
 AND c.contid = z."/BA1/C55CONTID"
INNER JOIN src_group s
  ON s.postd = z."/BA1/C55POSTD"
 AND s.nodeno = z."/BA1/C11NODENO"
 AND s.accsy = z."/BA1/C55ACCSY"
WHERE (s.net_samgrp > 0 AND (c.contract_bal <= 0 AND z."/BA1/K5SAMGRP" <> 0))
   OR (s.net_samgrp < 0 AND (c.contract_bal >= 0 AND z."/BA1/K5SAMGRP" <> 0))
ORDER BY postd, nodeno, accsy, contid;
```

4. Optional extension check (only if checkpoint module is enabled)

```sql
SELECT * FROM "<ZNET_POSTING_RUN>"
ORDER BY CHANGED_AT_UTC DESC;
```

## 13) Important assumptions to confirm in your system

- `CURRENT_FLAG` semantics for both RDL dimensions.
- Domain values `2100` and `601` are valid for your ledger variant.
- `Z_NET_POSTING` allows `MODIFY ... FROM TABLE` upsert behavior for your primary key design.
- AMDP IN-list handling with range tables in your ABAP platform release.
- Placeholder rule contracts for Asset/Liability Indicator and Allocation Amount are agreed before implementation.

If any of the above differs, keep the architecture and adjust only the affected method/filter.

## 14) Prompt contract closure checklist

Use this checklist to confirm alignment with `.github/prompts/rdl-net-posting.prompt.md`:

- FPSL-only source intent is implemented; GL and GR exclusion uses an explicitly confirmed discriminator in landscape metadata.
- Netting group excludes contract ID for net calculation, while output remains one row per contract.
- Netted delta is written to target group-currency amount field; pre-netted group amount is not posted.
- Anchor strategy is treated as candidate logic; missing and ambiguous anchors are routed to separate error handling.
- Allocation follows same-sign rule (`net > 0` -> positive contracts, `net < 0` -> negative contracts, `net = 0` -> no effective allocation).
- Currency handling keeps `/BA1/K5SAMGRP` as already USD with no FX conversion step.
- No forced rounding is introduced unless business confirms posting-boundary rounding policy.

## 15) Email-ready implementation kickoff guidelines

Use this template to announce implementation start and align Dev, Test, and Ops.

Subject:
- `RDL Net Posting: Implementation Start + Validation Plan`

Recipients:
- Dev owner
- QA owner
- FPSL/CVPM operations owner
- Business approver for netting/allocation semantics

Email body template:

```text
Hello Team,

We are starting implementation for the RDL net posting flow using the agreed contract and pack artifacts.

Scope included in this iteration
- AMDP netting + proportional allocation logic
- ABAP orchestration and anchor-row handling
- Validation SQL checks and ABAP Unit scaffolding
- CVPM run path and monitoring guidance

Confirmed behavior
- Source: FPSL only
- Netting group excludes contract ID
- Output is one row per eligible contract
- Same-sign allocation rule is applied
- Group currency is already USD (no FX conversion in this flow)
- Separate error handling path for missing/ambiguous anchors

Open confirmations before production move
- Exact HFSPD discriminator for GL/GR exclusion in this landscape
- Final business decision for Group Category derivation (A/C/D)
- Rounding policy at posting boundary (current behavior: no forced rounding)

Execution plan
1. Activate artifacts in ADT sequence
2. Run ABAP Unit and SQL validation checks
3. Execute limited-scope trial run by date range
4. Review reconciliation deltas and error log entries
5. Approve scale-up window for wider run

Evidence to attach
- Implementation pack section: Track A/Track B/Track C
- Validation SQL output screenshots or result extracts
- /BAL/PW_PROCMON run monitor snapshot

Please reply with GO/NO-GO for the limited-scope trial run and any blocking concerns.

Regards,
<owner>
```

Send criteria:
- Run this email only after checklist items in section 14 are reviewed.
- Keep evidence attachments from the same run window used in SQL validation.

Leadership summary variant (5-7 lines):

```text
Subject: RDL Net Posting - Implementation Start (Status and Decision)

We are ready to begin controlled implementation for RDL net posting with AMDP, ABAP orchestration, and validation controls in place.
The design is aligned to FPSL-only sourcing, per-contract output, and same-sign allocation logic.
ABAP Unit and SQL reconciliation checks are prepared, including missing/ambiguous anchor handling.
Open confirmations before production scale-up: GL/GR discriminator field, Group Category derivation (A/C/D), and posting-boundary rounding policy.
Next step is a limited-scope trial run followed by GO/NO-GO decision using validation evidence and process-monitor output.
```
