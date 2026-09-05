# Next Chat Handoff

## Authoritative Rule
`PROJECT_STATE.md`, repository artifacts, verified decisions and documented unresolved issues are authoritative. This file is downstream. Do not treat this continuation instruction as an independent source of truth.

## Current Phase
Phase 1, Existing-Law Baseline and Source Map: ACTIVE.
Phase 1 acceptance criteria: NOT YET SATISFIED.

## Current Position
33 of 36 States/UTs have substantive Phase 1 inventories. Jammu and Kashmir is the 33rd completed jurisdiction and remains PROCEED/CLOSE WITH LIMITATIONS with PH1-ISSUE-JK-001 through PH1-ISSUE-JK-018 open, including the unresolved Rule 8 Protection Cell contradiction and currentness residuals.

Remaining unresearched jurisdictions:
1. Ladakh
2. Lakshadweep
3. Puducherry

## Current Control-Remediation Gate

The master State Implementation Inventory reconciliation is complete.
The master State Implementation Source Ledger integration was completed for the five explicitly contributing later ledgers recorded in the integration report: Gujarat, Haryana, Himachal Pradesh, Kerala and Madhya Pradesh.
The independent zero-drift control record remains valid for preservation of the pre-integration master content and the five controlled additions.

A new website verification has identified two publication/control defects:
1. The committed master source ledger does not contain later jurisdiction-specific IDs such as `JK-001` and `MZ-STATE-001`, although those jurisdiction-specific source ledgers exist. The public source-set pages for 25 of 33 completed jurisdictions are therefore empty in the verified Pages artifact.
2. One generated existing-law page, `law/priority-central-legislation-screening.html`, exposes the project-control filename `DECISIONS_LOG.md` and project-management instructions, contrary to the public research-only content boundary.

Controlled defect record:
- `project-state/WEBSITE_SOURCE_SET_MISMATCH_2026-09-06.md`

## Website / Repository State

The public website build is repository-driven. `scripts/build_website.py` generates a production-oriented, multi-page public research library from substantive repository research records.

Public website boundary:
- Publish actual legal and jurisdictional implementation research only.
- Do not publish project-state controls, issue registers, decision logs or continuity prompts.
- Give every completed State/UT a dedicated research page.
- Give every completed State/UT a dedicated source-set page.
- Give each available existing-law research document its own page.
- Use internal Pages navigation rather than GitHub repository links.
- Generate `sitemap.xml`, `robots.txt` and `404.html`.
- Reject generated HTML containing the repository navigation URL.

The builder now cleans stale generated HTML, renders all completed jurisdiction records, renders jurisdiction source sets, renders existing-law research pages and verifies every completed jurisdiction has a generated page.

The builder's current source-set implementation reads only `research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md`. Because the master ledger does not contain all later jurisdiction-specific source IDs, 25 generated source-set pages are empty even though the corresponding jurisdiction-specific source ledgers exist.

The builder's current project-control stripping is incomplete. One generated existing-law page contains the literal `DECISIONS_LOG.md` filename and a project-record instruction. The current workflow validation does not detect this class of leakage.

The Pages workflow `.github/workflows/pages.yml` compiles the builder, prepares the Delhi compatibility alias, builds the site, validates required outputs and public-link policy, then deploys the generated `website/` artifact.

Workflow run #374 succeeded. Independent inspection of its artifact confirmed:
- 33 State/UT research pages.
- 33 State/UT source-set pages.
- 9 existing-law pages.
- 82 sitemap URLs.
- No repository-navigation links.
- No broken internal HTML links.
- 25 empty source-set pages caused by the master-ledger/source-set synchronization defect.
- One project-control filename leakage in `law/priority-central-legislation-screening.html`.

The workflow's current validation does not detect either empty source-set pages or project-control filename leakage.

GitHub Pages live publication is NOT independently verified because Pages administration/live-site verification is not exposed by the connector. The user-supplied screenshot shows the expected public URL rendering, but it is not treated as independent tool verification.

## Codespaces / Repository State

