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
| PH1-019 | SC/ST Rules clause extraction | Completed with qualification | A for underlying Government instruments; B/C for transcription aid | Principal Rules and amendment Gazettes; Department of Social Justice current publication index; consolidated India Code-derived text | Rules 1-18, 47 Schedule relief items, Annexure-I and Annexure-II/attached disability material inventoried. | Completed 2026-09-05; Annexure-II primary attachment identity remains open |
| PH1-020 | Rules current publication status | Verified as current-source indicator | A | Department of Social Justice and Empowerment current archive | Department site currently lists 1995 Rules plus separate 2016 and 2018 PoA Rules publications, page last updated 22-06-2026. | Verified 2026-09-05; not proof of absence of later Gazette instruments |
| PH1-021 | Rules Annexure-II source discrepancy | Open | A/B | Consolidated Rules transcription and Schedule item 43 citation | Schedule item 43 cites a 01-06-2001 disability notification, while attached Annexure-II material begins with a 06-08-1986 notification. | Primary-source resolution required |
| PH1-022 | SC/ST Act s.3 BNS conduct crosswalk | Advanced | A | BNS Act 45/2023; India Code/BPRD BNS text; SC/ST Act Schedule; S.O. 2790(E); GCA s.8; BNS s.358 | Section 3(1) conduct, section 3(2) aggravated offences, and all 32 IPC references in the statutory Schedule were mapped to BNS correspondence classes/subsections without assuming numerical equivalence. Material differences include BNS mergers, altered punishment ceilings/fines, grievous-hurt threshold change, and restructuring of sexual/intimidation provisions. | Stored in legislation/SCST_ACT_SECTION3_BNS_CROSSWALK.md; final primary-text freeze pending |
| PH1-023 | SC/ST Act Schedule inventory count | Verified provision inventory, final source reconciliation pending | A | 2015 Amendment Act Schedule; current/consolidated Act source | Present enumeration contains 32 distinct IPC references in the Act Schedule. This is separate from the Rules Schedule's 47 relief contingencies. | Verified against available statutory Schedule; reconcile with project extraction during final freeze |
| PH1-024 | Rule 2(ga) IPC s.39 BNS transition | Verified correspondence | A | BNS s.2(33); S.O. 2790(E); SC/ST Rules Rule 2(ga) | IPC s.39 “voluntarily” corresponds to BNS s.2(33). Core intention/knowledge test is retained. | Verified 2026-09-05 |
| PH1-025 | SC/ST Act and Rules BNSS procedural crosswalk | Advanced with qualification | A | BNSS Act 46/2023; SC/ST Act; SC/ST Rules; S.O. 2790(E); BNSS s.531 | Special-law procedural interfaces mapped for Act ss.2, 4, 7, 9-15, 15A, 17-20; Special/Exclusive Special Courts; direct cognizance; FIR/investigation; arrest; bail/anticipatory bail; appeals; externment; preventive action; victim/witness rights; property attachment/forfeiture; probation; Rule 7 DSP-level investigation and 60-day framework. | Stored in legislation/SCST_ACT_BNSS_PROCEDURAL_CROSSWALK.md; exact former-CrPC subject expansion and Rule 7 delay consequences remain open |
| PH1-026 | SC/ST Act and Rules BSA evidence/presumption crosswalk | Advanced with qualification | A | BSA Act 47/2023; SC/ST Act; SC/ST Rules; S.O. 2790(E) | Act s.8(a)-(b) special presumptions have no identified BSA equivalent; BSA ss.104-109 provide general burden architecture and s.2(l) defines “shall presume”. Act s.3(2)(i)-(ii), (vi) and other materially relevant provisions operate within BSA relevance/proof/witness/document/electronic evidence rules. | Stored in legislation/SCST_ACT_BSA_EVIDENCE_PRESUMPTION_CROSSWALK.md; judicial operation of s.8 and final later-instrument completeness remain open |
| PH1-027 | PCR Act/Rules comparison | Completed with qualification | A | `legislation/PCR_ACT_RULES_SECTION_RULE_COMPARISON.md`; India Code and Ministry sources | PCR offence, procedure, implementation and SC/ST Act s.16 dependency compared. | Completed 2026-09-05; final current-law completeness remains open |
| PH1-028 | Manual Scavengers Act/Rules comparison | Completed with qualification | A | `legislation/MANUAL_SCAVENGERS_ACT_RULES_SCST_CROSSWALK.md`; India Code | Manual-scavenging prohibitions, rehabilitation, trial, company liability and monitoring structures compared with SC/ST Act/Rules. | Completed 2026-09-05; later-instrument and transition checks remain open |
| PH1-029 | Bonded Labour Act/Rules crosswalk | Completed with qualification | A | `legislation/BONDED_LABOUR_ACT_RULES_SCST_CROSSWALK.md`; India Code/Government sources | BLSA ss.2(g), 4, 16 and 18 overlap strongly with SC/ST Act s.3(1)(h), while debt/property protections, forum/bail architecture and company liability remain distinct. | Completed 2026-09-05; current-law completeness and Rules notification discrepancies remain open |
| PH1-030 | Authoritative-record integration remediation | Verified | A | GitHub repository control records and `project-state/PH1_AUTHORITATIVE_RECORD_REMEDIATION.md` | Completed Phase 1 workstreams and sequencing are now integrated into state, handoff, ledger, issues and decisions records. Historical Phase 0 audit wording is preserved as historical. | Remediated 2026-09-05 |
| PH1-031 | Priority Central legislation screening | Completed at screening level with qualification | A | `legislation/CENTRAL_LEGISLATION_PRIORITY_SCREENING.md`; India Code; Ministry of Tribal Affairs | Remaining Priority 2 queue screened: Forest Rights, RPwD, Domestic Violence, POCSO, Juvenile Justice, Prevention of Corruption, Representation of the People, plus Child and Adolescent Labour as a relevant labour interface. | Completed 2026-09-05; no clause-level or final completeness freeze implied |
| PH1-032 | Bihar source-ledger integration | Verified | A | `research/states/BIHAR_SOURCE_LEDGER.md`; `research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md` | Bihar supplemental source ledger merged into the master State Implementation Source Ledger without discarding existing Andhra Pradesh, Arunachal Pradesh or Assam entries. | Verified 2026-09-05 |
| PH1-033 | Chhattisgarh State implementation inventory | Completed with qualification | A | Government of Chhattisgarh State administrative reports, Department of Tribal and Scheduled Caste Development, Chhattisgarh DPR, Chhattisgarh High Court; official Central PoA reports | Chhattisgarh implementation architecture mapped: Rule 9 nodal designation, Protection Cell/police machinery, V&MCs, Special Courts, prosecutors, relief, DBT, PCR and relevant State-law interfaces. | Stored in `legislation/states/CHHATTISGARH.md`; current 2026 instrument gaps remain open |
| PH1-034 | Chhattisgarh current judicial corroboration | Verified with qualification | A | Chhattisgarh High Court current judicial officer records and judgments | Current 2026 Special Judge under SC/ST (P.A.) Act postings and continuing appellate/trial operation were identified at specific locations; these do not establish a complete statewide notification matrix. | Verified 2026-09-05 |
| PH1-035 | Goa State implementation inventory | Completed with qualification | A for underlying State records and official Central reports | Government of Goa 2023 State Annual Report; Goa Commission for SC/ST current page; Goa Prosecution Citizen Charter 2023; Goa 2025-26 budget; Goa Statistical Handbook 2023-24; Goa Economic Survey 2024-25; Goa 2024 manual-scavenger notifications; Ministry of Social Justice and Empowerment official Goa implementation reports | Goa implementation architecture mapped: 2023 Rule 9 nodal order, reported absence of dedicated Protection Cell/Special Police Station at that reporting point, State/District V&MCs, Panaji/Margao Special Courts, SPP function, relief budget, Commission oversight, awareness activity and related-law interfaces. Current 2026 instrument census remains incomplete. | Stored in `legislation/states/GOA.md` and `research/states/GOA_SOURCE_LEDGER.md`; master ledger consolidation remains a controlled follow-up |
| PH1-036 | Goa supplemental source-ledger consolidation | Verified | A | `research/states/GOA_SOURCE_LEDGER.md`; `research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md` | All 17 Goa source-ledger entries were consolidated into the master State Implementation Source Ledger without discarding prior jurisdiction entries. | Verified 2026-09-05 |
| PH1-037 | Gujarat State implementation inventory | Completed with qualification | A | Government of Gujarat Department of Social Justice & Empowerment current PoA pages; Gujarat Legal Department notification; Gujarat Directorate; Gujarat Safai Kamdar Vikas Nigam; current State Acts/Rules and related official administrative material | Gujarat implementation architecture mapped: nodal arrangements, Police Protection Cell, Special Officers, sensitive districts, V&MC structures, 19 functional Special Courts, prosecutors, relief/rehabilitation schemes, atrocity data/statistics, PCR staffing, Manual Scavengers committees/enforcement and bonded-labour interface. | Stored in `legislation/states/GUJARAT.md` and `research/states/GUJARAT_SOURCE_LEDGER.md`; current primary-instrument census remains open |
| PH1-038 | Haryana State implementation inventory | Completed with qualification | A | Government of Haryana Social Justice Department; Haryana Gazette; Haryana Police; Haryana Prosecution Department; Haryana Home Department; Haryana State Legal Services Authority; Urban Local Bodies Department; official Government of India Haryana PoA implementation reports | Haryana implementation architecture mapped: departmental PoA/PCR mandate, Rule 9 and Rule 10 architecture in official reporting, reported Protection Cell/district-cell structure, State/District/Sub-Divisional V&MC instruments, 08-09-2017 Special Court notification, current prosecution publication, current relief service and 2025 police PoA count, Manual Scavengers and State SC institutional interfaces. | Stored in `legislation/states/HARYANA.md` and `research/states/HARYANA_SOURCE_LEDGER.md`; current 2026 primary-instrument census remains open |
| PH1-039 | Jharkhand State implementation inventory | Completed with qualification | A | `research/states/JHARKHAND_SOURCE_LEDGER.md`; official Jharkhand Welfare, Police, High Court, Finance, Labour, Revenue and Chief Minister sources; official Central PoA/manual-scavenger data | Jharkhand implementation architecture mapped at current/recent official-source level, including dedicated SC/ST police units in multiple districts, current Special Court assignments, 2026 three-post Special Court decision, 2023 lower-rank investigation authorization, relief/DBT/treasury infrastructure and related-law interfaces. | Completed 2026-09-05; current primary instrument census remains open |
| PH1-040 | Karnataka State implementation inventory | Completed with qualification | A for official State/Central underlying records; B/C for secondary instrument leads | Karnataka State Annual Reports 2023/2024; Karnataka Assembly Budget 2025-26; official Central PoA reports; official Central IPS civil list; Karnataka High Court; Karnataka Panchayat Raj Act | Karnataka implementation architecture mapped, including DCRE/33 special police stations, Rule 9 reporting architecture, State/District/Sub-Divisional V&MCs, Special/Exclusive Special Courts, prosecutors, relief, PCR, Manual Scavengers, bonded-labour and Panchayat Raj interfaces. | Completed 2026-09-05; current primary-instrument census remains open |
| PH1-041 | Kerala State implementation inventory | Completed with qualification | A for official State/Central sources | Kerala State Planning Board Economic Review 2025 and Annual Plans 2024-25/2025-26; Kerala Scheduled Tribes Development Department; Kerala Police; Kerala State Election Commission; Kerala LSGD; Kerala Law Department; Kerala Labour Commissionerate; official Central PoA scheme/implementation reports | Kerala implementation architecture mapped, including Special Courts/benches, Scheduled Castes Protection Cell, Special Police Stations, SC/ST atrocity petition handling, district legal support, relief/rehabilitation, current Police crime data through July 2026, Manual Scavengers implementation, bonded-labour and Panchayat Raj interfaces. | Completed 2026-09-05; current primary-instrument census remains open |
| PH1-042 | Madhya Pradesh State implementation inventory | Completed with qualification | A for official State/Central sources; C for one unverified budget lead | Government of Madhya Pradesh CM Helpline; MP Social Justice Department; MP Police; High Court of Madhya Pradesh; Madhya Pradesh Legislative Assembly; M.P. CODE; Government of India Ministry of Social Justice & Empowerment official PoA/PCR reports and current scheme data | Madhya Pradesh implementation architecture mapped: current PoA scheme/service listing, current Special Judge postings, current PoA-related police/prosecution training, historical and recent official Protection Cell/Special Police Station/V&MC/Rule 7/Rule 9 architecture, current relief activity and related-law source environment. | Stored in `legislation/states/MADHYA_PRADESH.md` and `research/states/MADHYA_PRADESH_SOURCE_LEDGER.md`; current primary-instrument census remains open |
| PH1-043 | Maharashtra master-ledger integration | Verified | A | `research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md`; `research/states/MAHARASHTRA_SOURCE_LEDGER.md`; GitHub commit comparison | Maharashtra MH-STATE-001 through MH-STATE-020 were integrated into the master ledger after controlled range retrieval of the complete pre-existing master content. Post-write retrieval and commit comparison verified preservation of the pre-existing jurisdiction entries. | Verified 2026-09-05 before Manipur research began |
| PH1-044 | Manipur State implementation inventory | Active with qualification | A for primary State/Central sources; B for one current administrative meeting report | Government of Manipur Law & Legislative Affairs Department; Manipur Police; High Court of Manipur; Government of Manipur Revenue/Social Welfare material; Parliament/Digital Sansad; Ministry of Social Justice & Empowerment; Ministry of Tribal Affairs | Manipur current/recent implementation architecture has been independently mapped. Current Police FIRs establish continuing PoA invocation and BNS/PoA coexistence. A 2019 primary SPP order establishes seven Sessions Court jurisdictions. Historical Central reports establish Rule 9 and Special Court arrangements. Current Rule 9, Protection Cell, Special Police Station, Rule 10, V&MC, Special/Exclusive Special Court, SPP/ESPP continuation, relief/payment, PoA-specific SOP/digital, related-law and post-BNS/BNSS/BSA status remain open. | Stored in `legislation/states/MANIPUR.md` and `research/states/MANIPUR_SOURCE_LEDGER.md`; residuals PH1-ISSUE-179 through PH1-ISSUE-255 |

