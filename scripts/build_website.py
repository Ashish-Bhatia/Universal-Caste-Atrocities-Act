#!/usr/bin/env python3
"""Build the public static research site from authoritative repository research files.

The public site intentionally excludes project-control files such as PROJECT_STATE,
NEXT_CHAT, issue registers and decision logs. It publishes research records only.
"""
from pathlib import Path
import html
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "website"
INV = ROOT / "legislation" / "STATE_IMPLEMENTATION_INVENTORY.md"
MASTER = ROOT / "research" / "STATE_IMPLEMENTATION_SOURCE_LEDGER.md"
STATE_DIR = ROOT / "legislation" / "states"

LAW_DOCS = [
    ("SC/ST Prevention of Atrocities Act", "SCST_ACT_CLAUSE_EXTRACTION.md", "Clause-level Act extraction and amendment provenance."),
    ("SC/ST Prevention of Atrocities Rules", "SCST_RULES_CLAUSE_EXTRACTION.md", "Rules, Schedule and Annexure inventory."),
    ("SC/ST Act, BNS crosswalk", "SCST_ACT_SECTION3_BNS_CROSSWALK.md", "Section 3 conduct and Schedule correspondence with BNS."),
    ("SC/ST Act, BNSS crosswalk", "SCST_ACT_BNSS_PROCEDURAL_CROSSWALK.md", "Procedural interfaces and transition questions."),
    ("SC/ST Act, BSA crosswalk", "SCST_ACT_BSA_EVIDENCE_PRESUMPTION_CROSSWALK.md", "Evidence, burden and statutory-presumption interfaces."),
    ("Protection of Civil Rights Act and Rules", "PCR_ACT_RULES_SECTION_RULE_COMPARISON.md", "Section/rule comparison with the PoA framework."),
    ("Manual Scavengers Act and Rules", "MANUAL_SCAVENGERS_ACT_RULES_SCST_CROSSWALK.md", "Prohibition, rehabilitation and related-law interfaces."),
    ("Bonded Labour Act and Rules", "BONDED_LABOUR_ACT_RULES_SCST_CROSSWALK.md", "Bonded-labour protections and PoA overlap."),
    ("Priority Central legislation screening", "CENTRAL_LEGISLATION_PRIORITY_SCREENING.md", "Screening of additional Central-law interfaces."),
]

NAV = [
    ("Research", "research.html"),
    ("States & UTs", "states.html"),
    ("Existing Law", "law.html"),
    ("Sources", "sources.html"),
    ("Methodology", "methodology.html"),
]


def slug(text):
    value = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return value or "page"


def parse_inventory():
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
            name, status, path = m.groups()
            rows.append((name.strip(), status.strip(), path.strip()))
        elif line.strip() and not line.lstrip().startswith("|"):
            break
    return rows


def markdown_inline(text):
    escaped = html.escape(text, quote=False)
    escaped = re.sub(
        r"\[([^\]]+)\]\((https?://[^)\s]+)\)",
        r'<a href="\2" rel="noopener noreferrer">\1</a>',
        escaped,
    )
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    return escaped


