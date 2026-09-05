# Universal Caste Atrocities Act

## Project State
- Phase 1, Existing-Law Baseline and Source Map: ACTIVE.
- Authoritative repository: `Ashish-Bhatia/Universal-Caste-Atrocities-Act`.
- Phase 1 acceptance criteria: NOT YET SATISFIED.
- Current state is determined by repository evidence plus verified decisions and documented unresolved issues. `NEXT_CHAT.md` is downstream and is not a source of truth.
- Methodology: evidence-first, primary-source preference, explicit evidence grading, no presumed necessity, constitutionality or superiority.

## State/UT Position
33 of 36 Indian States/UTs have substantive Phase 1 jurisdiction inventories.

Completed sequence:
Andhra Pradesh, Arunachal Pradesh, Assam, Bihar, Chhattisgarh, Goa, Gujarat, Haryana, Himachal Pradesh, Jharkhand, Karnataka, Kerala, Madhya Pradesh, Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland, Odisha, Punjab, Rajasthan, Sikkim, Tamil Nadu, Telangana, Tripura, Uttar Pradesh, Uttarakhand, West Bengal, Andaman and Nicobar Islands, Chandigarh, Dadra and Nagar Haveli and Daman and Diu, Delhi (NCT), Jammu and Kashmir.

Jammu and Kashmir is the 33rd completed jurisdiction and is classified PROCEED/CLOSE WITH LIMITATIONS. Its PH1-ISSUE-JK-001 through PH1-ISSUE-JK-018 remain open. The Rule 8 Protection Cell contradiction remains unresolved.

Remaining unresearched jurisdictions:
1. Ladakh
2. Lakshadweep
3. Puducherry

## Control Remediation Status, 2026-09-06

The website/source-ledger remediation has now produced the required deterministic control comparison. The control comparison is VERIFIED. The Pages deployment itself is NOT successful because the first non-cancelled post-remediation run failed during the controlled fallback build.

Authoritative control matrix: `project-state/PH1_CONTROL_MATRIX_2026-09-06.md`.

## Verified post-remediation source-ledger control

Workflow run #389, head commit `180663c0f64ba8970a239f3d828e91363709a9ad`, completed with `failure`. Its `source-ledger-control` artifact was successfully uploaded and independently downloaded and inspected.

Artifact: `source-ledger-control`, artifact ID `9976069045`, SHA-256 `989f586939b111e6902f69c6e59ac9611c1b19f9e71eea12577253d49bde6c6e`.

Exact control totals:
- `MASTER_IDS=261`
- `JURISDICTION_LEDGER_FILES=29`
- `JURISDICTION_LEDGER_IDS=571`
- `MISSING_FROM_MASTER=377`
- `MASTER_ONLY_IDS=67`

The exact 377-ID `MISSING_IDS` set is recorded in `project-state/WEBSITE_SOURCE_LEDGER_GAP_2026-09-06.md`.

Per-ledger control shows ten of the 29 scanned jurisdiction ledgers have zero IDs missing from the master: Bihar, Goa, Gujarat, Haryana, Himachal Pradesh, Jharkhand, Karnataka, Kerala, Madhya Pradesh and Maharashtra. Nineteen of the 29 scanned jurisdiction ledgers have one or more IDs missing from the master. The five previously identified later contributors, Gujarat, Haryana, Himachal Pradesh, Kerala and Madhya Pradesh, are fully represented by ID comparison, but this does not establish full later-jurisdiction integration.

The earlier five-ledger integration narrative must therefore be read narrowly. It establishes that those five named contributor ledgers were integrated/represented in the master at the relevant control point. It does not establish that all later jurisdiction-specific ledgers were integrated. The master ledger remains unchanged by this website remediation.

Controlled gap record: `project-state/WEBSITE_SOURCE_LEDGER_GAP_2026-09-06.md`.

## Website build result after remediation

Run #389 reached the source-ledger control artifact successfully, then failed in `scripts/build_website_v2.py` with:

`CONTROL FAILURE: completed jurisdiction has no controlled source rows: Arunachal Pradesh`

This occurred because Arunachal Pradesh has no substantive local source ledger recognized by the builder and its referenced source IDs are absent from the master ledger. The workflow correctly rejected silent empty-source publication under the selected control rule.

Because the build failed, generated-site validation, Pages artifact upload and deployment were skipped. No post-remediation generated Pages artifact exists from run #389. Live GitHub Pages publication remains independently unverified.

This is now a two-part control position:
1. Exact master-versus-jurisdiction source-ID gap: VERIFIED.
2. Public-site fallback coverage/build success: NOT VERIFIED; build currently fails on Arunachal Pradesh.

The controlled two-tier source rule remains the authoritative public-source rendering decision:
- master rows are authoritative for rows actually integrated into the master;
- jurisdiction-ledger fallback rows may be rendered where substantive local-ledger rows exist and are absent from the master;
- fallback must be explicitly labelled and is not master-ledger integration;
- a completed jurisdiction with neither master rows nor controlled local-ledger rows must fail rather than publish an empty source set.

## Cumulative Control Layer

The 2026-09-06 cumulative state-control reconciliation remains preserved.