## Phase 1 source artifacts

- legislation/EXISTING_LAW_BASELINE.md
- legislation/SOURCE_MAP.md
- legislation/SCST_ACT_CLAUSE_EXTRACTION.md
- legislation/SCST_RULES_VERSION_MATRIX.md
- legislation/SCST_RULES_CLAUSE_EXTRACTION.md
- legislation/SCST_ACT_SECTION3_BNS_CROSSWALK.md
- legislation/SCST_ACT_BNSS_PROCEDURAL_CROSSWALK.md
- legislation/SCST_ACT_BSA_EVIDENCE_PRESUMPTION_CROSSWALK.md
- legislation/PCR_ACT_RULES_SECTION_RULE_COMPARISON.md
- legislation/MANUAL_SCAVENGERS_ACT_RULES_SCST_CROSSWALK.md
- legislation/BONDED_LABOUR_ACT_RULES_SCST_CROSSWALK.md
- legislation/CENTRAL_LEGISLATION_PRIORITY_SCREENING.md
- legislation/states/CHHATTISGARH.md
- legislation/states/GOA.md
- legislation/states/GUJARAT.md
- legislation/states/HARYANA.md
- legislation/states/JHARKHAND.md
- legislation/states/KARNATAKA.md
- legislation/states/KERALA.md
- legislation/states/MADHYA_PRADESH.md
- legislation/states/MAHARASHTRA.md
- legislation/states/MANIPUR.md
- research/states/GOA_SOURCE_LEDGER.md
- research/states/GUJARAT_SOURCE_LEDGER.md
- research/states/HARYANA_SOURCE_LEDGER.md
- research/states/JHARKHAND_SOURCE_LEDGER.md
- research/states/KARNATAKA_SOURCE_LEDGER.md
- research/states/KERALA_SOURCE_LEDGER.md
- research/states/MADHYA_PRADESH_SOURCE_LEDGER.md
- research/states/MAHARASHTRA_SOURCE_LEDGER.md
- research/states/MANIPUR_SOURCE_LEDGER.md
- project-state/PH1_AUTHORITATIVE_RECORD_REMEDIATION.md
- project-state/MANIPUR_ISSUES_ADDENDUM.md
- project-state/MANIPUR_DECISIONS_ADDENDUM.md

