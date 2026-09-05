# Next Chat Handoff

## Authoritative Rule
`PROJECT_STATE.md`, repository artifacts, verified decisions and documented unresolved issues are authoritative. This file is downstream and must not be treated as proof of completion.

## Current Phase
Phase 1, Existing-Law Baseline and Source Map: ACTIVE.
Phase 1 acceptance criteria: NOT YET SATISFIED.

## Current State/UT Position
36 of 36 States/UTs have substantive Phase 1 inventories. Puducherry is the 36th completed jurisdiction and is PROCEED/CLOSE WITH LIMITATIONS.

Remaining unresearched jurisdiction: None.

The cumulative acceptance audit is `project-state/PH1_ACCEPTANCE_AUDIT_2026-09-06.md`.

## Verified Source-Ledger Control Baseline
The preserved historical control baseline remains:
- `MASTER_IDS=261`
- `JURISDICTION_LEDGER_FILES=29`
- `JURISDICTION_LEDGER_IDS=571`
- `MISSING_FROM_MASTER=377`
- `MASTER_ONLY_IDS=67`

A later filesystem enumeration after Ladakh, Lakshadweep and Puducherry found 32 jurisdiction ledgers, 628 jurisdiction-ledger IDs and 434 IDs absent from the master. Treat this only as a post-baseline delta recorded in `project-state/PH1_SOURCE_LEDGER_POST_BASELINE_DELTA_2026-09-06.md`. Do not rewrite the historical 377-ID comparison and do not integrate the later IDs into the master ledger merely for website synchronization.

## Current Pages Status
The website full static/artifact audit is PASS after a targeted rendering remediation.

Run #446, commit `2736bda6730a07943e48be75c8f90dfb59e81016`, passed workflow validation but independent artifact inspection found six heading-hierarchy defects on `research.html`, `states.html`, `law.html`, `sources.html`, `methodology.html` and `petition.html`.

The defects were fixed in `scripts/build_website_v2.py` in commit `5a84edf116aa686aac92d5d7a2822a59b9ebef2b` by adding an intervening h2 section heading on the affected pages.

Run #447 was superseded/cancelled during artifact upload by the subsequent push under Pages workflow concurrency. Its build and validation steps had passed before cancellation.

Run #448, head commit `800e0f4cf53887ac354a2eb997c2cd005d84cf49`, completed successfully through Pages deployment.

Artifact: `github-pages`, artifact ID `9976902207`, SHA-256 digest `580cecc882332a14f4708c36f9069b92ba307d6778eec4946719ead9b992752c`.

Independent artifact audit verified 90 HTML pages, 36 research pages, 36 source pages, `36 /36` public count text, no `33/36` text, no broken local assets/links, valid language/title/description metadata, no duplicate IDs, no missing image alt text, no empty text links, no heading hierarchy jumps, and 90 matching sitemap entries. Full record: `project-state/WEBSITE_FULL_AUDIT_2026-09-06.md`.

Live Pages HTTP/settings verification remains OPEN because the connector does not provide independent browser-level inspection.

## Current Acceptance Position
The State/UT inventory-completeness component is PASS at 36/36.

Overall Phase 1 acceptance remains NOT YET SATISFIED because:
1. Central current-law/Gazette completeness remains open, although the SC/ST Act current-text/version question is now closed with qualification and the Annexure-II source discrepancy is closed.
2. BNS/BNSS/BSA transition/source freeze remains open.
3. PCR Act/Rules, Manual Scavengers Act/Rules, bonded-labour and Priority 2 Central closure items remain open where their issue records require further evidence.
4. Jurisdiction currentness and instrument-level residuals remain open.
5. Live Pages HTTP/settings verification remains unavailable through the connector.

## Central-law Reconciliation Recorded 2026-09-06
`project-state/PH1_ISSUES_REGISTER_RECONCILIATION_2026-09-06.md` records the controlled reconciliation of stale PH1-ISSUE-001 and PH1-ISSUE-014 entries against `project-state/PH1_CENTRAL_LAW_CLOSURE_2026-09-06.md`.

PH1-ISSUE-001 reconciled to CLOSED WITH QUALIFICATION. PH1-ISSUE-014 reconciled to CLOSED. The physical rows in `ISSUES_REGISTER.md` remain to be synchronized to the reconciliation record and must not be treated as independently current until synchronized.

