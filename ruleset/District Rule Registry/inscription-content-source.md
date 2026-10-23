# Content: served District claim source

**Code ID (provisional):** `content`  
**Standard:** `0` (provisional current-profile value)  
**Earliest verified related implementation:** 25 September 2025 (`ord-tap` one-hop effective-payload change)  
**Explicit binary registry framing:** 22 October 2026  
**Status:** Independent historical alternative for **where** District claim bytes come from, not a delegate eligibility check. Here `content` means served/possibly delegated content. The older `content=1` rule meant own-body content, now separately named `body`; these are **not** aliases.

## Definition

When enabled (`1`), evaluate the District claim schema against **content served for the claimant inscription ID**, rather than reading its own envelope body directly. As a consequence of choosing this source, the content could be supplied by a delegate; delegation is not a requirement of this rule. In Ord terminology this is the effective body from the ordinary `/content/<id>` endpoint or its locally reproduced semantics:

- If claimant A has no delegate, served content uses A's own body.
- If A declares delegate B, served content uses **B's own body**, rather than A's, when B can be resolved. This does **not** follow an arbitrary nested chain A → B → C: the pinned Ord handler follows one hop only.
- If B cannot be resolved, the pinned Ord handler returns **not found**. By default, A supplies no served-content claim and its own body is **not** substituted. The separately switchable [`fallback`](fallback.md) rule can instead supply A's own body and MIME when enabled. An unresolved delegate does not invalidate or erase A as an inscription.

**Version pin:** Resolution means Ord [version `0.29.1`](https://github.com/ordinals/ord/blob/0.29.1/Cargo.toml#L1-L4), using the ordinary [`/content/<id>` handler](https://github.com/ordinals/ord/blob/0.29.1/src/subcommand/server/r.rs#L250-L279) and equivalent local reproduction of that behavior. The pinned version is a deterministic part of this rule's interpretation; upgrading Ord later does **not** silently change past District results. Any new semantics require an explicit registry/specification revision. This pins the content-resolution behavior, **not** unrelated features of Ord or other District rules. The independent [`fallback=1`](fallback.md) comparison bit is the **only presently defined override** for unresolved delegate lookups; it does not change normal successful resolution.

When disabled (`0`), this source-selection rule contributes no served-content candidate. It does not itself require the claimant to have, or to lack, a delegate.

This selects only **the content source**. The sole active [canonical District schema](canonical-district-schema.md) determines whether selected bytes qualify. The withdrawn hash-prefixed tutorial typo is **not** accepted (see [historical note](CODE-IDS-AND-REVIEW-GATES.md#deliberately-excluded-historical-typo)). MIME eligibility and decoding remain independent decisions, even though a served HTTP response can carry the delegate's MIME.

## History and evidence

- [Pinned Ord `0.29.1` `/content` handler](https://github.com/ordinals/ord/blob/0.29.1/src/subcommand/server/r.rs#L250-L279) resolves at most one delegate; if the target cannot be found, it returns not found without substituting the claimant's own envelope body. The [`/r/undelegated-content` handler](https://github.com/ordinals/ord/blob/0.29.1/src/subcommand/server/r.rs#L623-L645) is a different endpoint and is **not** used to resolve this source. Neither HTTP behavior proves an original 2023 Bitmap policy.
- The [25 September 2025 Trac-derived `ord-tap` change](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) changes District input from `payload` to one-hop `payload_eff`, including effective body and MIME. This verifies a later Rust implementation, not the missing original Trac writer.
- The later Trac-derived Rust implementation can fall back to the claimant's own payload when its declared delegate cannot be resolved. Its **distinct failed-lookup behavior** is now captured by the independent default-off [`fallback`](fallback.md) comparison rule, with [evidence preserved in the audit](TRAC-DISTRICT-AUDIT.md#district-specific-edge-cases-still-to-classify). Normal one-hop resolution remains in `content`, not in `fallback`; the superseded `delegate_content_resolution` code ID is not reinstated.
- The earliest 2023 ruleset's “claim command” wording did not distinguish served content from the inscription's own body. The policy's original historic inception is **unverified**.

## Independence and combinations

- [Inscription Body](inscription-body-source.md) is a different, independently switchable source: it always reads the claimant's **own** bytes.
- [Delegate Tag Exclusion](delegate-tag-exclusion.md) asks whether a claimant declaring a delegate is ineligible regardless of bytes. [Nested Delegate Exclusion](nested-delegate-exclusion.md) asks whether a second-hop declaration is disallowed. Neither is implied by selecting served content.
- Default Body `1` / Content `0` is **provisional**, not a retroactive reinterpretation of 2023. Both-off and both-on source combinations have no automatically assigned OR, AND, precedence, or source-fallback semantics, especially where two sources yield different canonical District strings. The explicitly defined [`fallback`](fallback.md) rule operates only inside enabled `content` on a failed delegate lookup; it does not resolve these source-combination questions.
- No additional claim format, MIME family, inscription ordering or Parcel semantics is introduced by this source rule.
