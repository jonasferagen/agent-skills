# Validation and alignment — Test Audit

## Behavioral scenarios

These describe expected outcomes. They are author-reviewed scenarios, not claims
of an independent agent evaluation or a live run.

| Request and context | Expected outcome |
| --- | --- |
| A focused-test marker (`.only`, `fit`, `fdescribe`) is found | Reported prominently as a hard finding: it silently skips every unfocused test in its scope (its file in some runners, the whole run in others), so the suite can still report green over a denominator it never names. Removed only with the user's approval. |
| A skip marker (`.skip`, `xit`, `xdescribe`) is found | An advisory candidate, not a hard finding: the runner still counts the skipped test, so the denominator stays visible. |
| A fast-subset or fail-fast lane is offered as the verification result | Refused as non-certifying; it stops early or excludes tests by design, so it does not name what it measured. |
| A fast lane lists its members explicitly | Membership is read as a performance classification, not a coverage exception; the full lane must still select every listed test. |
| Coverage is run to locate untested branches | Run on the full lane, with the report scoped to the surface under audit; a test elsewhere may cover that surface. |
| A double answers whatever the code asks it | Named as an unfalsifiable request: the label names, field names, format and exit codes the code claims about an external contract were never checked against the real thing. Distinguished from drift, because there was nothing to drift from. |
| A cast-shaped stub supplies fewer members than the collaborator's used methods | Treated as correctness evidence that can hide a live branch defect, not as style noise. |
| An integration test re-proves a rule the inner layer owns | Flagged: the duplicate is slower, fails in pairs so one regression reads as two, and the copies drift until one is quietly wrong. The integration test asserts the rule ran, not what it concluded. |
| An integration suite is offered as licence for an untested inner layer | Refused: wiring proved and decisions unproved leaves a green that measured none of the rules it claims to protect. |
| A 200 response, a no-throw, or a broad snapshot is the only assertion | Flagged as insufficient on its own; the test must be able to fail for the promised behavior. |
| A test asserts private fields, incidental calls or implementation order | Flagged; observable output or state is the subject. |
| A source file has no test while its siblings do | A candidate gap, not a verdict. Pass-throughs, type-only modules, framework scaffolding, fixtures and integration-covered contracts may be intentional. |
| Production and test trees are not colocated | Coverage asymmetry is traced by class and endpoint name, because a scanner cannot infer it. |
| A scanner reports a count of advisory findings | Read as drift against the last audit, not as a defect total; a healthy suite does not score zero. |
| A scanner's exemption ledger is proposed | Judged as a check in its own right: it may only shrink, so a new or increased violation fails. |
| A report-only drift stamp is proposed, with no consumer acting on the diff | Named as an anti-pattern; the scanner runs against the live tree instead. |
| The repository has no test scanner | The audit proceeds; the skill carries no scanner and the scanner step is conditional. |
| A test bends itself into knots around a production contract | Handed on as a finding about that contract, not papered over in the test. |
| The user asks for an audit and the suite has gaps | Gaps are reported; writing the missing tests is named as follow-up work, not performed as part of the audit. |
| Tests, fixtures or production code would need editing | Left read-only unless the user asked for edits; stale prose the audit surfaces is repaired where the fix is mechanical and the work already authorizes repository edits. |
| The repository's own testing guidance contradicts a lens here | The repository's conventions are the standard; the contradiction is reported to the user as documentation drift, quoting both passages, and neither side is edited. |
| Adopting the skill into an existing project | No test rewriting, framework change or coverage threshold is implied; deliberately thin tests are recorded with their rationale. |

## Scope boundaries

Audits settled tests. It does not review a change in flight, decide a
repository's testing standard, choose frameworks or layers, or write the missing
tests it finds. It carries no scanner: what a scanner is worth asserting and how
to read its output is guidance, not an included tool.

Three neighbouring passes are deliberately out of scope and handed on: tests
inside a change under review, a finding whose real subject is the production
contract, and whether a custom check or gate survives structural change.

## Sources inspected

Imported from the owner's Forge Agent Kit `test-audit` skill at
`c98147a115a30f36b952df5faf1c869b54480c59` (2026-09-18) on 2026-09-29, as
`SKILL.md` plus the `principles` and `triage` references.

