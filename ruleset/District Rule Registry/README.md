# District Rule Registry

The **Index** column remains deliberately blank until rule positions are assigned. Rows are arranged in **provisional historical order**, not in the order of our audit. Once an Index is assigned, later discoveries are appended without renumbering.

The **Default** is the currently proposed Standard-profile binary value (`1` enabled; `0` disabled), **not** proof of what every historical indexer enforced. **Introduced** means the earliest identified evidence for the policy or candidate in the linked rule page. Dates from a later implementation are not backdated to the original 2023 Trac service. An undated historical recollection is positioned tentatively and visibly marked.

| Index | Rule | Default | Introduced / earliest verified evidence | Definition |
| --- | --- | :---: | --- | --- |
|  | [BMP101 District prototype schema](bmp101-district-prototype-schema.md) | 0 | 24 May 2023 | Historical JSON `bmp101` District claim alternative; not the canonical `<height>.bitmap` format. |
|  | [Canonical District schema](canonical-district-schema.md) | 1 | 1 June 2023 | Accept an exact `<height>.bitmap` claim with canonical decimal height (no leading zeros). **Definition of which content bytes are tested remains open.** |
|  | [Hash-prefixed District schema](hash-prefixed-district-schema.md) | 0 | 3 June 2023 | Historical retracted `#<height>.bitmap` example, as an optional alternative schema. |
|  | [Plain-text inscription (`text/plain`)](plain-text-inscription.md) | 1 | 3 June 2023 (workflow evidence) | Require a `text/plain` media type, with valid MIME parameters permitted; early exclusivity is inferred, not directly proven. |
|  | [Claimed block exists](claimed-block-exists.md) | 1 | 16 June 2023 | Require claimed height `≤` the inscription's Bitcoin reveal-block height. |
|  | [Unix timestamp ordering](unix-timestamp-ordering.md) | 0 | **Undated; tentatively before July 2023** | Prefer eligible claim with lowest reveal-block header `nTime`; ties require an explicit outcome or deterministic tiebreak. |
|  | [Lowest inscription number](lowest-inscription-number.md) | 0 | **14 July 2023** (first published source) | Prefer the eligible claim with the lowest signed Ordinals inscription number. |
|  | [Strictly earlier reveal height](strict-prior-reveal-height.md) | 0 | **18 July 2023** (written alternative) | Require claimed height `<` the reveal-block height. Excludes same-block District claims; **not verified as a Trac enforcement rule**. |
|  | [Bitcoin transaction ordering](bitcoin-transaction-ordering.md) | 1 | **22 September 2023** (written precedence change) | Prefer earliest eligible reveal block and then lowest Bitcoin transaction index; same-transaction ties remain to be specified. |
|  | [Text MIME family exception](text-mime-family-exception.md) | 0 | 19 September 2025 (Rust snapshot) | Also permit MIME `text/*` labels for an otherwise exact District claim; narrowed to `text/plain` on 25 September 2025. |
|  | [JSON MIME exception](json-mime-exception.md) | 0 | 19 September 2025 (Rust snapshot) | Permit `application/json` as the MIME label, while still requiring canonical District claim bytes. |
|  | [Nested delegate exclusion](nested-delegate-exclusion.md) | 0 | 19 September 2025 (Rust snapshot) | Reject a claimant whose immediate delegate itself declares another delegate; initially after a separate TAP-start gate. |
|  | [Literal MIME string-prefix compatibility](mime-string-prefix-compatibility.md) | 0 | 19 September 2025 (Rust snapshot) | Reproduce permissive `starts_with` checks for **already enabled** MIME branches, including malformed labels with a matching prefix. |
|  | [Single-level delegate content resolution](delegate-content-resolution.md) | 0 | 25 September 2025 (Rust change) | Evaluate the first referenced delegate's own body and MIME as the candidate's effective content; **global content semantics are still undecided**. |
|  | [Negative inscription number exclusion](negative-inscription-number-exclusion.md) | 0 | 19 May 2026 (Rust change) | Reject District candidate inscriptions with negative signed Ordinals inscription numbers. |

## Unresolved policy decision: District “content”

The key decision is **what exactly an inscription must “contain” to be a District claim**. [Keep the content-definition and delegation questions open here](DISTRICT-CONTENT-OPEN-QUESTION.md). The distinct choices are: own/undelegated bytes versus one-level effective/delegated bytes; whether inscriptions carrying a delegate tag are eligible at all; and whether an otherwise-eligible nested delegate is excluded. The existing defaults do **not** decide these semantics. Do not silently revise the canonical District schema until this question has been settled.

## Evidence and extraction status

The Trac-derived public Rust implementation supplies **six** additional binary candidates: text MIME family exception, JSON MIME exception, nested delegate exclusion, literal MIME-prefix compatibility, one-level delegate content resolution, and negative inscription-number exclusion. The strict reveal-height rule is a **separate July 2023 authored-document alternative**, not a confirmed Trac implementation. Existing syntax, block-existence and winner selection rules are corroborated rather than duplicated. See [Trac District code audit](TRAC-DISTRICT-AUDIT.md) and [Trac source-lineage/evidence index](../../index/Trac.md).

**Open implementation comparisons, not automatically new dated rules:** Unknown/unavailable delegate fallback; explicit content-encoding tag veto versus raw bytes; unbound and reinscription flags; Bitcoin block `779832` as an *indexing coverage* start rather than intrinsic District eligibility; and multi-inscription same-transaction tie order. These need proof of distinct outcomes or an explicit policy decision before their own indexed registry rules are created.

The original **2023 Trac writer code was not recovered**. Chronological published ruleset changes (including `≤` versus `<` height and lowest inscription number versus first transaction order) are **not** automatically evidence of live Trac behaviour. Preserve source and uncertainty on each page. No Parcel rules are included in this District registry.
