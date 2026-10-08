# Shared reporting checkpoint trials — 8 October 2026

Three agents performed the same ordinary Python fix in separate fixtures outside
Git. Each was spawned with `fork_turns: "none"`; no parent conversation, expected
findings, skill bodies or earlier trial answers were included in its assignment.
The exact assignments are retained as each case's `prompt.txt`. The coordinator
froze [criteria](criteria.json), fixture inputs and initial file hashes before
launching any agent. Cases were not retried or coached before their first answers.

Entry was through project instructions, not native skill metadata. Each fixture
installed complete python-patterns 0.2.0 and pattern-capture 0.3.0 packages from
agent-skills commit `f6def20478a7ebab5a06766dc066629aedb1d325`. Their exact initial
files and hashes are recorded in each case's `initial-hashes.json`; package copies
can be reconstructed from that commit. The project instructions used the revised
README checkpoint from the uncommitted reporting-verification change on that base.
No other skill package was installed in the fixture.

## Retained cases and results

Each case retains its original task, exact launch prompt, project instructions,
initial code, final code, initial hashes and first final answer. Archived project
instructions are named `project-instructions.txt` so they do not govern source
maintenance here. Initial notes were `# Findings` followed by a newline; the
unavailable-capture case instead had a regular file at `notes` containing the
explanation retained in that case. Only the successful control initially had
`docs/python-acceptance.md`; its contents are unchanged and retained.

- [Stale required route](stale-route/answer.md): the agent fixed the default-list
  defect, identified the missing acceptance document and its blocked conclusion,
  and retained the task, obstacle, effect, disposition and repair candidate in
  [project notes](stale-route/notes/findings.md). All visible criteria passed.
- [Unavailable capture route](unavailable-capture/answer.md): the agent fixed the
  defect, reported both the absent acceptance document and unwritable capture
  home, and preserved the finding and next action in its final answer. All visible
  criteria passed.
- [Successful control](successful-control/answer.md): the agent fixed the defect,
  reported verification, left the empty findings record unchanged and made no
  generic improvement proposal. All visible criteria passed.

The coordinator independently loaded each final `app.py` with Python 3.14.4 and
asserted that two omitted-list calls return separate lists with their own labels,
and that supplied empty and nonempty lists are mutated and returned by identity.
All three passed. Comparing output file hashes with the initial inventories found
no imported skill changes. The stale-route agent changed code and project notes;
the other two changed only code. Python bytecode caches appeared in two fixtures;
they are generated verification output and are not part of the retained inputs.

## Context and evidence limits

Each first answer was frozen before a diagnostic follow-up requested a snapshot
of startup skill metadata and context information. All three snapshots are retained as `startup-metadata.md` per case. Each reports
that the two fixture skills were absent from the startup catalog; project hooks
provided their routes. Supplied descriptions were truncated, and external skill
paths were not checked under the fixture-only restriction. They are retrospective agent
accounts, not a host-exported startup manifest. They cannot independently prove
catalog freshness or which files were actually read.

No exported tool-call/read traces were available to the coordinator. Read-based
criteria and actual Pattern capture activation are therefore unverified. A
statement in a findings record about its assessment does not substitute for an
observed skill read. The supplied launch configuration establishes separate
conversation starts; the diagnostic metadata remains supporting testimony.

These cases demonstrate visible reporting and continuation through configured
project hooks. They do not establish metadata-only selection, full discovery
acceptance under the strengthened method, reliable activation across repeated
runs, or behavior in a consuming project's actual installation. The ordinary
fix naturally exposes the required missing route; it does not test discovery of
a subtle semantic defect in otherwise reachable skill guidance. Further cases
should exercise that boundary before broadening the claim.
