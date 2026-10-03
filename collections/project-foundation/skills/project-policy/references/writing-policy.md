# Write and check policy facts

Use this when establishing, changing or reconciling the policy document itself.
An assessment that preserves the existing policy can keep its findings in task
notes or the hand-back without loading these document-shape instructions.

Keep the Policy section of `project-docs/foundation.md` (or an established separate
policy owner) to one two-column table:
`Axis | Current fact or decision`. Use short, formal entries; separate facts with
semicolons and state unknowns explicitly. The
[foundation format](../../../references/foundation-format.md) owns document shape
and inheritance; keep interpretation instructions out of the foundation.
Record operating circumstances and adopted constraints, such as offline-only use
or a recovery target. Exclude repository procedures, implementation reports,
impact assessments and change history.

Interpret that table together with the established boundaries to derive downstream
requirements. Record durable requirements in their affected design or operational
owner; repository working rules belong in `AGENTS.md` or its linked contributor
guide. Put transition tasks and impact assessments in existing work notes, and
verification results in evidence records. Create another document only when no
existing owner serves the reader. Do not add a requirements table to the policy section.
Keep the originating policy axis and boundary traceable from downstream decisions.

When reconciling an expanded policy, relocate useful rules and evidence before
removing their sections. Preserve adopted obligations and repair consumers; moving
a requirement does not relax it. Use project-docs to choose appropriate homes.

## Verify the application

- When establishing or substantively revising policy, check that each axis has
  evidence, a decision or an explicit unknown. For wording-only edits, verify
  that obligations are unchanged without reconstructing the profile.
- Check that the policy body contains only the axis table, with concise facts,
  decisions and explicit unknowns; keep consequences and evidence in their owners.
- Trace changed requirements to their consumers, work items and acceptance
  evidence. For unaffected areas, record a short reason when reviewing a change.
- Confirm that existing commitments and live state were preserved unless their
  change was authorized. Separate current scope from a proposed future scope.
- Check local links and the repository's applicable documentation checks.
  Report which checks ran and which operational claims remain unverified.

Use [canonical document homes](../../../references/document-homes.md) for foundation
facts, governance decisions and impact records; technical consequences retain
their repository owners. Follow existing-layout transition rules before moving files.
