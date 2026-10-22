# Literal MIME string-prefix compatibility for District claims

**Code ID (provisional):** `mime_prefix_compatibility`  
**Default:** `0` (provisional compatibility option)  
**Earliest verified code snapshot:** 19 September 2025  
**Evidence class:** Public `Trac-Systems/ord-tap` implementation.

## Definition

When enabled, a District candidate's MIME eligibility is checked using the same **literal string-prefix behaviour** observed in the Trac-derived Rust intake gate, rather than accepting only a syntactically valid exact/base media type. For each MIME branch allowed by the selected profile:

- `text/plain` is matched by `starts_with("text/plain")`;
- `application/json` is matched by `starts_with("application/json")` only when the [JSON MIME exception](json-mime-exception.md) is enabled;
- the original broad `text/` prefix is matched when the [Text MIME family exception](text-mime-family-exception.md) is enabled.

Thus the historical code can admit malformed labels such as `text/plainbogus` or `application/jsonbogus` that merely start with those bytes. MIME compatibility **does not** relax the District inscription's required exact canonical `<height>.bitmap` body.

## History and evidence

- [Initial public Rust port, 19 September 2025](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater.rs#L984-L989): `ct.starts_with("text/") || ct.starts_with("application/json")`.
- [25 September 2025 commit `acf6b7b`](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea): text branch narrowed to `starts_with("text/plain")`; JSON prefix behaviour remained.
- The code applies the MIME test to the original payload in the first snapshot and to the one-level effective payload after 25 September. Which content fields a District rule should consult is a **separate unresolved registry decision**, not defined by this MIME option.
- No code proving the original 2023 Trac service used these literal prefix checks has been recovered.

## Clarifications

- This option is **conditional on the allowed MIME alternatives**; it does not enable `application/json` or arbitrary `text/*` by itself.
- A proper parameter like `text/plain;charset=utf-8` can already be valid under the baseline parsed-media-type policy. This option targets invalid/inexact prefix matches.
- Distinguish a string-prefix implementation quirk from a deliberate specification requiring certain MIME media types.
- Further tests should check candidate MIME labels and whether any accepted District winner actually depends on the quirk.
- Default `0` and registry numbering are provisional pending Standard-profile review.
