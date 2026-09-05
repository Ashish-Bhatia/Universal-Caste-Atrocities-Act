#!/usr/bin/env python3
"""Verify master/jurisdiction source-ledger synchronization for the public site.

This is a control comparison only. It does not modify the master ledger or perform
substantive source research.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "research" / "STATE_IMPLEMENTATION_SOURCE_LEDGER.md"
STATE_DIR = ROOT / "research" / "states"

HEADER_RE = re.compile(r"^\|\s*ID\s*\|", re.I)
ID_RE = re.compile(r"^[A-Z0-9][A-Z0-9_-]*-[A-Z0-9][A-Z0-9_-]*$")


def extract_ids(path: Path):
    ids = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or cells[0].lower() in {"id", "---"}:
            continue
        if ID_RE.fullmatch(cells[0]):
            ids.append(cells[0])
    return ids


master_ids = set(extract_ids(MASTER))
ledger_sets = {}
all_ledger_ids = set()
for path in sorted(STATE_DIR.glob("*_SOURCE_LEDGER.md")):
    ids = set(extract_ids(path))
    if ids:
        ledger_sets[path] = ids
        all_ledger_ids.update(ids)

missing_from_master = sorted(all_ledger_ids - master_ids)
master_only = sorted(master_ids - all_ledger_ids)

print(f"MASTER_IDS={len(master_ids)}")
print(f"JURISDICTION_LEDGER_FILES={len(ledger_sets)}")
print(f"JURISDICTION_LEDGER_IDS={len(all_ledger_ids)}")
print(f"MISSING_FROM_MASTER={len(missing_from_master)}")
print("MISSING_IDS=" + ",".join(missing_from_master))
print(f"MASTER_ONLY_IDS={len(master_only)}")

for path, ids in ledger_sets.items():
    gap = sorted(ids - master_ids)
    print(f"LEDGER {path.relative_to(ROOT)}: total={len(ids)} missing_from_master={len(gap)}")
    if gap:
        print("  " + ",".join(gap))
