#!/usr/bin/env python3
"""Production website builder with controlled jurisdiction-ledger fallback."""
from pathlib import Path
import html
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
WEB = ROOT / "website"
INV = ROOT / "legislation" / "STATE_IMPLEMENTATION_INVENTORY.md"
MASTER = ROOT / "research" / "STATE_IMPLEMENTATION_SOURCE_LEDGER.md"
SOURCE_DIR = ROOT / "research" / "states"
LAW_DOCS = [("SC/ST Prevention of Atrocities Act", "SCST_ACT_CLAUSE_EXTRACTION.md", "Clause-level Act extraction and amendment provenance."), ("SC/ST Prevention of Atrocities Rules", "SCST_RULES_CLAUSE_EXTRACTION.md", "Rules, Schedule and Annexure inventory."), ("SC/ST Act, BNS crosswalk", "SCST_ACT_SECTION3_BNS_CROSSWALK.md", "Section 3 conduct and Schedule correspondence with BNS."), ("SC/ST Act, BNSS crosswalk", "SCST_ACT_BNSS_PROCEDURAL_CROSSWALK.md", "Procedural interfaces and transition questions."), ("SC/ST Act, BSA crosswalk", "SCST_ACT_BSA_EVIDENCE_PRESUMPTION_CROSSWALK.md", "Evidence, burden and statutory-presumption interfaces."), ("Protection of Civil Rights Act and Rules", "PCR_ACT_RULES_SECTION_RULE_COMPARISON.md", "Section/rule comparison with the PoA framework."), ("Manual Scavengers Act and Rules", "MANUAL_SCAVENGERS_ACT_RULES_SCST_CROSSWALK.md", "Prohibition, rehabilitation and related-law interfaces."), ("Bonded Labour Act and Rules", "BONDED_LABOUR_ACT_RULES_SCST_CROSSWALK.md", "Bonded-labour protections and PoA overlap."), ("Priority Central legislation screening", "CENTRAL_LEGISLATION_PRIORITY_SCREENING.md", "Screening of additional Central-law interfaces.")]
NAV = [("Research", "research.html"), ("States & UTs", "states.html"), ("Existing Law", "law.html"), ("Sources", "sources.html"), ("Methodology", "methodology.html")]
ID_RE = re.compile(r"^[A-Z0-9][A-Z0-9_-]*-[A-Z0-9][A-Z0-9_-]*$")

def slug(value): return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "page"

def md_inline(value):
    value = html.escape(value, quote=False)
    value = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" rel="noopener noreferrer">\1</a>', value)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", value)

def md_html(text):
    out=[]; para=[]; bullets=[]
    def fp():
        nonlocal para
        if para: out.append(f"<p>{md_inline(' '.join(para))}</p>"); para=[]
    def fb():
        nonlocal bullets
        if bullets: out.append("<ul>"+"".join(f"<li>{md_inline(x)}</li>" for x in bullets)+"</ul>"); bullets=[]
    def table_block(block):
        rows=[]
        for line in block:
            cells=[c.strip() for c in line.strip().strip('|').split('|')]
            if cells: rows.append(cells)
        if len(rows)<2: return None
        header=rows[0]; separator=rows[1]
        is_sep=all(re.fullmatch(r':?-{3,}:?', c.replace(' ','')) for c in separator)
        body=rows[2:] if is_sep else rows[1:]
        html_out=['<div class="tablewrap"><table class="table"><thead><tr>']
        html_out.extend(f"<th>{md_inline(c)}</th>" for c in header); html_out.append('</tr></thead><tbody>')
        for row in body:
            html_out.append('<tr>'); html_out.extend(f"<td>{md_inline(row[i] if i<len(row) else '')}</td>" for i in range(len(header))); html_out.append('</tr>')
        html_out.append('</tbody></table></div>'); return ''.join(html_out)
    lines=text.splitlines(); i=0
    while i<len(lines):
        s=lines[i].strip()
        if s.startswith('|') and s.endswith('|') and i+1<len(lines) and re.fullmatch(r'\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?', lines[i+1].strip()):
            fp(); fb(); block=[lines[i],lines[i+1]]; i+=2
            while i<len(lines) and lines[i].strip().startswith('|') and lines[i].strip().endswith('|'): block.append(lines[i]); i+=1
            rendered=table_block(block)
            if rendered: out.append(rendered)
            continue
        if not s: fp(); fb(); i+=1; continue
        if s.startswith('# '): fp(); fb(); out.append(f"<h2>{md_inline(s[2:])}</h2>"); i+=1; continue
        if s.startswith('## '): fp(); fb(); t=s[3:]; out.append(f'<h2 id="{slug(t)}">{md_inline(t)}</h2>'); i+=1; continue
        if s.startswith('### '): fp(); fb(); out.append(f"<h3>{md_inline(s[4:])}</h3>"); i+=1; continue
        m=re.match(r'^[-*]\s+(.*)$',s)
        if m: fp(); bullets.append(m.group(1)); i+=1; continue
        m=re.match(r'^\d+\.\s+(.*)$',s)
        if m: fp(); bullets.append(m.group(1)); i+=1; continue
        para.append(s); i+=1
    fp(); fb(); return "\n".join(out)

