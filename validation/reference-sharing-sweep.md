# Reference ownership and checked copies — 2026-10-09

This source-maintenance sweep starts at `c2af65655109218569b2bffd79680b4fadff1765`.
The author retained the mapping discussion and reviewed the implementation with
another agent carrying the same task context. The routing exercises below are
informed walkthroughs, not independent discovery acceptance. No release tag or
consumer installation is created here.

## Shared values and distribution boundary

Source-of-truth 3.1.0 moves the external-identifier rule from definitions into
the self-contained `references/authoritative-values.md`. The entrypoint and
definitions route to it. It preserves the existing configuration owner, permits
explicitly supplied or derived inputs, distinguishes missing resources from
wrong values, and retains historical observations. It selects no README format,
repository layout or runtime configuration scheme. Installing or invoking the
skill does not establish those project choices.

A distribution can import this reference alone, recording its owning skill,
version, path and full commit. It remains an exact file import, not a second
skill registration. Complete skill imports remain unchanged. The file has no
sibling links, imports or other required resources. Distribution-specific
adoption, external-repository conventions and commands stay downstream.

The README and repository instructions now distinguish authoring reuse from
installed package closure. Reciprocal copy comments check that the counterpart
files still exist and name each other; they do not prove agreement. Contextual
applications of test, fixture, policy and evidence rules retain their separate
wording and recorded relationships.

## Two bounded checks

The module-syntax section in typescript-patterns is authoritative for its exact
copy in typescript-design. Both packages remain complete. The source gate reads
the two current passages and fails when either changes without the other.
Versions 2.0.2 and 1.0.2 clarify ownership without changing the TypeScript rule.

The runtime-operations `ServiceReport` declarations own the wire schema and
closed state/lifecycle vocabularies. The checker compares the standalone
dispatcher's schema and states and the service convention's schema, states and
lifecycles against them. Vocabulary order is not a protocol rule; membership is
compared as a set, while duplicate or empty declarations fail. Runtime-operations
2.1.1 and repository-services 0.3.1 clarify this ownership; report behavior and
the explicit service-member interface from 0.3.0 are unchanged.

These copies stop at source-of-truth's check rung. Installed packages cannot
import their siblings, and the copied dispatcher must run without any skill
installation. A new assembly lifecycle for these small copies would cost more
than a bounded comparison. No generic fragment format, prose compiler or runtime
dependency was introduced. The gate reads both current owners rather than a
committed expected vocabulary. It does not compare every repeated paragraph or
prove every service-report meaning.

## Executed evidence

`scripts/check_shared_contracts.py` performs six comparisons and names its measured
root. Its tests fabricate a separate tree with a different schema and vocabulary;
source/copy changes, stale guide vocabulary, missing homes, malformed code and
missing/empty/duplicate sections fail for their stated reasons. Reordering a
vocabulary remains valid. The command works from another directory and its help
shows the actual invocation path.

Compatibility tests send the real producer's messages through both report readers
for every current state and lifecycle, and exercise malformed/incompatible inputs.
The runtime reader clears an unknown lifecycle while the read-only dispatcher
preserves it; a pre-lifecycle report stays visible in both. A copied dispatcher
also consumes real producer messages through a fabricated executable controller
in an isolated temporary checkout with no runtime skill installation. This is
local protocol evidence, not a live service operation or readiness assessment.

The complete check command passes: 28 packages, six shared-contract comparisons,
and 176 tests across four discovered suites, with no skips. The source suite has
25 tests, repository-services 44, runtime-operations 81 and work-records 26.
`git diff --check` and the system skill validator for source-of-truth also pass.
The full command ran after the vocabulary-order correction. Node 24, the pinned
TypeScript compiler, Python and GnuPG were available; the normal gate includes
the GnuPG round trip and extracted language examples.

## Practical routing walkthroughs

An isolated synthetic consumer outside this checkout received a complete copy of
source-of-truth and a project instruction selecting it for shared-value drift.
Its settings file owned a namespace, the current README repeated an older value,
and a dated evidence file retained that older value.

For the reconciliation task, the author read the project hook, the affected
configuration and documents, the installed skill entrypoint and its new
shared-value reference. The README was changed to name and link the settings key;
configuration and retained evidence stayed unchanged. No references scaffold was
created. This exercises the new direct route without a framework installation.

For a nearby literal spelling correction, the author changed only the existing
README sentence. No configuration or installation work was performed and no
additional guidance was loaded. Because this followed the first case in the
same context, it is a scope walkthrough rather than a cold negative control.

For source maintenance, the author followed repository package-use guidance to
the TypeScript passage owner and copy, then ran the bounded checker and its
synthetic drift cases. A changed owner and a changed copy each failed; ordinary
package links still resolve without companion installation. The service cases
exercise the distinct protocol boundary rather than treating prose parity as
behavioral evidence.

Clear-writing and its instruction guidance were applied to the changed prose;
Python language/design and verification/test-writing guidance informed the
checker and tests. The general lesson already belongs to source-of-truth;
pattern-capture therefore selected that home rather than creating another skill.
Fresh-context discovery and broader post-refactor review remain separate future
evidence; these informed walkthroughs do not establish automatic activation.
