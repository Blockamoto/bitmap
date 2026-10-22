# Single-level delegate content resolution for District claims

**Default:** `0`  
**Introduced:** 25 September 2025

## Definition

When enabled, a District inscription may qualify using the **content body and content type of the inscription it delegates to** (one level deep), rather than only its own inscription body. The effective body must still match the canonical exact `<height>.bitmap` District syntax, and every other enabled District rule remains applicable.

## History and evidence

- [Trac-derived `ord-tap` commit, 25 September 2025](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) changes the District flow from examining `payload` to examining a one-level `payload_eff` resolved using `index.get_inscription_by_id(delegate_id)`. The MIME check is applied to `payload_eff` as well.
- [Current District invocation](https://github.com/Trac-Systems/ord-tap/blob/main/src/index/updater/inscription_updater.rs) still passes effective content to `index_bitmap_created`.
- This date proves the code change in the published `ord-tap` port; it does **not** establish when a comparable rule first ran in the 2023 Trac service.

## Clarifications

- [Nested delegate exclusion](nested-delegate-exclusion.md) is a distinct, separately switchable policy. The audited Trac-derived code rejects a known second delegate hop rather than chasing the chain.
- When the immediate delegate cannot be fetched, the audited code retains a clone of the original payload, and it does not automatically reject solely for the unresolved reference; that deserves its own edge-case comparison.
- This rule does not add a second District content schema; it selects which inscription's content is tested.
- Districts only, not Parcel provenance.
