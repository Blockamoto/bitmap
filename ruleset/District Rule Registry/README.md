# District Rule Registry

**Status:** Draft for review. **Scope:** Districts only. **Index** values `0`–`5` are provisional review indices, not a frozen bit layout, serialized profile or executable ruleset. Remaining indices are blank pending review.

| Index | ID | Standard | Definition |
| --- | --- | :---: | --- |
| 0 | [`schema`](canonical-district-schema.md) | 1 | Require the entire selected claim to use canonical `<height>.bitmap` syntax (decimal height, lowercase suffix), matching the [regex](district-claim.regex). |
| 1 | [`body`](inscription-body-source.md) | 1 | Evaluate the District claim using the claimant inscription's own envelope body, rather than content served for its inscription ID; a delegate's content is therefore not substituted. |
| 2 | [`text`](plain-text-inscription.md) | 1 | Require the parsed MIME media type `text/plain`; charset parameters do not themselves decide MIME eligibility. |
| 3 | [`ascii`](ascii-byte-matching.md) | 1 | Require the selected claim bytes to be US-ASCII (compatible with UTF-8 and other ASCII-compatible encodings), ignoring any declared charset. |
| 4 | [`height`](claimed-block-exists.md) | 1 | Require `<height>` to be no greater than the inscription's reveal block height. |
| 5 | [`order`](order.md) | 1 | Recognise the first eligible District claimant in Bitcoin reveal order: block height, transaction index, then inscription index (`i`) within the transaction (TXi). |
|  | [`content`](inscription-content-source.md) | 0 | Evaluate the District claim using content served for the claimant inscription ID, rather than reading its own envelope body directly; that content could therefore be supplied by a delegate. |
|  | [`number`](number.md) | 0 | Rank eligible District claims by lowest signed Ordinals inscription number. |
|  | [`fallback`](fallback.md) | 0 | If a declared delegate cannot be resolved while evaluating served `content`, use the claimant inscription's own envelope body and content type instead of returning not found. |
|  | [`json`](json.md) | 0 | Also permit the `application/json` MIME label without relaxing the District claim grammar. |
|  | [`brotli`](brotli-decompression-eligibility.md) | 0 | Permit Brotli decompression of selected body bytes to supply an additional candidate claim, still subject to all other enabled rules. |
|  | [`exclusion`](content-encoding-tag-exclusion.md) | 0 | Reject a claimant solely because its own inscription envelope contains content-encoding tag 9 in field position, regardless of the tag's value. |
|  | [`nested`](nested-delegate-exclusion.md) | 0 | Reject a claimant whose decoded delegate reference resolves to an inscription that itself has a decodable delegate reference. |
|  | [`negative`](negative-inscription-number-exclusion.md) | 0 | Reject a claimant whose signed Ordinals inscription number is below zero. |
|  | [`delegate`](delegate-tag-exclusion.md) | 0 | Reject a claimant solely because its own inscription envelope contains delegate tag 11 in field position, regardless of the tag's value. |
|  | [`prefix`](prefix.md) | 0 | Use literal, case-sensitive prefix matching for the MIME labels allowed by the profile, instead of parsed media-type matching. |

**Standard** is the *proposed* Bitmap Standard profile value (`1` enabled; `0` disabled), not a claim that every historical indexer used it. The six approved Standard `1` rules are ordered `schema`, `body`, `text`, `ascii`, `height`, `order` (draft indices `0`–`5`); `content` is the first Standard `0` and remains unnumbered, as do the other disabled rules. `prefix` remains last for later review. This ordering is not historical chronology, and provisional indices do not freeze a bit allocation, serialized profile or production hashes.

The canonical `<height>.bitmap` syntax is the only active District claim schema. Byte interpretation has **one active rule**: [`ascii`](ascii-byte-matching.md) = **`1`**, independent of declared MIME charset. The independent [`schema`](canonical-district-schema.md) rule requires a whole-claim match, and [`text`](plain-text-inscription.md) governs MIME eligibility. Keeping `text=1` is the current decision; any future `text=0` Standard proposal requires a full winner-ID comparison, not merely a count comparison. No such historical comparison has been completed by this documentation audit.

The previously considered charset-aware (`mime_charset`) interpretation is **deferred, not an active rule or fallback**. Its research rationale remains in [encoding comparisons](TEXT-ENCODING-COMPARISON.md) and the [earlier draft commit](https://github.com/Blockamoto/bitmap/commit/8a882873b85c451a605ea568a88ab7faeaca7d23). With no other byte interpretation defined, `ascii=0` leaves an incomplete profile. No implicit compatible mode is available.

See the [six-rule consolidation report](SIX-RULE-AUDIT.md) for the 23 October 2026 naming changes, source checks, independent-rule counterexamples and remaining limitations. There are **16** active IDs; all existing Standard values are unchanged. Descriptive filenames are retained to preserve existing links.

Historic evidence, dates, dependencies and unresolved decisions are preserved on the linked rule pages and in [encoding comparisons](TEXT-ENCODING-COMPARISON.md), [code-ID mapping and production gates](CODE-IDS-AND-REVIEW-GATES.md), and [source/delegation distinctions](DISTRICT-CONTENT-OPEN-QUESTION.md). The retracted hash-prefixed tutorial typo is **not** a registry rule. No Parcel definitions are included.

## Claim input and Ord compatibility (23 October 2026 clarification)

**Bitcoin is the source of record.** The proposed Standard reads Bitcoin transactions and recognizes Ordinals-style inscription envelopes from input witness Tapscript. For each recognized claimant, the [Body](inscription-body-source.md) source supplies the envelope's own stored body payload (the ordered concatenation of body data pushes where applicable). The claim is not matched against whole-block hex, transaction serialization, an entire witness script, or rendered content from an Ord HTTP endpoint.

**Raw body is not served content.** The separate `text`, `ascii`, `schema`, `height`, and `order` rules evaluate that candidate and its associated metadata. The Standard does not substitute delegate content or implicitly decompress Brotli/gzip. Ignoring a delegate when choosing the body is **not** rejecting a claimant merely for declaring one; `delegate` and `exclusion` remain independent Standard-off vetoes, while `brotli` remains a Standard-off optional transform. No rules or Standard values are added or changed here.

**Ord is a reference implementation, not the data authority.** An independent parser can reproduce the inscription-envelope convention using Bitcoin data. Reference Ord commits and compatibility fixtures can be recorded and compared, but no automatic rolling Ord update changes the Bitmap interpretation. The existing Ord 0.29.1 commit pin documents only the optional [served-content](inscription-content-source.md) resolver (`content=1`, currently off), **not** a claimed global compatibility certification for envelope parsing. No whole-chain outcome-equivalence test is asserted. If a later parser or Ord release produces different results, document the divergence and review an explicit specification/profile revision before adopting it.

## Creator QA checkpoint (23 October 2026)

The creator approved the six Standard-on rules in the sequence `schema`, `body`, `text`, `ascii`, `height`, `order`. The `body` definition stays as written. The [Schema history](canonical-district-schema.md#history) preserves the former dollar-sign regex and explains the negative-lookahead hardening. The `order` comparator is block height, transaction index, then transaction-local Ord inscription index (`TXi`, lowercase `i`), incorporating input order and any multiple reveals within one input. Indices `0`–`5` are assigned to the six approved Standard-on rules only; all Standard-off rules remain unnumbered. No Standard values or production hashes change.