## Manual Scavengers BNSS Transition Update
`project-state/PH1_MANUAL_SCAVENGERS_BNSS_TRANSITION_2026-09-06.md` advances PH1-ISSUE-016 from OPEN to ADVANCED WITH QUALIFICATION based on primary statutory sources. MS Act section 10 remains a special three-month cognizance limitation. MS Act section 21 retains its special Executive Magistrate/Judicial Magistrate first-class and summary-trial architecture. BNSS sections 3-5 provide the current construction-of-references, other-law and special-law framework. State-specific post-01-07-2024 empowerment orders remain open.

## Jurisdiction Residual Rule
Preserve all jurisdiction-specific residuals. Do not reopen a completed jurisdiction unless the formal reopening rule is met.

Puducherry: PH1-ISSUE-PY-001 through PH1-ISSUE-PY-016 remain open.
Lakshadweep: PH1-ISSUE-LK-001 through PH1-ISSUE-LK-018 remain open.
Ladakh: PH1-ISSUE-LA-001 through PH1-ISSUE-LA-018 remain open.
Jammu and Kashmir: PH1-ISSUE-JK-001 through PH1-ISSUE-JK-018 remain open, including the Rule 8 contradiction.

## Next Authorized Workstream
First synchronize the physical `ISSUES_REGISTER.md` rows for PH1-ISSUE-001 and PH1-ISSUE-014 with `project-state/PH1_ISSUES_REGISTER_RECONCILIATION_2026-09-06.md`. Do not alter any other issue row during that synchronization.

Then continue controlled closure of the remaining Phase 1 acceptance dependencies. The next substantive Central/transition priorities are PH1-ISSUE-015 later-instrument completeness for the Manual Scavengers Act/Rules, PH1-ISSUE-017 section 39 exemption-instrument verification, the broader Central later-instrument freeze under PH1-ISSUE-008, and the remaining BNS/BNSS/BSA transition matrix.

Do not begin Bill drafting, policy-superiority/necessity analysis, constitutional-validity analysis or Phase 2 case-law research.

## Required Reading Before Next Work
1. `PROJECT_STATE.md`
2. `NEXT_CHAT.md`
3. `project-state/PH1_CONTROL_MATRIX_2026-09-06.md`
4. `project-state/PH1_ACCEPTANCE_AUDIT_2026-09-06.md`
5. `project-state/PH1_CENTRAL_LAW_CLOSURE_2026-09-06.md`
6. `project-state/PH1_ISSUES_REGISTER_RECONCILIATION_2026-09-06.md`
7. `project-state/PH1_MANUAL_SCAVENGERS_BNSS_TRANSITION_2026-09-06.md`
8. `ISSUES_REGISTER.md`
9. `DECISIONS_LOG.md`
10. `legislation/STATE_IMPLEMENTATION_INVENTORY.md`

Read Puducherry, Ladakh or Lakshadweep substantive artifacts only if a qualifying reopening or targeted verification trigger exists.

## Do NOT Repeat

Do NOT repeat the run #389 Arunachal investigation.
Do NOT repeat the historical verified 377-ID comparison except targeted verification required by a new control defect.
Do NOT repeat run #397 artifact extraction and inspection.
Do NOT repeat run #438 artifact extraction and inspection absent a new control defect.
Do NOT repeat run #448 full artifact inspection absent a new control defect.
Do NOT repeat website builder/sanitizer/validator remediation unless a new failure occurs.
Do NOT modify the master State Implementation Source Ledger merely to synchronize the website.
Do NOT treat jurisdiction-ledger fallback as master-ledger integration.
Do NOT claim live Pages HTTP verification without direct evidence.
Do NOT repeat Jammu and Kashmir, Ladakh, Lakshadweep or Puducherry substantive research absent a formal reopening trigger.
Do NOT begin Bill drafting.
Do NOT conduct policy-superiority/necessity analysis.
Do NOT conduct constitutional-validity analysis.
Do NOT begin Phase 2 case-law research.
Do NOT repeat the SC/ST Act current-version closure, SC/ST Rules Annexure-II discrepancy resolution, or the completed Manual Scavengers crosswalk except for targeted verification.

## Exact Continuation Instruction

Continue the Universal Caste Atrocities Act project from the verified 2026-09-06 Phase 1 website full-audit closure point and cumulative Phase 1 acceptance audit.

