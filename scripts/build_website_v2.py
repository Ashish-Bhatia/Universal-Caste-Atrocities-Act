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
BANNED = ["PROJECT_STATE.md", "NEXT_CHAT.md", "RESEARCH_LEDGER.md", "ISSUES_REGISTER.md", "DECISIONS_LOG.md", "BASELINE_AUDIT.md"]
BANNED_PHRASES = ["modify the project record", "project-control", "project control", "continuation prompt", "no bill drafting", "no phase 2", "through `decisions_log.md`"]
ID_RE = re.compile(r"^[A-Z0-9][A-Z0-9_-]*-[A-Z0-9][A-Z0-9_-]*$")


def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "page"

def md_inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2" rel="noopener noreferrer">\1</a>', s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)

def md_html(text):
    out=[]; para=[]; bullets=[]
    def fp():
        nonlocal para
        if para: out.append(f"<p>{md_inline(' '.join(para))}</p>"); para=[]
    def fb():
        nonlocal bullets
        if bullets: out.append("<ul>"+"".join(f"<li>{md_inline(x)}</li>" for x in bullets)+"</ul>"); bullets=[]
    for raw in text.splitlines():
        s=raw.strip()
        if not s: fp(); fb(); continue
        if s.startswith("# "): fp(); fb(); out.append(f"<h1>{md_inline(s[2:])}</h1>"); continue
        if s.startswith("## "): fp(); fb(); t=s[3:]; out.append(f'<h2 id="{slug(t)}">{md_inline(t)}</h2>'); continue
        if s.startswith("### "): fp(); fb(); out.append(f"<h3>{md_inline(s[4:])}</h3>"); continue
        m=re.match(r"^[-*]\s+(.*)$",s)
        if m: fp(); bullets.append(m.group(1)); continue
        m=re.match(r"^\d+\.\s+(.*)$",s)
        if m: fp(); bullets.append(m.group(1)); continue
        para.append(s)
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

def refs(text): return {m.group(1) for m in re.finditer(r"\b([A-Z][A-Z0-9_]*-[A-Z0-9_-]+)\b",text)}

def local_ledger(path):
    stem=Path(path).stem
    p=SOURCE_DIR/f"{stem}_SOURCE_LEDGER.md"
    if p.exists(): return p
    if stem=="DELHI_NCT" and (SOURCE_DIR/"DELHI_SOURCE_LEDGER.md").exists(): return SOURCE_DIR/"DELHI_SOURCE_LEDGER.md"
    return None

def shell(title, active, body, prefix=""):
    nav="".join(f'<a class="nav-link {"active" if x==active else ""}" href="{prefix}{h}">{x}</a>' for x,h in NAV)
    return f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Evidence-first research on India\'s caste-atrocity legal and implementation framework."><title>{html.escape(title)} | Universal Caste Atrocities Act Research</title><link rel="stylesheet" href="{prefix}assets/site.css?v=20260906-3"></head><body><header class="topbar"><div class="shell nav"><a class="brand" href="{prefix}index.html">Universal Caste Atrocities Act Research</a><nav class="navlinks" aria-label="Primary navigation">{nav}</nav></div></header><main class="shell main">{body}</main><footer><div class="shell footergrid"><div><strong>Universal Caste Atrocities Act Research</strong><p>Public research interface. Evidence, source provenance and qualifications are preserved.</p></div></div></footer></body></html>'

def table(rows):
    if not rows: return '<p class="muted">No controlled source rows are available.</p>'
    out=['<div class="tablewrap"><table class="table"><thead><tr><th>Source ID</th><th>Source</th><th>Finding / Use</th><th>Grade</th><th>Verification</th><th>Tier</th></tr></thead><tbody>']
    for r in rows:
        tier="Master ledger" if r["provenance"]=="master" else "Jurisdiction-ledger fallback"
        out.append("<tr>"+"".join(f"<td>{md_inline(x)}</td>" for x in [r["id"],r["source"],r["finding"],r["grade"],r["verification"],tier])+"</tr>")
    return "".join(out)+"</tbody></table></div>"

