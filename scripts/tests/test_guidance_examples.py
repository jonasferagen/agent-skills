"""Compile/run the maintained examples directly from their Markdown owners."""

from pathlib import Path
import re
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
TYPESCRIPT = ROOT / 'collections/typescript-foundation/skills/typescript-patterns/references/typescript.md'
NODE = ROOT / 'collections/typescript-foundation/skills/node-patterns/SKILL.md'


def code_block(page: Path, language: str, containing: str) -> str:
    blocks = re.findall(rf'^```{language}\n(.*?)^```$', page.read_text(encoding='utf-8'), re.M | re.S)
    matches = [block for block in blocks if containing in block]
    if len(matches) != 1:
        raise ValueError(f'{page}: expected one {language} example containing {containing!r}, found {len(matches)}')
    return matches[0]


def run(command: list[str], directory: Path) -> None:
    result = subprocess.run(command, cwd=directory, stdin=subprocess.DEVNULL,
                            capture_output=True, text=True, encoding='utf-8', timeout=30)
    if result.returncode:
        raise AssertionError(f'{command[0]} failed ({result.returncode}):\n{result.stdout}\n{result.stderr}')


class GuidanceExamples(unittest.TestCase):
    def test_tuple_compiles_strictly_and_rejects_invalid_positions(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = code_block(TYPESCRIPT, 'ts', 'function assertVec3(')
            (root / 'tuple.ts').write_text(source + '''
const vector: [number, number, number] = assertVec3([1, 2, 3], 'fixture');
const third: number = vector[2];
// @ts-expect-error The checked result has no fourth position.
const fourth: number = vector[3];
export { assertVec3 };
''', encoding='utf-8')
            run(['node', str(ROOT / 'node_modules/typescript/bin/tsc'), '--strict',
                 '--noUncheckedIndexedAccess', '--target', 'ES2022', '--module', 'commonjs',
                 'tuple.ts'], root)
            (root / 'probe.cjs').write_text('''
const assert = require('node:assert/strict');
const { assertVec3 } = require('./tuple.js');
assert.deepEqual(assertVec3([1, 0, -3], 'fixture'), [1, 0, -3]);
for (const value of [null, {}, [], [1, 2], [1, 2, 3, 4], Array(3),
  [1, , 3], [1, undefined, 3], [1, '2', 3], [1, NaN, 3], [1, Infinity, 3]]) {
  assert.throws(() => assertVec3(value, 'synthetic'), /synthetic: expected three finite numbers/);
}
''', encoding='utf-8')
            run(['node', 'probe.cjs'], root)

    def test_node_outcomes_and_cancellation_preserve_child_and_wrapper_facts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = code_block(NODE, 'js', 'function outcomeOf(')
            (root / 'probe.mjs').write_text('''
import assert from 'node:assert/strict';
import { execFile } from 'node:child_process';
''' + source + '''
function execute(file, args, options = {}, afterStart = () => {}) {
  return new Promise((resolve) => {
    const child = execFile(file, args, { timeout: 5000, ...options }, (error, stdout) => {
      resolve({ outcome: outcomeOf(error), stdout });
    });
    child.stdin.end();
    afterStart(child);
  });
}
const node = process.execPath;
assert.deepEqual((await execute(node, ['-e', ''])).outcome, { kind: 'exited', status: 0 });
assert.deepEqual((await execute(node, ['-e', 'process.exitCode = 7'])).outcome,
  { kind: 'exited', status: 7 });
assert.deepEqual((await execute('./synthetic-missing-executable', [])).outcome,
  { kind: 'not_completed', reason: 'ENOENT' });
const eof = await execute(node, ['-e',
  "process.stdin.resume(); process.stdin.on('end', () => console.log('eof'));" ]);
assert.equal(eof.stdout.trim(), 'eof');
assert.deepEqual(eof.outcome, { kind: 'exited', status: 0 });
assert.deepEqual((await execute(node, ['-e', 'setInterval(() => {}, 1000)'],
  { timeout: 100 })).outcome, { kind: 'stopped', signal: 'SIGTERM' });
assert.deepEqual((await execute(node, ['-e', "console.log('x'.repeat(1000))"],
  { maxBuffer: 10 })).outcome, { kind: 'not_completed', reason: 'ERR_CHILD_PROCESS_STDIO_MAXBUFFER' });
const controller = new AbortController();
assert.deepEqual((await execute(node, ['-e',
  "console.log('ready'); setInterval(() => {}, 1000)"],
  { signal: controller.signal }, child => child.stdout.once('data', () => controller.abort()))).outcome,
  { kind: 'not_completed', reason: 'ABORT_ERR' });
let cancellation;
const graceful = await execute(node, ['-e',
  "process.on('SIGTERM', () => process.exit(0)); console.log('ready'); setInterval(() => {}, 1000)"],
  {}, child => child.stdout.once('data', () => { cancellation = 'cancelled'; child.kill(); }));
assert.deepEqual(graceful.outcome, { kind: 'exited', status: 0 });
assert.equal(cancellation, 'cancelled'); // The child outcome cannot undo the wrapper's decision.
const signaled = await execute(node, ['-e',
  "console.log('ready'); setInterval(() => {}, 1000)"], {},
  child => child.stdout.once('data', () => process.kill(child.pid, 'SIGKILL')));
assert.deepEqual(signaled.outcome, { kind: 'signaled', signal: 'SIGKILL' });
''', encoding='utf-8')
            run(['node', 'probe.mjs'], root)
