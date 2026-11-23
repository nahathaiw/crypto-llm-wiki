---
layout: default
title: "AGENTS.md"
---
# AGENTS.md — Rules for the Crypto Basics LLM Wiki

This wiki is written and maintained by an LLM, using the process "先討論、後生成" (discuss first, then generate).

## Folders
- `raw/` holds source notes, one file per source (`S#-slug.md`). There is YAML front matter with the URL, date, who added it, and the source type. Raw files are never edited after ingest, except to add ⚠ flags.
- `wiki/` holds concept pages, one concept per page, plus `index.md` (the catalog) and `log.md` (the history of each operation).
- `checks/` holds the lint and slide-check reports, one file per run.
- `slides/` holds the teaching HTML deck that is generated from the wiki.

## Page rules
1. Every factual sentence or bullet ends with a source tag such as `[S1]` or `[S2][S5]`. An untagged claim fails lint.
2. Opinions and predictions are marked with **(opinion)**, using a tag such as `[S7]`. They are never stated as facts.
3. Numbers keep their date or "as of" note. A number flagged ⚠ in raw/ is never used.
4. Links between pages use `[[page-name]]`, and every link must point to an existing page.
5. Every page has these sections: `## In one sentence`, `## Key ideas`, `## Beginner analogy` (marked as written by the AI and not taken from a source), `## Related`, `## Sources`.
6. The language is plain English for a classmate with no crypto background.

## Operations
- **Ingest:** fetch a source, write `raw/S#`, then update or create wiki pages and add a line to `log.md`.
- **Query:** answer questions or build the slide outline using wiki pages only, never outside knowledge.
- **Lint:** run `checks/lint.py`. It checks source tags, links, source ids, and ⚠ numbers.
- **Slide check:** every slide must list its wiki pages. Every claim on a slide must match a tagged claim on that page.
