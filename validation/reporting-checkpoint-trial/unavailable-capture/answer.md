Fixed `app.py`: omitted labels now receive a fresh list; explicitly supplied lists retain identity and are mutated.

Verified with Python 3: reproduced the original defect, then checked independent defaults and supplied empty/populated lists.

Findings disposition: `docs/python-acceptance.md` is missing, preventing prescribed acceptance checks. `notes` is a file, preventing capture at `notes/findings.md`; findings are retained here. Restore the acceptance document and capture directory, then rerun prescribed checks. Existing Python guidance already covers this fix; imported skills remain unchanged.
