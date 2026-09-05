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
        if active:
            if line.strip() == "|---|---|---|":
                continue
            m = re.match(r"^\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*`?([^|`]+?)`?\s*\|$", line)
            if m:
                name, status, path = m.groups()
                rows.append((name, status, path.strip()))
            elif line.strip() and not line.lstrip().startswith("|"):
                break
    return rows

def source_count():
    text = MASTER.read_text(encoding="utf-8")
    return len(re.findall(r"^\|\s*[A-Za-z0-9_-]+\s*\|", text, flags=re.M))

def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")

def nav_html(active):
    return "".join(f'<a class="nav-link {"active" if label == active else ""}" href="{href}">{label}</a>' for label, href in NAV)

def shell(title, active, body, extra_script=""):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Evidence-first research on India's caste-atrocity legal and implementation framework.">
<title>{html.escape(title)} | Universal Caste Atrocities Act Research</title>
<link rel="stylesheet" href="assets/site.css">
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
  <aside class="hero-panel"><div class="panel-label">Control position</div><strong>ACTIVE</strong><p>Substantive Phase 1 acceptance is not yet satisfied.</p><div class="mini-rule"></div><p>Master source ledger: {source_total} verified source rows indexed.</p></aside>
</section>
<section class="section"><div class="metric-grid">
  <div class="metric-card"><span>Jurisdictions</span><strong>{len(completed)}/{len(states)}</strong><small>inventoried</small></div>
  <div class="metric-card"><span>Unresearched</span><strong>{len(unresearched)}</strong><small>Ladakh, Lakshadweep, Puducherry</small></div>
  <div class="metric-card"><span>Source rows</span><strong>{source_total}</strong><small>master State ledger</small></div>
  <div class="metric-card"><span>Bill drafting</span><strong>Deferred</strong><small>prerequisite research first</small></div>
