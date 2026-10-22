# District Rule Registry

**Status:** Draft for production review, not a frozen or executable bit registry. **Scope:** Districts only. Last reviewed 22 October 2026.

Rules are organized in **two passes**: foundational choices that must be settled to evaluate a District, followed by optional compatibility and exclusion switches. Within each pass, related questions are grouped. Historical introduction/evidence dates are shown separately; they do **not** determine the active decision order. Undated recollections remain visibly provisional. Neither pass claims to reconstruct the original 2023 validator's execution sequence.

The **Index** field remains blank until permanent numeric positions are authorized. **Code ID** values are *provisional short identifiers* for discussing one current question in code, not assigned bit positions, protocol keys or previous profile IDs. [Historic ID crosswalk and remaining production review gates](CODE-IDS-AND-REVIEW-GATES.md). Defaults are the current proposed profile values (`1` on, `0` off), **not** historical consensus or proof of indexer enforcement.

## Active District decisions

**Ordering principle:** Essential questions that cannot be left semantically unspecified precede optional additions. Rules addressing the same decision are kept together within each pass. An option with default `0` may still appear in the essential pass when a **choice of modes** is mandatory: enabling that particular alternative is not mandatory. Rows are not chronological positions or bit indices; each retains its separate evidence date.

### Pass 1: Foundational decisions that an executable profile must settle

**1. Claim source: what bytes are examined?** Select the source policy explicitly. Standard proposes own inscription body `1`, served inscription content `0`; neither is a delegate veto. Both `0` and both `1` have no agreed executable combination semantics.

| Index | Code ID | Rule | Default | Earliest evidence / introduction | Decision |
| --- | --- | --- | :---: | --- | --- |
|  | `inscription_body` | [Inscription Body source](inscription-body-source.md) | 1 | **19 September 2025** (earliest verified code; explicit clarification in 2026) | Independently allow schema matching against claimant's own envelope body bytes, without resolving delegation. |
|  | `inscription_content` | [Inscription Content source](inscription-content-source.md) | 0 | **25 September 2025** (earliest verified served-payload use; explicit binary clarification in 2026) | Independently allow schema matching against the claimant's served/effective inscription content, which may come from a delegate. |

**2. Claim schema: what representation qualifies?** At least one schema must be explicitly selected. The BMP101 JSON prototype is a historical alternative, not permission to parse JSON under the canonical `regex` rule.

| Index | Code ID | Rule | Default | Earliest evidence / introduction | Decision |
| --- | --- | --- | :---: | --- | --- |
|  | `schema_bmp101` | [BMP101 District prototype schema](bmp101-district-prototype-schema.md) | 0 | 24 May 2023 | Historical JSON `bmp101` District claim alternative; not the canonical `<height>.bitmap` format. |
|  | `regex` | [Canonical District schema](canonical-district-schema.md) | 1 | 1 June 2023 | Accept an exact `<height>.bitmap` claim with canonical decimal height (no leading zeros). Claim source is selected independently, without rewriting 2023 terminology. |

**3. MIME and text interpretation: how are source bytes checked?** Specify media-type policy and a decoder mode. The `raw_utf8_strict` alternative is off by default; that `0` does **not** by itself define a complete charset-decoding algorithm. The working Standard separately proposes `decoder_mode=declared_charset_strict`, with unresolved label/BOM/missing-charset fixtures.

| Index | Code ID | Rule | Default | Earliest evidence / introduction | Decision |
| --- | --- | --- | :---: | --- | --- |
|  | `text` | [Plain-text inscription (`text/plain`)](plain-text-inscription.md) | 1 | 3 June 2023 (workflow evidence) | Require a `text/plain` media type, with valid MIME parameters permitted; early exclusivity is inferred, not directly proven. |
|  | `raw_utf8_strict` | [Raw Strict UTF-8 Decoding](raw-utf8-strict-decoding.md) | 0 | **5 December 2023** (OPI first public code) | Decode selected claim-source bytes as strict UTF-8 regardless of declared charset; reject malformed UTF-8, independently of MIME eligibility. |

**4. Claimed-block eligibility: is the target already available?** Inclusive reveal height is the proposed baseline. The stricter `<` historical variant is a supplemental modifier below.

| Index | Code ID | Rule | Default | Earliest evidence / introduction | Decision |
| --- | --- | --- | :---: | --- | --- |
|  | `height` | [Claimed block exists](claimed-block-exists.md) | 1 | 16 June 2023 | Require claimed height `≤` the inscription's Bitcoin reveal-block height. |

