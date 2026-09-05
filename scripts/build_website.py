#!/usr/bin/env python3
"""Build the public static research site from authoritative repository data."""
from pathlib import Path
import html
import re

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "website"
INV = ROOT / "legislation/STATE_IMPLEMENTATION_INVENTORY.md"
MASTER = ROOT / "research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md"
STATE_DIR = ROOT / "legislation/states"

NAV = [
    ("Research", "research.html"),
    ("States & UTs", "states.html"),
    ("Existing Law", "law.html"),
    ("Sources", "sources.html"),
    ("Methodology", "methodology.html"),
]


def parse_inventory():
    rows = []
    active = False
    for line in INV.read_text(encoding="utf-8").splitlines():
        if line.strip() == "| Jurisdiction | Status | First-pass record |":
            active = True
            continue
        if not active:
            continue
        if line.strip() == "|---|---|---|":
            continue
        m = re.match(r"^\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*`?([^|`]+?)`?\s*\|$", line)
        if m:
            name, status, path = m.groups()
            rows.append((name.strip(), status.strip(), path.strip()))
        elif line.strip() and not line.lstrip().startswith("|"):
            break
    return rows


def source_count():
    text = MASTER.read_text(encoding="utf-8")
    # Count source IDs, not Markdown table-header rows.
    return len(re.findall(r"^\|\s*[A-Z0-9]+-[A-Z0-9_-]+\s*\|", text, flags=re.M))


def nav_html(active):
    return "".join(
        f'<a class="nav-link {"active" if label == active else ""}" href="{href}">{label}</a>'
        for label, href in NAV
    )


def shell(title, active, body, extra_script=""):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Evidence-first research on India's caste-atrocity legal and implementation framework.">
<title>{html.escape(title)} | Universal Caste Atrocities Act Research</title>
<link rel="stylesheet" href="assets/site.css?v=20260906">
</head>
<body>
<header class="topbar"><div class="shell nav"><a class="brand" href="index.html">Universal Caste Atrocities Act</a><nav class="navlinks" aria-label="Primary">{nav_html(active)}</nav></div></header>
<main class="shell main">{body}</main>
<footer><div class="shell footergrid"><div><strong>Universal Caste Atrocities Act Research</strong><p>Evidence-first public research. GitHub is the authoritative project record.</p></div><div class="smalllinks"><a href="research.html">Research</a><a href="states.html">States & UTs</a><a href="sources.html">Sources</a></div><div class="smalllinks"><a href="methodology.html">Methodology</a><a href="law.html">Existing Law</a><a href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act">GitHub</a></div></div></footer>
{extra_script}</body></html>'''


states = parse_inventory()
completed = [r for r in states if "NOT STARTED" not in r[1]]
unresearched = [r for r in states if "NOT STARTED" in r[1]]
source_total = source_count()

cards = []
for name, status, path in states:
    is_open = "NOT STARTED" in status
    label = "Unresearched" if is_open else ("Close with limitations" if "LIMITATIONS" in status else "Inventoried")
    target = "https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/" + path if not is_open else "#"
    cards.append(f'''<article class="state-card" data-status="{html.escape(status)}" data-name="{html.escape(name.lower())}">
