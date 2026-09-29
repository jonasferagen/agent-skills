# Coverage-Gap Classification

Use this method to disposition an inventory of production files with no obvious
sibling test. The inventory is a search result, not a defect list. Keep the
current repository's path list and final dispositions in that repository or its
tracker; this reference owns only the classification method.

## Evidence Required

Open the candidate, its consumers, and every proposed covering test. A name
match is insufficient: imports, comments, fixture types, and mocks can all name
a unit without executing its behavior.

| Classification       | Required evidence                                                                                       | Action                                                          |
| -------------------- | ------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Real gap             | The unit owns branching, parsing, state, IO adaptation, or another observable promise with no assertion | Add a scoped behavior test                                      |
| Integration-covered  | A wider test executes the real unit and contains a named assertion that fails when its contract breaks  | Record the test and assertion; do not duplicate it mechanically |
| Legitimate exception | The file is passive types, a barrel, generated output, or pure delegation with no independent promise   | Record the reason and the owner of the real behavior            |
| Unclear              | The behavior or covering seam cannot be established from current evidence                               | Keep it unclassified and investigate; do not force a bucket     |

## Workflow

1. Produce the candidate inventory from production files and the repository's
   test-naming convention.
2. Remove obvious passive/type-only files and barrels, recording the mechanical
   reason rather than deleting them silently from the count.
3. For each remaining candidate, search for construction and calls, then open
   the tests that exercise those callers.
4. Trace one observable assertion back through the real unit. A mock that
   replaces the unit disqualifies the integration-covered claim.
5. Group real gaps by shared behavior or boundary, not by directory count, so a
   later test pass owns one coherent contract.
6. Store the dated inventory and disposition in the repository that owns the
   files. Refresh it after structural change; never publish a mutable product
   path inventory inside a shared skill.

## Common False Positives

- A type-only import proves compilation, not runtime behavior.
- A `mock()` call is the opposite of exercising the candidate.
- A route or registry test may prove wiring while saying nothing about the
  registered unit's behavior.
- Generated files usually inherit their evidence from the generator or schema,
  but only when that owner is tested.
- Thin delegation is exempt only when it adds no mapping, ordering, error
  policy, lifecycle, or resource ownership of its own.

## Output

Report totals by classification, then list every integration-covered candidate
with its covering assertion and every exception with its owning behavior. Real
gaps become scoped work; unresolved candidates remain explicit. Do not turn the
inventory into a hardcoded gate—use `selfcheck-guard` if a durable structural
check is proposed.
