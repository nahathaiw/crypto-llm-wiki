# Blockchain basics: blocks, hashes, the chain

## In one sentence
A blockchain is a public database that is shared and updated across many computers, where data is grouped into blocks and each block points to the one before it [S2][S5].

## Key ideas
- **Block:** a group of recent transactions. A transaction only counts once it has been added to a block [S2].
- **Hash:** a short fingerprint of data. Publishing the hash of a block proves the data existed at that time [S1].
- **Chain:** each block includes the hash of the previous block, so the blocks link together like a chain [S1][S2].
- Changing one old block would change its hash, which breaks every block after it. "The data in a block cannot change without changing all subsequent blocks" [S2].
- Thousands of copies of the ledger are kept on computers around the world, which makes it extremely hard to alter [S5].
- Bitcoin adds a new block roughly every 10 minutes. Other coins have different block times [S5].
- On Ethereum, blocks generally hold dozens to hundreds of transactions [S2].

## Beginner analogy (AI-written, not from a source)
Think of a stack of numbered receipts where each receipt has the previous receipt's fingerprint printed on it. If you change receipt #3, its fingerprint changes, and receipts #4, #5, #6... no longer match.

## Related
[[why-crypto]] · [[p2p-network]] · [[consensus]]

## Sources
S1, S2, S5
