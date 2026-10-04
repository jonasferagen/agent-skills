# Verification foundation

Version: 0.1.1

Use this collection to choose evidence, author tests or review an existing suite.
Read the project's requirements and testing standard first. Install all members
together; select by the requested outcome rather than loading every test skill.

| Task | Guidance |
| --- | --- |
| Decide checks for an active change or milestone | [Verification design](skills/verification-design/SKILL.md) |
| Add or change tests, test helpers, fixtures or test inputs | [Test writing](skills/test-writing/SKILL.md); use verification design first if the required evidence is undecided |
| Audit a settled suite for weak evidence, brittleness or drift | [Test audit](skills/test-audit/SKILL.md) |
| Implement fixes discovered in a test audit | [Test writing](skills/test-writing/SKILL.md) for changed tests; [verification design](skills/verification-design/SKILL.md) for new evidence decisions |
| Install, update or check this collection | [Installation](references/installation.md) |

Adding a regression for an active fix does not automatically start a settled-suite
audit. Selecting evidence can end with a plan when test authoring was not requested.
A literal documentation correction does not require this collection unless the
project's existing checks require evidence. Preserve explicit project gates;
collection installation adds no universal coverage threshold or exhaustive suite.

Language and runtime mechanics retain their project routes. Missing implementation
or a test prerequisite remains an explicit evidence limit. Ordinary consumption
needs neither source-maintenance instructions nor the installation guide.
