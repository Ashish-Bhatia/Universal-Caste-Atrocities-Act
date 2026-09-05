# Website Audit Control Decisions

Date: 2026-09-06

## DEC-WEB-2026-09-06-001
Run #446's rendering-control workflow pass is not treated as sufficient evidence of semantic heading correctness. Independent artifact inspection identified six h1-to-h3 heading jumps. The project therefore treats artifact-level accessibility/semantic inspection as a required supplemental control for material website changes.

Status: ACTIVE.

## DEC-WEB-2026-09-06-002
The six run #446 heading defects were remediated in `scripts/build_website_v2.py` by adding an intervening h2 section heading to the affected pages. Run #448 rebuilt and deployed successfully, and independent artifact inspection found no remaining heading hierarchy jumps.

Status: CLOSED.

## DEC-WEB-2026-09-06-003
The run #448 artifact is the current verified Pages artifact for the post-remediation website state. Its artifact digest is `sha256:580cecc882332a14f4708c36f9069b92ba307d6778eec4946719ead9b992752c`.

Status: ACTIVE until superseded by a later verified Pages artifact.

## DEC-WEB-2026-09-06-004
The historical source-ledger control baseline remains unchanged despite run #448 reporting the later filesystem state of 32 jurisdiction ledgers, 628 jurisdiction-ledger IDs and 434 IDs absent from the master. The historical `261/29/571/377/67` comparison remains authoritative for the preserved baseline. No master-ledger integration is performed for website synchronization.

Status: ACTIVE.

## DEC-WEB-2026-09-06-005
The website static/artifact audit is PASS. Independent live HTTP and GitHub Pages Settings verification remains OPEN because the available connector does not expose browser-level inspection or Pages administration state.

Status: ACTIVE.
