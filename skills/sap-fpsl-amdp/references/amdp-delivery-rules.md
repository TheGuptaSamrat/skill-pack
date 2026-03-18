# AMDP Delivery Rules

- Separate wrapper responsibilities from SQLScript responsibilities.
- Validate input shape, execution boundary, and fail-fast rules in ABAP.
- Keep AMDP focused on set-based transformation.
- Stage complex SQLScript in readable blocks.
- Use exact join keys and filter dimensions.
- Prefer `MERGE` or rerun-safe write patterns only when rerun behavior is required.
- Call out when a CDS table function is a better fit than a direct AMDP method.
- Include a test strategy even if full automation is not possible.
