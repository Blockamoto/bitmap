# Claimed block exists

**Code ID (provisional):** `height`  
**Standard:** `1`  
**Introduced:** 16 June 2023

## Definition

Require `<height>` to be no greater than the inscription's reveal block height.

## History

- **16 June 2023:** The verification guide explicitly excludes claims to future blocks. This is a documented-by date, not necessarily the date the rule was conceived.
- **14 July 2023:** [Blockamoto Labs ruleset](https://github.com/blockamotolabs/ruleset/blob/d140da22635b2d286b9b1960f5b3c76ba1a66632/README.md) explicitly says the claimed height is **≤** its reveal block height.
- **18 July 2023:** [Source commit `f43970c`](https://github.com/blockamotolabs/ruleset/commit/f43970ccd8241d3d630a13be8d80a9fff71c62bf) changes the written condition to **<**, while a later [Bitmap GitBook snapshot](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/areas/the-bitmap-standard/district-ruleset.md) explains **≤**. The stricter alternative is separately preserved in [Strictly earlier reveal-block height](strict-prior-reveal-height.md) without changing this default rule.

## Evidence

- [Historical verification guide](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/archive/_old/bitmap-theory-101/how-to-verify-blocks.md)

## Clarifications

- Compare the claimed height with the inscription reveal-block height. This baseline permits a **same-block** District claim; enabling the separate strict-before-reveal option disallows it.
- The 2023 documentary difference is **not proof** that Trac's original deployed writer enforced either interpretation on a specific date.
