# Body: District claim source

**Code ID (provisional):** `body`  
**Standard:** `1` (provisional current-profile value)  
**Earliest verified related code:** 19 September 2025 (`ord-tap` initial public snapshot)  
**Explicit 2026 clarification:** 16 October 2026 working specification, subsequently revised 21 October.  
**Status:** Independent binary source-selection rule; **not** proof of original 2023 Trac enforcement. Historic `content=1` referred to an own-body policy; it now corresponds most closely to `body=1`, **not** to the current served-content `content` rule.

## Definition

When enabled (`1`), evaluate the District claim schema against **the claimant inscription's own envelope body bytes**, rather than content served for its inscription ID. This is the optional byte sequence after the inscription's field/body separator in its Bitcoin reveal, also called the *undelegated body*. As a consequence of choosing this source, a delegate's content is not substituted. This does not itself exclude an inscription that declares a delegate.

When disabled (`0`), this source-selection rule contributes no claimant-body candidate. It **does not** mean “follow a delegate”; the alternate [Inscription Content](inscription-content-source.md) source has its own binary setting.

This rule selects **where claim bytes come from**, not whether they satisfy the sole active [canonical `<height>.bitmap` District schema](canonical-district-schema.md). Strict decoding and MIME eligibility remain separate. The withdrawn hash-prefixed tutorial typo is **not** a selectable schema; see [excluded historical typo](CODE-IDS-AND-REVIEW-GATES.md#deliberately-excluded-historical-typo).

## Envelope extraction and byte boundary (23 October 2026 clarification)

Bitcoin transactions, not an Ord server or inscription-content endpoint, are the input source for the proposed Standard. Inspect transaction **input witness Tapscript**, recognize Ordinals-style `ord` inscription envelopes and their field/body separator, then take the **claimant envelope's own body payload**. A body can be distributed across multiple script data pushes: concatenate those body pushes **in encounter order** to obtain the selected payload bytes. Do not run the District claim regex over the entire transaction, witness serialization, surrounding Tapscript opcodes, or envelope fields. Do not manufacture body bytes when the body is absent.

Those selected bytes are the stored payload **before** any HTTP content delivery, delegate resolution, Brotli/gzip decompression, charset transcoding, trimming or Unicode normalization. The independent [`text`](plain-text-inscription.md) rule evaluates the inscription's declared MIME type; [`ascii`](ascii-byte-matching.md) and [`schema`](canonical-district-schema.md) determine whether the selected payload qualifies. This Body rule does **not** implicitly apply a decoder or a general rejection of encoding declarations; those remain independently represented by [`brotli`](brotli-decompression-eligibility.md) and [`exclusion`](content-encoding-tag-exclusion.md).

An inscription may declare a delegate and still supply qualifying bytes in **its own body**. `body=1` never dereferences that declaration; not following a delegate is different from vetoing its declaration. The latter is the separate [`delegate`](delegate-tag-exclusion.md) rule (`0` in the proposed Standard).

Ord's parser is a **versioned comparison reference** for recognizing envelopes, not an external source of authority or an automatic rolling dependency. This clarification does not claim that a full envelope compatibility test against a particular Ord release has been completed. The specific Ord 0.29.1 pin on [`content`](inscription-content-source.md) is limited to that optional served-content resolution, which is disabled in the proposed Standard. Any upstream parsing difference capable of changing Bitmap results requires documented fixtures and an explicit review, not silent adoption.

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
