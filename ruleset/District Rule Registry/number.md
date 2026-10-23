# Number: Inscription-number precedence

**Code ID (provisional):** `number`  
**Standard:** `0`  
**Introduced:** 14 July 2023 (earliest verified published source in the existing audit; also documented 24 and 26-27 July)

## Definition

Prefer the eligible claim with the lowest signed Ordinals inscription number.

## History

Before the first verified inscription-number publication, the creator recalls an early Unix-timestamp precedence idea, with date and deployment unverified. The documented rule used lowest inscription number in July 2023 and changed to first valid inscription transaction on block in September 2023. This progression is also recorded in [Order](order.md#historical-notes); publication dates do not independently establish deployment changes.

- **14 July 2023:** [Blockamoto Labs commit `d140da2`](https://github.com/blockamotolabs/ruleset/commit/d140da22635b2d286b9b1960f5b3c76ba1a66632) specifies lowest inscription number of valid claims.
- **24 July 2023:** [Separate District file](https://github.com/blockamotolabs/ruleset/blob/d589a9006b3f964c173e94d211d5c73b8a2f25be/1-districts) retains that wording.
- **26-27 July 2023:** Historical GitBook documentation gives the same rule. Its [28 July GitHub import](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/areas/the-bitmap-standard/district-ruleset.md) is a snapshot, not the original drafting timestamp.
- **22 September 2023:** [Commit `b94efb8`](https://github.com/blockamotolabs/ruleset/commit/b94efb8f0982d7561a4582cfdb1937c2597cb63c) changes the wording to first valid inscription transaction on block. The live Trac service's change date is not established by that publication.

## OPI published-code comparison

The [OPI Rust reader](https://github.com/bestinslot-xyz/OPI/blob/7933f5d05d978fc226df8126026ed92f8c45d03b/ord/db_reader/src/server.rs#L662-L729) fetches candidates one block at a time and sorts eligible entries by ascending signed inscription number. Its [intake check](https://github.com/bestinslot-xyz/OPI/blob/7933f5d05d978fc226df8126026ed92f8c45d03b/ord/db_reader/src/server.rs#L309-L325) rejects negative numbers first. The [Python indexer](https://github.com/bestinslot-xyz/OPI/blob/7933f5d05d978fc226df8126026ed92f8c45d03b/modules/bitmap_index/bitmap_index.py) keeps the first eligible entry for a District while processing blocks by height.

That is **block-height-first, then eligible inscription-number order within each block**, not an unconstrained global sort of all historic signed numbers. Public code does not prove a hosted deployment or a marketplace's exact version.

Positive inscription numbering generally follows reveal order, but the [Ord documentation](https://github.com/ordinals/ord/blob/0.29.1/docs/src/inscriptions.md#inscription-numbers) describes historical fee-spend numbering exceptions. Negative numbering is another distinction, though the inspected OPI reader excludes negative numbers. A different comparator alone does not prove a changed winner; a qualifying collision must be demonstrated.

## Independent eligibility

The separate default-off exclusion is now named [`negative`](negative-inscription-number-exclusion.md), formerly `negative_inscription_number_exclusion`. Enabling `number` must not implicitly activate it. Conversely, `negative` may be used with Bitcoin reveal `order` instead.

Literal signed ordering can prefer negative numbers over positive numbers, and later-assigned negative numbers can be numerically smaller. Actual historical indexer behavior and the selected comparator composition must therefore be specified explicitly.

This consolidation does not change `number`, its Standard value or the unresolved conflict between simultaneously enabled winner-selection modes.
