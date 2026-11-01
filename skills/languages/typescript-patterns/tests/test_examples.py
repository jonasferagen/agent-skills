"""Compile reference examples and exercise their runtime boundaries.

Prerequisites: Python 3.11+, Node 24 and TypeScript 5.0+ (tsc on PATH).
No network, sibling package or source-repository helper is used. The source
runner supplies its pinned compiler on PATH; a standalone copy uses the
installed compiler. Missing prerequisites fail explicitly.
"""

from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


PACKAGE = Path(__file__).resolve().parents[1]


def example(page: str, marker: str) -> str:
    text = (PACKAGE / 'references' / page).read_text(encoding='utf-8')
    blocks = re.findall(r'^```ts\n(.*?)^```$', text, re.M | re.S)
    matches = [block for block in blocks if marker in block]
    if len(matches) != 1:
        raise AssertionError(f'{page}: expected one example containing {marker!r}')
    return matches[0]


class TypeScriptExamples(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.node = shutil.which('node')
        cls.tsc = shutil.which('tsc')
        if not cls.node or not cls.tsc:
            raise AssertionError('Install Node 24 and TypeScript 5.0+ (tsc on PATH) before running examples')

    def compile(self, source: str, runtime: str = '', *, succeeds: bool = True) -> str:
        with tempfile.TemporaryDirectory(prefix='typescript-patterns-') as directory:
            root = Path(directory)
            (root / 'example.ts').write_text(source + '\nexport {};\n', encoding='utf-8')
            (root / 'tsconfig.json').write_text('''{
  "compilerOptions": {
    "strict": true, "noUncheckedIndexedAccess": true, "exactOptionalPropertyTypes": true,
    "noEmitOnError": true, "target": "ES2022", "module": "commonjs",
    "lib": ["ES2022"], "types": []
  },
  "files": ["example.ts"]
}''', encoding='utf-8')
            result = subprocess.run([self.tsc, '-p', 'tsconfig.json'], cwd=root,
                                    stdin=subprocess.DEVNULL, capture_output=True,
                                    text=True, encoding='utf-8', timeout=30)
            diagnostics = result.stdout + result.stderr
            if succeeds:
                self.assertEqual(result.returncode, 0, diagnostics)
                if runtime:
                    (root / 'probe.cjs').write_text(
                        "const assert = require('node:assert/strict');\n"
                        "const sample = require('./example.js');\n" + runtime, encoding='utf-8')
                    executed = subprocess.run([self.node, 'probe.cjs'], cwd=root,
                                              stdin=subprocess.DEVNULL, capture_output=True,
                                              text=True, encoding='utf-8', timeout=15)
                    self.assertEqual(executed.returncode, 0, executed.stdout + executed.stderr)
            else:
                self.assertNotEqual(result.returncode, 0, 'An invalid caller compiled successfully')
            return diagnostics

    def test_tuple_preserves_positions_and_rejects_sparse_and_nonfinite_input(self):
        source = example('values-and-collections.md', 'function parseTriple(')
        self.compile(source + '''
const value: readonly [number, number, number] = parseTriple([1, 0, -3]);
const third: number = value[2];
// @ts-expect-error The triple has no fourth position.
const fourth = value[3];
export { parseTriple };
''', '''
assert.deepEqual(sample.parseTriple([1, 0, -3]), [1, 0, -3]);
for (const raw of [null, {}, [], [1, 2], [1, 2, 3, 4], Array(3), [1, , 3],
  [1, undefined, 3], [1, '2', 3], [1, NaN, 3], [1, Infinity, 3]]) {
  assert.throws(() => sample.parseTriple(raw), /Expected three finite numbers/);
}
''')

    def test_brands_reject_wrong_namespaces_and_invalid_raw_identifiers(self):
        source = example('types-and-boundaries.md', 'function parseAccountId(')
        self.compile(source + '''
const account: AccountId = parseAccountId('acct_sample');
const job: JobId = parseJobId('job_sample');
// @ts-expect-error Distinct identifier namespaces cannot be interchanged.
const wrong: AccountId = job;
// @ts-expect-error A raw string is not validated.
const raw: JobId = 'job_sample';
export { parseAccountId, parseJobId };
''', '''
assert.equal(sample.parseAccountId('acct_sample'), 'acct_sample');
assert.equal(sample.parseJobId('job_sample'), 'job_sample');
for (const raw of [null, 2, '', 'job_sample', 'acct_!']) {
  assert.throws(() => sample.parseAccountId(raw), /Expected an account identifier/);
}
''')

    def test_states_reject_impossible_payloads_and_new_unhandled_variant(self):
        source = example('states-and-registries.md', 'type TaskState =')
        self.compile(source + '''
// @ts-expect-error Running requires its payload.
const incomplete: TaskState = { kind: 'running' };
// @ts-expect-error Idle does not carry a failure payload.
const impossible: TaskState = { kind: 'idle', reason: 'failed' };
export { stateLabel };
''', '''
assert.equal(sample.stateLabel({ kind: 'idle' }), 'Waiting');
assert.equal(sample.stateLabel({ kind: 'running', startedAt: 0 }), 'Started at 0');
assert.equal(sample.stateLabel({ kind: 'failed', reason: 'fixture' }), 'fixture');
''')
        extended = source.replace(
            '| { readonly kind: "idle" }',
            '| { readonly kind: "suspended" }\n  | { readonly kind: "idle" }')
        diagnostics = self.compile(extended, succeeds=False)
        self.assertIn('never', diagnostics)
        self.assertIn('suspended', diagnostics)

    def test_total_table_rejects_missing_key_while_membership_array_allows_it(self):
        state = example('states-and-registries.md', 'type TaskState =')
        table = example('states-and-registries.md', 'const BADGES =')
        self.compile(state + table + '''
const precise: 'busy' = BADGES.running;
const subset = ['idle'] as const satisfies readonly TaskKind[];
''')
        diagnostics = self.compile(state + table.replace('  failed: "warning",\n', ''), succeeds=False)
        self.assertIn('failed', diagnostics)

    def test_generics_preserve_key_value_and_parser_handler_relationships(self):
        lookup = example('generics-and-correlation.md', 'function readProperty<')
        operation = example('generics-and-correlation.md', 'function defineOperation<')
        self.compile(lookup + operation + '''
const item = { count: 3, title: 'sample' };
const count: number = readProperty(item, 'count');
const title: string = readProperty(item, 'title');
// @ts-expect-error A count is not a title.
const wrong: string = readProperty(item, 'count');
function parseText(raw: unknown): string {
  if (typeof raw !== 'string') throw new Error('Expected text');
  return raw;
}
const lengthOperation = defineOperation(parseText, text => text.length);
const result: number = lengthOperation.prepare('sample').run();
// @ts-expect-error A string parser cannot feed a numeric handler.
const mismatched = defineOperation(parseText, (value: number) => value + 1);
export { lengthOperation };
''', '''
assert.equal(sample.lengthOperation.prepare('sample').run(), 6);
assert.throws(() => sample.lengthOperation.prepare(3), /Expected text/);
''')

    def test_optional_omission_and_readonly_do_not_imply_snapshot_isolation(self):
        self.compile('''
interface Patch { count?: number | null }
const omitted: Patch = {};
const cleared: Patch = { count: null };
const zero: Patch = { count: 0 };
// @ts-expect-error Explicit undefined is not omission under exact optional checking.
const explicitUndefined: Patch = { count: undefined };
export function example() {
  const original = { values: [1] };
  const view: Readonly<typeof original> = original;
  view.values.push(2); // Shallow readonly permits nested mutation.
  const borrowed: readonly number[] = original.values;
  const snapshot: readonly number[] = [...original.values];
  original.values.push(3);
  return { borrowed, snapshot, value: zero.count ?? 9 };
}
''', '''
const result = sample.example();
assert.deepEqual(result.borrowed, [1, 2, 3]);
assert.deepEqual(result.snapshot, [1, 2]);
assert.equal(result.value, 0);
''')


if __name__ == '__main__':
    unittest.main()