</div></section>
<section class="section"><div class="section-head"><div><span class="eyebrow">Current gate</span><h2>Control remediation</h2></div><span class="chip">2026-09-06</span></div><div class="callout"><strong>Master source-ledger integration completed.</strong><p>The later jurisdiction-specific rows were integrated without renumbering source IDs. Independent zero-drift verification is the control checkpoint. No new jurisdiction research is authorized by this page.</p></div></section>
<section class="section"><div class="section-head"><div><span class="eyebrow">Research map</span><h2>What the site exposes</h2></div></div><div class="grid"><a class="card" href="research.html"><h3>Research dashboard</h3><p>Current phase, controls, residuals and next authorized workstream.</p></a><a class="card" href="states.html"><h3>State & UT inventory</h3><p>33 completed jurisdiction records, plus three explicitly unresearched jurisdictions.</p></a><a class="card" href="law.html"><h3>Existing legal framework</h3><p>SC/ST Act and Rules, PCR, BNS, BNSS, BSA and related interfaces.</p></a><a class="card" href="sources.html"><h3>Evidence library</h3><p>Primary-source families, source-ledger coverage and repository traceability.</p></a><a class="card" href="methodology.html"><h3>Methodology</h3><p>Evidence grades, currentness, conflict resolution, reopening and zero-drift controls.</p></a><a class="card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act"><h3>Authoritative record</h3><p>GitHub remains the source of truth for project state and version history.</p></a></div></section>
'''
WEB.joinpath("index.html").write_text(shell("Research home", "", index_body), encoding="utf-8")

states_body = f'''
<section class="page-intro"><span class="eyebrow">Jurisdiction control surface</span><h1>States & Union Territories</h1><p class="lead">{len(completed)} of {len(states)} jurisdictions have substantive Phase 1 inventories. Status labels preserve qualifications and do not imply a complete 2026 census.</p></section>
<section class="toolbar"><label class="searchbox"><span>Search jurisdictions</span><input id="stateSearch" type="search" placeholder="e.g. Kerala, Delhi, Jammu" autocomplete="off"></label><div class="filter-row"><button class="filter active" data-filter="all">All</button><button class="filter" data-filter="completed">Inventoried</button><button class="filter" data-filter="open">Unresearched</button></div></section>
<section class="state-grid" id="stateGrid">{''.join(cards)}</section>
<p class="empty" id="emptyState" hidden>No jurisdictions match the current filter.</p>
'''
extra = '''<script>
const search=document.getElementById('stateSearch'), grid=document.getElementById('stateGrid'), empty=document.getElementById('emptyState');
let filter='all';
function render(){const q=search.value.toLowerCase().trim();let shown=0;document.querySelectorAll('.state-card').forEach(c=>{const open=c.querySelector('.status-dot').classList.contains('open');const okFilter=filter==='all'||(filter==='open'&&open)||(filter==='completed'&&!open);const okSearch=c.dataset.name.includes(q);c.hidden=!(okFilter&&okSearch);if(!c.hidden)shown++;});empty.hidden=shown!==0;}
search.addEventListener('input',render);document.querySelectorAll('.filter').forEach(b=>b.addEventListener('click',()=>{document.querySelectorAll('.filter').forEach(x=>x.classList.remove('active'));b.classList.add('active');filter=b.dataset.filter;render();}));
</script>'''
WEB.joinpath("states.html").write_text(shell("States & UTs", "States & UTs", states_body, extra), encoding="utf-8")

research_body = f'''
<section class="page-intro"><span class="eyebrow">Project dashboard</span><h1>Research control position</h1><p class="lead">Phase 1 remains active. The project is evidence-first and does not presume the desirability, necessity or constitutionality of a replacement statute.</p></section>
<section class="metric-grid"><div class="metric-card"><span>Phase</span><strong>1</strong><small>Existing-law baseline and source map</small></div><div class="metric-card"><span>State/UT coverage</span><strong>{len(completed)}/{len(states)}</strong><small>substantive inventories</small></div><div class="metric-card"><span>Source ledger</span><strong>{source_total}</strong><small>master source rows</small></div><div class="metric-card"><span>Acceptance</span><strong>Pending</strong><small>substantive criteria not yet satisfied</small></div></section>
<section class="section split"><div><span class="eyebrow">Completed control task</span><h2>Master source-ledger reconciliation</h2><ul class="clean-list"><li>Later jurisdiction-specific source rows integrated.</li><li>Existing source IDs preserved.</li><li>No cumulative IDs fabricated or renumbered.</li><li>No jurisdiction reopened.</li></ul></div><div class="callout"><strong>Closed restrictions</strong><p>No Ladakh, Lakshadweep or Puducherry research in this workstream. No Bill drafting. No policy-superiority or necessity analysis. No constitutional-validity analysis. No Phase 2 case-law research.</p></div></section>
<section class="section"><span class="eyebrow">Next authorized workstream</span><h2>Control closure, then substantive sequencing</h2><p>Maintain the reconciled State inventory and master source ledger as the control baseline. Preserve all jurisdiction-specific residuals. The next substantive jurisdiction remains Ladakh, but it is not authorized until the control-remediation gate is closed.</p></section>
'''
WEB.joinpath("research.html").write_text(shell("Research dashboard", "Research", research_body), encoding="utf-8")

law_body = '''
<section class="page-intro"><span class="eyebrow">Existing law</span><h1>Legal framework mapped so far</h1><p class="lead">This page is a navigation layer over the repository's existing-law research. It is not a legislative proposal and does not state a constitutional conclusion.</p></section>
<div class="grid"><a class="card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/SCST_ACT_CLAUSE_EXTRACTION.md"><h3>SC/ST PoA Act</h3><p>Clause-level extraction and amendment provenance.</p></a><a class="card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/SCST_RULES_CLAUSE_EXTRACTION.md"><h3>SC/ST PoA Rules</h3><p>Rules, Schedule and Annexure inventory with source qualifications.</p></a><a class="card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/SCST_ACT_SECTION3_BNS_CROSSWALK.md"><h3>BNS crosswalk</h3><p>Section 3 conduct mapped to current criminal-law correspondence classes.</p></a><a class="card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/SCST_ACT_BNSS_PROCEDURAL_CROSSWALK.md"><h3>BNSS interface</h3><p>Procedure, courts, investigation, appeals and transition interfaces.</p></a><a class="card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/SCST_ACT_BSA_EVIDENCE_PRESUMPTION_CROSSWALK.md"><h3>BSA interface</h3><p>Evidence, burden and statutory-presumption architecture.</p></a><a class="card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/PCR_ACT_RULES_SECTION_RULE_COMPARISON.md"><h3>Protection of Civil Rights</h3><p>Section/rule comparison and interaction with the PoA framework.</p></a><a class="card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/MANUAL_SCAVENGERS_ACT_RULES_SCST_CROSSWALK.md"><h3>Manual Scavengers law</h3><p>Prohibitions, rehabilitation, trial and institutional interfaces.</p></a><a class="card" href="https://github.com/Ashish-Bhatia/Universal-Caste-Atrocities-Act/blob/main/legislation/BONDED_LABOUR_ACT_RULES_SCST_CROSSWALK.md"><h3>Bonded Labour law</h3><p>Overlap and distinctions with atrocity-related coercion and relief.</p></a></div>
'''
WEB.joinpath("law.html").write_text(shell("Existing law", "Existing Law", law_body), encoding="utf-8")

sources_body = f'''
<section class="page-intro"><span class="eyebrow">Evidence library</span><h1>Source coverage</h1><p class="lead">The public interface exposes the source architecture without replacing the repository's substantive records.</p></section>
<section class="metric-grid"><div class="metric-card"><span>Master source rows</span><strong>{source_total}</strong><small>after controlled integration</small></div><div class="metric-card"><span>Jurisdiction ledgers</span><strong>{len(list(STATE_DIR.glob('*_SOURCE_LEDGER.md')))}</strong><small>dedicated ledgers currently present</small></div><div class="metric-card"><span>Evidence priority</span><strong>A</strong><small>primary authoritative sources preferred</small></div><div class="metric-card"><span>Search rule</span><strong>Controlled</strong><small>silence is not absence</small></div></section>
<section class="section"><h2>Primary source families</h2><div class="tag-cloud"><span>Constitution</span><span>Central Acts & Rules</span><span>State Acts & Rules</span><span>Gazettes</span><span>Supreme Court / High Courts</span><span>Parliament / Digital Sansad</span><span>Government reports</span><span>NCRB / BPRD</span><span>Police & Prosecution records</span><span>Budgets & administrative records</span></div></section>
<section class="section callout"><strong>Traceability rule</strong><p>Every material factual, legal or statistical proposition is expected to retain a traceable source. Secondary material is used for leads or corroboration where primary material is unavailable. Weak or unverified material is never the sole basis for a major conclusion.</p></section>
'''
WEB.joinpath("sources.html").write_text(shell("Sources", "Sources", sources_body), encoding="utf-8")

method_body = '''
<section class="page-intro"><span class="eyebrow">Methodology</span><h1>Evidence and control rules</h1><p class="lead">The project separates evidence, currentness, task completion and unresolved questions.</p></section>
<div class="grid"><article class="card"><h3>Evidence grades</h3><p>A = primary authoritative. B = strong official/credible. C = reliable secondary. D = weak/unverified. D-grade material is never the sole basis for a major conclusion.</p></article><article class="card"><h3>Currentness</h3><p>A historical report remains valid for its reporting period. It is not silently promoted into a 2026 census.</p></article><article class="card"><h3>Conflict resolution</h3><p>Prefer the higher-authority source. For equal authority, prefer the later operative instrument for current status. Preserve unresolved conflicts as open issues.</p></article><article class="card"><h3>Search stopping</h3><p>Stop only after verified resolution, a controlled negative result, an access/retrieval block, a conflict requiring escalation, or a satisfied scope.</p></article><article class="card"><h3>Reopening</h3><p>Do not reopen a completed jurisdiction for a control-layer defect alone. Reopen only for new authoritative evidence, a material source error, an unreliable substantive artifact, incomplete original scope, or an authorized targeted closure task.</p></article><article class="card"><h3>Zero drift</h3><p>Master indexes must preserve existing IDs, avoid fabricated cumulative IDs and retain traceability to jurisdiction-specific substantive records.</p></article></div>
'''
WEB.joinpath("methodology.html").write_text(shell("Methodology", "Methodology", method_body), encoding="utf-8")

print(f"Built website from {len(states)} jurisdictions and {source_total} master source rows")
