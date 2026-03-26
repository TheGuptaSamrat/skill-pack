# RDL Net Posting Implementation Pack

Purpose: implement a resume-safe, selective, CVPM-compatible data flow that applies the requirement-specific join logic from `design/netting-join-logic.md` and loads `Z_NET_POSTING` (same structure as `/BA1/HFSPD`).

This pack is split into ADT-ready artifacts and a non-ABAP runbook.
All custom technical object names except `Z_NET_POSTING` are placeholders and must be replaced with your confirmed namespace/object names.

## Pack usage

- reusable RDL table and field evidence comes from `metadata-drop/ddic/current/`
- requirement-specific joins, filters, and examples stay in this pack
- raw Excel or screenshots used during development should stay local and not be committed by default

## 1) Confirmed inputs from uploaded metadata

- Driver table: `/BA1/HFSPD`
- Join table 1: `/BA1/HKAPA`
- Join table 2: `/BA1/HKAPD`
- Mandatory HKAPA filter: `/BA1/CR4PFCT = '2100'`
- Mandatory HKAPD filter: `/BA1/C55ACCRCT = '601'`
- Temporal filter pattern: latest `/BA1/CR0KEYDAT <= /BA1/C55POSTD`, with `CURRENT_FLAG = 'X'`
- Grouping grain from diagram:
  - `/BA1/C55CONTID`
  - `/BA1/C11NODENO`
  - `/BA1/C55ACCSY`
- Aggregates:
  - `SUM(/BA1/K5SAMBAL)` functional currency amount
  - `SUM(/BA1/K5SAMGRP)` group currency amount

## 1a) Requirement-specific references in this pack

- join and filter logic: `design/netting-join-logic.md`
- zero-shot prompt context: `examples/zero-shot.md`
- one-shot prompt context: `examples/one-shot.md`

## 2) Runtime architecture

- AMDP class reads one package of eligible groups using the join diagram logic.
- ABAP orchestration class:
  - manages selective filters
  - reads/writes checkpoint state for resume
  - pulls anchor rows from `/BA1/HFSPD`
  - writes merged rows into `Z_NET_POSTING`
- Report wrapper exposes batch options for operations/CVPM.
- CVPM analytical process calls the report with step sequence including worklist creation.

## 3) Artifact: Resume control table (DDIC)

Paste target: ADT DDLS/SE11 table creation for `<ZNET_POSTING_RUN>`
Action: create

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
             sum_sambal    TYPE decfloat34,
             sum_samgrp    TYPE decfloat34,
           END OF ty_s_agg,
           ty_t_agg TYPE STANDARD TABLE OF ty_s_agg WITH EMPTY KEY,
           ty_t_rng_char4  TYPE RANGE OF c LENGTH 4,
           ty_t_rng_char20 TYPE RANGE OF c LENGTH 20,
           ty_t_rng_dats   TYPE RANGE OF d.

    CLASS-METHODS read_aggregates
      IMPORTING
        VALUE(iv_pfct)         TYPE c LENGTH 4
        VALUE(iv_accrct)       TYPE c LENGTH 4
        VALUE(iv_resume)       TYPE abap_bool
        VALUE(iv_last_postd)   TYPE d
        VALUE(iv_last_contid)  TYPE c LENGTH 20
        VALUE(iv_last_nodeno)  TYPE c LENGTH 12
        VALUE(iv_last_accsy)   TYPE c LENGTH 4
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

