"""Every package the selection scenarios name exists in the catalog, or is `none`."""

from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCENARIOS = Path(__file__).resolve().parent / 'selection-scenarios.md'
ROW = re.compile(r'^\| (?P<request>[^|]+) \| (?P<select>[^|]+) \| (?P<avoid>[^|]+) \|$')


def rows(page: Path) -> list[dict[str, str]]:
    found = []
    for line in page.read_text(encoding='utf-8').splitlines():
        match = ROW.match(line)
        if match and match.group('request') not in ('Request', '---'):
            found.append({key: value.strip() for key, value in match.groupdict().items()})
    return found


def names(cell: str) -> list[str]:
    return [name.strip() for name in cell.split(',') if name.strip() and name.strip() != 'none']


class SelectionScenarioTests(unittest.TestCase):
    def setUp(self):
        self.packages = {path.parent.name for path in (ROOT / 'skills').rglob('SKILL.md')}
        self.rows = rows(SCENARIOS)

    def test_scenarios_exist_and_are_complete(self):
        self.assertGreater(len(self.rows), 0)
        for row in self.rows:
            with self.subTest(request=row['request']):
                self.assertTrue(row['select'] and row['avoid'], 'both selection columns are filled')
                self.assertTrue(names(row['avoid']), 'every case names a neighbour that should not be selected')

    def test_every_named_package_is_in_the_catalog(self):
        for row in self.rows:
            for name in names(row['select']) + names(row['avoid']):
                with self.subTest(request=row['request'], package=name):
                    self.assertIn(name, self.packages)

    def test_a_package_is_not_both_selected_and_avoided(self):
        for row in self.rows:
            with self.subTest(request=row['request']):
                self.assertFalse(set(names(row['select'])) & set(names(row['avoid'])))


if __name__ == '__main__':
    unittest.main()
