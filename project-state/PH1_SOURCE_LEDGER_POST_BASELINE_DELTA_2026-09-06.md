# Phase 1 Source-Ledger Post-Baseline Delta

Date: 2026-09-06

## Control boundary

The verified historical control baseline remains unchanged and is not replaced:

- `MASTER_IDS=261`
- `JURISDICTION_LEDGER_FILES=29`
- `JURISDICTION_LEDGER_IDS=571`
- `MISSING_FROM_MASTER=377`
- `MASTER_ONLY_IDS=67`

A subsequent Pages workflow run, after completion of Ladakh, Lakshadweep and Puducherry, enumerated the current repository filesystem and observed:

- `MASTER_IDS=261`
- `JURISDICTION_LEDGER_FILES=32`
- `JURISDICTION_LEDGER_IDS=628`
- `MISSING_FROM_MASTER=434`
- `MASTER_ONLY_IDS=67`

The increase is attributable to three post-baseline jurisdiction source ledgers: Ladakh, Lakshadweep and Puducherry. Their IDs were not present in the earlier 29-file/571-ID baseline.

This is recorded as a post-baseline filesystem delta, not as a replacement of the preserved 29/571/377 control baseline and not as evidence that the master ledger changed. The master ledger remains at 261 IDs.

## Control decision

Do not rewrite the historical 377-ID comparison as if it were performed after the three later jurisdiction ledgers were added. Do not copy the 57 newly observed post-baseline IDs into the master ledger merely to reconcile the public website.

The public website may render controlled fallback rows from these later jurisdiction ledgers, with explicit fallback provenance. Fallback remains separate from master-ledger integration.
