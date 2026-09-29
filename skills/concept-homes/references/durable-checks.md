# Checks that survive restructuring

Rung 5 leaves a check behind. Each property below is stated as a rule, the shape
that breaks it, and the shape that holds. The failure they close is never
permissiveness: it is a check that encodes the structure it is checking, so every
legitimate move of that structure turns the gate red, or sends someone to
re-bless a baseline.

The cure is not more checks. It is checks built so that structural change cannot
rot them. [Make disagreement fail](boundaries.md#make-disagreement-fail) says
what a check must compare and where it must run; this page says what keeps it
from rotting afterwards. Whether a check is the right remedy at all is the
[rung ladder](../SKILL.md#derive-instead-of-restate)'s question — a check is
rung 5 because the four rungs above make disagreement impossible rather than
loud — and whether it earns its recurring cost is the reading project's own
policy. Examples are synthetic.

## Compute the invariant live

If the correct answer can be computed when the check runs, compute it. A
committed "expected" count or snapshot freezes last week's answer into the
repository, and every legitimate change then has to re-bless it. That
re-blessing is the treadmill, and it trains reviewers to approve diffs they
never audited.

- **Breaks:** a drift checker that stamps counts into committed baseline files
  and reports differences against them. Nothing consumes the report, it re-scans
  the whole tree on every run, and it goes red on every restructure.
- **Holds:** a parity check that reads both homes as they stand — two live
  databases, or a schema and the code that mirrors it — and compares them. There
  is no golden to re-bless, so a legitimate change cannot rot it.

A literal expectation is not a golden. A test stating the value an operation
should produce is doing its job, as
[what is not a second home](../SKILL.md#what-is-not-a-second-home) says. What
rots is a committed copy of a *structural* fact — a count, a file list, an
inventory — that is meant to track the home and can only be kept current by
hand.

A **shrink-only ledger** is a bounded exception rather than a golden: it names
known debt being paid down, belongs to the tree whose files it lists rather than
to a shared tool, gates hard — a new or increased violation fails — and only
ever gets shorter, so there is no moving count to chase.

## Anchor to the check's own location, or to version control

A check locates its own subject. It must not assume the directory it was
launched from, and it must not spell out where another tree sits.

Inventory commands such as `git ls-files` and `git grep` resolve relative to the
caller's working directory, so a check that derives a file set inherits whatever
directory invoked it. Resolve the root first — `git rev-parse --show-toplevel`,
or the equivalent lookup for the tool in hand — then run the query against that
root. Have the verdict name that root and the set it measured, so a partial
denominator cannot read as a whole-tree result.

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

## Fabricate the fixture

A check's own test carries its own world. It must not depend on which optional
components are present, which services are running, or which host tools happen
to be installed — none of which are facts about the concept it protects.

- **Breaks:** a test that reaches for a real neighbouring checkout or boots a
  live service. An incomplete environment then fails the gate on shape.
- **Holds:** a test that stubs the external commands it needs onto the path and
  builds the whole tree it examines inside a temporary directory. It depends on
  nothing real, so nothing real can break it.

## Report an absent dependency as absent

Distinguish "cannot run here" from "ran, and the homes disagree", and never let
the first report as the second. A check fails at the boundary that owes the
missing precondition, not on the surface that merely depends on it.

Who owes the dependency decides the remedy. Where the environment contract owes
it — a binary the image installs, a mounted path, a required variable — fail
where that contract is established, naming what is missing. Skipping there is a
false green, because the gate then certifies a tree it never exercised. Where
nobody opted in — an optional profile, a live backend — exit successfully with a
loud notice instead.

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
directories is this anti-pattern enforcing itself: it carries the topology as a
literal, and it needs re-blessing every time the structure moves. Where a
project wants these rules enforced mechanically, the enforcement lives in the
tree it checks, scoped to that tree, deriving its file set from version control
rather than from a copied list.
