# Next Chat Handoff

## Authoritative Rule
`PROJECT_STATE.md`, repository artifacts, verified decisions and documented unresolved issues are authoritative. This file is downstream.

## Current Phase
Phase 1, Existing-Law Baseline and Source Map: ACTIVE.
Phase 1 acceptance criteria: NOT YET SATISFIED.

## Current Position
33 of 36 States/UTs have substantive Phase 1 inventories. Jammu and Kashmir is the 33rd completed jurisdiction. Ladakh, Lakshadweep and Puducherry remain unresearched.

Do not repeat Jammu and Kashmir. Do not begin the remaining three jurisdictions.

## Website/Source-Ledger Control Position

The pre-remediation #374 Pages artifact contained 33 research pages and 33 source-set pages, with 25 source-set pages empty. It also exposed `DECISIONS_LOG.md` and a project-management instruction in `law/priority-central-legislation-screening.html`.

The post-remediation control comparison is now verified from workflow run #389. The `source-ledger-control` artifact was retrieved and inspected.

Exact control totals:
- `MASTER_IDS=261`
- `JURISDICTION_LEDGER_FILES=29`
- `JURISDICTION_LEDGER_IDS=571`
- `MISSING_FROM_MASTER=377`
- `MASTER_ONLY_IDS=67`

The exact 377-ID gap and all per-ledger totals are recorded in `project-state/WEBSITE_SOURCE_LEDGER_GAP_2026-09-06.md`.

Ten of the 29 scanned jurisdiction source ledgers have zero IDs missing from the master. Nineteen have one or more IDs missing. The five previously identified later contributors, Gujarat, Haryana, Himachal Pradesh, Kerala and Madhya Pradesh, are fully represented by ID comparison. This does not establish full later-jurisdiction integration.

The substantive master source ledger remains unchanged by this remediation.

## Production Build Result

Run #389 completed with `failure`. The source-ledger control artifact upload succeeded. The production builder then failed with:

`CONTROL FAILURE: completed jurisdiction has no controlled source rows: Arunachal Pradesh`

Arunachal Pradesh has no substantive local source ledger recognized by the builder and its referenced IDs are absent from the master. The builder therefore stopped rather than publishing an empty source set.

Generated-site validation, Pages artifact upload and deployment were skipped. There is no post-remediation generated Pages artifact to inspect from run #389. Do not claim successful public synchronization or live Pages publication.

## Control Decision

`project-state/WEBSITE_SOURCE_LEDGER_CONTROL_DECISION_2026-09-06.md` remains authoritative:

- Keep the master source ledger authoritative for rows actually integrated there.
- Use a controlled jurisdiction-ledger fallback for public source rendering where a completed jurisdiction has substantive local-ledger rows absent from the master.
- Label fallback rows explicitly as `Jurisdiction-ledger fallback`.
- Never represent fallback rows as master-ledger integration.
- Fail the build for a completed jurisdiction with neither master rows nor a controlled fallback.
- Validate generated HTML for project-control filenames and project-management instructions.

## Implemented Controls

- `scripts/verify_website_source_sync.py` performs the deterministic master-versus-jurisdiction source-ID comparison.
- `scripts/build_website_v2.py` is the production builder used by Pages. It implements master/fallback provenance and rejects completed jurisdictions with no controlled source rows.
- `scripts/sanitize_public_html.py` sanitizes the identified `DECISIONS_LOG.md` reference in generated public HTML without changing the substantive research source.
- `.github/workflows/pages.yml` compiles the control scripts, runs the source-ID comparison, preserves its exact output as a workflow artifact, builds the site, sanitizes the identified leakage, rejects empty source pages and rejects project-control leakage.
- The legacy `scripts/build_website.py` remains in the repository because its direct replacement operation through the repository connector returned a SHA conflict. It is not the production Pages builder after this remediation.

## Latest Verified Workflow State

- #374: SUCCESSFUL, pre-remediation artifact containing the identified defects.
- #385: queued/in progress during remediation, superseded by later control commits.
- #386: CANCELLED by workflow concurrency.
- #387: pending during queue transition.
- #388: queued on head commit `c4fbd1ee8583617e1c138bc58e9b6320c709a512`.
- #389: completed FAILURE on head commit `180663c0f64ba8970a239f3d828e91363709a9ad`; exact control artifact retrieved and inspected.

Do not treat queued/pending/cancelled as success. Run #389 is not a successful Pages deployment.

## Next Required Action

1. Reconcile the fallback-coverage failure exposed by run #389, beginning with Arunachal Pradesh's missing controlled source-row path. This is a website/control workstream only. Do not perform new substantive State research.
2. Preserve the exact verified 377-ID comparison as the current control baseline.
3. Keep the master State Implementation Source Ledger unchanged unless a separate explicit integration decision is made after the control comparison and narrative correction.
4. After the builder/control defect is corrected, obtain a new non-cancelled Pages run and inspect its `source-ledger-control` artifact.
5. If the build succeeds, inspect the generated Pages artifact for all 33 completed jurisdiction source pages, absence of project-control filenames/instructions, absence of the identified `DECISIONS_LOG.md` leakage and preservation of repository-navigation-link validation.
6. Only then determine whether the website/source-ledger synchronization control gate passes.
7. Preserve the Phase 1 substantive gate.

## Explicitly Closed

No Ladakh research.
No Lakshadweep research.
No Puducherry research.
No other new State/UT substantive research.
No Bill drafting.
No policy-superiority/necessity analysis.
No constitutional-validity analysis.
No Phase 2 case-law research.
No repetition of the completed 2026-09-06 audit, cumulative state-control reconciliation, State Implementation Inventory reconciliation, completed source-ledger integration or zero-drift test except targeted verification required for this website/control defect.

## Do NOT Repeat

Do NOT repeat Jammu and Kashmir.
Do NOT repeat substantive State/UT searches.
Do NOT search for new sources for the source-ledger gap. The gap is now verified from committed repository ledgers.
Do NOT modify `research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md` during fallback-coverage remediation.
Do NOT treat jurisdiction-ledger fallback as master-ledger integration.
Do NOT claim the website is synchronized until a successful post-remediation build artifact is independently inspected.
Do NOT claim live GitHub Pages publication without direct evidence.
Do NOT begin Ladakh, Lakshadweep or Puducherry.
Do NOT draft the Bill.
Do NOT conduct policy-superiority/necessity analysis.
Do NOT conduct constitutional-validity analysis.
Do NOT begin Phase 2 case-law research.
