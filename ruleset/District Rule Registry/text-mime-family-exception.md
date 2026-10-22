# Text MIME family exception for District claims

**Default:** `0`  
**Introduced:** 19 September 2025

## Definition

When enabled, accept a District inscription whose declared MIME content type begins with `text/`, including subtypes other than `text/plain`, **provided the inscription content still matches the canonical exact `<height>.bitmap` District syntax and all other enabled District validity checks**.

This is a MIME eligibility alternative, not a relaxation of the District claim's content.

## History and evidence

- [Initial public Trac-derived `ord-tap` implementation, 19 September 2025](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater.rs) used the shared filter `ct.starts_with("text/") || ct.starts_with("application/json")` before passing inscriptions into District indexing.
- [25 September 2025 commit](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) narrowed that filter to `text/plain` or `application/json`. The broader text-family behaviour is therefore present in a historical public indexer revision but not in the current code.
- The listed date is **the first verified public snapshot**, not proof of when the original 2023 Trac production writer first accepted the broader family.

## Clarifications

- Independent from the default-on [plain-text inscription](plain-text-inscription.md) requirement: this exception can be switched on to permit `text/html`, `text/markdown`, etc., where the body itself remains an exact District string.
- The historical implementation matches the literal prefix `text/`, even if the remaining subtype is empty or malformed; separating intentionally broad MIME-family policy from permissive string-prefix parsing is a further audit question.
- Do not mistake a MIME label of `text/html` for a body containing HTML: an HTML fragment does not pass the canonical District content check.
- This page concerns Districts only; Parcel rules are out of scope.
