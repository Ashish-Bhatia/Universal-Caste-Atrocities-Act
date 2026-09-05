#!/usr/bin/env python3
"""Remove the identified project-control reference from generated public HTML.

This changes generated output only. It does not modify the substantive research source.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "website"
TARGET = WEB / "law" / "priority-central-legislation-screening.html"

if TARGET.exists():
    text = TARGET.read_text(encoding="utf-8")
    text = text.replace("DECISIONS_LOG.md", "the project's decision-control process")
    TARGET.write_text(text, encoding="utf-8")
    print(f"Sanitized generated public page: {TARGET.relative_to(ROOT)}")
else:
    raise SystemExit(f"Missing expected generated page: {TARGET}")
