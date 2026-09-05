# Website Source-Set and Public-Content Mismatch Record

Date: 2026-09-06
Phase: Phase 1
Workstream: website/source-ledger synchronization control only
Status: EXACT GAP VERIFIED; FALLBACK BUILD FAILURE OPEN

## Verified pre-remediation defect

Pages run #374 contained 33 State/UT research pages and 33 State/UT source-set pages. Independent artifact inspection found 25 empty source-set pages and 8 non-empty source-set pages. The master source ledger did not contain later jurisdiction-specific IDs such as `JK-001` and `MZ-STATE-001`. The same artifact exposed `DECISIONS_LOG.md` and a project-management instruction in `law/priority-central-legislation-screening.html`.

## Post-remediation control result

The first non-cancelled post-remediation Pages run was #389, head commit `180663c0f64ba8970a239f3d828e91363709a9ad`. It completed with `failure`.

The `source-ledger-control` artifact was successfully retrieved and inspected. Artifact ID: `9976069045`. SHA-256: `989f586939b111e6902f69c6e59ac9611c1b19f9e71eea12577253d49bde6c6e`.

Exact deterministic comparison:
- `MASTER_IDS=261`
- `JURISDICTION_LEDGER_FILES=29`
- `JURISDICTION_LEDGER_IDS=571`
- `MISSING_FROM_MASTER=377`
- `MASTER_ONLY_IDS=67`

The exact 377-ID `MISSING_IDS` set and all per-ledger totals are recorded in `project-state/WEBSITE_SOURCE_LEDGER_GAP_2026-09-06.md`.

## Control determination

The prior master-ledger integration narrative is not accepted as proof of full later-jurisdiction integration. The exact comparison establishes that the five previously identified later contributors, Gujarat, Haryana, Himachal Pradesh, Kerala and Madhya Pradesh, have zero IDs missing from the master, but nineteen of the 29 jurisdiction-specific source ledgers scanned by the control have one or more IDs absent from the master.

The master State Implementation Source Ledger remains unchanged by this remediation. No master-ledger integration is inferred from jurisdiction-ledger fallback.

## Website source-set decision

The production website uses a controlled jurisdiction-ledger fallback. Master-ledger rows remain labelled `Master ledger`. Rows present in a jurisdiction-specific substantive source ledger but absent from the master are labelled `Jurisdiction-ledger fallback`. The fallback does not constitute master-ledger integration.

A completed jurisdiction with neither master rows nor a controlled local-ledger fallback is a build failure. Silent empty source-set publication is prohibited.

## Post-remediation build failure

Run #389 failed in `scripts/build_website_v2.py` with:

`CONTROL FAILURE: completed jurisdiction has no controlled source rows: Arunachal Pradesh`

The failure is consistent with the selected control rule. Arunachal Pradesh has no substantive local source ledger recognized by the builder and its referenced source IDs are absent from the master. The build therefore stopped rather than publishing an empty source set.

Because the build failed, the generated-site validation, Pages artifact upload and deployment steps were skipped. No generated Pages artifact exists from run #389. Live GitHub Pages publication is not claimed.

## Public-content controls

The production workflow still contains validation for:
- repository-navigation links;
- `PROJECT_STATE.md`;
- `NEXT_CHAT.md`;
- `RESEARCH_LEDGER.md`;
- `ISSUES_REGISTER.md`;
- `DECISIONS_LOG.md`;
- `BASELINE_AUDIT.md`;
- the identified project-management phrases;
- empty completed-jurisdiction source pages.

Those controls were present in the committed workflow, but their post-remediation runtime result was not reached in run #389 because the builder failed earlier. Therefore absence of leakage in a successful post-remediation generated artifact is not yet independently verified.

## Controlled records

- `scripts/verify_website_source_sync.py` performs the deterministic source-ID comparison.
- `scripts/build_website_v2.py` is the production builder and implements master/fallback provenance.
- `scripts/sanitize_public_html.py` removes the identified `DECISIONS_LOG.md` reference from generated public HTML.
- `.github/workflows/pages.yml` compiles the controls, preserves the exact comparison output as an artifact, builds the site, sanitizes generated HTML, validates public-content boundaries, rejects empty source pages, uploads the Pages artifact and deploys only after validation.
- `project-state/WEBSITE_SOURCE_LEDGER_GAP_2026-09-06.md` records the exact post-remediation control comparison and workflow result.

## Scope boundary

No State/UT substantive research was repeated.
No Ladakh, Lakshadweep or Puducherry research was performed.
No Jammu and Kashmir substantive research was repeated.
No Bill drafting, policy-superiority/necessity analysis, constitutional-validity analysis or Phase 2 case-law research was performed.
No substantive master source ledger modification was performed.