<div class="state-top"><span class="status-dot {'open' if is_open else 'done'}"></span><span class="chip">{html.escape(label)}</span></div>
<h3>{html.escape(name)}</h3><p>{html.escape(status)}</p>
{'<a class="text-link" href="'+target+'">Open jurisdiction record →</a>' if not is_open else '<span class="muted">Sequenced later, deliberately unresearched</span>'}
</article>''')

index_body = f'''
<section class="hero-grid">
<div class="hero-copy"><span class="eyebrow">Phase 1 · Existing-law baseline</span><h1>Evidence before legislation.</h1><p class="lead">A version-controlled examination of India's caste-atrocity law, implementation machinery and source record. The research does not presume replacement, reform, necessity or superiority.</p><div class="actions"><a class="btn primary" href="research.html">Open research dashboard</a><a class="btn secondary" href="states.html">Browse all jurisdictions</a></div></div>
<aside class="hero-panel"><div><div class="panel-label">Jurisdiction coverage</div><div class="hero-number">{len(completed)}<span> / {len(states)}</span></div><p>States and Union Territories with substantive Phase 1 inventories.</p><div class="progress"><i></i></div><div class="panel-meta"><span>33 inventoried</span><span>3 unresearched</span></div></div><p>Control position: ACTIVE. Substantive Phase 1 acceptance is not yet satisfied.</p></aside>
</section>
<section class="section"><div class="metric-grid">
<div class="metric-card"><span>Source IDs</span><strong>{source_total}</strong><small>master State Implementation Source Ledger</small></div>
<div class="metric-card"><span>Control status</span><strong>PASS</strong><small>master-ledger zero-drift control</small></div>
<div class="metric-card"><span>Remaining</span><strong>{len(unresearched)}</strong><small>Ladakh, Lakshadweep, Puducherry</small></div>
<div class="metric-card"><span>Bill drafting</span><strong>Deferred</strong><small>prerequisite research first</small></div>
</div></section>
<section class="section"><div class="section-head"><div><div class="section-kicker">Current gate</div><h2>Control remediation is closed.</h2></div><span class="chip">06 Sep 2026</span></div><div class="control-grid">
<div class="control-card"><span>01 · Inventory</span><strong>33 / 36 reconciled</strong><p>Every completed jurisdiction is indexed against its substantive artifact.</p></div>
<div class="control-card"><span>02 · Sources</span><strong>{source_total} source IDs</strong><p>Later jurisdiction-ledger rows were integrated without renumbering prior IDs.</p></div>
<div class="control-card"><span>03 · Integrity</span><strong>Zero drift: PASS</strong><p>Committed master content was independently read back after integration.</p></div>
</div></section>
<section class="section"><div class="section-head"><div><div class="section-kicker">Research architecture</div><h2>Follow the evidence.</h2></div></div><div class="grid">
<a class="card feature-card" href="research.html"><span class="index">01</span><div><h3>Research dashboard</h3><p>Current phase, controls, residuals and authorized sequencing.</p></div></a>
<a class="card feature-card" href="states.html"><span class="index">02</span><div><h3>States & UTs</h3><p>Jurisdiction-specific implementation records with qualifications preserved.</p></div></a>
<a class="card feature-card" href="law.html"><span class="index">03</span><div><h3>Existing law</h3><p>SC/ST Act and Rules, PCR, BNS, BNSS, BSA and related interfaces.</p></div></a>
<a class="card feature-card" href="sources.html"><span class="index">04</span><div><h3>Evidence library</h3><p>Source families, provenance and master-ledger coverage.</p></div></a>
<a class="card feature-card" href="methodology.html"><span class="index">05</span><div><h3>Methodology</h3><p>Evidence grades, currentness, conflict resolution and stopping rules.</p></div></a>
<a class="card feature-card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act"><span class="index">06</span><div><h3>Authoritative record</h3><p>GitHub remains the version-controlled source of project state.</p></div></a>
</div></section>
<section class="section frontier"><div class="frontier-main"><span class="eyebrow">Controlled frontier</span><h2>Three jurisdictions remain deliberately unresearched.</h2><p>They are preserved in the control layer and are not started automatically. A new jurisdictional workstream requires explicit authorization.</p></div><div class="frontier-list">{''.join(f'<div class="frontier-item"><strong>{html.escape(n)}</strong><span>Not started</span></div>' for n,_,_ in unresearched)}</div></section>
'''
WEB.joinpath("index.html").write_text(shell("Research home", "", index_body), encoding="utf-8")

states_body = f'''
<section class="page-intro"><span class="eyebrow">Jurisdiction control surface</span><h1>States & Union Territories</h1><p class="lead">{len(completed)} of {len(states)} jurisdictions have substantive Phase 1 inventories. Status labels preserve qualifications and do not imply a complete 2026 census.</p></section>
<section class="toolbar"><label class="searchbox"><span>Search jurisdictions</span><input id="stateSearch" type="search" placeholder="e.g. Kerala, Delhi, Jammu" autocomplete="off"></label><div class="filter-row"><button class="filter active" data-filter="all">All</button><button class="filter" data-filter="completed">Inventoried</button><button class="filter" data-filter="open">Unresearched</button></div></section>
<section class="state-grid" id="stateGrid">{''.join(cards)}</section><p class="empty" id="emptyState" hidden>No jurisdictions match the current filter.</p>
'''
extra = '''<script>
const search=document.getElementById('stateSearch'),empty=document.getElementById('emptyState');let filter='all';
function render(){const q=search.value.toLowerCase().trim();let shown=0;document.querySelectorAll('.state-card').forEach(c=>{const open=c.querySelector('.status-dot').classList.contains('open');const okFilter=filter==='all'||(filter==='open'&&open)||(filter==='completed'&&!open);const okSearch=c.dataset.name.includes(q);c.hidden=!(okFilter&&okSearch);if(!c.hidden)shown++;});empty.hidden=shown!==0;}
search.addEventListener('input',render);document.querySelectorAll('.filter').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.filter').forEach(x=>x.classList.remove('active'));b.classList.add('active');filter=b.dataset.filter;render();}));
</script>'''
WEB.joinpath("states.html").write_text(shell("States & UTs", "States & UTs", states_body, extra), encoding="utf-8")

research_body = f'''
<section class="page-intro"><span class="eyebrow">Project dashboard</span><h1>Research control position</h1><p class="lead">Phase 1 remains active. The project is evidence-first and does not presume the desirability, necessity or constitutionality of a replacement statute.</p></section>
<section class="metric-grid"><div class="metric-card"><span>Phase</span><strong>1</strong><small>Existing-law baseline and source map</small></div><div class="metric-card"><span>Coverage</span><strong>{len(completed)}/{len(states)}</strong><small>substantive State/UT inventories</small></div><div class="metric-card"><span>Sources</span><strong>{source_total}</strong><small>master source IDs</small></div><div class="metric-card"><span>Acceptance</span><strong>Pending</strong><small>substantive criteria not yet satisfied</small></div></section>
<section class="section split"><div class="card"><div class="section-kicker">Completed control task</div><h2>Master source-ledger reconciliation</h2><ul class="clean-list"><li>Later jurisdiction-specific source rows integrated.</li><li>Existing source IDs preserved.</li><li>No cumulative IDs fabricated or renumbered.</li><li>No jurisdiction reopened.</li></ul></div><div class="callout"><strong>Closed restrictions</strong><p>No Ladakh, Lakshadweep or Puducherry research in this workstream. No Bill drafting. No policy-superiority or necessity analysis. No constitutional-validity analysis. No Phase 2 case-law research.</p></div></section>
<section class="section frontier"><div class="frontier-main"><span class="eyebrow">Current gate</span><h2>Preserve the control baseline.</h2><p>The master State Implementation Inventory and master source ledger are reconciled. The remaining substantive Phase 1 work is separate from this closed control task.</p></div><div class="frontier-list"><div class="frontier-item"><strong>Central current-law completeness</strong><span>Open</span></div><div class="frontier-item"><strong>BNS / BNSS / BSA transition verification</strong><span>Open</span></div><div class="frontier-item"><strong>State currentness residuals</strong><span>Open</span></div></div></section>
'''
WEB.joinpath("research.html").write_text(shell("Research dashboard", "Research", research_body), encoding="utf-8")

law_body = '''
<section class="page-intro"><span class="eyebrow">Existing law</span><h1>Legal framework mapped so far.</h1><p class="lead">A navigation layer over the repository's existing-law research. This is not a legislative proposal and does not state a constitutional conclusion.</p></section>
<div class="grid"><a class="card feature-card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/SCST_ACT_CLAUSE_EXTRACTION.md"><span class="index">01</span><div><h3>SC/ST PoA Act</h3><p>Clause-level extraction and amendment provenance.</p></div></a><a class="card feature-card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/SCST_RULES_CLAUSE_EXTRACTION.md"><span class="index">02</span><div><h3>SC/ST PoA Rules</h3><p>Rules, Schedule and Annexure inventory with source qualifications.</p></div></a><a class="card feature-card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/SCST_ACT_SECTION3_BNS_CROSSWALK.md"><span class="index">03</span><div><h3>BNS crosswalk</h3><p>Section 3 conduct mapped to current criminal-law correspondence classes.</p></div></a><a class="card feature-card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/SCST_ACT_BNSS_PROCEDURAL_CROSSWALK.md"><span class="index">04</span><div><h3>BNSS interface</h3><p>Procedure, courts, investigation, appeals and transition interfaces.</p></div></a><a class="card feature-card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/SCST_ACT_BSA_EVIDENCE_PRESUMPTION_CROSSWALK.md"><span class="index">05</span><div><h3>BSA interface</h3><p>Evidence, burden and statutory-presumption architecture.</p></div></a><a class="card feature-card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/PCR_ACT_RULES_SECTION_RULE_COMPARISON.md"><span class="index">06</span><div><h3>Protection of Civil Rights</h3><p>Section/rule comparison and interaction with the PoA framework.</p></div></a><a class="card feature-card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/MANUAL_SCAVENGERS_ACT_RULES_SCST_CROSSWALK.md"><span class="index">07</span><div><h3>Manual Scavengers law</h3><p>Prohibitions, rehabilitation, trial and institutional interfaces.</p></div></a><a class="card feature-card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/BONDED_LABOUR_ACT_RULES_SCST_CROSSWALK.md"><span class="index">08</span><div><h3>Bonded Labour law</h3><p>Overlap and distinctions with atrocity-related coercion and relief.</p></div></a></div>
'''
WEB.joinpath("law.html").write_text(shell("Existing law", "Existing Law", law_body), encoding="utf-8")

sources_body = f'''
<section class="page-intro"><span class="eyebrow">Evidence library</span><h1>Source coverage.</h1><p class="lead">The public interface exposes the source architecture without replacing the repository's substantive records.</p></section>
<section class="metric-grid"><div class="metric-card"><span>Master source IDs</span><strong>{source_total}</strong><small>after controlled integration</small></div><div class="metric-card"><span>Dedicated ledgers</span><strong>{len(list(STATE_DIR.glob('*_SOURCE_LEDGER.md')))}</strong><small>jurisdiction ledgers in repository</small></div><div class="metric-card"><span>Evidence priority</span><strong>A</strong><small>primary authoritative sources preferred</small></div><div class="metric-card"><span>Search rule</span><strong>Controlled</strong><small>silence is not absence</small></div></section>
<section class="section"><h2>Primary source families</h2><div class="tag-cloud"><span>Constitution</span><span>Central Acts & Rules</span><span>State Acts & Rules</span><span>Gazettes</span><span>Supreme Court / High Courts</span><span>Parliament / Digital Sansad</span><span>Government reports</span><span>NCRB / BPRD</span><span>Police & Prosecution records</span><span>Budgets & administrative records</span></div></section>
<section class="section callout"><strong>Traceability rule</strong><p>Each material proposition must be traceable to a source. Evidence grade is independent of source hierarchy. A source's existence does not prove every proposition attributed to it.</p><p class="source-note">Master ledger control: 261 source IDs. Control-remediation and zero-drift verification are closed for the current workstream.</p></section>
'''
WEB.joinpath("sources.html").write_text(shell("Sources", "Sources", sources_body), encoding="utf-8")

method_body = '''
<section class="page-intro"><span class="eyebrow">Methodology</span><h1>How the evidence is controlled.</h1><p class="lead">The project separates task completion, evidentiary verification, currentness and unresolved limitations. No single label silently upgrades another.</p></section>
<section class="section"><div class="grid"><article class="card"><h3>A · Primary authoritative</h3><p>Constitution, legislation, Rules, Gazette instruments, judgments and authoritative Government records.</p></article><article class="card"><h3>B · Strong official / credible</h3><p>Official reports, institutional records and reliable corroboration with defined scope.</p></article><article class="card"><h3>C · Reliable secondary</h3><p>Used for leads, context or corroboration where primary retrieval is unavailable.</p></article></div></section>
<section class="section control-grid"><article class="control-card"><span>Control 01</span><strong>Currentness</strong><p>Historical reports remain tied to their reporting period. They do not become current through search silence.</p></article><article class="control-card"><span>Control 02</span><strong>Conflicts</strong><p>Higher-authority and later operative instruments control where scope and date are comparable.</p></article><article class="control-card"><span>Control 03</span><strong>Reopening</strong><p>Completed work reopens only for material new evidence, a substantive source error, a control defect or authorized closure work.</p></article></section>
<section class="section"><div class="callout"><strong>Universal stopping rule</strong><p>Research stops only on verified resolution, controlled negative result, access/retrieval block, unresolved conflict requiring escalation, or satisfied scope. Search silence never proves legal absence.</p></div></section>
'''
WEB.joinpath("methodology.html").write_text(shell("Methodology", "Methodology", method_body), encoding="utf-8")
