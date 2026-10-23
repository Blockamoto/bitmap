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

**Match semantics:** Match from the beginning of the **selected inscription body or resolved content**, as chosen by the separate source rule, **without multiline (`m`) mode**, or use an equivalent true full-string matcher. The terminal negative lookahead `(?![\s\S])` requires that no character follows `.bitmap`, including trailing spaces or newlines. The earlier `# Canonical District schema

**Code ID (provisional):** `schema`  
**Standard:** `1`  
**Introduced:** 1 June 2023

## Definition

Require the **entire selected claim** to use canonical District format `<height>.bitmap`, matching the [District regex](district-claim.regex). The `height` is a non-negative decimal Bitcoin block height without leading zeros (except `0`), followed by the lowercase suffix `.bitmap`. Reject any extra characters, including spaces, carriage returns, newlines, BOMs or invisible Unicode characters.

**Regex:** [Standalone District claim regex](district-claim.regex)

```regex
^(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])
```

 could match before a final newline in some engines. Engines without lookahead must enforce the same exact-content requirement through full-match and length checks. Do not trim or normalize. Bitcoin witness and Ordinals envelope data outside the selected body/content are not part of the match. The schema does not choose the source.

## History

- **1 June 2023:** `0.bitmap` was inscribed, establishing the canonical District-claim format.
- **Earlier draft reference:** `^(?:0|[1-9][0-9]*)\.bitmap# Canonical District schema

**Code ID (provisional):** `schema`  
**Standard:** `1`  
**Introduced:** 1 June 2023

## Definition

Require the **entire selected claim** to use canonical District format `<height>.bitmap`, matching the [District regex](district-claim.regex). The `height` is a non-negative decimal Bitcoin block height without leading zeros (except `0`), followed by the lowercase suffix `.bitmap`. Reject any extra characters, including spaces, carriage returns, newlines, BOMs or invisible Unicode characters.

**Regex:** [Standalone District claim regex](district-claim.regex)

```regex
^(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])
```

**Match semantics:** Match from the beginning of the **selected inscription body or resolved content**, as chosen by the separate source rule, **without multiline (`m`) mode**, or use an equivalent true full-string matcher. The terminal negative lookahead `(?![\s\S])` requires that no character follows `.bitmap`, including trailing spaces or newlines. The earlier `# Canonical District schema

**Code ID (provisional):** `schema`  
**Standard:** `1`  
**Introduced:** 1 June 2023

## Definition

Require the **entire selected claim** to use canonical District format `<height>.bitmap`, matching the [District regex](district-claim.regex). The `height` is a non-negative decimal Bitcoin block height without leading zeros (except `0`), followed by the lowercase suffix `.bitmap`. Reject any extra characters, including spaces, carriage returns, newlines, BOMs or invisible Unicode characters.

**Regex:** [Standalone District claim regex](district-claim.regex)

```regex
^(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])
```

 could match before a final newline in some engines. Engines without lookahead must enforce the same exact-content requirement through full-match and length checks. Do not trim or normalize. Bitcoin witness and Ordinals envelope data outside the selected body/content are not part of the match. The schema does not choose the source.

## History

. The `# Canonical District schema

**Code ID (provisional):** `schema`  
**Standard:** `1`  
**Introduced:** 1 June 2023

## Definition

Require the **entire selected claim** to use canonical District format `<height>.bitmap`, matching the [District regex](district-claim.regex). The `height` is a non-negative decimal Bitcoin block height without leading zeros (except `0`), followed by the lowercase suffix `.bitmap`. Reject any extra characters, including spaces, carriage returns, newlines, BOMs or invisible Unicode characters.

**Regex:** [Standalone District claim regex](district-claim.regex)

```regex
^(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])
```

