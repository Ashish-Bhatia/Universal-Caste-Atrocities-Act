# Website Phase 1 Synchronization Verification

Date: 2026-09-06

## Result

CURRENT POST-PUDUCHERRY PAGES BUILD: PASS.

GitHub Actions run #438, head commit `013797f0a1180e22c16d11b9ad467d716dd3e6b1`, completed successfully through Pages deployment.

Pages artifact:
- name: `github-pages`
- artifact ID: `9976731876`
- SHA-256: `d292344a73fb8c045cb0a7ffd363e79130a1705c5a44325dd81d81c5a47575b8`

## Workflow controls verified

- website builder compilation: PASS
- source-ledger control step: PASS as a workflow step; its current filesystem enumeration is recorded separately as a post-baseline delta
- website build: PASS
- Phase 1 website synchronization: PASS, `completed=36`, `total=36`, `state_pages=36`, `source_pages=36`
- public sanitization: PASS
- generated-site validation: PASS
- Pages configuration: PASS
- Pages artifact upload: PASS
- Pages deployment: PASS

The build generated 90 HTML pages, including 36 jurisdiction research pages and 36 jurisdiction source pages.

## Independent artifact inspection

The downloaded Pages artifact was independently inspected after extraction.

Verified:
- 90 HTML pages
- 36 state/UT research pages
- 36 state/UT source pages
- Puducherry research route present
- Puducherry source route present and non-empty
- public home page contains `36/36`
- public home page does not contain `33/36`
- Petition / Support pathway present on all HTML pages
- no broken local links
- responsive `@media` rules present
- `:focus-visible` accessibility rules present
- no internal project-control filenames detected in generated HTML

## Source-ledger boundary

The historical verified control baseline remains unchanged:

`MASTER_IDS=261`
`JURISDICTION_LEDGER_FILES=29`
`JURISDICTION_LEDGER_IDS=571`
`MISSING_FROM_MASTER=377`
`MASTER_ONLY_IDS=67`

The current filesystem enumeration in run #438 was 32 jurisdiction ledger files, 628 jurisdiction-ledger IDs and 434 IDs absent from the master. This is a post-baseline delta caused by the three later jurisdiction ledgers for Ladakh, Lakshadweep and Puducherry. It does not alter the master ledger and does not constitute master-ledger integration.

## Publication limitation

The Actions deployment itself succeeded and the workflow exposed the Pages environment URL `https://ashish-bhatia.github.io/Universal-Caste-Atrocities-Act/` in its deployment environment result. The connector still does not provide independent browser-level HTTP inspection or Pages Settings inspection. Therefore this record verifies workflow deployment and artifact content, not independent live-URL HTTP availability.
