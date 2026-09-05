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
| PH1-005 | SC/ST Rules baseline | Updated | A | India Code Act record; Ministry of Tribal Affairs; Government Gazette instruments | Principal Rules and amendments in 2011, 2013, two in 2014, 2016 and 2018 verified at instrument level. | Verified |
| PH1-006 | BNS baseline | Verified | A | India Code Act 45/2023 | BNS current general substantive criminal code, enforced 01-07-2024. | Verified |
| PH1-007 | BNSS baseline | Verified | A | India Code Act 46/2023 | BNSS current general criminal procedure code, enforced 01-07-2024. | Verified |
| PH1-008 | BSA baseline | Verified | A | India Code Act 47/2023 | BSA current general evidence code, enforced 01-07-2024. | Verified |
| PH1-009 | PCR Act baseline | Verified | A | India Code Act 22/1955 | PCR Act criminalises untouchability-related conduct and contains special procedure/implementation provisions. | Verified at section-structure level |
| PH1-010 | PCR Rules baseline | Verified | A | India Code; Ministry of Tribal Affairs | PCR Rules 1977 identified. | Text extraction pending |
| PH1-011 | SC/ST identity instruments | Verified | A | Constitution (SC) Order 1950; Constitution (ST) Order 1950; Articles 341/342 | Primary identity instruments verified. | Detailed constitutional analysis reserved |
| PH1-012 | Existing-law interaction | Working | A | Primary statutes above | Multiple overlapping substantive/procedural/evidence layers require crosswalk. | Offence/procedure/evidence crosswalk pending |
| PH1-013 | State-law source map | Open | A | India Code and State official sources | State implementation machinery remains to be mapped state-by-state. | Not complete |
| PH1-014 | SC/ST Act clause extraction | Advanced | A | India Code consolidated Act, as on 21-09-2025 | Sections 1-23 and Schedule extracted by operative subject, amendment provenance and interaction points. | Stored in legislation/SCST_ACT_CLAUSE_EXTRACTION.md |
| PH1-015 | Post-2018 Act verification | Advanced | A | India Code 2025 consolidation; Ministry of Law and Justice S.O. 2790(E), 16-07-2024 | No later Central amendment Act was located in targeted official searches through 05-09-2026. J&K Reorganisation Act 2019 is included in the 2025 consolidation. | Provisional pending final Gazette/Legislative Department index check |
| PH1-016 | BNS transition of legacy IPC references | Verified as transition instrument | A | Ministry of Law and Justice S.O. 2790(E), 16-07-2024; General Clauses Act s.8; BNS s.358 | Official notification directs references to IPC/CrPC/Indian Evidence Act in specified instruments to be read as references to BNS/BNSS/BSA and corresponding provisions. Direct numerical substitution is not assumed. | Verified source; exact Act-by-Act correspondence remains crosswalk task |
| PH1-017 | SC/ST Rules amendment history | Advanced | A | Government Gazette instruments G.S.R. 896(E), 725(E), 416(E), 774(E), 424(E), 588(E) | Principal Rules and each identified amendment through 2018 have been dispositioned at instrument level. | Stored in legislation/SCST_RULES_VERSION_MATRIX.md |
| PH1-018 | Post-2018 Rules verification | Advanced | A | India Code Rules index; Ministry of Tribal Affairs; targeted official-source search | No later Central amendment to the Rules after G.S.R. 588(E) was located through 05-09-2026. | Provisional pending final Gazette/Legislative Department index check |
| PH1-019 | SC/ST Rules clause extraction | Completed with qualification | A for underlying Government instruments; B/C for transcription aid | Principal Rules and amendment Gazettes; Department of Social Justice current publication index; consolidated India Code-derived text | Rules 1-18, all identified sub-rules, 47 Schedule relief items, Annexure-I and Annexure-II/attached disability material inventoried. | Completed 2026-09-05; Annexure-II primary attachment identity remains open |
| PH1-020 | Rules current publication status | Verified as current-source indicator | A | Department of Social Justice and Empowerment current archive | Department site currently lists 1995 Rules plus separate 2016 and 2018 PoA Rules publications, page last updated 22-06-2026. | Verified 2026-09-05; not proof of absence of later Gazette instruments |
| PH1-021 | Rules Annexure-II source discrepancy | Open | A/B | Consolidated Rules transcription and Schedule item 43 citation | Schedule item 43 cites a 01-06-2001 disability notification, while attached Annexure-II material begins with a 06-08-1986 notification. | Primary-source resolution required |
| PH1-022 | SC/ST Act s.3 BNS conduct crosswalk | Advanced | A | BNS Act 45/2023; India Code/BPRD BNS text; SC/ST Act Schedule; S.O. 2790(E); GCA s.8; BNS s.358 | Section 3(1) conduct, section 3(2) aggravated offences, and all 32 IPC references in the statutory Schedule were mapped to BNS correspondence classes/subsections without assuming numerical equivalence. Material differences include BNS mergers, altered punishment ceilings/fines, grievous-hurt threshold change, and restructuring of sexual/intimidation provisions. | Stored in legislation/SCST_ACT_SECTION3_BNS_CROSSWALK.md; final primary-text freeze pending |
| PH1-023 | SC/ST Act Schedule inventory count | Verified provision inventory, final source reconciliation pending | A | 2015 Amendment Act Schedule; current/consolidated Act source | Present enumeration contains 32 distinct IPC references in the Act Schedule. This is separate from the Rules Schedule's 47 relief contingencies. | Verified against available statutory Schedule; reconcile with project extraction during final freeze |
| PH1-024 | Rule 2(ga) IPC s.39 BNS transition | Verified correspondence | A | BNS s.2(33); S.O. 2790(E); SC/ST Rules Rule 2(ga) | IPC s.39 “voluntarily” corresponds to BNS s.2(33). Core intention/knowledge test is retained. | Verified 2026-09-05 |
| PH1-025 | SC/ST Act and Rules BNSS procedural crosswalk | Advanced with qualification | A | BNSS Act 46/2023; SC/ST Act; SC/ST Rules; S.O. 2790(E); BNSS s.531 | Special-law procedural interfaces mapped for Act ss.2, 4, 7, 9-15, 15A, 17-20; Special/Exclusive Special Courts; direct cognizance; FIR/investigation; arrest; bail/anticipatory bail; appeals; externment; preventive action; victim/witness rights; property attachment/forfeiture; probation; Rule 7 DSP-level investigation and 60-day framework. | Stored in legislation/SCST_ACT_BNSS_PROCEDURAL_CROSSWALK.md; exact former-CrPC subject expansion and Rule 7 delay consequences remain open |
| PH1-026 | SC/ST Act and Rules BSA evidence/presumption crosswalk | Advanced with qualification | A | BSA Act 47/2023; SC/ST Act; SC/ST Rules; S.O. 2790(E) | Act s.8(a)-(b) special presumptions have no identified BSA equivalent; BSA ss.104-109 provide general burden architecture and s.2(l) defines “shall presume”. Act s.3(2)(i)-(ii), (vi) and other materially relevant provisions operate within BSA relevance/proof/witness/document/electronic evidence rules. BSA ss.61-63 supply electronic-record admissibility; s.170 supplies repeal/savings. | Stored in legislation/SCST_ACT_BSA_EVIDENCE_PRESUMPTION_CROSSWALK.md; judicial operation of s.8 and final later-instrument completeness remain open |

