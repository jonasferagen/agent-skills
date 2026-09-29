# Validation scenarios — TypeScript Patterns

Use these cases when changing the skill. They define useful observable outcomes;
they are not claims that an independent agent has passed them.

| Request and context | Expected outcome |
| --- | --- |
| A constructor takes six positional arguments, two of them optional | Escalate to a parameter object at the documented trigger; stop there unless invariants or behavior accrete. |
| A DTO parsed from a wire response gains its first normalization helper | Keep it a named passive contract; promote to a value object only once normalization, invariants or derived values gather around it, and say which trigger fired. |
| A consumer accepts a whole client but calls one method | Introduce a port at the consumer. Do not add one where the consumer genuinely needs the concrete dependency. |
| A cast is unavoidable at an opaque browser or vendor boundary | Keep the cast local and explained; prefer it to a false abstraction that would license invalid production values. |
| Asked to add tests for a module the skill just reshaped | Defer to the reading repository's own testing conventions. The canon carries no test layout, fixture, mock or coverage policy. |
| Asked which companion skill reviews the current diff | Answer from the reading repository's own workflow. The package names no companion skills and must not invent one. |
| The reading repository's instructions contradict a rule here | Surface it as documentation drift between two owners, not as permission to follow whichever rule is easier. |
| A non-React codebase asks for help naming a module and its exports | Apply the framework-neutral rules only; the conditional React guidance stays unapplied. |
| Fix a one-line naming typo in a file that has several other smells | Make the small edit. Do not open a broad reshaping pass off the back of it. |
| A lint rule catches a real defect class and a correct-by-construction idiom alike | Follow the exemption guidance rather than weakening the rule or disabling it wholesale. |
| A helper is wanted for a value that already has a natural home class | Prefer a static on that class over a new standalone exported function. |
| Asked to wrap an awkward legacy shape so call sites stop seeing it | Prefer removing the bad shape to adding a compatibility layer; name what the wrapper would owe the transitive contract. |

## Initial checks — 2026-09-29

Structure validated against the skill-creator conventions: an 80-line `SKILL.md`,
and a table of contents on `references/typescript.md`, the one reference page
over 300 lines. Every relative link and heading anchor resolves inside the
package, with none pointing outward. No references to companion skills remain
after the decoupling, and the frontmatter description was rewritten to list
call-site symptoms rather than advertise testing.

The author reviewed the instructions against the cases above. No independent
behavioral evaluation has been run, and the package has not yet been exercised
in a real project since testing left its scope.
