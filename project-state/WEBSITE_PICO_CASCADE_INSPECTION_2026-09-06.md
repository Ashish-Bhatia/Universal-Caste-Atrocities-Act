# Website Theme Cascade Inspection

Date: 2026-09-06
Status: SUPERSEDED BY TABLER/OPEN PROPS REDESIGN

## Historical inspection

The earlier inspection evaluated Pico CSS 2.1.1 as a candidate layer. That candidate is no longer the selected third-party foundation.

## Current controlled cascade

The historical `website/assets/pico-theme.css` filename is retained for build compatibility. Its current contents load Tabler 1.4.0 and Open Props 1.7.23. The generated HTML continues to load this foundation before `assets/site.css`. The Pages workflow then appends `website/assets/site-overrides.css` to the generated `site.css`, making the project presentation layer last.

The current design therefore follows this order:

1. Tabler 1.4.0, MIT-licensed UI foundation based on Bootstrap 5.
2. Open Props 1.7.23, MIT-licensed design-token layer.
3. Existing `site.css` project styles.
4. `site-overrides.css`, final project presentation and responsive/accessibility layer.

## Redesign controls

The final project layer was redesigned to address readability defects identified in the existing site:

- reduced oversized display typography;
- stronger body-text contrast and line-height;
- justified long-form paragraphs on desktop, with mobile left alignment;
- fixed evidence-table column proportions;
- normal text wrapping and overflow-safe source/finding cells;
- consistent left alignment and top vertical alignment in tables;
- alternating table rows and hover state;
- restrained card borders and shadows;
- clearer navigation and focus states;
- responsive one-column fallback on narrow screens.

## Verification status

The CSS/source changes are committed. They are not yet a verified replacement for Pages run #479. A new Pages workflow run and artifact inspection are required before the redesign is declared deployed/verified.

## Scope protection

No research scope, legal conclusion, evidence grade, source-ledger boundary or Phase 1 acceptance criterion was changed by the presentation redesign.
