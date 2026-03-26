# RDL Net Posting Implementation Pack

Version: 2.3.0
Date: 2026-03-26
Primary contract: `.github/prompts/rdl-net-posting.prompt.md`

Purpose: deliver one simple, ADT-ready first-pass implementation for RDL net posting using AMDP + ABAP orchestration, with tests inline and optional abstractions deferred.

## 0) First-pass build path (single linear flow)

1. Create DDIC targets (`Z_NET_POSTING`, `Z_NET_POSTING_ERR`)
2. Implement AMDP method (`<ZCL_RDL_NET_POSTING_AMDP>=>READ_AGGREGATES`)
3. Implement one concrete ABAP class (`<ZCL_RDL_NET_POSTING_JOB>`) and its `RUN` method
4. Add ABAP Unit tests inline immediately after the implementation section
5. Create report wrapper (`<ZR_RDL_NET_POSTING_RUN>`)
6. Run validation SQL
7. Move to optional hardening only after core path is stable

## 1) Confirmed requirement baseline

- Source scope: FPSL only
- Driver: `/BA1/HFSPD`
- Validation dimension 1: `/BA1/HKAPA`
  - hard filter `/BA1/CR4PFCT = '2100'`
  - temporal filter latest `/BA1/CR0KEYDAT <= /BA1/C55POSTD`
  - `CURRENT_FLAG = 'X'`
- Validation dimension 2: `/BA1/HKAPD`
  - hard filter `/BA1/C55ACCRCT = '601'`
  - temporal filter latest `/BA1/CR0KEYDAT <= /BA1/C55POSTD`
  - `CURRENT_FLAG = 'X'`
- Netting group excludes contract ID
- One output row per eligible contract
- Net basis: `SUM(/BA1/K5SAMGRP)`
- Same-sign proportional allocation

## 2) GL/GR exclusion status (explicit downgrade)

This release explicitly downgrades GL/GR exclusion to a controlled TODO until the landscape discriminator is confirmed.

Current behavior:
- No active GL/GR discriminator is enforced in AMDP Stage 1.

Required TODO in AMDP:
- `TODO: activate GL/GR exclusion only after confirmed `/BA1/HFSPD` discriminator field/value in landscape metadata.`

## 3) DDIC artifacts

### 3.1 `Z_NET_POSTING`

Create by cloning `/BA1/HFSPD`.

Checks:
- Preserve source key order exactly
- Preserve `/BA1/K5SAMBAL` and `/BA1/K5SAMGRP` technical types

### 3.2 `Z_NET_POSTING_ERR`

```abap
@EndUserText.label: 'Net Posting Error Log'
@AbapCatalog.enhancement.category: #NOT_EXTENSIBLE
@AbapCatalog.tableCategory: #TRANSPARENT
@AbapCatalog.deliveryClass: #A
@AbapCatalog.dataMaintenance: #RESTRICTED
define table z_net_posting_err {
  key mandt      : mandt not null;
  key error_id   : abap.int8 not null;
  postd          : abap.dats;
  contid         : abap.char(20);
  nodeno         : abap.char(12);
  accsy          : abap.char(4);
  error_msg      : abap.char(255);
  created_at     : timestampl;
  created_by     : syuname;
}
```

## 4) AMDP artifact

### 4.1 AMDP class definition

```abap
CLASS <ZCL_RDL_NET_POSTING_AMDP> DEFINITION PUBLIC FINAL CREATE PUBLIC.
  PUBLIC SECTION.
    INTERFACES if_amdp_marker_hdb.

    TYPES: BEGIN OF ty_s_agg,
             client         TYPE mandt,
             postd          TYPE d,
             lgent          TYPE c LENGTH 4,
             contid         TYPE c LENGTH 20,
             nodeno         TYPE c LENGTH 12,
             accsy          TYPE c LENGTH 4,
             anchor_docnum  TYPE c LENGTH 10,
             anchor_docitm  TYPE n LENGTH 6,
             sum_sambal     TYPE decfloat34,
             sum_samgrp     TYPE decfloat34,
             alloc_amount   TYPE decfloat34,
           END OF ty_s_agg,
           ty_t_agg TYPE STANDARD TABLE OF ty_s_agg WITH EMPTY KEY.

    CLASS-METHODS read_aggregates
      IMPORTING VALUE(iv_pfct) TYPE c LENGTH 4
                VALUE(iv_accrct) TYPE c LENGTH 4
                VALUE(iv_package_size) TYPE i
                VALUE(iv_postd_from) TYPE d
                VALUE(iv_postd_to) TYPE d
      EXPORTING VALUE(et_agg) TYPE ty_t_agg.
ENDCLASS.
```

