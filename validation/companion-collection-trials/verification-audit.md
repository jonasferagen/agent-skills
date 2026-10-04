# Settled-suite audit

The suite provides only a narrow smoke check: `capped(20)` returns something other than `None` without raising. It does not supply useful evidence that the function caps its result at 10. The original suite passes, and two intentionally incorrect replacements also pass.

## Findings

1. **Quick win — weak assertion** (`test_sample.py:6–7`). `assertIsNotNone(capped(20))` accepts 0, 20, strings, and other non-null values. The implementation in `sample.py:1–2` returns `min(value, 10)`, so the observed result for 20 is 10. An uncapped replacement returning 20 passed the complete selected suite; a constant-zero replacement passed too. The smallest useful fix is an exact assertion that `capped(20) == 10`, if that is the intended public contract. Test edits were not requested and were not made.

2. **Coverage gap — values at and below the cap** (`sample.py:1–2`, `test_sample.py:6–7`). The only exercised input is 20. Nothing checks that inputs below the cap retain their value or that 10 is accepted unchanged. Even a constant-10 implementation would satisfy the proposed above-cap assertion. A small follow-up should check a value below 10 and the boundary value 10, after confirming the numeric contract. Error handling and supported input types are unspecified by the local requirements; absence of such tests is an evidence limit, not a proven requirement violation.

## Source-to-test asymmetry and intentional thinness

| Public operation | Existing test | Evidence supplied | Missing behavioral evidence |
| --- | --- | --- | --- |
| `sample.capped(value)` | `ExampleTests.test_returns_something` | For input 20, no exception and a non-null result | Exact upper cap, preservation below cap, boundary behavior |

There are no other production operations or test files in the selected fixture. The smoke check has limited value as a smoke check; no local policy establishes intentional thin coverage for this function. The original test uses no mocks, network, clock, randomness, sleeps, or filesystem data. No focused-test marker or skip is present. There is no brittleness or determinism finding in this small suite. No production-contract smell was established, and no stale prose was repaired.

## Execution and limits

- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -v`: exit 0; the complete discovered fixture suite ran 1 test and passed. Unittest reported `0.000s`, which is its rounded timing, not a benchmark. No coverage tool ran and no coverage percentage is claimed.
- A separate Python process loaded the same unittest suite and temporarily substituted its imported `capped` binding using `unittest.mock.patch.object`. Both `lambda value: 0` and `lambda value: value` ran 1 test with 0 failures and 0 errors. This demonstrates assertion weakness; it does not constitute a production-code mutation or measure mutation coverage. No implementation or test file changed, and bytecode output was disabled.
- `GIT_CEILING_DIRECTORIES=/tmp/foundation-group-trials-bnwo1blg git status --short --untracked-files=all`: exit 128, reporting that the fixture is not a Git repository. No worktree was needed or created for this read-only audit plus requested report.
- `rg --files` and `rg --files --hidden` inventoried this fixture. Only its `AGENTS.md` instruction entry appeared. No repository test scanner was present in the inventory; the collection's installation checker is not a test scanner and was not run.
- Initial login-shell commands emitted `Failed to create stream fd: Operation not permitted` warnings, but completed with exit 0 and supplied their requested output. Subsequent commands used a non-login shell. No dependency installation, network, live service, other fixture, or source repository was accessed.
- A final Python file check confirmed that `result.md` exists and that both source files still match their initially inspected contents; exit 0. That check reread the source files without redisplaying them.

## Instruction reads and cost

Paths are relative to `/tmp/foundation-group-trials-bnwo1blg/verification-audit`. Approximate word counts use whitespace splitting; each file is counted once toward unique instruction volume.

| Read path | Approximate words | Relevance | Content reads | Additional reads |
| --- | ---: | --- | ---: | --- |
| `AGENTS.md` | 26 | Routes verification and settled-suite review to the collection | 1 | 1 programmatic count pass |
| `project.md` | 51 | Local-only scope, no installation/services, Python unittest standard | 1 | 1 programmatic count pass |
| `.agents/collections/verification-foundation/COLLECTION.md` | 222 | Selects test audit rather than active-change design or test writing | 1 | 1 programmatic count pass |
| `.agents/collections/verification-foundation/skills/test-audit/SKILL.md` | 989 | Focused audit workflow, assertion strength, classifications and reporting | 1 | 1 programmatic count pass |
| `README.md` | 7 | Context only; no testing requirements or behavioral contract | 1 | 1 programmatic count pass |

Unique instruction volume is approximately 1,288 words, or 1,295 including README context. The counting script reread all five files once without displaying their contents; there were no repeated content displays or retries. All content outputs were complete and untruncated. `sample.py` and `test_sample.py` were displayed once each; subsequent test execution necessarily loaded them. No audit references were opened because the headline assertion-strength and edge-case lenses resolved this focused case without a further judgment rule. Installation, test-writing and verification-design guidance was not loaded.

Only `result.md` was created.
