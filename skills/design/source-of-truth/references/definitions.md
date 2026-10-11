# Choosing an authoritative definition

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

## Decide which prose claims to keep

Before consolidating a changing claim, ask whether the reader needs it. Omit
incidental status from maintained prose rather than maintaining a more accurate
copy. An overview may need to explain how to find releases without saying
whether a release exists. If the answer matters, link the existing authoritative
release, catalog or tracking owner with enough context for the reader to use it.
Do not create an inventory or another document for every removed statement.

Keep a limitation, uncertainty or qualification where readers need it to
understand the current behavior or contract. A required guarantee and observed
support answer different questions; neither can replace the other. A dated
record retains what was observed at its assessed revision, even after the current
answer changes.

For a prose home that needs manual maintenance, name the responsible owner, its
scope and what changes trigger an update. Keep the maintained set small enough
for that responsibility to be practical. Other documents explain their own
subject and point to the home instead of keeping independent status, inventories
or ownership summaries. A reference across a repository boundary should reach
the owner of the answer, not a chain of summaries restating it.

## Choose the home that decides

Identify the one appearance that decides the answer. Changing it changes the
system's behavior; changing any other appearance changes a copy. The deciding
appearance is authoritative.

It is usually the appearance enforced by the strictest mechanism: the
constraint that rejects the write, the schema that produces the column, the
setting the process actually reads, the generated artifact that ships. Code that
filters on a vocabulary is downstream of whatever admits values into it. A
document describing the vocabulary is downstream of both.

For a shared setting or external identifier, follow
[one owner for a shared value](authoritative-values.md). It covers existing
configuration owners, lookup declarations, explicit inputs and historical values.

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
   [keep the check durable](check-design.md#keep-the-check-durable).
6. **Record it.** The duplication is structural. Say so where the concept lives,
   and name what must be edited together.

Rungs 1 to 4 make disagreement impossible. Rung 5 makes it fail a check. Rung 6
only records the risk; use it only when a boundary genuinely prevents every
higher option. [Boundaries](boundaries.md) explains those boundaries
and the options each leaves available.

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