states=inventory(); completed=[x for x in states if "NOT STARTED" not in x[1]]
master=source_rows(MASTER.read_text(encoding="utf-8"),"master"); master_ids={x["id"] for x in master}
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
WEB.joinpath("index.html").write_text(shell("Research home","",'<section class="page-intro"><span class="eyebrow">Public research library</span><h1>Evidence before legislation.</h1><p class="lead">Evidence-first research on India\'s caste-atrocity legal and implementation framework.</p></section><section class="grid"><a class="card feature-card" href="states.html"><h3>States & UTs</h3><p>Jurisdiction implementation research.</p></a><a class="card feature-card" href="law.html"><h3>Existing law</h3><p>Central-law research and interfaces.</p></a><a class="card feature-card" href="sources.html"><h3>Sources</h3><p>Source provenance and controlled tiers.</p></a><a class="card feature-card" href="methodology.html"><h3>Methodology</h3><p>Evidence handling and source control.</p></a></section>'),encoding="utf-8")
WEB.joinpath("states.html").write_text(shell("States & UTs","States & UTs",'<section class="page-intro"><span class="eyebrow">Jurisdiction research</span><h1>States & Union Territories</h1></section><section class="state-grid">'+"".join(f'<a class="state-card" href="states/{slug(n)}.html"><h3>{html.escape(n)}</h3><p>Implementation inventory</p></a>' for n,_,_ in completed)+'</section>'),encoding="utf-8")
source_cards=[]
for name,_,state_path in completed:
    raw=(ROOT/state_path).read_text(encoding="utf-8"); lp=local_ledger(state_path); lr=source_rows(lp.read_text(encoding="utf-8"),str(lp.relative_to(ROOT))) if lp else []
    combined={r["id"]:r for r in master if r["id"] in refs(raw)}; fallback={}
    for r in lr:
        if r["id"] not in combined: combined[r["id"]]=r; fallback[r["id"]]=r
    if not combined: raise RuntimeError(f"CONTROL FAILURE: completed jurisdiction has no controlled source rows: {name}")
    rows=list(combined.values()); note="" if not fallback else f'<div class="notice"><strong>Controlled fallback:</strong> {len(fallback)} row(s) come from the substantive jurisdiction ledger because their IDs are absent from the master ledger. They are not represented as master-ledger integrations.</div>'
    body=f'<section class="page-intro"><span class="eyebrow">State & UT research</span><h1>{html.escape(name)}</h1></section><section class="section prose-card">{md_html(strip_controls(raw))}</section><section class="section"><h2>Sources cited by this record</h2>{note}{table(rows)}</section>'
    WEB.joinpath("states",f"{slug(name)}.html").write_text(shell(name,"States & UTs",body,"../"),encoding="utf-8")
    sbody=f'<section class="page-intro"><span class="eyebrow">Jurisdiction source set</span><h1>{html.escape(name)}</h1><p>Master-ledger rows and explicitly labelled jurisdiction-ledger fallback rows.</p></section><section class="section">{note}{table(rows)}</section>'
    WEB.joinpath("sources",f"{slug(name)}.html").write_text(shell(f"{name} Sources","Sources",sbody,"../"),encoding="utf-8")
    source_cards.append(f'<a class="card feature-card" href="sources/{slug(name)}.html"><h3>{html.escape(name)}</h3><p>{len(rows)} controlled source rows, {len(fallback)} fallback row(s).</p></a>')
WEB.joinpath("sources.html").write_text(shell("Sources","Sources",'<section class="page-intro"><h1>Sources</h1><p>Source provenance and master-versus-jurisdiction-ledger tiers are preserved.</p></section><section class="grid">'+"".join(source_cards)+'</section>'),encoding="utf-8")

law_cards=[]
for title,fn,desc in LAW_DOCS:
    p=ROOT/"legislation"/fn
    if not p.exists(): continue
    law_cards.append(f'<a class="card feature-card" href="law/{slug(title)}.html"><h3>{html.escape(title)}</h3><p>{html.escape(desc)}</p></a>')
    body=f'<section class="page-intro"><h1>{html.escape(title)}</h1><p>{html.escape(desc)}</p></section><section class="section prose-card">{md_html(strip_controls(p.read_text(encoding="utf-8")))}</section>'
    WEB.joinpath("law",f"{slug(title)}.html").write_text(shell(title,"Existing Law",body,"../"),encoding="utf-8")
WEB.joinpath("law.html").write_text(shell("Existing Law","Existing Law",'<section class="page-intro"><h1>Legal framework</h1><p>Existing-law research records and interfaces.</p></section><section class="grid">'+"".join(law_cards)+'</section>'),encoding="utf-8")
WEB.joinpath("research.html").write_text(shell("Research","Research",'<section class="page-intro"><h1>Research by subject.</h1></section><section class="grid"><a class="card feature-card" href="states.html"><h3>State implementation</h3></a><a class="card feature-card" href="law.html"><h3>Existing law</h3></a><a class="card feature-card" href="sources.html"><h3>Source evidence</h3></a></section>'),encoding="utf-8")
WEB.joinpath("methodology.html").write_text(shell("Methodology","Methodology",'<section class="page-intro"><h1>Research methodology</h1></section><section class="grid"><article class="card"><h3>Primary-source preference</h3><p>Constitutional text, legislation, Rules, Gazettes, Government orders, judgments, Parliament and official statistics are preferred.</p></article><article class="card"><h3>Evidence grades</h3><p>A is primary authoritative evidence. B is strong official or credible evidence. C is reliable secondary evidence. D is weak or unverified material.</p></article><article class="card"><h3>Source-ledger control</h3><p>The master ledger remains distinct from jurisdiction-specific ledgers. Fallback rows are explicitly labelled and never treated as master integrations.</p></article></section>'),encoding="utf-8")
WEB.joinpath("404.html").write_text(shell("Page not found","",'<section class="page-intro"><h1>Page not found.</h1></section>'),encoding="utf-8")
WEB.joinpath("robots.txt").write_text("User-agent: *\nAllow: /\n",encoding="utf-8")
pages=sorted(p.relative_to(WEB).as_posix() for p in WEB.rglob("*.html"))
WEB.joinpath("sitemap.xml").write_text("\n".join(['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']+[f"<url><loc>{html.escape(p)}</loc></url>" for p in pages]+['</urlset>']),encoding="utf-8")
html_text="\n".join(p.read_text(encoding="utf-8") for p in WEB.rglob("*.html"))
for x in BANNED:
    if x.lower() in html_text.lower(): raise RuntimeError(f"PUBLIC CONTENT FAILURE: {x}")
for x in BANNED_PHRASES:
    if x.lower() in html_text.lower(): raise RuntimeError(f"PUBLIC CONTENT FAILURE: {x}")
print(f"Built {len(pages)} HTML pages from {len(completed)} jurisdictions; master source rows={len(master)}; fallback rows available={len(gap)}")
