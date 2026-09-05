# Control Decisions, 2026-09-06

These decisions are a controlled extension of `DECISIONS_LOG.md`. Existing decision IDs are preserved and are not renumbered. This addendum records only decisions made during the present control-remediation workstream.

| ID | Date | Decision | Reason | Status |
|---|---|---|---|---|
| DEC-CTRL-2026-09-06-001 | 2026-09-06 | Establish `project-state/PH1_CONTROL_MATRIX_2026-09-06.md` as the authoritative Phase 1 control-definition matrix for status terms, source hierarchy, conflict resolution, search stopping, reopening and reconciliation standards. | The audit identified multiple status terms and control rules that were not governed by one formal matrix. | ACTIVE |
| DEC-CTRL-2026-09-06-002 | 2026-09-06 | Define COMPLETED, VERIFIED, CURRENT, OPEN, QUALIFIED and PROCEED/CLOSE WITH LIMITATIONS as distinct control concepts. | Prevents an inventory being silently treated as a current, exhaustive or unqualified legal census. | ACTIVE |
| DEC-CTRL-2026-09-06-003 | 2026-09-06 | Apply the formal source hierarchy and conflict-resolution rule in all subsequent Phase 1 work. | Prevents lower-authority webpages, historical reports or search silence from overriding controlling instruments or unresolved conflicts. | ACTIVE |
| DEC-CTRL-2026-09-06-004 | 2026-09-06 | Apply the universal search stopping rule and prohibit materially identical repeated searches without a new retrieval route, repository update, document identifier or reasoned expansion. | Addresses recurring search loops and prevents false confidence from repeated negative retrieval. | ACTIVE |
| DEC-CTRL-2026-09-06-005 | 2026-09-06 | Reconcile `legislation/STATE_IMPLEMENTATION_INVENTORY.md` against the 33 verified jurisdiction artifacts. | The master State inventory was stale relative to the substantive jurisdiction artifacts. | COMPLETED |
| DEC-CTRL-2026-09-06-006 | 2026-09-06 | Do not reopen completed jurisdictions solely because a dedicated control artifact is absent. Reopening requires a substantive evidentiary or control defect meeting the formal reopening rule. | Missing control artifacts must not create unnecessary substantive research loops. | ACTIVE |
| DEC-CTRL-2026-09-06-007 | 2026-09-06 | Record the master source-ledger reconciliation in `research/STATE_IMPLEMENTATION_SOURCE_LEDGER_RECONCILIATION_2026-09-06.md` without falsely claiming later jurisdiction rows are integrated into the master ledger. | The master ledger's last verified substantive integration point remains Maharashtra. The distinction must be explicit before a safe later-row integration operation. | ACTIVE |
| DEC-CTRL-2026-09-06-008 | 2026-09-06 | Require a controlled master source-ledger integration write followed by independent re-read and zero-drift testing before control remediation is closed. | Prevents destructive reconstruction or silent source-row loss during synchronization. | ACTIVE |
| DEC-CTRL-2026-09-06-009 | 2026-09-06 | Do not begin Ladakh, Lakshadweep or Puducherry research until the present control-remediation gate is closed. | The user-authorized sequence requires control remediation before new substantive work. | ACTIVE |
| DEC-CTRL-2026-09-06-010 | 2026-09-06 | Preserve the exact 377-ID master-versus-jurisdiction comparison as an immutable control baseline during website remediation. | The discrepancy was independently verified and must not be altered to make the website build pass. | COMPLETED |
| DEC-CTRL-2026-09-06-011 | 2026-09-06 | Resolve jurisdiction source coverage from master-ledger jurisdiction sections before applying local-ledger fallback. | Arunachal's build failure was caused by source-selection logic, not absence of controlled master rows. | COMPLETED |
| DEC-CTRL-2026-09-06-012 | 2026-09-06 | Treat jurisdiction-ledger fallback rows as public evidence with explicit fallback provenance, never as master-ledger integration. | Prevents website fallback from concealing or rewriting substantive master-ledger gaps. | ACTIVE |
| DEC-CTRL-2026-09-06-013 | 2026-09-06 | Run public-content sanitization before final generated-site leakage validation, with sanitization limited to generated HTML. | Substantive source documents contain internal-control wording that must not leak into public pages, while the source records themselves must remain unchanged. | COMPLETED |
| DEC-CTRL-2026-09-06-014 | 2026-09-06 | Require the Pages artifact itself to pass page-count, route, navigation, accessibility, link-integrity, source-coverage and public/internal separation tests before deployment. | Workflow success alone is insufficient evidence of production website integrity. | COMPLETED |
| DEC-CTRL-2026-09-06-015 | 2026-09-06 | Accept run #397 as a successful website/source-rendering control gate, but do not treat it as substantive Phase 1 acceptance. | The website control defect is fixed, while the three remaining jurisdictions and substantive Phase 1 residuals remain open. | ACTIVE |

## Decision-control status

Website/source-ledger rendering remediation: CLOSED AND VERIFIED.

Pages workflow/artifact validation: CLOSED AND VERIFIED for run #397.

Exact 377-ID master-versus-jurisdiction comparison: PRESERVED AND VERIFIED.

Master-ledger later-row integration: NOT CLOSED. No master-ledger content was modified by this remediation.

Phase 1 substantive acceptance: NOT YET SATISFIED.

Next substantive authorization remains gated by the documented remediation closure and the existing Phase 1 control matrix.
