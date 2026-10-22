# First eligible claimant wins

**Code ID (provisional):** `first`  
**Standard:** `1` (current proposed profile)  
**Earliest relevant published wording:** 14 July 2023, “first is first” among valid claims, with *lowest inscription number* as the then-specified comparator.  
**Independent binary separation:** Documented in the 21 October 2026 [bitmap-old District atomicity reference](https://github.com/Blockamoto/bitmap-old/blob/main/DISTRICT-RULESET.md).  
**Status:** District-only draft decision; not a frozen bit position.

## Single decision

When `first=1`, select the **first eligible** claimant for a District under a **separately specified comparator**. Apply all enabled syntax, source, MIME, decoding, height and veto rules **before** ranking. A previously seen *ineligible* inscription is not a winner and does not reserve a District.

When `first=0`, **this rule does not select an earliest candidate**. The profile must declare another winner policy before any unique outcome is committed. Do not treat `0` as “last wins”, “all win”, or “no one wins” by implication.

This rule is independent of **which comparator determines first**:

- [Unix timestamp precedence](unix-timestamp-ordering.md) (undated historical recollection; ties within a reveal block and potentially across blocks).
- [Lowest signed inscription number](lowest-inscription-number.md) (documented 14 July 2023).
- [Bitcoin reveal/transaction order](bitcoin-transaction-ordering.md) (documented 22 September 2023; within-transaction order still needs a pinned interpreter).

Exactly one comparator and its deterministic tie-handling must be specified for a single-winner executable profile. Enabling several precedence bits without composition semantics is **not** equivalent to first-wins.

## Evidence, chronology and scope

- [14 July 2023 Blockamoto Labs ruleset](https://github.com/blockamotolabs/ruleset/blob/d140da22635b2d286b9b1960f5b3c76ba1a66632/README.md) says “first is first = lowest inscription number of valid claims.” This establishes historical wording **with that comparator**, not a standalone Boolean.
- [22 September 2023 authored ruleset change](https://github.com/blockamotolabs/ruleset/commit/754d4d7eda182de76ad543844e530c53426c855c) updates the written precedence to first valid inscription transaction.
- [21 October 2026 atomicity review](https://github.com/Blockamoto/bitmap-old/blob/main/RULESET-ATOMICITY.md) separates `first` from the older compound `fiftxi` identifier. The current registry recognizes that separation without retrospectively attributing it to the 2023 indexer.
- The original 2023 Trac writer remains unverified. No Parcel behaviour is defined here.

**Production prerequisite:** specify comparator, tie policy and parser/reveal physical order; unresolved input evidence is not an automatic rejection or winner. [Registry ordering](README.md) · [code-ID crosswalk](CODE-IDS-AND-REVIEW-GATES.md).
