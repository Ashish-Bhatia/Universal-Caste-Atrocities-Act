# Universal Caste Atrocities Act

## Project State
- Phase 1, Existing-Law Baseline and Source Map: ACTIVE.
- Authoritative repository: `Ashish-Bhatia/Universal-Caste-Atrocities-Act`.
- Phase 1 acceptance criteria: NOT YET SATISFIED.
- 36 of 36 States/UTs have substantive Phase 1 jurisdiction inventories. Puducherry is the 36th completed jurisdiction.
- Current state is determined by repository evidence plus verified decisions and documented unresolved issues. `NEXT_CHAT.md` is downstream and is not a source of truth.
- Methodology: evidence-first, primary-source preference, explicit evidence grading, no presumed necessity, constitutionality or superiority.

## State/UT Position

36 of 36 Indian States/UTs have substantive Phase 1 jurisdiction inventories. No State/UT remains unresearched.

Completed sequence:
Andhra Pradesh, Arunachal Pradesh, Assam, Bihar, Chhattisgarh, Goa, Gujarat, Haryana, Himachal Pradesh, Jharkhand, Karnataka, Kerala, Madhya Pradesh, Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland, Odisha, Punjab, Rajasthan, Sikkim, Tamil Nadu, Telangana, Tripura, Uttar Pradesh, Uttarakhand, West Bengal, Andaman and Nicobar Islands, Chandigarh, Dadra and Nagar Haveli and Daman and Diu, Delhi (NCT), Jammu and Kashmir, Ladakh, Lakshadweep, Puducherry.

Jammu and Kashmir remains the 33rd completed jurisdiction and is classified PROCEED/CLOSE WITH LIMITATIONS. Its PH1-ISSUE-JK-001 through PH1-ISSUE-JK-018 remain open. The Rule 8 Protection Cell contradiction remains unresolved.

Ladakh is the 34th completed jurisdiction and is classified PROCEED/CLOSE WITH LIMITATIONS. Its residuals PH1-ISSUE-LA-001 through PH1-ISSUE-LA-018 are recorded in `project-state/LADAKH_ISSUES_2026-09-06.md`.

Lakshadweep is the 35th completed jurisdiction and is classified PROCEED/CLOSE WITH LIMITATIONS. Its residuals PH1-ISSUE-LK-001 through PH1-ISSUE-LK-018 are recorded in `project-state/LAKSHADWEEP_ISSUES_2026-09-06.md`.

Puducherry is the 36th completed jurisdiction and is classified PROCEED/CLOSE WITH LIMITATIONS. Its residuals PH1-ISSUE-PY-001 through PH1-ISSUE-PY-016 are recorded in `project-state/PUDUCHERRY_ISSUES_2026-09-06.md`.

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

Pico CSS 2.1.1 is now integrated in the production builder. `scripts/build_website_v2.py` loads `website/assets/pico-theme.css` before `assets/site.css`, with a versioned Pico cache key. The existing production site CSS remains the primary visual layer and the existing overrides remain last.

A new GitHub Pages workflow run #479 built the Pico-integrated commit `dae56579daf386fcfd27fe18b35267ae34d7a515` successfully. Pages artifact `github-pages`, artifact ID `9977570690`, digest `sha256:5e1606eab5b5a96cf08ba10c002e0e961be7bf731a72eba26ab7064beec47a8b`, was produced and deployed successfully.

Independent inspection of the downloaded run #479 artifact verified 90 HTML pages, 36 jurisdiction pages, 36 source pages, 9 law pages, 90 sitemap entries, 36/36 public hero count, no 33/36 text, Pico before site.css on all 90 HTML pages, both CSS assets present, zero broken local links and zero heading-hierarchy jumps. All 90 pages contained language, title and description metadata.

The Pages workflow itself passed Python compilation, source-ledger reconciliation, site build, count synchronization, responsive/accessibility rendering controls, sanitization, generated-site validation, artifact upload and deployment.

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

The Manual Scavengers Gazette/Legislative Department census is a controlled closure with qualifications. The identified Central instrument chain includes the 2013 commencement instrument, 2013 Rules, 2014-2018 Central Monitoring Committee amendments and six later section 29 CMC amendments in 2023-2025. No Central Rules amendment was identified in the defined search, and no Central section 39 exemption order was identified. These are controlled instrument-census results, not categorical absence conclusions. PH1-ISSUE-015 and PH1-ISSUE-017 are CLOSED WITH QUALIFICATION. PH1-ISSUE-016 is ADVANCED WITH QUALIFICATION.

The broader BNS/BNSS/BSA transition is under a CONTROLLED FREEZE WITH QUALIFICATIONS in `project-state/PH1_BNS_BNSS_BSA_TRANSITION_FREEZE_2026-09-06.md`. Legislative Department S.O. 2790(E), 16-07-2024 is the controlling construction-of-references instrument. It does not justify blanket numerical substitution and does not displace special-law provisions. SC/ST Act BNS/BNSS/BSA residuals remain open where the existing crosswalks record material correspondence, punishment, procedural or evidence questions.

