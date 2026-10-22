# Single-level delegate content resolution for District claims

**Code ID (provisional):** `delegate_content_resolution`  
**Standard:** `0` (provisional pending the District content-definition decision)  
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
- This rule does not add a second District content schema. It records the **specific Trac-derived one-hop effective-payload implementation**, including its delegate-lookup/fallback behaviour. The registry now separately exposes a general [Inscription Content (served source)](inscription-content-source.md) binary alongside [Inscription Body](inscription-body-source.md). These can overlap; before producing an executable comparison profile, establish whether the Trac-specific behaviour actually differs from ordinary served-content semantics for the selected candidate, rather than counting the same delegate resolution twice.
- The alternative **content sources are now independently represented**. Their exact combined semantics and provenance remain under review in [the District source-and-delegation record](DISTRICT-CONTENT-OPEN-QUESTION.md); default `0` here is not a historical verdict about the original 2023 Trac writer.
- Accepting inscriptions carrying a delegate tag, selecting own versus effective bytes, and excluding nested delegates are separate decisions.
- Districts only, not Parcel provenance.
