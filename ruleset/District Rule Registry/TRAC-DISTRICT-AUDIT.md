# Trac District indexer audit

**Audit date:** 22 October 2026  
**Scope:** Bitmap **District** validity, candidate eligibility and winner selection only. No Parcel, ownership, transfer, tapping, or staking rules are included.  
**Status:** Public-code comparison complete for the confirmed points below; the original 2023 production writer and some edge cases remain unverified.

## Evidence boundaries

- [Public 2023 Trac Bitmap API description](https://github.com/BennyTheDev/trac-bitmap-public-endpoint) documents live Bitmap validity lookups but does **not** publish the original District validation algorithm. Its Git history begins in July 2023.
- [Trac-Systems/ord-tap](https://github.com/Trac-Systems/ord-tap) is a later, standalone Rust port of the Trac/TAP writer, with an initial public revision on **19 September 2025**. Its behaviour is an actual implementation to audit, **not proof** that the original 2023 service behaved identically.
- Rule rows below use the earliest **verified public code date** (or actual dated diff when found); introductory dates in the registry contain dates only, and evidence distinctions are captured on the individual pages.

## New District Rule Registry entries

The listed entries are unnumbered and **off (`0`) by default** pending Standard-profile review. Trac-derived code supplies **implementation evidence for comparison rules** that can reproduce material differences between major indexers; it does not make Trac's policies the Bitmap Standard, and it is not evidence of how the unrecovered original 2023 Trac writer behaved.

| Rule | Earliest verified code/date | Distinction |
| --- | --- | --- |
| [Text MIME family exception](text-mime-family-exception.md) | 19 September 2025 | Initial Rust port accepts `text/*`; narrowed to `text/plain` on 25 September 2025. |
| [JSON MIME exception](json-mime-exception.md) | 19 September 2025 | Shared intake permits `application/json` labels even when District content itself must be exact `<height>.bitmap`. |
| [Literal MIME string-prefix compatibility](mime-string-prefix-compatibility.md) | 19 September 2025 | Actual `starts_with` MIME intake can match malformed prefix-compatible labels; independent of which MIME family/exception is enabled. |
| [Nested delegate exclusion](nested-delegate-exclusion.md) | 19 September 2025 | Reject a delegation target that delegates again. Initially located after the TAP-start gate. |
| [Fallback for unresolved delegate](fallback.md) | 25 September 2025 | When a declared delegate lookup fails, retain the claimant's original body and content type instead of Ord's not-found result. Normal delegate resolution remains part of `content`. |
| [Negative inscription number exclusion](negative-inscription-number-exclusion.md) | 19 May 2026 | Explicitly reject signed Ordinals inscription numbers below zero. Previously absent from the Rust District creator. |

Relevant changes: [Initial port](https://github.com/Trac-Systems/ord-tap/commit/3f3f851a00301b780e333fc9d8a3c3eaf29920e3) · [MIME narrowing and effective delegation](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) · [Negative-number guard](https://github.com/Trac-Systems/ord-tap/commit/12ddc36ccfa7655a2bbec20d0245deecdec0ec55).

## Separate historical authored-rule alternatives

- **14 July 2023:** [Blockamoto Labs source](https://github.com/blockamotolabs/ruleset/commit/d140da22635b2d286b9b1960f5b3c76ba1a66632) already describes **lowest inscription number** as the winner; this is earlier than the 26–27 July GitBook date previously used in the registry. [Number](number.md) now records that primary evidence.
- **22 September 2023:** [Blockamoto Labs commit `754d4d7`](https://github.com/blockamotolabs/ruleset/commit/754d4d7eda182de76ad543844e530c53426c855c) changes winner phrasing from lowest inscription number to **first valid inscription transaction on block**, and the [District file follow-up](https://github.com/blockamotolabs/ruleset/commit/b94efb8f0982d7561a4582cfdb1937c2597cb63c) confirms it the same day. [Order (Bitcoin reveal order)](order.md) records this historical evidence and now specifies TXI reveal order. The published 2023 phrase does not independently verify that complete order in the original Trac deployment.

## Source-selection binaries and delegate-tag veto, distinct from Trac rules

**22 October 2026:** At the creator's direction, the registry now separately records [Body](inscription-body-source.md) (`body=1`), [Content](inscription-content-source.md) (`content=0`), and [Delegate Tag Exclusion](delegate-tag-exclusion.md) (default `0`). These are independent questions about claim source versus candidate eligibility, not a merged delegate rule or a rewording falsely attributed to 2023. The short IDs were selected in 2026; earlier `content=1` referred to own-body processing, unlike the current `content` source.

The body-source rule has directly related verified code from **19 September 2025**; served-content resolution has related code from **25 September 2025**; the all-delegates veto appears as an explicit working comparison policy by **16 October 2026** in [the earlier Bitmap specification](https://github.com/Blockamoto/bitmap-old/blob/ccf7271a61a2cead4781d4a2bb9c86da761f1cd6/DISTRICT-RULESET.md). No such code dates prove inception in the original 2023 Trac service. The Trac-derived ordinary delegate lookup is already covered by the separately defined **`content` source**, whose chosen reference is [Ord `0.29.1`](https://github.com/ordinals/ord/blob/0.29.1/src/subcommand/server/r.rs#L250-L279). Its **different behavior only when a delegate lookup fails** is now an independent default-off [`fallback`](fallback.md) comparison rule; the former combined `delegate_content_resolution` rule remains retired.

**Remaining composition questions:** If both source binaries are `0`, no source is selected; if both are `1`, a candidate could yield two different claim bodies. No rule for combining them has been agreed. A nested-delegate veto stays independent of the broader all-delegates veto. The [District source/eligibility semantics note](DISTRICT-CONTENT-OPEN-QUESTION.md) records those unresolved combinations. These are **not** blockers to documenting the three binary alternatives, and no current rule-set hashes or executable profile selections are assumed.

## Existing rules corroborated, not duplicated

The [District creation routine](https://github.com/Trac-Systems/ord-tap/blob/main/src/index/updater/inscription_updater/tap/ops/bitmap.rs) requires the body to contain a canonical lowercase `<height>.bitmap` string with no leading zeros, rejects future claimed heights, and preserves the first accepted claim for each District height using the existing `bm/<height>` record. These overlap the registry's canonical schema, claimed-block-exists, and winner-order rules.

The public routine uses the indexer's processing order; the current [`order`](order.md) draft explicitly uses Bitcoin block, transaction, input and in-input inscription reveal order (TXI). Match that policy to pinned Ord envelope-parser behaviour and test fixtures before claiming equivalence with Trac's historical implementation.

## District-specific edge cases still to classify

1. **MIME string-prefix matching: recorded as a separate candidate.** The shared filter uses `starts_with("text/plain")` or `starts_with("application/json")`, not parsed base media types. This can permit malformed MIME strings that merely begin with those bytes. Its historical compatibility policy is now separately documented in [Literal MIME string-prefix compatibility](mime-string-prefix-compatibility.md), default off; fixture-level outcome comparison remains open.
2. **Encoding and compression.** The District creator applies `String::from_utf8_lossy(body)` to raw inscription bytes; the District path does not explicitly veto the `content_encoding` tag or decompress a body. Because the accepted District body consists entirely of ASCII digits and the literal `.bitmap`, replacing invalid UTF-8 bytes does **not** create a newly valid District claim. Thus lossy versus strict UTF-8 decoding does not by itself justify an additional validity switch for this schema. A correctly formatted ASCII body that merely carries a content-encoding tag is a separate metadata-policy comparison for Live OCI.
3. **Minimum scan/activation height.** Mainnet `TAP_BITMAP_START_HEIGHT` is `779832`. The creation hook exits before indexing at lower heights. Decide whether an operational index start should be part of District eligibility rules or only the indexer coverage record.
4. **Reinscriptions and unbound status.** The Trac-derived District creation hook does **not** explicitly veto `reinscription` or `unbound` flags passed through to its outer inscription hook. That absence is **not** evidence that all such inscriptions reach the hook successfully or were accepted by the original production Trac service. Audit the Ord envelope/curse stage before proposing a District exclusion rule.
5. **Unknown/unavailable delegate (separate `fallback=0` comparison rule).** The later Trac-derived hook starts with the claimant's original payload, replacing it only if the declared delegate is fetched successfully. On a missing target or failed lookup it retains the original payload and content type. By contrast, pinned [Ord `0.29.1`](https://github.com/ordinals/ord/blob/0.29.1/src/subcommand/server/r.rs#L250-L279) returns not found without using the original body. The default-off [`fallback`](fallback.md) bit captures this **failed-lookup difference only**. It may change the winner in an exceptional collision if `content=1`; with `content=0` in Bitmap Standard the bit has no effect.

## Not yet established

The original **2023 Trac Bitmap writer's** MIME policy, delegated-content handling, encoding policy and cursed/reinscription behaviour are **not established** by the 2025–26 Rust port. Do not backdate the above rules to 2023 solely because the endpoint was active then.

When continuing the audit, verify 2023 writer/deployment evidence and any fixture that demonstrably produces different District winners; treat operational configuration separately from eligibility unless its effect on validity is demonstrated.