**5. Winner policy and comparator: which eligible claimant takes the District?** The `first` predicate and the ordering comparator are **different decisions**. Choose exactly one defined comparator in an executable single-winner profile, and separately resolve its ties. The three comparator rows record alternative historical interpretations; they are not conjunctive requirements. `precedence_unix_timestamp` is tentatively dated and requires a tie rule before it could yield a unique winner.

| Index | Code ID | Rule | Default | Earliest evidence / introduction | Decision |
| --- | --- | --- | :---: | --- | --- |
|  | `first` | [First eligible claimant wins](first-eligible-wins.md) | 1 | 14 July 2023 (first-winner wording; independent switch documented 21 October 2026) | Recognize the first **eligible** claimant according to the separately chosen precedence comparator; do not conflate eligibility with sorting. |
|  | `precedence_unix_timestamp` | [Unix timestamp ordering](unix-timestamp-ordering.md) | 0 | **Undated; tentatively before July 2023** | Prefer eligible claim with lowest reveal-block header `nTime`; ties require an explicit outcome or deterministic tiebreak. |
|  | `precedence_inscription_number` | [Lowest inscription number](lowest-inscription-number.md) | 0 | **14 July 2023** (first published source) | Prefer the eligible claim with the lowest signed Ordinals inscription number. |
|  | `precedence_bitcoin_reveal` | [Bitcoin transaction ordering](bitcoin-transaction-ordering.md) | 1 | **22 September 2023** (written precedence change) | Prefer earliest eligible reveal block and then lowest Bitcoin transaction index; same-transaction ties remain to be specified. |

### Pass 2: Optional restrictions, exceptions and implementation-specific alternatives

**Claimed-block strictness:** This additional restriction changes the same height-decision area as `height`; disabling it leaves the inclusive baseline intact.

| Index | Code ID | Rule | Default | Earliest evidence / introduction | Decision |
| --- | --- | --- | :---: | --- | --- |
|  | `strict_height` | [Strictly earlier reveal height](strict-prior-reveal-height.md) | 0 | **18 July 2023** (written alternative) | Require claimed height `<` the reveal-block height. Excludes same-block District claims; **not verified as a Trac enforcement rule**. |

**Served-content implementation detail:** Trac's 2025 one-hop lookup/fallback behaviour is preserved for comparison, not silently combined with the general served-content source.

| Index | Code ID | Rule | Default | Earliest evidence / introduction | Decision |
| --- | --- | --- | :---: | --- | --- |
|  | `delegate_content_resolution` | [Single-level delegate content resolution](delegate-content-resolution.md) | 0 | 25 September 2025 (Rust change) | Retain the specific Trac-derived one-hop resolution/fallback behaviour for historical comparison; overlaps the general served-content source and awaits profile-composition review. |

**Additional MIME compatibility:** The default-off allowances can broaden, or reproduce quirks in, the MIME check without changing the canonical District claim grammar.

| Index | Code ID | Rule | Default | Earliest evidence / introduction | Decision |
| --- | --- | --- | :---: | --- | --- |
|  | `text_mime_family` | [Text MIME family exception](text-mime-family-exception.md) | 0 | 19 September 2025 (Rust snapshot) | Also permit MIME `text/*` labels for an otherwise exact District claim; narrowed to `text/plain` on 25 September 2025. |
|  | `json_mime` | [JSON MIME exception](json-mime-exception.md) | 0 | 19 September 2025 (Rust snapshot) | Permit `application/json` as the MIME label, while still requiring canonical District claim bytes. |
|  | `mime_prefix_compatibility` | [Literal MIME string-prefix compatibility](mime-string-prefix-compatibility.md) | 0 | 19 September 2025 (Rust snapshot) | Reproduce permissive `starts_with` checks for **already enabled** MIME branches, including malformed labels with a matching prefix. |

**Extra transforms and metadata vetoes:** Decompression eligibility and mere presence of an encoding tag remain separate decisions.

| Index | Code ID | Rule | Default | Earliest evidence / introduction | Decision |
| --- | --- | --- | :---: | --- | --- |
|  | `brotli` | [Brotli Decompression Eligibility](brotli-decompression-eligibility.md) | 0 | **15 October 2026** (prior working rule) | Permit a separately specified Brotli-decompression eligibility route for claim bytes; does not reject encoding-tag presence. |
|  | `encoding_tag_exclusion` | [Content-Encoding Tag Exclusion](content-encoding-tag-exclusion.md) | 0 | **21 October 2026** (atomic working specification) | Reject a claimant solely for declaring Ord content-encoding tag 9, independent of any decoding/decompression route. |

