# GitHub Pages Run #491 Artifact Verification

Date: 2026-09-06
Status: VERIFIED FOR CURRENT TABLER/OPEN PROPS REDESIGN

## Workflow
- Workflow: Deploy GitHub Pages
- Run: #491
- Run ID: `33994656136`
- Head commit: `076337243ff1f837b163a8b2e5c1eac61326adb1`
- Conclusion: SUCCESS
- Deploy job: `101383543188`

All workflow steps completed successfully, including website build, count synchronization, accessibility/responsive overrides, rendering controls, sanitization, generated-site validation, Pages configuration, artifact upload and deployment.

## Artifact
- Name: `github-pages`
- Artifact ID: `9977739622`
- GitHub artifact digest: `sha256:23a586181daa4d92064fc818fee8ccd4c05eda5fe07e2ab66089fb24ba623489`
- Artifact archive inspected after download and extraction.

## Structural verification
- HTML pages: 90
- State/UT pages: 36
- Source pages: 36
- Law pages: 9
- Sitemap entries: 90
- 36/36 jurisdiction count present.
- No stale `33/36`, `33 of 36` or equivalent 33-jurisdiction text located.
- Every HTML page contains one H1.
- No heading-level jumps detected.
- Zero broken local links detected across all 90 HTML pages.

## Theme and cascade verification
- `assets/pico-theme.css` is retained as the historical filename and loads Tabler 1.4.0 plus Open Props 1.7.23.
- Generated HTML loads `assets/pico-theme.css` before project `assets/site.css`.
- The generated `site.css` contains the final project presentation rules, including the production overrides represented by `website/assets/site-overrides.css`.
- Table rules verified: fixed layout, explicit column proportions, normal whitespace, overflow wrapping and horizontal scrolling container.
- Table cells are left aligned.
- Long-form `.prose-card` paragraphs and list items are justified on desktop.
- Mobile media rules switch long-form paragraphs/list items to left alignment.

## Responsive and accessibility verification
- Responsive media queries are present in the generated project CSS.
- Focus-visible outlines are defined for links, buttons, inputs, cards and navigation controls.
- 180 `aria-label` attributes are present across the generated HTML set.
- No inline style attributes were detected.
- No script tags were detected in generated HTML.
- Viewport metadata present on all 90 HTML pages.
- Description metadata present on all 90 HTML pages.

## Qualification
This is artifact-level verification of the GitHub Pages workflow output. It does not independently verify live Pages HTTP delivery or Pages administrative settings beyond the successful workflow steps, because the available connector does not provide independent browser-level verification.

## Result
The current Tabler/Open Props website redesign is artifact-verified in run #491. The prior run #479 remains a historical verification point and was not repeated for inspection.
