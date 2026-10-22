# Lowest inscription number

**Code ID (provisional):** `precedence_inscription_number`  
**Standard:** `0`  
**Introduced:** 14 July 2023 (earliest verified published source; also documented 24 and 26–27 July)

## Definition

Prefer the eligible claim with the lowest signed Ordinals inscription number.

## History

- **14 July 2023:** [Blockamoto Labs ruleset commit `d140da2`](https://github.com/blockamotolabs/ruleset/commit/d140da22635b2d286b9b1960f5b3c76ba1a66632) already specifies “first is first = lowest inscription number of valid claims”. Its repository was created on 14 July; this is the earliest verified public source found in the current audit.
- **24 July 2023:** [Separate `1-districts` ruleset file](https://github.com/blockamotolabs/ruleset/blob/d589a9006b3f964c173e94d211d5c73b8a2f25be/1-districts) retains the same wording.
- **26–27 July 2023:** The historical Bitmap GitBook documented the same rule; its [28 July GitHub import](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/areas/the-bitmap-standard/district-ruleset.md) is a snapshot, not the original drafting timestamp.
- **22 September 2023:** [Blockamoto Labs commit `b94efb8`](https://github.com/blockamotolabs/ruleset/commit/b94efb8f0982d7561a4582cfdb1937c2597cb63c) changes this wording to first valid inscription transaction on block. That **documented change** does not prove the live Trac service switched its winner-selection algorithm on the same day.

## Evidence

- [14 July 2023 first-party ruleset snapshot](https://github.com/blockamotolabs/ruleset/blob/d140da22635b2d286b9b1960f5b3c76ba1a66632/README.md)
- [Historical District Ruleset GitBook snapshot](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/areas/the-bitmap-standard/district-ruleset.md)

## OPI published-code comparison (audited 23 October 2026)

The current public [Best in Slot OPI Rust reader](https://github.com/bestinslot-xyz/OPI/blob/main/ord/db_reader/src/server.rs#L662-L729) fetches new Bitmap inscriptions for **one block at a time**, applies its intake checks, then explicitly sorts the returned candidates **by ascending signed `inscription_number`** (lines 726–727). Its [`is_valid_bitmap` check](https://github.com/bestinslot-xyz/OPI/blob/main/ord/db_reader/src/server.rs#L309-L325) rejects negative inscription numbers before that sort. The [Python Bitmap indexer](https://github.com/bestinslot-xyz/OPI/blob/main/modules/bitmap_index/bitmap_index.py) loops through the already ordered response, accepting only the first eligible entry for each Bitmap number (`ON CONFLICT (bitmap_number) DO NOTHING`). Blocks are processed in height order. Thus **OPI implements block-height-first, then lowest *eligible* inscription number within a block**; it does **not** globally sort all historical candidates by inscription number.

This demonstrates that inscription-number ordering remains an explicit choice in OPI's **published code**, rather than being only a 2023 textual rule. It does **not** verify the exact version previously deployed by OPI's hosted service or establish which third-party marketplaces use this code.

**Outcome caveat:** [Ord's inscription-number documentation](https://github.com/ordinals/ord/blob/master/docs/src/inscriptions.md#inscription-numbers) says positive numbers generally follow block, transaction and envelope reveal order, but documents an exceptional historical fee-spend numbering case in which inscriptions revealed and immediately spent to fees are numbered as if they appeared last in their block. Negative cursed numbering is another divergence source, although the cited OPI reader excludes negative numbers. Accordingly, **a different comparator does not by itself prove a different winning District**: identify a same-District, same-block collision with a reversed ordering among eligible candidates before claiming an observed conflict with `fif`.

This OPI implementation is a **comparison target**, not an amendment to the present rule ID, its Standard `0` value, or the separate default-off `negative_inscription_number_exclusion` binary. Do not automatically apply OPI's negative-number veto when enabling this precedence rule.

## Clarifications

- Literal signed comparison means negative cursed inscription numbers can outrank positive numbers, and lower negative numbers may be assigned later.
- The actual behavior of early deployed indexers requires separate verification.
