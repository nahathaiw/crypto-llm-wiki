# Real run record — 2026-11-23 (Taipei)

This is one complete run of the graph. The AI doing each step was Claude. Every result below was observed, and the raw outputs are in this folder.

| # | Node | Result | Evidence |
|---|---|---|---|
| 1 | Discuss | Pure chose the topic, confirmed the audience, added 4 subtopics, gave 4 links | thread messages 14:26, 14:48 |
| 2 | Fetch (direct curl) | **FAILED** for all 11 URLs: the sandbox proxy refused the connection (HTTP 403) | switched to the web-fetch tool |
| 3 | Fetch (web-fetch) | 7/8 OK; **Investopedia FAILED** (site blocked) | raw/S1–S7 |
| 4 | Ingest check | **Flagged** the GWI "nearly $5 billion by 2030" claim as inconsistent with ethereum.org's USDT ≈ $175B; labeled the Avalanche blog as opinion; noted GWI's missing date | raw/S6, raw/S7 |
| 5 | Generate wiki | 9 pages + index + log | wiki/ |
| 6 | Lint run 1 | PASS (0). The lint script was first tested on a corrupted copy: it caught all planted errors | lint-run1.txt |
| 7 | Grounding check run 1 | **3 problems**: overclaim ("most people"), a term not in the source ("slashed"), a fact hidden in an AI analogy (private keys) → all fixed | grounding-check-run1.md |
| 8 | Lint run 2 | PASS | lint-run2.txt |
| 9 | Generate slides | 15 slides | slides/ |
| 10 | Slide check run 1 | **4 FAILs**: 2 slides with no source tags (roadmap, quiz); 2 FAILs on slide 7 caused by a **bug in the checker itself** (its regex dropped the "2" in `p2p-network`) | slide-check-run1.txt |
| 11 | Slide claim review | **2 problems**: a slide said "a changed copy stands out right away" (not in the wiki); the PoS row "votes weighted by staked ETH" was in raw S2 but **missing from the wiki** → added it to the wiki first (loop back to node 5), then kept the slide | — |
| 12 | Lint run 3 + slide check run 2 | PASS / PASS | lint-run3.txt, slide-check-run2.txt |
| 13 | Render check | Desktop OK; **phone: footer overlapped the content** → CSS fix → re-check OK (long slides scroll inside the card) | Playwright screenshots |
| 14 | Publish | wiki + slides published | links in submission.md |

Counts by node: generation nodes (wiki + slides) produced 5 content errors (3 + 2), the slide footer step produced 2 missing-tag errors, the fetch node failed twice, the checker had 1 bug, and the render node had 1 layout bug.

# Run 2 — 2026-11-23 16:04–16:20 (adding one source to fill the wallets/keys gap)

| # | Node | Result | Evidence |
|---|---|---|---|
| 1 | Discuss | Pure asked for more sources; Claude pointed out the wallets/keys gap found in run 1; Pure gave an Investopedia link | thread 16:03–16:04 |
| 2 | Fetch | **Investopedia FAILED again** (the site is known to be blocked) → Pure picked CoinDesk from 3 alternatives → OK | raw/S8 |
| 3 | Ingest check (now includes a grounding check) | **Flagged** S8's "public key encrypts transactions": it conflicts with S1 (transactions are signed, not encrypted). Marked ⚠ DO NOT USE *before* generation | raw/S8 |
| 4 | Generate wiki | New page `wallets-and-keys`; the gap note in `bitcoin` was replaced with a link | wiki/ |
| 5 | Lint run 4 | PASS | lint-run4.txt |
| 6 | Grounding check run 2 | **1 problem**: "Not your keys" was quoted as if S8 said it, but the phrase isn't clearly on the page → rewritten | wiki/log.md |
| 7 | Lint run 5 + slide check run 3 | PASS / PASS (16 slides) | lint-run5.txt, slide-check-run3.txt |
| 8 | Render check | Desktop: all 16 OK. Phone: long slides scroll inside the card, with no overlap | Playwright |
| 9 | Publish | both links updated in place | — |

Compared with run 1: generation produced 1 content error (run 1 had 3 on the wiki). One wrong claim was stopped at ingest instead of reaching the wiki.
