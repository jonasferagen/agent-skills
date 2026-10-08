# Validation scenarios — TypeScript design

This package carries the class-based house style extracted from
`typescript-patterns` 1.x. The [split record](typescript-patterns.md#split-into-language-and-design--2026-09-30)
maps every former reference and describes migration and verification limits.
Historical validation of the combined package remains on that page.

| Request and context | Expected outcome |
| --- | --- |
| An exported pure geometry operation has no state | Use a static-method class; purity does not exempt it. |
| A service owns state across calls | Use an instance class with constructor-injected dependencies. |
| A React hook, file-private helper or branded-ID guard fits a documented exception | Retain the exception; do not force it into an operation class. |
| A constructor takes six positional arguments, including optional values | Introduce a parameter object at its existing trigger; do not automatically promote it to a value object. |
| A wire DTO gains a normalization helper | Keep passive boundary contracts passive; promote runtime domain data only when its behavior or invariants justify it. |
| A helper reads only one domain object's public surface | Put general behavior on that object, with the existing consumer-specific and trivial-expression exceptions. |
| A consumer uses one method but forwards the dependency to a concrete-dependent recipient | Trace the whole use path; retain the concrete type where needed. |
| A consumer accepts a whole client but uses one stable method | Introduce a truthful consumer-owned port; retain a concrete dependency when its full semantics are needed. |
| A branded-ID guard has a natural home class | Prefer a static on that class over a standalone function, preserving the existing exception. |
| An awkward legacy shape is proposed behind a compatibility wrapper | Prefer removing the obsolete shape; retain a transition only for a named live consumer or published guarantee. |
| Two query clients have the same methods but only one preserves a transaction session | Include lifecycle semantics; structural compatibility alone is insufficient. |
| A sibling contract file is shared by nearby callers | Use PascalCase `{Topic}Types.ts`; retain the separate contract-directory and class-free runtime rules. |
| A folder is named `parsers/` or top-level `utils/` | Apply the concept-or-phase rule; only passive `types/` has its documented exemption. |
| A directory needs no stable public import boundary | Keep direct imports; a barrel is not mandatory. |
| A default could erase meaningful zero or absence | Preserve the domain's absence model and precedence; do not replace it with a sentinel for convenience. |
| A lifecycle grows subscriptions and teardown work | Keep ownership visible and replacement symmetric; delegate domain behavior to collaborators. |
| A non-React module only needs a name | Apply naming guidance without the conditional React conventions. |
| A one-line typo is requested | Make the scoped edit; do not expand it into a broad reshape. |
| A request only concerns a generic type error or a compiler flag | Select language guidance separately; design alone supplies no enforcement policy. |
| Asked for test conventions or the project's review process | Defer to the consuming repository. |
| Local docs contradict this package | Report both passages without editing either owner to settle the conflict. |

## Extraction review — 2026-09-30

The author statically reviewed these scenarios against the extracted references.
The class-shape page, including all exceptions, is unchanged from the source.
The parameter-object, domain-primitive, port and orchestration rules retain their
existing triggers. Type-focused diagnostic questions moved to the language
package; design questions remain here. Each package is independently selectable.

Clear writing was applied to the entrypoint and scope wording. Diagrams and
tables guidance retained the shape-escalation table and selected a symptom table
for the references. No independent agent trial or consumer rollout is claimed;
see the shared split record for measured checks.

## Decisions left for separate changes

The split preserves these conventions rather than revisiting them: class-based
operations and their exceptions, filename case, one primary runtime export,
parameter-object triggers, directory placement, and barrel boundaries. Each can
now be reviewed within design without changing the language package. Enforcement
stays in patterns until a separate tooling trigger justifies another skill.

## Checked package copies — 2026-10-09

Version 1.0.2 identifies module syntax as a checked copy of the passage owned
by typescript-patterns. The rule itself is unchanged.
The [reference-sharing sweep](reference-sharing-sweep.md) records checks,
compatibility evidence and remaining review limits.
