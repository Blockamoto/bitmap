# Raw strict UTF-8 decoding for District claims

**Code ID (provisional):** `raw_utf8_strict`  
**Standard:** `0` (off; independent decoding alternative)  
**Earliest verified public code:** 5 December 2023 (Best in Slot's OPI Bitmap module)  
**Status:** Historical comparison option; its `1` behaviour is evidenced in OPI, not attributed to the 2023 Trac service.

## Binary question

**Must selected District claim bytes be interpreted using strict UTF-8, regardless of any declared charset?**

- **`1` (on):** Obtain the raw bytes from the **selected inscription source**, decode those bytes as **UTF-8 with strict error handling**, and pass the decoded string to whichever District claim schema is enabled. **Invalid UTF-8 is rejected**, without replacement characters, charset fallback, Unicode normalization, trimming, decompressing, HTML extraction or JSON-object interpretation.
- **`0` (off):** Do **not** impose this raw UTF-8 decoder override. The profile must select its independent decoder, for example the proposed Standard's [`mime_charset=1`](mime-charset-decoding.md) interpretation of MIME-declared charsets. `0` is not permission to skip decoding or to assume lossy UTF-8.

**Raw bytes are the input; the string schema is checked *after* strict decoding.** This is an encoding rule, not a prohibition on MIME labels. Thus `text/plain;charset=utf-8` may satisfy the separate text MIME rule, but a `charset=utf-16` label is **not honored by this decoder**. MIME eligibility remains independently configured.

## Raw UTF-8 and canonical ASCII-byte equivalence

For an **entire exact canonical District claim** matching `(?:0|[1-9][0-9]*)\.bitmap`, all accepted characters are US-ASCII. RFC 3629 encodes US-ASCII characters in identical single octets in UTF-8. Therefore, strict raw UTF-8 decoding followed by a full canonical-string match accepts the **same candidate byte sequences** as a direct exact ASCII-byte match. This result assumes unchanged source bytes, no transformation or normalization and the canonical grammar. It is **not** asserted for historical BMP101 JSON or arbitrary text schemas.

A UTF-8 BOM decoded as U+FEFF, leading/trailing whitespace, final newline, zero-width characters and invalid UTF-8 must not be removed to manufacture a canonical string. Charset metadata is ignored *for decoding* in this mode, but independently configured MIME and encoding-tag checks still apply.

**This mode is not the MIME US-ASCII default.** The [MIME charset mode](mime-charset-decoding.md) respects an explicitly declared `charset=utf-16` (subject to pinned decoding details), whereas raw strict UTF-8 does not; the two modes coincide for ordinary canonical ASCII bytes. [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html#section-3) documents the UTF-8/US-ASCII byte identity.

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
- The proposed `mime_charset` mode is an alternative selector, not a simultaneous check. Both-on and both-off combinations are currently undefined and require explicit profile validation before indexing. This new `0` bit alone does not fully specify the baseline decoder, label registry, BOM treatment, or absent-charset fallback. Those must be pinned independently before execution.
- Live OCI/Boppleton encoding semantics have not been independently source-verified in this audit. See [Encoding evidence comparison](TEXT-ENCODING-COMPARISON.md). Districts only.
