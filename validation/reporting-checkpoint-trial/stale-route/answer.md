Fixed `append_label` to allocate a fresh list when labels are omitted.

Verified with `python3` that omitted calls return independent lists and explicitly supplied empty or nonempty lists are mutated and returned unchanged by identity.

Required `docs/python-acceptance.md` is missing, so project acceptance checks remain unavailable. Recorded the obstacle, effect, disposition, and repair candidate in `notes/findings.md`. Imported skills remain unchanged.