def strip_controls(text):
    out=[]; skip=False
    for line in text.splitlines():
        s=line.strip()
        if re.match(r"^(Status|Phase|Research date|Opened):",s): continue
        if s=="## Disposition": skip=True; continue
        if skip and s.startswith("## "): skip=False
        if skip or "No Bill drafting" in s or "No Phase 2" in s: continue
        out.append(line)
    return "\n".join(out)

def inventory():
    rows=[]; active=False
    for line in INV.read_text(encoding="utf-8").splitlines():
        if line.strip()=="| Jurisdiction | Status | First-pass record |": active=True; continue
        if not active: continue
        if line.strip().startswith("|---"): continue
        m=re.match(r"^\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*`?([^|`]+?)`?\s*\|$",line)
        if m: rows.append(tuple(x.strip() for x in m.groups()))
        elif line.strip() and not line.lstrip().startswith("|"): break
    return rows

def source_rows(text, provenance):
    result=[]; lines=text.splitlines(); i=0
    while i<len(lines):
        if not lines[i].strip().startswith("|"): i+=1; continue
        header=[c.strip().lower() for c in lines[i].strip().strip("|").split("|")]
        if not header or header[0]!="id": i+=1; continue
        i+=2
        while i<len(lines) and lines[i].strip().startswith("|"):
            cells=[c.strip() for c in lines[i].strip().strip("|").split("|")]
            if cells and ID_RE.fullmatch(cells[0]):
                d=dict(zip(header,cells)); result.append({"id":cells[0],"source":d.get("source",""),"finding":d.get("finding",d.get("use",d.get("description",""))),"grade":d.get("grade",""),"verification":d.get("verification status",d.get("verification","")),"provenance":provenance})
            i+=1
    return result

def master_rows_by_jurisdiction(text):
    sections={}; current=None; block=[]
    for line in text.splitlines():
        if line.startswith("## "):
            if current is not None: sections[current]=source_rows("\n".join(block),"master")
            current=line[3:].strip(); block=[]
        else: block.append(line)
    if current is not None: sections[current]=source_rows("\n".join(block),"master")
    return sections

def jurisdiction_master_rows(sections, name):
    target=name.casefold()
    return [row for heading, rows in sections.items() if target in heading.casefold() for row in rows]

def local_ledger(path):
    stem=Path(path).stem; p=SOURCE_DIR/f"{stem}_SOURCE_LEDGER.md"
    if p.exists(): return p
    if stem=="DELHI_NCT" and (SOURCE_DIR/"DELHI_SOURCE_LEDGER.md").exists(): return SOURCE_DIR/"DELHI_SOURCE_LEDGER.md"
    return None

