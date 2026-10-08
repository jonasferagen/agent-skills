# Project policy extraction review

Reviewed on 2026-10-08 from agent-skills base
`2611f25f8360bc898ebd5eb120fa06b62d9c6b2b`. Version 0.1.0 is an unreleased
standalone skill. The package carries forward the project-policy workflow from
the retired project-foundation documents collection and the lightweight native
convention in project-bootstrap at `395aa2d9830acca7a1f3f022af347da081d25667`.
It does not adopt the retired framework's table format, authority files or paths.

## Author walkthrough

These are informed author reviews of the completed entrypoint and conditional
references, with intended outputs checked against the instructions. They are not
independent discovery trials or evidence of spontaneous selection. No isolated
agent context or host metadata was exercised; no context-cost total is claimed.

| Request and supplied facts | Route reviewed | Result |
| --- | --- | --- |
| Explain whether a documented command rule covers a wrapper | SKILL.md; known policy scope and exceptions | Answer the scoped interpretation; establishment and change references are unnecessary |
| A recovery rule exists but no restore result is supplied | SKILL.md compliance and evidence guidance | Report the guarantee as unverified; neither waive the rule nor invent a failure |
| Establish policy for a local experiment with real retained records | SKILL.md; establish.md | Review data, authority, lifetime and recovery facts; local and experimental labels do not imply disposal permission; unknown decisions stay explicit |
| Expand a local service to shared use, retaining its data | SKILL.md; changes.md; relevant axes in establish.md | Trace users, access, compatibility and recovery requirements; route affected service responsibilities to service-boundaries and implementation checks; adoption does not prove readiness |
| Stop supporting a client while retained state still matters | SKILL.md; changes.md | Assess simplification against remaining guarantees; do not infer permission to purge state or remove all compatibility mechanisms |
| Correct a spelling error in an existing operating guide | Task boundary in SKILL.md | Use writing guidance; no policy reconstruction, new record or format migration |

The first two cases need no deeper references. Establishment reaches the seven
axes without mandating a schema; changed circumstances reach consequences even
without a policy-file edit. The nearby wording task avoids the broader workflow.
Relevant missing project decisions and missing evidence remain separate.

## Checks and limits

The skill-creator quick validator and package validator passed. The full
`python3 scripts/check.py` passed on Python 3.14.4 and Node 24: four suites,
157 tests, no skips. No executable helper or document template was added.

The review does not establish policy adequacy for a real consuming project,
operational compliance, native client registration or independent discovery and
reporting reliability. Those claims require separate evidence. No release tag
was created.

## Reusable finding

Policy interpretation and establishment have a reusable workflow beyond document
placement. Keeping that workflow in a standalone skill avoids competing with a
distribution's document-home conventions. Project-bootstrap owns adoption and
placement defaults; the consuming project owns facts, requirements and exceptions.
This extraction supplies the missing skill home without adding framework rules
to source-of-truth, work-records or service-boundaries.
