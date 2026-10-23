# Exclusion

**Code ID:** `exclusion`  
**Previous draft ID:** `encoding_tag_exclusion`  
**Standard:** `0`  
**Scope:** The claimant's own content-encoding tag 9 only. The short name is not a generic switch for all exclusions.

## Definition

When enabled, reject a District claimant solely because its own authenticated inscription envelope contains the **exact tag byte `0x09` in field-key position before the body separator**.

Presence is sufficient. The value may be `br`, `gzip`, empty, unsupported or malformed. A repeated tag still establishes presence. An exact tag in an incomplete field-key position also establishes the raw presence predicate; the envelope's separate parser/eligibility status must not be concealed by that check.

When disabled, the tag's presence is not itself a reason to reject. All selected source, MIME, byte, schema, height and other eligibility rules continue to apply. `exclusion=0` does not enable decompression or validate the tag's value.

This is an exact field-position test, not a search through arbitrary bytes: `0x09` inside the body or another field's value does not count. A different field identifier, including property-encoding tag 19 (`0x13`), does not count. If the authenticated envelope is unavailable, the result is unknown, not proven absent.

## Source and transform independence

The predicate concerns the **claimant**, even when [`content`](inscription-content-source.md) selects another inscription's body. A coding tag on that delegate alone does not satisfy this claimant-tag predicate. Do not silently widen the rule to inspect every inscription used during resolution.

Keep [`brotli`](brotli-decompression-eligibility.md) separate. For example, raw canonical bytes with an encoding declaration can pass raw matching when both bits are `0`, but are vetoed by `exclusion=1`. Rejecting a declaration and permitting a transformation are different decisions.

## Evidence and limits

- The [21 October 2026 working comparison specification](https://github.com/Blockamoto/bitmap-old/blob/63e77aa6f5cd95248e3abad55e168fa2215e0e32/COMPARISON-OPTIONS.md) explicitly separates the old `encoding_tag_exclusion` ID from `body_transform=none`.
- [Ord 0.29.1 envelope parsing](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/inscriptions/envelope.rs#L28-L91) distinguishes field pairs from the body. Its [inscription accessors](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/inscriptions/inscription.rs) also demonstrate why a parsed HTTP-compatible value is not identical to raw tag presence.
- Live OCI's blanket content-encoding rejection is a **reported comparison target**. The exact Live OCI program and its parser have not been independently recovered in this audit. In particular, a truthiness check on an exported `contentEncoding` property is not automatically proof that empty, malformed, duplicate or incomplete raw fields are rejected.
- The inspected Trac-derived District parser does not introduce this tag-presence veto. No assertion is made that every historical OPI export or marketplace implementation has been fully checked.

The raw tag-presence definition is retained as the existing draft policy, not promoted to a proven byte-for-byte Live OCI implementation match. Standard remains `0`; only the ID and explanatory precision change.

[Registry](README.md) · [Audit report](SIX-RULE-AUDIT.md).