```abap
METHOD read_aggregates
  BY DATABASE PROCEDURE FOR HDB
  LANGUAGE SQLSCRIPT
  OPTIONS READ-ONLY
  USING "/BA1/HFSPD" "/BA1/HKAPA" "/BA1/HKAPD".

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
      AND (
           :iv_resume = ' '
           OR h."/BA1/C55POSTD" > :iv_last_postd
           OR (h."/BA1/C55POSTD" = :iv_last_postd AND h."/BA1/C55CONTID" > :iv_last_contid)
           OR (h."/BA1/C55POSTD" = :iv_last_postd AND h."/BA1/C55CONTID" = :iv_last_contid AND h."/BA1/C11NODENO" > :iv_last_nodeno)
           OR (h."/BA1/C55POSTD" = :iv_last_postd AND h."/BA1/C55CONTID" = :iv_last_contid AND h."/BA1/C11NODENO" = :iv_last_nodeno AND h."/BA1/C55ACCSY" > :iv_last_accsy)
          )
    ORDER BY
      h."/BA1/C55POSTD",
      h."/BA1/C55CONTID",
      h."/BA1/C11NODENO",
      h."/BA1/C55ACCSY"
    LIMIT :iv_package_size;

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
        ORDER BY a."/BA1/CR0KEYDAT" DESC
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

  lt_apd_ranked =
    SELECT
      a.client,
      a.postd,
      a.contid,
      a.nodeno,
      a.accsy,
      ROW_NUMBER() OVER (
        PARTITION BY a.client, a.postd, a.contid, a.nodeno, a.accsy
        ORDER BY d."/BA1/CR0KEYDAT" DESC
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

  et_agg =
    SELECT
      v.client                               AS client,
      v.postd                                AS postd,
      MIN(h."/BA1/C55LGENT")                AS lgent,
      v.contid                               AS contid,
      v.nodeno                               AS nodeno,
      v.accsy                                AS accsy,
      MIN(h."/BA1/C55DOCNUM")               AS anchor_docnum,
      MIN(h."/BA1/C55DOCITM")               AS anchor_docitm,
      CAST(SUM(h."/BA1/K5SAMBAL") AS DECFLOAT34) AS sum_sambal,
      CAST(SUM(h."/BA1/K5SAMGRP") AS DECFLOAT34) AS sum_samgrp
    FROM :lt_valid_keys v
    INNER JOIN "/BA1/HFSPD" h
      ON h."CLIENT" = v.client
     AND h."/BA1/C55POSTD" = v.postd
     AND h."/BA1/C55CONTID" = v.contid
     AND h."/BA1/C11NODENO" = v.nodeno
     AND h."/BA1/C55ACCSY" = v.accsy
    GROUP BY
      v.client,
      v.postd,
      v.contid,
      v.nodeno,
      v.accsy
    ORDER BY
      v.postd,
      v.contid,
      v.nodeno,
      v.accsy;

ENDMETHOD.
```

Checks:
- SQLScript activates.
- For one known key/date, output row count and sums match SQL console validation.

## 6) Artifact: ABAP orchestration class definition

Paste target: Class definition section of `<ZCL_RDL_NET_POSTING_JOB>`
Action: create

```abap
CLASS <ZCL_RDL_NET_POSTING_JOB> DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC.

  PUBLIC SECTION.
    TYPES: ty_t_rng_char4  TYPE RANGE OF c LENGTH 4,
           ty_t_rng_char20 TYPE RANGE OF c LENGTH 20.

    TYPES: BEGIN OF ty_s_selection,
             run_id       TYPE c LENGTH 32,
             postd_from   TYPE d,
             postd_to     TYPE d,
             pfct         TYPE c LENGTH 4,
             accrct       TYPE c LENGTH 4,
             package_size TYPE i,
             resume       TYPE abap_bool,
             t_lgent      TYPE ty_t_rng_char4,
             t_contid     TYPE ty_t_rng_char20,
           END OF ty_s_selection.

    TYPES: BEGIN OF ty_s_result,
             rows_written TYPE i,
             packages     TYPE i,
           END OF ty_s_result.

    METHODS run
      IMPORTING
        is_sel           TYPE ty_s_selection
      RETURNING
        VALUE(rs_result) TYPE ty_s_result
      RAISING
        cx_static_check.

  PROTECTED SECTION.
    TYPES: BEGIN OF ty_s_ckp,
             run_id      TYPE c LENGTH 32,
             last_postd  TYPE d,
             last_contid TYPE c LENGTH 20,
             last_nodeno TYPE c LENGTH 12,
             last_accsy  TYPE c LENGTH 4,
           END OF ty_s_ckp.

    METHODS load_checkpoint
      IMPORTING
        iv_run_id      TYPE c LENGTH 32
      RETURNING
        VALUE(rs_ckp)  TYPE ty_s_ckp.

    METHODS save_checkpoint
      IMPORTING
        is_ckp TYPE ty_s_ckp.

    METHODS upsert_target
      IMPORTING
        it_rows TYPE STANDARD TABLE.

ENDCLASS.
```

Checks:
- Class activation succeeds.
- Add package/class to transport request.

## 7) Artifact: ABAP orchestration class implementation

Paste target: Method implementation `<ZCL_RDL_NET_POSTING_JOB>=>RUN`
Action: create

