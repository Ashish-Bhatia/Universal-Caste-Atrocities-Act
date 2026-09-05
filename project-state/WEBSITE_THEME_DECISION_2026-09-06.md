# Website Theme Decision

Date: 2026-09-06

## Decision

Pico CSS 2.1.1 is selected as the controlled open-source theme candidate for the public research website. Pico CSS is MIT licensed and is designed as a lightweight semantic HTML framework.

Official project: https://github.com/picocss/pico
Official documentation: https://picocss.com/

## Rationale

- The existing site is a hand-built static HTML/CSS system.
- Pico provides a mature baseline for typography, tables, forms, responsive spacing, focus states and light/dark presentation without JavaScript.
- The existing custom classes and information architecture should be preserved rather than replaced wholesale.
- The theme must remain compatible with the evidence-first research presentation and accessible table rendering.

## Controlled integration status

A separate candidate file has been added at `website/assets/pico-theme.css`. It imports the pinned Pico 2.1.1 stylesheet from jsDelivr and defines project-specific Pico variables.

The candidate is NOT YET wired into `scripts/build_website_v2.py` and is therefore NOT part of the current production Pages build. This is deliberate. The production builder and current deployment remain unchanged until the theme is rendered and audited against the existing 90-page validation controls.

## Required next integration checks

1. Wire the candidate after the current production stylesheet or convert the current stylesheet to an explicit cascade strategy.
2. Build all generated pages.
3. Check tables, navigation, cards, responsive layouts, source pages, state pages and accessibility focus states.
4. Confirm no content, route, count, source-ledger or heading-hierarchy regression.
5. Deploy only after the static audit passes.

## Scope protection

This decision changes presentation only. It does not change research scope, evidence grades, legal conclusions, acceptance criteria or the authoritative source-ledger boundary.
