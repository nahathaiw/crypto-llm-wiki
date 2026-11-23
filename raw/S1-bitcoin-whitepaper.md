---
id: S1
title: "Bitcoin: A Peer-to-Peer Electronic Cash System"
author: Satoshi Nakamoto
date: 2008 (paper says "as of 2008")
url: https://courses.csail.mit.edu/6.857/2015/files/L07-nakamoto-bitcoin-a-peer-to-peer-electronic-cash-system.pdf
fetched: 2026-11-23 (web-fetch, full PDF text)
added_by: Claude (proposed), Pure approved source list
type: primary source
---
## Notes (paraphrased by section)
- Abstract: P2P electronic payments without a financial institution; double-spending solved by timestamping transactions into a chain of hash-based proof-of-work; secure while honest nodes control most CPU power.
- §1: Online payments rely on trusted third parties (financial institutions). Reversible payments need mediation → higher costs, no small payments, merchants wary. Goal: cryptographic proof instead of trust, so two parties transact directly.
- §2: A coin is a chain of digital signatures: each owner signs a hash of the previous transaction + next owner's public key. Payee can't tell if an earlier owner double-spent; a central mint could check but then everything depends on it. Fix: announce transactions publicly and agree on one order; earliest counts.
- §3: Timestamp server: hash a block of items and publish; each timestamp includes the previous hash, forming a chain.
- §4: Proof-of-work (like Hashcash): find a nonce so SHA-256 hash starts with N zero bits; hard to find, one hash to verify. Changing a block means redoing it and all later blocks. "One-CPU-one-vote"; longest chain = most work. Difficulty adjusts to target a set number of blocks per hour.
- §5 Network steps: broadcast tx → nodes collect into block → find PoW → broadcast block → accept only if all tx valid and unspent → build next block on its hash. Longest chain is correct; ties break when next block arrives.
- §6 Incentive: first tx in a block creates new coins for the block creator; plus transaction fees. Greedy attacker earns more by following rules.
- §7–9: Merkle tree pruning; header ~80 bytes, ~4.2 MB/year at 1 block / 10 min; SPV light clients; tx have multiple inputs/outputs (payment + change).
- §10 Privacy: public keys are anonymous; public sees amounts moving between keys, not identities. New key pair per tx.
- §11: Attacker can only try to reverse his own recent spend; cannot create value or steal. Catch-up probability drops exponentially with confirmations z (e.g. q=0.10 → z=5 for P<0.1%).
## Quotes
- §1 "What is needed is an electronic payment system based on cryptographic proof instead of trust"
- §2 "We define an electronic coin as a chain of digital signatures."
- §4 "Proof-of-work is essentially one-CPU-one-vote."
- §5 "Nodes always consider the longest chain to be the correct one and will keep working on extending it."
- §11 "An attacker can only try to change one of his own transactions to take back money he recently spent."