**Match semantics:** Match from the beginning of the **selected inscription body or resolved content**, as chosen by the separate source rule, **without multiline (`m`) mode**, or use an equivalent true full-string matcher. The terminal negative lookahead `(?![\s\S])` requires that no character follows `.bitmap`, including trailing spaces or newlines. The earlier `# Canonical District schema

**Code ID (provisional):** `schema`  
**Standard:** `1`  
**Introduced:** 1 June 2023

## Definition

Require the **entire selected claim** to use canonical District format `<height>.bitmap`, matching the [District regex](district-claim.regex). The `height` is a non-negative decimal Bitcoin block height without leading zeros (except `0`), followed by the lowercase suffix `.bitmap`. Reject any extra characters, including spaces, carriage returns, newlines, BOMs or invisible Unicode characters.

**Regex:** [Standalone District claim regex](district-claim.regex)

```regex
^(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])
```

 could match before a final newline in some engines. Engines without lookahead must enforce the same exact-content requirement through full-match and length checks. Do not trim or normalize. Bitcoin witness and Ordinals envelope data outside the selected body/content are not part of the match. The schema does not choose the source.

## History

 anchor could match immediately before a final newline in some regex engines if used with a prefix-style match; accepting such a newline was never the intended schema.
- **23 October 2026 QA:** Changed the reference to `^(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])`, removing the redundant `# Canonical District schema

**Code ID (provisional):** `schema`  
**Standard:** `1`  
**Introduced:** 1 June 2023

## Definition

Require the **entire selected claim** to use canonical District format `<height>.bitmap`, matching the [District regex](district-claim.regex). The `height` is a non-negative decimal Bitcoin block height without leading zeros (except `0`), followed by the lowercase suffix `.bitmap`. Reject any extra characters, including spaces, carriage returns, newlines, BOMs or invisible Unicode characters.

**Regex:** [Standalone District claim regex](district-claim.regex)

```regex
^(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])
```

**Match semantics:** Match from the beginning of the **selected inscription body or resolved content**, as chosen by the separate source rule, **without multiline (`m`) mode**, or use an equivalent true full-string matcher. The terminal negative lookahead `(?![\s\S])` requires that no character follows `.bitmap`, including trailing spaces or newlines. The earlier `# Canonical District schema

**Code ID (provisional):** `schema`  
**Standard:** `1`  
**Introduced:** 1 June 2023

## Definition

Require the **entire selected claim** to use canonical District format `<height>.bitmap`, matching the [District regex](district-claim.regex). The `height` is a non-negative decimal Bitcoin block height without leading zeros (except `0`), followed by the lowercase suffix `.bitmap`. Reject any extra characters, including spaces, carriage returns, newlines, BOMs or invisible Unicode characters.

**Regex:** [Standalone District claim regex](district-claim.regex)

```regex
^(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])
```

 could match before a final newline in some engines. Engines without lookahead must enforce the same exact-content requirement through full-match and length checks. Do not trim or normalize. Bitcoin witness and Ordinals envelope data outside the selected body/content are not part of the match. The schema does not choose the source.

## History

. Keep the start anchor and disable multiline mode, or use exact full-match semantics. This is a 2026 regex-hardening change, not a retrospective assertion about the 2023 implementation.

## Evidence

- [Bitmap District Ruleset (historical GitBook snapshot)](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/areas/the-bitmap-standard/district-ruleset.md)

## Clarifications

- Only decimal height `0` may begin with a zero.
- The historically used “district claim command” wording did not explicitly define the data source. The registry now records [Body](inscription-body-source.md) and [Content](inscription-content-source.md) as **separate, independently switchable binary sources**, without retroactively attributing either definition to 2023.
- [Delegate Tag Exclusion](delegate-tag-exclusion.md) and [Nested Delegate Exclusion](nested-delegate-exclusion.md) are separate eligibility decisions. See [open combination and provenance questions](DISTRICT-CONTENT-OPEN-QUESTION.md).
- The first published syntax and the Trac-derived content-resolution alternatives are kept distinct. Further evidence and rule lineage remain to be audited.

- The canonical whole-string claim is ASCII-only. Under the active [ASCII byte rule](ascii-byte-matching.md) (`ascii=1`), the selected bytes are interpreted as US-ASCII and must satisfy this entire schema exactly. This accepts the same canonical claims as strict UTF-8. The original 2023 text did not settle charset-aware alternatives; they remain [documented research](TEXT-ENCODING-COMPARISON.md), **not** an active compatibility mode.
