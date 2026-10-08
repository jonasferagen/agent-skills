Updated `append_label` to allocate a fresh list when labels are omitted.

Verified with Python 3 that omitted calls return distinct lists and that a supplied empty list is mutated and returned unchanged in identity. All required checks passed.
