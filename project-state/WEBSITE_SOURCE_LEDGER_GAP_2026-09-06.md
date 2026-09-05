# Website Source-Ledger Gap Control Record

Date: 2026-09-06
Phase: Phase 1, Existing-Law Baseline and Source Map
Workstream: website/source-ledger synchronization control only
Status: VERIFIED GAP CAPTURED; PAGES BUILD FAILED BEFORE SITE ARTIFACT

## Control-run identification

The first non-cancelled post-remediation Pages run was workflow run #389, head commit `180663c0f64ba8970a239f3d828e91363709a9ad`, created 2026-09-05 20:03:23 UTC and completed with conclusion `failure` at 2026-09-05 20:07:09 UTC.

This run is the first verified non-cancelled post-remediation run after the remediation commits. Run #386 was cancelled. Earlier queued/pending runs were not treated as success.

The run's `deploy` job completed with `failure`. The source-ledger control step and artifact upload succeeded. The production site build then failed on a completed jurisdiction with no controlled source rows: Arunachal Pradesh. Therefore no Pages artifact was produced by this run, and no live publication is claimed.

## Retrieved control artifact

Artifact: `source-ledger-control`
Artifact ID: `9976069045`
Workflow run: `33988950065` / run #389
SHA-256: `989f586939b111e6902f69c6e59ac9611c1b19f9e71eea12577253d49bde6c6e`

The artifact was downloaded and inspected. Its contents are treated as the authoritative exact control comparison for this remediation point.

## Exact control totals

- `MASTER_IDS=261`
- `JURISDICTION_LEDGER_FILES=29`
- `JURISDICTION_LEDGER_IDS=571`
- `MISSING_FROM_MASTER=377`
- `MASTER_ONLY_IDS=67`

The 377 missing IDs are the exact deterministic set produced by `scripts/verify_website_source_sync.py`. They are not reconstructed from memory and were not inferred from source-ledger prose.

## Exact MISSING_IDS set

