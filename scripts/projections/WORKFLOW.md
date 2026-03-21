# HANA Volume Tracker — Local Script Workflow

No AI needed. This is a fully repeatable, script-driven process.

## Files

| File | Purpose |
|------|---------|
| `hana_volume_snapshot.sql` | Run in HANA Studio / HANA Cockpit — 4 sections |
| `volume-snapshots.csv` | Append table-level results here each run |
| `db-size-snapshots.csv` | Append DB-level disk results here each run |
| `generate_projection_workbook.py` | Reads both CSVs → produces Excel workbook |

---

## Weekly / Monthly Procedure

### Step 1 — Run the SQL

Open `hana_volume_snapshot.sql` in HANA Studio (or DBeaver, HANA Cockpit).

- Edit the `SCHEMA_NAME IN (...)` list in **Section 1** with your actual schema names.
- Run **Section 1** (per-table column store). Export as CSV.
- Run **Section 3** (DB disk usage). Export as CSV.

### Step 2 — Append to the CSV files

Append the Section 1 results to `volume-snapshots.csv`.
Append the Section 3 results to `db-size-snapshots.csv`.

> Keep the header row only once (first time). Subsequent appends are data rows only.
> Date format must be `YYYY-MM-DD`.

### Step 3 — Generate the workbook

```bash
cd scripts/projections

# Install dependency once:
pip install openpyxl

# Generate (adjust paths as needed):
python generate_projection_workbook.py \
  --tables volume-snapshots.csv \
  --dbsize db-size-snapshots.csv \
  --output FPSL-volume-$(date +%Y-%m-%d).xlsx \
  --horizon 26
```

`--horizon 26` projects 26 weeks (6 months) forward. Change to `13` for 3 months.

---

## Workbook Output Sheets

| Sheet | Content |
|-------|---------|
| **Cover** | Run metadata, sheet index, refresh steps |
| **Raw Data** | All rows from the table snapshot CSV |
| **Table Trend** | Pivot — each table × each date, records + memory MB |
| **DB Size Trend** | Disk usage per volume type, red/amber at 80 / 60% utilization |
| **Growth Rates** | Period-over-period delta and % change, red rows at >10% weekly growth |
| **Projection** | Linear extrapolation per table for the configured horizon |
| **Chart — DB Data** | Line chart of DATA volume used GB over time |

---

## Recommended Cadence

| Action | Frequency |
|--------|-----------|
| Run SQL + append CSVs | Every 7 days |
| Generate workbook | Monthly (or after each quarter for planning) |
| Review `Growth Rates` tab | Monthly — flag tables with sustained >5%/week growth |
| Share workbook | With infrastructure / capacity planning teams |

---

## Tips

- Do not delete old rows from the CSVs — historical data is what powers the trend and projection sheets.
- If a table is dropped or renamed, it will simply stop appearing in future snapshots; old history is retained.
- To reset the projection baseline, start a new CSV with only the most recent N months of data.
- Section 4 of the SQL (top-20 ad-hoc audit) is optional; do not append it to the tracking CSVs.
