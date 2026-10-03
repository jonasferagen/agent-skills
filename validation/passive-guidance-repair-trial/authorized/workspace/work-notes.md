# Work notes

## 2026-10-03: Broken evidence guidance link during delivery reading

Task: answer who may accept a delivery and whether a successful copy establishes
acceptance; correct `recieve` to `receive` without changing the agreement.
The installed `project-contracts/SKILL.md`, reached from `AGENTS.md`, links to
`../../references/status-and-evidence-note.md`. Reading that path failed because
it does not exist. Provenance pins the collection to
`960ababc1a5a1ef7ae23361df5df13e25ad28d9c` in the authorized source repository.
This is a broken guidance route, not a missing project acceptance decision.

The authoritative agreement supplied the complete answer, so unaffected work
continued: `answer.md` names Mira and the matching revision/receipt conditions,
explains that copying proves transfer only, and cites the agreement. The spelling
correction is complete. The agreement SHA-256 stayed
`3356125903061fbe8a67dde2c164fddc41fa3470cc65c66f622040404e1dd51e`.

The source at the pinned revision has the same incorrect link; its existing
`references/status-and-evidence.md` supplies the intended status/evidence guidance.
Standing project authorization covered a one-link source repair, required checks,
validation notes and local landing. The repair and its record were committed in
an isolated source worktree and fast-forwarded to local `main` as
`5c13806dfcd14203919f99425c5045d2f490b795`. The source worktree is retained.

Checks observed: nine skill metadata checks passed, collection-local link errors
decreased from one to zero, and `git diff --check` passed. The original reading
case, nearby literal spelling route and a deeper focused acceptance-review case
were traced. The full prescribed validator did not pass: this fixture omits its
standalone package tree and four referenced companion-package copies. Direct
collection checks showed those four omissions unchanged by the repair. Details
and the initial corrected helper-invocation mistake are in source
`validation/notes.md`; runtime compliance and omitted standalone packages remain
unverified.

Consumer adoption was not requested: its installed files and provenance pin were
not changed. A future reading through the installed link will still encounter
the defect until a separately authorized collection adoption.