def shell(title, active, body, prefix=""):
    nav="".join(f'<a class="nav-link {"active" if x==active else ""}" href="{prefix}{h}">{x}</a>' for x,h in NAV)
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Evidence-first research on India\'s caste-atrocity legal and implementation framework."><meta name="theme-color" content="#102a43"><title>{html.escape(title)} | Universal Caste Atrocities Act Research</title><link rel="stylesheet" href="{prefix}assets/site.css?v=20260906-4"></head><body><header class="topbar"><div class="shell nav"><a class="brand" href="{prefix}index.html" aria-label="Universal Caste Atrocities Act Research home">Universal Caste Atrocities Act Research</a><nav class="navlinks" aria-label="Primary navigation">{nav}</nav><a class="support-btn" href="{prefix}petition.html">Petition / Support</a></div></header><main class="shell main">{body}</main><footer><div class="shell footergrid"><div><strong>Universal Caste Atrocities Act Research</strong><p>Public research interface. Evidence, source provenance and qualifications are preserved.</p><span class="version">Research baseline: 06 September 2026 · Phase 1</span></div><div><strong>Explore</strong><div class="smalllinks"><a href="{prefix}research.html">Research</a><a href="{prefix}states.html">States & UTs</a><a href="{prefix}law.html">Existing law</a><a href="{prefix}sources.html">Sources</a></div></div><div><strong>Project</strong><div class="smalllinks"><a href="{prefix}bill.html">Bill</a><a href="{prefix}petition.html">Petition / Support</a><a href="{prefix}methodology.html">Methodology</a></div></div></div></footer></body></html>'

def table(rows):
    if not rows: return '<p class="empty">No controlled source rows are available.</p>'
    out=['<div class="tablewrap"><table class="table"><thead><tr><th>Source ID</th><th>Source</th><th>Finding / Use</th><th>Grade</th><th>Verification</th><th>Tier</th></tr></thead><tbody>']
    for r in rows:
        tier="Master ledger" if r["provenance"]=="master" else "Jurisdiction-ledger fallback"
        out.append("<tr>"+"".join(f"<td>{md_inline(x)}</td>" for x in [r["id"],r["source"],r["finding"],r["grade"],r["verification"],tier])+"</tr>")
    return "".join(out)+"</tbody></table></div>"

states=inventory(); completed=[x for x in states if "NOT STARTED" not in x[1]]; total=len(states); completed_count=len(completed)
master_text=MASTER.read_text(encoding="utf-8"); master=source_rows(master_text,"master"); master_ids={x["id"] for x in master}; sections=master_rows_by_jurisdiction(master_text)
local=[]
for p in sorted(SOURCE_DIR.glob("*_SOURCE_LEDGER.md")): local.extend(source_rows(p.read_text(encoding="utf-8"),str(p.relative_to(ROOT))))
local_ids={x["id"] for x in local}; gap=sorted(local_ids-master_ids)
print(f"SOURCE_LEDGER_CONTROL master={len(master_ids)} jurisdiction={len(local_ids)} missing_from_master={len(gap)}")
print("MISSING_FROM_MASTER="+",".join(gap))
WEB.mkdir(parents=True,exist_ok=True)
for p in WEB.glob("*.html"): p.unlink()
for d in (WEB/"states",WEB/"law",WEB/"sources"):
    if d.exists(): shutil.rmtree(d)
    d.mkdir(parents=True)
