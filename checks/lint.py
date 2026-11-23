"""Wiki lint: rule checks from AGENTS.md. Usage: python3 checks/lint.py <wiki_dir> <raw_dir>"""
import re, sys, pathlib
wiki, raw = map(pathlib.Path, sys.argv[1:3])
src_ids = {p.name.split('-')[0] for p in raw.glob('S*.md')}
flagged = []  # numbers flagged with ⚠ in raw
for p in raw.glob('S*.md'):
    for line in p.read_text().splitlines():
        if '⚠' in line:
            flagged += re.findall(r'\$\d[\d.,]*\s*(?:billion|trillion|B|T)?', line)
pages = {p.stem for p in wiki.glob('*.md')}
REQ = ['## In one sentence', '## Key ideas', '## Beginner analogy', '## Related', '## Sources']
problems = []
for p in sorted(wiki.glob('*.md')):
    if p.stem in ('index', 'log'):
        continue
    text = p.read_text()
    for h in REQ:
        if h not in text: problems.append((p.stem, 'missing section', h))
    for l in re.findall(r'\[\[([^\]]+)\]\]', text):
        if l not in pages: problems.append((p.stem, 'broken link', l))
    used = set(re.findall(r'\[(S\d+)\]', text))
    for s in used - src_ids: problems.append((p.stem, 'unknown source', s))
    listed = set(re.findall(r'S\d+', text.split('## Sources')[-1]))
    if used != listed: problems.append((p.stem, 'Sources section mismatch', f'used={sorted(used)} listed={sorted(listed)}'))
    # claims = bullets + one-sentence line in factual sections
    sec = re.split(r'\n## ', text)
    for block in sec:
        name = block.split('\n')[0]
        if name.startswith(('In one sentence', 'Key ideas')):
            for line in block.split('\n')[1:]:
                s = line.strip()
                if not s or s.startswith('#'): continue
                is_step = re.match(r'\d+\.', s)
                if not re.search(r'\[S\d+\]', s) and not is_step:
                    problems.append((p.stem, 'untagged claim', s[:70]))
    for f in flagged:
        if f.strip() and f.strip() in text: problems.append((p.stem, 'uses ⚠ flagged number', f))
print(f'pages checked: {len(pages)-2}, sources: {sorted(src_ids)}, flagged numbers: {flagged}')
for pr in problems: print('FAIL', *pr, sep=' | ')
print('RESULT:', 'PASS' if not problems else f'{len(problems)} problem(s)')
