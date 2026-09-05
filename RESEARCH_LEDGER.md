# Research Ledger

## Initialization Status

Phase 0 baseline complete. Phase 1 substantive research active.

## Evidence Method

- Primary authoritative sources preferred: Constitution, legislation and Rules, Gazette notifications, Supreme Court/High Court judgments/orders, Parliament/Digital Sansad, NCRB and Government statistics, Ministries, Law Commission and Parliamentary committees.
- Secondary sources may supplement primary sources.
- Evidence grades: A = primary authoritative, B = strong official/credible, C = reliable secondary, D = weak/unverified.
- D-grade evidence must not be the sole basis of a major conclusion.
- Material claims require traceable provenance.
- A source's existence is not proof of every proposition attributed to it. Clause-level verification is required for operative legal claims.

## Entries

| ID | Workstream | Status | Evidence Grade | Source | Finding | Verification |
|---|---|---|---|---|---|---|
| INIT-001 | Repository baseline | Verified | A | GitHub repository metadata and repository operations | Repository exists, is public, default branch main, with authenticated read/write access. | Verified 2026-09-05 |
| INIT-002 | Existing repository artifacts | Verified | A | GitHub repository content, branches, commits, issues | Repository was empty before initialization; no historical research or drafts were found. | Verified 2026-09-05 |
| INIT-003 | Tool capability boundary | Verified | A | Available GitHub connector operations | Codespaces and Pages administration are not exposed. | Verified 2026-09-05 |
| PH1-001 | Constitutional baseline | Verified | A | Legislative Department Constitution, 2024 consolidated text; India Code | Priority constitutional provisions identified. Detailed Phase 4 analysis remains pending. | Source verified |
| PH1-002 | Legislative competence | Verified | A | Constitution Seventh Schedule, List III | Concurrent List Entries 1, 2, 11A and 12 cover criminal law, criminal procedure, administration of justice/court organisation subject to constitutional allocation, and evidence/oaths. | Verified |
| PH1-003 | SC/ST Act baseline | Verified | A | India Code Act 33/1989 | Act structure and principal sections verified. | Verified |
| PH1-004 | SC/ST Act version history | Updated | A | India Code Act metadata and 2025 consolidated PDF | Metadata says last updated 19-11-2018, while India Code hosts a consolidated PDF expressly marked as on 21-09-2025. The latter lists 2015 Amendment Act, 2018 Amendment Act and J&K Reorganisation Act 2019. | Verified 2026-09-05; final Gazette index pass still open |
| PH1-005 | SC/ST Rules baseline | Updated | A | India Code Act record; Ministry of Tribal Affairs; Government Gazette instruments | Principal Rules and amendments in 2011, 2013, two in 2014, 2016 and 2018 verified at instrument level. | Verified; consolidated clause extraction pending |
| PH1-006 | BNS baseline | Verified | A | India Code Act 45/2023 | BNS current general substantive criminal code, enforced 01-07-2024. | Verified |
| PH1-007 | BNSS baseline | Verified | A | India Code Act 46/2023 | BNSS current general criminal procedure code, enforced 01-07-2024. | Verified |
| PH1-008 | BSA baseline | Verified | A | India Code Act 47/2023 | BSA current general evidence code, enforced 01-07-2024. | Verified |
| PH1-009 | PCR Act baseline | Verified | A | India Code Act 22/1955 | PCR Act criminalises untouchability-related conduct and contains special procedure/implementation provisions. | Verified at section-structure level |
| PH1-010 | PCR Rules baseline | Verified | A | India Code; Ministry of Tribal Affairs | PCR Rules 1977 identified. | Text extraction pending |
| PH1-011 | SC/ST identity instruments | Verified | A | Constitution (SC) Order 1950; Constitution (ST) Order 1950; Articles 341/342 | Primary identity instruments verified. | Detailed constitutional analysis reserved |
| PH1-012 | Existing-law interaction | Working | A | Primary statutes above | Multiple overlapping substantive/procedural/evidence layers require crosswalk. | Offence/procedure/evidence crosswalk pending |
| PH1-013 | State-law source map | Open | A | India Code and State official sources | State implementation machinery remains to be mapped state-by-state. | Not complete |
| PH1-014 | SC/ST Act clause extraction | Advanced | A | India Code consolidated Act, as on 21-09-2025 | Sections 1-23 and Schedule extracted by operative subject, amendment provenance and interaction points. | Stored in legislation/SCST_ACT_CLAUSE_EXTRACTION.md; full exact-text reproduction not required for this research ledger |
| PH1-015 | Post-2018 Act verification | Advanced | A | India Code 2025 consolidation; Ministry of Law and Justice S.O. 2790(E), 16-07-2024 | No later Central amendment Act was located in targeted official searches through 05-09-2026. J&K Reorganisation Act 2019 is included in the 2025 consolidation. | Provisional pending final Gazette/Legislative Department index check |
| PH1-016 | BNS transition of legacy IPC references | Verified as transition instrument | A | Ministry of Law and Justice S.O. 2790(E), 16-07-2024; General Clauses Act s.8; BNS s.358 | Official notification directs references to IPC/CrPC/Indian Evidence Act in specified instruments to be read as references to BNS/BNSS/BSA and corresponding provisions. BNS s.358 repeals IPC with savings. | Verified source; exact Act-by-Act correspondence remains crosswalk task |
| PH1-017 | SC/ST Rules amendment history | Advanced | A | Government Gazette instruments G.S.R. 896(E), 725(E), 416(E), 774(E), 424(E), 588(E) | Principal Rules and each identified amendment through 2018 have been dispositioned at instrument level. | Stored in legislation/SCST_RULES_VERSION_MATRIX.md; consolidated rule-by-rule extraction remains open |
| PH1-018 | Post-2018 Rules verification | Advanced | A | India Code Rules index; Ministry of Tribal Affairs; targeted official-source search | No later Central amendment to the Rules after G.S.R. 588(E) was located through 05-09-2026. | Provisional pending final Gazette/Legislative Department index check |

## Phase 1 source artifacts

- legislation/EXISTING_LAW_BASELINE.md
- legislation/SOURCE_MAP.md
- legislation/SCST_ACT_CLAUSE_EXTRACTION.md
- legislation/SCST_RULES_VERSION_MATRIX.md

## Current research stopping point

The SC/ST Act has been extracted section-by-section from the India Code consolidation marked as on 21-09-2025. The identified SC/ST Rules amendment history through 2018 has been verified at instrument level. The next discrete workstream is the consolidated rule-by-rule extraction, followed by the BNS conduct crosswalk and BNSS/BSA procedural/evidence crosswalks. Phase 1 remains open. No Bill drafting or policy/constitutional conclusion has begun.
