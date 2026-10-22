# MIME charset-aware decoding for District claims

**Code ID (provisional):** `mime_charset`  
**Standard:** `1` (proposed current-profile interpretation; not a production-decoder guarantee)  
**Explicit registry formulation:** 22 October 2026  
**Historical status:** A standards-grounded 2026 interpretation of original “text inscription” language, **not** evidence that the 2023 Trac service or original authored rule implemented this behaviour.

## Binary question

**When the selected District claim source qualifies as `text/plain`, must its bytes be decoded according to the declared MIME `charset`, rather than ignoring that declaration?**

- **`1` (on):** Use the charset explicitly declared on the applicable `text/plain` content type. If it declares none, use the **US-ASCII MIME default** retained by [RFC 6657 §4](https://www.rfc-editor.org/rfc/rfc6657.html#section-4) from [RFC 2046 §4.1.2](https://www.rfc-editor.org/rfc/rfc2046.html#section-4.1.2). Decode under a pinned charset implementation and compare the **entire decoded string** against the independently enabled District claim schema. Do not substitute a browser's unspecified heuristics or assume the body is always UTF-8.
- **`0` (off):** This option supplies no decoder. The profile needs another explicit choice such as [`raw_utf8_strict`](raw-utf8-strict-decoding.md); `0` by itself does not imply a fallback decoder.

**MIME type eligibility remains separate:** [`text`](plain-text-inscription.md) determines whether `text/plain` is required; a decoder cannot grant an otherwise ineligible MIME label. If optional MIME exceptions allow `text/*` or `application/json`, their charset defaults and interactions with this option must also be specified, since the US-ASCII fallback cited here is expressly for `text/plain`.

## Distinguishing examples

- `840000.bitmap` stored as ordinary ASCII-compatible bytes, with `text/plain` and no charset, yields exactly the canonical string under either strict US-ASCII or strict raw UTF-8. No decoder disagreement on those bytes.
- `840000.bitmap` encoded as UTF-16 with a correctly declared `text/plain; charset=utf-16` may decode to the canonical string under this mode. The **different raw UTF-16 bytes** are not the canonical ASCII-byte sequence and do not pass the raw UTF-8 mode.
- A false declaration (`charset=utf-16` but ASCII bytes), an unsupported charset label, invalid encoded bytes, or contradictory BOM/charset indicators can produce different results. **No guessing, replacement, silent UTF-8 fallback, BOM stripping or charset override is approved here.** These cases require deterministic shared test vectors and final rule text before production.
- A byte-order mark, newline or extra character may be significant; no trimming, Unicode normalization or substring search is implicit.

## Independence and open production dependencies

This is a **decoder selector**, independent of the [inscription's own body versus served-content source](DISTRICT-CONTENT-OPEN-QUESTION.md), the [MIME type predicate](plain-text-inscription.md), [Brotli transformation](brotli-decompression-eligibility.md), and [content-encoding tag veto](content-encoding-tag-exclusion.md). Those questions are not answered by choosing a charset decoder.

The two registry bits `mime_charset` and `raw_utf8_strict` describe **alternative interpretations**. Proposed Standard uses `mime_charset=1`, `raw_utf8_strict=0`. Neither both-on nor both-off combination currently has agreed executable semantics: a production profile must select exactly one decoder or explicitly define another composition policy before evaluation.

**Unresolved and not backdated:** supported IANA charset names and aliases; exact decoder algorithms/version; which source's charset applies when effective content comes from a delegate; malformed/duplicated parameters; charset/BOM/endian choices; decoding failures; non-`text/plain` MIME exceptions; and any historical on-chain cases where accepted District winners differ.

An [IANA character-set registration](https://www.iana.org/assignments/character-sets) does not guarantee an arbitrary browser or programming language can decode it. The [WHATWG Encoding Standard](https://encoding.spec.whatwg.org/) defines its **own** supported labels and algorithms, which are not identical to all IANA registrations. A Bitmap standard must pin an actual decoder policy rather than rely on implementation defaults.

## Evidence and comparison

- [RFC 2046 §4.1.2](https://www.rfc-editor.org/rfc/rfc2046.html#section-4.1.2): media-type `charset` and plain-text default.
- [RFC 6657 §4](https://www.rfc-editor.org/rfc/rfc6657.html#section-4): retains the `text/plain` default as US-ASCII, while other `text/*` subtypes can have different rules.
- [RFC 3629 §3](https://www.rfc-editor.org/rfc/rfc3629.html#section-3): UTF-8 has exactly the same single-octet encoding for US-ASCII characters.
- [OPI vs Trac vs Live OCI audit](TEXT-ENCODING-COMPARISON.md): OPI's strict UTF-8 and Trac-derived lossy UTF-8 are **observed later implementations**, not proof of how the original 2023 author intended MIME decoding.

District claims only. No Parcel rule, main-branch policy or committed Bitmap Chain fingerprint is changed.