WEB.joinpath("index.html").write_text(shell("Research home","",f'<section class="hero-grid"><div class="hero-copy"><span class="eyebrow">Public research library</span><h1>Evidence before legislation.</h1><p class="lead">Evidence-first research on India\'s caste-atrocity legal and implementation framework. Sources, qualifications and unresolved questions remain visible.</p><div class="actions"><a class="btn primary" href="states.html">Explore the jurisdictions</a><a class="btn secondary" href="petition.html">Petition / Support</a></div></div><aside class="hero-panel"><div><span class="panel-label">Research baseline</span><div class="hero-number">{completed_count}<span>/{total}</span></div><p>States and Union Territories with substantive Phase 1 inventories.</p></div><div class="panel-note">{total - completed_count} jurisdiction(s) remain outside the completed sequence. The public library does not treat this as a policy or constitutional conclusion.</div></aside></section><section class="section"><div class="section-head"><div><span class="section-kicker">Browse</span><h2>Research library</h2></div></div><div class="grid"><a class="card feature-card" href="states.html"><h3>States & UTs</h3><p>Jurisdiction implementation research with source provenance and qualifications.</p></a><a class="card feature-card" href="law.html"><h3>Existing law</h3><p>Central-law research, crosswalks and related legal interfaces.</p></a><a class="card feature-card" href="sources.html"><h3>Sources</h3><p>Controlled master-ledger and jurisdiction-ledger source sets.</p></a><a class="card feature-card" href="methodology.html"><h3>Methodology</h3><p>Evidence hierarchy, verification and source-control principles.</p></a></div></section>'),encoding="utf-8")
WEB.joinpath("states.html").write_text(shell("States & UTs","States & UTs",'<section class="page-intro"><span class="eyebrow">Jurisdiction research</span><h1>States & Union Territories</h1><p class="lead">Each completed jurisdiction has its own research page. Remaining jurisdictions are not represented as completed research.</p></section><section class="section"><h2>Jurisdiction research records</h2><div class="state-grid">'+"".join(f'<a class="state-card" href="states/{slug(n)}.html"><span class="chip">Research record</span><h3>{html.escape(n)}</h3><p>Implementation inventory and evidence.</p></a>' for n,_,_ in completed)+'</div></section>'),encoding="utf-8")
source_cards=[]
for name,_,state_path in completed:
    raw=(ROOT/state_path).read_text(encoding="utf-8"); master_for_state=jurisdiction_master_rows(sections,name)
    if not master_for_state:
        refs={m.group(1) for m in re.finditer(r"\b([A-Z][A-Z0-9_]*-[A-Z0-9_-]+)\b",raw)}; master_for_state=[row for row in master if row["id"] in refs]
    lp=local_ledger(state_path); lr=source_rows(lp.read_text(encoding="utf-8"),str(lp.relative_to(ROOT))) if lp else []
    combined={row["id"]:row for row in master_for_state}; fallback={}
    for row in lr:
        if row["id"] not in combined: combined[row["id"]]=row; fallback[row["id"]]=row
    if not combined: raise RuntimeError(f"CONTROL FAILURE: completed jurisdiction has no controlled source rows: {name}")
    rows=list(combined.values()); note="" if not fallback else f'<div class="notice"><strong>Controlled fallback:</strong> {len(fallback)} row(s) come from the substantive jurisdiction ledger because their IDs are absent from the master ledger. They are not represented as master-ledger integrations.</div>'
    body=f'<section class="page-intro"><span class="eyebrow">State & UT research</span><h1>{html.escape(name)}</h1></section><section class="section prose-card">{md_html(strip_controls(raw))}</section><section class="section"><h2>Sources cited by this record</h2>{note}{table(rows)}</section>'
    WEB.joinpath("states",f"{slug(name)}.html").write_text(shell(name,"States & UTs",body,"../"),encoding="utf-8")
    sbody=f'<section class="page-intro"><span class="eyebrow">Jurisdiction source set</span><h1>{html.escape(name)}</h1><p>Master-ledger rows and explicitly labelled jurisdiction-ledger fallback rows.</p></section><section class="section">{note}{table(rows)}</section>'
    WEB.joinpath("sources",f"{slug(name)}.html").write_text(shell(f"{name} Sources","Sources",sbody,"../"),encoding="utf-8")
    source_cards.append(f'<a class="card feature-card" href="sources/{slug(name)}.html"><h3>{html.escape(name)}</h3><p>{len(rows)} controlled source rows, {len(fallback)} fallback row(s).</p></a>')
WEB.joinpath("sources.html").write_text(shell("Sources","Sources",'<section class="page-intro"><span class="eyebrow">Evidence library</span><h1>Sources</h1><p class="lead">The public source layer distinguishes master-ledger integration from controlled jurisdiction-ledger fallback.</p></section><section class="section"><h2>Jurisdiction source sets</h2><div class="grid">'+"".join(source_cards)+'</div></section>'),encoding="utf-8")
law_cards=[]
for title,fn,desc in LAW_DOCS:
    p=ROOT/"legislation"/fn
    if not p.exists(): continue
    law_cards.append(f'<a class="card feature-card" href="law/{slug(title)}.html"><h3>{html.escape(title)}</h3><p>{html.escape(desc)}</p></a>')
    body=f'<section class="page-intro"><span class="eyebrow">Existing-law research</span><h1>{html.escape(title)}</h1><p>{html.escape(desc)}</p></section><section class="section prose-card">{md_html(strip_controls(p.read_text(encoding="utf-8")))}</section>'
    WEB.joinpath("law",f"{slug(title)}.html").write_text(shell(title,"Existing Law",body,"../"),encoding="utf-8")