### 4.2 Concrete AMDP implementation (single method)

```abap
CLASS <ZCL_RDL_NET_POSTING_AMDP> IMPLEMENTATION.

  METHOD read_aggregates
    BY DATABASE PROCEDURE
    FOR HDB
    LANGUAGE SQLSCRIPT
    OPTIONS READ-ONLY
    USING /ba1/hfspd /ba1/hkapa /ba1/hkapd.

    -- Stage 1: HFSPD candidates in requested posting-date window.
    -- TODO (intentional downgrade): activate GL/GR exclusion only after confirmed discriminator field/value in landscape metadata.
    lt_hfspd =
      SELECT
        h.mandt              AS client,
        h."/BA1/C55POSTD"    AS postd,
        h."/BA1/C55LGENT"    AS lgent,
        h."/BA1/C55CONTID"   AS contid,
        h."/BA1/C55NODENO"   AS nodeno,
        h."/BA1/C55ACCSY"    AS accsy,
        h."/BA1/C55DOCNUM"   AS anchor_docnum,
        h."/BA1/C55DOCITM"   AS anchor_docitm,
        h."/BA1/K5SAMBAL"    AS sambal,
        h."/BA1/K5SAMGRP"    AS samgrp
      FROM /ba1/hfspd AS h
      WHERE h.mandt = SESSION_CONTEXT('CLIENT')
        AND h."/BA1/C55POSTD" BETWEEN :iv_postd_from AND :iv_postd_to
      LIMIT :iv_package_size;

    -- Stage 2: HKAPA latest valid row per contract for PFCT.
    lt_hkapa_valid =
      SELECT
        a."/BA1/C55CONTID" AS contid,
        MAX( a."/BA1/CR0KEYDAT" ) AS max_keydat
      FROM /ba1/hkapa AS a
      INNER JOIN :lt_hfspd AS h
        ON h.contid = a."/BA1/C55CONTID"
       AND a."/BA1/CR0KEYDAT" <= h.postd
      WHERE a."/BA1/CR4PFCT" = :iv_pfct
        AND a.current_flag = 'X'
      GROUP BY a."/BA1/C55CONTID";

    -- Stage 3: HKAPD latest valid row per contract for ACCRCT.
    lt_hkapd_valid =
      SELECT
        d."/BA1/C55CONTID" AS contid,
        MAX( d."/BA1/CR0KEYDAT" ) AS max_keydat
      FROM /ba1/hkapd AS d
      INNER JOIN :lt_hfspd AS h
        ON h.contid = d."/BA1/C55CONTID"
       AND d."/BA1/CR0KEYDAT" <= h.postd
      WHERE d."/BA1/C55ACCRCT" = :iv_accrct
        AND d.current_flag = 'X'
      GROUP BY d."/BA1/C55CONTID";

    -- Stage 4: keep only contracts valid in both dimensions and aggregate per contract.
    lt_contract =
      SELECT
        h.client,
        h.postd,
        h.lgent,
        h.contid,
        h.nodeno,
        h.accsy,
        MIN( h.anchor_docnum ) AS anchor_docnum,
        MIN( h.anchor_docitm ) AS anchor_docitm,
        SUM( h.sambal ) AS sum_sambal,
        SUM( h.samgrp ) AS sum_samgrp
      FROM :lt_hfspd AS h
      INNER JOIN :lt_hkapa_valid AS ka ON ka.contid = h.contid
      INNER JOIN :lt_hkapd_valid AS kd ON kd.contid = h.contid
      GROUP BY
        h.client,
        h.postd,
        h.lgent,
        h.contid,
        h.nodeno,
        h.accsy;

    -- Stage 5: netting denominator uses same-sign rule within a netting group.
    lt_group =
      SELECT
        c.client,
        c.postd,
        c.lgent,
        c.nodeno,
        c.accsy,
        SUM( c.sum_samgrp ) AS net_amount,
        SUM(
          CASE
            WHEN SIGN( c.sum_samgrp ) = SIGN( SUM( c.sum_samgrp ) OVER (PARTITION BY c.client, c.postd, c.lgent, c.nodeno, c.accsy) )
            THEN ABS( c.sum_samgrp )
            ELSE 0
          END
        ) AS same_sign_denom
      FROM :lt_contract AS c
      GROUP BY c.client, c.postd, c.lgent, c.nodeno, c.accsy;

    -- Stage 6: proportional allocation to one output row per contract.
    -- No forced rounding here; apply rounding only after explicit business confirmation.
    et_agg =
      SELECT
        c.client,
        c.postd,
        c.lgent,
        c.contid,
        c.nodeno,
        c.accsy,
        c.anchor_docnum,
        c.anchor_docitm,
        c.sum_sambal,
        c.sum_samgrp,
        CASE
          WHEN g.same_sign_denom = 0 THEN 0
          WHEN SIGN( c.sum_samgrp ) = SIGN( g.net_amount )
            THEN g.net_amount * ( ABS( c.sum_samgrp ) / g.same_sign_denom )
          ELSE 0
        END AS alloc_amount
      FROM :lt_contract AS c
      INNER JOIN :lt_group AS g
        ON g.client = c.client
       AND g.postd  = c.postd
       AND g.lgent  = c.lgent
       AND g.nodeno = c.nodeno
       AND g.accsy  = c.accsy;

  ENDMETHOD.

ENDCLASS.
```