**Additional claimant exclusions:** Optional indexer interpretations are separated from claim-source selection and historical validity. A declared delegate is not automatically a reason to reject an own-body claim.

| Index | Code ID | Rule | Default | Earliest evidence / introduction | Decision |
| --- | --- | --- | :---: | --- | --- |
|  | `nested_delegate_exclusion` | [Nested delegate exclusion](nested-delegate-exclusion.md) | 0 | 19 September 2025 (Rust snapshot) | Reject a claimant whose immediate delegate itself declares another delegate; initially after a separate TAP-start gate. |
|  | `negative_inscription_number_exclusion` | [Negative inscription number exclusion](negative-inscription-number-exclusion.md) | 0 | 19 May 2026 (Rust change) | Reject District candidate inscriptions with negative signed Ordinals inscription numbers. |
|  | `delegate_exclusion` | [Delegate Tag Exclusion](delegate-tag-exclusion.md) | 0 | **16 October 2026** (prior working spec; original inception unverified) | Reject any claimant declaring Ord delegate tag 11, regardless of its body, served content, or nested delegation. |

## Excluded historical typo

**The hash-prefixed `#<height>.bitmap` example is not an active rule.** The creator confirmed that `0.bitmap` was the intended original exemplar, and the `#` form was a GitBook tutorial error, not a canonical claim schema or known independent indexer policy. The mistaken example appeared on **3 June 2023**, was corrected by **14 June**, and the **16 June verification guide** expressly rejected `#69.bitmap`. Historical evidence remains in the [3 June GitBook revision](https://gitbook.bitmap.land/~/revisions/AZO0a8slhI90dZCq0SNg/) and [archived verification instructions](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/archive/_old/bitmap-theory-101/how-to-verify-blocks.md). **No `#` schema switch or ID will be assigned.** This removes a withdrawn typo from the normative candidate set, without deleting the historical occurrence.

## Dependencies and review boundaries

**Source and delegation are separate:** `inscription_body` tests the inscription's own undelegated body; `inscription_content` tests content as served for that inscription ID, which may be supplied by a delegate; `delegate_exclusion` rejects a declared delegate tag; and `nested_delegate_exclusion` is only a second-hop veto. The Trac-specific `delegate_content_resolution` candidate overlaps with served content and is retained for versioned implementation comparison. [Source/delegation decision record](DISTRICT-CONTENT-OPEN-QUESTION.md). The paired source-bit combinations and unresolved delegate fallback are **not defined by a hidden default**.

**MIME and decoding are independent:** The baseline `text` MIME rule is not a charset decoder. `raw_utf8_strict` is an OPI-backed alternative decoder and must not silently bypass `text`. `brotli` permits an extra decompression eligibility route; `encoding_tag_exclusion` rejects mere tag presence. [Trac, OPI and Live OCI evidence comparison](TEXT-ENCODING-COMPARISON.md), with Live OCI behaviour still awaiting direct audit.

**Height and winner selection are different questions:** `height` admits a claim for the inscription's own reveal block (`≤`); `strict_height` is the documented `<` alternative. The three **precedence** rows are competing historical comparators, not three ordering requirements to combine silently. The independent [`first`](first-eligible-wins.md) rule (earliest eligible wins) is now explicitly listed apart from the legacy `fiftxi` bundled comparator. If `first=0`, the replacement winner policy must be declared; no implied multi-winner acceptance. Same-transaction and timestamp ties and incompatible comparator combinations still require versioned decisions. See [code-ID crosswalk](CODE-IDS-AND-REVIEW-GATES.md).

**Cursed versus reinscriptions:** A negative-number veto is narrower than a blanket cursed-status veto. The creator requested that **reinscription exclusion not be an active rule at present**; it remains only in [historical OPI evidence](https://github.com/Blockamoto/bitmap-old/blob/old/edge-cases/reinscriptions.md) and can be added later if warranted.

**Evidence is not deployment:** The original **2023 Trac writer** remains unlocated. Dates on indexer-derived entries generally date **the earliest verified source snapshot**, not the rule's first production introduction. [Trac District audit](TRAC-DISTRICT-AUDIT.md) · [Trac source lineage](../../index/Trac.md).

**Production gates still open:** Code IDs and Index positions are provisional; no canonical serialization or executable schema/decoder/transform/precedence contract is approved. [Review checklist and legacy-ID mapping](CODE-IDS-AND-REVIEW-GATES.md). Do not silently treat an unsupported combination as valid, a missing source as absent, or a historical rule variant as the currently selected profile. Parcel ruleset, `main`, and Bitcoin/Bitmap Chain commitments are not changed by this registry organization.
