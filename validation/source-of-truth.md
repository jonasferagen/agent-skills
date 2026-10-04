# Validation and alignment — Source of Truth

## Behavioral scenarios

These describe expected outcomes. They are author-reviewed scenarios, not claims
of an independent agent evaluation.

| Request and context | Expected outcome |
| --- | --- |
| A vocabulary is enforced by a database constraint and restated in application code | The constraint is authoritative; the application derives the vocabulary or a gate check compares the two. |
| A list in code holds every value the constraint admits | Treated as a copy that will fall behind, not as a policy. |
| A list in code holds some of the values the constraint admits | Treated as a policy over the vocabulary; left in place with its reason stated. |
| An input boundary validates more strictly than the column that stores the value | The stricter check is identified as able only to reject stored values; narrowing needs its own stated reason. |
| A lookup returns a default for an unknown code | Named as the mechanism that makes drift silent; exhaustiveness or explicit failure proposed where the concept must be complete. |
| A consumer states a fixed label and ignores the stored value | Treated as worse than a missing label, because the stated fact becomes false; a derived vague answer preferred. |
| The same rule exists in two languages with different spellings | Copying rejected; the spelling difference is attributed to each language's parsing, and a normalising home-to-home check is proposed. |
| A proposed fix would import a server module into a client bundle | Unification refused; request-time delivery or a dependency-free shared module proposed instead. |
| Only a type is shared across a bundle boundary | Type-only declarations are erased, so the boundary does not block it. |
| Paired processes each hardcode the other's address | The hardcoded value is removed from shared code and supplied at the edge by whichever process owns it. |
| Neither paired process can know the other's value, and a shared settings source is out of scope | Where both settings are in the repository, a check reads both and fails when they disagree (rung 5); otherwise the pair is recorded at rung 6. |
| A vocabulary would need to become rows a check constraint reads | Identified as impossible for a check constraint and as a schema decision; the project's migration rules govern. |
| A test restates the expected values as the check | Rejected as a third home; the check must compare one home to the other. |
| A relevant test exists but runs only behind an environment variable | Reported as unprotected in the gate rather than as covered. |
| A proposed check has never been observed to fail | Disagreement is introduced deliberately to confirm the check fails, then reverted. |
| Two similar lists answer different questions | Not a second home; the questions are compared rather than the contents. |
| One constant is used several times inside one module | Not a duplication. |
| A document and a constraint both list a vocabulary and the document is stale | The document is a home; it is reconciled in the present tense. |
| A plugin namespace appears in docs, a generated manifest and UI prompts | One project-owned lookup value decides the namespace; docs use its key, generated files derive the literal, and historical pins retain their original names. |
| A manifest needs a literal namespace but its loader does not expand variables | A placeholder is rejected; generate the literal or compare it with the owner in a required check. |
| A duplication can be neither derived nor checked | Recorded where the concept lives, naming what must change together and what goes wrong when one is missed. |
| Ranking a stable constant copied many times against one growing cross-medium vocabulary | The growing cross-medium concept ranks higher; copy count alone does not decide. |
| A gate check compares a freshly scanned count against a committed expected one | Named as a golden that has to be re-blessed on every legitimate change; the check computes its answer live instead. |
| A home cannot be read when the check runs | No committed copy of its answer is added; the dependency is reported as absent, or the duplication is recorded at rung 6. |
| A unit test states the value an operation should produce | Not a golden; a literal expectation about behaviour is the test doing its job. |
| An exemption ledger lists files grandfathered out of a settled convention | Accepted as a bounded exception where it gates hard, may only shrink, and belongs to the tree whose files it lists. |
| A check derives its file inventory with `git ls-files` from the caller's working directory | Flagged; the repository root is resolved first and the verdict names the root and set it measured. |
| A check reports a pass without stating what it measured | Treated as a partial denominator that can read as a whole-tree result; the verdict names its basis. |
| A check's own test builds fixtures at a hard-coded path outside its tree | Rejected; it anchors to its own location and fabricates its world in a temporary directory. |
| A check copies a directory list the build configuration already declares | Rung 1 applied to the check: it reads the declaration rather than restating it. |
| A check's test requires a neighbouring checkout or a running service | Rejected as a dependency on environment shape; external commands are stubbed and the tree fabricated. |
| A check throws, or asserts against empty output, when a required tool is absent | The failure moves to the boundary that owes the tool, naming what is missing. |
| A dependency nobody opted into is unavailable | The check exits successfully with a loud notice; a silent skip is rejected because it reads as a pass. |
| A check is report-only, with nothing consuming its output | Named as cost without teeth; it gains a live invariant and a real gate, or it goes. |
| A check can fire for changes that cannot affect the consequence it protects | The trigger is narrowed, or the proxy's cost is stated against the cost of a missed defect. |
| Mechanical enforcement is proposed as a scanner over a fixed set of directories | Rejected as the anti-pattern enforcing itself; enforcement is scoped to the tree it checks and derives its file set from version control. |
| Whether a given check earns its recurring cost | Deferred to the reading project's own policy; the durability bar applies to a check already being kept. |
| Adopting the skill into an existing project | No renaming, code movement or schema change is implied; existing project conventions take precedence. |
| A changed policy raises the consequence of inconsistent copies | Revisit affected copies and checks, link unmet requirements to active work, and keep desired requirements distinct from observed behavior. |
| A project has no policy skill installed | Use available project decisions and expose consequential unknowns; do not require installing another skill. |

