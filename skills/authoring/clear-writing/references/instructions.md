# Writing instructions

An instruction should let its reader decide whether it applies and what to do.
Use this guidance for skills, project instructions, rules and procedures.

## State the condition and action

Place the trigger or prerequisite beside the action it governs. Name the actor
when responsibility could be confused. State the observable outcome or stopping
condition when completing the action would otherwise be ambiguous.

Prefer "If the command fails, report its exit status and stop" to "Command
failures require termination with exit-status reporting." The first makes the
condition and both required actions easier to see.

Keep order explicit when correctness depends on it. "Verify the backup before
deploying" is different from a list containing "verify the backup" and "deploy."
Do not turn an unordered set of recommendations into a required sequence.

## Distinguish the strength of a rule

- **Requirement:** say what must happen or must not happen. Use a direct
  imperative when its force is clear in context.
- **Default:** state the usual choice and what can justify another choice.
- **Suggestion:** describe when an option helps, leaving the reader free to
  choose another suitable approach.

For example, "Use a table to compare options" requires a table. "A table usually
helps when readers need to compare the same attributes across options" offers a
default with a reason. Choose the wording that matches the intended rule; editing
for clarity is not permission to strengthen it.

Use a requirement where deviation would violate a real constraint. Avoid making
an editorial preference mandatory merely because a firm sentence sounds cleaner.
When the source is ambiguous about the rule's strength and that affects behavior,
ask the user or leave the ambiguity visible.

## Keep exceptions with their rules

Put an exception beside the rule it changes, with its scope explicit. "Retry up
to three times, except when the service reports invalid credentials" is easier
to apply than a general retry rule followed much later by that exception.

Do not summarize away qualifiers such as "only," "unless," "at most" or "after."
Check the whole condition: "Stop unless both checks pass" does not mean "Stop if
both checks fail."

If several rules conflict, report the conflict instead of silently choosing a
new precedence. A rewrite can clarify a precedence the source already states; it cannot
invent one.

## Preserve technical and authorization boundaries

Keep exact identifiers, commands, paths and quantities when they carry operational
meaning. Explain them around the literal text rather than replacing them with an
approximation. A procedure that needs precise steps should retain them even when
the result is longer.

Preserve who may act, which system or records an action may affect, and what
approval or evidence it requires. "Get approval before deploying" must not
become "Deploy when ready." Likewise, avoid adding an approval requirement that
the source does not contain.

Examples illustrate a rule; they should not quietly broaden it. Mark assumptions
and use synthetic details when illustrating behavior. Keep explanations next to
the rules they clarify, and remove repeated commands that could drift apart.
