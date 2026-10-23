# District rule code IDs and production review gates

**Status:** Provisional code identifiers, reviewed 22 October 2026. **Not numeric bit indices**, an executable ruleset, a frozen serialization contract, or authorization to commit production hashes.

## Naming convention

Short lowercase `snake_case` names identify **one current binary registry question** and are stable *within this draft review*. The [District registry](README.md) now presents one continuous table with the columns **Index**, **ID**, **Standard** and **Definition**. The code ID links to its detail page; no separate human-readable name or evidence-date column appears in the overview. The registry remains the source of the currently included set. Code IDs are distinct from display titles, former compound aliases, dated evidence IDs, and future binary positions.

Earlier work had at least two naming systems:

- **Short rule IDs** in [`bitmap-old` District reference](https://github.com/Blockamoto/bitmap-old/blob/main/DISTRICT-RULESET.md): `content`, `text`, `regex`, `height`, `first` and `fiftxi`, with optional `fifin`, `brotli`, `delegate_exclusion`, `encoding_tag_exclusion`, and other exclusion bits.
- **Research/provenance IDs** such as `BMP-DISTRICT-001`, `BMP-CONTENT-003`, `BMP-ORD-001` and `BMP-ORDER-003` in [the older repository's `old` branch](https://github.com/Blockamoto/bitmap-old/blob/old/rules/README.md). These classify claims/evidence and **must not be misread as numeric bit allocations**.

## Exact or close carryovers

| Earlier identifier | Present code ID | Mapping |
| --- | --- | --- |
| `text` | `text` | Same independent `text/plain` media-type check; charset decoding is no longer hidden inside it. |
| `regex` | `schema` | Same canonical `<height>.bitmap` full-string grammar, now named for the District claim schema rather than its matching mechanism; independent of claim source. |
| `height` | `height` | Same inclusive `target_height ≤ reveal_height` check. |
| `brotli` | `brotli` | Same default-off *additional Brotli-decompression eligibility*, not an encoding-tag veto. |
| `delegate_exclusion` | `delegate_exclusion` | Same default-off exclusion based on a declared Ord delegate tag. |
| `encoding_tag_exclusion` | `encoding_tag_exclusion` | Same default-off exclusion for Ord content-encoding tag 9 presence. |
| `decoder_mode=raw_utf8_strict` | `ascii` | Historical strict UTF-8 interpretation; for an exact ASCII-only District claim it accepts the same bytes as current `ascii=1`. Not the same rule identifier. |
| `decoder_mode=declared_charset_strict` | **No active rule (deferred)** | Previously proposed charset-aware compatibility interpretation; retained as [encoding research](TEXT-ENCODING-COMPARISON.md), not a present Standard setting, binary ID or fallback. |

## Related historical names that are **not exact aliases**

| Earlier name | Current related entry | Important difference |
| --- | --- | --- |
| `content=1` (historical) | `body=1` (current) | The old `content` rule meant the inscription's **own body**. The present `content=0` rule instead selects **served content** (possibly delegated). These are distinct and the reused word must not be treated as a lossless alias. |
| `first=1` | `order=1` | The former standalone first-wins switch was merged with Bitcoin reveal-order precedence (briefly called `fif`), now `order`; no separate active `first` bit remains. |
| `fiftxi=1` / `precedence_bitcoin_reveal=1` | `order=1` | The current rule specifies first eligible claimant by Bitcoin block, transaction, input and in-input inscription reveal order (TXI). Earlier IDs remain historical identifiers, not active bits. |
| `fifin=1` | `number=1` | Closest historical alternative by lowest signed global inscription number, but old mode also specified *replacement* of the Bitcoin comparator. Incompatible simultaneous precedence modes must be rejected or resolved by declared rules. |
| `raw_utf8_body=1` | `ascii=1` + selected source and independent MIME | The older compound `raw_utf8_body` implicitly bypassed MIME and selected the own body; ASCII interpretation **does not** choose a source or bypass the MIME filter. |
| `cursed_exclusion=1` | `negative_inscription_number_exclusion=1` | **Not equivalent:** the current candidate tests negative signed number, not every wider curse/vindication status. Default 0 imposes no negative-number veto; no new cursed-status veto is silently adopted. |
| `reinscription_exclusion=1` | **Not currently active** | Explicitly deferred by creator on 22 October 2026. Preserve [old evidence](https://github.com/Blockamoto/bitmap-old/blob/old/edge-cases/reinscriptions.md), but do not add a live toggle merely because older OPI filtered cursed inscriptions. |

## Current identifier inventory

The **16** code IDs appearing on [README](README.md) are unique within the active draft. `schema=1` is the only canonical District grammar, `ascii=1` the only active byte-interpretation rule, and `order=1` the single current first-eligible-wins policy with Bitcoin transaction/input reveal order (TXI). Earlier standalone `first` and `precedence_bitcoin_reveal` rows were consolidated (briefly under the draft ID `fif`) into `order`, not retained as extra binary positions. The `mime_charset` proposal is withdrawn from the active registry. Other alternative IDs include `content`, `fallback`, `json`, `mime_prefix_compatibility`, `nested_delegate_exclusion`, `negative_inscription_number_exclusion` and `number`. None is asserted to have existed with these exact new names in 2023. The former default-off `precedence_unix_timestamp` draft entry was removed on 23 October 2026; the unverified early time-ordering recollection and its technical limitations are preserved only in [Order history](order.md#historical-notes), not as a binary option.

## Production review gates, still open

1. **Foundational decision completeness:** executable District profiles must select a claim source, schema, MIME and byte-interpretation semantics, eligibility rules, and a complete winner-selection policy such as `order`. Defaults are proposed values, not proof of a completed execution contract.
2. **Canonical claim grammar:** [`schema=1`](canonical-district-schema.md) is the sole active District schema, matching the separately published [District regex](district-claim.regex). A profile with `schema=0` has no defined alternative schema and is not executable. Enforce a true full-string match; merely searching with `^...$` can admit a final newline in some regex engines. Never trim, normalize, or permit extra characters.
3. **Claim-source combinations and unresolved delegates:** define or reject `body=0; content=0` and `body=1; content=1`. Do not invent OR, AND, source precedence, or implicit source fallback. `content=1` resolves served content under **pinned Ord `0.29.1` semantics**, with no claimant-body fallback for an unresolved delegate by default. The distinct [`fallback=1`](fallback.md) comparison rule instead supplies the claimant's own body and MIME **only when that delegate lookup fails**; it has no effect with `content=0`. The retired `delegate_content_resolution` code ID is not an active option. Historic `content=1` meant own-body input and must not be confused with the current `content` ID.
4. **Winner selection and alternative precedence:** [`order=1`](order.md) means the first eligible claim in Bitcoin block, transaction, input and within-input inscription reveal order (TXI). The optional `number` row is a separate comparison policy, not an extra part of `order`; Unix-timestamp ordering has been retired from the registry and is [history only](order.md#historical-notes). Any profile enabling conflicting winner procedures must define an explicit combination or be rejected. A versioned Ord parser and repeatable fixtures must establish physical reveal order before production.
5. **Data source, MIME, byte interpretation:** [`ascii=1`](ascii-byte-matching.md) interprets selected bytes as US-ASCII regardless of the declared charset; a full canonical schema match accepts precisely the canonical ASCII byte sequence. This is also valid UTF-8 and matches the previous strict UTF-8 District outcome. The independent `text` MIME filter is not bypassed. `ascii=0` has no defined replacement byte-interpretation mode in this draft; the discarded MIME-charset alternative remains [research only](TEXT-ENCODING-COMPARISON.md). Pin the envelope parser, MIME handling, transformation rules and fixtures before production.
6. **Transform and metadata:** an enabled `brotli` eligibility route needs trigger, decompression limits and failure policy. `encoding_tag_exclusion` is a separate tag-presence veto. No inference from an unverified Live OCI implementation.
7. **Evidence and reproducibility:** fixture inputs must include actual witness bytes, source policy, chain reveal coordinates, collisions, delegated content, encoding edge cases, effective MIME fields and declared profile. Verify version-specific indexer claims rather than declaring historical consensus from one modern source.
8. **No premature allocation:** blank `Index` values, provisional code names and defaults, no canonical serialized profile, no deployed hashes or final production validator.

## Deliberately excluded historical typo

The 3 June 2023 `#<height>.bitmap` tutorial typo was withdrawn/corrected by 14 June, and the 16 June verification guide rejected `#69.bitmap`. The creator has directed that it **not be an active District rule**. Preserve it as documentation history via the [earlier tutorial revision](https://gitbook.bitmap.land/~/revisions/AZO0a8slhI90dZCq0SNg/) and [archived verification guide](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/archive/_old/bitmap-theory-101/how-to-verify-blocks.md), not as a switch that recognizes `#<height>.bitmap`.

**Scope:** District-only. No Parcel or `main` updates.