```text
AN-STATE-001,AN-STATE-002,AN-STATE-003,AN-STATE-004,AN-STATE-005,AN-STATE-006,AN-STATE-007,AN-STATE-008,AN-STATE-009,AN-STATE-010,AN-STATE-011,AN-STATE-012,AN-STATE-013,AN-STATE-014,AN-STATE-015,AN-STATE-016,AN-STATE-017,AN-STATE-018,AN-STATE-019,AN-STATE-020,
CH-STATE-001,CH-STATE-002,CH-STATE-003,CH-STATE-004,CH-STATE-005,CH-STATE-006,CH-STATE-007,CH-STATE-008,CH-STATE-009,CH-STATE-010,CH-STATE-011,CH-STATE-012,CH-STATE-013,CH-STATE-014,CH-STATE-015,CH-STATE-016,CH-STATE-017,CH-STATE-018,CH-STATE-019,CH-STATE-020,
DDD-STATE-001,DDD-STATE-002,DDD-STATE-003,DDD-STATE-004,DDD-STATE-005,DDD-STATE-006,DDD-STATE-007,DDD-STATE-008,DDD-STATE-009,DDD-STATE-010,DDD-STATE-011,DDD-STATE-012,DDD-STATE-013,DDD-STATE-014,DDD-STATE-015,DDD-STATE-016,
DL-STATE-001,DL-STATE-002,DL-STATE-003,DL-STATE-004,DL-STATE-005,DL-STATE-006,DL-STATE-007,DL-STATE-008,DL-STATE-009,DL-STATE-010,DL-STATE-011,DL-STATE-012,DL-STATE-013,DL-STATE-014,DL-STATE-015,DL-STATE-016,DL-STATE-017,DL-STATE-018,
JK-001,JK-002,JK-003,JK-004,JK-005,JK-006,JK-007,JK-008,JK-009,JK-010,JK-011,JK-012,JK-013,JK-014,JK-015,JK-016,JK-017,JK-018,JK-019,JK-020,JK-021,JK-022,
MG-STATE-001,MG-STATE-002,MG-STATE-003,MG-STATE-004,MG-STATE-005,MG-STATE-006,MG-STATE-007,MG-STATE-008,MG-STATE-009,MG-STATE-010,MG-STATE-011,MG-STATE-012,MG-STATE-013,MG-STATE-014,MG-STATE-015,
MN-STATE-001,MN-STATE-002,MN-STATE-003,MN-STATE-004,MN-STATE-005,MN-STATE-006,MN-STATE-007,MN-STATE-008,MN-STATE-009,MN-STATE-010,MN-STATE-011,MN-STATE-012,MN-STATE-013,MN-STATE-014,MN-STATE-015,MN-STATE-016,MN-STATE-017,MN-STATE-018,MN-STATE-019,MN-STATE-020,MN-STATE-021,MN-STATE-022,MN-STATE-023,MN-STATE-024,MN-STATE-025,MN-STATE-026,MN-STATE-027,MN-STATE-028,MN-STATE-029,MN-STATE-030,MN-STATE-031,MN-STATE-032,MN-STATE-033,MN-STATE-034,MN-STATE-035,MN-STATE-036,MN-STATE-037,MN-STATE-038,MN-STATE-039,
MZ-STATE-001,MZ-STATE-002,MZ-STATE-003,MZ-STATE-004,MZ-STATE-005,MZ-STATE-006,MZ-STATE-007,MZ-STATE-008,MZ-STATE-009,MZ-STATE-010,MZ-STATE-011,MZ-STATE-012,MZ-STATE-013,MZ-STATE-014,MZ-STATE-015,MZ-STATE-016,MZ-STATE-017,MZ-STATE-018,
NG-STATE-001,NG-STATE-002,NG-STATE-003,NG-STATE-004,NG-STATE-005,NG-STATE-006,NG-STATE-007,NG-STATE-008,NG-STATE-009,NG-STATE-010,NG-STATE-011,NG-STATE-012,NG-STATE-013,NG-STATE-014,NG-STATE-015,NG-STATE-016,NG-STATE-017,NG-STATE-018,
OD-STATE-001,OD-STATE-002,OD-STATE-003,OD-STATE-004,OD-STATE-005,OD-STATE-006,OD-STATE-007,OD-STATE-008,OD-STATE-009,OD-STATE-010,OD-STATE-011,OD-STATE-012,OD-STATE-013,OD-STATE-014,OD-STATE-015,OD-STATE-016,OD-STATE-017,OD-STATE-018,
PB-STATE-001,PB-STATE-002,PB-STATE-003,PB-STATE-004,PB-STATE-005,PB-STATE-006,PB-STATE-007,PB-STATE-008,PB-STATE-009,PB-STATE-010,PB-STATE-011,PB-STATE-012,PB-STATE-013,PB-STATE-014,PB-STATE-015,PB-STATE-016,PB-STATE-017,PB-STATE-018,PB-STATE-019,
RJ-STATE-001,RJ-STATE-002,RJ-STATE-003,RJ-STATE-004,RJ-STATE-005,RJ-STATE-006,RJ-STATE-007,RJ-STATE-008,RJ-STATE-009,RJ-STATE-010,RJ-STATE-011,RJ-STATE-012,RJ-STATE-013,RJ-STATE-014,RJ-STATE-015,RJ-STATE-016,RJ-STATE-017,RJ-STATE-018,RJ-STATE-019,RJ-STATE-020,RJ-STATE-021,RJ-STATE-022,RJ-STATE-023,RJ-STATE-024,RJ-STATE-025,RJ-STATE-026,RJ-STATE-027,RJ-STATE-028,
SK-STATE-001,SK-STATE-002,SK-STATE-003,SK-STATE-004,SK-STATE-005,SK-STATE-006,SK-STATE-007,SK-STATE-008,SK-STATE-009,SK-STATE-010,SK-STATE-011,SK-STATE-012,SK-STATE-013,SK-STATE-014,SK-STATE-015,SK-STATE-016,SK-STATE-017,SK-STATE-018,SK-STATE-019,
TG-STATE-001,TG-STATE-002,TG-STATE-003,TG-STATE-004,TG-STATE-005,TG-STATE-006,TG-STATE-007,TG-STATE-008,TG-STATE-009,TG-STATE-010,TG-STATE-011,TG-STATE-012,TG-STATE-013,TG-STATE-014,TG-STATE-015,TG-STATE-016,
TN-STATE-001,TN-STATE-002,TN-STATE-003,TN-STATE-004,TN-STATE-005,TN-STATE-006,TN-STATE-007,TN-STATE-008,TN-STATE-009,TN-STATE-010,TN-STATE-011,TN-STATE-012,TN-STATE-013,TN-STATE-014,TN-STATE-015,TN-STATE-016,TN-STATE-017,TN-STATE-018,
TR-STATE-001,TR-STATE-002,TR-STATE-003,TR-STATE-004,TR-STATE-005,TR-STATE-006,TR-STATE-007,TR-STATE-008,TR-STATE-009,TR-STATE-010,TR-STATE-011,TR-STATE-012,TR-STATE-013,TR-STATE-014,TR-STATE-015,TR-STATE-016,TR-STATE-017,TR-STATE-018,
UK-STATE-001,UK-STATE-002,UK-STATE-003,UK-STATE-004,UK-STATE-005,UK-STATE-006,UK-STATE-007,UK-STATE-008,UK-STATE-009,UK-STATE-010,UK-STATE-011,UK-STATE-012,UK-STATE-013,UK-STATE-014,UK-STATE-015,UK-STATE-016,UK-STATE-017,UK-STATE-018,
UP-STATE-001,UP-STATE-002,UP-STATE-003,UP-STATE-004,UP-STATE-005,UP-STATE-006,UP-STATE-007,UP-STATE-008,UP-STATE-009,UP-STATE-010,UP-STATE-011,UP-STATE-012,UP-STATE-013,UP-STATE-014,
WB-STATE-001,WB-STATE-002,WB-STATE-003,WB-STATE-004,WB-STATE-005,WB-STATE-006,WB-STATE-007,WB-STATE-008,WB-STATE-009,WB-STATE-010,WB-STATE-011,WB-STATE-012,WB-STATE-013,WB-STATE-014,WB-STATE-015,WB-STATE-016,WB-STATE-017,WB-STATE-018,WB-STATE-019,WB-STATE-020,WB-STATE-021,WB-STATE-022,WB-STATE-023
```