## Current research stopping point

The SC/ST Act and Rules baseline/extractions remain authoritative. The Rules clause extraction is complete with the Annexure-II source discrepancy preserved. The section 3 BNS crosswalk is advanced with qualification. The BNSS procedural crosswalk is advanced with qualification. The BSA evidence/presumption crosswalk is advanced with qualification. PCR, Manual Scavengers and Bonded Labour comparisons are complete with qualifications. The remaining Priority 2 Central legislation queue has been screened at screening level. State inventories through Manipur have now been independently researched with explicit currentness qualifications. Maharashtra's master-ledger integration was completed and verified before Manipur began. Manipur remains active for current-instrument closure, especially Rule 9, Protection Cell/Special Police Station, Rule 10/sensitive areas, V&MCs, Special/Exclusive Special Courts, SPP/ESPP continuation, relief/payment, PoA-specific SOP/digital systems, related-law interfaces, annual-report submission and post-BNS/BNSS/BSA State instructions. Final primary-text freezes, later-instrument completeness, known source discrepancy resolution, transition reconciliation, remaining State/UT inventory and Pages verification remain open. No Bill drafting or policy/constitutional conclusion has begun.

## Cumulative Phase 1 jurisdiction-control index

The following index is a reconciliation-only control layer. It does not recreate or replace jurisdiction-specific substantive research. It records artifact traceability already verified in `project-state/PH1_STATE_CONTROL_RECONCILIATION_2026-09-06.md`.

