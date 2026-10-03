# Spelling trial

Request completed: corrected the single `archvie` occurrence to `archive` in README.md. No other project content changed.

## Files actually read

| File | Approximate words | Classification | Reason |
| --- | ---: | --- | --- |
| AGENTS.md | 18 | Required | Fixture entry instructions. |
| context.md | 14 | Required, useful | Explicitly routed; identifies README ownership and literal scope. |
| .agents/collections/project-foundation/COLLECTION.md | 344 | Required, useful | Explicitly routed; says literal wording edits need no authoring workflow. |
| README.md | 6 | Required | Target text. |

No additional guidance was loaded. The collection's other workflow routes were irrelevant to this literal correction. No live repository files or previous trial answers were read.

## Reads and checks

All displayed file reads were complete, with no truncation or content rereads. The edit script reread README.md to make and verify the edit; it also read all four files to count words, without redisplaying their content. Verification asserted exactly one original misspelling and exact final content: heading `Archive`, followed by `A local photo archive.`

The first script attempt failed because `python` was unavailable; retrying with `python3` succeeded. Shell startup emitted stream-fd warnings; file reads and the successful edit/check completed normally. No tests were needed for the literal text edit.
