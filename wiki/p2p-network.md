# Peer-to-peer networks and nodes

## In one sentence
Instead of one bank's server, a crypto network is many independent computers (nodes) that each keep a copy of the ledger and check each other's work [S2][S5].

## Key ideas
- **Peer-to-peer (P2P)** means the two parties transact directly, with no financial institution in between [S1].
- **Nodes** are the computers in the network. They must agree on each new block so that everyone has the same data [S2].
- In traditional payments a trusted intermediary validates transactions. In crypto, "a distributed network of nodes validates transactions and records them on a shared blockchain ledger" [S5].
- How a Bitcoin payment spreads through the network, in 6 steps [S1]:
  1. The new transaction is broadcast to all nodes.
  2. Nodes collect transactions into a block.
  3. Nodes work on the proof-of-work for that block (see [[consensus]]).
  4. The node that finds it broadcasts the block.
  5. Other nodes accept the block only if all of its transactions are valid and not already spent.
  6. Nodes show they accept it by building the next block on top of it.
- Nodes always treat the longest chain as the correct one. If two blocks appear at once, the tie breaks when the next block arrives [S1].
- Light users do not need the full chain. They can keep only block headers and verify their own payment (Simplified Payment Verification) [S1].

## Beginner analogy (AI-written, not from a source)
It's like a group chat where every member keeps a full copy of the message history. If one person edits their copy, everyone else's copies disagree, so the fake version gets ignored.

## Related
[[blockchain-basics]] · [[consensus]] · [[bitcoin]]

## Sources
S1, S2, S5