def markdown_to_html(text):
    lines = text.splitlines()
    out = []
    i = 0
    paragraph = []
    list_items = []

    def flush_paragraph():
        nonlocal paragraph
        if paragraph:
            joined = " ".join(x.strip() for x in paragraph)
            out.append(f"<p>{markdown_inline(joined)}</p>")
            paragraph = []

    def flush_list():
        nonlocal list_items
        if list_items:
            out.append("<ul>" + "".join(f"<li>{markdown_inline(x)}</li>" for x in list_items) + "</ul>")
            list_items = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            flush_paragraph()
            flush_list()
            i += 1
            continue

        if stripped.startswith("```"):
            flush_paragraph()
            flush_list()
            code = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            out.append(f"<pre><code>{html.escape(chr(10).join(code))}</code></pre>")
            i += 1
            continue

        if stripped.startswith("# "):
            flush_paragraph()
            flush_list()
            out.append(f"<h1>{markdown_inline(stripped[2:].strip())}</h1>")
            i += 1
            continue
        if stripped.startswith("## "):
            flush_paragraph()
            flush_list()
            title = stripped[3:].strip()
            out.append(f'<h2 id="{slug(re.sub(r"^[0-9]+[.)]?\s*", "", title))}">{markdown_inline(title)}</h2>')
            i += 1
            continue
        if stripped.startswith("### "):
            flush_paragraph()
            flush_list()
            out.append(f"<h3>{markdown_inline(stripped[4:].strip())}</h3>")
            i += 1
            continue

        if stripped.startswith("|"):
            flush_paragraph()
            flush_list()
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            if len(table_lines) >= 2:
                rows = []
                for row in table_lines:
                    cells = [c.strip() for c in row.strip("|").split("|")]
                    if not all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                        rows.append(cells)
                if rows:
                    head = rows[0]
                    body = rows[1:]
                    table = ["<div class=\"tablewrap\"><table class=\"table\"><thead><tr>"]
                    table.append("".join(f"<th>{markdown_inline(c)}</th>" for c in head))
                    table.append("</tr></thead><tbody>")
                    for row in body:
                        padded = row + [""] * max(0, len(head) - len(row))
                        table.append("<tr>" + "".join(f"<td>{markdown_inline(c)}</td>" for c in padded[:len(head)]) + "</tr>")
                    table.append("</tbody></table></div>")
                    out.append("".join(table))
            continue

        m = re.match(r"^[-*]\s+(.*)$", stripped)
        if m:
            flush_paragraph()
            list_items.append(m.group(1))
            i += 1
            continue

        if re.match(r"^\d+\.\s+", stripped):
            flush_paragraph()
            flush_list()
            items = []
            while i < len(lines):
                mm = re.match(r"^\d+\.\s+(.*)$", lines[i].strip())
                if not mm:
                    break
                items.append(mm.group(1))
                i += 1
            out.append("<ol>" + "".join(f"<li>{markdown_inline(x)}</li>" for x in items) + "</ol>")
            continue

        if stripped.startswith(">"):
            flush_paragraph()
            flush_list()
            out.append(f"<blockquote>{markdown_inline(stripped[1:].strip())}</blockquote>")
            i += 1
            continue

        paragraph.append(stripped)
        i += 1

    flush_paragraph()
    flush_list()
    return "\n".join(out)


def strip_project_controls(text):
    lines = text.splitlines()
    cleaned = []
    skip = False
    for line in lines:
        stripped = line.strip()
        if re.match(r"^(Status|Phase|Research date|Opened):", stripped):
            continue
        if stripped == "## Disposition":
            skip = True
            continue
        if skip and stripped.startswith("## "):
            skip = False
        if skip:
            continue
        if "No Bill drafting" in stripped or "No Phase 2" in stripped:
            continue
        cleaned.append(line)
    return "\n".join(cleaned)


def parse_source_rows():
    rows = []
    for line in MASTER.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        if cells[0] in {"ID", "---"}:
            continue
        source_id = cells[0]
        if not re.fullmatch(r"[A-Z0-9]+-[A-Z0-9_-]+", source_id):
            continue
        rows.append(cells)
    return rows


def source_ids_for_text(text):
    return {m.group(1) for m in re.finditer(r"\b([A-Z][A-Z0-9_]*-[A-Z0-9_-]+)\b", text)}


def source_table(rows):
    if not rows:
        return '<p class="muted">No matching master-ledger rows were found for this research record.</p>'
    parts = [
        '<div class="tablewrap"><table class="table"><thead><tr>'
        "<th>Source ID</th><th>Source</th><th>Finding</th><th>Grade</th><th>Verification</th>"
        "</tr></thead><tbody>"
    ]
    for cells in rows:
        padded = cells + [""] * (5 - len(cells))
        parts.append("<tr>" + "".join(f"<td>{markdown_inline(c)}</td>" for c in padded[:5]) + "</tr>")
    parts.append("</tbody></table></div>")
    return "".join(parts)


def nav_html(active):
    return "".join(
        f'<a class="nav-link {"active" if label == active else ""}" href="{href}">{label}</a>'
        for label, href in NAV
    )


