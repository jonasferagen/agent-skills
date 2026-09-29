---
name: concept-homes
description: "Decide which medium owns a concept and keep every other appearance of it derived or loudly checked. Use when one value, list, rule, pattern or shape appears in more than one place — across languages, schema, configuration, build files, tests or documentation — when adding a case to a vocabulary means editing several files, or when deciding where a new constant, type or rule belongs. Use it also when writing or reviewing the check that makes disagreement fail, or when a check keeps breaking because a directory moved, a count changed or a tool was absent rather than because anything is actually wrong."
metadata:
  version: "1.1.0"
---

# Concept homes

One concept, one home that decides it. Every other appearance is derived from
that home, or something fails when the two disagree.

Reach for this when a value, list, rule, pattern or shape appears in more than
one place, when adding a case to a vocabulary means editing several files, or
when deciding where a new constant, type or rule belongs. It covers the seam
between media — schema and application code, configuration and the code that
reads it, one language and another, code and the documents that describe it.
That seam is where a restatement is hardest to see and most likely to drift,
because no single search finds both sides of it.

Start from the project's own owning guides: they may already name the home for a
concept, and an explicit project convention takes precedence over this guidance.
Adopting this skill does not call for renaming anything, moving existing code or
changing a schema. Examples below are synthetic.

## Start by symptom

