"""Run the `outcomeOf` example from SKILL.md against real child processes.

Prerequisites: Python 3.11 or later and a `node` executable on PATH. The
behaviors were reproduced on Node 24 on Linux; the test fails explicitly, rather
than skipping, when `node` is absent. It needs nothing outside this package.
"""

from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest


PACKAGE = Path(__file__).resolve().parents[1]
SKILL = PACKAGE / 'SKILL.md'


def code_block(page: Path, language: str, containing: str) -> str:
    blocks = re.findall(rf'^```{language}\n(.*?)^```$', page.read_text(encoding='utf-8'), re.M | re.S)
    matches = [block for block in blocks if containing in block]
    if len(matches) != 1:
        raise ValueError(f'{page}: expected one {language} example containing {containing!r}, found {len(matches)}')
    return matches[0]


class OutcomeExample(unittest.TestCase):
    def test_outcomes_and_cancellation_preserve_child_and_wrapper_facts(self):
        node = shutil.which('node')
        self.assertIsNotNone(node, 'node is required on PATH to run the node-patterns example check')
        source = code_block(SKILL, 'js', 'function outcomeOf(')
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
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
            result = subprocess.run([node, 'probe.mjs'], cwd=root, stdin=subprocess.DEVNULL,
                                    capture_output=True, text=True, encoding='utf-8', timeout=30)
            self.assertEqual(result.returncode, 0,
                             f'node failed ({result.returncode}):\n{result.stdout}\n{result.stderr}')


if __name__ == '__main__':
    unittest.main()
