# Wiki grounding check — run 1 (2026-11-23, ~15:25 Taipei)

What this check does: an LLM (Claude) reads each tagged claim in wiki/ and compares it with the raw/ note for the source in its tag. This catches things the structural lint can't see, because a claim can have a valid tag and still say more than the source does.

| Page | Claim (before) | Problem | Fix |
|---|---|---|---|
| exchanges-and-price | "Most people get crypto by buying it on an exchange [S5]" | **Overclaim.** S5 lists buying on an exchange as one way, but says nothing about "most people". | Changed to "One common way… Others include rewards…" |
| consensus | "Misbehaving validators can lose (be 'slashed' for) part of their stake [S2]" | **Term not in the source.** S2 says the collateral "can be destroyed" and never uses the word "slashed". | Rewrote it using S2's own wording |
| bitcoin (analogy) | "The private key is like your signature plus PIN… Whoever has it controls the coins." | **Fact hidden in the AI-written analogy.** None of the sources covers private keys, and the analogy section isn't checked for tags. | Rewrote the analogy around signatures (S1) and logged a coverage gap |

Kept but noted:
- blockchain-basics: "Hash: a short fingerprint of data" is an explanation added by Claude, not a sourced definition. S1 only supports "publishing a hash proves the data existed".
- The ⚠ S6 "$5 billion" figure is not used anywhere. The lint check confirms it.

Result after fixes: lint run 2 PASS (see lint-run2.txt).
