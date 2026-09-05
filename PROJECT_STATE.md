# Universal Caste Atrocities Act

## Project State
- Phase 1, Existing-Law Baseline and Source Map: ACTIVE.
- Authoritative repository: `Ashish-Bhatia/Universal-Caste-Atrocities-Act`.
- Phase 1 acceptance criteria: NOT YET SATISFIED.
- 36 of 36 States/UTs have substantive Phase 1 jurisdiction inventories. Puducherry is the 36th completed jurisdiction.
- Current state is determined by repository evidence plus verified decisions and documented unresolved issues. `NEXT_CHAT.md` is downstream and is not a source of truth.
- Methodology: evidence-first, primary-source preference, explicit evidence grading, no presumed necessity, constitutionality or superiority.

## State/UT Position

36 of 36 Indian States/UTs have substantive Phase 1 jurisdiction inventories.

Completed sequence:
Andhra Pradesh, Arunachal Pradesh, Assam, Bihar, Chhattisgarh, Goa, Gujarat, Haryana, Himachal Pradesh, Jharkhand, Karnataka, Kerala, Madhya Pradesh, Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland, Odisha, Punjab, Rajasthan, Sikkim, Tamil Nadu, Telangana, Tripura, Uttar Pradesh, Uttarakhand, West Bengal, Andaman and Nicobar Islands, Chandigarh, Dadra and Nagar Haveli and Daman and Diu, Delhi (NCT), Jammu and Kashmir, Ladakh, Lakshadweep, Puducherry.

Jammu and Kashmir remains the 33rd completed jurisdiction and is classified PROCEED/CLOSE WITH LIMITATIONS. Its PH1-ISSUE-JK-001 through PH1-ISSUE-JK-018 remain open. The Rule 8 Protection Cell contradiction remains unresolved.

Ladakh is the 34th completed jurisdiction and is classified PROCEED/CLOSE WITH LIMITATIONS. Its residuals PH1-ISSUE-LA-001 through PH1-ISSUE-LA-018 are recorded in `project-state/LADAKH_ISSUES_2026-09-06.md`.

Lakshadweep is the 35th completed jurisdiction and is classified PROCEED/CLOSE WITH LIMITATIONS. Its residuals PH1-ISSUE-LK-001 through PH1-ISSUE-LK-018 are recorded in `project-state/LAKSHADWEEP_ISSUES_2026-09-06.md`.

Puducherry is the 36th completed jurisdiction and is classified PROCEED/CLOSE WITH LIMITATIONS. Its residuals PH1-ISSUE-PY-001 through PH1-ISSUE-PY-016 are recorded in `project-state/PUDUCHERRY_ISSUES_2026-09-06.md`.

Remaining unresearched jurisdiction: None.

## Cumulative Phase 1 Acceptance Audit

The cumulative acceptance audit is recorded in `project-state/PH1_ACCEPTANCE_AUDIT_2026-09-06.md`.

The State/UT inventory-completeness component is satisfied at 36/36. Overall Phase 1 acceptance remains NOT YET SATISFIED because Central current-law completeness, BNS/BNSS/BSA transition/source freeze and jurisdiction currentness/instrument residuals remain open.

## Source-ledger Control Baseline

The exact historical source-ledger control comparison remains preserved:
- `MASTER_IDS=261`
- `JURISDICTION_LEDGER_FILES=29`
- `JURISDICTION_LEDGER_IDS=571`
- `MISSING_FROM_MASTER=377`
- `MASTER_ONLY_IDS=67`

The exact 377-ID `MISSING_IDS` set is recorded in `project-state/WEBSITE_SOURCE_LEDGER_GAP_2026-09-06.md`.

A later repository filesystem enumeration after Ladakh, Lakshadweep and Puducherry found 32 jurisdiction ledgers, 628 jurisdiction-ledger IDs and 434 IDs absent from the master. This is recorded as a post-baseline delta in `project-state/PH1_SOURCE_LEDGER_POST_BASELINE_DELTA_2026-09-06.md`. It does not replace the preserved historical baseline and does not change the master ledger.

No IDs were copied into `research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md` for website synchronization. Jurisdiction-ledger fallback is not master-ledger integration.

