# Plan

## Recovery evidence before cleanup

Status: proposed next step; not executed. Owner: archive maintainer (individual not recorded).

The evidence in [design.md](design.md) records one successful copy command and no restore attempt. It does not satisfy the evidence required by [policy.md](policy.md): recovery remains unverified, including the limit of 24 hours of loss. This is missing proof, not proof that recovery would fail.

Next bounded step: the archive maintainer should restore a small, explicitly selected set from the existing local backup into a separate local scratch directory, preserving all originals. Inputs are the selected original files, their corresponding backup copies, a safe scratch destination and available copy timestamps or run records. Record the selected files, backup and restore times, comparison results (byte equality or hashes), and whether the restored files can be opened. Record failures and missing inputs explicitly. This step requires authorized access to the photos; this plan update does not execute it.

Completion evidence: a dated restore record identifies the tested backup and files and demonstrates that the restored originals match and are readable, or records the failure and next corrective action. A sample establishes recovery only for the tested scope; broader coverage remains unverified. Review available backup timing evidence against the 24-hour loss limit and explicitly retain any cadence or coverage gap. One successful copy or restore does not establish an ongoing 24-hour guarantee.

Daily cleanup after copying is deferred until recovery evidence and the loss limit are supported, and the intended cleanup behavior has been checked against the obligation to preserve originals. Revisit cleanup after the bounded check; do not treat a successful sample as permission to delete originals.

Storage migration and cloud access remain deferred as recorded in [context.md](context.md); revisit only when project scope changes. Neither is a prerequisite for this local recovery check.
