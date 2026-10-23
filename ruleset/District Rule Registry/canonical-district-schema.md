# Canonical District schema

**Code ID (provisional):** `schema`  
**Standard:** `1`  
**Introduced:** 1 June 2023

## Definition

Require the **entire selected claim** to use canonical District format `<height>.bitmap`, matching the [District regex](district-claim.regex). The `height` is a non-negative decimal Bitcoin block height without leading zeros (except `0`), followed by the lowercase suffix `.bitmap`. Reject any extra characters, including spaces, carriage returns, newlines, BOMs or invisible Unicode characters.

**Regex:** [Standalone District claim regex](district-claim.regex)

```regex
^(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])
```

**Match semantics:** Evaluate the expression from the beginning of the **selected inscription body or served content**, as determined by the source rule. Without multiline (`m`) mode, the leading `^` requires the start, and the terminal negative lookahead `(?![\s\S])` requires that **no character at all follows** `.bitmap`, including spaces, carriage returns or newlines. A true full-string matcher is equivalent when implemented correctly. Engines without lookahead must enforce an exact-end check separately. Do not trim or normalize. The Bitcoin transaction and Ordinals envelope outside the selected content are not part of the schema match.

## History

- **1 June 2023:** `0.bitmap` was inscribed, establishing the canonical District-claim format.
- **Earlier draft reference regex:** `^(?:0|[1-9][0-9]*)\.bitmap$`. The terminal `$` is a conventional end anchor, but in some engines it also matches immediately before a final newline. That behavior was not intended as part of the District schema.
- **23 October 2026 QA:** Changed the reference regex to `^(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])`, removing the now-redundant `$` and retaining the explicit exact-content requirement. The reference should be used without multiline mode; implementations with a true full-string matcher can use that instead. This is a 2026 specification clarification, not an assertion about the original 2023 implementation.

## Evidence

- [Bitmap District Ruleset (historical GitBook snapshot)](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/areas/the-bitmap-standard/district-ruleset.md)

## Clarifications

- Only decimal height `0` may begin with a zero.
- The historically used “district claim command” wording did not explicitly define the data source. The registry now records [Body](inscription-body-source.md) and [Content](inscription-content-source.md) as **separate, independently switchable binary sources**, without retroactively attributing either definition to 2023.
- [Delegate Tag Exclusion](delegate-tag-exclusion.md) and [Nested Delegate Exclusion](nested-delegate-exclusion.md) are separate eligibility decisions. See [open combination and provenance questions](DISTRICT-CONTENT-OPEN-QUESTION.md).
- The first published syntax and the Trac-derived content-resolution alternatives are kept distinct. Further evidence and rule lineage remain to be audited.

- The canonical whole-string claim is ASCII-only. Under the active [ASCII byte rule](ascii-byte-matching.md) (`ascii=1`), the selected bytes are interpreted as US-ASCII and must satisfy this entire schema exactly. This accepts the same canonical claims as strict UTF-8. The original 2023 text did not settle charset-aware alternatives; they remain [documented research](TEXT-ENCODING-COMPARISON.md), **not** an active compatibility mode.
