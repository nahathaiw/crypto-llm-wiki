# Consensus: Proof of Work vs Proof of Stake

## In one sentence
A consensus mechanism is the rule that lets thousands of nodes that don't trust each other agree on which block comes next [S2].

## Key ideas
- Blockchains need a consensus mechanism to reach distributed agreement [S2].
- **Proof of Work (PoW, used by Bitcoin):** nodes search for a number (a nonce) that makes the block's SHA-256 hash start with enough zeros. This is hard to find but takes only one hash to check [S1].
- PoW is "essentially one-CPU-one-vote": influence depends on computing power, not on how many IP addresses you control [S1].
- To change an old block, an attacker would have to redo its work and the work of every later block. Their chance of catching up shrinks exponentially with each new block [S1].
- Bitcoin adjusts the difficulty so that blocks keep arriving at a steady rate [S1].
- Miners are rewarded with new coins plus transaction fees, which gives them a reason to stay honest [S1].
- **Proof of Stake (PoS, used by Ethereum):** validators lock up (stake) ETH as collateral. Validators are picked at random to propose blocks, and others check them [S2].
- In PoS, staked ETH also weights validators' votes when the network chooses between competing chains (fork choice) [S2].
- In PoS, honest validators are rewarded. The staked ETH is collateral that can be destroyed if a validator misbehaves [S2].
- **(opinion/observation)** GWI notes that Bitcoin mining has become concentrated in a few large companies with lots of computing power and electricity [S6].

## Beginner analogy (AI-written, not from a source)
PoW is a lottery where you buy tickets with electricity. PoS is a lottery where you buy tickets by putting down a deposit, and you lose the deposit if you cheat.

## Related
[[p2p-network]] · [[bitcoin]] · [[ethereum]]

## Sources
S1, S2, S6