PCR Act/Rules remain completed at comparison level with qualification. The current Department of Social Justice and Empowerment archive continues to list the PCR Act and 1977 Rules. The defined targeted official search did not identify a later Central amendment instrument. This remains controlled search evidence, not proof of legal absence.

Bonded Labour Act/Rules remain completed at crosswalk level with qualification. The Act's identified Central amending Act is the Bonded Labour System (Abolition) Amendment Act, 1985. The Central Rules record the 1976 Rules with identified 1978 and 1983 amendments in the consolidated official reproduction. No later Central amendment instrument was established by the targeted search. Search silence is not treated as legal absence.

Priority 2 Central legislation remains screened rather than clause-level closed.

## Control-Record Supersession

`project-state/PH1_STATE_CONTROL_RECONCILIATION_2026-09-06.md` remains a historical pre-Puducherry control record and is superseded for current State/UT count by the current acceptance audit and State Implementation Inventory.

The physical `ISSUES_REGISTER.md` rows for PH1-ISSUE-015, PH1-ISSUE-016 and PH1-ISSUE-017 are now synchronized to the Manual Scavengers closure/control records.

## Closed for This Workstream

No State/UT research reopened.
No Manual Scavengers Gazette census repeated.
No Manual Scavengers section 39 search repeated.
No Manual Scavengers BNSS transition verification repeated.
No Bill drafting.
No policy-superiority or necessity analysis.
No constitutional-validity analysis.
No Phase 2 case-law research.
No modification of `research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md` for website synchronization.

## Decision Gate

STATE/UT INVENTORY COMPLETENESS: PASS, 36/36.

EXACT HISTORICAL MASTER-VERSUS-JURISDICTION SOURCE-ID CONTROL: PRESERVED, 261/29/571/377/67.

CURRENT POST-BASELINE SOURCE FILESYSTEM DELTA: RECORDED, NOT INTEGRATED INTO MASTER.

WEBSITE FALLBACK CONTROL: PASS.

PICO INTEGRATION: PASS, verified in run #479 artifact.

CURRENT PAGES ARTIFACT: PASS, run #479, artifact `9977570690`, digest `5e1606eab5b5a96cf08ba10c002e0e961be7bf731a72eba26ab7064beec47a8b`.

WEBSITE STATIC/ARTIFACT AUDIT: PASS, 90 HTML pages, 36 jurisdiction research pages, 36 source pages, 9 law pages, 90 sitemap entries, 36/36 count, no 33/36 text, Pico-before-site.css order on all pages, zero broken local links and zero heading jumps.

LIVE PAGES HTTP/SETTINGS VERIFICATION: OPEN, connector limitation.

SC/ST ACT CURRENT-TEXT/VERSION QUESTION: CLOSED WITH QUALIFICATION.

SC/ST RULES ANNEXURE-II SOURCE DISCREPANCY: CLOSED.

MANUAL SCAVENGERS LATER-INSTRUMENT CENSUS: CLOSED WITH QUALIFICATION, PH1-ISSUE-015.

MANUAL SCAVENGERS SECTION 39 CENTRAL INSTRUMENT CENSUS: CLOSED WITH QUALIFICATION, PH1-ISSUE-017.

MANUAL SCAVENGERS BNSS TRANSITION: ADVANCED WITH QUALIFICATION, PH1-ISSUE-016.

CENTRAL CURRENT-LAW COMPLETENESS: OPEN, PH1-ISSUE-008.

BNS/BNSS/BSA TRANSITION FREEZE: CONTROLLED FREEZE WITH QUALIFICATIONS, PH1-ISSUE-003, PH1-ISSUE-004, PH1-ISSUE-005, PH1-ISSUE-009 and related residuals remain open.

JURISDICTION CURRENTNESS/INSTRUMENT RESIDUALS: OPEN.

PHASE 1 SUBSTANTIVE ACCEPTANCE: NOT YET SATISFIED.

Next authorized workstream: continue PH1-ISSUE-008 later-instrument closure and unresolved BNS/BNSS/BSA correspondence classes using primary sources, without reopening completed work.

## Latest Controlled Update

2026-09-06: synchronized PH1-ISSUE-015, PH1-ISSUE-016 and PH1-ISSUE-017 to the Manual Scavengers closure/control records; reconciled PROJECT_STATE; integrated Pico CSS 2.1.1 before site.css; triggered Pages run #479; verified artifact `9977570690` and digest `sha256:5e1606eab5b5a96cf08ba10c002e0e961be7bf731a72eba26ab7064beec47a8b`; completed independent artifact static checks with PASS results recorded above.
