# Structured process pages

Use this reference when creating a named process from the process template or
deliberately preparing an existing process for machine browsing. Ordinary reading
and prose corrections need no format migration. Placement remains owned by
[document homes](document-homes.md); status remains scoped under
[status and evidence](status-and-evidence.md).

## Select the format

The [process template](../templates/project-docs/process/README.md) selects
`Process format: project-process/v1` on a separate paragraph after the scoped
Status paragraph. Existing unversioned pages remain valid. An installation upgrade
does not opt them in. Unsupported versions and malformed selected pages fail the
checker rather than silently falling back to prose.

The canonical Markdown page owns the process. A browser derives its facts and
navigation from that page; its manifest must not maintain another editable copy.
This format supplies source structure, not execution instructions or adoption of
the described process. Diagram nodes need not map one-to-one to process steps.

## Facts and sections

Mark a section immediately before its ATX heading with
`<!-- process-section: purpose -->`. Allowed roles are `purpose`, `participants`,
`stages`, `interruptions`, `handoffs` and `evidence`, each at most once. Preserve
existing heading text and anchors when migrating; the marker supplies its role.
Purpose and stages are required. Omit other roles without content rather than
inventing responsibilities, interruptions or evidence to complete a template.

The purpose section contains exactly one `Fact | Value` table. Use the five keys
below in order, with a populated value. Explicit consequential unknowns name their
owner and affected work. The process Owner is not automatically every step's owner.

| Fact | Value describes |
| --- | --- |
| Reader question | The question this process page answers |
| Trigger | The event or request that starts the work |
| Owner | The owner of this explanation and overall process scope |
| Inputs | Required source, context and authority for this process |
| Completion | The scoped result, including meaningful failure or unresolved outcomes |

Keep scope and exclusions beside the table. Keep longer explanations and evidence
in their existing homes and link them. Successful execution, acceptance, selection
and consumer adoption retain their distinct owners and meanings.

## Stable steps and explicit handoffs

The stages section has exactly one table with columns
`Step | Action | Owner | Input | Result / condition | Detail`.
The first cell is a stable lowercase hyphenated key, independent of the displayed
Action, ordinal or Mermaid node ID. Keys are unique within the page and stay stable
when labels change. Owner, input and result state the actual responsibility and
condition. Detail is one explicit Markdown link to the owning explanation, section,
procedure or contract. A table row can summarize linked prose; it must not become
a second independently maintained procedure. Its order does not define execution
order, and linked processes retain their own scope and status.

A handoffs section has exactly one table with columns
`Handoff | From | To | Result | Kind | Detail`, using the same stable-key and
single-link rules. `From` and `To` name the stated participants or processes.
`Kind` is `transfer` for an exchange, `feedback` for findings returning to an owner,
or `specialization` for a bounded process opening a broader process's detail.
These meanings do not establish data transport, authorization or contract adoption.
If no handoff applies, write `Handoffs: None.`; if consequential terms are unknown,
write `Handoffs: Unknown` followed by the owner and dependent work. Do not infer
handoffs from nearby links or arrows. Contract obligations remain with their owner.

## Check and consume

Run `python3 <installed-collection>/scripts/validate-project-docs.py project-docs`.
It checks document homes and the selected process structure. The collection's
`scripts/process_format.py` exports `parse_process(text)`: source-located roles,
facts, steps and handoffs, `None` for legacy prose, or `ValueError` for malformed
selected input. Fenced examples and unrelated HTML comments are ignored.

The checker establishes populated fields, unique keys and supported syntax;
it cannot establish semantic correctness, actual ownership or process completion.
The consumer must resolve Detail links against its selected source roots and heading
anchors, preserve scoped statuses, and report unavailable targets. Record the parser
revision or hash with the generated snapshot. Project-specific graph bindings and
presentation remain governed by that project's selected browsing convention.
