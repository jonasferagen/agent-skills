# Python foundation

Version: 0.2.0

Use this collection for Python implementation. Start with repository instructions,
its supported interpreter and existing design. Install both members together;
load only the guidance the current change needs.

| Task | Guidance |
| --- | --- |
| Shape operations, state, dependency protocols, naming or module boundaries | [Python design](skills/python-design/SKILL.md) |
| Change types, data boundaries or defaults | [Python patterns](skills/python-patterns/SKILL.md) |
| Handle exceptions, text I/O, resource cleanup or async tasks | [Python patterns](skills/python-patterns/SKILL.md) |
| Add an operation with ownership and language-boundary decisions | Read both members, then their relevant references |
| Install, update or check this collection | [Installation](references/installation.md) |

A focused exception or cleanup fix need not reopen class organization. Design
choices use the member's class-based house style within the project's adopted
constraints; collection adoption does not authorize a repository-wide refactor.
Follow the member's conflict handling when local design and house guidance differ.
Literal prose or JavaScript edits do not select Python guidance.

Application behavior, service lifecycle and verification retain their project
routes. Python tests also need test guidance when being authored. Report a missing
required route with its consequence; ordinary work needs no installation guide or
source-catalog lookup. No interpreter or dependency upgrade is selected by install.
