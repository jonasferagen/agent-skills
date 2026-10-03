# Run-record pattern capture

2026-10-03. Conditional application-design reference; no new skill or schema.

Mechanism: retained stage outcomes and consumed-byte identities explain partial
completion; an explicit publication boundary determines what recovery can promise.
Applies to operations whose results need later recovery or handoff evidence. A
pure read-only calculation returning a value is outside scope.

The existing application-design state/recovery guidance and external-integrations
reference already own the broad rules. The new reference supplies conditional
file-record detail without requiring a job framework or adding an ordinary-work
capture pass. Source examples differ: staged runs retain stage state, adoption
replaces files individually, and package preparation publishes a staged directory
under a serial writer assumption. They do not establish a common transaction.

A temporary-directory experiment exercised existing Python source-comparison and
atomic-write helpers. A changed source was detected; restoring original bytes
returned unchanged, demonstrating the limit on historical claims. Injected failure
before replacement preserved the old file. Completing one replacement and failing
the second left mixed old/new output. Temporary fixtures were removed; source
projects were not edited. This validates the stated limits, not power-loss recovery,
concurrent publication or the complete source applications. Staged directory
publication was inspected, not executed. No implementation defect repair is claimed.

Required boundary cases include interrupted publication, conflicting revision
identity, changed input during capture, unknown stage outcome and safe repetition.
The independent supplied-metadata design trial below covers a subset; unexercised
cases remain limits. Clear-writing review kept byte identity, canonical identity,
source comparison, publication and acceptance distinct. Package checks pass.

## Independent draft trial

A fresh subagent received six synthetic tasks and three discovery descriptions,
with no expected answers. It read the three SKILL.md files, run-records.md, the
Forge calibration process and its command guide. All six reads were relevant to
the combined tasks; context was reused across tasks, so this is not six isolated
cold-entry trials. No maintenance catalog or source history was loaded. The trial
used source worktrees, not a copied standalone installation; package validation
checks installation boundaries separately. No automatic-discovery reliability is
claimed.

Observed responses preserved nonzero probe failure and existing log checks pending
engine evidence; retained source UID/import files and excluded generated cache;
required transformed bounds and identified animation samples; kept an already-seen
observer informed and traversal feedback separate from creative acceptance. The
review followed the deeper calibration route without importing old observer facts
or adopting its proposed status. Screenshot renaming activated no review skill.

The run-record case proposed immutable revision publication with a single pointer
and cooperating-writer lock for concurrent delivery, and named fixed-path readers
and power-loss durability as unresolved constraints. The string-length function
received no receipt system. These are design responses, not executed recovery or
engine tests. No demonstrated guidance defect was found. Remaining validation is
real engine behavior, actual human review use and isolated consumer discovery.
