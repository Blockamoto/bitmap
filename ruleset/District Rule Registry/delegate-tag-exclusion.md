# Delegate

**Code ID:** `delegate`  
**Previous draft ID:** `delegate_exclusion`  
**Standard:** `0`  
**Scope:** An all-delegate-declarations veto, not a delegation-enabling switch or a content resolver.

## Definition

When enabled, reject a District claimant solely because its own authenticated inscription envelope contains the **exact delegate tag byte `0x0b` (11) in field-key position before the body separator**.

Presence counts even when the value is empty, malformed, duplicated, dangling or names an unavailable target. An exact tag in an incomplete field-key position also establishes this raw presence predicate; independent parser/eligibility rules still apply. A successful lookup or a decodable inscription ID is not required.

When disabled, that declaration alone does not veto the claimant. All other source, MIME, byte, schema, height, precedence and exclusion rules still apply. `delegate=0` does not mean "use the delegate's content".

Tag-looking bytes in the body or an unrelated field value do not count. Without authenticated envelope evidence, the presence predicate is unknown rather than false.

## Independence

[`body`](inscription-body-source.md) reads the claimant's own envelope body. It does not prohibit that claimant from having other fields. A claimant with raw canonical bytes and a delegate tag can therefore pass `body=1` while being rejected by `delegate=1`.

[`content`](inscription-content-source.md) selects the resolved source. [`fallback`](fallback.md) selects a substitute on a failed lookup. Neither overrides this claimant-eligibility veto.

[`nested`](nested-delegate-exclusion.md) rejects the narrower case in which the claimant's decoded reference resolves to a target with its own decoded reference. `delegate=1` subsumes that veto on these candidates, but `delegate=0; nested=1` is a useful distinct profile. Keep the two questions separate.

## Evidence and limits

- The [16 October 2026 working specification](https://github.com/Blockamoto/bitmap-old/blob/ccf7271a61a2cead4781d4a2bb9c86da761f1cd6/DISTRICT-RULESET.md) records the former `delegate_exclusion=0` separately from own-body selection. The [21 October comparison specification](https://github.com/Blockamoto/bitmap-old/blob/63e77aa6f5cd95248e3abad55e168fa2215e0e32/COMPARISON-OPTIONS.md) makes tag presence explicit.
- [Ord 0.29.1 envelope parsing](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/inscriptions/envelope.rs#L28-L91) preserves field data; [`delegate()`](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/inscriptions/inscription.rs) instead attempts to decode an inscription ID. Testing that accessor alone is not an implementation of this raw-presence veto.
- Live OCI's rejection of delegates remains a **reported comparison target**, not independently verified here down to empty, malformed, duplicate and incomplete fields. Its exact program and parser are needed before claiming full equivalence.
- Trac's verified nested check is not an all-delegates ban. No original 2023 Trac enforcement of this blanket veto is established.

Only the active ID is shortened; the raw-presence policy and Standard `0` are retained. Ord parent/child provenance and Parcel rules are not involved.

[Registry](README.md) · [Audit report](SIX-RULE-AUDIT.md).
