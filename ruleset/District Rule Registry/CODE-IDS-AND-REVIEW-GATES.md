# District rule code IDs and production review gates

**Status:** Draft identifiers, reviewed 23 October 2026. Not numeric bit indices, an executable ruleset, a frozen serialization contract or authorization to commit production hashes.

## Naming and authority

The [District registry](README.md) is the source of the current IDs, order and Standard values. IDs identify one binary question; display titles, filenames, historical evidence IDs and future bit positions are separate. Descriptive filenames are retained where useful so existing links continue to resolve.

There are **16** active IDs:

`schema`, `body`, `ascii`, `height`, `order`, `text`, `content`, `number`, `fallback`, `json`, `brotli`, `exclusion`, `nested`, `negative`, `delegate`, `prefix`.

The first six have proposed Standard value `1`; the remaining ten have value `0`. `text` remains immediately after `order` and before `content`. `prefix` remains last. No numeric `Index` positions have been allocated.

## Latest one-word consolidation

| Previous draft ID | Current ID | Change |
| --- | --- | --- |
| `brotli` | `brotli` | Retained; transform permission is separate from tag rejection and HTTP delivery. |
| `encoding_tag_exclusion` | `exclusion` | Rename only; claimant's own raw tag 9 presence. |
| `nested_delegate_exclusion` | `nested` | Rename and precision correction: the evidenced Trac check tests decoded delegate references, not every malformed raw declaration. |
| `negative_inscription_number_exclusion` | `negative` | Rename only; exact signed-number predicate, not a blanket cursed-status veto. |
| `delegate_exclusion` | `delegate` | Rename only; claimant's own raw tag 11 presence. |
| `prefix` | `prefix` | Retained at the bottom; literal case sensitivity and OPI evidence clarified. |

The [six-rule audit](SIX-RULE-AUDIT.md) records why none of these six independent questions was deleted or merged. Old identifiers quoted inside dated historical evidence remain historical, not extra active bits.

## Earlier mappings

The earlier [short District reference](https://github.com/Blockamoto/bitmap-old/blob/main/DISTRICT-RULESET.md) and [research/provenance IDs](https://github.com/Blockamoto/bitmap-old/blob/old/rules/README.md) use different naming systems. `BMP-DISTRICT-*` and related evidence IDs must not be read as numeric bit allocations.

| Earlier identifier | Current entry | Mapping or boundary |
| --- | --- | --- |
| `text` | `text` | Independent `text/plain` MIME eligibility, not charset decoding. |
| `regex` | `schema` | Canonical whole-claim grammar, named for the schema rather than its mechanism. |
| `height` | `height` | Inclusive `target_height <= reveal_height`. |
| `content=1` (historic own-body meaning) | `body` | Not an alias for the current served-source `content` ID. |
| `first`, `fiftxi`, `precedence_bitcoin_reveal`, brief `fif` | `order` | First eligible claimant by block, transaction, input and in-input envelope reveal order. No separate first-wins bit. |
| `fifin` | `number` | Closest signed-number ordering alternative; old replacement-mode semantics require attention. |
| `raw_utf8_body` | `ascii` plus source and MIME choices | The older compound setting also chose a body and bypassed MIME; not an exact alias. |
| `decoder_mode=raw_utf8_strict`, brief `strict` | `ascii` | Same qualifying bytes under the exact ASCII-only District grammar, not identical rule identifiers. |
| `decoder_mode=declared_charset_strict`, `mime_charset` | No active bit | Deferred [encoding research](TEXT-ENCODING-COMPARISON.md), not an implicit decoder fallback. |
| `cursed_exclusion` | Related to `negative`, not an exact alias | A general cursed-status interpretation can differ from signed-number comparison. |
| `json_mime` | `json` | MIME-label alternative only; prefix matching belongs to `prefix`. |
| `mime_prefix_compatibility` | `prefix` | Literal MIME prefix comparator; this is not charset compatibility. |
| `delegate_content_resolution` | No active bit | Normal one-hop resolution belongs to `content`; the distinct failed-lookup override is `fallback`. |
| `text_mime_family` | No active bit | The brief 2025 broader text intake is history under [`text`](plain-text-inscription.md). |
| `precedence_unix_timestamp` | No active bit | Creator recollection and technical limitations remain [history under `order`](order.md#historical-notes). |
| `reinscription_exclusion` | No active bit | Explicitly deferred on 22 October 2026; retain [earlier evidence](https://github.com/Blockamoto/bitmap-old/blob/old/edge-cases/reinscriptions.md), not a newly adopted ban. |

## Production gates, still open

1. **Complete profile:** choose claim source, schema, MIME semantics, byte interpretation, eligibility and a complete winner policy. Proposed defaults do not prove a complete execution contract.
2. **Schema:** `schema=1` is the sole active claim grammar. `schema=0` has no defined replacement. Use a true full-string match; do not admit a final newline because a regex engine lets `$` match before it. No trimming or normalization.
3. **Source composition:** define or reject both `body=0; content=0` and `body=1; content=1`. Do not invent OR, AND or source precedence. `fallback` changes a failed delegate lookup within enabled `content`, not arbitrary source combinations.
4. **Resolution and snapshots:** pin Ord 0.29.1's source-resolution semantics to commit `d2ff0a789033e3d784048a23e856f15c54e88806`, along with replay state, same-block availability and missing-target/error behavior. A network or local database failure must not masquerade as a historical on-chain fact. Raw tag-presence checks and decoded-value accessors are different predicates.
5. **Transforms:** `content` does not secretly enable HTTP auto-decompression. `brotli=1` needs an adopted trigger, source metadata, stream/failure policy, decoder version and safe output bounds. A tagged single-decode route is proposed, not frozen. Gzip is neither implied nor added as an active bit in this pass.
6. **MIME and bytes:** `ascii=1` ignores declared charset; `ascii=0` has no defined alternative decoder. `text=1` stays on pending historical comparison. `json` selects an additional label; `prefix` selects a comparator. Under the agreed no-MIME-filter interpretation of `text=0`, these label/comparator modifiers are inert. Pin the parsed-MIME policy and distinguish Trac's UTF-8 string intake from OPI's hex-prefix intake before claiming exact indexer equivalence.
7. **Winner selection:** `order` specifies Bitcoin reveal order; `number` is an alternative, not an extra hidden component. Resolve or reject conflicting enabled comparators. `negative` is eligibility only and is not implicitly enabled by `number`.
8. **Evidence and fixtures:** authenticate actual witness bytes, parsing, source selection, MIME/coding metadata, envelope positions, signed-number provenance and same-District collisions. The [32 synthetic checks](six-rule-checks.py) demonstrate counterexamples only; they do not establish deployed behavior or identical historical winners.
9. **Live OCI:** exact implementation identity and parser remain unverified in this pass. Do not equate truthiness of exported properties with raw tag presence for empty, malformed, repeated or incomplete fields.
10. **No premature freeze:** numeric positions, serialized profiles, production hashes and a final production validator remain outside this documentation pass. A clean historical comparison to a fixed tip would not prove identical behavior for future inscriptions.

## Deliberately excluded historical typo

The withdrawn `#<height>.bitmap` tutorial typo is not selectable. Preserve its history through the [earlier tutorial revision](https://gitbook.bitmap.land/~/revisions/AZO0a8slhI90dZCq0SNg/) and [archived verification guide](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/archive/_old/bitmap-theory-101/how-to-verify-blocks.md), not as a switch accepting hash-prefixed claims.

**Scope:** District-only draft branch. No Parcel, `main`, frozen hash or deployed-validator changes.
