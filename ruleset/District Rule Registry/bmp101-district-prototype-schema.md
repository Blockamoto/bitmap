# BMP101 District prototype schema

**Code ID (provisional):** `schema_bmp101`  
**Standard:** `0`  
**Introduced:** 24 May 2023

## Definition

Accept a JSON District claim with `"p":"bmp101"`, `"op":"dis"`, and a `"dis<height>":"<name>"` entry; `"memo"` is optional.

## History and evidence

Pending review of the original Carrd publication and subsequent documentation.

## Clarifications

- Historical alternative schema, disabled by default.
- This rule concerns recognition of the JSON District claim format; other BMP101 mechanics are not implicitly adopted.
- This is **a schema rule**, not a choice of which bytes constitute the claim. When applying it to any historical or comparison profile, keep [Inscription Body](inscription-body-source.md) versus [Inscription Content](inscription-content-source.md) **as independent source-selection binaries**. Do not claim that the original May 2023 BMP101 document specified the later terminology.
- [Delegate Tag Exclusion](delegate-tag-exclusion.md) is an independent eligibility veto, not an implicit part of this JSON schema.
