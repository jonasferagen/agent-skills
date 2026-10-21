# Project design scenarios

Requests, context and expected behavior this skill is evaluated against. Use them
when changing the skill; ordinary use of the skill does not read them. Record a
run's observed results with the change that ran it, not here.

## Cases

| Request and context | Route | Expected behavior |
| --- | --- | --- |
| Shape a repository whose output is design decisions | SKILL.md, then workflows | A manual document process is a valid mechanism; no service, runtime or deployment is inferred. |
| Distinguish a lending title, a physical copy and a loan | SKILL.md, then conceptual models | Independent lifecycles explain identity; a returned damaged copy need not be available. No database schema is selected. |
| Separate runtime code from authored content | SKILL.md, concrete normal and change cases | Trace content-only and runtime changes, preparation writes and compatibility before choosing another repository or container. |
| Compare ways to execute a selected operation | SKILL.md, then integrations | Compare manual and local options, authority, effects and evidence; no provider guarantee or execution permission follows from a proposal. |
| Sequence an experiment and the implementation that depends on it | SKILL.md | Use the project's planning document or issue tracker; add no second list of open work. With neither, open points stay in the design note and the user is told. |
| A design changes an agreed obligation | SKILL.md | The change is raised through the project's process or with the user; writing it down does not establish implementation. |
| Evidence for one choice is missing | SKILL.md | Only the dependent choice waits; the rest of the design proceeds. |
| Interpret one existing handoff term | The existing handoff agreement | No architecture redesign or full integration pass. |
| Correct a label in a current guide | The existing document | No design reconstruction or format migration. |

## Limits

- The skill supplies reasoning and the default design-note headings in SKILL.md; it ships no further templates.