## 5) First-pass ABAP orchestration (one concrete class)

Default path uses one concrete class first. Do not keep public interfaces or helper classes in this section.

```abap
CLASS <ZCL_RDL_NET_POSTING_JOB> DEFINITION PUBLIC FINAL CREATE PUBLIC.
  PUBLIC SECTION.
    TYPES: BEGIN OF ty_s_sel,
             postd_from   TYPE d,
             postd_to     TYPE d,
             pfct         TYPE c LENGTH 4,
             accrct       TYPE c LENGTH 4,
             package_size TYPE i,
           END OF ty_s_sel,
           BEGIN OF ty_s_result,
             rows_written TYPE i,
             packages     TYPE i,
           END OF ty_s_result.

    METHODS run
      IMPORTING is_sel TYPE ty_s_sel
      RETURNING VALUE(rs_result) TYPE ty_s_result
      RAISING cx_static_check.
ENDCLASS.

CLASS <ZCL_RDL_NET_POSTING_JOB> IMPLEMENTATION.

  METHOD run.
    DATA lt_agg TYPE <zcl_rdl_net_posting_amdp>=>ty_t_agg.
    DATA ls_agg TYPE <zcl_rdl_net_posting_amdp>=>ty_s_agg.

    CLEAR rs_result.

    <zcl_rdl_net_posting_amdp>=>read_aggregates(
      EXPORTING
        iv_pfct         = is_sel-pfct
        iv_accrct       = is_sel-accrct
        iv_package_size = is_sel-package_size
        iv_postd_from   = is_sel-postd_from
        iv_postd_to     = is_sel-postd_to
      IMPORTING
        et_agg          = lt_agg ).

    IF lt_agg IS INITIAL.
      RETURN.
    ENDIF.

    rs_result-packages = 1.

    LOOP AT lt_agg INTO ls_agg.
      DATA lt_anchor_rows TYPE STANDARD TABLE OF /ba1/hfspd WITH EMPTY KEY.

      " Replace <HFSPD_DOCNUM_FIELD>/<HFSPD_DOCITM_FIELD> with confirmed technical names if they differ.
      SELECT *
        FROM /ba1/hfspd
        WHERE mandt                 = @sy-mandt
          AND /ba1/c55docnum        = @ls_agg-anchor_docnum
          AND /ba1/c55docitm        = @ls_agg-anchor_docitm
        INTO TABLE @lt_anchor_rows.

      IF lines( lt_anchor_rows ) = 0.
        INSERT z_net_posting_err FROM VALUE #(
          mandt      = sy-mandt
          error_id   = cl_system_uuid=>create_uuid_x16_static( )
          postd      = ls_agg-postd
          contid     = ls_agg-contid
          nodeno     = ls_agg-nodeno
          accsy      = ls_agg-accsy
          error_msg  = 'ANCHOR_NOT_FOUND'
          created_at = utclong_current( )
          created_by = sy-uname ).
        CONTINUE.
      ENDIF.

      IF lines( lt_anchor_rows ) > 1.
        INSERT z_net_posting_err FROM VALUE #(
          mandt      = sy-mandt
          error_id   = cl_system_uuid=>create_uuid_x16_static( )
          postd      = ls_agg-postd
          contid     = ls_agg-contid
          nodeno     = ls_agg-nodeno
          accsy      = ls_agg-accsy
          error_msg  = 'ANCHOR_AMBIGUOUS'
          created_at = utclong_current( )
          created_by = sy-uname ).
        CONTINUE.
      ENDIF.

      DATA ls_target TYPE z_net_posting.
      MOVE-CORRESPONDING lt_anchor_rows[ 1 ] TO ls_target.

      ls_target-/ba1/k5samgrp = ls_agg-alloc_amount.

      MODIFY z_net_posting FROM @ls_target.
      IF sy-subrc <> 0.
        INSERT z_net_posting_err FROM VALUE #(
          mandt      = sy-mandt
          error_id   = cl_system_uuid=>create_uuid_x16_static( )
          postd      = ls_agg-postd
          contid     = ls_agg-contid
          nodeno     = ls_agg-nodeno
          accsy      = ls_agg-accsy
          error_msg  = 'TARGET_MODIFY_FAILED'
          created_at = utclong_current( )
          created_by = sy-uname ).
        CONTINUE.
      ENDIF.

      rs_result-rows_written = rs_result-rows_written + 1.
    ENDLOOP.
  ENDMETHOD.

ENDCLASS.
```