def shell(title, active, body):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Evidence-first research on India's caste-atrocity legal and implementation framework.">
<title>{html.escape(title)} | Universal Caste Atrocities Act Research</title>
<link rel="stylesheet" href="assets/site.css?v=20260906-2">
</head>
<body>
<header class="topbar"><div class="shell nav">
<a class="brand" href="index.html">Universal Caste Atrocities Act Research</a>
<nav class="navlinks" aria-label="Primary navigation">{nav_html(active)}</nav>
</div></header>
<main class="shell main">{body}</main>
<footer><div class="shell footergrid">
<div><strong>Universal Caste Atrocities Act Research</strong><p>Public research interface. Evidence, source provenance and qualifications are preserved.</p></div>
<div class="smalllinks"><a href="research.html">Research</a><a href="states.html">States & UTs</a><a href="law.html">Existing Law</a></div>
<div class="smalllinks"><a href="sources.html">Sources</a><a href="methodology.html">Methodology</a></div>
</div></footer>
</body></html>'''


states = parse_inventory()
completed = [r for r in states if "NOT STARTED" not in r[1]]
source_rows = parse_source_rows()

WEB.mkdir(parents=True, exist_ok=True)
for path in WEB.glob("*.html"):
    path.unlink()
for directory in (WEB / "states", WEB / "law", WEB / "sources"):
    if directory.exists():
        shutil.rmtree(directory)

index_body = f'''
<section class="hero-grid">
<div class="hero-copy">
<span class="eyebrow">Public research library</span>
<h1>Evidence before legislation.</h1>
<p class="lead">A source-controlled examination of India's caste-atrocity legal and implementation framework. The public record separates law, jurisdictional implementation evidence and source provenance.</p>
<div class="actions"><a class="btn primary" href="states.html">Browse State & UT research</a><a class="btn secondary" href="law.html">Read existing-law research</a></div>
</div>
<aside class="hero-panel">
<div><div class="panel-label">Jurisdiction research</div><div class="hero-number">States<br><span>& UTs</span></div><p>Published implementation records, with evidentiary qualifications and currentness limitations retained.</p></div>
<div class="panel-note">Each page is generated from a substantive jurisdiction research record.</div>
</aside>
</section>
<section class="section">
<div class="section-head"><div><div class="section-kicker">Research library</div><h2>Browse the evidence by subject.</h2></div></div>
<div class="grid">
<a class="card feature-card" href="states.html"><span class="index">01</span><div><h3>States & UTs</h3><p>Jurisdiction-specific implementation inventories and evidence.</p></div></a>
<a class="card feature-card" href="law.html"><span class="index">02</span><div><h3>Existing law</h3><p>SC/ST Act and Rules, BNS, BNSS, BSA and related Central-law interfaces.</p></div></a>
<a class="card feature-card" href="sources.html"><span class="index">03</span><div><h3>Source library</h3><p>Source identifiers, findings, evidence grades and verification status.</p></div></a>
<a class="card feature-card" href="methodology.html"><span class="index">04</span><div><h3>Methodology</h3><p>Evidence grades, source hierarchy, currentness and conflict rules.</p></div></a>
</div>
</section>
<section class="section prose-card">
<div class="section-kicker">Scope</div>
<h2>What this site publishes</h2>
<ul class="clean-list">
<li>Actual legal and implementation research from the repository's substantive records.</li>
<li>Primary-source provenance and evidence grades where recorded.</li>
<li>Jurisdiction-specific qualifications, contradictions and unresolved research questions.</li>
<li>Existing-law crosswalks and related-law interfaces.</li>
</ul>
</section>
'''
WEB.joinpath("index.html").write_text(shell("Research home", "", index_body), encoding="utf-8")

state_cards = []
for name, status, path in completed:
    state_cards.append(
        f'<a class="state-card" href="states/{slug(name)}.html"><span class="chip">Research record</span>'
        f"<h3>{html.escape(name)}</h3><p>State/UT implementation inventory</p>"
        f'<span class="text-link">Open research →</span></a>'
    )
states_body = f'''
<section class="page-intro">
<span class="eyebrow">Jurisdiction research</span>
<h1>States & Union Territories</h1>
<p class="lead">Browse the published State and Union Territory implementation inventories. The pages publish research records rather than project-control material.</p>
</section>
<section class="toolbar">
<label class="searchbox"><span>Search jurisdictions</span><input id="stateSearch" type="search" placeholder="e.g. Kerala, Delhi, Jammu" autocomplete="off"></label>
</section>
<section class="state-grid" id="stateGrid">{''.join(state_cards)}</section>
<p class="empty" id="emptyState" hidden>No jurisdictions match the search.</p>
'''
state_extra = '''<script>
const input=document.getElementById('stateSearch');
const empty=document.getElementById('emptyState');
function filterStates(){
  const q=input.value.toLowerCase().trim();
  let shown=0;
  document.querySelectorAll('.state-card').forEach(card=>{
    const ok=card.textContent.toLowerCase().includes(q);
    card.hidden=!ok;
    if(ok) shown++;
  });
  empty.hidden=shown!==0;
}
input.addEventListener('input',filterStates);
</script>'''
WEB.joinpath("states.html").write_text(shell("States & UTs", "States & UTs", states_body + state_extra), encoding="utf-8")

WEB.joinpath("states").mkdir(parents=True, exist_ok=True)
for name, status, path in completed:
    src = ROOT / path
    if not src.exists():
        raise FileNotFoundError(f"Inventory file listed in master matrix is missing: {path}")
    raw = src.read_text(encoding="utf-8")
    research = strip_project_controls(raw)
    ids = source_ids_for_text(raw)
    matched = [row for row in source_rows if row[0] in ids]
    body = f'''
