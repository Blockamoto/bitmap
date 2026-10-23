# Brotli

**Code ID:** `brotli`  
**Standard:** `0`  
**Scope:** An additional body-transform eligibility route, not a content source, MIME check or tag-presence veto.  
**Evidence status:** Explicit Bitmap working proposal by 15 October 2026. This is not a verified original 2023 rule or proof that a major Bitmap validator accepts compressed claims.

## Definition

When enabled, permit a candidate derived by **Brotli-decompressing the selected stored body bytes**, then apply the independently enabled ASCII, exact District schema, height and eligibility checks to the result.

When disabled, decompression cannot confer additional eligibility. This does **not** reject an otherwise valid raw claim merely because an encoding tag exists. Raw-byte evaluation remains separate; a failed transformed route does not by itself erase a valid raw route.

Selecting `body` or `content` determines which inscription supplies bytes. It does not silently enable this transform. `brotli` does not enable gzip, charset transcoding, repeated decompression, whitespace trimming or JSON extraction.

## Bitcoin, Ord and HTTP are different layers

Bitcoin supplies the committed witness bytes; a reader can explicitly decompress those bytes without asking Ord. The distinction is the reader's transformation policy, not whether the data came from Bitcoin or from an Ord node.

The audited reference is **Ord 0.29.1, commit `d2ff0a789033e3d784048a23e856f15c54e88806`**:

- [`Inscription::body()` / `into_body()`](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/inscriptions/inscription.rs) return stored body bytes. They do not automatically decompress them.
- [`content_response`](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/subcommand/server/r.rs#L283-L357) can return those bytes with a `Content-Encoding` header when the requested coding is acceptable to the client. A client may then decode them.
- The server-side fallback explicitly decompresses **Brotli** only when `server_config.decompress` is enabled and the client has not accepted that coding. Otherwise the response may be not acceptable. An Ord URL alone therefore does not identify which byte representation the caller evaluated.
- Ord's wallet compressor uses Brotli and retains compressed bytes only when they are smaller. A short canonical claim need not become compressed just because `--compress` was requested. This is a wallet-production choice, not a validity rule for inscriptions produced by other software.

The inspected [Trac-derived Bitmap parser](https://github.com/Trac-Systems/ord-tap/blob/b8f6ea35cf6b9d405d4db7c58555e3c8ab33e8cd/src/index/updater/inscription_updater/tap/ops/bitmap.rs#L4-L42) reads the selected raw `body()` through UTF-8 without a Brotli decode. The [historical OPI parser](https://github.com/bestinslot-xyz/OPI/blob/4987c31eacb6d77a56124daaa98fe2f2595cfb5b/modules/bitmap_index/bitmap_index.py#L57-L71) similarly decodes supplied body hex as UTF-8. The latter observation does not independently audit every upstream OPI export or deployment.

## Why this is not `exclusion`

A raw body `123.bitmap` carrying tag 9 can pass raw ASCII/schema checks while `brotli=0`, but [`exclusion=1`](content-encoding-tag-exclusion.md) rejects it because the tag exists. Conversely, a genuinely compressed claim can fail raw matching while becoming eligible through an enabled decompression route. One question is about transforming bytes; the other is about vetoing a declaration. Neither replaces the other.

`exclusion` checks the claimant's own envelope. When `content` selects a delegate's body, that delegate's coding metadata and the claimant's tag-presence predicate are not interchangeable.

## Gzip

Gzip is a **different transform**, not included in `brotli`. The pinned Ord server can pass a stored `gzip`-labelled body to a client advertising gzip, but its built-in `--decompress` fallback is Brotli-specific. See [`AcceptEncoding`](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/subcommand/server/accept_encoding.rs) and `content_response` above.

No active `gzip` bit is added in this six-rule consolidation. A gzip comparison would need its own defined route and supporting Bitmap comparison target. Server transport coding, client decoding support and demonstrated District acceptance must not be conflated.

## Execution details still requiring review

The existing draft permitted an additional route without freezing its trigger. This audit does **not** silently settle that missing policy. Before enabling it in an executable profile, specify tag-required versus explicit untagged decoding, the selected source of coding metadata, exactly one versus repeated decoding, stream consumption/trailing-data handling, failure policy, decoder version, output bounds and any conflicting raw/decoded claim outcome.

A conservative proposal is one decode when the selected source declares exactly `br`, no sniffing and no recursive decoding. This is a **proposal for review**, not an extra implicit rule. With canonical schema and `height=1`, a qualifying result cannot exceed `decimal_digits(reveal_height) + 7` bytes, so that bound can reject overlong output without discarding a qualifying District string. Profiles lacking those prerequisites need a separately specified bound. Resource or data-fetch failures must not be silently converted into consensus invalidity.

## History

The [15 October working specification](https://github.com/Blockamoto/bitmap-old/blob/1751e0d37073ab920cbd8b5548c61b74c37716d1/DISTRICT-RULESET.md) and [16 October revision](https://github.com/Blockamoto/bitmap-old/blob/ccf7271a61a2cead4781d4a2bb9c86da761f1cd6/DISTRICT-RULESET.md) record `brotli=0`. The [21 October atomicity revision](https://github.com/Blockamoto/bitmap-old/blob/63e77aa6f5cd95248e3abad55e168fa2215e0e32/COMPARISON-OPTIONS.md) separates transform permission from encoding-tag exclusion. These are specification history, not proof of historic indexer enforcement.

[Registry](README.md) · [Audit report](SIX-RULE-AUDIT.md).
