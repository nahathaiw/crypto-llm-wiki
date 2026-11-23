---
layout: default
title: "README"
---
# Crypto Basics LLM Wiki → Teaching HTML Slides

Generative AI course homework: build an LLM Wiki on my own topic, then use it as the only knowledge source for a teaching HTML slide deck.

- **Live site:** https://nahathaiw.github.io/crypto-llm-wiki/
- **Slides:** https://nahathaiw.github.io/crypto-llm-wiki/slides/
- **Wiki:** https://nahathaiw.github.io/crypto-llm-wiki/wiki/

## What's in here
| Path | What it is |
|---|---|
| `AGENTS.md` | Rules the LLM follows to maintain the wiki: folders, page format, source tags, operations |
| `raw/S1–S8` | Ingested source notes (paraphrase + short quotes, with URL and date) |
| `wiki/*.md` | 10 concept pages + `index.md` + `log.md` (operation history) |
| `wiki/index.html` | Browsable wiki, built by `build_wiki_html.py` |
| `slides/index.html` | 16-slide teaching deck. Each footer links to its wiki page and sources |
| `loop-design.md` | Loop/graph design: diagram, which steps repeat, where checks happen, why |
| `checks/` | `lint.py`, `slide_check.py`, outputs of every run, `run-record.md` |

## Loop in one line
Discuss → fetch → ingest check → raw note (×N) → generate wiki → lint + grounding check (loop back) → query wiki → generate slides → slide check (back to slides, or back to the wiki) → render check → publish.

## Reproduce the checks
```bash
python3 checks/lint.py wiki raw
python3 checks/slide_check.py slides/index.html wiki
pip install markdown && python3 build_wiki_html.py   # rebuilds wiki-site.html from wiki/ + raw/
```

## AI use
The wiki text, slides, scripts and site were generated with Claude (Anthropic) during a guided session. I chose the topic, the audience and the extra subtopics (stablecoins, price/exchanges, P2P, why crypto), and I gave 4 of the source links plus the wallets/keys source choice. Every check result in `checks/` is from a real run.
