# Negative inscription number exclusion for District claims

**Code ID (provisional):** `negative_inscription_number_exclusion`  
**Default:** `0`  
**Introduced:** 19 May 2026

## Definition

When enabled, reject a District candidate whose **Ordinals inscription number is negative** (historically called a cursed inscription), even when its inscription body otherwise satisfies the canonical District schema and the remaining enabled rules.

## History and evidence

- [Trac-derived `ord-tap` commit, 19 May 2026](https://github.com/Trac-Systems/ord-tap/commit/12ddc36ccfa7655a2bbec20d0245deecdec0ec55) adds an explicit `if inscription_number < 0 { return; }` check at the start of `index_bitmap_created`.
- [Previous 18 May 2026 revision](https://github.com/Trac-Systems/ord-tap/blob/24d093aba2/src/index/updater/inscription_updater/tap/ops/bitmap.rs) did **not** have this District creation-time exclusion. The negative-number check in those earlier routines applied to the **claimed Bitcoin block height** instead, not to the Ordinals inscription number.
- The history of the original 2023 production Trac writer remains unproven. The date above refers to this confirmed code change, not a claim that all earlier Trac services accepted cursed Districts.

## Clarifications

- This condition concerns the signed Ordinals **inscription number**, not the District's claimed height. A `-1.bitmap` body is already rejected by the existing canonical District syntax.
- Its default is off pending audit of which historical semantics the Bitmap Standard should adopt. An indexer may enforce this exclusion even though the present registry's default does not.
- Reinscriptions, unbound inscriptions, and other Ordinals properties are not equivalent to having a negative inscription number.
- District recognition only; Parcel rules are out of scope.
