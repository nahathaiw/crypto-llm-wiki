"""Render wiki/*.md + raw/*.md into one browsable HTML page (wiki-site.html)."""
import re, pathlib, html, markdown
root = pathlib.Path(__file__).parent
order = ['index','why-crypto','blockchain-basics','p2p-network','consensus','bitcoin','wallets-and-keys','ethereum','stablecoins','exchanges-and-price','risks-and-future','log']
def md(t):
    t = re.sub(r'\[\[([^\]]+)\]\]', r'<a class="wl" href="#\1">\1</a>', t)
    t = re.sub(r'\[(S\d+)\]', r'<a class="st" href="#src-\1">\1</a>', t)
    t = re.sub(r'(?m)^(\| [^|]*\| )(\w[\w-]*)( \|)', lambda m: m.group(0), t)
    t = re.sub(r'\(opinion[^)]*\)', lambda m: f'<span class="op">{m.group(0)}</span>', t)
    return markdown.markdown(t, extensions=['tables'])
nav, secs = [], []
for name in order:
    text = (root/'wiki'/f'{name}.md').read_text()
    title = text.split('\n')[0].lstrip('# ').strip()
    nav.append(f'<a href="#{name}">{html.escape(title)}</a>')
    secs.append(f'<article id="{name}"><p class="pid">wiki/{name}.md</p>{md(text)}</article>')
srcs = []
for p in sorted((root/'raw').glob('S*.md')):
    t = p.read_text(); fm, body = t.split('---',2)[1], t.split('---',2)[2]
    sid = re.search(r'id: (S\d+)', fm).group(1)
    meta = ''.join(f'<div><b>{html.escape(k)}</b> {html.escape(v.strip().strip(chr(34)))}</div>' for k,v in re.findall(r'(\w+): (.*)', fm))
    srcs.append(f'<article id="src-{sid}"><p class="pid">raw/{p.name}</p><h2>{sid}</h2><div class="meta">{meta}</div>{markdown.markdown(body)}</article>')
nav.append('<a href="#sources">Raw sources S1–S7</a>')
tpl = (root/'wiki_template.html').read_text()
out = tpl.replace('{{NAV}}', '\n'.join(nav)).replace('{{PAGES}}', '\n'.join(secs)).replace('{{SOURCES}}', '\n'.join(srcs))
head = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n<style>[hidden]{display:none!important}</style>\n'
i = out.index('</style>') + len('</style>')
out = head + out[:i] + '\n</head><body>' + out[i:].replace('<header><h1>', '<header><p style="margin:0 0 8px;font:13px var(--mono)"><a href="../">← Project home</a> · <a href="../slides/">Teaching slides</a></p><h1>', 1) + '\n</body></html>'
(root/'wiki/index.html').write_text(out); print('wrote wiki-site.html', len(out))
