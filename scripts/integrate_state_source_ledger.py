#!/usr/bin/env python3
"""Safely integrate jurisdiction source-ledger rows into the master ledger.

This script preserves the existing master byte-for-byte up to the append point,
adds only previously absent source IDs from jurisdiction *_SOURCE_LEDGER.md files,
and refuses to rewrite or truncate the existing master content.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MASTER = ROOT / "research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md"
STATE_DIR = ROOT / "research/states"
OUT_REPORT = ROOT / "project-state/PH1_MASTER_SOURCE_LEDGER_INTEGRATION_REPORT_2026-09-06.md"

ID_RE = re.compile(r"^\|\s*([A-Za-z0-9_-]+)\s*\|")
HEADER = "| ID | Source | Finding | Grade | Verification status |"
SEP = "|---|---|---|---|---|"

def extract_rows(text):
    rows = []
    in_table = False
    for line in text.splitlines():
        if line.strip() == HEADER:
            in_table = True
            continue
        if in_table and line.strip() == SEP:
            continue
        if in_table:
            m = ID_RE.match(line)
            if m and m.group(1) not in {"ID"}:
                rows.append((m.group(1), line.rstrip()))
            elif line.strip() and not line.lstrip().startswith("|"):
                in_table = False
    return rows

master_text = MASTER.read_text(encoding="utf-8")
master_ids = [i for i, _ in extract_rows(master_text)]
master_id_set = set(master_ids)
if len(master_ids) != len(master_id_set):
    dupes = sorted({i for i in master_ids if master_ids.count(i) > 1})
    raise SystemExit(f"ABORT: duplicate IDs already present in master: {dupes}")

ledgers = sorted(STATE_DIR.glob("*_SOURCE_LEDGER.md"))
if not ledgers:
    raise SystemExit("ABORT: no jurisdiction source ledgers found")

new_by_file = []
all_source_ids = set()
for path in ledgers:
    rows = extract_rows(path.read_text(encoding="utf-8"))
    if not rows:
        continue
    local_seen = set()
    new_rows = []
    for sid, line in rows:
        if sid in local_seen:
            raise SystemExit(f"ABORT: duplicate ID {sid} inside {path}")
        local_seen.add(sid)
        if sid in all_source_ids:
            # Duplicate across jurisdiction ledgers is unsafe. Existing master
            # membership is handled separately, so only cross-ledger duplicates abort.
            if sid not in master_id_set:
                raise SystemExit(f"ABORT: source ID {sid} appears in multiple jurisdiction ledgers")
        all_source_ids.add(sid)
        if sid not in master_id_set:
            new_rows.append(line)
    if new_rows:
        new_by_file.append((path, new_rows))

if not new_by_file:
    report = """# Phase 1 Master Source Ledger Integration Report\n\nDate: 2026-09-06\n\n## Result\n\nNO-OP. Every source-ledger row ID is already present in the master State Implementation Source Ledger.\n\nThe script performed no rewrite and no truncation.\n"""
    OUT_REPORT.write_text(report, encoding="utf-8")
    print("NO-OP: master already contains all source-ledger IDs")
    raise SystemExit(0)

append_parts = ["", "## Controlled later-jurisdiction integration, 2026-09-06", ""]
for path, rows in new_by_file:
    append_parts.append(f"## {path.stem.replace('_SOURCE_LEDGER', '').replace('_', ' ').title()} inventory, controlled integration")
    append_parts.append("")
    append_parts.append(HEADER)
    append_parts.append(SEP)
    append_parts.extend(rows)
    append_parts.append("")

new_text = master_text.rstrip("\n") + "\n" + "\n".join(append_parts).rstrip("\n") + "\n"

# Safety invariant: original master content must be an exact prefix.
if not new_text.startswith(master_text.rstrip("\n")):
    raise SystemExit("ABORT: original master content was not preserved as an exact prefix")

MASTER.write_text(new_text, encoding="utf-8")

post_ids = [i for i, _ in extract_rows(new_text)]
if len(post_ids) != len(set(post_ids)):
    dupes = sorted({i for i in post_ids if post_ids.count(i) > 1})
    raise SystemExit(f"ABORT AFTER WRITE: duplicate IDs detected: {dupes}")
if not master_id_set.issubset(set(post_ids)):
    raise SystemExit("ABORT AFTER WRITE: pre-existing master ID set was not preserved")

added = [i for i in post_ids if i not in master_id_set]
expected_new = [sid for _, rows in new_by_file for sid, _ in [(ID_RE.match(r).group(1), r) for r in rows]]
if set(added) != set(expected_new):
    raise SystemExit("ABORT AFTER WRITE: added ID set differs from source-ledger delta")

report_lines = [
    "# Phase 1 Master Source Ledger Integration Report",
    "",
    "Date: 2026-09-06",
    "Workstream: controlled master source-ledger integration",
    "",
    "## Result",
    "",
    "PASS. Later jurisdiction-specific source-ledger rows were integrated into the master ledger without rewriting or truncating the pre-existing master content.",
    "",
    f"- Master IDs before integration: {len(master_ids)}",
    f"- Master IDs after integration: {len(post_ids)}",
    f"- New IDs integrated: {len(added)}",
    f"- Jurisdiction ledgers contributing new rows: {len(new_by_file)}",
    "- Existing master ID set preserved: YES",
    "- Duplicate source IDs after integration: NONE",
    "- Source-ledger delta matches added master IDs: YES",
    "",
    "## Contributing ledgers",
    "",
]
for path, rows in new_by_file:
    report_lines.append(f"- `{path.relative_to(ROOT)}`: {len(rows)} new rows")
report_lines += [
    "",
    "## Control statement",
    "",
    "The script does not infer legal absence, alter jurisdiction-specific substantive findings, renumber IDs, or reopen jurisdictions. It integrates only rows already present in repository jurisdiction source ledgers.",
]
OUT_REPORT.write_text("\n".join(report_lines) + "\n", encoding="utf-8")
print(f"PASS: integrated {len(added)} new source rows")
