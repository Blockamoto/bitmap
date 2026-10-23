# Content: served District claim source

**Code ID (provisional):** `content`  
**Standard:** `0` (provisional current-profile value)  
**Earliest verified related implementation:** 25 September 2025 (`ord-tap` effective-payload change)  
**Explicit binary registry framing:** 22 October 2026  
**Status:** Alternative for where District claim bytes come from, not a delegate eligibility check. Historic `content=1` meant own-body content, now `body`; those are not aliases.

## Definition

When enabled, evaluate the District schema against **content served for the claimant inscription ID**, rather than reading its own envelope body directly. As a consequence of choosing this source, that content could be supplied by a delegate; delegation is not required.

Resolution follows **Ord 0.29.1, commit `d2ff0a789033e3d784048a23e856f15c54e88806`**, using the source-selection behavior of the ordinary [`/content/<id>` handler](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/subcommand/server/r.rs#L250-L279), or equivalent local reproduction:

- If A has no decodable delegate reference, use A's body.
- If A has a decodable reference to B and B resolves, use B's own body. Do not recursively follow B to C.
- A validly decoded reference to a missing B produces no served-content claim by default; it does not substitute A's body. [`fallback=1`](fallback.md) is the separate failed-lookup override.

A malformed raw delegate value can fail Ord's `delegate()` decoding and therefore not initiate a lookup at all. That is different from a decodable but unresolved reference, and different again from the raw tag-presence veto in [`delegate`](delegate-tag-exclusion.md).

When disabled, this source rule contributes no served-content candidate. It neither requires nor forbids the claimant having a delegate tag.

**Boundary relative to the Standard:** `content=0` means the approved `body=1` path does **not** fetch `/content/<id>` or follow the claimant's delegate. The Ord 0.29.1 snapshot cited here is the specified comparison reference **only if this alternative source rule is enabled**. It is not an authority over the ordinary raw-envelope Body rule and does not establish a global Ord version pin or a completed envelope-compatibility test. A future Ord update must not silently alter even this optional resolution behavior.

## Source bytes versus HTTP delivery

This rule selects **which inscription supplies the stored body and associated metadata**. It does not select an implicit transformation pipeline. Preserve the resolved inscription's stored body before HTTP content decoding; the independent [`brotli`](brotli-decompression-eligibility.md) rule controls whether decompression may add eligibility.

Ord's response layer can send compressed bytes with `Content-Encoding`, decompress Brotli under a server option, or return not acceptable depending on the request. A browser/client can also automatically decode. These delivery choices must not alter District validity just because different callers requested the same URL. A client lacking the original selected bytes/metadata must report insufficient evidence, not assume that decoded HTTP bytes are the committed body. Server hiding/proxy settings and transport failures are likewise not District rules.

The pin freezes source-resolution behavior; it does not make local index incompleteness equivalent to a missing on-chain inscription. Replay snapshot, same-block target availability and lookup-error policy still need reproducible fixtures.

## Separate checks and combinations

The independent [`schema`](canonical-district-schema.md), [`ascii`](ascii-byte-matching.md), MIME and exclusion rules apply after source selection. Served metadata can belong to B rather than A; that does not relocate claimant-specific [`exclusion`](content-encoding-tag-exclusion.md) or `delegate` vetoes onto B.

[`nested`](nested-delegate-exclusion.md) is a separate Trac-derived eligibility veto, not part of Ord's one-hop resolution. The two source bits remain independent: both-off and both-on configurations have no automatically assigned OR, AND, precedence or fallback semantics. [`fallback`](fallback.md) only changes an unresolved lookup inside enabled `content`.

Default `body=1; content=0` is unchanged. No additional MIME family, claim grammar, precedence or Parcel policy is introduced.

## History and evidence

- [Ord's pinned content handler](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/subcommand/server/r.rs#L250-L357) separates one-hop source selection from response/coding behavior. Its `/r/undelegated-content` endpoint is a different source route, not used to follow a delegate.
- The [25 September 2025 Trac-derived change](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) changes District input to `payload_eff`, including effective body and MIME. Its distinctive failed-lookup retention of the original payload is separately recorded by `fallback`.
- The superseded `delegate_content_resolution` ID remains retired. Successful one-hop resolution and a failed-lookup fallback are not bundled together again.
- Original 2023 claim-command wording did not expressly distinguish these sources. Neither a modern endpoint nor the later Rust port proves original 2023 deployment behavior.

Future Ord releases do not silently revise this rule. Any changed source or transform semantics require an explicit specification revision.

[Registry](README.md) · [Source composition](DISTRICT-CONTENT-OPEN-QUESTION.md) · [Audit report](SIX-RULE-AUDIT.md).
