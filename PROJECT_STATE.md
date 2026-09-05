# Universal Caste Atrocities Act

## Project State
- Phase 1, Existing-Law Baseline and Source Map: ACTIVE.
- Authoritative repository: `Ashish-Bhatia/Universal-Caste-Atrocities-Act`.
- Phase 1 acceptance criteria: NOT YET SATISFIED.
- Current state is determined by repository evidence plus verified decisions and documented unresolved issues. `NEXT_CHAT.md` is downstream and is not a source of truth.
- Methodology: evidence-first, primary-source preference, explicit evidence grading, no presumed necessity, constitutionality or superiority.

## State/UT Position
34 of 36 Indian States/UTs have substantive Phase 1 jurisdiction inventories.

Completed sequence:
Andhra Pradesh, Arunachal Pradesh, Assam, Bihar, Chhattisgarh, Goa, Gujarat, Haryana, Himachal Pradesh, Jharkhand, Karnataka, Kerala, Madhya Pradesh, Maharashtra, Manipur, Meghalaya, Mizoram, Nagaland, Odisha, Punjab, Rajasthan, Sikkim, Tamil Nadu, Telangana, Tripura, Uttar Pradesh, Uttarakhand, West Bengal, Andaman and Nicobar Islands, Chandigarh, Dadra and Nagar Haveli and Daman and Diu, Delhi (NCT), Jammu and Kashmir, Ladakh.

Jammu and Kashmir remains the 33rd completed jurisdiction and is classified PROCEED/CLOSE WITH LIMITATIONS. Its PH1-ISSUE-JK-001 through PH1-ISSUE-JK-018 remain open. The Rule 8 Protection Cell contradiction remains unresolved.

Ladakh is the 34th completed jurisdiction and is classified PROCEED/CLOSE WITH LIMITATIONS. Its residuals PH1-ISSUE-LA-001 through PH1-ISSUE-LA-018 are recorded in `project-state/LADAKH_ISSUES_2026-09-06.md`.

Remaining unresearched jurisdictions:
1. Lakshadweep
2. Puducherry

## Control Remediation Status, 2026-09-06

The website/source-ledger remediation is CLOSED AND VERIFIED for the public rendering/control layer. The exact 377-ID master-versus-jurisdiction comparison remains preserved and unchanged. The substantive master State Implementation Source Ledger was not modified.

Authoritative control matrix: `project-state/PH1_CONTROL_MATRIX_2026-09-06.md`.

Remediation closure report: `project-state/REMEDIATION_CLOSURE_REPORT_2026-09-06.md`.

## Verified source-ledger control baseline

The exact source-ledger control comparison was independently verified from workflow artifacts and remains:
- `MASTER_IDS=261`
- `JURISDICTION_LEDGER_FILES=29`
- `JURISDICTION_LEDGER_IDS=571`
- `MISSING_FROM_MASTER=377`
- `MASTER_ONLY_IDS=67`

The exact 377-ID `MISSING_IDS` set is recorded in `project-state/WEBSITE_SOURCE_LEDGER_GAP_2026-09-06.md`.

The comparison baseline was preserved unchanged through the remediation. No IDs were copied into the master ledger.

## Website remediation result

The earlier run #389 failure is resolved. The builder defect was source-selection logic: it did not first map master-ledger rows by jurisdiction section, causing Arunachal Pradesh to appear to have no controlled source rows even though its substantive source rows are represented in the master ledger.

`scripts/build_website_v2.py` now maps master-ledger rows by jurisdiction section heading first, uses jurisdiction-ledger rows only as an explicitly labelled fallback for IDs absent from the master, rejects a completed jurisdiction with neither master rows nor controlled fallback, and reports the exact master-versus-jurisdiction ID comparison without changing it.

`scripts/sanitize_public_html.py` sanitizes internal filenames and project-management phrases across generated HTML only. `scripts/validate_public_site.py` validates page counts, route existence, navigation, header/footer, Petition / Support pathway, responsive/accessibility CSS controls, local links, source-page non-emptiness and public/internal separation.

## Verified production Pages run

GitHub Actions run #397, head commit `29fc336b5ca5293e0abfb3bb011b7a8d3cce6a6f`, completed successfully.

Successful steps verified:
- source-ledger control comparison;
- source-ledger control artifact upload;
- website build;
- production accessibility/responsive CSS application;
- public HTML sanitization;
- generated-site validation;
- Pages configuration;
- Pages artifact upload;
- Pages deployment.

Generated Pages artifact:
- name: `github-pages`
- artifact ID: `9976320948`
- SHA-256: `2245022e4732f9d4c1bd16a83f3ffdc95abad8f586479e6b3ff8f808ef99bc40`

Independent artifact inspection verified:
- 84 HTML pages;
- 33 completed-jurisdiction research pages;
- 33 completed-jurisdiction source pages;
- matching state/source route sets;
- no empty completed-jurisdiction source pages;
- no broken local links;
- header and footer on every HTML page;
- Petition / Support pathway on every HTML page;
- responsive media rules;
- focus-visible accessibility rules;
- support-button and footer styling;
- no internal control-file leakage;
- no project-management control wording;
- Arunachal Pradesh source page populated from controlled master-ledger rows.

