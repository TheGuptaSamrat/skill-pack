#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"

python3 "$repo_root/scripts/audit_skill_pack_redundancy.py" \
  --repo-root "$repo_root" \
  --out-md "docs-context/indexes/redundancy-audit.md" \
  --out-json "docs-context/indexes/redundancy-audit.json"

python3 "$repo_root/scripts/validate_skill_pack_links.py" \
  --repo-root "$repo_root" \
  --out-json "docs-context/indexes/validation-skill-pack.json"

echo "Context optimization audit completed."
echo "- docs-context/indexes/redundancy-audit.md"
echo "- docs-context/indexes/redundancy-audit.json"
echo "- docs-context/indexes/validation-skill-pack.json"
