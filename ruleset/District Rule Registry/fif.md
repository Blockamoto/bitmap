# FIF: First Is First

**Code ID (provisional):** `fif`  
**Standard:** `1`  
**Current policy:** First eligible District claimant, ordered by Bitcoin reveal position (TXI). Districts only.

## Definition

The **first eligible District claimant wins** when inscriptions are examined in Bitcoin reveal order: **block height → transaction index within the block → input index within the transaction → inscription-reveal order within that input (TXI)**.

Apply the enabled source, MIME, ASCII, schema, height, and exclusion rules to each claim. The first claimant **passing** those tests for a particular District wins. Earlier ineligible inscriptions do not reserve a District; later eligible claimants for the same District lose to the first eligible one.

The TXI sequence is physical reveal order, **not** the Ordinals global inscription number, a block timestamp, output order, or the order returned by an explorer. There is no independent active `first` switch or `precedence_bitcoin_reveal` switch; those previous draft decisions are combined in `fif`.

When `fif=0`, this winner-selection rule is disabled. An executable profile must specify a different complete winner policy; `0` does not imply last-wins or another particular ordering. The separately registered [lowest-inscription-number](lowest-inscription-number.md) comparison policy is not automatically combined with `fif`. The earlier Unix-timestamp idea is documented only in the history below, **not** as a selectable District rule.

## Historical notes

- **Before 14 July 2023 (creator recollection; unverified):** The creator recalls an early idea of ordering District claims by Unix timestamp, before the published lowest-inscription-number wording. No dated publication or implementation of that idea has yet been found. Its original clock source and any use by a deployed 2023 indexer remain unverified.
- [14 July 2023 authored ruleset](https://github.com/blockamotolabs/ruleset/blob/d140da22635b2d286b9b1960f5b3c76ba1a66632/README.md) used “first is first” with the then-stated lowest-inscription-number comparator.
- [22 September 2023 authored change](https://github.com/blockamotolabs/ruleset/commit/754d4d7eda182de76ad543844e530c53426c855c) changed precedence wording to the first valid inscription transaction on block.
- On 23 October 2026, the draft `first` and `precedence_bitcoin_reveal` entries were merged and renamed `fif`, retaining TXI ordering in the definition. This is a current specification decision, not proof that the 2023 Trac writer used every stated tie-break.

### Retired Unix-timestamp interpretation (historical context only)

The former **`precedence_unix_timestamp`** draft row (Standard `0`) tentatively modelled earliest-time ordering as the lowest Unix timestamp in the candidate's Bitcoin **reveal block header** (`nTime`), not an inscription-specific clock or a website's display time. This was a **2026 comparison reconstruction**, not verified evidence of how a 2023 indexer selected winners. On 23 October 2026 it was removed from the active binary registry. It is neither part of `fif` nor a selectable precedence option.

Bitcoin block-header `nTime` is miner-chosen within Bitcoin consensus constraints and need not increase with block height. All inscriptions revealed in the same block share that timestamp. Thus a timestamp-only comparison can tie and cannot always identify a unique District winner without an independently defined tie-break or explicit tied/no-unique-winner outcome. Neither is adopted here.

**Implementation note:** The intended physical within-input inscription-reveal order must be reproduced by the chosen versioned Ord parser and fixtures before committing production outcomes. No numeric bit position or hashed profile has been assigned.

[Registry](README.md) · [Code ID and review gates](CODE-IDS-AND-REVIEW-GATES.md).
