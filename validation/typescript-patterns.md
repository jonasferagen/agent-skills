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

## Release 1.0.0 — 2026-09-29

Added manifest version metadata for the per-skill release and commit pinning
convention. The TypeScript description is quoted so its colon parses as YAML. The instruction body and references are unchanged.
The manifest validator passes, and all 119 internal links and heading anchors
resolve. Behavioral scenarios remain the review basis above; this packaging
release does not claim a new independent behavioral evaluation.

## Release 1.0.1 — 2026-09-29

Removed three leftover dependencies on the source project's policy. Compatibility
guidance now checks actual deployed consumers and published contracts instead of
assuming nothing is in production. Enforcement guidance states its own rationale.
The manifest validator and all 119 local links/anchors pass. A package search
finds no remaining source-project policy references.

## Clear writing pass — 2026-09-30

Version 1.0.2 revises the prose of the manifest and twelve reference pages;
`types-and-generics.md` needed no change. See the [package
sweep](clear-writing.md#package-sweep--2026-09-30). The description's "blurring"
became "becoming unclear", matching the symptom table. Review found one changed
causal claim about where a total mirror's compile error appears and one clarity
regression; both were corrected with the other wording notes. Code, links and
heading anchors are unchanged. No behavioral trial was run.

Left unresolved, because each answer changes behavior:

- The manifest calls a contradiction with local docs drift "to reconcile"; the
  scenario above says to surface it.
- `directories.md` says an import from outside a folder loses the path context,
  while its rationale says such consumers import through the barrel, whose path
  names the directory.
- `directories.md` forbids `parsers/` as a role name, then implies a folder
  holding only parsers is acceptable.
- `review-heuristics.md` applies its prompts to reviewing a colleague's code,
  then says reviewing a diff is a separate task.
- `dependency-ports.md` uses "conduit" both for a class that only forwards a
  dependency and for an opaque external boundary.
- `enforcement.md` never defines the "both directions" in which a rule can fail.

## Diagrams and tables pass — 2026-09-30

See the [package pass](diagrams-and-tables.md#package-pass--2026-09-30). Three
passages became tables: the shape-escalation steps in the manifest, the family
and subsystem cases in `directories.md`, and the closed-union shapes in
`review-heuristics.md`. Review corrected one changed quantifier, "the other two
fail open" for "two shapes fail open". The tables were rendered at 830 px in
both themes. The version stays 1.0.2, which is unreleased.

Left unresolved:

- Filename case for type-only and contract modules has three answers: a
  lowercase domain noun in `naming-and-placement.md`, camelCase for class-free
  contract modules, and PascalCase in `DeliveryTypes` and `XTypes.ts`.
- `review-heuristics.md` says the safe closed-union shape triggers TS2366
  without the compiler-settings caveat that `typescript.md` gives.