## Website Control Status

The earlier website/source-ledger remediation remains CLOSED AND VERIFIED for its original rendering/control defect.

Current post-remediation Pages deployment was verified by workflow run #461 and its generated artifact.

Run #461 is the latest verified Pages deployment before the controlled Pico integration requested in the current workstream.

The existing full static/artifact audit is recorded in `project-state/WEBSITE_FULL_AUDIT_2026-09-06.md`.

Pico 2.1.1 was inspected but was not previously integrated. The controlled integration decision is to load `website/assets/pico-theme.css` before `assets/site.css` in the generated HTML. A new complete static audit and a new Pages artifact verification are required before any Pico deployment claim.

The connector still lacks independent browser-level live-URL HTTP verification and Pages Settings inspection. Deployment success is therefore recorded as a workflow/artifact fact, not as a separately browser-verified live-site claim.

## Source-ledger Synchronization Boundary

The public source layer has two controlled tiers:
- master-ledger rows are authoritative where actually integrated in the master;
- jurisdiction-ledger fallback rows may be rendered where substantive local-ledger rows exist and are absent from the master;
- fallback rows are explicitly labelled and are never treated as master-ledger integration;
- a completed jurisdiction with neither controlled master rows nor controlled fallback rows fails the build.

The 377-ID discrepancy remains unresolved as a historical classification/integration question. The later 57 post-baseline IDs are not treated as a correction to the master ledger.

## Central and Transition Residuals

The SC/ST Act current consolidated text has reached a controlled closure outcome for the Act-version question. India Code's 21-09-2025 consolidation was verified and a targeted 2026 search located no later Central amending Act. This closes PH1-ISSUE-001 with qualification, while PH1-ISSUE-008 remains open for the broader later-instrument search.

The SC/ST Rules Annexure-II apparent 1986/2001 source discrepancy is resolved by the official Ministry of Tribal Affairs-hosted Rules PDF, which identifies the attached Annexure-II as the 01-06-2001 notification and explains the 06-08-1986 instrument as the earlier guideline being reviewed. PH1-ISSUE-014 is closed.

The Manual Scavengers Gazette/Legislative Department census is now a controlled closure with qualifications. The identified Central instrument chain includes the 2013 commencement instrument, 2013 Rules, 2014-2018 Central Monitoring Committee amendments and six later section 29 CMC amendments in 2023-2025. No Central Rules amendment was identified in the defined search, and no Central section 39 exemption order was identified. These are controlled instrument-census results, not categorical absence conclusions. PH1-ISSUE-015 and PH1-ISSUE-017 are therefore CLOSED WITH QUALIFICATION in the authoritative closure records.

Manual Scavengers BNSS transition remains ADVANCED WITH QUALIFICATION under `project-state/PH1_MANUAL_SCAVENGERS_BNSS_TRANSITION_2026-09-06.md`. The targeted work is not to be repeated. State-specific post-01-07-2024 section 21 empowerment orders remain unresolved.

The broader BNS/BNSS/BSA transition is under a CONTROLLED FREEZE WITH QUALIFICATIONS in `project-state/PH1_BNS_BNSS_BSA_TRANSITION_FREEZE_2026-09-06.md`. Legislative Department S.O. 2790(E), 16-07-2024 is the controlling construction-of-references instrument. It does not justify blanket numerical substitution and does not displace special-law provisions. SC/ST Act BNS/BNSS/BSA residuals remain open where the existing crosswalks record material correspondence, punishment, procedural or evidence questions.

PCR Act/Rules remain completed at comparison level with qualification. The current Department of Social Justice and Empowerment archive continues to list the PCR Act and 1977 Rules. The final Gazette/Legislative Department completeness question remains under PH1-ISSUE-008.

Bonded Labour Act/Rules remain completed at crosswalk level with qualification. The Act's identified Central amending Act is the Bonded Labour System (Abolition) Amendment Act, 1985. The Central Rules record the 1976 Rules with identified 1978 and 1983 amendments in the consolidated official reproduction. No later Central amendment instrument has been established by the current targeted search; this remains a controlled search result, not a legal-absence conclusion.

Priority 2 Central legislation remains screened rather than clause-level closed. Search silence is not treated as absence.

