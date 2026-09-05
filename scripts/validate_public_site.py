#!/usr/bin/env python3
"""Validate the generated public site before GitHub Pages publication."""
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "website"
STATE_DIR = WEB / "states"
SOURCE_DIR = WEB / "sources"
INV = ROOT / "legislation" / "STATE_IMPLEMENTATION_INVENTORY.md"
CSS = WEB / "assets" / "site.css"
BANNED = ["PROJECT_STATE.md", "NEXT_CHAT.md", "RESEARCH_LEDGER.md", "ISSUES_REGISTER.md", "DECISIONS_LOG.md", "BASELINE_AUDIT.md"]
BANNED_PHRASES = ["modify the project record", "project-control", "project control", "continuation prompt", "no bill drafting", "no phase 2"]


def fail(message):
    raise SystemExit(f"PUBLIC SITE VALIDATION FAILURE: {message}")


def completed_inventory_count():
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
    return len([r for r in rows if "NOT STARTED" not in r[1]])


html_files = sorted(WEB.rglob("*.html"))
if not html_files:
    fail("no HTML pages generated")
expected = completed_inventory_count()
state_count = len(list(STATE_DIR.glob("*.html")))
source_count = len(list(SOURCE_DIR.glob("*.html")))
if state_count != expected:
    fail(f"expected {expected} completed-jurisdiction research pages, found {state_count}")
if source_count != expected:
    fail(f"expected {expected} completed-jurisdiction source pages, found {source_count}")
for required in ["index.html", "research.html", "states.html", "law.html", "sources.html", "methodology.html", "bill.html", "petition.html", "404.html", "robots.txt", "sitemap.xml"]:
    if not (WEB / required).exists():
        fail(f"missing required route: {required}")

all_html = "\n".join(path.read_text(encoding="utf-8") for path in html_files)
for banned in BANNED:
    if banned.casefold() in all_html.casefold():
        fail(f"internal filename leaked: {banned}")
for phrase in BANNED_PHRASES:
    if phrase.casefold() in all_html.casefold():
        fail(f"internal project-management phrase leaked: {phrase}")
if "github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act" in all_html:
    fail("repository-navigation URL leaked into public HTML")

css = CSS.read_text(encoding="utf-8")
for token in ["@media", ".support-btn", ".footergrid", ":focus-visible"]:
    if token not in css:
        fail(f"required responsive/accessibility CSS control missing: {token}")

for page in html_files:
    text = page.read_text(encoding="utf-8")
    for required in ['<header class="topbar">', '<footer>', 'Petition / Support']:
        if required not in text:
            fail(f"{required} missing from {page.relative_to(WEB)}")

for page in html_files:
    text = page.read_text(encoding="utf-8")
    for href in re.findall(r'href="([^"]+)"', text):
        parsed = urlparse(href)
        if parsed.scheme or href.startswith("#"):
            continue
        target = href.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        resolved = (page.parent / target).resolve()
        if not resolved.exists():
            fail(f"broken local link {href!r} from {page.relative_to(WEB)}")

for page in SOURCE_DIR.glob("*.html"):
    text = page.read_text(encoding="utf-8")
    if "No controlled source rows are available" in text:
        fail(f"empty completed-jurisdiction source page: {page.relative_to(WEB)}")

print(f"Public site validation passed: {len(html_files)} HTML pages, {state_count} jurisdiction pages, {source_count} source pages")