## Phase 1 source artifacts

- legislation/EXISTING_LAW_BASELINE.md
- legislation/SOURCE_MAP.md
- legislation/SCST_ACT_CLAUSE_EXTRACTION.md
- legislation/SCST_RULES_VERSION_MATRIX.md
- legislation/SCST_RULES_CLAUSE_EXTRACTION.md
- legislation/SCST_ACT_SECTION3_BNS_CROSSWALK.md
- legislation/SCST_ACT_BNSS_PROCEDURAL_CROSSWALK.md
- legislation/SCST_ACT_BSA_EVIDENCE_PRESUMPTION_CROSSWALK.md

## Current research stopping point

The SC/ST Act and Rules baseline/extractions remain authoritative. The Rules clause extraction is complete with the Annexure-II source discrepancy preserved. The section 3 BNS crosswalk is advanced with qualification. The BNSS procedural crosswalk is advanced with qualification and records the defined special-procedure interfaces. The BSA evidence/presumption crosswalk is now recorded, covering Act s.8 presumptions, evidence-related aspects of s.3(2), materially relevant Rules evidence/document interfaces, BSA definitions, burdens, presumptions, electronic records, witnesses/documents and BSA s.170 transition, with S.O. 2790(E) incorporated as the legacy-reference transition instrument. Final primary-text freezes and later-instrument completeness remain open. No Bill drafting or policy/constitutional conclusion has begun.