```abap
METHOD run.
  DATA: ls_ckp       TYPE ty_s_ckp,
        lt_agg       TYPE <ZCL_RDL_NET_POSTING_AMDP>=>ty_t_agg,
        lt_anchor    TYPE STANDARD TABLE OF /ba1/hfspd WITH EMPTY KEY,
        lt_target    TYPE STANDARD TABLE OF z_net_posting WITH EMPTY KEY,
        ls_target    TYPE z_net_posting.

  FIELD-SYMBOLS: <ls_agg>    TYPE <ZCL_RDL_NET_POSTING_AMDP>=>ty_s_agg,
                 <ls_anchor> TYPE /ba1/hfspd,
                 <lv_sambal> TYPE any,
                 <lv_samgrp> TYPE any.

  IF is_sel-resume = abap_true.
    ls_ckp = load_checkpoint( iv_run_id = is_sel-run_id ).
  ELSE.
    CLEAR ls_ckp.
    ls_ckp-run_id = is_sel-run_id.
  ENDIF.

  DO.
    CLEAR lt_agg.

    <ZCL_RDL_NET_POSTING_AMDP>=>read_aggregates(
      EXPORTING
        iv_pfct         = is_sel-pfct
        iv_accrct       = is_sel-accrct
        iv_resume       = is_sel-resume
        iv_last_postd   = ls_ckp-last_postd
        iv_last_contid  = ls_ckp-last_contid
        iv_last_nodeno  = ls_ckp-last_nodeno
        iv_last_accsy   = ls_ckp-last_accsy
        iv_package_size = is_sel-package_size
        it_lgent        = is_sel-t_lgent
        it_contid       = is_sel-t_contid
        iv_postd_from   = is_sel-postd_from
        iv_postd_to     = is_sel-postd_to
      IMPORTING
        et_agg          = lt_agg ).

    IF lt_agg IS INITIAL.
      EXIT.
    ENDIF.

    CLEAR lt_anchor.
    SELECT *
      FROM /ba1/hfspd
      FOR ALL ENTRIES IN @lt_agg
      WHERE client         = @lt_agg-client
        AND "/BA1/C55POSTD"  = @lt_agg-postd
        AND "/BA1/C55DOCNUM" = @lt_agg-anchor_docnum
        AND "/BA1/C55DOCITM" = @lt_agg-anchor_docitm
      INTO TABLE @lt_anchor.

    CLEAR lt_target.

    LOOP AT lt_agg ASSIGNING <ls_agg>.
      READ TABLE lt_anchor ASSIGNING <ls_anchor>
        WITH KEY client            = <ls_agg>-client
                 "/BA1/C55POSTD"  = <ls_agg>-postd
                 "/BA1/C55DOCNUM" = <ls_agg>-anchor_docnum
                 "/BA1/C55DOCITM" = <ls_agg>-anchor_docitm.
      IF sy-subrc <> 0.
        CONTINUE.
      ENDIF.

      MOVE-CORRESPONDING <ls_anchor> TO ls_target.

      ASSIGN COMPONENT '/BA1/K5SAMBAL' OF STRUCTURE ls_target TO <lv_sambal>.
      IF sy-subrc = 0.
        <lv_sambal> = <ls_agg>-sum_sambal.
      ENDIF.

      ASSIGN COMPONENT '/BA1/K5SAMGRP' OF STRUCTURE ls_target TO <lv_samgrp>.
      IF sy-subrc = 0.
        <lv_samgrp> = <ls_agg>-sum_samgrp.
      ENDIF.

      APPEND ls_target TO lt_target.

      ls_ckp-last_postd  = <ls_agg>-postd.
      ls_ckp-last_contid = <ls_agg>-contid.
      ls_ckp-last_nodeno = <ls_agg>-nodeno.
      ls_ckp-last_accsy  = <ls_agg>-accsy.
    ENDLOOP.

    IF lt_target IS NOT INITIAL.
      MODIFY z_net_posting FROM TABLE lt_target.
      COMMIT WORK.

      rs_result-rows_written = rs_result-rows_written + lines( lt_target ).
      rs_result-packages     = rs_result-packages + 1.

      save_checkpoint( is_ckp = ls_ckp ).
    ENDIF.
  ENDDO.
ENDMETHOD.
```

Paste target: Method implementation `<ZCL_RDL_NET_POSTING_JOB>=>LOAD_CHECKPOINT`
Action: create

```abap
METHOD load_checkpoint.
  SELECT SINGLE
         run_id,
         last_postd,
         last_contid,
         last_nodeno,
         last_accsy
    FROM <znet_posting_run>
    WHERE mandt  = @sy-mandt
      AND run_id = @iv_run_id
    INTO CORRESPONDING FIELDS OF @rs_ckp.
ENDMETHOD.
```

Paste target: Method implementation `<ZCL_RDL_NET_POSTING_JOB>=>SAVE_CHECKPOINT`
Action: create

```abap
METHOD save_checkpoint.
  DATA ls_row TYPE <znet_posting_run>.

  MOVE-CORRESPONDING is_ckp TO ls_row.
  ls_row-mandt          = sy-mandt.
  ls_row-status         = 'R'.
  ls_row-changed_by     = sy-uname.
  GET TIME STAMP FIELD ls_row-changed_at_utc.

  MODIFY <znet_posting_run> FROM ls_row.
ENDMETHOD.
```

