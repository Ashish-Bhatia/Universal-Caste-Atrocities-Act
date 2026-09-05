# Website and Codespaces Remediation Record

Date: 2026-09-06

## Scope

This is an infrastructure and publication-layer workstream. It does not authorize or perform new State/UT substantive research, Bill drafting, policy-superiority/necessity analysis, constitutional-validity analysis or Phase 2 case-law research.

## Website findings

The previous public interface exposed repository links as substitutes for jurisdiction and law pages and mixed research content with project-control information.

The public publication boundary is now:

1. Publish substantive legal and implementation research only.
2. Give every completed State/UT a dedicated research page.
3. Give every completed State/UT a dedicated source-set page.
4. Give each existing-law research document its own page when the source document exists.
5. Keep PROJECT_STATE, NEXT_CHAT, issue registers, decision logs and other project-management controls out of the public interface.
6. Use internal Pages navigation rather than GitHub repository links for public research navigation.
7. Generate sitemap.xml, robots.txt and 404.html.
8. Validate the generated site before Pages deployment.

## Website implementation

`scripts/build_website.py` is now a deterministic multi-page static-site generator. It reads:

- `legislation/STATE_IMPLEMENTATION_INVENTORY.md`
- `legislation/states/*.md` substantive jurisdiction inventories
- selected `legislation/*.md` existing-law research records
- `research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md`

It creates:

- public research home
- research subject page
- State/UT index
- one State/UT research page per completed inventory
- one State/UT source-set page per completed inventory
- existing-law index
- one page per available existing-law research document
- source index
- methodology page
- 404 page
- sitemap
- robots.txt

The builder deletes stale generated HTML under the generated website directories before rebuilding. It verifies every completed jurisdiction has a generated page.

`.github/workflows/pages.yml` now compiles the builder, runs the build, validates required pages, rejects generated HTML containing the repository navigation URL, uploads the generated website artifact and deploys it to GitHub Pages.

## Codespaces finding

The 2026-09-06 screenshot shows the Codespaces rebuild in the container-image retrieval stage. Multiple image layers display active download progress while other layers are waiting. The screenshot does not show a Python `postCreateCommand` failure.

The selected image, `mcr.microsoft.com/devcontainers/python:3-3.12-bookworm`, is a valid Microsoft Dev Container image tag. The repository configuration now runs `python3 scripts/build_website.py` after container creation through `postCreateCommand`.

Live Codespaces administration remains unavailable through the connector. Therefore the following remain verification items rather than PASS findings:

- container rebuild completes after image download;
- `postCreateCommand` executes successfully;
- generated website files appear in the Codespace;
- Explorer configuration is loaded;
- remote connection becomes ready.

## Verification boundary

GitHub Pages live publication remains independently unverified because the connector does not expose Pages administration/live-site verification.

The repository-side changes are implementation-complete. Production verification remains pending until the deployment result and live publication are observable.

## Source basis

- Microsoft Dev Container Python image documentation and current tag registry: `https://mcr.microsoft.com/en-us/product/devcontainers/python/about`
- Microsoft Artifact Registry tag record for `devcontainers/python:3-3.12-bookworm`: `https://mcr.microsoft.com/en-us/artifact/mar/devcontainers/python/tag/3-3.12-bookworm`
- Repository source files and generated build controls listed above.
