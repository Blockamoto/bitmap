# District Rule Registry

**Status:** Draft for review. **Scope:** Districts only. **Index** positions are intentionally blank until permanent binary positions are agreed. This is not an executable or frozen ruleset.

| Index | ID | Standard | Definition |
| --- | --- | :---: | --- |
|  | [`schema_bmp101`](bmp101-district-prototype-schema.md) | 0 | Recognize the historical BMP101 JSON District-claim format. |
|  | [`regex`](canonical-district-schema.md) | 1 | Require an entire selected claim to match canonical `<height>.bitmap` syntax, with decimal height and lowercase suffix. |
|  | [`inscription_body`](inscription-body-source.md) | 1 | Evaluate the claimant inscription's own undelegated envelope body. |
|  | [`inscription_content`](inscription-content-source.md) | 0 | Evaluate content served for the claimant inscription ID, potentially supplied by its delegate. |
|  | [`text`](plain-text-inscription.md) | 1 | Require the parsed MIME media type `text/plain`; charset parameters do not themselves decide MIME eligibility. |
|  | [`strict`](raw-utf8-strict-decoding.md) | 1 | Decode selected bytes as strict UTF-8 (ASCII-compatible), ignoring any declared charset; canonical District claims must match exact ASCII bytes. |
|  | [`height`](claimed-block-exists.md) | 1 | Require the claimed block height to be no greater than the inscription's reveal-block height. |
|  | [`first`](first-eligible-wins.md) | 1 | Recognize the first eligible District claimant under the independently selected precedence comparator. |
|  | [`precedence_unix_timestamp`](unix-timestamp-ordering.md) | 0 | Rank eligible reveals by the Bitcoin reveal block's `nTime`; ties need explicit handling. |
|  | [`precedence_inscription_number`](lowest-inscription-number.md) | 0 | Rank eligible claims by lowest signed Ordinals inscription number. |
|  | [`precedence_bitcoin_reveal`](bitcoin-transaction-ordering.md) | 1 | Rank eligible claims by reveal-block height, then transaction position; intra-transaction ties remain open. |
|  | [`strict_height`](strict-prior-reveal-height.md) | 0 | Require claimed block height strictly below reveal height, excluding same-block claims. |
|  | [`delegate_content_resolution`](delegate-content-resolution.md) | 0 | Reproduce Trac-derived one-hop delegate-content lookup and fallback as a separate comparison policy. |
|  | [`text_mime_family`](text-mime-family-exception.md) | 0 | Also permit MIME `text/*` subtypes beyond `text/plain` for otherwise qualifying claims. |
|  | [`json_mime`](json-mime-exception.md) | 0 | Also permit the `application/json` MIME label without relaxing the District claim grammar. |
|  | [`mime_prefix_compatibility`](mime-string-prefix-compatibility.md) | 0 | Apply historical literal MIME-string prefix matching rather than strictly parsed MIME matching. |
|  | [`brotli`](brotli-decompression-eligibility.md) | 0 | Allow a separately specified Brotli-decompression path to make claim bytes eligible. |
|  | [`encoding_tag_exclusion`](content-encoding-tag-exclusion.md) | 0 | Reject a candidate solely because Ord content-encoding tag 9 is present. |
|  | [`nested_delegate_exclusion`](nested-delegate-exclusion.md) | 0 | Reject claimants whose immediate delegate itself declares a delegate. |
|  | [`negative_inscription_number_exclusion`](negative-inscription-number-exclusion.md) | 0 | Reject claimants with negative signed Ordinals inscription numbers. |
|  | [`delegate_exclusion`](delegate-tag-exclusion.md) | 0 | Reject any claimant declaring Ord delegate field 11, independently of its own body. |

**Standard** is the *proposed* Bitmap Standard profile value (`1` enabled; `0` disabled), not a claim that every historical indexer used it. Rules that resolve the fundamental schema, content source, text interpretation, height and winner questions appear first; additional historical exceptions follow. Related decisions remain adjacent. No rule positions or profile hashes have been assigned.

Text decoding currently has **one active rule**: [`strict`](raw-utf8-strict-decoding.md) = **`1`**. It decodes the selected inscription bytes as strict UTF-8, rejects malformed UTF-8, and passes the unchanged decoded string to the District schema. Because the canonical whole-string District grammar is ASCII-only, this accepts exactly the canonical ASCII byte sequence. A declared MIME `charset` does **not** change decoding in this Standard profile. The separate `text` rule still governs `text/plain` MIME eligibility.

The previously considered charset-aware (`mime_charset`) interpretation is **deferred, not an active rule or fallback**. Its research rationale is retained in [encoding comparisons](TEXT-ENCODING-COMPARISON.md) and the [earlier draft commit](https://github.com/Blockamoto/bitmap/commit/8a882873b85c451a605ea568a88ab7faeaca7d23). With no other decoder enabled or defined, `strict=0` leaves an incomplete, non-executable profile. No implicit compatible mode is available.

Historic evidence, dates, dependencies and unresolved decisions are preserved on the linked rule pages and in [encoding comparisons](TEXT-ENCODING-COMPARISON.md), [code-ID mapping and production gates](CODE-IDS-AND-REVIEW-GATES.md), and [source/delegation distinctions](DISTRICT-CONTENT-OPEN-QUESTION.md). The retracted hash-prefixed tutorial typo is **not** a registry rule. No Parcel definitions are included.
