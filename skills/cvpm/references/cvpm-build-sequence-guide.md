# CVPM Build Sequence Guide

**Classification:** extracted-customer-demo-evidence  
**Usage:** Use when the task needs a practical end-to-end CVPM setup sequence with configuration touchpoints and run-monitoring guidance.  
**Do not use for:** Direct reuse of sample `Z*` names, class names, or IDs as productive defaults.

This guide distills the local CVPM image set into a reusable build sequence.

## What the Image Set Confirms

- CVPM orchestrates analytical processes inside FPSL.
- It interfaces with SDL and RDL.
- It supports background and parallel processing.
- Its lifecycle is reviewed through the CVPM process monitor.

## Evidence-Based Build Order

Use this as the practical build sequence when the user asks how to develop a custom CVPM flow.

1. Create the server or worklist class.
2. Create the CVPM execution class.
3. Register the server for the primary data source.
4. Create the primary data source.
5. Create the analytical process.
6. Create the custom step sequence for that process.
7. Execute the run and review it in the monitor.

Keep all names as placeholders unless customer evidence confirms them.

## What Each Step Does

### 1. Server or Worklist Class

- exposes source records to the process
- defines package and worklist read behavior
- acts as the source-facing entry point

### 2. CVPM Execution Class

- contains the process logic executed by the analytical process
- receives prepared data and runs calculation or enrichment logic
- may group data into package-level execution structures

### 3. Server Registration for Primary Data Sources

- connects the implementation class to the FPSL data-source framework
- makes the server available for primary-data-source setup

### 4. Primary Data Source

- defines the source entry consumed by the process
- binds server, parameters, and selection characteristics

### 5. Analytical Process

- defines process identity and runtime behavior
- binds controller, process category, and technical settings

Observed fields in the screenshots include:

- report title
- step controller
- process category
- latest time stamp
- dynamic selection behavior
- subobject and authorization attributes

### 6. Custom Step Sequence

- defines the ordered processing chain
- separates parameter prep, worklist creation, and enrichment/calculation logic

Observed pattern:

- enrich parameters
- worklist
- enrich data

Treat this as a useful pattern, not a universal default.

### 7. Run and Monitor

- execute via background run or program trigger
- review in the CVPM monitor
- inspect step execution, timestamps, runtime, packages, and records processed

## Navigation Hints Seen In the Images

- `Financial Products Subledger -> Data Loading Process -> Data Sources for Worklists`
- `Financial Products Subledger -> Calculation and Valuation Process Manager (CVPM) -> General Settings for Custom Processes -> Edit Analytical Processes`
- `Financial Products Subledger -> Calculation and Valuation Process Manager (CVPM) -> General Settings for Custom Processes -> Edit Custom Step Sequences for Analytical Processes`
- `Financial Products Subledger -> Calculation and Valuation Process Manager (CVPM) -> /BAL/PW_PROCMON`

## Monitoring Signals Seen In the Images

The screenshots show run-review evidence such as:

- process name
- step sequence
- start and end time
- runtime
- package count
- record count

Use these as validation targets when users ask what a successful run should prove.

## Companion Skill Routing

- use `abap` or `amdp` for implementation artifacts
- use `reconciliation` for SQL checks after the run
- use `quality` for SDL/RDL rule checks
- use `mapping` for source-to-target mapping details feeding the process