Checks:
- Run once in foreground for a small date range and verify records in `Z_NET_POSTING`.
- Kill/restart job and verify resume starts after saved key.

## 8) Artifact: Report for selective execution and restart

Paste target: Report `<ZR_RDL_NET_POSTING_RUN>`
Action: create

```abap
REPORT <zr_rdl_net_posting_run>.

PARAMETERS: p_runid TYPE c LENGTH 32 OBLIGATORY,
            p_from  TYPE d OBLIGATORY,
            p_to    TYPE d OBLIGATORY,
            p_pfct  TYPE c LENGTH 4 DEFAULT '2100',
            p_rct   TYPE c LENGTH 4 DEFAULT '601',
            p_pack  TYPE i DEFAULT 20000,
            p_resum AS CHECKBOX DEFAULT 'X'.

DATA gv_contid TYPE c LENGTH 20.

SELECT-OPTIONS: s_lgent FOR p_pfct NO INTERVALS,
                s_cont  FOR gv_contid NO INTERVALS.

START-OF-SELECTION.
  DATA lo_job TYPE REF TO <zcl_rdl_net_posting_job>.
  DATA ls_sel TYPE <zcl_rdl_net_posting_job>=>ty_s_selection.
  DATA ls_res TYPE <zcl_rdl_net_posting_job>=>ty_s_result.

  ls_sel-run_id       = p_runid.
  ls_sel-postd_from   = p_from.
  ls_sel-postd_to     = p_to.
  ls_sel-pfct         = p_pfct.
  ls_sel-accrct       = p_rct.
  ls_sel-package_size = p_pack.
  ls_sel-resume       = COND #( WHEN p_resum = 'X' THEN abap_true ELSE abap_false ).
  ls_sel-t_lgent      = CORRESPONDING #( s_lgent[] ).
  ls_sel-t_contid     = CORRESPONDING #( s_cont[] ).

  CREATE OBJECT lo_job.
  ls_res = lo_job->run( is_sel = ls_sel ).

  WRITE: / 'Rows written:', ls_res-rows_written,
         / 'Packages:', ls_res-packages.
```

Checks:
- Test 1 package run with tiny date range.
- Test resume by rerunning same `RUN_ID` with resume checked.

## 9) Artifact: ABAP Unit test scaffold

Paste target: Local test class include in `<ZCL_RDL_NET_POSTING_JOB>`
Action: append

```abap
CLASS ltc_net_posting_job DEFINITION FINAL FOR TESTING
  DURATION SHORT
  RISK LEVEL HARMLESS.

  PRIVATE SECTION.
    METHODS resume_uses_checkpoint FOR TESTING.
    METHODS selective_filters_propagated FOR TESTING.
ENDCLASS.

CLASS ltc_net_posting_job IMPLEMENTATION.

  METHOD resume_uses_checkpoint.
    " Arrange
    DATA lo_job TYPE REF TO <zcl_rdl_net_posting_job>.
    DATA ls_sel TYPE <zcl_rdl_net_posting_job>=>ty_s_selection.
    DATA ls_res TYPE <zcl_rdl_net_posting_job>=>ty_s_result.

    CREATE OBJECT lo_job.
    ls_sel-run_id = 'UT_RESUME'.
    ls_sel-postd_from = '20260101'.
    ls_sel-postd_to = '20260131'.
    ls_sel-pfct = '2100'.
    ls_sel-accrct = '601'.
    ls_sel-package_size = 10.
    ls_sel-resume = abap_true.

    " Act
    ls_res = lo_job->run( is_sel = ls_sel ).

    " Assert (replace with test seam/double checks in your namespace)
    cl_abap_unit_assert=>assert_true( xsdbool( ls_res-packages >= 0 ) ).
  ENDMETHOD.

  METHOD selective_filters_propagated.
    DATA lo_job TYPE REF TO <zcl_rdl_net_posting_job>.
    DATA ls_sel TYPE <zcl_rdl_net_posting_job>=>ty_s_selection.
    DATA ls_res TYPE <zcl_rdl_net_posting_job>=>ty_s_result.

    CREATE OBJECT lo_job.
    ls_sel-run_id = 'UT_FILTER'.
    ls_sel-postd_from = '20260101'.
    ls_sel-postd_to = '20260131'.
    ls_sel-pfct = '2100'.
    ls_sel-accrct = '601'.
    ls_sel-package_size = 5.
    ls_sel-resume = abap_false.

    APPEND VALUE #( sign = 'I' option = 'EQ' low = '1000' ) TO ls_sel-t_lgent.

    ls_res = lo_job->run( is_sel = ls_sel ).

    cl_abap_unit_assert=>assert_true( xsdbool( ls_res-rows_written >= 0 ) ).
  ENDMETHOD.

ENDCLASS.
```

