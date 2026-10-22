# Strict UTF-8 decoding for District claims

**Code ID (provisional):** `strict`  
**Standard:** `1` (on; sole active District text decoder)  
**Earliest verified public code:** 5 December 2023 (Best in Slot's OPI Bitmap module)  
**Status:** Proposed current Bitmap Standard behaviour, corroborated by the public OPI decoder but not attributed to the unseen original 2023 Trac writer or every marketplace.

## Binary question

**Must selected District claim bytes be interpreted using strict UTF-8, regardless of any declared charset?** This is the current Standard's only decoding mode.

- **`1` (on):** Obtain the raw bytes from the **selected inscription source**, decode those bytes as **UTF-8 with strict error handling**, and pass the decoded string to the canonical District claim schema. **Invalid UTF-8 is rejected**, without replacement characters, charset fallback, Unicode normalization, trimming, decompressing, HTML extraction or JSON-object interpretation.
- **`0` (off):** This rule supplies **no decoder**. There is no active compatible/charset-aware fallback. Until an independent decoder is explicitly added and fully specified, `strict=0` is an incomplete, non-executable District profile. `0` does not mean lossy UTF-8 or skipped decoding.

**Raw bytes are the input; the string schema is checked *after* strict decoding.** This is an encoding rule, not a prohibition on MIME labels. Thus `text/plain;charset=utf-8` may satisfy the separate text MIME rule, but a `charset=utf-16` label is **not honored by this decoder**. MIME eligibility remains independently configured.

## Raw UTF-8 and canonical ASCII-byte equivalence

For an **entire exact canonical District claim** matching `(?:0|[1-9][0-9]*)\.bitmap`, all accepted characters are US-ASCII. RFC 3629 encodes US-ASCII characters in identical single octets in UTF-8. Therefore, strict raw UTF-8 decoding followed by a full canonical-string match accepts the **same candidate byte sequences** as a direct exact ASCII-byte match. This result assumes unchanged source bytes, no transformation or normalization and the canonical grammar. It does not grant eligibility to any alternative claim schema.

A UTF-8 BOM decoded as U+FEFF, leading/trailing whitespace, final newline, zero-width characters and invalid UTF-8 must not be removed to manufacture a canonical string. Charset metadata is ignored *for decoding* in this mode, but independently configured MIME and encoding-tag checks still apply.

**Strict UTF-8 is not MIME's US-ASCII fallback.** It ignores any declared `charset` for decoding. For example, a genuine UTF-16 body declared as `text/plain; charset=utf-16` may pass the *separate* MIME type rule, but its UTF-16 bytes do **not** pass `strict=1` for the canonical District grammar. [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html#section-3) documents the identical UTF-8/US-ASCII encoding of ASCII characters. The previously discussed charset-aware interpretation is deferred; see [encoding research](TEXT-ENCODING-COMPARISON.md).

## First public implementation evidence

- [5 December 2023 OPI Bitmap indexer source](https://github.com/bestinslot-xyz/OPI/blob/4987c31eacb6d77a56124daaa98fe2f2595cfb5b/modules/bitmap_index/bitmap_index.py#L57-L71) includes:
  ```python
  content = codecs.decode(content_hex, "hex").decode('utf-8')
  ```
  inside `try/except`. A decoding failure yields no District number. The function then validates the lowercase `.bitmap` suffix and numeric part. It does **not** select a decoder from declared `charset`.
- [Later OPI version](https://github.com/bestinslot-xyz/OPI/blob/main/modules/bitmap_index/bitmap_index.py#L133-L147) retains the same strict UTF-8 step. The initial code filters `text/plain` content type **separately** upstream; neither a MIME filter nor this decoder automatically enforces the other.
- [Trac-derived `ord-tap` initial public source, 19 September 2025](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater/tap/ops/bitmap.rs#L13-L23) instead uses Rust `String::from_utf8_lossy(body)`, which substitutes replacement characters for malformed UTF-8. That is a **different implementation technique**, though it need not change winner recognition under a purely ASCII District grammar.
- [Blockamoto's 21 October 2026 previous working options](https://github.com/Blockamoto/bitmap-old/blob/63e77aa6f5cd95248e3abad55e168fa2215e0e32/COMPARISON-OPTIONS.md) name `raw_utf8_strict` separately from `text=1` and from `declared_charset_strict`.

## Independence and implementation cautions

- [Inscription Body](inscription-body-source.md) versus [Inscription Content](inscription-content-source.md) chooses **whose bytes** to decode. OPI specifically reads its stored `content_hex` body input; this rule generalizes the strict decoder to whichever input source a profile selects. Do not equate “raw” with an implicit prohibition on delegates.
- [Plain-text MIME eligibility](plain-text-inscription.md) and any [MIME exceptions](json-mime-exception.md) remain separate. Setting this decoder to `1` never silently disables `text/plain` filtering.
- [Brotli eligibility](brotli-decompression-eligibility.md) controls whether bytes may be transformed *before* decoding. [Content-Encoding Tag Exclusion](content-encoding-tag-exclusion.md) tests mere field presence; neither is implied by strict UTF-8.
- A canonical District claim comprises only ASCII digits plus `.bitmap`. UTF-8 replacement characters created by a lossy decoder cannot by themselves form those exact valid bytes; therefore strict versus lossy handling of malformed UTF-8 alone may yield **no different accepted Districts** for that schema. A correctly declared UTF-16 body can differ from both UTF-8 paths when an independent charset-aware decoder is available.
- **`strict=1` is the only active decoding selection in the current District draft.** The earlier `mime_charset` proposal is not a selectable rule, and charset guessing, BOM stripping, Unicode normalization or fallback decoding are not permitted. No second decoder-combination constraint is needed. A future alternative would require its own explicitly specified rule, versioned decoder support and comparison fixtures; do not silently add it.
- Live OCI/Boppleton encoding semantics have not been independently source-verified in this audit. See [Encoding evidence comparison](TEXT-ENCODING-COMPARISON.md). Districts only.
