# Next Chat Handoff

## Authoritative Rule
`PROJECT_STATE.md`, repository artifacts, verified decisions and documented unresolved issues are authoritative. This file is downstream.

## Current Phase
Phase 1, Existing-Law Baseline and Source Map: ACTIVE.
Phase 1 acceptance criteria: NOT YET SATISFIED.

## Current Position
33 of 36 States/UTs have substantive Phase 1 inventories. Jammu and Kashmir is the 33rd completed jurisdiction. Ladakh, Lakshadweep and Puducherry remain unresearched.

Do not repeat Jammu and Kashmir. Do not begin the remaining three jurisdictions.

## Website/Source-Ledger Defect Position

The verified #374 Pages artifact contained 33 research pages and 33 source-set pages, with 25 source-set pages empty. The master source ledger lacks later jurisdiction-specific IDs such as `JK-001` and `MZ-STATE-001`, while corresponding substantive jurisdiction ledgers exist.

The same artifact exposed `DECISIONS_LOG.md` and a project-management instruction in `law/priority-central-legislation-screening.html`.

The previous master-ledger integration narrative is therefore not accepted as proof of full later-jurisdiction integration. The substantive master ledger remains unmodified by this remediation.

## Control Decision Already Recorded

`project-state/WEBSITE_SOURCE_LEDGER_CONTROL_DECISION_2026-09-06.md` records the production decision:

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

## Exact Gap Status

The exact source-ID delta is intentionally not asserted until the first non-cancelled post-remediation workflow run produces the control artifact.

Latest Pages runs:
- #374: SUCCESSFUL, pre-remediation artifact containing the identified defects.
- #385: queued/in progress during remediation, superseded by later control commits.
- #386: CANCELLED by workflow concurrency.
- #387: pending during queue transition.
- #388: queued as of the latest repository check, head commit `c4fbd1ee8583617e1c138bc58e9b6320c709a512`.

Do not treat a queued/pending run as successful. Do not claim exact gap completion until its control artifact is retrieved and inspected.

## Next Required Action

1. Wait for the non-cancelled post-remediation Pages run to complete.
2. Retrieve the `source-ledger-control` workflow artifact.
3. Record the exact `MISSING_IDS` set and per-ledger counts in `project-state/WEBSITE_SOURCE_LEDGER_GAP_2026-09-06.md`.
4. Correct the control/reconciliation narrative if the five-ledger integration record overstated later-jurisdiction integration. Do not alter the substantive master ledger.
5. Inspect the Pages job result and generated-site validation result.
6. If successful, inspect the Pages artifact for source-set population and absence of project-control leakage. Live Pages publication remains independently unverified unless direct tool evidence becomes available.
7. Update `PROJECT_STATE.md`, this file and the website mismatch record with the verified run result.
8. Preserve the Phase 1 substantive gate.

## Explicitly Closed

No Ladakh research.
No Lakshadweep research.
No Puducherry research.
No other new State/UT substantive research.
No Bill drafting.
No policy-superiority/necessity analysis.
No constitutional-validity analysis.
No Phase 2 case-law research.
No repetition of the completed 2026-09-06 audit, cumulative state-control reconciliation, State Implementation Inventory reconciliation, completed source-ledger integration or zero-drift test except targeted verification required for this defect.

## Do NOT Repeat

Do NOT repeat Jammu and Kashmir.
Do NOT repeat substantive State/UT searches.
Do NOT search for new sources for the source-ledger gap. The gap must be computed from committed repository ledgers only.
Do NOT modify `research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md` until the control comparison and integration-status correction are explicit.
Do NOT treat jurisdiction-ledger fallback as master-ledger integration.
Do NOT claim the website is synchronized until the post-remediation artifact is verified.
Do NOT begin Ladakh, Lakshadweep or Puducherry.
Do NOT draft the Bill.
Do NOT conduct policy-superiority/necessity analysis.
Do NOT conduct constitutional-validity analysis.
Do NOT begin Phase 2 case-law research.
