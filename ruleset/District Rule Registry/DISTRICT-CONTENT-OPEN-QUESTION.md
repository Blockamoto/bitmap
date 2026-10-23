# District source and delegation distinctions

**Recorded:** 22 October 2026; terminology reconciled 23 October 2026.  
**Scope:** Current draft source, fallback and veto distinctions. Original 2023 language must not be rewritten as though these later choices were explicit then. Numeric positions and executable composition remain pending.

## Independent questions

| ID | Question | Proposed Standard |
| --- | --- | :---: |
| [`body`](inscription-body-source.md) | Evaluate the claimant's own envelope body rather than served-source content. | 1 |
| [`content`](inscription-content-source.md) | Evaluate the source selected for the claimant ID by pinned Ord one-hop resolution. | 0 |
| [`fallback`](fallback.md) | On a failed delegate lookup within enabled content resolution, substitute the claimant's own body and content type. | 0 |
| [`delegate`](delegate-tag-exclusion.md) | Veto a claimant for raw tag-11 presence in its own envelope, regardless of the value. | 0 |
| [`nested`](nested-delegate-exclusion.md) | Veto a claimant whose decoded reference resolves to a target with its own decodable delegate reference. | 0 |

The first two are source selectors, the third is a conditional source override, and the last two are eligibility vetoes. None is defined simply as the negation of another. Historic `content=1` meant own-body input and must not be confused with today's served-source `content` ID.

**Proposed Standard path (23 October 2026 clarification):** `body=1; content=0; fallback=0; delegate=0; nested=0`. The claimant's own envelope body is extracted from Bitcoin transaction input witness Tapscript. The delegate target is **not dereferenced** to obtain claim bytes, but the presence of a delegate declaration is not by itself a disqualification. This leaves the independent MIME, byte, schema, height, order and encoding/exclusion settings to do their stated jobs. The Ord 0.29.1 pin below is only for the disabled `content` alternative, not a general authority over raw envelope recognition.

## Concrete distinction

Suppose A's body is `123.bitmap`, A refers to B, and B's own body is `234.bitmap`.

- `body` tests `123.bitmap` for claimant A.
- `content` tests B's stored `234.bitmap` bytes for claimant A under pinned one-hop resolution, before any separately permitted decompression.
- `delegate=1` vetoes A because its own envelope contains tag 11, even if A's raw body is otherwise eligible.
- `nested=1` vetoes A if B itself has a decodable delegate reference. It need not fetch that reference's target C. A malformed raw value on B that does not decode is not sufficient for the evidenced Trac predicate.

If A has no decodable delegate reference, Ord uses A's own body. A malformed raw delegate field may therefore leave source selection unchanged while still triggering the independent raw-presence `delegate` veto. Do not conflate an absent decoded reference with an absent raw field.

If A has a decoded reference to a missing B, pinned Ord source resolution supplies no served-content claim by default. `fallback=1` can substitute A's own body and content type. This does not override `delegate` or other eligibility vetoes. A successful lookup whose content fails the District schema does not trigger fallback.

`content` is pinned to Ord **0.29.1, commit `d2ff0a789033e3d784048a23e856f15c54e88806`**. This fixes the source-selection reference, not transient HTTP availability, proxy behavior, client auto-decompression or unrelated Ord features. See [the handler](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/subcommand/server/r.rs#L250-L357).

## Coding metadata and claimant metadata are different

Source selection must preserve the selected inscription's stored body and associated metadata before transport/client decoding. [`brotli`](brotli-decompression-eligibility.md) independently asks whether a decompressed variant can qualify. The claimant's [`exclusion`](content-encoding-tag-exclusion.md) tag-9 veto and `delegate` tag-11 veto continue to inspect A, not automatically B. This separation prevents an HTTP request's encoding negotiation from silently becoming a validity rule.

## Historical evidence

- [July 2023 authored rules](https://github.com/blockamotolabs/ruleset/blob/d140da22635b2d286b9b1960f5b3c76ba1a66632/README.md) name a District claim command and grammar without explicitly settling own versus served source or a blanket delegate veto.
- [19 September 2025 Trac-derived initial District parser](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater/tap/ops/bitmap.rs#L4-L23) reads original `payload.body()`.
- [25 September 2025 change](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) introduces the effective payload and moves the nested veto. This is evidence for the later public Rust port, not the original 2023 writer.
- [16 October 2026 working specification](https://github.com/Blockamoto/bitmap-old/blob/ccf7271a61a2cead4781d4a2bb9c86da761f1cd6/DISTRICT-RULESET.md) explicitly distinguishes own-body use from rejecting delegate declarations.
- [Pinned Trac hook](https://github.com/Trac-Systems/ord-tap/blob/b8f6ea35cf6b9d405d4db7c58555e3c8ab33e8cd/src/index/updater/inscription_updater.rs#L1245-L1320) separates nesting detection, effective-payload selection and lookup-failure retention. The [indexer audit](../../index/Trac.md) records the historical evidence boundaries.

## Still to resolve before executable profiles

**Both source bits off:** no source is selected. Define or reject that profile rather than assuming a default.

**Both source bits on:** A may supply two different canonical heights. No approved OR, AND, source priority, simultaneous claim or implicit source-fallback policy exists. The explicit `fallback` bit does not answer that composition question.

**Replay snapshot and availability:** define whether target existence is evaluated at the claimant reveal, at a fixed comparison tip or under another explicitly specified snapshot. Same-block targets and local database failures must have reproducible treatment. Do not let a failed network request stand in for authenticated absence.

**MIME and coding metadata:** source selection has been distinguished, but complete executable linkage, malformed fields, byte transforms and fixtures still need freezing. `json` selects a label and `prefix` a matching method; neither selects a body or a decoder.

**Live OCI:** reported delegate and coding exclusions still need the exact implementation/parser before raw field-presence equivalence can be claimed. The proposed defaults are working decisions, not claims about unanimous historical deployment.

[Registry](README.md) · [Six-rule audit](SIX-RULE-AUDIT.md) · [Production gates](CODE-IDS-AND-REVIEW-GATES.md).
