# Canonical District schema

**Default:** `1`  
**Introduced:** 1 June 2023

## Definition

Accept exact `<height>.bitmap` content, with height `0` or a decimal integer without leading zeros.

## History

- **1 June 2023:** `0.bitmap` was inscribed, establishing the canonical District-claim format.

## Evidence

- [Bitmap District Ruleset (historical GitBook snapshot)](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/areas/the-bitmap-standard/district-ruleset.md)

## Clarifications

- Only decimal height `0` may begin with a zero.
- The term **“content” does not yet settle which inscription's bytes are evaluated** when a candidate carries a delegate tag. That is an [explicit open District registry decision](DISTRICT-CONTENT-OPEN-QUESTION.md), and this page does not silently define own/undelegated content versus one-level effective/served content.
- The first published syntax and the Trac-derived content-resolution alternatives are kept distinct. Further evidence and rule lineage remain to be audited.
