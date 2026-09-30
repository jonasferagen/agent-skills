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
| The reading repository's instructions contradict a rule here | Report it to the user as documentation drift between two owners, quoting both passages. Edit neither side, and do not follow whichever rule is easier. |
| A non-React codebase asks for help naming a module and its exports | Apply the framework-neutral rules only; the conditional React guidance stays unapplied. |
| Fix a one-line naming typo in a file that has several other smells | Make the small edit. Do not open a broad reshaping pass off the back of it. |
| A lint rule catches a real defect class and a correct-by-construction idiom alike | Follow the exemption guidance rather than weakening the rule or disabling it wholesale. |
| A helper is wanted for a value that already has a natural home class | Prefer a static on that class over a new standalone exported function. |
| Asked to wrap an awkward legacy shape so call sites stop seeing it | Prefer removing the bad shape to adding a compatibility layer; name what the wrapper would owe the transitive contract. |
| Name a file of passive types shared by nearby callers | `{Topic}Types.ts` in PascalCase beside them. A lowercase domain noun only inside a `types/` contract directory; camelCase only for class-free runtime modules. |
| A `parsers/` folder holds only parsers for several domains | Treat it as a role folder: split by concept, or rename it to a pipeline phase such as `parse/`. |
| Asked to review a colleague's diff for shape smells | Use the review heuristics as questions inside the repository's own review workflow. The package supplies prompts, not a review procedure. |
| A closed-union `switch` returns a value and has no `default` | Call it safe only under `strictNullChecks` with a declared return type that excludes `undefined`, or under `noImplicitReturns`. |

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

## Resolutions — 2026-09-30

Version 1.1.0 carries these changes.

The owner accepted every recommendation below. The version stays 1.0.2 until
release.

- Drift with local docs: "reconcile" versus the scenario's "surface". The
  manifest now says to report it to the user, quoting both passages, and to
  edit neither side. Owner decision: report.
- Type-module filename case: three answers. Owner chose PascalCase
  `{Topic}Types.ts` for sibling contract files, a lowercase noun only inside a
  contract directory, and camelCase for class-free runtime modules, in
  `naming-and-placement.md` and `typescript.md`.
- Prefix versus barrel: "the import site loses the path context" versus
  importing through the barrel. A prefix now stays for concepts used widely
  outside the directory, because it names the domain at every later use.
- `parsers/`: forbidden, then implied acceptable. It is now a role folder even
  when every file is a parser; only a `types/` contract folder is exempt.
- Prefix-rule "When Not To Use": two items were not exceptions. They are now
  rules; the public-API item joined the public-identity condition.
- "Two or three files … known growth area": exempted no rule. It is now an
  exception to the one-file flattening rule. Owner decision.
- Review heuristics: authoring-only versus reviewing a colleague's code. The
  page now supplies prompts for use inside the repository's review workflow,
  and its diagnostics say "the change" instead of "the diff".
- TS2366: the safe closed-union shape lacked a settings caveat. Both pages now
  require a declared return type without `undefined` under `strictNullChecks`
  (TS2366), or `noImplicitReturns` (TS7030). Tested with TypeScript 5.9.3 (no
  error by default) and 7.0.2 (TS2366 by default; none with `--strict false`).
- "Conduit": a forwarding class and an external boundary. The external sense
  is now "boundary", matching the vendor-cast scenario.
- Enforcement "both directions": undefined. The probe now checks that the idiom
  stops being reported and the defect is still reported.
- Smaller slips: "constraint" became "type parameter" in
  `types-and-generics.md`; `class-shape.md` names the costs it compares; the
  lifecycle list in `dependency-ports.md` no longer calls keeping the concrete
  dependency a port; its contents list gains the provider-types section;
  `resolution.md` says "the ledger" for "it".
- Testing leftovers removed: the fixture-module naming sentence in
  `naming-and-placement.md` and `fixtures/` in `directories.md`.

Still open: `directories.md` allows a top-level `utils/` catch-all, while
`naming-and-placement.md` says to avoid `Utils` and the concept-or-phase rule
forbids `helpers/`.

## Discovery routing — 2026-09-30

The description was shortened. See [the discovery review](discovery.md) for the measured sizes, scope and verification. Earlier behavioral results do not establish the new discovery behavior.
