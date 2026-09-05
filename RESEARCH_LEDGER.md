# Research Ledger

## Initialization Status

Phase 0 baseline complete. Phase 1 substantive research has now started.

## Evidence Method

- Primary authoritative sources preferred: Constitution of India, legislation and Rules, Gazette notifications, Supreme Court and High Court judgments/orders, Parliament/Digital Sansad, NCRB and Government statistics, Ministries, Law Commission, Parliamentary committees.
- Secondary sources may supplement primary sources.
- Evidence grades: A = primary authoritative, B = strong official/credible, C = reliable secondary, D = weak/unverified.
- D-grade evidence must not be the sole basis for a major conclusion.
- Material claims require traceable provenance.
- A source's existence is not proof of every proposition attributed to it. Clause-level verification is required for operative legal claims.

## Entries

| ID | Workstream | Status | Evidence Grade | Source | Finding | Verification |
|---|---|---|---|---|---|---|
| INIT-001 | Repository baseline | Verified | A | GitHub repository metadata and repository operations | Repository exists, is public, is empty, and authenticated access has admin/maintain/push/pull/triage permissions. | Verified 2026-09-05 |
| INIT-002 | Existing repository artifacts | Verified | A | GitHub repository content, branches, commits, issues | No pre-existing files, commits, branches, issues, research, drafts, datasets, workflows or website assets were found. | Verified 2026-09-05 |
| INIT-003 | Tool capability boundary | Verified | A | Available GitHub connector operations | Current connector exposes repository/content/branch/commit/PR/issue/Actions operations but does not expose Codespaces administration or GitHub Pages configuration. | Verified 2026-09-05 |
| PH1-001 | Constitutional baseline | Verified | A | Legislative Department Constitution of India, 2024 consolidated text; India Code constitutional text | Constitution identified as primary governing source. Articles 14, 15, 17, 19, 21, 245, 246, 338, 338A, 341, 342 and Seventh Schedule are priority provisions. | Source/version verified; detailed clause extraction pending for several provisions. |
| PH1-002 | Legislative competence | Verified | A | Constitution Seventh Schedule, List III | Concurrent List Entry 1 covers criminal law, Entry 2 criminal procedure, Entry 11A administration of justice/court organisation subject to constitutional limits, Entry 12 evidence and oaths. | Verified from official Legislative Department text. |
| PH1-003 | SC/ST Act baseline | Verified | A | India Code Act 33/1989 | Act addresses atrocities against SC/ST members, Special/Exclusive Special Courts, relief and rehabilitation; sections 2-23 structure offences, official neglect, externment, courts, appeals, victim/witness rights, preventive powers, overriding effect and rule-making. | Verified at consolidated section-structure level. |
| PH1-004 | SC/ST Act version history | Verified | A | India Code Act 33/1989 record | India Code lists the Act as last updated 19-11-2018 and lists Rules/amendments through 2018. This is a source-record date, not a conclusion that no later legal instrument exists. | Verified; later-instrument search remains required. |
| PH1-005 | SC/ST Rules baseline | Verified | A | Ministry of Tribal Affairs Knowledge Hub and India Code | Official sources identify the 1995 Rules and amendments in 2011, 2013, two in 2014, 2016 and 2018. | Verified at instrument-list level; consolidated rule text pending. |
| PH1-006 | BNS baseline | Verified | A | India Code Act 45/2023 | BNS is the current general substantive criminal-law statute, enacted 25-12-2023 and enforced from 01-07-2024. | Verified. |
| PH1-007 | BNSS baseline | Verified | A | India Code Act 46/2023 | BNSS is the current general criminal-procedure statute, enacted 25-12-2023 and enforced from 01-07-2024. Sections 173-193 form a major investigation/reporting interface. | Verified. |
| PH1-008 | BSA baseline | Verified | A | India Code Act 47/2023 | BSA is the current general evidence statute, enacted 25-12-2023 and enforced from 01-07-2024. Sections 104-117 cover burden/presumption provisions. | Verified. |
| PH1-009 | PCR Act baseline | Verified | A | India Code Act 22/1955 | PCR Act implements Article 17 through offences concerning untouchability-related disabilities, access, services, compulsory labour and related consequences; section 15 addresses cognizability/summary trial and section 15A implementation duties. | Verified at section-structure level. |
| PH1-010 | PCR Rules baseline | Verified | A | India Code and Ministry of Tribal Affairs | Protection of Civil Rights Rules, 1977 are identified as subordinate rules. | Verified instrument identity; text extraction pending. |
| PH1-011 | SC/ST identity instruments | Verified | A | Constitution (SC) Order 1950; Constitution (ST) Order 1950; Constitution Articles 341/342 | Constitutional orders specify SC/ST lists by the constitutional mechanism. | Orders verified; detailed legal-effect analysis reserved for Phase 4. |
| PH1-012 | Existing-law interaction | Working | A | Primary statutes above | SC/ST Act, PCR Act, BNS, BNSS and BSA form overlapping substantive/procedural/evidence layers. A full crosswalk is required before policy or drafting conclusions. | Structural proposition verified; offence-level crosswalk pending. |
| PH1-013 | State-law source map | Open | A | India Code state repositories and State official gazettes to be searched | State implementation machinery and materially relevant State laws must be mapped state-by-state. No State-level completeness claim made. | Not complete. |

## Phase 1 source artifacts

- `legislation/EXISTING_LAW_BASELINE.md`
- `legislation/SOURCE_MAP.md`

## Current research stopping point

The first primary-source baseline is recorded. The work has not reached Phase 1 acceptance. Next research must focus on clause-level extraction of the SC/ST Act and Rules, current-version verification, and a BNS/BNSS/BSA/PCR crosswalk, followed by the state-law source inventory.
