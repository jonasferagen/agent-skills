# Scheduled service trial — 2026-10-07

Fresh-context trial for revision 0.9.0, which added the scheduled service class.
The fixture was a consumer with one running service already defined and a project
whose stated facts made part of the obvious design unschedulable: exports are
built by a command that takes the catalogue write lock and must not run while an
author is editing, and shipping costs money per call. The operator's request was
only that shipping stop being something they remember. Nothing was installed,
started or enabled.

## Result

The class was found and used, and the decision the class exists for was made
correctly. The evaluator scheduled only the shipping of exports already finished
and left the build command alone, naming the write lock as an attended
precondition that nobody can promise for an unattended window. That is the same
conclusion the one real instance of this class reached on its own, reached this
time from the guidance rather than from the instance.

Its design carried the class's properties without being told them case by case:
the five actions operate the schedule, `start` installs and arms it, `stop`
disables it while leaving unit files, completed runs and the ledger in place, unit
names derive from the checkout, a missed window runs late rather than skipping,
one lock is shared between the schedule and manual invocation so the second
declines, evidence lives outside the unit, and `status` reports schedule, last run
and last success together, exiting nonzero with a named reason. It read no helper
implementation source, confirming for a second trial that the binding surface is
documented where consumers look.

It recorded its departure from the shared runtime helper and explained it
correctly: that binding's `start` operates an installed unit without installing
one and its `status` asks for live readiness, which is the wrong evidence for a
service holding no process.

## Findings

- **A rule of this revision was written too absolutely.** The run rules listed
  making a paid call among the things an unattended run must not do, while the
  operator's whole request was a daily paid shipment. The evaluator read it as
  forbidding gratuitous spend, bounded the spend, and said the stricter reading
  would mean the schedule should not exist. The reading was right and the wording
  was wrong: it had been generalized from an instance where the paid call was
  incidental. Fixed in the same revision, which now separates disturbing live work
  from spending, and requires a scheduled run to bound the cost its policy chose
  rather than avoid cost as such.
- **The implementation departure recurred.** Both this trial and the real instance
  wrote their own schedule units and justified doing so. The convention now states
  that a scheduled service owns its own units because `start` is what installs the
  schedule, so the shape is expected rather than a departure to defend. Whether
  the helper should gain a schedule binding stays open; one real instance is not
  a basis for that interface.
- **Not a product defect:** the evaluator reported that the fixture's
  `project-docs/foundation.md` has no `## References` heading, so the project-wide
  bare status never reached the installed collection's checkout. The fixture was
  at fault. All four repositories in the authoring workspace carry the heading and
  a bare status reaches every member, including one with no service home, which was
  checked directly rather than assumed.

## Limits

One trial, one fixture, one task shape. The evaluator exercised its own job
against a stand-in command in a throwaway copy, but installed no unit, so no
`start`, `stop`, `restart` or timer firing is evidenced, and the unit text was
never parsed by systemd. The class guidance is therefore verified as guidance a
consumer can follow, not as a running schedule. The nearby-work and
source-authoring routing cases remain unexercised.
