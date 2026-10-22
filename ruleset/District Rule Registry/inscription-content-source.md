# Inscription Content: served District claim source

**Code ID (provisional):** `inscription_content`  
**Standard:** `0` (provisional current-profile value)  
**Earliest verified related implementation:** 25 September 2025 (`ord-tap` one-hop effective-payload change)  
**Explicit binary registry framing:** 22 October 2026  
**Status:** Independent historical alternative for **where** District claim bytes come from, not a delegate eligibility check.

## Definition

When enabled (`1`), evaluate the candidate's District claim schema against **inscription content as served for the claimant inscription ID**. In Ord terminology this is the effective body from the ordinary `/content/<id>` endpoint or its locally reproduced semantics:

- If claimant A has no delegate, served content uses A's own body.
- If A declares delegate B, served content can instead use **B's own body**, rather than A's, as Ord's current handler resolves one level of delegation.
- This is **not** the same thing as following an arbitrary nested chain A → B → C. Ord's current handler uses only a single delegate hop. Policies for inaccessible/malformed delegates or alternative fallback behaviours must be declared separately.

When disabled (`0`), this source-selection rule contributes no served-content candidate. It does not itself require the claimant to have, or to lack, a delegate.

This selects only **the content source**. The sole active [canonical District schema](canonical-district-schema.md) determines whether selected bytes qualify. The withdrawn hash-prefixed tutorial typo is **not** accepted (see [historical note](CODE-IDS-AND-REVIEW-GATES.md#deliberately-excluded-historical-typo)). MIME eligibility and decoding remain independent decisions, even though a served HTTP response can carry the delegate's MIME.

## History and evidence

- [Ord's current `/content` handler](https://github.com/ordinals/ord/blob/master/src/subcommand/server/r.rs#L250-L279) follows the candidate's delegate once before constructing the response; the [`/r/undelegated-content` handler](https://github.com/ordinals/ord/blob/master/src/subcommand/server/r.rs#L623-L645) does not. HTTP endpoint semantics alone do **not** prove a 2023 Bitmap eligibility rule.
- The [25 September 2025 Trac-derived `ord-tap` change](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) changes District input from `payload` to one-hop `payload_eff`, including effective body and MIME. This verifies a later Rust implementation, not the missing original Trac writer.
- The pre-existing [Single-Level Delegate Content Resolution](delegate-content-resolution.md) page preserves that **particular 2025 Trac code path** and its delegate-lookup/fallback edge cases. This new source rule records the more general **served-content interpretation**. Their possible overlap must be reconciled before constructing an executable profile; do not count the same resolution operation twice or infer fallback from this source selector.
- The earliest 2023 ruleset's “claim command” wording did not distinguish served content from the inscription's own body. The policy's original historic inception is **unverified**.

## Independence and combinations

- [Inscription Body](inscription-body-source.md) is a different, independently switchable source: it always reads the claimant's **own** bytes.
- [Delegate Tag Exclusion](delegate-tag-exclusion.md) asks whether a claimant declaring a delegate is ineligible regardless of bytes. [Nested Delegate Exclusion](nested-delegate-exclusion.md) asks whether a second-hop declaration is disallowed. Neither is implied by selecting served content.
- Default Body `1` / Content `0` is **provisional**, not a retroactive reinterpretation of 2023. Both-off and both-on combinations are not automatically assigned AND/OR/fallback semantics, especially where two sources yield different canonical District strings.
- No additional claim format, MIME family, inscription ordering or Parcel semantics is introduced by this source rule.