| Sequence | Jurisdiction | Inventory | Source ledger | Issue record | Decision record | Control disposition |
|---:|---|---|---|---|---|---|
| 1 | Andhra Pradesh | `legislation/states/ANDHRA_PRADESH.md` | ABSENT/INDEXED | ABSENT/INDEXED | ABSENT/INDEXED | Completed with qualification; residuals carried in cumulative controls. |
| 2 | Arunachal Pradesh | `legislation/states/ARUNACHAL_PRADESH.md` | ABSENT/INDEXED | ABSENT/INDEXED | ABSENT/INDEXED | Completed with currentness residuals. |
| 3 | Assam | `legislation/states/ASSAM.md` | ABSENT/INDEXED | ABSENT/INDEXED | ABSENT/INDEXED | Completed with currentness and instrument residuals. |
| 4 | Bihar | `legislation/states/BIHAR.md` | `research/states/BIHAR_SOURCE_LEDGER.md` | ABSENT/INDEXED | ABSENT/INDEXED | Completed with currentness and instrument residuals. |
| 5 | Chhattisgarh | `legislation/states/CHHATTISGARH.md` | ABSENT/INDEXED | ABSENT/INDEXED | ABSENT/INDEXED | Completed with currentness, instrument and related-law residuals. |
| 6 | Goa | `legislation/states/GOA.md` | `research/states/GOA_SOURCE_LEDGER.md` | ABSENT/INDEXED | ABSENT/INDEXED | Completed with qualifications. |
| 7 | Gujarat | `legislation/states/GUJARAT.md` | `research/states/GUJARAT_SOURCE_LEDGER.md` | ABSENT/INDEXED | ABSENT/INDEXED | Completed with current instrument/workflow residuals. |
| 8 | Haryana | `legislation/states/HARYANA.md` | `research/states/HARYANA_SOURCE_LEDGER.md` | ABSENT/INDEXED | ABSENT/INDEXED | Completed with current instrument residuals. |
| 9 | Himachal Pradesh | `legislation/states/HIMACHAL_PRADESH.md` | `research/states/HIMACHAL_PRADESH_SOURCE_LEDGER.md` | `research/states/HIMACHAL_PRADESH_MASTER_LEDGER_APPEND.md` | `research/states/HIMACHAL_PRADESH_MASTER_LEDGER_APPEND.md` | Completed with qualification; PH1-ISSUE-089 through PH1-ISSUE-100 and DEC-0081 through DEC-0084 are controlled later records in the append artifact. |
| 10 | Jharkhand | `legislation/states/JHARKHAND.md` | `research/states/JHARKHAND_SOURCE_LEDGER.md` | ABSENT/INDEXED | ABSENT/INDEXED | Completed with current instrument residuals. |
| 11 | Karnataka | `legislation/states/KARNATAKA.md` | `research/states/KARNATAKA_SOURCE_LEDGER.md` | ABSENT/INDEXED | ABSENT/INDEXED | Completed with current instrument and transition residuals. |
| 12 | Kerala | `legislation/states/KERALA.md` | `research/states/KERALA_SOURCE_LEDGER.md` | ABSENT/INDEXED | ABSENT/INDEXED | Completed with current and historical/current reconciliation residuals. |
| 13 | Madhya Pradesh | `legislation/states/MADHYA_PRADESH.md` | `research/states/MADHYA_PRADESH_SOURCE_LEDGER.md` | ABSENT/INDEXED | ABSENT/INDEXED | Completed with current instrument/source-grade residuals. |
| 14 | Maharashtra | `legislation/states/MAHARASHTRA.md` | `research/states/MAHARASHTRA_SOURCE_LEDGER.md` | `project-state/MAHARASHTRA_ISSUES_ADDENDUM.md` | `project-state/MAHARASHTRA_DECISIONS_ADDENDUM.md` and controlled continuation records | PH1-ISSUE-163 through PH1-ISSUE-178 and later jurisdiction decisions preserved in controlled records. |
| 15 | Manipur | `legislation/states/MANIPUR.md` | `research/states/MANIPUR_SOURCE_LEDGER.md` | `project-state/MANIPUR_ISSUES_ADDENDUM.md` and continuation records | `project-state/MANIPUR_DECISIONS_ADDENDUM.md` and continuation records | PH1-ISSUE-179 through PH1-ISSUE-255 and DEC-MN-0124 through DEC-MN-0171 preserved in controlled records. |
| 16 | Meghalaya | `legislation/states/MEGHALAYA.md` | `research/states/MEGHALAYA_SOURCE_LEDGER.md` | `project-state/MEGHALAYA_ISSUES_2026-09-05.md` | `project-state/MEGHALAYA_DECISIONS_2026-09-05.md` | PH1-ISSUE-256 through PH1-ISSUE-265 open; PROCEED/CLOSE WITH LIMITATIONS. |
| 17 | Mizoram | `legislation/states/MIZORAM.md` | `research/states/MIZORAM_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-MZ-001 through PH1-ISSUE-MZ-016 open. |
| 18 | Nagaland | `legislation/states/NAGALAND.md` | `research/states/NAGALAND_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-NG-001 through PH1-ISSUE-NG-018 open. |
| 19 | Odisha | `legislation/states/ODISHA.md` | `research/states/ODISHA_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-OD-001 through PH1-ISSUE-OD-018 open. |
| 20 | Punjab | `legislation/states/PUNJAB.md` | `research/states/PUNJAB_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-PB-001 through PH1-ISSUE-PB-016 open. |
| 21 | Rajasthan | `legislation/states/RAJASTHAN.md` | `research/states/RAJASTHAN_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-RJ-001 through PH1-ISSUE-RJ-016 open. |
| 22 | Sikkim | `legislation/states/SIKKIM.md` | `research/states/SIKKIM_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | Current Rule 9 and other instrument residuals preserved. |
| 23 | Tamil Nadu | `legislation/states/TAMIL_NADU.md` | `research/states/TAMIL_NADU_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-TN-001 through PH1-ISSUE-TN-016 open. |
| 24 | Telangana | `legislation/states/TELANGANA.md` | `research/states/TELANGANA_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-TG-001 through PH1-ISSUE-TG-016 open. |
| 25 | Tripura | `legislation/states/TRIPURA.md` | `research/states/TRIPURA_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-TR-001 through PH1-ISSUE-TR-016 open; Rule 8 contradiction preserved. |
| 26 | Uttar Pradesh | `legislation/states/UTTAR_PRADESH.md` | `research/states/UTTAR_PRADESH_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-UP-001 through PH1-ISSUE-UP-016 open. |
| 27 | Uttarakhand | `legislation/states/UTTARAKHAND.md` | `research/states/UTTARAKHAND_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-UK-001 through PH1-ISSUE-UK-016 open. |
| 28 | West Bengal | `legislation/states/WEST_BENGAL.md` | `research/states/WEST_BENGAL_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-WB-001 through PH1-ISSUE-WB-016 open. |
| 29 | Andaman and Nicobar Islands | `legislation/states/ANDAMAN_NICOBAR.md` | `research/states/ANDAMAN_NICOBAR_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-AN-001 through PH1-ISSUE-AN-016 open plus controlled interface residual. |
| 30 | Chandigarh | `legislation/states/CHANDIGARH.md` | `research/states/CHANDIGARH_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-CH-001 through PH1-ISSUE-CH-016 open. |
| 31 | Dadra and Nagar Haveli and Daman and Diu | `legislation/states/DADRA_NAGAR_HAVELI_DAMAN_DIU.md` | `research/states/DADRA_NAGAR_HAVELI_DAMAN_DIU_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-DD-001 through PH1-ISSUE-DD-016 open. |
| 32 | Delhi (NCT) | `legislation/states/DELHI.md` | `research/states/DELHI_SOURCE_LEDGER.md` | jurisdiction-specific record present | jurisdiction-specific record present | PH1-ISSUE-DL-001 through PH1-ISSUE-DL-016 open. |
| 33 | Jammu and Kashmir | `legislation/states/JAMMU_KASHMIR.md` | `research/states/JAMMU_KASHMIR_SOURCE_LEDGER.md` | `project-state/JAMMU_KASHMIR_ISSUES_2026-09-05.md` | `project-state/JAMMU_KASHMIR_DECISIONS_2026-09-05.md` | PH1-ISSUE-JK-001 through PH1-ISSUE-JK-018 open; Rule 8 contradiction preserved. |

### Control-layer rules

1. This index is an artifact-control index, not a substitute for the jurisdiction-specific substantive record.
2. `ABSENT/INDEXED` means the reconciliation verified the absence of a dedicated file and explicitly recorded the control path. It does not mean the underlying evidence is absent.
3. Existing cumulative IDs PH1-001 through PH1-044 remain unchanged.
4. No new substantive research findings are created by this index.
5. The three remaining jurisdictions, Ladakh, Lakshadweep and Puducherry, remain unresearched.
6. `legislation/STATE_IMPLEMENTATION_INVENTORY.md` and `research/STATE_IMPLEMENTATION_SOURCE_LEDGER.md` remain outside this repair.
7. The cumulative control layer is synchronized as of 2026-09-06, subject to independent post-write verification.


## Jurisdiction Control Index: Lakshadweep, 2026-09-06

This section is reconciliation metadata only. It does not create new cumulative research IDs and does not replace the jurisdiction-specific substantive record.

| Jurisdiction | Inventory | Source ledger | Issue record | Decision record | Disposition | Source IDs | Residual IDs | Decision IDs |
|---|---|---|---|---|---|---|---|---|
| Lakshadweep | `legislation/states/LAKSHADWEEP.md` | `research/states/LAKSHADWEEP_SOURCE_LEDGER.md` | `project-state/LAKSHADWEEP_ISSUES_2026-09-06.md` | `project-state/LAKSHADWEEP_DECISIONS_2026-09-06.md` | PROCEED/CLOSE WITH LIMITATIONS | LAK-001 through LAK-019 | PH1-ISSUE-LK-001 through PH1-ISSUE-LK-018 | DEC-LK-2026-09-06-001 through DEC-LK-2026-09-06-010 |

Control note: Lakshadweep is the 35th completed jurisdiction. Its jurisdiction-specific source, residual and decision IDs remain governed by the jurisdiction-specific artifacts. No cumulative PH1, PH1-ISSUE or DEC ID has been fabricated, renumbered or promoted.