## 6) ABAP Unit tests (inline, same path)

```abap
CLASS ltc_net_posting_job DEFINITION FINAL FOR TESTING
  DURATION SHORT
  RISK LEVEL HARMLESS.
  PRIVATE SECTION.
    DATA mo_cut TYPE REF TO <zcl_rdl_net_posting_job>.

    METHODS setup.
    METHODS empty_agg_exits_cleanly FOR TESTING.
    METHODS writes_rows_for_one_package FOR TESTING.
    METHODS anchor_mismatch_skips_row FOR TESTING.
    METHODS anchor_ambiguous_skips_row FOR TESTING.
    METHODS rerun_is_deterministic FOR TESTING.
    METHODS multi_row_collapse_sums_amounts FOR TESTING.
ENDCLASS.

CLASS ltc_net_posting_job IMPLEMENTATION.

  METHOD setup.
    CREATE OBJECT mo_cut.
    DELETE FROM z_net_posting.
    DELETE FROM z_net_posting_err.
  ENDMETHOD.

  METHOD empty_agg_exits_cleanly.
    DATA ls_sel TYPE <zcl_rdl_net_posting_job>=>ty_s_sel.
    ls_sel-postd_from = '20990101'.
    ls_sel-postd_to   = '20990101'.
    ls_sel-pfct       = '2100'.
    ls_sel-accrct     = '601'.
    ls_sel-package_size = 100.

    DATA(ls_res) = mo_cut->run( ls_sel ).
    cl_abap_unit_assert=>assert_equals( act = ls_res-rows_written exp = 0 ).
  ENDMETHOD.

  METHOD writes_rows_for_one_package.
    " Prepare one minimal eligible source row set in /BA1/HFSPD + /BA1/HKAPA + /BA1/HKAPD.
    " Then run and verify one target row exists.
    DATA ls_sel TYPE <zcl_rdl_net_posting_job>=>ty_s_sel.
    ls_sel-postd_from = '20260101'.
    ls_sel-postd_to   = '20260131'.
    ls_sel-pfct       = '2100'.
    ls_sel-accrct     = '601'.
    ls_sel-package_size = 1000.

    DATA(ls_res) = mo_cut->run( ls_sel ).
    cl_abap_unit_assert=>assert_true( act = xsdbool( ls_res-rows_written >= 1 ) ).
  ENDMETHOD.

  METHOD anchor_mismatch_skips_row.
    DATA ls_sel TYPE <zcl_rdl_net_posting_job>=>ty_s_sel.
    ls_sel-postd_from = '20260101'.
    ls_sel-postd_to   = '20260131'.
    ls_sel-pfct       = '2100'.
    ls_sel-accrct     = '601'.
    ls_sel-package_size = 1000.

    mo_cut->run( ls_sel ).

    SELECT COUNT( * ) FROM z_net_posting_err WHERE error_msg = 'ANCHOR_NOT_FOUND' INTO @DATA(lv_cnt).
    cl_abap_unit_assert=>assert_true( act = xsdbool( lv_cnt >= 1 ) ).
  ENDMETHOD.

  METHOD anchor_ambiguous_skips_row.
    DATA ls_sel TYPE <zcl_rdl_net_posting_job>=>ty_s_sel.
    ls_sel-postd_from = '20260101'.
    ls_sel-postd_to   = '20260131'.
    ls_sel-pfct       = '2100'.
    ls_sel-accrct     = '601'.
    ls_sel-package_size = 1000.

    mo_cut->run( ls_sel ).

    SELECT COUNT( * ) FROM z_net_posting_err WHERE error_msg = 'ANCHOR_AMBIGUOUS' INTO @DATA(lv_cnt).
    cl_abap_unit_assert=>assert_true( act = xsdbool( lv_cnt >= 1 ) ).
  ENDMETHOD.

  METHOD rerun_is_deterministic.
    DATA ls_sel TYPE <zcl_rdl_net_posting_job>=>ty_s_sel.
    ls_sel-postd_from = '20260101'.
    ls_sel-postd_to   = '20260131'.
    ls_sel-pfct       = '2100'.
    ls_sel-accrct     = '601'.
    ls_sel-package_size = 1000.

    DATA(ls_res_1) = mo_cut->run( ls_sel ).
    DATA(ls_res_2) = mo_cut->run( ls_sel ).

    cl_abap_unit_assert=>assert_equals( act = ls_res_1-rows_written exp = ls_res_2-rows_written ).
  ENDMETHOD.

  METHOD multi_row_collapse_sums_amounts.
    DATA ls_sel TYPE <zcl_rdl_net_posting_job>=>ty_s_sel.
    ls_sel-postd_from = '20260101'.
    ls_sel-postd_to   = '20260131'.
    ls_sel-pfct       = '2100'.
    ls_sel-accrct     = '601'.
    ls_sel-package_size = 1000.

    mo_cut->run( ls_sel ).

    SELECT SUM( /ba1/k5samgrp ) FROM z_net_posting INTO @DATA(lv_sum_target).
    cl_abap_unit_assert=>assert_not_initial( act = lv_sum_target ).
  ENDMETHOD.

ENDCLASS.
```