The three cumulative controls contain explicit reconciliation-only indexes:
- `RESEARCH_LEDGER.md` contains the cumulative 33-jurisdiction artifact-control index through Jammu and Kashmir.
- `ISSUES_REGISTER.md` contains the cumulative residual-control index covering the later jurisdiction-specific issue sets without renumbering existing IDs.
- `DECISIONS_LOG.md` contains the cumulative jurisdiction-decision control index through Jammu and Kashmir without fabricating cumulative IDs.

The jurisdiction-specific records remain the substantive records. The indexes are control metadata only.

## Central and Transition Residuals

Central later-instrument/current-law completeness remains open. BNS/BNSS/BSA transition verification remains open. Existing State residuals remain jurisdiction-specific. Search silence is not treated as absence.

## Website and Repository Synchronization

A repository-driven website builder generates the public research interface from substantive repository research records at Pages deployment time.

The public website content boundary is explicit:
- Publish actual legal and jurisdictional implementation research only.
- Publish source provenance, source identifiers, findings, evidence grades and verification status where recorded.
- Give every completed State/UT a dedicated research page.
- Give every completed State/UT a dedicated source-set page.
- Give each existing-law research document its own page where the source document exists.
- Keep project-state controls, issue registers, decision logs, continuity prompts and other project-management data out of the public research interface.
- Use internal Pages links for public navigation. Do not send readers to GitHub repository pages as substitutes for research pages.
- Generate `sitemap.xml`, `robots.txt` and `404.html`.
- Build-time validation rejects repository-navigation links in generated HTML.

The production builder is `scripts/build_website_v2.py`. It implements the controlled master/fallback source rule and rejects completed jurisdictions with no controlled source rows. `scripts/sanitize_public_html.py` removes the identified `DECISIONS_LOG.md` reference from generated output before public validation. The workflow compiles the control scripts, records the source-ledger comparison as an artifact, builds the site, sanitizes generated output, validates page counts and public-content boundaries, uploads the Pages artifact and deploys only after validation.

The latest verified run did not reach the public validation or deployment stages because the controlled builder correctly failed at Arunachal Pradesh. Therefore repository-side control implementation is present, but successful production synchronization is not yet established.

## Codespaces / Repository-Side Infrastructure

Repository-side Codespaces configuration remains available through `.devcontainer/devcontainer.json`; Codespaces administration itself remains unavailable through the connector.

The current `.devcontainer/devcontainer.json`:
- uses the supported `mcr.microsoft.com/devcontainers/python:3-3.12-bookworm` image;
- preserves the existing Explorer settings;
- opens `README.md` and `PROJECT_STATE.md`;
- runs `ln -sf DELHI.md legislation/states/DELHI_NCT.md && python3 scripts/build_website.py` as `postCreateCommand`.

The 2026-09-06 screenshot shows the Codespaces container setup actively downloading image layers, with several large layers reporting download progress and others waiting. This is evidence of container image retrieval during the rebuild, not evidence of a Python `postCreateCommand` failure. A successful rebuild still requires observation of the post-download completion state because Codespaces administration is not exposed through the connector.

## Closed for This Workstream

No Ladakh research.
No Lakshadweep research.
No Puducherry research.
No other new State/UT substantive research.
No Bill drafting.
No policy-superiority or necessity analysis.
No constitutional-validity analysis.
No Phase 2 case-law research.
No reopening of completed jurisdiction baselines absent a genuine evidentiary/control defect. The website/source-ledger synchronization defect remains a control defect and does not itself authorize substantive jurisdiction reopening.
No repetition of the completed 2026-09-06 independent audit, cumulative state-control reconciliation, master State Implementation Inventory reconciliation, master source-ledger integration or zero-drift verification except targeted verification required to resolve the website/source-ledger control defect.

## Decision Gate

CUMULATIVE CONTROL RECONCILIATION: PASS.

EXACT MASTER-VERSUS-JURISDICTION SOURCE-ID CONTROL: PASS, verified from post-remediation workflow artifact.

WEBSITE FALLBACK COVERAGE / PRODUCTION BUILD: FAIL/OPEN, because run #389 rejected Arunachal Pradesh for having no controlled source rows.

Master State Implementation Inventory reconciliation: COMPLETE.

Master State Implementation Source Ledger substantive content: UNCHANGED by this remediation.

Website production-library remediation: IMPLEMENTED, but successful source-set synchronization is NOT VERIFIED because the post-remediation build failed before public-site validation and Pages deployment.

Codespaces repository-side remediation: IMPLEMENTED, live rebuild completion pending.

Phase 1 substantive acceptance remains NOT YET SATISFIED.

No substantive next-jurisdiction work is authorized until the remaining website/source-ledger control defect is reconciled and the next control gate is explicitly opened.

## Latest Controlled Update

2026-09-06: retrieved and inspected the first non-cancelled post-remediation Pages control artifact from run #389; verified `MASTER_IDS=261`, `JURISDICTION_LEDGER_FILES=29`, `JURISDICTION_LEDGER_IDS=571`, `MISSING_FROM_MASTER=377` and `MASTER_ONLY_IDS=67`; recorded the exact 377-ID gap and all per-ledger totals in `project-state/WEBSITE_SOURCE_LEDGER_GAP_2026-09-06.md`; verified the Pages job failure at the controlled fallback build for Arunachal Pradesh; did not claim a Pages artifact or live publication; preserved the prohibition on new jurisdiction research and substantive Bill/policy/constitutional/Phase 2 work.
