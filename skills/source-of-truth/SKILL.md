---
name: source-of-truth
description: "Choose the authoritative place for a concept, then derive its other appearances from that source or make disagreement fail a check. Use when a value, list, rule, pattern or shape appears in several places across languages, schemas, configuration, build files, tests or documentation; when adding a vocabulary member requires several edits; or when deciding where a constant, type or rule belongs. Also use when writing or reviewing checks for disagreement, or when a check fails because a directory moved, a count changed or a tool is absent even though the concept is still consistent."
metadata:
  version: "1.2.1"
---

# Authoritative definitions

Give each concept one authoritative home: the place that decides its value or
rule. Derive every other appearance from that home, or make a check fail when the
two disagree.

Use this guidance when a value, list, rule, pattern or shape appears in several
places, when adding a vocabulary member requires edits to several files, or when
deciding where a new constant, type or rule belongs. A vocabulary is a set of
allowed values. A restatement is a separate definition of the same concept.

The guidance covers concepts shared across schemas and application code,
configuration and the code that reads it, different languages, and code and its
documentation. Restatements across these media are especially hard to find and
likely to drift, because no single search finds both sides.

Start with the project's guides for the area you are working in. They may already
name a concept's home, and an explicit project convention takes precedence over
this guidance. Adopting this skill does not call for renaming anything, moving
existing code or changing a schema. Examples below are synthetic.

Use the project's policy to judge the consequence of disagreement and the
evidence worth maintaining. A policy change can alter that consequence: revisit
affected copies and checks, and record unmet requirements in the active queue.
Keep project policy authoritative for requirements and implementation owners
authoritative for observed behavior; one cannot prove the other. A prototype
label does not by itself waive an existing guarantee. This guidance works without
a separate policy skill; missing policy facts remain explicit unknowns.

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

Name the concept with one question the system answers. For example: which
capacities may a participant hold? What shape does an identifier have? Which
address does the paired service listen on? If the question needs an "and", it
probably combines two concepts. Split them and start again.

The question determines what counts as an appearance of the concept. A name such
as "the list in that module" hides other places that answer the same question.
Look for every answer, whether it appears in a programming language, a schema, a
build file or prose.

## Find the homes

Search for each way the concept is expressed. The same rule is usually written
differently in each place, so a search for one exact form misses other
appearances.

- Search for each value in the set. A vocabulary restated in another
  language will not match the original's quoting or separators.
- Search the transformed form. A code stored as `two_words` may appear elsewhere
  as `two words`, as `twoWords`, or as a display string.
- Search the schema, configuration, build files, tests and prose, not only the
  application source. A document that lists a vocabulary is a home: readers act
  on what it says.
- Read the history of the appearance you believe is authoritative. A vocabulary
  extended once will be extended again. The commit that extended it shows whether
  the other homes were updated too.

History provides evidence of drift. If an earlier extension changed only one
home, the drift already shipped. The current state of the other homes tells you
how long it went unnoticed.

## Choose the home that decides

Identify the one appearance that decides the answer. Changing it changes the
system's behavior; changing any other appearance changes a copy. The deciding
appearance is authoritative.

It is usually the appearance enforced by the strictest mechanism: the
constraint that rejects the write, the schema that produces the column, the
setting the process actually reads, the generated artifact that ships. Code that
filters on a vocabulary is downstream of whatever admits values into it. A
document describing the vocabulary is downstream of both.

