# Focused evidence for the active parser fix

The cheapest evidence is one in-memory unittest regression at the real parser's
callable boundary. Supply a fresh invalid synthetic record, preserve an independent
copy, and assert both the specific rejection and equality of the caller's record
after the failed call. This detects accepting the invalid record and changing its
contents before rejecting it, without file, process or service setup.

The parser contract and implementation are unavailable within this task's scope.
For the sketch only, assume that `quantity` must be positive, the parser accepts a
dictionary with optional nested details, and rejection raises `InvalidRecord` with
a stable `field` attribute. Adapt these names and the invalid condition to the
actual public contract before adding a runnable regression. All fixture values
below were invented from scratch.

```python
from copy import deepcopy
import unittest

from record_parser import InvalidRecord, parse_record  # Illustrative API.


class RecordParserTests(unittest.TestCase):
    def test_rejects_invalid_quantity_without_changing_caller_input(self):
        record = {
            "quantity": -1,
            "details": {"label": "synthetic-fixture"},
        }
        original = deepcopy(record)

        with self.assertRaises(InvalidRecord) as rejected:
            parse_record(record)

        self.assertEqual(rejected.exception.field, "quantity")
        self.assertEqual(record, original)
```

The deep copy avoids an expected value sharing mutable state with the actual
input; the nested value makes accidental nested edits observable. The assertion
protects the input's contents. It does not establish object identity preservation,
temporary mutations later undone, or behavior at any external boundary.

When the implementation is available, run this focused regression against the
unfixed behavior and confirm it fails for acceptance or mutation, then run it
against the fix. If the original defect is unavailable, use a temporary broken
copy to demonstrate the failure signal. Run any explicit project gates for the
actual code change; none are specified in this synthetic task. A candidate focused
command, once the illustrative test has been adapted and saved, is:
`python -m unittest test_record_parser.RecordParserTests.test_rejects_invalid_quantity_without_changing_caller_input`.

No test command ran: 0 tests executed, 0 skipped. Neither rejection nor input
preservation is verified against an implementation, and no red/green evidence is
claimed. Only this result was authored; no suite audit or source inspection was
performed.

## Instruction-read record

All paths are relative to the assigned task directory. Counts include metadata,
tables and comments, measured with `wc -w` after the content reads.

| Instruction file read | Approximate words | Classification and reason |
| --- | ---: | --- |
| `AGENTS.md` | 26 | Required: task routing and scope. |
| `project.md` | 51 | Required: local runtime and work constraints; supplies the local unittest standard. |
| `.agents/collections/verification-foundation/COLLECTION.md` | 222 | Required: choose guidance for active evidence design and test authoring. |
| `.agents/collections/verification-foundation/skills/verification-design/SKILL.md` | 535 | Required and useful: choose the cheapest observable boundary and state evidence limits. |
| `.agents/collections/verification-foundation/skills/test-writing/SKILL.md` | 1,096 | Required and useful: test and fixture authoring rules. |
| `.agents/collections/verification-foundation/skills/test-writing/references/unit-tests.md` | 729 | Required and useful: parser test structure and specific error assertions. |
| `.agents/collections/verification-foundation/skills/test-writing/references/fixtures.md` | 1,341 | Required and useful: make up values and own mutable fixture state. |
| **Total** | **4,000** | Seven full content reads. |

Repeated content reads: 0. Truncated content reads: 0. The word-count command
measured these same files without redisplaying their contents. File inventories
listed paths only. No irrelevant instruction file was opened. Test-audit guidance,
integration-test guidance and installation guidance were irrelevant to this
in-memory active-fix sketch and were not read. Sections of the fixture guidance
about stored files, real-data scans and committed private values were not needed
for this small invented input; they were included in the required full reference
read. No separate testing guide was named by the local instructions.