`.devcontainer/devcontainer.json` runs `ln -sf DELHI.md legislation/states/DELHI_NCT.md && python3 scripts/build_website.py` as `postCreateCommand` after container creation. The image remains `mcr.microsoft.com/devcontainers/python:3-3.12-bookworm`, a valid Microsoft Dev Container image tag.

The 2026-09-06 screenshot shows active container image-layer downloads. Treat this as the image retrieval stage, not as evidence of a failed website build or failed post-create command. The next verification point remains whether the container completes after the image download and the post-create command runs.

Codespaces administration/synchronization remains unavailable through the connector.

## Explicitly Closed for This Workstream
- No Ladakh research.
- No Lakshadweep research.
- No Puducherry research.
- No other new State/UT substantive research.
- No Bill drafting.
- No policy-superiority/necessity analysis.
- No constitutional-validity analysis.
- No Phase 2 case-law research.
- No reopening of completed State/UT research unless a genuine evidentiary/control defect requires targeted verification.
- Do not repeat the 2026-09-06 cumulative state-control reconciliation or independent audit.
- Do not repeat completed State/UT inventories or Jammu and Kashmir research.
- Do not treat the new website/source-set defects as authorization for substantive State research.

## Remaining Phase 1 Work

The next task is a targeted control reconciliation of the website/source-set and public-content defects. This is not a new State/UT workstream.

Required sequence:
1. Re-read `PROJECT_STATE.md`, `NEXT_CHAT.md`, `research/STATE_IMPLEMENTATION_SOURCE_LEDGER_RECONCILIATION_2026-09-06.md`, `project-state/PH1_MASTER_SOURCE_LEDGER_INTEGRATION_REPORT_2026-09-06.md`, `project-state/PH1_MASTER_SOURCE_LEDGER_ZERO_DRIFT_2026-09-06.md`, `project-state/WEBSITE_SOURCE_SET_MISMATCH_2026-09-06.md`, `scripts/build_website.py`, `.github/workflows/pages.yml`, `legislation/STATE_IMPLEMENTATION_INVENTORY.md` and the relevant later jurisdiction-specific source ledgers.
2. Reconcile the exact source-ID set present in jurisdiction-specific ledgers but absent from the master ledger. Do not repeat source searches.
3. Determine whether the 2026-09-06 master-ledger reconciliation record overstated later-jurisdiction integration status. Do not modify the substantive master ledger until the control comparison is explicit.
4. Decide and record whether the public source-set generator must remain master-ledger-only or use a controlled jurisdiction-ledger fallback. The decision must preserve source provenance and must not conceal the master-ledger gap.
5. Add build-time validation preventing silent empty source-set pages for completed jurisdictions unless the absence is explicitly controlled and recorded.
6. Add build-time public-content validation for project-control filenames and project-management instructions.
7. Remove or appropriately sanitize the identified `DECISIONS_LOG.md` leakage from the generated public page without altering the underlying substantive research record.
8. Re-run the Pages build only after the control decision and implementation are recorded.
9. Re-check the live-publication limitation. Do not claim independent live verification without direct tool evidence.
10. Preserve the Phase 1 substantive gate and do not open Ladakh, Lakshadweep or Puducherry.

## Continuity Constraints

Preserve all existing jurisdiction-specific issue IDs, decision IDs and source IDs. Do not fabricate cumulative IDs. Treat cumulative indexes as control metadata and jurisdiction-specific records as substantive authority. Do not treat search silence as absence. Do not repeat a materially identical search without a new retrieval route, repository update, document identifier or reasoned search expansion.

## Do NOT Repeat

Do NOT repeat the independent 2026-09-06 audit, cumulative state-control reconciliation, master State Implementation Inventory reconciliation, completed master source-ledger integration or zero-drift control test except for targeted verification necessary to resolve the newly identified website publication defects.
Do NOT repeat completed State/UT inventories or Jammu and Kashmir research.
Do NOT begin Ladakh, Lakshadweep or Puducherry without an explicit authorized workstream.
Do NOT draft the Bill.
Do NOT conduct policy-superiority/necessity analysis.
Do NOT conduct constitutional-validity analysis.
Do NOT begin Phase 2 case-law research.