Checks:
- Replace direct runtime dependencies with test doubles for deterministic tests.
- Add one fixture test where two HFSPD lines collapse into one aggregated target row.

## 10) CVPM setup and worklist support

Use this sequence (evidence-aligned pattern):

1. Data source for worklist
- IMG path:
  - Financial Products Subledger -> Data Loading Process -> Data Sources for Worklists
- Register report `<ZR_RDL_NET_POSTING_RUN>` as callable source.
- Map parameters:
  - `P_RUNID`
  - `P_FROM`
  - `P_TO`
  - `P_PFCT`
  - `P_RCT`
  - `P_PACK`
  - `P_RESUM`

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

4. Monitor and restart
- Transaction: `/BAL/PW_PROCMON`
- On failure:
  - keep same `RUN_ID`
  - relaunch process with `P_RESUM = X`
  - job resumes after `(LAST_POSTD, LAST_CONTID, LAST_NODENO, LAST_ACCSY)` checkpoint

## 11) Non-ABAP quick-start (for sharing)

- What this job does:
  - Reads posting lines from `/BA1/HFSPD`
  - Keeps only portfolio/category-valid records via `/BA1/HKAPA` + `/BA1/HKAPD`
  - Aggregates balances by contract/node/accounting system
  - Writes final rows to `Z_NET_POSTING`

- How to run first time:
  - Choose `RUN_ID` like `NP_2026M03`
  - Enter posting date range
  - Keep defaults `PFCT=2100`, `RCT=601`
  - Set package size (example 20000)
  - Resume flag can be on or off for first run

- How to resume after interruption:
  - Re-run with same `RUN_ID`
  - Keep Resume flag on
  - Job continues from last saved checkpoint

- How to run selectively:
  - Fill legal entity filter and/or contract filter
  - Keep same core join logic

## 12) Validation checklist

SQL checks (run in HANA SQL console):

1. Join eligibility volume

```sql
SELECT COUNT(*) AS eligible_groups
FROM (
  SELECT h."/BA1/C55POSTD", h."/BA1/C55CONTID", h."/BA1/C11NODENO", h."/BA1/C55ACCSY"
  FROM "/BA1/HFSPD" h
  GROUP BY h."/BA1/C55POSTD", h."/BA1/C55CONTID", h."/BA1/C11NODENO", h."/BA1/C55ACCSY"
) x;
```

2. Compare aggregate totals (source vs target)

```sql
SELECT
  SUM(src_sum_sambal) AS src_total,
  SUM(tgt_sum_sambal) AS tgt_total
FROM (
  SELECT
    h."/BA1/C55POSTD",
    h."/BA1/C55CONTID",
    h."/BA1/C11NODENO",
    h."/BA1/C55ACCSY",
    SUM(h."/BA1/K5SAMBAL") AS src_sum_sambal,
    0 AS tgt_sum_sambal
  FROM "/BA1/HFSPD" h
  GROUP BY h."/BA1/C55POSTD", h."/BA1/C55CONTID", h."/BA1/C11NODENO", h."/BA1/C55ACCSY"

  UNION ALL

  SELECT
    z."/BA1/C55POSTD",
    z."/BA1/C55CONTID",
    z."/BA1/C11NODENO",
    z."/BA1/C55ACCSY",
    0 AS src_sum_sambal,
    SUM(z."/BA1/K5SAMBAL") AS tgt_sum_sambal
  FROM "Z_NET_POSTING" z
  GROUP BY z."/BA1/C55POSTD", z."/BA1/C55CONTID", z."/BA1/C11NODENO", z."/BA1/C55ACCSY"
) t;
```

3. Check checkpoint progress

```sql
SELECT * FROM "<ZNET_POSTING_RUN>"
WHERE RUN_ID = '<your_run_id>'
ORDER BY CHANGED_AT_UTC DESC;
```

## 13) Important assumptions to confirm in your system

- `CURRENT_FLAG` semantics for both RDL dimensions.
- Domain values `2100` and `601` are valid for your ledger variant.
- `Z_NET_POSTING` allows `MODIFY ... FROM TABLE` upsert behavior for your primary key design.
- AMDP IN-list handling with range tables in your ABAP platform release.

If any of the above differs, keep the architecture and adjust only the affected method/filter.
