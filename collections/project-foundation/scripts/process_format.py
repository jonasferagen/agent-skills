"""Parse the opt-in project-process/v1 Markdown contract; no runtime execution."""
import re

VERSION = 'project-process/v1'
ROLES = {'purpose', 'participants', 'stages', 'interruptions', 'handoffs', 'evidence'}
FACTS = ('Reader question', 'Trigger', 'Owner', 'Inputs', 'Completion')
STEPS = ('Step', 'Action', 'Owner', 'Input', 'Result / condition', 'Detail')
HANDOFFS = ('Handoff', 'From', 'To', 'Result', 'Kind', 'Detail')
KINDS = {'transfer', 'feedback', 'specialization'}
KEY = re.compile(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*\Z')
LINK = re.compile(r'\[[^\]\n]+\]\(([^\s)]+)\)')


def _visible_lines(text):
    """Retain source positions but ignore fenced examples and multiline comments."""
    lines, fence, comment = [], None, False
    for raw in text.splitlines():
        stripped = raw.strip()
        match = re.match(r'^(`{3,}|~{3,})', stripped)
        if fence:
            lines.append('')
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not stripped[len(match[1]):].strip():
                fence = None
            continue
        if match and not comment:
            fence = match[1]
            lines.append('')
            continue
        if comment:
            lines.append('')
            if '-->' in stripped:
                comment = False
            continue
        if '<!--' in stripped and not re.fullmatch(r'<!-- process-section: [a-z-]+ -->', stripped):
            comment = '-->' not in stripped
            lines.append('')
            continue
        lines.append(raw)
    return lines


def _cells(line):
    return [cell.strip().replace(r'\|', '|') for cell in re.split(r'(?<!\\)\|', line.strip().strip('|'))]


def _table(lines, start, stop, columns, label):
    matches = [i for i in range(start, stop) if lines[i].strip().startswith('|') and tuple(_cells(lines[i])) == columns]
    if len(matches) != 1:
        raise ValueError(f'{label}: expected exactly one table with columns {" | ".join(columns)}')
    index = matches[0]
    if index + 1 >= stop or len(_cells(lines[index + 1])) != len(columns) or not all(re.fullmatch(r':?-{3,}:?', cell) for cell in _cells(lines[index + 1])):
        raise ValueError(f'line {index + 2}: {label} needs a Markdown table separator')
    rows = []
    for i in range(index + 2, stop):
        if not lines[i].strip().startswith('|'):
            break
        cells = _cells(lines[i])
        if len(cells) != len(columns) or any(not cell or '{{' in cell for cell in cells):
            raise ValueError(f'line {i + 1}: {label} needs {len(columns)} populated cells; state an unknown explicitly')
        rows.append({'line': i + 1, 'cells': cells})
    if not rows:
        raise ValueError(f'{label}: table needs at least one row')
    return rows


def parse_process(text):
    """Return source-located facts/roles/steps/handoffs, or None for legacy prose.

    Raise ValueError for malformed selected input. Links are explicit destinations;
    the consumer resolves them using its own document roots and anchor convention.
    """
    lines = _visible_lines(text)
    versions = [(i + 1, line.strip().removeprefix('Process format: ')) for i, line in enumerate(lines) if line.strip().startswith('Process format:')]
    markers = [(i, re.fullmatch(r'<!-- process-section: ([a-z-]+) -->', line.strip())) for i, line in enumerate(lines) if 'process-section:' in line]
    if not versions and not markers:
        return None
    if len(versions) != 1 or versions[0][1] != VERSION:
        raise ValueError(f'Process format: expected exactly one {VERSION} declaration')
    roles = {}
    for i, match in markers:
        if not match or match[1] not in ROLES:
            raise ValueError(f'line {i + 1}: unsupported process-section marker')
        role = match[1]
        if role in roles:
            raise ValueError(f'line {i + 1}: duplicate process-section {role}')
        heading = i + 1
        while heading < len(lines) and not lines[heading].strip():
            heading += 1
        title = re.fullmatch(r'(#{2,6})\s+(.+?)\s*#*', lines[heading]) if heading < len(lines) else None
        if not title:
            raise ValueError(f'line {i + 1}: process-section must precede an ATX heading')
        stop = heading + 1
        while stop < len(lines):
            next_heading = re.match(r'^(#{1,6})\s', lines[stop])
            if next_heading and len(next_heading[1]) <= len(title[1]):
                break
            stop += 1
        roles[role] = {'line': heading + 1, 'title': title[2], 'start': heading + 1, 'stop': stop}
    missing = {'purpose', 'stages'} - roles.keys()
    if missing:
        raise ValueError(f'missing process-section: {", ".join(sorted(missing))}')
    purpose = roles['purpose']
    facts = _table(lines, purpose['start'], purpose['stop'], ('Fact', 'Value'), 'process facts')
    if [row['cells'][0] for row in facts] != list(FACTS):
        raise ValueError(f'process facts: use exactly these ordered keys: {", ".join(FACTS)}')
    stages = roles['stages']
    steps = _table(lines, stages['start'], stages['stop'], STEPS, 'process steps')
    handoffs = []
    if 'handoffs' in roles:
        handoff = roles['handoffs']
        body = '\n'.join(lines[handoff['start']:handoff['stop']])
        if not re.search(r'^Handoffs: (?:None\.|Unknown\b.+)$', body, re.M):
            handoffs = _table(lines, handoff['start'], handoff['stop'], HANDOFFS, 'process handoffs')
    for label, rows in [('steps', steps), ('handoffs', handoffs)]:
        seen = set()
        for row in rows:
            key = row['cells'][0]
            if not KEY.fullmatch(key) or key in seen:
                raise ValueError(f'line {row["line"]}: {label} need unique stable lowercase hyphenated keys')
            seen.add(key)
            if not LINK.fullmatch(row['cells'][-1]):
                raise ValueError(f'line {row["line"]}: Detail needs one explicit Markdown link')
            if label == 'handoffs' and row['cells'][4] not in KINDS:
                raise ValueError(f'line {row["line"]}: unsupported handoff Kind; use transfer, feedback or specialization')
            row['key'] = key
            row['detail'] = LINK.fullmatch(row['cells'][-1])[1]
    return {'version': VERSION, 'roles': roles, 'facts': facts, 'steps': steps, 'handoffs': handoffs}
