# Trac District indexer audit

**Audit date:** 22 October 2026  
**Scope:** Bitmap **District** validity, candidate eligibility and winner selection only. No Parcel, ownership, transfer, tapping, or staking rules are included.  
**Status:** Public-code comparison complete for the confirmed points below; the original 2023 production writer and some edge cases remain unverified.

## Evidence boundaries

- [Public 2023 Trac Bitmap API description](https://github.com/BennyTheDev/trac-bitmap-public-endpoint) documents live Bitmap validity lookups but does **not** publish the original District validation algorithm. Its Git history begins in July 2023.
- [Trac-Systems/ord-tap](https://github.com/Trac-Systems/ord-tap) is a later, standalone Rust port of the Trac/TAP writer, with an initial public revision on **19 September 2025**. Its behaviour is an actual implementation to audit, **not proof** that the original 2023 service behaved identically.
- Rule rows below use the earliest **verified public code date** (or actual dated diff when found); introductory dates in the registry contain dates only, and evidence distinctions are captured on the individual pages.

## New District Rule Registry entries

All remain unnumbered and **off (`0`) by default** pending Standard-profile review.

| Rule | Earliest verified code/date | Distinction |
| --- | --- | --- |
| [Text MIME family exception](text-mime-family-exception.md) | 19 September 2025 | Initial Rust port accepts `text/*`; narrowed to `text/plain` on 25 September 2025. |
| [JSON MIME exception](json-mime-exception.md) | 19 September 2025 | Shared intake permits `application/json` labels even when District content itself must be exact `<height>.bitmap`. |
| [Nested delegate exclusion](nested-delegate-exclusion.md) | 19 September 2025 | Reject a delegation target that delegates again. Initially located after the TAP-start gate. |
| [Single-level delegate content resolution](delegate-content-resolution.md) | 25 September 2025 | Use one referenced delegate's content and MIME as the effective District payload. |
| [Negative inscription number exclusion](negative-inscription-number-exclusion.md) | 19 May 2026 | Explicitly reject signed Ordinals inscription numbers below zero. Previously absent from the Rust District creator. |

Relevant changes: [Initial port](https://github.com/Trac-Systems/ord-tap/commit/3f3f851a00301b780e333fc9d8a3c3eaf29920e3) · [MIME narrowing and effective delegation](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) · [Negative-number guard](https://github.com/Trac-Systems/ord-tap/commit/12ddc36ccfa7655a2bbec20d0245deecdec0ec55).

## Existing rules corroborated, not duplicated

The [District creation routine](https://github.com/Trac-Systems/ord-tap/blob/main/src/index/updater/inscription_updater/tap/ops/bitmap.rs) requires the body to contain a canonical lowercase `<height>.bitmap` string with no leading zeros, rejects future claimed heights, and preserves the first accepted claim for each District height using the existing `bm/<height>` record. These overlap the registry's canonical schema, claimed-block-exists, and winner-order rules.

The public routine uses the indexer's processing order, while the registry currently defines *earliest reveal block, then Bitcoin transaction index*. The winner when **multiple qualifying inscriptions occur in the same Bitcoin transaction** still needs an explicit order-of-envelopes clarification and, ideally, a test fixture.

## District-specific edge cases still to classify

1. **MIME string-prefix matching.** The shared filter uses `starts_with("text/plain")` or `starts_with("application/json")`, not parsed base media types. This can permit malformed MIME strings that merely begin with those bytes. It could become a separate default-off binary rule if that distinction is retained, rather than a clarification of the two MIME entries.
2. **Encoding and compression.** The District creator applies `String::from_utf8_lossy(body)` to raw inscription bytes; the District path does not explicitly veto the `content_encoding` tag or decompress a body. Because the accepted District body consists entirely of ASCII digits and the literal `.bitmap`, replacing invalid UTF-8 bytes does **not** create a newly valid District claim. Thus lossy versus strict UTF-8 decoding does not by itself justify an additional validity switch for this schema. A correctly formatted ASCII body that merely carries a content-encoding tag is a separate metadata-policy comparison for Live OCI.
3. **Minimum scan/activation height.** Mainnet `TAP_BITMAP_START_HEIGHT` is `779832`. The creation hook exits before indexing at lower heights. Decide whether an operational index start should be part of District eligibility rules or only the indexer coverage record.
4. **Reinscriptions and unbound status.** The Trac-derived District creation hook does **not** explicitly veto `reinscription` or `unbound` flags passed through to its outer inscription hook. That absence is **not** evidence that all such inscriptions reach the hook successfully or were accepted by the original production Trac service. Audit the Ord envelope/curse stage before proposing a District exclusion rule.
5. **Unknown/unavailable delegate.** The later hook starts with the original payload, replacing it if the referenced delegate is fetched successfully. If not found, it can retain the original payload. This differs from the independent question of rejecting a *known nested* delegate and needs fixture-level verification.

## Not yet established

The original **2023 Trac Bitmap writer's** MIME policy, delegated-content handling, encoding policy and cursed/reinscription behaviour are **not established** by the 2025–26 Rust port. Do not backdate the above rules to 2023 solely because the endpoint was active then.

When continuing the audit, verify 2023 writer/deployment evidence and any fixture that demonstrably produces different District winners; treat operational configuration separately from eligibility unless its effect on validity is demonstrated.
