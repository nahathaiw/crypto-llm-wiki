---
id: S2
title: "Technical intro to Ethereum"
publisher: ethereum.org
date: not shown
url: https://ethereum.org/developers/docs/intro-to-ethereum.md
fetched: 2026-11-23 (web-fetch, full page)
added_by: Claude (proposed)
type: official documentation
---
## Notes
- Blockchain = a public database updated and shared across many computers. "Block": data stored in consecutive groups; a tx succeeds only once added to a block. "Chain": each block cryptographically references its parent; changing a block requires changing all later blocks and network consensus.
- Nodes must agree on each new block → consensus mechanism needed.
- Ethereum uses proof-of-stake: block producers stake ETH as collateral and run validator software; validators are randomly selected to propose blocks; others check; rewards and penalties encourage honesty.
- Ethereum = "a blockchain with a computer embedded in it": a single canonical computer, the EVM; every node keeps its state.
- ETH is the native cryptocurrency; requests pay an ETH fee ("bounty"), part burned, rest to the worker; scales with resources; prevents spam. ETH also secures the network (rewards, slashable collateral, vote weight). (Page does not use the word "gas".)
- Smart contracts: reusable programs uploaded to the EVM, called with parameters; "like a sort of vending machine". Anyone can publish/call for a fee. Apps on them = dapps (marketplaces, financial instruments, games).
- Accounts hold ETH; a transaction = a fulfilled request + its state change.
## Quotes
- "A blockchain is a public database that is updated and shared across many computers in a network."
- "The data in a block cannot change without changing all subsequent blocks"
- "Ethereum is a blockchain with a computer embedded in it."
- "you can think of a smart contract like a sort of vending machine"