First read `PROJECT_STATE.md`, `NEXT_CHAT.md`, `project-state/PH1_CONTROL_MATRIX_2026-09-06.md`, `project-state/PH1_ACCEPTANCE_AUDIT_2026-09-06.md`, `project-state/PH1_CENTRAL_LAW_CLOSURE_2026-09-06.md`, `project-state/PH1_ISSUES_REGISTER_RECONCILIATION_2026-09-06.md`, `project-state/PH1_MANUAL_SCAVENGERS_BNSS_TRANSITION_2026-09-06.md`, `ISSUES_REGISTER.md`, `DECISIONS_LOG.md` and `legislation/STATE_IMPLEMENTATION_INVENTORY.md`.

36/36 State/UT inventories are complete. No State/UT remains unresearched. Do not repeat completed jurisdiction research unless the formal reopening rule is met.

The preserved historical source-ledger baseline remains `MASTER_IDS=261`, `JURISDICTION_LEDGER_FILES=29`, `JURISDICTION_LEDGER_IDS=571`, `MISSING_FROM_MASTER=377`, `MASTER_ONLY_IDS=67`. The later 32-file/628-ID/434-gap filesystem enumeration is a post-baseline delta only. Do not modify the master ledger for website synchronization.

The current Pages artifact is verified by run #452 after remediation of the run #446 heading-hierarchy defects. The full static audit is PASS. Live HTTP/settings verification remains unavailable through the connector. Do not repeat the website audit absent a new control defect.

The SC/ST Act current-text/version question is closed with qualification. The SC/ST Rules Annexure-II apparent 1986/2001 discrepancy is closed using the official Ministry-hosted Rules PDF.

The stale PH1-ISSUE-001 and PH1-ISSUE-014 rows have an authoritative reconciliation record in `project-state/PH1_ISSUES_REGISTER_RECONCILIATION_2026-09-06.md`; synchronize only those two physical rows before further substantive work.

PH1-ISSUE-016 has been advanced to ADVANCED WITH QUALIFICATION by `project-state/PH1_MANUAL_SCAVENGERS_BNSS_TRANSITION_2026-09-06.md`. Do not repeat that targeted verification. Next substantive work should address PH1-ISSUE-015, PH1-ISSUE-017, PH1-ISSUE-008 or another specifically selected unresolved Central/transition dependency using primary-source closure rules.

Do not repeat completed work, the historical 377-ID comparison, run #397, run #438, run #448 artifact inspection, Bill drafting, policy-superiority/necessity analysis, constitutional-validity analysis or Phase 2 case-law research.

## 2026-09-06 Website Remediation Continuation

The website/source/build remediation pass is closed and merged to `main`. Do not repeat the audit-only baseline or the remediation work already completed.

Current authoritative position:
- Phase 1 ACTIVE; substantive acceptance NOT YET SATISFIED.
- 36/36 State/UT substantive inventories complete. No State/UT remains unresearched.
- Central current-law completeness, BNS/BNSS/BSA transition, jurisdiction currentness and instrument residuals remain open.
- SC/ST Act current-text/version question CLOSED WITH QUALIFICATION.
- SC/ST Rules Annexure-II discrepancy CLOSED.
- Manual Scavengers BNSS transition PH1-ISSUE-016 ADVANCED WITH QUALIFICATION.

Website control position:
- Committed website HTML/routes are build output, not authoritative source. Assets remain committed.
- `scripts/build_website_v2.py` is the production builder and now computes current counts, renders Markdown tables and prevents embedded duplicate H1 headings.
- Codespaces and Pages use the same v2 production builder.
- Current Pages deployment was run #460 from head `c667a9ed42bb892136f01d5f5ce0ebbcb81eab25`; artifact ID `9977341147`; digest `sha256:824ce74957da05c05ed7cddd708ff5f66ced4567ce80e91df5b6665fea854465`. Deployment completed successfully.
- Direct HTTP validation of the public root remains UNVERIFIED because the tool environment returns a cache miss.

Next task:
1. Read `PROJECT_STATE.md`, `NEXT_CHAT.md`, `RESEARCH_LEDGER.md`, `ISSUES_REGISTER.md`, `DECISIONS_LOG.md` and the latest project-state control records.
2. Reconcile the current central-law and transition residuals against the authoritative source map.
3. Verify any remaining currentness/instrument residuals only where required for Phase 1 acceptance.
4. Update the relevant research and control ledgers with traceable primary sources.
5. Do not begin Bill drafting, policy-superiority/necessity analysis, constitutional-validity analysis or Phase 2 case-law research.
6. Do not repeat completed State/UT inventories, Ladakh, Lakshadweep, Puducherry, SC/ST Act current-version closure, Rules Annexure-II resolution or the completed website remediation unless a targeted verification defect requires it.