## Sources inspected

Derived from an audit of Personal Atlas at
`a70229a79009ae6bce9fde56f26c5db6b30bc183`, comparing application source,
migrations, tests, build configuration and documentation. The audit ran as six
parallel searches — validation rules, domain vocabularies, logic expressed in
more than one medium, configuration constants, types and shapes, and
documentation — with each candidate independently challenged before being
accepted. Twenty-seven duplications survived that challenge; several claims were
corrected or rejected by it, and those corrections are the source of the
false-positive guidance above.

The distinction between a complete copy and a deliberate subset, the observation
that silent drift is nearly always a fallback, the objection that a test stating
its expectations is a third home rather than a check, and the point that an
opt-in test does not constitute gate coverage all came from that challenge step
rather than from the initial findings.

The durable-check material was imported on 2026-09-29 from the owner's Forge
Agent Kit `selfcheck-guard` skill at
`c98147a115a30f36b952df5faf1c869b54480c59` (2026-09-18), as its manifest and the
`five-properties` reference. It is folded in rather than kept as a ninth skill
because this one already ends at a check — rung 5, and the rules for making
disagreement fail — and stopped without saying what keeps that check from rotting
when the structure moves.

Citations of the Forge Project Policy were redirected, because that policy opens
by stating nothing is in production while both consuming projects are. Two
carried substance now stated in place: that a check protects a named consequence
with the least costly evidence able to observe it, and that a check fails at the
boundary owing a missing precondition rather than on the surface that merely
depends on it. Whether a check earns its recurring cost defers to the reading
project's own policy. References to sibling Agent Kit skills were dropped rather
than described: the remedy-order question they handed off — change the shape
before adding a guard — is already answered here by the rung ladder, and a
cross-package path would break when this skill is installed alone. Upstream's
repository-set framing, in which a check breaks on whether a sibling repository
is checked out, was generalised to any tree, directory or optional component,
since the seam this skill addresses sits inside one project as often as between
several.

## Extraction decisions

Retained the diagnostic sequence — name the concept as a question, find its
appearances across media, identify the appearance that decides, then derive,
check or record — together with the escalation rungs, the boundary analysis, the
fallback mechanism and the false-positive tests.

Removed every project-specific instance: schema, table, column, role, port and
project identifiers, the domain vocabularies themselves, and the source project's
migration approval, backup and merge policy. Those remain in their owning
documentation. The package names no language, framework, database or toolchain as
a requirement, and no scenario depends on the source project's structure.