## 7) Report wrapper

```abap
REPORT <ZR_RDL_NET_POSTING_RUN>.

PARAMETERS: p_from TYPE d OBLIGATORY,
            p_to   TYPE d OBLIGATORY,
            p_pfct TYPE c LENGTH 4 DEFAULT '2100',
            p_rct  TYPE c LENGTH 4 DEFAULT '601',
            p_pack TYPE i DEFAULT 20000.

START-OF-SELECTION.
  DATA lo_job TYPE REF TO <zcl_rdl_net_posting_job>.
  DATA ls_sel TYPE <zcl_rdl_net_posting_job>=>ty_s_sel.
  DATA ls_res TYPE <zcl_rdl_net_posting_job>=>ty_s_result.

  ls_sel-postd_from   = p_from.
  ls_sel-postd_to     = p_to.
  ls_sel-pfct         = p_pfct.
  ls_sel-accrct       = p_rct.
  ls_sel-package_size = p_pack.

  CREATE OBJECT lo_job.
  ls_res = lo_job->run( is_sel = ls_sel ).

  WRITE: / 'Rows written:', ls_res-rows_written,
         / 'Packages:', ls_res-packages.
```

## 8) Validation SQL

Run three checks:
1. eligible contracts vs target row parity
2. net reconciliation per netting group
3. same-sign rule violations

## 9) Optional hardening (trailing section)

Only after core path works:
- public interfaces (`<ZIF_NET_POSTING_*>`) for alternate providers/mocks
- helper classes (`lcl_*`) if decomposition is needed
- checkpoint table (`<ZNET_POSTING_RUN>`) and restart cursor
- restart/re-drive scaffolding from error table
- advanced CVPM run control extensions

## 10) Implementation checklist

- [ ] `Z_NET_POSTING` activated
- [ ] `Z_NET_POSTING_ERR` activated
- [ ] AMDP active and tested
- [ ] one concrete ABAP class active and executing
- [ ] inline ABAP Unit tests pass
- [ ] report executes on limited scope
- [ ] SQL validation checks pass
- [ ] GL/GR filter remains downgraded until discriminator is confirmed
