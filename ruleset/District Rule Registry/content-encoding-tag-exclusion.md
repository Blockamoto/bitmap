# Content-Encoding Tag Exclusion for District claims

**Code ID (provisional):** `encoding_tag_exclusion`  
**Default:** `0` (off; independent metadata veto)  
**Earliest verified explicit published formulation:** 21 October 2026 (`Blockamoto/bitmap-old` atomic District specification)  
**Original 2023 introduction and individual indexer enforcement:** Unverified.

## Single binary question

**Must a District candidate be rejected merely because its own authenticated Ord inscription envelope declares content-encoding tag 9, irrespective of its content bytes?**

- **`1`:** Exclude any claimant whose inscription fields contain **exact Ord `content_encoding` tag 9** before the body separator. Its value may be `br`, `gzip`, empty, malformed, unsupported, repeated, or unresolved: field **presence**, not successful decompression, triggers the exclusion.
- **`0` (default):** Do **not** reject a District claim solely because it declares an encoding tag. All source, MIME, decoding, schema and transform rules still apply.

The field check must use an authenticated parsed inscription envelope. Tag-looking bytes inside the body or unrelated field values do not establish field presence. If envelope evidence is unavailable, the presence predicate is **unknown**, never silently absent.

## History and evidence

- [21 October 2026 comparison specification](https://github.com/Blockamoto/bitmap-old/blob/63e77aa6f5cd95248e3abad55e168fa2215e0e32/COMPARISON-OPTIONS.md) explicitly defines `encoding_tag_exclusion=0`, separate from `body_transform=none`.
- [21 October 2026 District binary rules](https://github.com/Blockamoto/bitmap-old/blob/63e77aa6f5cd95248e3abad55e168fa2215e0e32/DISTRICT-RULESET.md) records `encoding_tag_exclusion` as an optional independent default-off comparison question.
- [Ord inscription field documentation](https://docs.ordinals.com/inscriptions.html#fields) distinguishes `content_encoding` tag **9** from `delegate` tag **11** and `property_encoding` tag **19**. Property encoding tag 19 does **not** trigger this veto.
- [Prior indexer comparison](TEXT-ENCODING-COMPARISON.md): Trac-derived Rust and OPI's checked Bitmap module have **no visible explicit encoding-tag veto** in their District parsers; Live OCI reportedly disallows all `contentEncoding` tags, but its exact current implementation and introduction date have **not** been independently checked.

## Independent of Brotli and charset

This is a **declaration-based eligibility exclusion**, not a text decoder and not a decompression allowance. The [Brotli Decompression Eligibility](brotli-decompression-eligibility.md) rule controls whether transformed content may qualify. Charset selection (`utf-8`, `utf-16`, etc.) under a `Content-Type` parameter is also a separate operation.

This rule remains separate from delegate-tag exclusion and nested-delegate exclusion. Districts only; no Parcel rules are adopted.
