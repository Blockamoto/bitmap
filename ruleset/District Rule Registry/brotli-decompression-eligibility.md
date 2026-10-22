# Brotli decompression eligibility for District claims

**Code ID (provisional):** `brotli`  
**Default:** `0` (off; historical comparison option)  
**Earliest verified published working rule:** 15 October 2026 (`Blockamoto/bitmap-old`)  
**Original 2023 introduction and indexer enforcement:** Unverified.

## Single binary question

**May a District claim qualify solely because its selected body bytes are decompressed with Brotli before applying the selected text decoder and canonical District schema?**

- **`0` (default):** No **Brotli-derived eligibility**. A candidate is not made valid by decompressing its stored/selected bytes. Normal untransformed body eligibility remains governed by the independently selected content source, MIME, decoder and schema.
- **`1`:** Enable a **Brotli-decompression eligibility route** for candidate content. The *decompressed* result must still satisfy the selected District schema and all separately enabled eligibility rules.

**A body-transform permission is not an encoding-tag exclusion.** Rejecting any inscription that merely declares a `content_encoding` tag is a separate default-off [Content-Encoding Tag Exclusion](content-encoding-tag-exclusion.md) option. These may be configured independently; an exclusion, if active, still vetoes candidates under its own predicate.

## Historical evidence

- [15 October 2026 original District working specification](https://github.com/Blockamoto/bitmap-old/blob/1751e0d37073ab920cbd8b5548c61b74c37716d1/DISTRICT-RULESET.md) explicitly includes `brotli=0`, meaning no extra validity solely from Brotli decompression.
- [16 October 2026 follow-up](https://github.com/Blockamoto/bitmap-old/blob/ccf7271a61a2cead4781d4a2bb9c86da761f1cd6/DISTRICT-RULESET.md) retains `brotli=0`.
- [21 October 2026 atomic separation](https://github.com/Blockamoto/bitmap-old/blob/63e77aa6f5cd95248e3abad55e168fa2215e0e32/COMPARISON-OPTIONS.md) retains Standard `body_transform=none` and explains that the former `brotli` choice was an **additional decompression route**, distinct from any tag-presence veto. The `body_transform` pipeline was **not yet frozen**.
- [Current decoding and indexer comparison](TEXT-ENCODING-COMPARISON.md) describes the prior Trac, OPI and Boppleton/Live OCI findings, preserving their different evidentiary status.

## Remaining interpretation and reproducibility work

An enabled `1` cannot be evaluated reproducibly without specifying: exactly when decompression is attempted, whether a `content_encoding: br` declaration is required, one versus multiple decompression attempts, failure handling, a maximum expansion/output size, and how decompression feeds the separately chosen text decoder. Do **not** silently interpret a tag as meaning the bytes were decompressed or that any compressed claim is valid.

`gzip` is **not** automatically enabled by this Brotli-specific bit; any other transform must be specified separately. A lack of relevant historical examples or unverified third-party implementations does not prove that no outcomes differ.

This applies to **Districts only**. The two independent [Inscription Body / Inscription Content](DISTRICT-CONTENT-OPEN-QUESTION.md) source rules select which bytes enter the transform stage; this Brotli rule does not select a source or bypass MIME eligibility.
