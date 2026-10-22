# Delegate Tag Exclusion for District claims

**Code ID (provisional):** `delegate_exclusion`  
**Standard:** `0` (off; provisional candidate)  
**Earliest verified published working rule:** 16 October 2026 (`Blockamoto/bitmap-old` District comparison)  
**Status:** Tentative independent binary exclusion; later indexer comparisons remain to be audited.

## Definition

When enabled (`1`), **reject any District claimant whose own inscription envelope declares a delegate field**, irrespective of whether the body matches the District schema, whether the delegate exists, or whether the selected claim source is own-body or served-content.

The test is for the **presence of the exact Ord delegate field tag 11 in field position before the body separator**. Even an empty, malformed, duplicated, dangling or unresolved delegate value counts as a declaration for this veto. Mere delegate-looking bytes inside an unrelated field value or the body do **not** count. If authenticated inscription envelope bytes are unavailable, field presence is **unknown**, not proven absent.

When disabled (`0`), merely declaring a delegate is **not** an additional reason to disqualify a claim. All other enabled District eligibility, schema and source rules still apply.

## History and evidence

- [16 October 2026 published prior Bitmap working-spec revision](https://github.com/Blockamoto/bitmap-old/blob/ccf7271a61a2cead4781d4a2bb9c86da761f1cd6/DISTRICT-RULESET.md) lists `delegate_exclusion=0` separately from its own-body content rule. [2026 comparison details](https://github.com/Blockamoto/bitmap-old/blob/63e77aa6f5cd95248e3abad55e168fa2215e0e32/COMPARISON-OPTIONS.md) define it as an envelope tag-presence test, not a content-fetch or successful delegate resolution test.
- **22 October 2026:** Added as its own provisional entry to the chronological District Rule Registry at the creator's request.
- **Original Trac 2023 validator:** no published source located that proves such a rule. A separate Boppleton/Live OCI policy reportedly excludes delegates, but its precise historical implementation and date still require the dedicated District-only indexer audit before being asserted as evidence here.

## Clarifications

- Independent of [Inscription Body](inscription-body-source.md) and [Inscription Content](inscription-content-source.md) source selection: selecting own-body bytes does **not** entail a delegate veto, and selecting served bytes does not automatically grant an exception.
- Independent of [Nested Delegate Exclusion](nested-delegate-exclusion.md), which rejects **only** candidates whose immediate delegate itself delegates. If this all-delegates veto is enabled, the nested veto is redundant on those candidates but remains a separately recordable rule for alternative profiles.
- This is about Ord **delegation tag**, not Ord parent/child provenance or Parcel claims. No Parcel rules are included.
