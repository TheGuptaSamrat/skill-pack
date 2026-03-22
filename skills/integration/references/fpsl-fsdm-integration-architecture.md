# FPSL FSDM Integration Architecture

This reference summarizes the standard FSDM-to-FPSL data-loading seam from the repo's official SAP material.

## Core Roles

- FSDM acts as the provisioning and harmonization layer.
- FPSL acts as the consuming accounting and valuation layer.
- The Data Loading (DL) process is the controlled bridge between them.

## Standard DL Flow

1. Change pointer generation identifies new or modified source objects.
2. Extraction retrieves those objects through `/FSDL/EXTRACT`-family interfaces.
3. Transformation applies consumption-layer logic and mapping views.
4. Loading persists data into FPSL target structures for downstream accounting and valuation.

## Important Integration Assets

- `/FSDL/EXTRACT` function group for extraction framing
- `/FSDL/MV_*` consumption and mapping views for transformation
- `/FSDL/MAP_*` value-mapping tables for code translation

## Runtime Design Points

- keep last successful extraction marker explicit
- separate extract success from load success
- track counts per checkpoint
- preserve restartability after staging
- isolate source-data defects from transport or destination failures

## 2023-Oriented Product Notes

- FSDM 2023 is ABAP-based, not HANA-native
- mapping-view performance improvements matter for high-volume flows
- LOT_ID length mismatch must be handled before or during transformation
- contract versus security routing must be explicit in the orchestration design