The generated artifact is the authoritative evidence for the website build inspection. The connector still lacks direct browser-level Pages settings inspection and independent live-URL HTTP verification. Therefore deployment success is recorded as a workflow/artifact fact, not as a separately browser-verified live-site claim.

## Source-ledger synchronization boundary

The public source layer now has two controlled tiers:
- master-ledger rows are authoritative where actually integrated in the master;
- jurisdiction-ledger fallback rows may be rendered where substantive local-ledger rows exist and are absent from the master;
- fallback rows are explicitly labelled and are never treated as master-ledger integration;
- a completed jurisdiction with neither controlled master rows nor controlled fallback rows fails the build.

The 377-ID discrepancy remains unresolved as a classification/integration question. It was not hidden by website fallback and was not rewritten.

## Cumulative Control Layer

The 2026-09-06 cumulative state-control reconciliation remains preserved. The three cumulative controls contain explicit reconciliation-only indexes through Jammu and Kashmir. Ladakh's new jurisdiction-specific issue, decision and source records are substantive jurisdiction artifacts and are not represented as fabricated cumulative IDs.

## Central and Transition Residuals

Central later-instrument/current-law completeness remains open. BNS/BNSS/BSA transition verification remains open. Existing State residuals remain jurisdiction-specific. Search silence is not treated as absence.

## Website and Repository Synchronization

The repository-driven website builder remains the verified production Pages builder. Public source provenance remains separated from internal project-control files.

## Ladakh Phase 1 Position

Ladakh was researched on 2026-09-06 using the Phase 1 control matrix, primary-source hierarchy, currentness rules and reopening controls. The primary baseline includes the 2019 Reorganisation Act transition, 2021 Rule 8 Protection Cell order, 2021 Rule 9 Nodal Officer order, 2021 UT-level V&MC order, 2024 separate Ladakh ST list, current 2025 reservation framework, current 2026 Kargil V&MC activity, current 2026 Kargil PoA awareness activity and current Central scheme data. The jurisdiction is PROCEED/CLOSE WITH LIMITATIONS, not an unqualified 2026 census.

Current residuals include Rule 8 staffing/reconstitution, Rule 9 incumbent, Rule 3/Rule 10 instruments, full V&MC matrix, Rule 7 investigation audit, Special Court/Exclusive Special Court notifications, PoA SPP/ESPP roster, case-level relief/payment audit, section 15A/legal aid, Section 21(4) reporting, complete PoA/PCR instrument corpus, BNS/BNSS/BSA transition and UT expenditure reconciliation.

## Closed for This Workstream

No Lakshadweep research.
No Puducherry research.
No Bill drafting.
No policy-superiority or necessity analysis.
No constitutional-validity analysis.
No Phase 2 case-law research.
No reopening of completed jurisdiction baselines absent a genuine evidentiary/control defect.
No repetition of the completed 2026-09-06 remediation, cumulative reconciliation, verified 377-ID comparison or run #397 artifact inspection except targeted verification required by a new control defect.
No repetition of Jammu and Kashmir or Ladakh without a qualifying reopening trigger.

## Decision Gate

CUMULATIVE CONTROL RECONCILIATION: PASS.

EXACT MASTER-VERSUS-JURISDICTION SOURCE-ID CONTROL: PASS, verified and preserved.

WEBSITE FALLBACK COVERAGE / PRODUCTION BUILD: PASS, verified by run #397 and independent artifact inspection.

PUBLIC/INTERNAL SEPARATION: PASS, verified by generated artifact inspection.

WEBSITE ZERO-DRIFT CONTROL: PASS for the remediated rendering layer.

Master State Implementation Inventory reconciliation: COMPLETE through Ladakh substantive artifact addition.

Master State Implementation Source Ledger substantive content: UNCHANGED by the website remediation and by the Ladakh work. Ladakh's jurisdiction source ledger is separate and is not represented as master-ledger integration.

Master-ledger later-row integration: NOT CLOSED.

PH1-ISSUE-021: remains a qualified publication limitation because live Pages URL/settings were not independently inspected through the connector, despite successful Actions deployment.

Phase 1 substantive acceptance remains NOT YET SATISFIED.

Next authorized substantive workstream: Lakshadweep Phase 1 State/UT research.

## Latest Controlled Update

2026-09-06: completed Ladakh Phase 1 State/UT inventory as the 34th jurisdiction; created `legislation/states/LADAKH.md`, `research/states/LADAKH_SOURCE_LEDGER.md`, `project-state/LADAKH_ISSUES_2026-09-06.md` and `project-state/LADAKH_DECISIONS_2026-09-06.md`; classified Ladakh PROCEED/CLOSE WITH LIMITATIONS; preserved all open residuals; updated the State/UT master inventory; did not modify the master State Implementation Source Ledger or reopen completed jurisdictions.