The five durability properties are deliberately split. The bar's six
requirements and the seven questions that apply it sit in the manifest, at the
rung where a reader decides to keep a check, so the check can be judged without
opening a reference; each property's rule, the shape that breaks it and the
shape that holds are in `references/durable-checks.md`. They are not appended to
`references/boundaries.md`, whose subject is the boundaries that forbid
derivation — a check's durability is not one of them, and mixing the two would
give that page a second subject. What a check must compare and where it must run
stays in that page's make-disagreement-fail section; the new page cites it
rather than restating it.

This skill deliberately does not cover code shape, naming or module layout, which
belong to a TypeScript or language-specific canon, nor schema design, which
belongs to a database canon. Its subject is only the seam between media and what
keeps a restatement honest across it.

## Verification limits

The author reviewed the extracted instructions against the scenarios above and
against the audit findings and their challenges. No independent agent evaluation
was performed. The skill has been applied in one project only; it needs
experience in a second before its scope boundaries can be considered settled. In
particular, the rung list has not been exercised on a build-time generation case
(rung 2), and the language-boundary guidance rests on a single observed instance.

The durability material adds its own limits. It has not been applied to a real
check in either consuming project; upstream's examples came from a third
project's tooling and were read, not reproduced. No check has been observed here
failing on environment shape and then surviving the same move after the bar was
applied, so the claim that a check built this way survives restructuring
untouched rests on upstream experience rather than on evidence gathered in this
repository. The rule that a verdict names the root and set it measured has not
been exercised against a case where the inventory basis was actually wrong. The
reconciliation between a literal test expectation and a committed golden is new
in this fold and has not been reviewed by anyone who had already absorbed the
false-positive list, which is where a reader is most likely to mistake one for
the other. The proportionality questions — the consequence a check protects, and
whether it can fire for changes that cannot affect it — are adapted from a policy
this repository does not carry, and no consuming project has yet judged a check
against them.

## Project foundations update — 2026-09-30

Version 1.2.0 uses the display name “Authoritative definitions” and makes project
policy relevant to the consequences of inconsistent copies and the evidence
required. Installation path unchanged. Author review covered changed requirements,
standalone use, and preservation of existing guarantees. Package validation and
the skill-creator manifest check passed. No new live consistency check or separate
behavioral trial was executed for this update.

## Clear writing pass — 2026-09-30

