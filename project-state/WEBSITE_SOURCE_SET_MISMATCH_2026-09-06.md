# Website Source-Set Mismatch Record

Date: 2026-09-06
Phase: 1, Existing-Law Baseline and Source Map
Workstream: website publication/control verification only
Status: OPEN

## Finding

The Pages production workflow is succeeding, but the generated public source-set pages do not consistently contain source rows.

The run #374 Pages artifact contains 33 State/UT research pages and 33 State/UT source-set pages. Independent artifact inspection found 25 empty source-set pages and 8 non-empty source-set pages.

The 25 empty source-set pages are:

- Andaman and Nicobar Islands
- Arunachal Pradesh
- Assam
- Bihar
- Chandigarh
- Chhattisgarh
- Dadra and Nagar Haveli and Daman and Diu
- Delhi (NCT)
- Jammu and Kashmir
- Karnataka
- Kerala
- Manipur
- Meghalaya
- Mizoram
- Nagaland
- Odisha
- Punjab
- Rajasthan
- Sikkim
- Tamil Nadu
- Telangana
- Tripura
- Uttar Pradesh
- Uttarakhand
- West Bengal

The 8 non-empty source-set pages are Andhra Pradesh, Goa, Gujarat, Haryana, Himachal Pradesh, Jharkhand, Madhya Pradesh and Maharashtra.

## Verified artifact result

Pages workflow run #374 succeeded on head commit `e2d1c34a0510724a3a402d5a04c79637fe8b6454`.

The downloaded `github-pages` artifact has SHA-256:

`f026601244d056c3f203563e2acc8dbaa1ef533e8973ac9d530a5489e10216c0`

The artifact contains:

- 33 State/UT research pages.
- 33 State/UT source-set pages.
- 9 existing-law research pages.
- `index.html`, `research.html`, `states.html`, `law.html`, `sources.html`, `methodology.html`, `404.html`.
- `sitemap.xml` with 82 URLs.
- `robots.txt`.
- No generated HTML containing the repository navigation URL.
- No broken internal HTML links in the artifact.

Independent artifact parsing found 25 source-set pages containing the builder's `No matching master-ledger rows were found for this research record.` message. Eight source-set pages contain master-ledger tables.

## Repository-level cause

The committed master State Implementation Source Ledger currently contains the integrated rows through Maharashtra plus the controlled Gujarat, Haryana, Himachal Pradesh, Kerala and Madhya Pradesh additions. The committed master blob was independently read back and does not contain later jurisdiction-specific IDs such as `MZ-STATE-001` or `JK-001`.

The jurisdiction-specific ledgers for later jurisdictions do exist. For example, `research/states/JAMMU_KASHMIR_SOURCE_LEDGER.md` contains JK-001 through JK-022, but the generated Jammu and Kashmir source page is empty because `scripts/build_website.py` reads only `research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md` when building source-set tables.

This is inconsistent with the broader 2026-09-06 reconciliation narrative stating that later jurisdiction-specific source ledgers were already represented in the master ledger. The master integration report itself only records five contributing ledgers and 97 newly integrated IDs, which explains the current master content.

## Control significance

This is a newly identified control defect. It does not invalidate the underlying jurisdiction research records or the completed zero-drift test against the pre-integration master. It does mean the website source-set publication layer is not synchronized with all completed jurisdiction source ledgers.

The defect must not be resolved by silently modifying substantive State inventories or by treating website output as evidence that a source ledger is integrated.

## Required remediation

1. Reconcile the master-ledger integration position against the jurisdiction-specific source ledgers without repeating searches.
2. Determine the exact set of source IDs absent from the master ledger after the 2026-09-06 integration.
3. Correct the master-ledger control record if its later-jurisdiction integration status is overstated.
4. Decide whether the website should use the master ledger exclusively or use a controlled jurisdiction-ledger fallback when master rows are absent. Record the decision before implementation.
5. Add build validation so a completed jurisdiction source page cannot silently publish as an empty source set without an explicit controlled absence.
6. Re-run the Pages build only after the control position is corrected.

## Scope boundary

No State/UT substantive research was repeated.
No Ladakh, Lakshadweep or Puducherry research was performed.
No Jammu and Kashmir substantive research was repeated.
No Bill drafting, policy-superiority/necessity analysis, constitutional-validity analysis or Phase 2 case-law research was performed.
