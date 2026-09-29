# Validation and alignment — Test Audit

## Behavioral scenarios

These describe expected outcomes. They are author-reviewed scenarios, not claims
of an independent agent evaluation or a live run.

| Request and context | Expected outcome |
| --- | --- |
| A focused-test marker (`.only`, `fit`, `fdescribe`) is found | Reported prominently as a hard finding: it silently disables every sibling in its file, so the suite reports green over a denominator it never names. Removed only with the user's approval. |
| A fast-subset or fail-fast lane is offered as the verification result | Refused as non-certifying; it stops early or excludes tests by design, so it does not name what it measured. |
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
| Tests, fixtures or production code would need editing | Left read-only unless the user asked for edits; stale prose the audit surfaces may be repaired where the work already authorizes repository edits. |
| The repository's own testing guidance contradicts a lens here | The repository's conventions are the standard; the contradiction is reported as documentation drift to reconcile. |
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