| Symptom or decision | Read |
| --- | --- |
| The same list, pattern or value appears twice | [Find the homes](#find-the-homes), then [Choose the home that decides](#choose-the-home-that-decides) |
| Adding a case to a vocabulary means editing several files | [Derive instead of restate](#derive-instead-of-restate) |
| A restatement sits in another language, a bundle, a schema or a document | [Boundaries that forbid derivation](references/boundaries.md) |
| Two appearances look alike and may mean different things | [What is not a second home](#what-is-not-a-second-home) |
| A missing case produces plausible output instead of an error | [Beware the fallback](#beware-the-fallback) |
| A restatement can be neither derived nor removed | [Make disagreement fail](references/boundaries.md#make-disagreement-fail) |
| You are writing the check that fails when two homes disagree | [Keep the check durable](#keep-the-check-durable) |
| A check keeps breaking when the structure moves, or when a tool is absent | [Checks that survive restructuring](references/durable-checks.md) |
| Deciding how much a given duplication is worth | [Rank by how it fails](#rank-by-how-it-fails) |

## Name the concept

State what the concept is in one sentence, as a question the system answers:
which capacities a participant may hold, what shape an identifier has, which
address the paired service listens on. If the sentence needs an "and", you are
probably holding two concepts. Split them and start again.

The sentence decides what counts as an appearance. Named after its container
("the list in that module") a concept hides its other homes. Named as a question,
its appearances are whatever answers it — in any language, in the schema, in a
build file, in prose.

## Find the homes

Search for the concept, not for the text. The same rule is usually spelled
differently in each place it lives, which is why one search understates the
problem.

- Search each value in the set, not the set. A vocabulary restated in another
  language will not match the original's quoting or separators.
- Search the transformed form. A code stored as `two_words` may appear elsewhere
  as `two words`, as `twoWords`, or as a display string.
- Search the schema, configuration, build files, tests and prose, not only the
  application source. A document that lists a vocabulary is a home: readers act
  on what it says.
- Read the history of the appearance you believe is authoritative. A vocabulary
  extended once will be extended again, and the commit that extended it shows
  whether the other homes moved with it.

That last check turns an argument into evidence. If an earlier extension touched
only one home, the drift is not hypothetical — it already shipped, and the
current state of the other homes tells you how long it went unnoticed.

## Choose the home that decides

Among the appearances, exactly one decides the answer: change it and the system
behaves differently; change any other and you have changed a copy. That one is
authoritative.

It is usually whichever appearance the strictest mechanism enforces — the
constraint that rejects the write, the schema that produces the column, the
setting the process actually reads, the generated artifact that ships. Code that
filters on a vocabulary is downstream of whatever admits values into it. A
document describing the vocabulary is downstream of both.

Validating more strictly than the home is its own defect. A check that refuses
input the home would accept cannot protect anything; it can only reject a value
the system already stores. Where a boundary deliberately narrows what it accepts,
that narrowing is a policy and needs its own stated reason — see
[what is not a second home](#what-is-not-a-second-home).

Do not choose a home for convenience. If the convenient home is not the deciding
one, the result is two homes plus a habit of editing the wrong one.

## Derive instead of restate

Work down this list and stop at the first rung that holds.

1. **Remove the restatement.** The consumer reads the concept from its home.
   Available whenever home and consumer share a medium and a dependency
   direction.
2. **Derive it at build time.** Generate the restatement from the home, so a
   shipped artifact cannot disagree with it.
3. **Derive it at start time.** Read the home as the process starts and refuse to
   start when the answer is not what the code expects.
4. **Derive it at request time.** Send the concept with the data that depends on
   it, so a consumer that cannot import the home still receives it.
5. **Check it in the gate.** Keep the restatement and add a check, to whichever
   suite always runs, that fails when the two homes disagree. The check is now
   something you maintain; [keep the check durable](#keep-the-check-durable) is
   its bar.
6. **Record it.** The duplication is structural. Say so where the concept lives,
   and name what must be edited together.

Rungs 1 to 4 make disagreement impossible. Rung 5 makes it loud. Rung 6 only
makes it known, and is the answer only when a boundary genuinely forbids the
rungs above it. [Boundaries](references/boundaries.md) covers which boundaries do
that and what each one leaves available.

## Keep the check durable

Rung 5 leaves a check behind, and a check has a failure mode of its own: it can
encode the very structure it is checking. Hold it to one bar — it protects a
named consequence proportionately, computes its answer live rather than comparing
against a committed golden, reads each structural fact from the home that declares
it, anchors to its own location, fabricates its own fixtures, and fails only when
the homes disagree. A check built that way survives the next restructure
untouched.

What the bar closes is a check that hard-codes an inventory: a directory set, a
member list, an expected count, a failure when some tool is absent — written as a
literal instead of derived from whatever already declares it. The literal is
invisible until the structure moves. Then the check fails on the shape of the
environment rather than on a disagreement between homes, and the only remedy is
to patch the literal and re-bless the baseline. A check that must be re-blessed
teaches reviewers to approve diffs they never read.

| Ask of the check | If yes |
| --- | --- |
| Is the consequence it protects anything less than concrete? | do not add the check until that answer is concrete |
| Is there cheaper evidence that observes the same consequence? | use that evidence instead |
| Can it fire for a change that cannot affect that consequence? | narrow the trigger, or say why the proxy costs less than a missed defect |
| Does it hold a name, a list or a count that also lives in the home? | read the home instead: that is rung 1 applied to the check |
| Would it break if a directory moved, or if an optional component were absent? | anchor it to its own location and give it fabricated fixtures |
| Does it fail when a tool or service is missing, rather than when the homes disagree? | move the failure to the boundary that owes the tool, or skip loudly where nobody owes it |
| Is it report-only, with nothing consuming its output? | it is cost without teeth: give it a live invariant and a real gate, or drop it |

[Checks that survive restructuring](references/durable-checks.md) states each
property with the shape that breaks it and the shape that holds. Read it while
writing the check, not after the gate has gone red. Whether a check is worth its
recurring cost at all is the project's own policy; this bar keeps a check you
have decided to keep from rotting.

## Beware the fallback

A restatement drifts silently when the consumer has somewhere to go for an answer
it does not have. A lookup with a default, a filter that simply fails to match, a
branch with a catch-all: each turns a missing entry into plausible output instead
of a failure.

    // A value the map does not know renders as empty, with no error anywhere.
    const label = labels[code] ?? '';

Silent drift is nearly always a fallback. Where the concept must be complete,
make the consumer total over it: no default, no catch-all, and an explicit
failure for an answer it does not recognise. A compiler that proves
exhaustiveness is the cheapest possible version of rung 5, and it runs on every
build without a test.

Worse than a missing label is a wrong one. A consumer that ignores the stored
value and states a fixed answer will keep stating it after the value changes, and
a reader cannot tell it is false. Prefer a vague answer derived from the home over
a specific answer invented beside it.

A fallback is right when the concept is genuinely open — free text, or an
extensible set the consumer is not required to understand. Say which it is, so a
later reader does not mistake deliberate tolerance for an oversight.

## What is not a second home

Rejecting a false match matters as much as finding a real one. None of these is a
second home.

- **A deliberate subset, or a policy over the concept.** A list naming which
  members of a vocabulary get some treatment is a different concept: a policy
  about the vocabulary, not a copy of it. The test is completeness — a list
  holding every value is tracking the vocabulary and will fall behind it; a list
  holding some values is making a choice. Establish which you have before
  proposing anything.
- **A test that states a literal.** A test restating the expected value is doing
  its job. A test that derives its expectation from the code under test proves
  nothing.
- **Two things sharing a shape.** Two sets of ports, two identifier patterns, two
  lists of hosts may answer different questions. Compare the questions, not the
  contents.
- **Repetition inside one home.** Several uses of one constant in one module is
  not duplication.

Where unification would create a worse coupling than the duplication — pulling a
server module into a client bundle, making a schema depend on application code,
forcing a test to import the thing it exists to check — the duplication stays.
Move to rung 5 or 6 and say which coupling you refused.

## Rank by how it fails

Effort follows the failure, not the number of copies.

- **How does disagreement present?** Silent wrong output is worst. A stated fact
  that becomes false is worse than a missing one, because a reader cannot tell. A
  crash, a rejected write or a failed build is comparatively cheap.
- **Can one search find every home?** Homes in different languages or media
  cannot be found together, so they drift further before anyone looks.
- **Does the concept grow?** A vocabulary already extended once will be extended
  again. A value fixed for the system's lifetime is a small risk however many
  copies it has.
- **Is the restatement complete?** A complete copy is meant to track the home and
  will fall behind. A partial one may be a policy.

One silent, cross-medium, growing concept deserves more attention than twenty
copies of a stable constant.

## Review and verification

- Name the concept, its authoritative home, and the rung you stopped at.
- Show that drift was possible before and is not now: the check that fails when
  the homes disagree, the restatement that no longer exists, or the history of an
  extension that missed a home.
- Where you stopped at rung 5 or 6, name the boundary that forbade the rungs
  above, and what remains unprotected.
- Where you left a check behind, say what it reads at run time on each side, and
  have its verdict name the root and the set it measured.
- Reconcile the documents that state the concept, in the present tense, and leave
  the deciding home named in the guide that owns it.
- Run the project's own checks. A check added to the gate belongs in the same
  change, not in a follow-up.
