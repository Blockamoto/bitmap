# District Rule Registry

**Status:** Draft for review. **Scope:** Districts only. **Index** positions are intentionally blank until permanent binary positions are agreed. This is not an executable or frozen ruleset.

| Index | ID | Standard | Definition |
| --- | --- | :---: | --- |
|  | [`schema`](canonical-district-schema.md) | 1 | Require the entire selected claim to use canonical `<height>.bitmap` syntax (decimal height, lowercase suffix), matching the [regex](district-claim.regex). |
|  | [`body`](inscription-body-source.md) | 1 | Evaluate the District claim using the claimant inscription's own envelope body, rather than content served for its inscription ID; a delegate's content is therefore not substituted. |
|  | [`text`](plain-text-inscription.md) | 1 | Require the parsed MIME media type `text/plain`; charset parameters do not themselves decide MIME eligibility. |
|  | [`ascii`](ascii-byte-matching.md) | 1 | Require the selected claim bytes to be US-ASCII (compatible with UTF-8 and other ASCII-compatible encodings), ignoring any declared charset. |
|  | [`height`](claimed-block-exists.md) | 1 | Require `<height>` to be no greater than the inscription's reveal block height. |
|  | [`order`](order.md) | 1 | Recognise the first eligible District claimant in Bitcoin reveal order: block, transaction, input, then inscription reveal within that input (TXI). |
|  | [`content`](inscription-content-source.md) | 0 | Evaluate the District claim using content served for the claimant inscription ID, rather than reading its own envelope body directly; that content could therefore be supplied by a delegate. |
|  | [`number`](number.md) | 0 | Rank eligible District claims by lowest signed Ordinals inscription number. |
|  | [`fallback`](fallback.md) | 0 | If a declared delegate cannot be resolved while evaluating served `content`, use the claimant inscription's own envelope body and content type instead of returning not found. |
|  | [`text_mime_family`](text-mime-family-exception.md) | 0 | Also permit MIME `text/*` subtypes beyond `text/plain` for otherwise qualifying claims. |
|  | [`json`](json.md) | 0 | Also permit the `application/json` MIME label without relaxing the District claim grammar. |
|  | [`mime_prefix_compatibility`](mime-string-prefix-compatibility.md) | 0 | Apply historical literal MIME-string prefix matching rather than strictly parsed MIME matching. |
|  | [`brotli`](brotli-decompression-eligibility.md) | 0 | Allow a separately specified Brotli-decompression path to make claim bytes eligible. |
|  | [`encoding_tag_exclusion`](content-encoding-tag-exclusion.md) | 0 | Reject a candidate solely because Ord content-encoding tag 9 is present. |
|  | [`nested_delegate_exclusion`](nested-delegate-exclusion.md) | 0 | Reject claimants whose immediate delegate itself declares a delegate. |
|  | [`negative_inscription_number_exclusion`](negative-inscription-number-exclusion.md) | 0 | Reject claimants with negative signed Ordinals inscription numbers. |
|  | [`delegate_exclusion`](delegate-tag-exclusion.md) | 0 | Reject any claimant declaring Ord delegate field 11, independently of its own body. |

**Standard** is the *proposed* Bitmap Standard profile value (`1` enabled; `0` disabled), not a claim that every historical indexer used it. The table groups all proposed Standard `1` rules above the `0` rules, beginning with `schema`, `body`, and `text`. This is a review/display order, **not** historical chronology or permanent numeric bit positions. The canonical `<height>.bitmap` syntax is the only active District claim schema; no prototype/alternate schema is selectable. No rule positions or profile hashes have been assigned.

Byte interpretation currently has **one active rule**: [`ascii`](ascii-byte-matching.md) = **`1`**. It evaluates the selected claim bytes as US-ASCII without consulting any declared MIME charset. UTF-8 and other ASCII-compatible encodings represent the canonical `<height>.bitmap` claim with identical ASCII bytes. The independent [`schema`](canonical-district-schema.md) rule requires a whole-claim match, and [`text`](plain-text-inscription.md) still governs `text/plain` MIME eligibility.

The previously considered charset-aware (`mime_charset`) interpretation is **deferred, not an active rule or fallback**. Its research rationale remains in [encoding comparisons](TEXT-ENCODING-COMPARISON.md) and the [earlier draft commit](https://github.com/Blockamoto/bitmap/commit/8a882873b85c451a605ea568a88ab7faeaca7d23). With no other byte interpretation defined, `ascii=0` leaves an incomplete profile. No implicit compatible mode is available.

Historic evidence, dates, dependencies and unresolved decisions are preserved on the linked rule pages and in [encoding comparisons](TEXT-ENCODING-COMPARISON.md), [code-ID mapping and production gates](CODE-IDS-AND-REVIEW-GATES.md), and [source/delegation distinctions](DISTRICT-CONTENT-OPEN-QUESTION.md). The retracted hash-prefixed tutorial typo is **not** a registry rule. No Parcel definitions are included.
