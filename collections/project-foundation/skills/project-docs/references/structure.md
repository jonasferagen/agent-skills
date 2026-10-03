# Structure and ownership

Choose document boundaries by reader task. These are possible homes, not required
filenames or a minimum number of files.

| Reader question | Useful home | Keep elsewhere |
| --- | --- | --- |
| What is this, and where do I start? | README or entry page | Detailed setup, release chronology |
| What does this term mean? | Glossary or domain reference | Long implementation explanations |
| How do the elements relate, and why? | Design or architecture explanation | Exhaustive schema transcription |
| How do I perform and verify this action? | Task-specific procedure | Unresolved design proposals |
| What happened, and what was checked? | Dated evidence record | Undated claims of current state |
| What remains to do? | Owning checklist, linked from a short handoff | Copies of the same queue across pages |
| What must an agent preserve? | Project instructions | Full product manuals and repeated workflows |

For a small library, one README may answer most questions. An existing docs site
may already provide the right homes. Add a glossary when terminology carries real
ambiguity, not merely because a project has nouns.

## Foundation definitions

For one project spanning repositories, follow [multi-repository foundations](../../../references/multi-repository.md).
Choose owners at project scope and preserve only local differences in members.
The default entry is `docs/foundation.md` in the
[foundation format](../../../references/foundation-format.md). Preserve its five
sections and table columns. References and Inheritance are declarations;
Boundaries, Overview and Policy hold facts. Keep empty tables as headers only.
Do not add prose, comments, tutorials, routes or extra sections. Link detailed
architecture, procedures, evidence and exception records from the relevant cells
or project instructions. Preserve established homes unless migration is requested.

## Glossary and semantics

Use the reader's term first, followed by a compact definition and an implementation
name only when it helps locate the concept. Identify terms with no dedicated table
or component. Distinguish concepts from representations: a person, a login and an
audit actor can refer to the same human without being interchangeable records.

Explain consequences in the design page: what a relationship means, what it does
not establish, and where uncertainty is allowed. Use a synthetic worked example
when abstract definitions alone do not make the distinction clear.

## Present state and history

Record changing status once, with evidence and a verification date when available.
Entry pages can summarize it and link to the detailed record. Keep unresolved
acceptance checks in one place; distinguish completed provisioning from verified
behavior.

Historical records need a clear milestone or scope. Preserve their evidence, but
avoid letting old imperatives appear to govern current work. Move history when
it interrupts the current explanation; a dated section is enough for short records.
Repair links whenever files move. Do not archive material just to meet a folder plan.

## Prose

Lead with the action or concept the reader needs. Use familiar verbs and short,
connected paragraphs. Lists help with steps; tables help with comparisons.
Avoid conversational residue, unexplained abbreviations and unsupported absolutes.

Explain the reason for a boundary where it helps a decision. Keep necessary
cautions beside risky steps, while linking to the authoritative explanation.
Brief repetition for comprehension is useful; independent copies of changing facts
each need maintenance and can drift apart. Prefer exact references over
copying configuration or schema declarations into prose.

## Project instructions

Keep the entry instructions short enough to route work without loading every
procedure. Preserve project boundaries such as data handling and migration
immutability when they actually apply. Do not infer new approval requirements
from generic skill advice.

A workflow can map change types to checks: documentation links, application tests,
database tests, configuration parsing, or diagram rendering. Discover commands
from the project rather than importing another project's toolchain. Avoid fixed
steps unrelated to correctness, such as installing app dependencies for a prose
change.

For vendored skills, keep project-specific compatibility guidance outside the
vendor directory. Record any necessary local correction, its evidence and how to
reassess it during an update. A pinned upstream version identifies the base; it
does not prove every upstream instruction fits this project.