Validation that is stricter than the home is also a defect. A check that refuses
input the home would accept cannot protect the concept; it can only reject a
value the system already stores. If a boundary deliberately narrows what it
accepts, that narrowing is a policy and needs its own stated reason. See
[what is not a second home](#what-is-not-a-second-home).

Do not choose a home for convenience. Choosing a copy as the home leaves both
definitions in place and encourages people to edit the copy.

## Derive instead of restate

Work down these options in order and stop at the first one that is possible.
The rest of this skill refers to these numbered options as rungs.

1. **Remove the restatement.** The consumer reads the concept from its home.
   This is available whenever the home and consumer share a medium and the
   dependency direction allows the consumer to read the home.
2. **Derive it at build time.** Generate the restatement from the home, so a
   shipped artifact cannot disagree with it.
3. **Derive it at start time.** Read the home as the process starts and refuse to
   start when the answer is not what the code expects.
4. **Derive it at request time.** Send the concept with the data that depends on
   it, so a consumer that cannot import the home still receives it.
5. **Check it in the gate.** Keep the restatement and add a check that fails when
   the two homes disagree. Put it in the gate: the suite that always runs. You
   must now maintain the check; apply the requirements in
   [keep the check durable](#keep-the-check-durable).
6. **Record it.** The duplication is structural. Say so where the concept lives,
   and name what must be edited together.

Rungs 1 to 4 make disagreement impossible. Rung 5 makes it fail a check. Rung 6
only records the risk; use it only when a boundary genuinely prevents every
higher option. [Boundaries](references/boundaries.md) explains those boundaries
and the options each leaves available.

## Keep the check durable

The check added at rung 5 can itself become a restatement if it hard-codes the
structure it checks. A durable check must:

- Protect a named consequence at a cost proportionate to that consequence.
- Compute its answer when it runs, instead of comparing with a committed
  baseline, or "golden", that copies structural facts.
- Read each structural fact from the home that declares it.
- Resolve its location from its own file or module.
- Use tests that create their own fixtures.
- Fail only when the homes disagree.

A check built this way survives the next restructure without changes.

Hard-coded directory sets, member lists and expected counts copy facts that
already have a home. Failures caused by an absent tool can create the same
problem: the check fails because the environment changed, even though the homes
still agree. Updating the copied literal and approving a new baseline then
becomes routine. That routine teaches reviewers to approve diffs they have not
read.

<!-- Package-boundary copy: test-audit/references/triage.md applies the report-only rule below to scanner drift stamps. Keep both passages aligned. -->
| Ask of the check | If yes |
| --- | --- |
| Is it missing a concrete consequence to protect? | do not add the check until you can name that consequence concretely |
| Is there cheaper evidence that observes the same consequence? | use that evidence instead |
| Can it fail for a change that cannot affect that consequence? | narrow the trigger, or explain why using that change as a proxy costs less than a missed defect |
| Does it hold a name, a list or a count that also lives in the home? | read the home instead: that is rung 1 applied to the check |
| Would it break if a directory moved, or if an optional component were absent? | resolve paths from its own location and make its tests create their fixtures |
| Does it fail when a tool or service is missing, rather than when the homes disagree? | fail at the boundary where the environment contract requires that dependency; if no contract requires it, skip with a prominent notice |
| Does it only produce a report, with nothing consuming that report? | make it check an invariant using current facts and fail a real gate, or remove it |

[Checks that survive restructuring](references/durable-checks.md) explains each
property with examples of checks that violate and satisfy it. Read it while
writing the check. The project's own policy decides whether a check is worth its
recurring cost; these requirements keep a retained check working as the project
changes.

## Beware the fallback

A restatement drifts silently when the consumer supplies a fallback for an
answer it does not know. A lookup with a default, a filter that simply fails to
match, or a branch with a catch-all turns a missing entry into plausible output
instead of a failure.

    // A value the map does not know renders as empty, with no error anywhere.
    const label = labels[code] ?? '';

Silent drift is nearly always caused by a fallback. Where the concept must be
complete, make the consumer handle every allowed value: no default, no catch-all,
and an explicit failure for an answer it does not recognise. A compiler that
proves exhaustiveness is the cheapest possible version of rung 5, and it runs on
every build without a test.

Worse than a missing label is a wrong one. A consumer that ignores the stored
value and states a fixed answer will keep stating it after the value changes, and
a reader cannot tell it is false. Prefer a vague answer derived from the home over
a specific answer invented beside it.

A fallback is right when the concept is genuinely open: free text, or an
extensible set the consumer is not required to understand. State which case
applies, so a later reader can see that the tolerance is deliberate.

## What is not a second home

Before treating similar definitions as competing homes, check these exceptions:

- **A deliberate subset, or a policy over the concept.** A list naming which
  members of a vocabulary get some treatment is a different concept: a policy
  about the vocabulary. Check whether the list is complete: a list holding every
  value tracks the vocabulary and will fall behind it; a list holding some values
  makes a choice. Establish which you have before proposing anything.
- **A test that states a literal.** A test restating the expected value is doing
  its job. A test that derives its expectation from the code under test proves
  nothing.
- **Two things sharing a shape.** Two sets of ports, two identifier patterns or
  two lists of hosts may answer different questions. Compare the questions they
  answer to decide whether they represent the same concept.
- **Repetition inside one home.** Several uses of one constant in one module is
  not duplication.

Keep the duplication if unifying it would create a dependency that costs more
than the duplication: pulling a server module into a client bundle, making a
schema depend on application code, or forcing a test to import the thing it
exists to check. Move to rung 5 or 6 and state which dependency you avoided.

## Rank by how it fails

Set the effort according to the consequences of disagreement.

- **How does disagreement appear?** Silent wrong output is worst. A stated fact
  that becomes false is worse than a missing one, because a reader cannot tell. A
  crash, a rejected write or a failed build is comparatively cheap.
- **Can one search find every home?** A single search cannot find homes in
  different languages or media, so they drift further before anyone looks.
- **Does the concept grow?** A vocabulary already extended once will be extended
  again. A value fixed for the system's lifetime is a small risk however many
  copies it has.
- **Is the restatement complete?** A complete copy is meant to track the home and
  will fall behind. A partial one may be a policy.

One growing concept copied across media, whose copies can disagree silently,
deserves more attention than twenty copies of a stable constant.

## Review and verification

- Name the concept, its authoritative home, and the rung you stopped at.
- Show evidence of the drift risk and how the chosen option addresses it: a
  removed restatement, derivation from the authoritative home, a required check
  that fails on disagreement, or a record of structural duplication and what
  must be edited together. An earlier extension that missed a copy is evidence
  of the risk; it does not prove that the risk has been removed.
- If you stopped at rung 5 or 6, name the boundary that prevented the higher
  rungs and state what remains unprotected.
- If you added or retained a check, state what it reads on each side when it
  runs. Its verdict must name the root and the set it measured.
- Update the documents that state the concept to agree with its current
  definition. Use the present tense and name the authoritative home in the guide
  responsible for that concept.
- Run the project's own checks. Include any new gate check in the same change.
