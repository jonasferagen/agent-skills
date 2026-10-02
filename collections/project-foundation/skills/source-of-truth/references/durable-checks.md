# Checks that survive restructuring

Rung 5 leaves a check behind. Each property below is stated as a rule, the shape
that breaks it, and the shape that holds. The failure they prevent is never a
check that is too permissive. It is a check that encodes the structure it is
checking, so every legitimate move of that structure makes the gate fail, or
sends someone to update and re-approve a baseline.

The remedy is not more checks. It is checks built so that structural change
cannot break them.
[Make disagreement fail](boundaries.md#make-disagreement-fail) says what a check
must compare and where it must run; this page says what keeps it working
afterwards. The [rung ladder](definitions.md#derive-instead-of-restate)
decides whether a check is the right remedy at all: a check is rung 5 because
rungs 1 to 4 make disagreement impossible, while a check only makes it fail. The
project's own policy decides whether a check is worth its recurring cost.
Examples are synthetic.

<!-- Package-boundary copy: test-writing/references/fixtures.md (Prefer derived references to stored goldens) states this rule for ordinary tests. Keep both passages aligned. -->
## Compute the invariant live

Compute the answer when the check runs, by reading the homes as they stand. If
a home cannot be read then, do not commit a copy of its answer:
[report the dependency as absent](#report-an-absent-dependency-as-absent), or
stop at rung 6. A committed "expected" count or snapshot stores the answer from
when it was committed, and every legitimate change then has to update and
re-approve it. That update becomes routine, and the routine trains reviewers to
approve diffs they have not read.

- **Breaks:** a drift checker that stamps counts into committed baseline files
  and reports differences against them. Nothing consumes the report, it re-scans
  the whole tree on every run, and it fails on every restructure.
- **Holds:** a parity check that reads both homes as they stand and compares
  them, for example two live databases, or a schema and the code that mirrors
  it. There is no golden to update, so a legitimate change cannot break it.

A literal expectation is not a golden. A test stating the value an operation
should produce is doing its job, as
[what is not a second home](definitions.md#what-is-not-a-second-home) says. What
goes stale is a committed copy of a *structural* fact, such as a count, a file
list or an inventory, that is meant to track the home and can only be kept
current by hand.

<!-- Package-boundary copy: test-audit/references/triage.md applies this ledger rule to test scanners. Keep both passages aligned. -->
A **shrink-only ledger** is a bounded exception rather than a golden. It names
known debt being paid down and belongs to the tree whose files it lists rather
than to a shared tool. It gates hard: a new or increased violation fails. It
only ever gets shorter, so there is no moving count to chase.

## Anchor to the check's own location, or to version control

A check locates its own subject. It must not assume the directory it was
launched from, and it must not spell out where another tree sits.

Inventory commands such as `git ls-files` and `git grep` resolve relative to the
caller's working directory, so a check that derives a file set inherits whatever
directory invoked it. Resolve the root first, with
`git rev-parse --show-toplevel` or the equivalent lookup for the tool in use,
then run the query against that root. Have the verdict name that root and the
set it measured, so a result measured over part of the tree cannot be mistaken
for a whole-tree result.

- **Breaks:** a check that resolves its targets against the process's working
  directory and so measures one subdirectory while reporting on the tree; a
  self-test that builds fixtures at a hard-coded path outside its own tree.
- **Holds:** a check that anchors to its own module or file location, and
  derives every path it needs from version control rather than from a path
  literal.

## Read the manifest — do not copy it

This is rung 1 applied to the check itself. Each structural fact has one
declaration, so the check reads that declaration instead of re-typing it. A
check that restates the home is a second home with a gate attached, and it
drifts exactly as any other restatement does.

- **Breaks:** a directory list hand-copied into four scripts that have already
  diverged from one another; a vocabulary re-asserted as a literal in three
  separate tests.
- **Holds:** a check that reads its directories from the configuration the build
  already reads, or its members from the manifest that declares them. Topology
  has one declaration: resolve through it, never through a constructed path.

<!-- Package-boundary copy: test-writing/references/fixtures.md (Keep fixtures small and inside the test) states this rule for ordinary tests. Keep both passages aligned. -->
## Fabricate the fixture

A check's own test creates its own fixtures. It must not depend on which
optional components are present, which services are running, or which host tools
happen to be installed. None of those are facts about the concept it protects.

- **Breaks:** a test that uses a real neighbouring checkout or boots a live
  service. An incomplete environment then fails the gate for a reason unrelated
  to the concept.
- **Holds:** a test that stubs the external commands it needs onto the path and
  builds the whole tree it examines inside a temporary directory. It depends on
  nothing real outside that directory, so the host environment cannot break it.

## Report an absent dependency as absent

Distinguish "cannot run here" from "ran, and the homes disagree", and never
report the first as the second. A check fails at the boundary responsible for
providing the missing precondition, not on the surface that merely depends on
it.

Who is responsible for providing the dependency decides the remedy. If the
environment contract requires it, as with a binary the image installs, a mounted
path or a required variable, fail where that contract is established and name
what is missing. Skipping there is a false pass, because the gate then reports
success for a tree it never exercised. If nobody opted in to the dependency, as
with an optional profile or a live backend, exit successfully with a loud notice
instead.

- **Breaks:** a check that throws, or asserts against empty output, when a
  required tool is absent. The provisioning gap reads as a defect in the thing
  under check, and every environment lacking the tool re-diagnoses the same
  absence from scratch.
- **Holds:** an environment check that fails at start naming the absent tool,
  leaving the checks downstream of it free of absence guards; and, where the
  dependency is genuinely optional, a check that exits successfully with a
  **loud notice** that it could not run.

The loudness matters as much as the skip. A silent skip is worse than a hard
failure, because it reads as a pass.

## Enforcement belongs in the tree it checks

A detector that pattern-matches a catalogue of signatures across a fixed set of
directories itself follows the anti-pattern it is meant to detect: it
hard-codes the topology, and it needs updating and re-approval every time the
structure moves. Where a project wants these rules enforced mechanically, the
enforcement lives in the tree it checks and is scoped to that tree. It derives
its file set from version control rather than from a copied list.
