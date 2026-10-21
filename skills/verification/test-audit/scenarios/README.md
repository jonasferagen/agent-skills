# Test audit scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Markers, subsets and coverage

| Request and context | Expected behavior |
| --- | --- |
| A focused-test marker (`.only`, `fit`, `fdescribe`, or the runner's equivalent) is found | Reported prominently as a hard finding: it silently skips every unfocused test in its scope (its file in some runners, the whole run in others), so the suite can still report green over a denominator it never names. Removed only with the user's approval. |
| A skip marker (`.skip`, `xit`, `xdescribe`, or the runner's equivalent) is found | An advisory candidate, not a hard finding: the runner still counts the skipped test, so the denominator stays visible. |
| The project's fast test subset lists its members explicitly | Membership is read as a performance classification, not a coverage exception; the full run must still select every listed test. |
| Coverage is run to locate untested branches | Run on the full suite, with the report scoped to the surface under audit; a test elsewhere may cover that surface. |
| A fast-subset or fail-fast run is offered as a complete verification result | Reported as partial feedback; it excludes tests by design. |
| A source file has no test while its siblings do | A candidate gap, not a verdict. Pass-throughs, type-only modules, framework scaffolding, fixtures and integration-covered contracts may be intentional. |
| Production and test trees are not colocated | Coverage asymmetry is traced by class and endpoint name, because a scanner cannot infer it. |

## Doubles and assertions

| Request and context | Expected behavior |
| --- | --- |
| A double answers whatever the code asks it | Named as an unfalsifiable request: the label names, field names, format and exit codes the code claims about an external contract were never checked against the real thing. Distinguished from drift, because there was nothing to drift from. |
| A cast-shaped stub supplies fewer members than the collaborator's used methods | Treated as correctness evidence that can hide a live branch defect, not as style noise. |
| An integration test re-proves a rule the inner layer owns without seeing another boundary | Flagged as overlapping; keep a public-path case and any cases where the boundary changes the outcome. |
| An integration test that runs the command as a separate process checks contention between independent sessions, which an in-process test cannot see | Kept as distinct evidence, even if both tests call the same command. |
| An integration suite is offered as licence for an untested inner layer | Refused: wiring proved and decisions unproved leaves a green that measured none of the rules it claims to protect. |
| A 200 response, a no-throw, or a broad snapshot is the only assertion | Flagged as insufficient on its own; the test must be able to fail for the promised behavior. |
| A test asserts private fields, incidental calls or implementation order | Flagged; observable output or state is the subject. |

## Scanners

| Request and context | Expected behavior |
| --- | --- |
| A scanner reports a count of advisory findings | Read as drift against the last audit, not as a defect total; a healthy suite does not score zero. |
| A scanner's exemption list is proposed | Judged as a check in its own right: it may only shrink, so a new or increased violation fails. |
| A report-only baseline snapshot is proposed, with nothing acting on the diff | Named as an anti-pattern; the scanner runs against the live tree instead. |
| The repository has no test scanner | The audit proceeds; the skill carries no scanner and the scanner step is conditional. |

## Scope and authority

| Request and context | Expected behavior |
| --- | --- |
| A test bends itself into knots around a production contract | Reported to the user as a finding about that contract, not papered over in the test. |
| The user asks for an audit and the suite has gaps | Gaps are reported; writing the missing tests is named as follow-up work, not performed as part of the audit. |
| Tests, fixtures or production code would need editing | Left read-only unless the user asked for edits; stale prose the audit surfaces is repaired where the fix is mechanical and the work already authorizes repository edits. |
| The repository's own testing guidance contradicts a lens here | The repository's conventions are the standard; the contradiction is reported to the user as documentation drift, quoting both passages, and neither side is edited. |
| An existing project is audited for the first time | No test rewriting, framework change or coverage threshold is implied; deliberately thin tests are recorded with their rationale. |

## Limits

- The focused-marker scope statements were checked against a few JavaScript
  runners only (some skip the rest of the focused file, others run only the
  focused cases across files; exit status varies). Other runners are untested;
  confirm the scope in the runner's own documentation.
- The unfalsifiable-request lens and the scanner guidance are the least
  validated parts of the skill.
