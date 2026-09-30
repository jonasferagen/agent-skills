# Boundaries that forbid derivation

Four boundaries commonly stop a consumer from reading a concept's home. Each
leaves a different set of rungs available, so name the boundary before settling
for a lower rung. Examples are synthetic.

## The language boundary

The home is in one language and a consumer is in another. Copying the values
across is the obvious move and the wrong one, because each language normalises
differently. For example, one URL parser may expose a bracketed IPv6 host and
another the bare address, so the two allow-lists that mean the same thing cannot
be the same strings. A copy looks right, passes review, and encodes a difference
nobody stated.

Available: build-time generation from the home into each language; a data file
both languages read at run time; or, where the home is a database, reading it
directly from both.

If the rule must be stated once per language, say in each place that it is one
rule with two spellings, and add a check that compares the two after
normalising. Do not add a check that restates the expected values; it would be
a third home.

## The bundle boundary

A client cannot import a server module without shipping that module's
dependencies. This is a real cost, not a style objection: one import can pull a
validation library or a database driver into a browser bundle.

Available: request-time delivery (rung 4), which sends the concept with the data
that needs it; or extracting a dependency-free module that both sides import,
while the heavier machinery stays in the home.

Type-only declarations are erased at compile time and cross this boundary for
free, so sharing a type costs nothing while sharing a value may cost a great deal.
Check which one the consumer actually needs before deciding the boundary blocks
you.

## The process boundary

Two processes each own a setting the other needs. For example, each half of a
pair needs the other's address, or each side of a handoff needs the other's
schedule. Neither can read the other's configuration, and code shared between
them cannot know either setting.

Available: make the value an explicit input at the edge. The process that owns a
setting passes it in; shared code receives it and never guesses. A hardcoded
default inside the shared code is the shape to remove, because it is a second home
for a value the edge already knows.

Where neither process can know the other's value, the pair itself is the concept
and needs a home outside both: one settings source they both read. Introducing
that shared source is a larger change than it looks; if it is out of scope, stop
at rung 6 and record which two places must change together.

## The schema boundary

A database constraint cannot consult application code, and often cannot consult
another table either: a check constraint takes no subquery, so a vocabulary
enforced by a check cannot be stored as rows that the check reads. Turning it into
rows means a foreign key and a different way of enforcing integrity, which is a
schema decision, not a refactor.

Available: keep the schema authoritative and derive in the application at start
time (rung 3) or request time (rung 4). A deployed migration is immutable in most
projects, so a new migration is the only way to change the home at all. That
usually puts schema changes outside the scope of a duplication fix. Confirm the
project's own migration and approval rules before proposing one.

## Make disagreement fail

When rungs 1 to 4 are unavailable, a check is what remains. A check is only
worth having if it would actually fail.

- **It must read both homes.** A check that states the expected values is a third
  home and will drift alongside the second. Compare home to home.
- **It must run in the suite that always runs.** A check behind an environment
  variable, a manual command or an optional job protects nothing by default. If
  the project keeps such tests deliberately opt-in, say that the concept is
  unprotected in the gate rather than implying it is covered.
- **It must fail for the right reason.** Confirm it fails when the homes disagree,
  not merely that it passes today. Introduce the disagreement, watch the check
  fail, then undo the disagreement. Until you have seen a check fail, you have
  no evidence that it checks anything.
- **Prefer a mechanism over a test.** Exhaustiveness the compiler proves, a
  constraint the database enforces, or a start-time refusal all run without anyone
  remembering to look.

A check you keep is a check you must maintain. It usually breaks because it
encodes the structure it checks rather than reading it. [Checks that survive
restructuring](durable-checks.md) sets out the requirements that prevent this.

Where a check is impossible too, rung 6 is what remains: state the duplication
where the concept lives, name every place that must change together, and say what
goes wrong when one is missed. A recorded duplication is a known risk. An
unrecorded one becomes a surprise when a later change updates only one of those
places.
