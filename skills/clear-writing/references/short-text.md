# Short text

Use this guidance for labels, one-line descriptions, commit subjects, table cells
and brief confirmations. Aim for the shortest wording that lets the reader
recognize the thing or understand the result without guessing.

## Keep the useful distinction

- Name the thing, action or result directly. Include the owner when ownership
  helps this audience distinguish it from similar things.
- Prefer a stable category over a list of current contents when describing a
  collection. Put an inventory where readers expect it to be maintained.
- Keep qualifiers that change the reader's understanding. Remove those that
  merely praise, hedge without reason or repeat nearby context.
- Preserve real uncertainty. A short status must still distinguish a completed
  action, a planned action and an unverified result.
- Stop when the reader has enough to act or decide. A one-line confirmation
  rarely needs an introduction or a closing summary.

These are choices, not a word budget. Add detail when two plausible readings
would lead the reader to different actions.

## Examples

| Context | Less useful | Clearer |
| --- | --- | --- |
| Description of a growing collection | Agent skills for documentation, diagrams, writing and more | Reusable agent skills |
| Commit subject for a known bug fix | Improve timeout handling | Stop retrying after the final timeout |
| Confirmation after three files were verified as removed | The cleanup operation has now been successfully completed | Removed the three temporary files. |
| Brief status after a successful backup command, with no restore test | Backup verified. | The backup command finished successfully; a restore has not been tested. |

The examples depend on their stated context. Include distinguishing scope when
"Reusable agent skills" is too broad for the audience, and report only results
that the available evidence supports.

## Know when more text is needed

A label can rely on its surrounding interface; an isolated message may need to
name the affected item. Check the text where readers will see it.

Do not compress a procedure into a slogan. Preconditions, failure handling and
exceptions still belong in instructions even when a short label links to them.
