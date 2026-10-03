# Proposed archive handoff: policy impact assessment

The ten-year association handoff needs new ownership, access and succession decisions. It is not ready on the supplied evidence: the founding maintainer alone knows the decryption passphrase, and yesterday’s successful backup report does not establish recoverability. The proposal has not been adopted or implemented. This assessment leaves `policy.md` unchanged.

## What changes and what stays binding

The proposed use changes reliance from one maintainer’s private reference work to successive volunteers retrieving and adding documents. It adds an explicit ten-year horizon and requires recovery responsibility that survives any individual’s departure. These tighten continuity obligations and change ownership; they do not relax the existing guarantees.

The adopted requirements remain: preserve irreplaceable encrypted files and existing archive identifiers, operate offline without external transfers, and lose at most 24 hours of accepted additions. “Maintainer owns recovery” is still the adopted responsibility until deliberately revised. An association handoff must clarify whether custody changes conflict with “no external transfers”; offline operation alone does not resolve that boundary. No transfer is authorized here.

## Decisions and prerequisites

1. **Accountability and succession — association governing body with the founding maintainer.** Decide who may approve the handoff and nominate accountable archive and recovery roles, deputies, and replacements when volunteers leave. Proposed requirement: retrieval and recovery must not depend on the founder remaining available. The association must accept these responsibilities before the handoff can be called complete.

2. **Decryption continuity — nominated recovery owner.** Decide how authorized successors obtain usable decryption access without the founder, while preserving confidentiality. Options include controlled offline recovery custody or multiple authorized custodians; no particular mechanism is adopted. Define who may use recovery access, how it is kept current and how loss or departure is handled. A document saying where a passphrase is kept is insufficient unless an authorized successor can actually recover and decrypt the archive. This blocks a credible continuity claim now.

3. **Volunteer access and departure — archive owner with the association.** Define who may retrieve, add, correct or delete documents; whether additions require acceptance; and how departing volunteers lose future access. Shared knowledge of a passphrase cannot simply be “revoked.” Decide whether a departure requires credential or encryption changes and how old backups remain recoverable. Do not promise recall of copies already accessible to former volunteers. These decisions govern onboarding, departure procedures and any necessary implementation work.

4. **Recovery scope and targets — recovery owner and association.** Preserve the 24-hour loss limit and define the acceptance event used to measure it. Decide tolerable downtime, covered failure scenarios, backup custody and recovery ownership. Include founder unavailability and loss of the working device among the proposed scenarios to test. The backup and recovery process must preserve the original identifiers and document contents. A particular backup schedule is a mechanism, not proof of the loss guarantee.

5. **Ten-year stewardship — association governing body.** Assign capacity for periodic recovery checks, media and software maintenance, documentation updates and successor training. Decide custody at the end of ten years or if the association dissolves; the horizon does not authorize deleting irreplaceable files. Any migration must preserve identifiers and verified content. These decisions block a complete long-term operating commitment.

6. **Custody boundary — current policy owner and association.** Clarify which people, devices and physical storage locations belong within the approved local archive boundary. If association custody constitutes an external transfer under current policy, it needs an explicit authorized policy decision before execution. Preserve offline operation; cloud storage or remote key services are not assumed solutions.

## Evidence required before handoff

- An authorized successor, working without the founder’s help, retrieves existing documents and completes a restore into an isolated local test environment using the documented recovery materials.
- The restore verifies decryption, file integrity, stable identifiers and the recoverable set of accepted additions. Compare the accepted-addition history with restored records at a stated failure time to show the loss is within 24 hours. A successful job report alone cannot establish this.
- A volunteer follows documented onboarding, adds a document through the agreed acceptance process and retrieves it. A departure exercise demonstrates the chosen access change and continuing recovery access.
- The recovery owner records results, failures and unresolved limits, including measured restore duration against the downtime target once chosen. The association records responsibility acceptance and a schedule for repeating checks after key, personnel or storage changes.

The supplied evidence establishes only that a backup job reported success yesterday. Recoverability and compliance with the loss limit remain unverified, rather than proven failed. The founder-only passphrase is a known dependency that must be removed or otherwise addressed before independent succession is demonstrated.

## Transition and limits

Keep policy adoption, implementation and verification separate: approve the changed responsibilities and unresolved choices; implement authorized custody, access and recovery arrangements; then collect the evidence above before relying on the handoff. Preserve the existing archive during tests and migration. Record adopted decisions in `policy.md`, procedures in their appropriate owner and results in `evidence.md` when that work is authorized.

This document reviewed only `context.md`, `policy.md` and `evidence.md` with the installed guidance. No systems, backups or permissions were inspected or changed. No handoff, setup or external action occurred. Code, storage formats and available equipment remain unknown; the proposed requirements do not prescribe an unnecessary implementation.
