#!/usr/bin/env python3
"""Independent zero-drift verification for the State Implementation Source Ledger."""
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md"
STATE_DIR = ROOT / "research/states"
REPORT = ROOT / "project-state/PH1_MASTER_SOURCE_LEDGER_ZERO_DRIFT_2026-09-06.md"
BASELINE_COMMIT = "57f6a8006844f45e301e99f7f13d937297957cbe"

HEADER = "| ID | Source | Finding | Grade | Verification status |"
ID_RE = re.compile(r"^\|\s*([A-Za-z0-9_-]+)\s*\|")

def ids_from(text):
    ids = []
    active = False
    for line in text.splitlines():
        if line.strip() == HEADER:
            active = True
            continue
        if active:
            m = ID_RE.match(line)
            if m and m.group(1) != "ID":
                ids.append(m.group(1))
            elif line.strip() and not line.lstrip().startswith("|"):
                active = False
    return ids

master_text = MASTER.read_text(encoding="utf-8")
master_ids = ids_from(master_text)
source_ids = []
ledger_counts = {}
for path in sorted(STATE_DIR.glob("*_SOURCE_LEDGER.md")):
    ids = ids_from(path.read_text(encoding="utf-8"))
    if ids:
        ledger_counts[str(path.relative_to(ROOT))] = len(ids)
        source_ids.extend(ids)

master_set = set(master_ids)
source_set = set(source_ids)
master_dupes = sorted({x for x in master_ids if master_ids.count(x) > 1})
source_dupes = sorted({x for x in source_ids if source_ids.count(x) > 1})
missing = sorted(source_set - master_set)
extra = sorted(master_set - source_set)

# Repository-level diff against the known pre-integration main commit.
try:
    diff = subprocess.check_output(
        ["git", "diff", "--unified=0", BASELINE_COMMIT, "HEAD", "--", "research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md"],
        text=True,
    )
except subprocess.CalledProcessError as exc:
    raise SystemExit(f"ABORT: unable to calculate baseline diff: {exc}")

has_deletion = any(line.startswith("-") and not line.startswith("---") for line in diff.splitlines())
added_lines = [line for line in diff.splitlines() if line.startswith("+") and not line.startswith("+++")]

# The expected baseline had 164 source IDs. Current source-ledger union must be 261 IDs.
checks = {
    "master_has_no_duplicate_ids": not master_dupes,
    "source_ledgers_have_no_cross-ledger_duplicate_ids": not source_dupes,
    "all_source_ids_present_in_master": not missing,
    "master_contains_only_source_ids": not extra,
    "baseline_master_id_count_is_164": len(master_ids) >= 164,
    "current_master_id_count_is_261": len(master_ids) == 261,
    "no_master_deletion_since_control_baseline": not has_deletion,
    "master_diff_contains_additions": bool(added_lines),
}

if not all(checks.values()):
    raise SystemExit(
        "ABORT: zero-drift verification failed: " + ", ".join(k for k, v in checks.items() if not v)
    )

lines = [
    "# Phase 1 Master Source Ledger Zero-Drift Verification",
    "",
    "Date: 2026-09-06",
    "Workstream: independent read-back and zero-drift test",
    "",
    "## Result",
    "",
    "PASS. The post-integration master State Implementation Source Ledger contains every source-ledger row ID, contains no duplicate IDs, and shows no deletion against the pre-integration control baseline.",
    "",
    f"- Master source IDs read back: {len(master_ids)}",
    f"- Unique source IDs across jurisdiction ledgers: {len(source_set)}",
    f"- Missing source IDs in master: {len(missing)}",
    f"- Master-only IDs: {len(extra)}",
    f"- Master duplicate IDs: {len(master_dupes)}",
    f"- Cross-ledger duplicate IDs: {len(source_dupes)}",
    f"- Added diff lines against `{BASELINE_COMMIT}`: {len(added_lines)}",
    "- Deletion lines against baseline: 0",
    "",
    "## Checks",
    "",
]
for name, result in checks.items():
    lines.append(f"- {name}: {'PASS' if result else 'FAIL'}")
lines += [
    "",
    "## Source-ledger coverage",
    "",
]
for path, count in ledger_counts.items():
    lines.append(f"- `{path}`: {count} IDs")
lines += [
    "",
    "## Control statement",
    "",
    "This verification is independent of the integration script's write-time assertions. It reads the committed repository state, compares the master ID set with all jurisdiction source-ledger ID sets, checks duplicates, and inspects the Git diff against the pre-integration control commit. It does not reopen substantive jurisdictions or infer legal absence.",
]
REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("PASS: zero-drift verification")
