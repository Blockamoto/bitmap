# FIF: First Is First

**Code ID (provisional):** `fif`  
**Standard:** `1`  
**Current policy:** First eligible District claimant, ordered by Bitcoin reveal position (TXI). Districts only.

## Definition

The **first eligible District claimant wins** when inscriptions are examined in Bitcoin reveal order: **block height → transaction index within the block → input index within the transaction → inscription-reveal order within that input (TXI)**.

Apply the enabled source, MIME, ASCII, schema, height, and exclusion rules to each claim. The first claimant **passing** those tests for a particular District wins. Earlier ineligible inscriptions do not reserve a District; later eligible claimants for the same District lose to the first eligible one.

The TXI sequence is physical reveal order, **not** the Ordinals global inscription number, a block timestamp, output order, or the order returned by an explorer. There is no independent active `first` switch or `precedence_bitcoin_reveal` switch; those previous draft decisions are combined in `fif`.

When `fif=0`, this winner-selection rule is disabled. An executable profile must specify a different complete winner policy; `0` does not imply last-wins or another particular ordering. Independently listed historical alternatives such as [Unix-time precedence](unix-timestamp-ordering.md) and [lowest inscription number](lowest-inscription-number.md) are not automatically combined with `fif`.

## Historical notes

- [14 July 2023 authored ruleset](https://github.com/blockamotolabs/ruleset/blob/d140da22635b2d286b9b1960f5b3c76ba1a66632/README.md) used “first is first” with the then-stated lowest-inscription-number comparator.
- [22 September 2023 authored change](https://github.com/blockamotolabs/ruleset/commit/754d4d7eda182de76ad543844e530c53426c855c) changed precedence wording to the first valid inscription transaction on block.
- On 23 October 2026, the draft `first` and `precedence_bitcoin_reveal` entries were merged and renamed `fif`, retaining TXI ordering in the definition. This is a current specification decision, not proof that the 2023 Trac writer used every stated tie-break.

**Implementation note:** The intended physical within-input inscription-reveal order must be reproduced by the chosen versioned Ord parser and fixtures before committing production outcomes. No numeric bit position or hashed profile has been assigned.

[Registry](README.md) · [Code ID and review gates](CODE-IDS-AND-REVIEW-GATES.md).
