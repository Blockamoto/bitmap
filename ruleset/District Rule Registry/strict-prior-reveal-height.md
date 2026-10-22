# Strictly earlier reveal-block height for District claims

**Default:** `0` (provisional historical alternative)  
**Earliest verified published wording:** 18 July 2023  
**Evidence class:** Dated **authored ruleset document**, not verified Trac server behaviour.

## Definition

When enabled, a District claim for Bitcoin block height `N` is eligible only when `N < reveal_block_height`. An inscription revealed in the *same* Bitcoin block it claims is therefore excluded. This is a stricter alternative to the existing default-on [Claimed block exists](claimed-block-exists.md) check, which permits `N ≤ reveal_block_height`.

The strict rule is a separate optional exclusion, not a change to the canonical `<height>.bitmap` body syntax.

## History and evidence

- [14 July 2023 Blockamoto Labs ruleset snapshot](https://github.com/blockamotolabs/ruleset/blob/d140da22635b2d286b9b1960f5b3c76ba1a66632/README.md) says the claim height is **≤** its inscription block height.
- [18 July 2023 commit `f43970c`](https://github.com/blockamotolabs/ruleset/commit/f43970ccd8241d3d630a13be8d80a9fff71c62bf) changes this line to **<** while reorganising and proofreading the public ruleset. This is the earliest verified source for the *stricter wording*, not evidence that a live indexer started enforcing it that day.
- [24 July 2023 District ruleset file](https://github.com/blockamotolabs/ruleset/blob/d589a9006b3f964c173e94d211d5c73b8a2f25be/1-districts) retains the strict **<** wording.
- [28 July 2023 GitHub snapshot of the Bitmap GitBook District ruleset](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/areas/the-bitmap-standard/district-ruleset.md) explicitly explains **≤**, meaning *equal to, or lower than*, an incompatible contemporaneous publication.

## Clarifications and unresolved history

- The discrepancy might be an editorial inconsistency, an intentional policy alternative, or a real change. Published text alone does not resolve that.
- The original 2023 Trac validator source and dated outputs for same-block claims have **not** been recovered. Do not report this as a confirmed Trac enforcement rule.
- Default `0` preserves the broader existing `≤` check; numbering and standard-profile validation remain pending.
- Districts only. No Parcel rules are implied.