## Per-jurisdiction-ledger control totals

| Jurisdiction source ledger | Total IDs | Missing from master |
|---|---:|---:|
| `ANDAMAN_NICOBAR_ISLANDS_SOURCE_LEDGER.md` | 20 | 20 |
| `BIHAR_SOURCE_LEDGER.md` | 18 | 0 |
| `CHANDIGARH_SOURCE_LEDGER.md` | 20 | 20 |
| `DADRA_NAGAR_HAVELI_DAMAN_DIU_SOURCE_LEDGER.md` | 16 | 16 |
| `DELHI_SOURCE_LEDGER.md` | 18 | 18 |
| `GOA_SOURCE_LEDGER.md` | 17 | 0 |
| `GUJARAT_SOURCE_LEDGER.md` | 15 | 0 |
| `HARYANA_SOURCE_LEDGER.md` | 18 | 0 |
| `HIMACHAL_PRADESH_SOURCE_LEDGER.md` | 26 | 0 |
| `JAMMU_KASHMIR_SOURCE_LEDGER.md` | 22 | 22 |
| `JHARKHAND_SOURCE_LEDGER.md` | 22 | 0 |
| `KARNATAKA_SOURCE_LEDGER.md` | 20 | 0 |
| `KERALA_SOURCE_LEDGER.md` | 18 | 0 |
| `MADHYA_PRADESH_SOURCE_LEDGER.md` | 20 | 0 |
| `MAHARASHTRA_SOURCE_LEDGER.md` | 20 | 0 |
| `MANIPUR_SOURCE_LEDGER.md` | 39 | 39 |
| `MEGHALAYA_SOURCE_LEDGER.md` | 15 | 15 |
| `MIZORAM_SOURCE_LEDGER.md` | 18 | 18 |
| `NAGALAND_SOURCE_LEDGER.md` | 18 | 18 |
| `ODISHA_SOURCE_LEDGER.md` | 18 | 18 |
| `PUNJAB_SOURCE_LEDGER.md` | 19 | 19 |
| `RAJASTHAN_SOURCE_LEDGER.md` | 28 | 28 |
| `SIKKIM_SOURCE_LEDGER.md` | 19 | 19 |
| `TAMIL_NADU_SOURCE_LEDGER.md` | 18 | 18 |
| `TELANGANA_SOURCE_LEDGER.md` | 16 | 16 |
| `TRIPURA_SOURCE_LEDGER.md` | 18 | 18 |
| `UTTARAKHAND_SOURCE_LEDGER.md` | 18 | 18 |
| `UTTAR_PRADESH_SOURCE_LEDGER.md` | 14 | 14 |
| `WEST_BENGAL_SOURCE_LEDGER.md` | 23 | 23 |

## Control interpretation

1. The exact repository comparison shows a substantially larger gap than the earlier five-ledger integration narrative implied.
2. The five previously identified later contributors, Gujarat, Haryana, Himachal Pradesh, Kerala and Madhya Pradesh, are fully represented in the current master by this comparison, with zero IDs missing from the master for each of those five ledgers.
3. That fact does not establish full later-jurisdiction integration. Nineteen of the 29 jurisdiction source ledgers have at least one ID absent from the master.
4. Bihar, Goa, Jharkhand and Karnataka, as well as the five named later contributors, have zero missing IDs in this comparison. This is a repository-ID result only and does not by itself establish how or when each master row entered the master ledger.
5. `MASTER_ONLY_IDS=67` shows the master also contains IDs not present in the 29 jurisdiction-specific ledgers scanned by the control script. The two sets are therefore not expected to have a one-to-one cardinality relationship.
6. The website fallback rule remains conceptually valid, but the current production builder does not complete the build because Arunachal Pradesh has no controlled local source-ledger rows and its referenced source IDs are not present in the master.
7. The run therefore verifies the control comparison and exposes a separate fallback-coverage defect. It does not verify a successful public-site build.

## Pages workflow result

Run #389 failed at `scripts/build_website_v2.py` with:

`CONTROL FAILURE: completed jurisdiction has no controlled source rows: Arunachal Pradesh`

The source-ledger control artifact was successfully uploaded before the build failure. `Sanitize generated public HTML`, `Validate generated site`, `Configure GitHub Pages`, `Upload Pages artifact` and `Deploy to GitHub Pages` were skipped.

No generated Pages artifact exists from run #389. No claim of successful publication or live-site synchronization is made.

## Verification scope

This record is limited to the deterministic source-ID comparison and workflow-control result. It does not reopen substantive jurisdiction research, does not modify the master State Implementation Source Ledger, and does not authorize Ladakh, Lakshadweep or Puducherry research.

No Bill drafting, policy-superiority/necessity analysis, constitutional-validity analysis or Phase 2 case-law research was performed.
