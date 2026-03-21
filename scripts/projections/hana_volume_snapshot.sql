-- ============================================================
-- HANA Volume Snapshot Query
-- Purpose : Collect table-level volume and DB-size metrics
--           for FPSL / FSDM growth tracking
-- Frequency: Run every 7 days (or monthly at minimum)
-- Paste results into: volume-snapshots.csv (append each run)
-- ============================================================

-- -------------------------------------------------------
-- SECTION 1 — Per-Table Snapshot (Column Store)
-- Run in HANA Studio / HANA Cockpit / any SQL client
-- Replace the IN list with your actual schema names
-- -------------------------------------------------------

SELECT
    TO_VARCHAR(CURRENT_DATE, 'YYYY-MM-DD')              AS SNAPSHOT_DATE,
    SCHEMA_NAME,
    TABLE_NAME,
    RECORD_COUNT,
    ROUND(MEMORY_SIZE_IN_TOTAL          / 1048576.0, 2) AS MEMORY_SIZE_MB,
    ROUND(DISK_SIZE                     / 1048576.0, 2) AS DISK_SIZE_MB,
    ROUND(DELTA_MEMORY_SIZE_IN_TOTAL    / 1048576.0, 2) AS DELTA_MEMORY_MB,
    ROUND(
        (MEMORY_SIZE_IN_TOTAL + DELTA_MEMORY_SIZE_IN_TOTAL) / 1048576.0,
    2)                                                  AS TOTAL_MEMORY_MB,
    IS_COLUMN_TABLE,
    LOAD_UNIT
FROM
    SYS.M_CS_TABLES
WHERE
    SCHEMA_NAME IN (
        'FPSL_SCHEMA',   -- replace with actual FPSL schema
        'FSDM_SCHEMA'    -- replace with actual FSDM schema
    )
    -- Uncomment to filter for top-N by size:
    -- AND MEMORY_SIZE_IN_TOTAL > 1048576          -- tables > 1 MB only
ORDER BY
    MEMORY_SIZE_IN_TOTAL DESC;


-- -------------------------------------------------------
-- SECTION 2 — Row Store Tables (if any FPSL/FSDM tables
--             live in row store; usually none but check)
-- -------------------------------------------------------

SELECT
    TO_VARCHAR(CURRENT_DATE, 'YYYY-MM-DD')              AS SNAPSHOT_DATE,
    SCHEMA_NAME,
    TABLE_NAME,
    RECORD_COUNT,
    ROUND(ALLOCATED_FIXED_PART_SIZE     / 1048576.0, 2) AS ALLOCATED_FIXED_MB,
    ROUND(ALLOCATED_VARIABLE_PART_SIZE  / 1048576.0, 2) AS ALLOCATED_VAR_MB,
    ROUND(
        (ALLOCATED_FIXED_PART_SIZE + ALLOCATED_VARIABLE_PART_SIZE) / 1048576.0,
    2)                                                  AS TOTAL_ALLOCATED_MB
FROM
    SYS.M_RS_TABLES
WHERE
    SCHEMA_NAME IN (
        'FPSL_SCHEMA',
        'FSDM_SCHEMA'
    )
ORDER BY
    TOTAL_ALLOCATED_MB DESC;


-- -------------------------------------------------------
-- SECTION 3 — Database-Level Disk Usage Snapshot
-- Shows overall DATA / LOG / TRACE disk consumption
-- -------------------------------------------------------

SELECT
    TO_VARCHAR(CURRENT_DATE, 'YYYY-MM-DD')              AS SNAPSHOT_DATE,
    HOST,
    VOLUME_TYPE,
    ROUND(USED_SIZE  / 1073741824.0, 3)                 AS USED_GB,
    ROUND(TOTAL_SIZE / 1073741824.0, 3)                 AS TOTAL_GB,
    ROUND(USED_SIZE * 100.0 / NULLIF(TOTAL_SIZE, 0), 2) AS UTILIZATION_PCT
FROM
    SYS.M_DISK_USAGE
ORDER BY
    VOLUME_TYPE,
    HOST;


-- -------------------------------------------------------
-- SECTION 4 — OPTIONAL: Top 20 heaviest tables (any schema)
-- Useful for an ad-hoc size audit run
-- -------------------------------------------------------

SELECT TOP 20
    TO_VARCHAR(CURRENT_DATE, 'YYYY-MM-DD')              AS SNAPSHOT_DATE,
    SCHEMA_NAME,
    TABLE_NAME,
    RECORD_COUNT,
    ROUND(MEMORY_SIZE_IN_TOTAL / 1048576.0, 2)          AS MEMORY_SIZE_MB,
    ROUND(DISK_SIZE            / 1048576.0, 2)          AS DISK_SIZE_MB
FROM
    SYS.M_CS_TABLES
ORDER BY
    MEMORY_SIZE_IN_TOTAL DESC;