## Puducherry Phase 1 Position

Puducherry was researched on 2026-09-06 using the Phase 1 control matrix, primary-source hierarchy and currentness rules. The jurisdiction has a dedicated PCR Cell, State and District V&MC architecture, a specified Special Judge framework, prosecution arrangements and relief instruments. It is PROCEED/CLOSE WITH LIMITATIONS. Sixteen residuals remain open, including current Rule 9/10 appointments, investigation-allocation conflict, current court/prosecution rosters, current meetings, current case/relief data and post-BNS/BNSS/BSA workflow verification.

## Control-Record Supersession

`project-state/PH1_STATE_CONTROL_RECONCILIATION_2026-09-06.md` is retained as a historical control-layer record of the pre-Puducherry 33/36 state. It is superseded for current State/UT count and sequencing by `project-state/PH1_ACCEPTANCE_AUDIT_2026-09-06.md`, the current State Implementation Inventory and this file.

`project-state/PH1_ISSUES_REGISTER_RECONCILIATION_2026-09-06.md` records the earlier authoritative reconciliation of stale PH1-ISSUE-001 and PH1-ISSUE-014 statuses. The physical rows for those issues were synchronized. The current Manual Scavengers closure records now supersede the older Manual Scavengers status wording and require physical synchronization of PH1-ISSUE-015, PH1-ISSUE-016 and PH1-ISSUE-017 before those rows are treated as synchronized.

## Closed for This Workstream

Puducherry Phase 1 research completed; no Phase 2 case-law research.
No Bill drafting.
No policy-superiority or necessity analysis.
No constitutional-validity analysis.
No Phase 2 case-law research.
No reopening of completed jurisdictions absent a genuine evidentiary/control defect.
No repetition of the completed 2026 remediation, verified historical 377-ID comparison or run #397 artifact inspection except targeted verification required by a new control defect.
No repetition of Jammu and Kashmir, Ladakh, Lakshadweep or Puducherry without a qualifying reopening trigger.
No modification of `research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md` for website synchronization.
No repetition of the completed Manual Scavengers Gazette census, section 39 search or Manual Scavengers BNSS transition verification.

## Decision Gate

STATE/UT INVENTORY COMPLETENESS: PASS, 36/36.

EXACT HISTORICAL MASTER-VERSUS-JURISDICTION SOURCE-ID CONTROL: PRESERVED, 261/29/571/377/67.

CURRENT POST-BASELINE SOURCE FILESYSTEM DELTA: RECORDED, NOT INTEGRATED INTO MASTER.

WEBSITE FALLBACK CONTROL: PASS.

CURRENT POST-REMEDIATION PAGES ARTIFACT: PASS, run #461, before Pico integration.

WEBSITE FULL STATIC/ARTIFACT AUDIT: PASS, recorded in `project-state/WEBSITE_FULL_AUDIT_2026-09-06.md`, before Pico integration.

PICO INTEGRATION: PENDING NEW BUILD AND ARTIFACT VERIFICATION.

LIVE PAGES HTTP/SETTINGS VERIFICATION: OPEN, connector limitation.

SC/ST ACT CURRENT-TEXT/VERSION QUESTION: CLOSED WITH QUALIFICATION.

SC/ST RULES ANNEXURE-II SOURCE DISCREPANCY: CLOSED.

MANUAL SCAVENGERS LATER-INSTRUMENT CENSUS: CLOSED WITH QUALIFICATION, PH1-ISSUE-015.

MANUAL SCAVENGERS SECTION 39 CENTRAL INSTRUMENT CENSUS: CLOSED WITH QUALIFICATION, PH1-ISSUE-017.

MANUAL SCAVENGERS BNSS TRANSITION: ADVANCED WITH QUALIFICATION, PH1-ISSUE-016.

CENTRAL CURRENT-LAW COMPLETENESS: OPEN, PH1-ISSUE-008.

BNS/BNSS/BSA TRANSITION FREEZE: CONTROLLED FREEZE WITH QUALIFICATIONS, PH1-ISSUE-003, PH1-ISSUE-004, PH1-ISSUE-005, PH1-ISSUE-009 and related crosswalk residuals remain open.

