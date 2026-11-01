"""Check the design references' session and dependency examples.

Prerequisites: Python 3.11+, Node 24 and TypeScript 5.0+ (tsc on PATH).
The examples are read from this package and exercised in temporary directories.
No source-repository helper, sibling skill, network or external service is used.
"""

from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


PACKAGE = Path(__file__).resolve().parents[1]


def example(page: str) -> str:
    blocks = re.findall(r'^```ts\n(.*?)^```$',
                        (PACKAGE / 'references' / page).read_text(encoding='utf-8'),
                        re.M | re.S)
    if len(blocks) != 1:
        raise AssertionError(f'{page}: expected one maintained TypeScript example')
    return blocks[0]


class DesignExamples(unittest.TestCase):
    def compile_and_run(self, source: str, probe: str):
        node, compiler = shutil.which('node'), shutil.which('tsc')
        self.assertIsNotNone(node, 'Node is required on PATH')
        self.assertIsNotNone(compiler, 'TypeScript 5.0+ (tsc on PATH) is required')
        with tempfile.TemporaryDirectory(prefix='typescript-design-') as directory:
            root = Path(directory)
            (root / 'example.ts').write_text(source, encoding='utf-8')
            (root / 'tsconfig.json').write_text('''{
  "compilerOptions": {
    "strict": true, "noUncheckedIndexedAccess": true, "exactOptionalPropertyTypes": true,
    "target": "ES2022", "module": "commonjs", "lib": ["ES2022"], "types": [],
    "noEmitOnError": true
  },
  "files": ["example.ts"]
}''', encoding='utf-8')
            result = subprocess.run([compiler, '-p', 'tsconfig.json'], cwd=root,
                                    stdin=subprocess.DEVNULL, capture_output=True,
                                    text=True, encoding='utf-8', timeout=30)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            (root / 'probe.cjs').write_text(
                "const assert = require('node:assert/strict');\n"
                "const sample = require('./example.js');\n" + probe, encoding='utf-8')
            result = subprocess.run([node, 'probe.cjs'], cwd=root, stdin=subprocess.DEVNULL,
                                    capture_output=True, text=True, encoding='utf-8', timeout=15)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_session_owns_independent_state_and_detached_callbacks_keep_it(self):
        self.compile_and_run(example('operations-and-state.md') + '''
export { createCounterSession };
''', '''
const first = sample.createCounterSession(0);
const second = sample.createCounterSession(10);
const { next, reset } = first;
assert.equal(next(), 1);
assert.equal(next(), 2);
assert.equal(second.next(), 11);
reset();
assert.equal(next(), 1);
assert.equal(second.next(), 12);
second.reset();
assert.equal(second.next(), 11);
assert.equal(next(), 2);
''')

    def test_consumer_accepts_small_checked_role_without_acquiring_teardown(self):
        self.compile_and_run(example('dependencies-and-composition.md') + '''
const minimal: ReadingSource = { read: () => 2 };
// @ts-expect-error The role requires numerical readings.
const wrong: ReadingSource = { read: () => 'invalid' };
function unsupportedTeardown(source: ReadingSource): void {
  // @ts-expect-error Borrowing the reading role grants no teardown capability.
  source.close();
}
export { totalReadings };
''', '''
let value = 3;
let closed = false;
const source = { read: () => ++value, close: () => { closed = true; } };
assert.equal(sample.totalReadings(source, 3), 15);
assert.equal(value, 6);
assert.equal(closed, false);
assert.equal(sample.totalReadings(source, 0), 0);
assert.equal(value, 6);
assert.equal(sample.totalReadings({ read: () => 2 }, 4), 8);
''')


if __name__ == '__main__':
    unittest.main()
