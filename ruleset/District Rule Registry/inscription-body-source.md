# Inscription Body: District claim source

**Code ID (provisional):** `inscription_body`  
**Default:** `1` (provisional current-profile value)  
**Earliest verified related code:** 19 September 2025 (`ord-tap` initial public snapshot)  
**Explicit 2026 clarification:** 16 October 2026 working specification, subsequently revised 21 October.  
**Status:** Independent binary source-selection rule; **not** proof of original 2023 Trac enforcement.

## Definition

When enabled (`1`), evaluate the District claim schema against **the claimant inscription's own envelope body bytes**. This is the optional byte sequence after the inscription's field/body separator in its Bitcoin reveal. It is also called the *undelegated body*; no delegate target is fetched, substituted or followed to obtain these bytes.

When disabled (`0`), this source-selection rule contributes no claimant-body candidate. It **does not** mean “follow a delegate”; the alternate [Inscription Content](inscription-content-source.md) source has its own binary setting.

This rule selects **where claim bytes come from**, not which schema is valid. The separate [BMP101 prototype](bmp101-district-prototype-schema.md) and [canonical `<height>.bitmap`](canonical-district-schema.md) schemas are applied to a selected candidate source, using whatever independent decoding and MIME eligibility rules are selected. The old hash-prefixed tutorial typo is **not** a selectable schema; see [excluded historical typo](README.md#excluded-historical-typo).

## History and evidence

- The [July 2023 authored District rules](https://github.com/blockamotolabs/ruleset/blob/d140da22635b2d286b9b1960f5b3c76ba1a66632/README.md) describe a District “claim command” and pattern, but **do not explicitly define “content” as the envelope body** or settle delegation.
- The earliest verified [19 September 2025 `ord-tap` Rust snapshot](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater/tap/ops/bitmap.rs#L4-L23) obtains its candidate bytes via `payload.body()` from the original inscription. This verifies an implementation, not the original 2023 Trac writer.
- The [16 October 2026 prior District working specification](https://github.com/Blockamoto/bitmap-old/blob/ccf7271a61a2cead4781d4a2bb9c86da761f1cd6/DISTRICT-RULESET.md) describes `content=1` as the own undelegated body. The [21 October 2026 atomicity revision](https://github.com/Blockamoto/bitmap-old/blob/63e77aa6f5cd95248e3abad55e168fa2215e0e32/DISTRICT-RULESET.md) retains that interpretation and keeps `delegate_exclusion` independent.
- Formal registry framing as its own source-selection binary was requested **22 October 2026**.

## Independence and unaddressed combinations

- A delegate tag does not disqualify the claimant by this source check alone. That is controlled by [Delegate Tag Exclusion](delegate-tag-exclusion.md). A nested delegate is a separate question again.
- [Inscription Content](inscription-content-source.md) can be enabled or disabled independently. Do **not** infer one bit as the negation of the other.
- For the currently proposed defaults, own body is on and served content is off. The semantics of both bits `0` (no selected source) and both `1` (possibly conflicting successful claims from the same inscription) need explicit profile rules **before** a single-winner implementation can commit an outcome. Do not silently combine them as AND, OR, fallback, or precedence.
- MIME type and decoding are separate checks; this binary is not an implicit `text/plain`, UTF-8, or no-compression requirement.
- Districts only. Earlier historical documents remain quoted exactly, not rewritten as though they specified body semantics.
