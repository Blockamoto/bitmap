# Fallback: unresolved delegate content

**Code ID (provisional):** `fallback`  
**Standard:** `0`  
**Verified related implementation:** 25 September 2025 (`Trac-Systems/ord-tap` Rust change)  
**Scope:** District served-content source only; not a separate delegate-lookup algorithm.

## Definition

When `fallback=1` **and `content=1`**, if the claimant inscription declares a delegate but that delegate **cannot be resolved**, use the **claimant's own envelope body and its own content-type metadata** as the candidate content instead of returning no served content.

When `fallback=0`, follow [`content`'s pinned Ord `0.29.1` semantics](inscription-content-source.md): an unresolved declared delegate produces **not found** and contributes no served-content claim. `fallback` has no effect when `content=0` because that source is not selected.

This is **only a lookup-failure fallback**. It does not change Ord's normal delegate resolution when the referenced inscription can be fetched; does not fall back just because successfully resolved content fails the District schema, MIME, or other enabled checks; and does not enable or disable delegates as claimants. Nested-delegate exclusion and all-delegate exclusion remain separate rules. Claimant identity and Bitcoin reveal precedence do not change.

For reproducing the evidenced Trac-derived behavior, a failed delegate lookup includes a target not found **or a lookup error**, because the audited code substitutes a fetched delegate only on `Ok(Some(...))`. The candidate then goes through the ordinary enabled checks with the substituted body and content type. More specific error semantics must be fixed in implementation fixtures before executable profiles are frozen.

## Evidence and limitations

- [25 September 2025 Trac-derived `ord-tap` implementation](https://github.com/Trac-Systems/ord-tap/blob/acf6b7bbc7862e50999edd42c02ae170dfe23eea/src/index/updater/inscription_updater.rs#L1027-L1050) initializes `payload_eff` from the claimant and replaces it only when the delegate lookup returns `Ok(Some(insc))`. On lookup failure, the claimant's own body and MIME are retained.
- [Ord `0.29.1` served-content handler](https://github.com/ordinals/ord/blob/0.29.1/src/subcommand/server/r.rs#L250-L279) instead returns not found for an unresolved delegate; it does not substitute the claimant's body.
- This difference is evidenced in a **2025 Rust implementation**, not proven for the original 2023 Trac service or for every subsequent deployment. It is retained as a **comparison bit** so distinct indexer outcomes can be reproduced without attributing the fallback to Ord itself.

## Composition

`content` selects the served-content source and pins normal one-level resolution to Ord `0.29.1`. `fallback` changes **only** that source's behavior upon failed delegate resolution. `body` independently selects the claimant's own envelope body even when no lookup is attempted. This rule must not be treated as another general body-source toggle, a second delegate-resolution algorithm, or a substitute for a delegate-eligibility rule.

[District registry](README.md) · [Content](inscription-content-source.md) · [Trac audit](TRAC-DISTRICT-AUDIT.md).
