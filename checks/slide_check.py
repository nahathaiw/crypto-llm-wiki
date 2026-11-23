"""Slide traceability check. Usage: python3 checks/slide_check.py slides/x.html wiki/"""
import re, sys, pathlib
html = pathlib.Path(sys.argv[1]).read_text(); wiki = pathlib.Path(sys.argv[2])
slides = re.findall(r'<section class="slide" data-wiki="([^"]+)">(.*?)</section>', html, re.S)
probs = []
for n, (page, body) in enumerate(slides, 1):
    foot = re.sub(r'<a [^>]*>|</a>', '', re.search(r'<div class="foot">(.*?)</div>', body, re.S).group(1))
    pages = re.findall(r'[a-z][a-z0-9-]+', re.search(r'Wiki: (.*?)</span>', foot).group(1).replace('<b>', ' ').replace('</b>', ' '))
    tags = set()
    for a, b in re.findall(r'S(\d)(?:–S(\d))?', re.search(r'<div class="foot">(.*?)</div>', body, re.S).group(1)):
        tags |= {f'S{k}' for k in range(int(a), int(b or a) + 1)}
    allowed = set()
    for p in pages:
        f = wiki / f'{p}.md'
        if not f.exists(): probs.append((n, 'wiki page missing', p)); continue
        allowed |= set(re.findall(r'S\d+', f.read_text()))
    if not tags: probs.append((n, 'no source tags in footer', ''))
    extra = tags - allowed
    if extra: probs.append((n, 'footer cites source not on its wiki page', sorted(extra)))
    if '$5 billion' in body: probs.append((n, 'uses ⚠ flagged number', '$5 billion'))
print(f'slides checked: {len(slides)}')
for p in probs: print('FAIL', *p, sep=' | ')
print('RESULT:', 'PASS' if not probs else f'{len(probs)} problem(s)')