<section class="page-intro">
<span class="eyebrow">State & UT research</span>
<h1>{html.escape(name)}</h1>
<p class="lead">Jurisdiction-specific implementation evidence from the repository research record. Qualifications and unresolved questions are retained.</p>
</section>
<section class="section prose-card">{markdown_to_html(research)}</section>
<section class="section">
<div class="section-head"><div><div class="section-kicker">Evidence library</div><h2>Sources cited by this record</h2></div><span class="chip">{len(matched)} matched source rows</span></div>
{source_table(matched)}
</section>
<section class="section actions"><a class="btn secondary" href="../states.html">Back to States & UTs</a><a class="btn secondary" href="../sources/{slug(name)}.html">Open source set</a></section>
'''
    WEB.joinpath("states", f"{slug(name)}.html").write_text(
        shell(name, "States & UTs", body)
        .replace('href="research.html"', 'href="../research.html"')
        .replace('href="states.html"', 'href="../states.html"')
        .replace('href="law.html"', 'href="../law.html"')
        .replace('href="sources.html"', 'href="../sources.html"')
        .replace('href="methodology.html"', 'href="../methodology.html"')
        .replace('href="index.html"', 'href="../index.html"')
        .replace('href="assets/site.css', 'href="../assets/site.css'),
        encoding="utf-8",
    )

law_cards = []
for title, filename, description in LAW_DOCS:
    source = ROOT / "legislation" / filename
    if not source.exists():
        continue
    law_cards.append(
        f'<a class="card feature-card" href="law/{slug(title)}.html"><span class="index">{len(law_cards)+1:02d}</span>'
        f"<div><h3>{html.escape(title)}</h3><p>{html.escape(description)}</p></div></a>"
    )
law_body = f'''
<section class="page-intro">
<span class="eyebrow">Existing-law research</span>
<h1>Legal framework</h1>
<p class="lead">Research records covering the principal Central statutes and identified interfaces. These pages do not contain a proposed Bill.</p>
</section>
<section class="grid">{''.join(law_cards)}</section>
'''
WEB.joinpath("law.html").write_text(shell("Existing Law", "Existing Law", law_body), encoding="utf-8")

WEB.joinpath("law").mkdir(parents=True, exist_ok=True)
for title, filename, description in LAW_DOCS:
    source = ROOT / "legislation" / filename
    if not source.exists():
        continue
    research = strip_project_controls(source.read_text(encoding="utf-8"))
    body = f'''
<section class="page-intro">
<span class="eyebrow">Existing-law research</span>
<h1>{html.escape(title)}</h1>
<p class="lead">{html.escape(description)}</p>
</section>
<section class="section prose-card">{markdown_to_html(research)}</section>
<section class="section actions"><a class="btn secondary" href="../law.html">Back to Existing Law</a></section>
'''
    WEB.joinpath("law", f"{slug(title)}.html").write_text(
        shell(title, "Existing Law", body)
        .replace('href="research.html"', 'href="../research.html"')
        .replace('href="states.html"', 'href="../states.html"')
        .replace('href="law.html"', 'href="../law.html"')
        .replace('href="sources.html"', 'href="../sources.html"')
        .replace('href="methodology.html"', 'href="../methodology.html"')
        .replace('href="index.html"', 'href="../index.html"')
        .replace('href="assets/site.css', 'href="../assets/site.css'),
        encoding="utf-8",
    )

research_body = '''
<section class="page-intro">
<span class="eyebrow">Research library</span>
<h1>Research by subject.</h1>
<p class="lead">The public site exposes substantive research records and source provenance. Project-management controls remain outside the public research interface.</p>
</section>
<section class="grid">
<a class="card feature-card" href="states.html"><span class="index">01</span><div><h3>State implementation</h3><p>Jurisdiction-specific implementation inventories.</p></div></a>
<a class="card feature-card" href="law.html"><span class="index">02</span><div><h3>Existing law</h3><p>Central legislation and BNS/BNSS/BSA transition research.</p></div></a>
<a class="card feature-card" href="sources.html"><span class="index">03</span><div><h3>Source evidence</h3><p>Source identifiers, findings, grades and verification status.</p></div></a>
</section>
'''
WEB.joinpath("research.html").write_text(shell("Research", "Research", research_body), encoding="utf-8")

source_cards = []
WEB.joinpath("sources").mkdir(parents=True, exist_ok=True)
for name, status, path in completed:
    raw = (ROOT / path).read_text(encoding="utf-8")
    ids = source_ids_for_text(raw)
    matched = [row for row in source_rows if row[0] in ids]
    source_cards.append(
        f'<a class="card feature-card" href="sources/{slug(name)}.html"><span class="index">{len(source_cards)+1:02d}</span>'
        f'<div><h3>{html.escape(name)}</h3><p>{len(matched)} source rows linked to the jurisdiction research record.</p></div></a>'
    )
    source_body = f'''