Three citations of the Forge Project Policy were redirected, because that policy
opens by stating nothing is in production and both consuming projects are, with
their own posture documents. Two of the three carried substance that is now
stated in place: that a green result over an unnamed denominator is a defect in
the check, and that unproved decisions behind proved wiring are a defect in the
evidence. The third defers to the reading project's own policy.

References to three sibling Agent Kit skills were replaced with descriptions of
the boundary, since each skill directory is the installable unit here and a
cross-package path would break when this one is installed alone. One reference
into a sibling's reference page was inlined, keeping the shrink-only ledger rule
and the report-only drift-stamp anti-pattern it was citing.

One upstream sentence was dropped at import without being recorded here: a fast
lane's explicit membership list is a performance classification, not a coverage
exception, so the full lane must still select every listed test. It was restored
on 2026-09-30; see the resolutions below.

This fills a gap the repository declared on purpose: `typescript-patterns` leaves
testing conventions to the reading repository, so both consuming projects owned
them locally with no shared method.

## Review limits

- No independent agent evaluation has run against these scenarios.
- Not yet applied to a real suite in either consuming project. The two surfaces
  it is expected to matter most for are a mail runner whose doubles stand in for
  a provider API, and a producer/consumer boundary between the two projects.
- The scanner guidance is untested here, because neither consuming project has a
  test scanner. It remains conditional in the workflow.
- The unfalsifiable-request lens is the highest-value claim in the package and
  the least validated: it has been reasoned about, not yet run against a suite
  built on provider doubles.

## Clear writing pass — 2026-09-30

Version 0.1.1 revises the prose; see the [package
sweep](clear-writing.md#package-sweep--2026-09-30). The two instructions to read
local testing guidance first were merged, "footgun" became "hard finding", and
idioms in the principles were replaced with the behavior they described.
Independent review found the requirements unchanged; two wording corrections
followed. No behavioral trial was run.

Left unresolved, because each answer changes behavior:

- The entrypoint and `triage.md` treat focused *and parked* markers as hard
  failures; `principles.md` makes the focused-test marker the only hard finding.
- The entrypoint says a focused marker reduces the suite to one case;
  `principles.md` and the scenario above say it disables every sibling in its
  file.
- `triage.md` scopes the coverage run to the surface under audit, then says to
  run it on the complete suite, without saying whether that means the whole
  repository.
- "Documentation drift to reconcile" does not say whether reconciling includes
  editing documentation during an otherwise read-only audit.

## Diagrams and tables pass — 2026-09-30

No change; see the [package
pass](diagrams-and-tables.md#package-pass--2026-09-30). The package has no
diagrams or tables, and a table of scanner signals would have to settle the
marker-tier contradiction recorded above. Newly found: `triage.md` also says a
focused marker shrinks the suite to a single case, a third instance of the scope
conflict.

## Resolutions — 2026-09-30

The owner accepted each proposal from the contradiction research; the decisions
on marker tiers and on documentation drift are theirs. Version 0.2.0 carries
these changes.

- Marker tiers: the entrypoint and `triage.md` made focused *and parked*
  markers hard → only the focused-test marker is hard; skip markers are
  advisory, in all three pages and the scenarios above (owner decision).
- Focused-marker scope: "one case" and "every sibling in its file" → "every
  unfocused test in its scope (its file in some runners, the whole run in
  others)". Tested in a scratch project: Jest 30.5.2 and Vitest 5.0.3 skipped
  only the rest of the focused file; Mocha 12.0.2 and Jasmine 7.0.0 ran only
  the focused case across both files. Jest and Mocha exited 0, Jasmine exited 2
  ("Incomplete"), and Vitest failed only with `CI=true`; hence "can still report
  green".
- Coverage run: scoped to the surface and also "the complete suite" → the full
  lane runs; the coverage report, not the test selection, is scoped to the
  surface.
- Documentation drift: "drift to reconcile" named neither side nor the action →
  a contradiction between local guidance and a lens is reported to the user,
  quoting both passages, and neither side is edited (owner decision).
- Stale prose: the entrypoint's "mechanically repair" and the scenario's "may be
  repaired" → repaired where the fix is mechanical and edits are authorized.
- Undefined terms: "coverage-shape pass" → the repository's report of source
  files without tests; "owning factories" → fixture factories from the package
  that owns the type, as upstream `typescript-patterns` defined them.
- Fast-lane membership: the upstream sentence dropped at import is restored in
  the entrypoint, with a scenario above.