WEB.joinpath("law.html").write_text(shell("Existing Law","Existing Law",'<section class="page-intro"><span class="eyebrow">Legal framework</span><h1>Existing law</h1><p class="lead">Central-law research and interfaces relevant to the existing caste-atrocity framework.</p></section><section class="section"><h2>Central and related legal research</h2><div class="grid">'+"".join(law_cards)+'</div></section>'),encoding="utf-8")
WEB.joinpath("research.html").write_text(shell("Research","Research",'<section class="page-intro"><span class="eyebrow">Public research library</span><h1>Research by subject.</h1></section><section class="section"><h2>Research areas</h2><div class="grid"><a class="card feature-card" href="states.html"><h3>State implementation</h3><p>Jurisdiction-specific evidence and implementation architecture.</p></a><a class="card feature-card" href="law.html"><h3>Existing law</h3><p>Acts, Rules and legal crosswalks.</p></a><a class="card feature-card" href="sources.html"><h3>Source evidence</h3><p>Controlled source provenance and verification status.</p></a></div></section>'),encoding="utf-8")
WEB.joinpath("methodology.html").write_text(shell("Methodology","Methodology",'<section class="page-intro"><span class="eyebrow">Research method</span><h1>Evidence and source control.</h1></section><section class="section"><h2>Research controls</h2><div class="grid"><article class="card"><h3>Primary-source preference</h3><p>Constitutional text, legislation, Rules, Gazettes, Government orders, judgments, Parliament and official statistics are preferred.</p></article><article class="card"><h3>Evidence grades</h3><p>A is primary authoritative evidence. B is strong official or credible evidence. C is reliable secondary evidence. D is weak or unverified material.</p></article><article class="card"><h3>Source-ledger control</h3><p>The master ledger remains distinct from jurisdiction-specific ledgers. Fallback rows are explicitly labelled and never treated as master integrations.</p></article><article class="card"><h3>Currentness</h3><p>Historical reports remain tied to their reporting periods. Search silence is not treated as proof of legal absence.</p></article></div></section>'),encoding="utf-8")
WEB.joinpath("bill.html").write_text(shell("Bill","",'<section class="page-intro"><span class="eyebrow">Public status</span><h1>Bill publication</h1><p class="lead">A final Bill has not been published in the public research library. The public library is preserving the existing-law evidence baseline before a verified draft is released.</p></section><section class="callout"><strong>Publication status</strong><p>The applicable Bill version will be identified when a verified draft is released.</p></section>'),encoding="utf-8")
WEB.joinpath("petition.html").write_text(shell("Petition / Support","",'<section class="page-intro"><span class="eyebrow">Public participation</span><h1>Petition / Support</h1><p class="lead">The public research library provides the petition pathway without collecting personal information here.</p></section><section class="section"><h2>Participation status</h2><div class="split"><article class="card"><h3>Current status</h3><p>A public petition collection mechanism has not yet been configured. No personal information is requested or stored through this static site.</p></article><article class="card"><h3>What will be published</h3><p>When the petition is opened, this page will identify the request, applicable research or Bill version, responsible recipient and privacy/data-handling terms.</p></article></div></section>'),encoding="utf-8")
WEB.joinpath("404.html").write_text(shell("Page not found","",'<section class="page-intro"><span class="eyebrow">404</span><h1>Page not found.</h1><p class="lead">Use the navigation to return to the public research library.</p><a class="btn primary" href="index.html">Return home</a></section>'),encoding="utf-8")
WEB.joinpath("robots.txt").write_text("User-agent: *\nAllow: /\n",encoding="utf-8")
pages=sorted(p.relative_to(WEB).as_posix() for p in WEB.rglob("*.html"))
WEB.joinpath("sitemap.xml").write_text("\n".join(['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']+[f"<url><loc>{html.escape(p)}</loc></url>" for p in pages]+['</urlset']),encoding="utf-8")
print(f"Built {len(pages)} HTML pages from {len(completed)} jurisdictions; master source rows={len(master)}; fallback IDs available={len(gap)}")