<section class="page-intro">
<span class="eyebrow">Jurisdiction source set</span>
<h1>{html.escape(name)}</h1>
<p class="lead">Source rows linked to the published {html.escape(name)} implementation research record.</p>
</section>
<section class="section">{source_table(matched)}</section>
<section class="section actions"><a class="btn secondary" href="../sources.html">Back to Sources</a><a class="btn secondary" href="../states/{slug(name)}.html">Open research record</a></section>
'''
    WEB.joinpath("sources", f"{slug(name)}.html").write_text(
        shell(f"{name} Sources", "Sources", source_body)
        .replace('href="research.html"', 'href="../research.html"')
        .replace('href="states.html"', 'href="../states.html"')
        .replace('href="law.html"', 'href="../law.html"')
        .replace('href="sources.html"', 'href="../sources.html"')
        .replace('href="methodology.html"', 'href="../methodology.html"')
        .replace('href="index.html"', 'href="../index.html"')
        .replace('href="assets/site.css', 'href="../assets/site.css'),
        encoding="utf-8",
    )

sources_body = f'''
<section class="page-intro">
<span class="eyebrow">Evidence library</span>
<h1>Sources</h1>
<p class="lead">Browse the source set attached to each published State and Union Territory research record. Source provenance, findings, grades and verification status are preserved.</p>
</section>
<section class="section"><div class="grid">{''.join(source_cards)}</div></section>
'''
WEB.joinpath("sources.html").write_text(shell("Sources", "Sources", sources_body), encoding="utf-8")

methodology_body = '''
<section class="page-intro">
<span class="eyebrow">Research methodology</span>
<h1>How the evidence is handled.</h1>
<p class="lead">The research separates legal authority, administrative evidence, historical reporting and unresolved questions.</p>
</section>
<section class="grid">
<article class="card"><h3>Primary-source preference</h3><p>Constitutional text, legislation, Rules, Gazettes, Government orders, judgments, Parliament and official statistics are preferred.</p></article>
<article class="card"><h3>Evidence grades</h3><p>A is primary authoritative evidence. B is strong official or credible evidence. C is reliable secondary evidence. D is weak or unverified material and is never the sole basis of a major conclusion.</p></article>
<article class="card"><h3>Currentness</h3><p>Historical reports remain tied to their reporting period. A current webpage does not silently replace an underlying appointment, notification or establishment instrument.</p></article>
<article class="card"><h3>Conflicts</h3><p>Conflicting authoritative records are preserved and escalated where no controlling later instrument or judgment resolves the issue. Search silence is not treated as legal absence.</p></article>
<article class="card"><h3>Jurisdictional separation</h3><p>State and Union Territory arrangements are researched independently. One jurisdiction is not treated as representative of another.</p></article>
<article class="card"><h3>Traceability</h3><p>Material research propositions retain source identifiers or source provenance so readers can trace the evidence back to the repository record.</p></article>
</section>
'''
WEB.joinpath("methodology.html").write_text(shell("Methodology", "Methodology", methodology_body), encoding="utf-8")

WEB.joinpath("404.html").write_text(
    shell("Page not found", "", """
<section class="page-intro">
<span class="eyebrow">Research library</span>
<h1>Page not found.</h1>
<p class="lead">The requested research page does not exist in the current published site.</p>
<div class="actions"><a class="btn primary" href="index.html">Return to research home</a><a class="btn secondary" href="states.html">Browse States & UTs</a></div>
</section>
"""),
    encoding="utf-8",
)
WEB.joinpath("robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")

all_pages = sorted(p.relative_to(WEB).as_posix() for p in WEB.rglob("*.html"))
sitemap = ["<?xml version=\"1.0\" encoding=\"UTF-8\"?>", '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for page in all_pages:
    sitemap.append(f"  <url><loc>{html.escape(page)}</loc></url>")
sitemap.append("</urlset>")
WEB.joinpath("sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")

for name, _, _ in completed:
    if not WEB.joinpath("states", f"{slug(name)}.html").exists():
        raise RuntimeError(f"Missing generated State/UT page: {name}")

print(f"Built {len(all_pages)} HTML pages from {len(completed)} jurisdiction records and {len(source_rows)} master source rows.")
