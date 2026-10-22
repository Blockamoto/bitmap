# Canonical District schema

**Code ID (provisional):** `regex`  
**Default:** `1`  
**Introduced:** 1 June 2023

## Definition

Accept an exact `<height>.bitmap` claim from the **selected inscription source**, with height `0` or a decimal integer without leading zeros. The schema does not choose own-body versus served-content source.

## History

- **1 June 2023:** `0.bitmap` was inscribed, establishing the canonical District-claim format.

## Evidence

- [Bitmap District Ruleset (historical GitBook snapshot)](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/areas/the-bitmap-standard/district-ruleset.md)

## Clarifications

- Only decimal height `0` may begin with a zero.
- The historically used “district claim command” wording did not explicitly define the data source. The registry now records [Inscription Body](inscription-body-source.md) and [Inscription Content](inscription-content-source.md) as **separate, independently switchable binary sources**, without retroactively attributing either definition to 2023.
- [Delegate Tag Exclusion](delegate-tag-exclusion.md) and [Nested Delegate Exclusion](nested-delegate-exclusion.md) are separate eligibility decisions. See [open combination and provenance questions](DISTRICT-CONTENT-OPEN-QUESTION.md).
- The first published syntax and the Trac-derived content-resolution alternatives are kept distinct. Further evidence and rule lineage remain to be audited.
