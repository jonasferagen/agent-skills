# Fixtures

A fixture is any input a test supplies: a value, a record, a message, a file,
a directory tree, rows in a database, and the helpers that build them.

## Make up every value

Do not copy a value from real data into a test. Real data means production
records, customer and personal records, a local corpus, logs, and the output
of any tool you just ran over those.

This needs saying because of how the mistake happens. A test about a kind of
value, such as a phone number that must not be read as an invoice number,
wants an example of that kind. The nearest example is the real one on the
screen. A test file is tracked and shared even when the directory that holds
the data is ignored, so the copied value leaves its protected home through a
file that no ignore rule covers. It then stays in history after the file is
corrected.

When the shape of a real value matters, make up a value with that shape.
Start from nothing: a value made by trimming a real one, or by changing one
digit, still carries it. So does a file name or an address built around a real
name.

- Keep what the code under test looks at: the length, the character classes,
  the separators, and a valid check digit if the code verifies one.
- Make it visibly artificial where the rule allows: repeated or counting
  digits, a name such as "Example Person".
- Use a range reserved for examples where one exists: the domains
  `example.com`, `.test` and `.invalid`, the address blocks `192.0.2.0/24`
  and `2001:db8::/32`, and the fictional number ranges that some telephone
  numbering plans set aside.
- Keep made-up values consistent with each other where a relationship
  matters, such as two records that share an identifier.

| The real record holds | The fixture holds |
| --- | --- |
| A customer's phone number | Digits of the same length that are plainly not a number in use, such as `00000000` |
| An identity number with a birth date in it | The same length with no real date in it, such as `00000000000` |
| An invoice number the code must find | A number of that format that you chose, such as `INV-1234567` |
| A person's name and address | `Example Person`, `1 Example Street` |
| A mailbox | `someone@example.test` |

A made-up value can still match real data by chance. If the check below
reports one, change the made-up value; do not allow it.

The rule covers everything a test writes down: test names, comments, assertion
messages, snapshots, recorded responses, and failure output that lands in a
log.

Not everything that looks like data is private. A code from a public standard,
or a product name from public documentation, can appear as it is. The project's
policy decides what counts as private. Where it does not say, treat anything
that identifies a person, an account, a contract or a payment as private, and
ask.

<!-- Package-boundary copy: source-of-truth/references/durable-checks.md (Fabricate the fixture) states the rule on building fixtures in a temporary location for a check's own tests. Keep both passages aligned. -->
## Keep fixtures small and inside the test

- Supply only the fields the behavior needs. Put defaults in a builder and the
  one value that matters in the test, so that the test shows what it is about.
- Make sure the builder can express absence: a missing field, an empty value,
  a malformed one. A helper that only builds valid input leaves every invalid
  path untested.
- Build files and directory trees in a temporary location during the test.
  Depend on nothing that happens to exist on the machine.
- Where the package that owns a type already offers a builder for it, use that
  builder instead of writing another.

## Stored fixture files

Store a fixture as a file only when it cannot reasonably be built in the test:
a binary format, a large document, a recorded exchange.

- Make it synthetic from the start. If it is derived from a real artifact,
  replace every field, and check the parts nobody reads: metadata, embedded
  attachments, headers, comments and author fields. Editing the visible values
  is not enough.
- Keep the smallest file that exercises the behavior.
- Put a note beside it: what it stands for, how it was produced, and that it is
  synthetic.
- For a response recorded from a real service, remove tokens, identifiers and
  personal data before storing it, and note its date and source. It pins what
  was observed, once.

<!-- Package-boundary copy: source-of-truth/references/durable-checks.md (the invariant computed live, and its note that a literal expectation is not a golden) states this rule for consistency checks. Keep both passages aligned. -->
## Prefer derived references to stored goldens

When a test needs the output of an earlier step as its input, or compares a
result with a known good one:

- derive the reference at test time from the real earlier step, when that step
  lives in the same repository, or
- validate a stored reference with the same contract check the producer is
  held to.

A stored golden that copies structural facts goes stale without failing, and
then gets approved again without review. A literal expectation is different.
The value an operation should return for a given input is a statement of the
requirement. Write it in the test.

## Real data as test input

Some tests run against real data on purpose: a local corpus, a sample of
production. Do this only where the project's policy allows it.

- Read the data from its untracked home at run time.
- Skip visibly, with the reason, when it is absent. A run without it is
  partial.
- Assert only what is safe to write down: counts, states, public or made-up
  identifiers. Keep private values out of the assertion, the test name and the
  output.
- Write anything computed from the data to a temporary or untracked location.

## Guard the rule with a check

A rule that depends on every author remembering it gets broken. A check that
fails does not depend on anyone's memory. So where a policy keeps private data
out of tracked files and the data is at hand, give the project a check. The
bundled [copiedValues.py](../scripts/copiedValues.py) is one:

- At run time it collects numbers of six or more digits and mail addresses
  from every file of the private data, including the text inside database
  files. A number made of one repeated digit identifies nothing and is left
  out.
- It searches the files Git tracks, and those it would track, for them, for
  numbers that contain a private number or are contained in one, and for the
  names you list.
- It reports the file, the line and the kind of value, never the value.
- Only exit status 0 is a pass. Status 1 means copied values were found, 2
  that none of the private paths exists, and 3 that the check could not run.

Run it before you report work that touched tests or fixtures, as step 6 of
the [workflow](../SKILL.md#workflow) says. Better, have one test in the
project's own suite run it over every tracked file. Let that test look for
the private data itself, and skip with the reason only when the data is
absent. Fail on every other status than 0: a broken check that skips reports
success for files it never read. A run with copied values then fails for
whoever made them, whether or not they read this skill.

A value the project has decided may be public, such as an identifier its
documentation uses on purpose, goes in an allow file that the project owns,
passed with `--allow-file`. Do not add a value there to make a finding go
away. Names go in a file kept with the private data, passed with
`--term-file`. A test that lists them itself puts them in a tracked file.

The helper does not see free text, a name you did not list, a name inside a
file name, a number written in groups such as `555 01 000`, a number with one
digit changed, a number a database stores in binary, or text inside an
encoded mail part. Read fixtures for those.
A scan for shapes, such as anything that looks like a phone number, is a
useful advisory signal. It cannot tell a made-up value from a real one, so do
not let it fail a build.

If a private value has already been committed, replacing it in the working
tree does not remove it from history. Report it. The project's policy decides
whether history is rewritten or a secret is rotated.
