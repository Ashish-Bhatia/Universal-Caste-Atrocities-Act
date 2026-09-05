#!/usr/bin/env python3
"""Remove internal project-control references from generated public HTML only."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "website"
REPLACEMENTS = {
    "PROJECT_STATE.md": "internal project state record",
    "NEXT_CHAT.md": "internal continuity record",
    "RESEARCH_LEDGER.md": "internal research-control record",
    "ISSUES_REGISTER.md": "internal issue-control record",
    "DECISIONS_LOG.md": "the project's decision-control process",
    "BASELINE_AUDIT.md": "historical internal baseline record",
    "project-control": "internal project management",
    "project control": "internal project management",
    "continuation prompt": "continuity instruction",
    "through `decisions_log.md`": "through the project's decision-control process",
}

changed = 0
for target in WEB.rglob("*.html"):
    text = target.read_text(encoding="utf-8")
    updated = text
    for old, new in REPLACEMENTS.items():
        updated = updated.replace(old, new).replace(old.lower(), new)
    if updated != text:
        target.write_text(updated, encoding="utf-8")
        changed += 1
        print(f"Sanitized public page: {target.relative_to(ROOT)}")

print(f"Public sanitization completed: {changed} HTML page(s) changed")
