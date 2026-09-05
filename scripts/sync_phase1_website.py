#!/usr/bin/env python3
"""Validate and synchronize Phase 1 jurisdiction counts in generated public HTML."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "website"
INV = ROOT / "legislation" / "STATE_IMPLEMENTATION_INVENTORY.md"

def inventory_rows():
    rows = []
    active = False
    for line in INV.read_text(encoding="utf-8").splitlines():
        if line.strip() == "| Jurisdiction | Status | First-pass record |":
            active = True
            continue
        if not active:
            continue
        if line.strip().startswith("|---"):
            continue
        m = re.match(r"^\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*`?([^|`]+?)`?\s*\|$", line)
        if m:
            rows.append(tuple(x.strip() for x in m.groups()))
        elif line.strip() and not line.lstrip().startswith("|"):
            break
    return rows

rows = inventory_rows()
completed = [r for r in rows if "NOT STARTED" not in r[1]]
total = len(rows)
completed_count = len(completed)
state_pages = sorted((WEB / "states").glob("*.html")) if (WEB / "states").exists() else []
source_pages = sorted((WEB / "sources").glob("*.html")) if (WEB / "sources").exists() else []

if not (WEB / "index.html").exists():
    raise SystemExit("CONTROL FAILURE: website/index.html is missing")
if len(state_pages) != completed_count:
    raise SystemExit(f"CONTROL FAILURE: state page count {len(state_pages)} != completed jurisdiction count {completed_count}")
if len(source_pages) != completed_count:
    raise SystemExit(f"CONTROL FAILURE: source page count {len(source_pages)} != completed jurisdiction count {completed_count}")

for p in WEB.rglob("*.html"):
    text = p.read_text(encoding="utf-8")
    text = re.sub(r'<div class="hero-number">\d+<span>/\d+</span></div>', f'<div class="hero-number">{completed_count}<span>/{total}</span></div>', text)
    text = re.sub(r'<div class="panel-note">.*?</div>', f'<div class="panel-note">{total - completed_count} jurisdiction(s) remain outside the completed sequence. The public library does not treat this as a policy or constitutional conclusion.</div>', text, flags=re.S)
    p.write_text(text, encoding="utf-8")

print(f"PH1_WEBSITE_SYNC completed={completed_count} total={total} state_pages={len(state_pages)} source_pages={len(source_pages)}")
