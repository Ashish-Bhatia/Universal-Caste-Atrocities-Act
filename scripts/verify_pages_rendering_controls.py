#!/usr/bin/env python3
"""Verify static rendering controls in the final Pages artifact tree."""
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "website"
CSS = WEB / "assets" / "site.css"
OVERRIDES = WEB / "assets" / "site-overrides.css"


def fail(message):
    raise SystemExit(f"PAGES RENDERING CONTROL FAILURE: {message}")

html_files = sorted(WEB.rglob("*.html"))
if not html_files:
    fail("no HTML pages found")
if not CSS.exists():
    fail("site.css missing")
if not OVERRIDES.exists():
    fail("site-overrides.css missing")

css = CSS.read_text(encoding="utf-8")
overrides = OVERRIDES.read_text(encoding="utf-8")
required_css = ["@media", ".support-btn", ".footergrid", ":focus-visible", ".tablewrap"]
for token in required_css:
    if token not in css:
        fail(f"final site.css missing rendering token: {token}")

for page in html_files:
    text = page.read_text(encoding="utf-8")
    if "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">" not in text:
        fail(f"missing responsive viewport: {page.relative_to(WEB)}")
    if "assets/site.css" not in text:
        fail(f"missing site stylesheet reference: {page.relative_to(WEB)}")
    if "Petition / Support" not in text:
        fail(f"missing public support pathway: {page.relative_to(WEB)}")
    for href in re.findall(r'href="([^"]+)"', text):
        parsed = urlparse(href)
        if parsed.scheme or href.startswith("#"):
            continue
        target = href.split("#", 1)[0].split("?", 1)[0]
        if not target:
            continue
        if not (page.parent / target).resolve().exists():
            fail(f"broken local render asset/link {href!r} from {page.relative_to(WEB)}")

# The production workflow merges the overrides into site.css before publication.
# Verify the merge is present rather than assuming the separate override file was loaded.
missing_from_final = [token for token in [".support-btn", ".nav", ".prose-card", "@media(max-width:640px)"] if token not in css]
if missing_from_final:
    fail("production override merge incomplete: " + ", ".join(missing_from_final))

print(f"Pages rendering controls passed: {len(html_files)} HTML pages; responsive, support, focus, table and local-link controls verified")
