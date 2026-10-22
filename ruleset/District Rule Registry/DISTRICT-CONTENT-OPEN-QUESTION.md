# Open question: what does a District inscription's “content” mean?

**Decision status:** **Unresolved. Do not infer or silently amend the Bitmap Standard.**  
**Added to registry discussion:** 22 October 2026  
**Not a dated historical rule and not assigned an Index number.**

## The actual question

When a District rule says that an inscription **contains** exactly `<height>.bitmap`, what is the input?

**A. Own / undelegated content.** Validate the bytes physically present in *the claimant inscription's own envelope* (Ord `Inscription.body()`, comparable to `/r/undelegated-content/<id>`). The candidate's own declared content type is tested separately.

**B. Effective / served content.** If the claimant inscription A carries a delegate tag to B, validate B's own content bytes and MIME as the effective content for A (one level, as implemented by Ord's `/content/<id>` route and the later Trac-derived code). Do not imply recursive traversal A → B → C.

**C. Delegate-tag eligibility is a separate question.** Even if the content source is A's own bytes, a profile could either **allow** or **exclude** inscriptions that merely carry a delegation tag. “Use undelegated content” does not necessarily mean “reject all delegated inscriptions.” Conversely, permitting one-level delegation does not itself determine that the *delegated* body may satisfy a District claim.

**D. Nested delegate exclusion** is a further independent veto, only relevant when a candidate carries a delegate tag that is otherwise eligible. It must not silently settle choices A–C.

## Dated implementation evidence, not a standard decision

- [19 September 2025 initial `ord-tap` snapshot](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater.rs#L980-L1039): Bitmap creator receives the original `payload`; a nested-delegate check runs only in the later TAP path.
- [25 September 2025 commit `acf6b7b`](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea): resolves `payload_eff` one level first, then applies the MIME and District body checks to those effective fields. A known nested delegate is rejected.
- [Ord content endpoint](https://github.com/ordinals/ord/blob/master/src/subcommand/server/r.rs#L250-L279) follows one delegate hop; [undelegated content endpoint](https://github.com/ordinals/ord/blob/master/src/subcommand/server/r.rs#L623-L645) uses A's own inscription. The two endpoints do not define a Bitmap validity rule.
- [Trac District audit](../../index/Trac.md) records the missing original 2023 writer and uncertainties. Do not backdate Rust semantics to 2023.

## Separate rule and implementation questions to revisit

1. Should “content” in the **canonical District schema** be explicitly defined as A (own body), B (effective body), or should its rule describe an abstract candidate-input field chosen by an independent content-resolution rule?
2. Are inscriptions carrying any delegate tag eligible, **even if** their own bytes match the District schema? A **delegate-tag exclusion** is a candidate policy, not decided or assigned a historical date here.
3. Should single-level content resolution remain an independent off-by-default binary compatibility rule? [Current candidate](delegate-content-resolution.md).
4. What happens when B is unavailable? `ord-tap`'s later Rust intake may fall back to A's original payload; this needs an explicit failure/fallback test and a choice about whether it warrants another binary.
5. Can a candidate resolve to another delegate (nested A → B → C)? [Nested delegate exclusion](nested-delegate-exclusion.md) is independently defined but depends on the decisions above.

**Registry guardrail:** Keep existing candidate defaults and canonical content wording **provisional** until this discussion is settled. Do not infer an official 2023 rule from the 2025 Rust port or silently collapse delegate eligibility, content selection and nested delegation into one switch.
