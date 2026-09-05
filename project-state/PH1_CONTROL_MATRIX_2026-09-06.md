# Phase 1 Control Matrix

Date: 2026-09-06
Phase: 1, Existing-Law Baseline and Source Map
Status: ACTIVE

## Authority

This file is the authoritative Phase 1 control-definition matrix for status terminology, source hierarchy/conflict resolution, search stopping rules and reconciliation states. It does not replace jurisdiction-specific substantive records, the Research Ledger, Issues Register or Decisions Log. Those records remain authoritative for their respective domains.

## 1. Status definitions

| Term | Formal definition | What it permits | What it does not permit |
|---|---|---|---|
| COMPLETED | The assigned workstream's defined inventory/extraction task has been performed to its stated scope and its principal artifact exists. | Treat the task as performed and move to the next authorized workstream. | Does not mean exhaustive, current, complete in 2026, or free of residual issues. |
| VERIFIED | The proposition or artifact has been checked against its cited source and the source supports the proposition at the stated level. | Use the proposition at the recorded evidence grade and qualification. | Does not imply statewide/national completeness or currentness unless expressly verified. |
| CURRENT | The source or instrument is verified as operative/relevant for the stated reference date or reporting period. | Use it for current-status statements within its verified scope. | Does not extend currentness beyond the verified date or scope. |
| OPEN | A material question, evidence gap, contradiction or control defect remains unresolved and requires action or an explicit closure decision. | Carry the item forward and prevent unsupported closure. | Does not mean the underlying proposition is false. |
| QUALIFIED | A workstream/proposition is usable for progression but has an identified limitation, residual, source-grade constraint or currentness restriction. | Use with the recorded qualification. | Does not support an unqualified completion/currentness claim. |
| PROCEED/CLOSE WITH LIMITATIONS | The defined jurisdiction/workstream inventory is sufficiently developed to leave the workstream without reopening it, while specified residuals remain open and are carried into closure. | Proceed to the next authorized workstream without treating the residuals as resolved. | Does not mean all current instruments, implementation details or residuals are verified. |

## 2. Status precedence

Where labels overlap, use the narrowest proposition supported by evidence. `VERIFIED` describes evidentiary support. `CURRENT` describes temporal/operative status. `COMPLETED` describes task performance. `QUALIFIED` describes limitations. `OPEN` controls unresolved matters. `PROCEED/CLOSE WITH LIMITATIONS` is a workstream disposition, not a claim that every component is current or complete.

No status term may be silently upgraded because a later source is convenient, a search returns no contrary result, or another jurisdiction has stronger evidence.

## 3. Source-of-truth hierarchy

For a proposition, apply the following order unless the proposition's nature requires a more specific source:

1. Constitution of India and authoritative constitutional text.
2. Central or State legislation and Rules in authoritative statutory/Gazette form.
3. Official Government Gazette notifications, orders, circulars, appointments and other operative instruments.
4. Supreme Court/High Court judgments and orders for judicial propositions and procedural status.
5. Parliament/Digital Sansad and Parliamentary Committee records for parliamentary facts and official statements.
6. Official Government departmental, police, prosecution, judicial and administrative records, including current repositories and reports.
7. NCRB, BPRD and other official statistical datasets for their defined statistical propositions.
8. Official institutional or commission records.
9. Reliable secondary sources for leads, corroboration or context where primary material is unavailable.
10. Weak/unverified material only as a search lead, never as the sole basis of a material conclusion.

Evidence grade remains independent of hierarchy. A source must be graded according to the project's A/B/C/D standard.

## 4. Conflict-resolution rule

When sources conflict:

1. Identify whether they address the same proposition, date and scope. If not, record them as non-conflicting reporting-period/scope differences.
2. Prefer the higher-authority source for the proposition at issue.
3. Among sources of the same authority, prefer the later operative instrument for current status, unless the later instrument expressly preserves, limits or supersedes the earlier one.
4. A court judgment/order controls propositions about judicial holdings and the status of proceedings within its scope.
5. A Gazette/statutory instrument controls the legal existence and operative wording of the instrument; an administrative webpage cannot silently amend it.
6. A current administrative webpage may establish published current architecture but does not substitute for an underlying appointment, notification, establishment or amendment instrument when instrument-level verification is required.
7. Historical reports remain valid for their reporting period. They do not become current merely because no newer contrary source was found.
8. If conflict cannot be resolved from authoritative sources, retain both propositions, log the contradiction, mark the issue OPEN, and do not infer a resolution.
9. Search silence never resolves a legal conflict or proves absence.

## 5. Universal search stopping rule

A search loop may stop for a specific residual only when one of the following controlled outcomes is reached:

A. VERIFIED RESOLUTION: an authoritative source directly resolves the question and its scope/date are recorded.

B. CONTROLLED NEGATIVE RESULT: the defined authoritative repositories and reasonable search variants have been searched, no operative source was located, and the record explicitly states that non-location is not proof of legal absence.

C. ACCESS/RETRIEVAL BLOCK: the authoritative source is identified but cannot be retrieved with available tooling. Record the source identity, retrieval failure, attempted route and required follow-up.

D. CONFLICT REQUIRES ESCALATION: authoritative sources conflict and no controlling later instrument/judgment resolves the conflict. Stop the loop, preserve both sources and open an issue.

E. SCOPE SATISFIED: the assigned task's defined scope is complete and remaining questions belong to a separate later workstream.

Before stopping under B or C, record at least: repository/source family searched, relevant search terms or document identifiers, date of search, result, and residual limitation. Do not repeat substantially identical searches without a new retrieval route, new date, new repository content, a changed document identifier, or a reasoned search expansion.

## 6. Reopening rule

A completed jurisdiction/workstream is not reopened solely because a dedicated control artifact is absent or because a later audit identifies a control-layer synchronization defect. Reopen only where:

- new authoritative evidence directly changes a material recorded proposition;
- an identified source or citation is materially wrong;
- a control defect prevents reliable use of the substantive artifact;
- the original defined scope was not in fact performed; or
- a separately authorized closure workstream requires targeted verification.

## 7. Reconciliation standard

A master index is reconciled when every completed jurisdiction is represented with a traceable substantive artifact path, its status is aligned with the jurisdiction-specific record, all known jurisdiction-specific source ledgers are indexed, controlled absences are explicit, and no cumulative ID is fabricated or renumbered.

A reconciliation index is control metadata. It does not replace the substantive jurisdiction record or silently convert a qualification into a verification.

## 8. Gate effect

This matrix does not alter the Phase 1 gate. Phase 1 remains ACTIVE and acceptance remains NOT YET SATISFIED until the substantive acceptance criteria are independently met.

## Control IDs

- CTRL-2026-09-06-001: Status-definition matrix established.
- CTRL-2026-09-06-002: Source hierarchy and conflict-resolution rule established.
- CTRL-2026-09-06-003: Universal search stopping rule established.
- CTRL-2026-09-06-004: Reopening rule established.
- CTRL-2026-09-06-005: Master-index reconciliation standard established.
