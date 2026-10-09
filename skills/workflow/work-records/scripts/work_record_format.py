#!/usr/bin/env python3
"""Parse the opt-in work-record/v1 metadata block; unselected records are not parsed."""
import datetime
import re

SELECTOR = re.compile(r'^Record format: work-record/(?P<version>\S+)$', re.MULTILINE)
SUPPORTED = 'v1'
IDENTITY = re.compile(
    r'^(?P<field>Record|Brief) ID: `(?P<identifier>[a-z0-9]+(?:-[a-z0-9]+)*)`'
    r' · Revision: (?P<revision>[1-9][0-9]*)'
    r' · Date: (?P<date>\d{4}-\d{2}-\d{2})$')
KIND = ('concept', 'experience', 'experiment', 'integration', 'assessment')
WORKFLOW = ('draft', 'ready', 'in-progress', 'in-review', 'done', 'parked')
# Declared order after the identity line; preserve compatibility with existing records.
OPTIONAL = {'Kind': KIND, 'Workflow': WORKFLOW, 'Worklog': None}
ORDER = ('Kind', 'Workflow', 'Owner', 'Status', 'Worklog')
REQUIRED = ('Owner', 'Status')
LINK = re.compile(r'^\[[^\]]+\]\([^)\s]+\)$')


class RecordError(ValueError):
    """A selected record does not satisfy work-record/v1."""


def selects(text: str) -> bool:
    """Report whether this document opts into the format, at any supported or future version."""
    return SELECTOR.search(text) is not None


def parse_record(text: str) -> dict:
    """Return the metadata of a selected record, or raise RecordError."""
    selected = SELECTOR.search(text)
    if selected is None:
        raise RecordError('not a selected work record')
    if selected.group('version') != SUPPORTED:
        raise RecordError(f'unsupported record format version: work-record/{selected.group("version")}')

    lines = text.splitlines()
    heading = next((index for index, line in enumerate(lines) if line.startswith('# ')), None)
    if heading is None:
        raise RecordError('missing a level-one title before the format line')
    marker = text[:selected.start()].count('\n')
    if marker != heading + 2 or lines[heading + 1].strip():
        raise RecordError('the format line must follow the title after one blank line')
    if marker + 1 >= len(lines) or lines[marker + 1].strip():
        raise RecordError('the metadata block must follow the format line after one blank line')

    block = []
    for line in lines[marker + 2:]:
        if not line.strip():
            break
        block.append(line)
    if not block:
        raise RecordError('missing the metadata block')

    if any('{{' in line for line in block):
        raise RecordError('unfilled template placeholder in the metadata block')

    identity = IDENTITY.match(block[0])
    if identity is None:
        raise RecordError('malformed identity line: expected "Record ID: `id` · Revision: N · Date: YYYY-MM-DD"')
    try:
        datetime.date.fromisoformat(identity.group('date'))
    except ValueError:
        raise RecordError(f'not a real calendar date: {identity.group("date")}') from None

    fields, seen = {}, []
    for line in block[1:]:
        name, separator, value = line.partition(': ')
        if not separator or name not in ORDER:
            raise RecordError(f'unexpected metadata line: {line}')
        if name in fields:
            raise RecordError(f'duplicate metadata field: {name}')
        if not value.strip():
            raise RecordError(f'empty metadata field: {name}')
        allowed = OPTIONAL.get(name)
        if allowed is not None and value not in allowed:
            raise RecordError(f'{name} must be one of {", ".join(allowed)}; found {value}')
        if name == 'Worklog' and not LINK.match(value):
            raise RecordError('Worklog must be a single Markdown link')
        fields[name] = value
        seen.append(name)

    missing = [name for name in REQUIRED if name not in fields]
    if missing:
        raise RecordError(f'missing required field(s): {", ".join(missing)}')
    expected = [name for name in ORDER if name in fields]
    if seen != expected:
        raise RecordError(f'metadata fields out of order: expected {", ".join(expected)}')

    return {'identifier': identity.group('identifier'), 'identity_field': identity.group('field'),
            'revision': int(identity.group('revision')), 'date': identity.group('date'), **fields}
