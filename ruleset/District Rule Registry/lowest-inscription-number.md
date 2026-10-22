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

## Clarifications

- Literal signed comparison means negative cursed inscription numbers can outrank positive numbers, and lower negative numbers may be assigned later.
- The actual behavior of early deployed indexers requires separate verification.