Version 1.2.1 revises `boundaries.md` and `durable-checks.md`; the entrypoint
was revised in the earlier Clear Writing trial and is unchanged. See the
[package sweep](clear-writing.md#package-sweep--2026-09-30). "Re-bless" became
"update and re-approve", "false green" became "false pass", and relative
references such as "the rungs above" now name rungs checked against the
entrypoint. The shrink-only ledger still states the same rule as its copy in
`test-audit`. Review found the meaning preserved; four wording corrections
followed. No live check or behavioral trial was run.

Left unresolved: `durable-checks.md` says to compute the answer "if the correct
answer can be computed when the check runs", while the entrypoint requires a
durable check to compute its answer without that condition. The README counts
seven questions in the bar; the extraction notes above count six.

## Diagrams and tables pass — 2026-09-30

No change; see the [package
pass](diagrams-and-tables.md#package-pass--2026-09-30). Both tables are
complete; the rung list stays an ordered list. Newly found: `boundaries.md` says
each boundary leaves a different set of rungs available, but most options do not
name their rung, so a boundary-by-rung matrix cannot be filled. The manifest's
bar lists six requirements, while the README counts seven questions and the
extraction notes above count six.

## Resolutions — 2026-09-30

The owner accepted each proposal from the contradiction research, including
rung 3 for the two options whose rung was open. Version 1.3.0 carries these
changes.

- Computing live: `durable-checks.md` computed the answer "if" it could be
  computed, while the entrypoint required it unconditionally → both require it;
  if a home cannot be read, the dependency is reported as absent or the
  duplication recorded at rung 6. A scenario above covers that case.
- The bar's count: the extraction notes said six questions and the README seven
  → the bar has six requirements and the table seven questions, because the fold
  split upstream's first question in two. The extraction notes and one README
  sentence now say so, and the entrypoint says the reference page states
  requirements two to six as its five properties.
- Boundary rungs: `boundaries.md` said each boundary leaves different rungs but
  named few → every option now names its rung. A data file both languages read
  and a settings source both processes read are rung 3, read as they start
  (owner decision; either could be read as rung 1).
- Process boundary: an out-of-scope shared settings source went straight to
  rung 6, although rung 6 is only for when every higher rung is blocked → a
  rung 5 check that reads both settings comes first where both are in the
  repository. A scenario above covers it.

## Discovery routing — 2026-09-30

The description was shortened and conditional entrypoint guidance moved to references. See [the discovery review](discovery.md) for the measured sizes, scope and verification. Earlier behavioral results do not establish the new discovery behavior.

## External identifier lookup — 2026-09-30

Version 1.4.0 adds a conditional rule for project-chosen external identifiers
repeated across documentation and machine-readable files. The plugin namespace of
the grouped layout on the skill-discovery branch prompted it; main has no plugin
build. The rule uses the existing rungs: derive copies where possible, then
require a check where a consumer must keep a literal. It does not require a new
table when configuration already owns the value, or rewrite historical pins. The
cases above were reviewed against that branch's generated plugin build, not
against anything on main; no independent discovery trial was run.

## Candidate: record meaning versus storage origin

Proposed on 2 October 2026, from a pattern-capture review in the intake-spike
project. Proposed home: [Authoritative definitions](../skills/design/source-of-truth/SKILL.md).

**The point.** When code decides what a record means from where it came from,
such as its table, file or assertion kind, moving that kind of record to another
home changes the code's behavior without any error. Giving each fact one home is
exactly such a move, so check consumers for this before the move.

**Mechanism.** A consumer branches on provenance to decide meaning. That works
only while each kind of record lives in one store, so consolidating the stores
breaks it silently. A catch-all branch makes it worse: in the case below, any key
that is not one of the project's own assertions counts as an identity, which is
the silent fallback that [definitions](../skills/design/source-of-truth/references/definitions.md)
already warns about.

**Evidence.** The intake project's lookup calls an address match an alias when
its key came from intake's own assertions and an identity otherwise, and only an
identity leads to task candidates. On the project's made-up test data, the same
sender fact stored as a source-system row gave the identity rule and two task
candidates. Stored as one of intake's own assertions, it gave the alias rule and
none. The planned consolidation would have renamed 21 matches in the project's
corpus, and no existing check would have failed. One reproduced case; no second
case yet.

**Where it applies.** Records that carry provenance, such as an origin, a source
system or an assertion kind, read by code that uses it to decide what the record
is. It matters most before moving a kind of record to another home.

**Where it does not.** Provenance can itself be the meaning. A review status that
decides whether a value needs review, or a trust level that decides whether
evidence may resolve something, is a correct branch on provenance and should
stay.

**Simplest rule.** Store the kind of record as data and branch on that. Keep
provenance for reporting and for decisions about trust. Before moving a concept's
home, search its consumers for branches on origin, source or assertion fields.

**Validation still needed.**

- Reproduce the mechanism in an unrelated case, such as configuration that
  behaves differently depending on whether a value came from a file or from the
  environment.
- Check a case outside the rule, such as branching on review status, and confirm
  that the guidance does not discourage it.
- Then choose between a short addition to the definitions reference, beside the
  passage on silent fallbacks, and one line in the skill's review list.

This concerns consumers of a definition, not consistency checks. It stays with
source-of-truth even if consistency-check design moves out, as
[Decisions](../DECISIONS.md) proposes.

Preserved from `ideas.md` on 2 October 2026. The intake observations above are
the recorded evidence from that review; this pass did not reproduce them or run
the outstanding trials. No new reusable rule has been adopted.


## Standalone source after framework extraction — 4 October 2026

Version `3.0.0` is owned at `skills/design/source-of-truth`. Package-local references,
examples and UI metadata remain together. The entrypoint now follows declared
project authority and repair routes instead of requiring project-foundation.
Earlier dated records retain their original tested source identities.
Migration routing evidence is recorded in [the extraction review](framework-extraction.md).
