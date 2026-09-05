# Website Theme Decision

Date: 2026-09-06

## Decision

The public research website will use Tabler 1.4.0 as the open-source UI foundation, with Open Props 1.7.23 used for design-token support and a project-specific final CSS layer for the research information architecture.

Tabler is MIT licensed, based on Bootstrap 5, responsive and includes mature table, typography, navigation, card and accessibility-oriented components. Open Props is MIT licensed and provides reusable CSS design tokens. Bootstrap 5.3 is the underlying open-source layout/component ecosystem used by Tabler.

## Rationale

The prior Pico candidate was too generic for the project's research-library presentation and did not address the primary usability defects sufficiently: weak long-form readability, inconsistent table wrapping, poor column proportions, weak visual hierarchy and inconsistent alignment.

The controlled redesign therefore uses:

- Tabler for the third-party UI foundation and component conventions.
- Open Props for reusable design-token support.
- Project CSS for the evidence-library visual hierarchy, legal research tables, source cards and responsive research pages.
- No JavaScript dependency is introduced for the visual redesign.

## Controlled integration status

The historical `website/assets/pico-theme.css` filename is retained to avoid route/build churn, but its contents now load the pinned Tabler and Open Props foundations. The Pages workflow already loads this stylesheet before `site.css`, and the workflow appends `site-overrides.css` as the final project presentation layer.

The new presentation layer explicitly addresses:

1. readable body typography and restrained heading scale;
2. justified long-form research paragraphs on desktop, with left alignment on narrow screens;
3. fixed table column proportions with wrapping and horizontal overflow rather than clipped text;
4. consistent left alignment for table content and top vertical alignment;
5. zebra rows and hover state for dense evidence tables;
6. clearer navigation, cards, status chips and research panels;
7. stronger focus-visible controls;
8. responsive layouts for mobile and tablet widths.

## Required verification

A new Pages build and artifact inspection are required. The existing run #479 remains the verified prior artifact and must not be represented as verification of this redesign.

The new artifact must be checked for:

- 90-page route/count integrity;
- 36/36 public jurisdiction count;
- zero stale 33/36 text;
- third-party foundation before project CSS;
- table wrapping and readable column proportions;
- paragraph alignment and mobile fallback;
- zero broken local links;
- heading hierarchy;
- metadata completeness;
- sanitization and responsive/accessibility controls.

## Scope protection

This decision changes presentation only. It does not change research scope, evidence grades, legal conclusions, acceptance criteria, State/UT inventories or the authoritative source-ledger boundary.
