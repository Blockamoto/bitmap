# Lowest inscription number

**Default:** `0`  
**Introduced:** 26–27 July 2023

## Definition

Prefer the eligible claim with the lowest signed Ordinals inscription number.

## History

- **26–27 July 2023:** The District Ruleset described “first is first” in terms of the lowest inscription number.
- Later superseded by transaction ordering.

## Evidence

- [Historical District Ruleset snapshot](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/areas/the-bitmap-standard/district-ruleset.md)

## Clarifications

- Literal signed comparison means negative cursed inscription numbers can outrank positive numbers, and lower negative numbers may be assigned later.
- The actual behavior of early deployed indexers requires separate verification.
