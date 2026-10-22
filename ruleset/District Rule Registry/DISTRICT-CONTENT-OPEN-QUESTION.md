# District source and delegation distinctions: 22 October 2026

**Registry status:** **Three separate binary questions are now recorded**, at the creator's direction; original 2023 usage and certain cross-rule combinations remain unverified.  
**Historical protection:** The original 2023 rules' “district claim command” and “inscription must contain” language is preserved as written. Do not substitute this 2026 clarification into a purported 2023 quotation.  
**Index positions and executable profile semantics:** Pending.

## Recorded independent choices

1. **[Body](inscription-body-source.md):** Enable evaluating the candidate against the claimant inscription's **own undelegated envelope body bytes**, regardless of what HTTP content serving would return.
2. **[Content](inscription-content-source.md):** Enable evaluating the candidate against content that would be **served for the claimant inscription ID**. Under Ord's current content handler, a declared delegate can supply the served bytes; this is not a different claim schema.
3. **[Delegate Tag Exclusion](delegate-tag-exclusion.md):** Reject any claimant **merely for declaring a delegate**, regardless of how content was selected and whether its own bytes match.

A fourth pre-existing rule, **[Nested Delegate Exclusion](nested-delegate-exclusion.md)**, rejects the narrower A → B → C scenario when A's immediate delegate B itself declares a delegate. It is **not** the same as all-delegates exclusion.

**ID clarification (22 October 2026):** The short names are now `body` (claimant's own bytes) and `content` (served bytes). The historical `content=1` own-body rule is not equivalent to today's `content` ID. Do not translate old and new profiles merely by matching the name.

No one of these binaries is defined as the negation of another. The first two concern **source selection** only, the third and fourth concern **eligibility vetoes**.

## Concrete distinction

Suppose A's own body is `123.bitmap`, but it delegates to B whose body is `234.bitmap`.

- **Inscription Body** examines `123.bitmap` for A.
- **Inscription Content** examines `234.bitmap` for A under Ord's one-hop served-content behaviour.
- **Delegate Tag Exclusion** (if on) makes A ineligible regardless of which source(s) match.
- **Nested Delegate Exclusion** (if on) rejects A only if B **also declares a delegate**, even if the content source might otherwise match.

If A has no delegate, its served and own-body bytes ordinarily coincide. Missing/unavailable delegate content is **not** automatically the claimant's own body in ordinary Ord HTTP semantics; a specific indexer may have a separate fallback quirk.

## Historical sources and limits

- [July 2023 Blockamoto Labs District rules](https://github.com/blockamotolabs/ruleset/blob/d140da22635b2d286b9b1960f5b3c76ba1a66632/README.md) name the *district claim command* and grammar, without explicitly choosing own-body versus served-content source or a general delegate veto.
- [19 September 2025 Trac-derived initial Rust Bitmap implementation](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater/tap/ops/bitmap.rs#L4-L23) parses the claimant's original `payload.body()`. This verifies that later public code, not the original 2023 writer.
- [25 September 2025 `ord-tap` commit](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) selects a one-level `payload_eff` and also moves a nested-delegate veto.
- [Ord served-content handler](https://github.com/ordinals/ord/blob/master/src/subcommand/server/r.rs#L250-L279) follows one delegate hop; [undelegated content handler](https://github.com/ordinals/ord/blob/master/src/subcommand/server/r.rs#L623-L645) does not. Endpoint semantics aren't themselves a Bitmap rule.
- [16 October 2026 prior District working specification](https://github.com/Blockamoto/bitmap-old/blob/ccf7271a61a2cead4781d4a2bb9c86da761f1cd6/DISTRICT-RULESET.md) explicitly distinguishes using one's own body from rejecting all delegates.
- The original 2023 Trac writer remains unrecovered. Its actual enforcement of any alternative is **unknown**. The [Trac audit](../../index/Trac.md) stores what has and has not been observed.

## Not yet resolved

- **Both source bits off:** No input source has been selected; an executable profile must define or reject this configuration.
- **Both source bits on:** What if both sources match *different* District heights for the same inscription? There is no approved precedence, merge or simultaneous-claim interpretation yet. Do **not** silently impose an OR, AND, fallback or source-preference policy.
- **Overlap with the [Single-Level Delegate Content Resolution](delegate-content-resolution.md) historical code option:** The later Trac implementation has source resolution and fallback details. Preserve its dated code record, but don't double-apply the same resolved content or assert these are automatically two independent filters with distinct outcomes.
- **MIME and decoder linkage:** Which field's declared content type is tested when using served content, and how declared encoding interacts with selected bytes, requires explicit rules or fixtures. This does **not** change the distinction between body source and served source.
- **Live OCI / Boppleton delegate policy:** The all-delegates exclusion is a separate candidate, currently off; verify the Live OCI implementation and earliest public date in the later District-only audit.

**Current provisional default combination:** `body=1`; `content=0`; Delegate Tag Exclusion `0`; Nested Delegate Exclusion `0`. These are **working profile defaults**, not a declaration that an ambiguous 2023 author or original Trac implementation had specified these exact binaries. No Parcel interpretation is imported.
