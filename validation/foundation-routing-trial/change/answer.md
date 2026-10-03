# Archive handoff assessment

Date: 2026-10-03. Sources: `context.md`, adopted obligations in `policy.md`, and observations in `evidence.md`.

## Conclusion and status

The association handoff is a substantive proposed change. It has not been adopted, implemented or verified by this assessment. Preserve the current policy. Before association use, resolve responsibility and access decisions and demonstrate that successive volunteers can retrieve, add and recover documents without relying on the founder remaining available.

The founder alone knowing the passphrase is an observed continuity dependency. Their ability to leave at any time makes durable access a prerequisite for the proposed use. It does not, by itself, establish a breach of the current single-maintainer policy. Separately, compliance with the existing 24-hour loss limit remains unverified today.

## Affected obligations

- **Users and reliance:** One maintainer's private reference use would become continued association use by successive volunteers. This tightens continuity and access requirements; permitted readers, contributors and administrators still need decisions.
- **Lifetime:** “Maintained local archive” would gain a ten-year commitment. This adds specificity and tightens the stated planning obligation, without establishing that the existing commitment ends at ten years. The start date, ongoing maintenance responsibility and disposition after ten years remain open.
- **Recovery ownership:** The founder currently owns recovery. A transfer to association responsibility changes the responsible actor; it does not relax the maximum loss of 24 hours of accepted additions. The association's accountable role, deputies and acceptance of responsibility are undecided.
- **Authority and exposure:** Offline operation and no external transfers remain adopted obligations. Define permitted custody and location under the handoff. Whether the custody transfer fits the existing “no external transfers” boundary requires an explicit decision by the policy owner; do not silently treat the proposal as permission to copy files or disclose credentials.
- **Preserved guarantees:** Retain irreplaceable documents, encryption of retained files, existing identifiers, offline operation and the 24-hour loss limit. No relaxation of these guarantees was requested.

## Decisions and work before handoff

The roles below are proposed owners, not appointments. The current policy owner must identify actual decision authority and obtain the association's explicit acceptance. These items are follow-up work, not actions performed here.

1. **Accountability and succession.** The policy owner and association should name an accountable archive custodian, recovery owner and substitute, with a process for replacing each when volunteers leave. Decide the ten-year period and the end-of-period custody decision. These decisions must precede adoption of the handoff and assignment of operational work.
2. **Independent decryption access.** The association custodian should choose how authorized successors obtain the passphrase or equivalent recovery access without the founder. Define who may hold it, how it is retained offline, how access is recovered if a custodian disappears, and how departure or compromise is handled. Options such as multiple authorized custodians or sealed offline recovery material need evaluation; neither is adopted here. Before handoff, demonstrate decryption by an authorized successor with the founder unavailable, using the intended procedure and custody arrangements.
3. **Volunteer authority and reliable additions.** The custodian should decide who may read, add, correct or delete records, how volunteers are authorized and removed, and when an addition counts as accepted. Determine whether volunteers act sequentially or concurrently and how conflicting additions are prevented or resolved. Before volunteer use, demonstrate retrieval and addition under those rules, preserved identifiers and retained documents, and an adequate departure process. A former volunteer's knowledge of an unchanged shared passphrase cannot simply be revoked administratively.
4. **Recoverability.** The recovery owner should specify backup coverage, timing, failure handling, offline storage and custody of both encrypted files and the means to decrypt them. Include all state needed to interpret the archive and preserve identifiers. Before handoff, perform a restore with an authorized successor, verify documents are readable and complete, compare identifiers and accepted additions, and measure the recoverable cutoff against the 24-hour loss limit. Define repeat checks over the ten-year period and after relevant changes. Backup success alone is insufficient.
5. **Maintenance over ten years.** The association should assign responsibility and resources for storage media, readable formats, software and offline installation/recovery materials. Identify dependencies that could make future access fail. Before handoff, demonstrate the chosen offline retrieval and recovery procedure on the intended replacement environment. Any later migration must preserve identifiers, irreplaceable data and recoverability; no migration is currently authorized or shown necessary.
6. **Custody and scope.** The policy owner should resolve the transfer boundary and define what files, copies and recovery materials may change custody, where they remain, and who is authorized to receive them. This decision precedes any transfer. Acceptance evidence should cover the approved inventory and offline process. Preserve encryption and avoid treating a handoff proposal as an exception to current restrictions.

## Consequences and simplification

Product and architecture need review for successive operators, durable access and loss of founder knowledge. Stored data need an inventory and preservation checks; the fixture supplies no evidence that conversion or deletion is necessary. Interfaces and consumers must preserve existing identifiers; no other consumers or integrations were supplied. Identity and permissions need the volunteer and credential decisions above. Tests and release checks need successor access, offline use, preserved identifiers and measured recovery evidence. Operations need usable procedures for additions, backups, failures and volunteer changes. Documentation must eventually reflect deliberately adopted responsibility and access changes in its owning documents, with procedures and verification results kept separate from policy.

A simple offline archive with documented custody, trained successors and verified recovery may meet the proposed use. A server, cloud service or complex identity system is not established as necessary. Compare simpler mechanisms against the same guarantees before choosing implementation. There is no inspected implementation from which to justify removing existing safeguards.

## Evidence and gate

`evidence.md` establishes only that a backup job reported success yesterday. It supplies no restore outcome or measurement of recoverable accepted additions. It cannot establish usable decryption access, file integrity, identifier preservation or compliance with the loss limit. No operational tests were performed in this document-only fixture.

The gate for the proposed use is: explicit policy and custody decisions by the appropriate owners; accepted operational ownership; implemented successor access and procedures; and recorded acceptance evidence for independent offline retrieval, additions, preservation and recovery within the existing loss limit. Adoption alone does not pass this gate. Continue unaffected work under current policy while the handoff remains proposed.

Checks performed: compared the request with every adopted policy axis; distinguished the current passphrase dependency from proposed association use; checked supplied evidence against the recovery claim; and searched the fixture's project-file inventory for additional owners or consumers. No foundation declaration, boundaries, overview, runbook or task queue was supplied in that inventory. Implementation and downstream consumers remain uninspected. The installed collection's `UPSTREAM.md` provenance was not needed. No policy, guidance, archive data or external systems were changed.