JURISDICTION CURRENTNESS/INSTRUMENT RESIDUALS: OPEN.

PHASE 1 SUBSTANTIVE ACCEPTANCE: NOT YET SATISFIED.

Next authorized workstream: synchronize the three Manual Scavengers physical issue rows, then continue controlled PH1-ISSUE-008 later-instrument closure and unresolved BNS/BNSS/BSA correspondence classes, followed by controlled Pico integration, complete static audit and new Pages artifact verification.

## Latest Controlled Update

2026-09-06: completed Puducherry Phase 1 State/UT inventory as the 36th jurisdiction; reconciled the master State/UT inventory to 36/36; completed the cumulative Phase 1 acceptance audit; added the Phase 1 website count synchronization control; fixed the hard-coded 33/36 validation defect; verified the current 36-jurisdiction Pages artifact in run #438; recorded the post-baseline source-ledger filesystem delta; did not modify the master State Implementation Source Ledger.

2026-09-06: closed the SC/ST Act current-text/version residual on a qualified controlled basis and resolved the SC/ST Rules Annexure-II 1986/2001 source discrepancy using the official Ministry-hosted Rules PDF. Remaining Central and transition dependencies remain open.

2026-09-06: independent audit of run #446 identified six heading-hierarchy defects. The builder was corrected, run #448 deployed successfully, and the subsequent run #452 artifact reproduced the full static audit PASS. Live browser-level HTTP/Pages Settings verification remains open due connector limitations.

2026-09-06: recorded the stale central-law issue reconciliation for PH1-ISSUE-001 and PH1-ISSUE-014 and advanced the Manual Scavengers BNSS transition workstream for PH1-ISSUE-016 using primary statutory sources. The physical `ISSUES_REGISTER.md` rows for PH1-ISSUE-015, PH1-ISSUE-016 and PH1-ISSUE-017 remain a synchronization task.

2026-09-06: final Manual Scavengers Gazette/Legislative Department census closed PH1-ISSUE-015 and PH1-ISSUE-017 with qualifications. The broader BNS/BNSS/BSA transition was frozen at the construction-of-references level using S.O. 2790(E), with unresolved correspondence classes preserved.

## 2026-09-06 Controlled Website Remediation Closure

The independent 2026-09-06 website/project audit remediation pass is closed at the source/build/deployment-control layer. Phase 1 substantive acceptance remains NOT YET SATISFIED. All 36 State/UT substantive inventories are complete. No new State/UT research, Bill drafting, policy-superiority/necessity analysis, constitutional-validity analysis or Phase 2 case-law research was performed.

Verified remediation outcomes:
- `scripts/build_website_v2.py` computes the completed/total jurisdiction count and no longer depends on hard-coded 33/36 hero text.
- Embedded Markdown tables are rendered as HTML tables.
- Embedded document H1 headings are rendered as H2 so state/law pages do not duplicate the page-level H1.
- Codespaces uses the same production v2 builder path as Pages.
- Generated website HTML/routes are treated as build output and are not committed as authoritative source. Website assets remain committed.
- README, stale State-control classification, PH1-ISSUE-001/014 physical statuses and Central decision IDs were synchronized.
- The accidental `legislation/states/DELHI_NCT.md` compatibility symlink and generated Python cache were removed from repository state.

Verification records:
- Isolated remediation workflow run #5 passed its 90-page generated-site audit.
- GitHub Pages run #460, head `c667a9ed42bb892136f01d5f5ce0ebbcb81eab25`, completed successfully.
- Pages artifact `github-pages`, artifact ID `9977341147`, digest `sha256:824ce74957da05c05ed7cddd708ff5f66ced4567ce80e91df5b6665fea854465`, was produced from current `main` and deployed successfully.
- Direct HTTP validation of the public Pages root remains unavailable from the current tool environment and therefore remains UNVERIFIED.

Current publication verdict before the new Pico integration: source/build/deployment controls PASS WITH QUALIFICATIONS; live URL independently UNVERIFIED.

Next substantive Phase 1 work remains central-law completeness, BNS/BNSS/BSA transition residuals, jurisdiction currentness and instrument residuals. Do not repeat completed State/UT research or closed control questions.
