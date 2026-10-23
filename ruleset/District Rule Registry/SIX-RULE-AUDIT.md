# Six-rule District consolidation audit

**Date:** 23 October 2026  
**Repository and branch:** `Blockamoto/bitmap`, `draft/district-rule-registry`  
**Starting commit:** `ccc2b6b2c32a8d6db934ddea39609c6d32eddc26`  
**Scope:** The six entries from Brotli downwards, plus directly dependent naming and composition corrections. Districts only. This is a documentation/source-code audit, not a full-chain replay or a production-validator release.

**Subsequent creator QA (23 October 2026):** The original audit below records the former ordering with `text` after `order`. The [current registry](README.md) now lists the six approved enabled rules as `schema`, `body`, `text`, `ascii`, `height`, `order` at provisional indices `0`–`5`, followed by the first disabled rule `content` at index `6`. Schema's reference regex is hardened, and Order now uses lowercase `i` in `TXi`. Standard values remain unchanged; the dated findings below remain an audit snapshot.

## Outcome

The registry still contains **16 active rules**. Every proposed Standard value is unchanged. The final six are:

| ID | Standard | Decision |
| --- | :---: | --- |
| `brotli` | 0 | Keep the independent decompression-permission question. Correct the Bitcoin/Ord/HTTP explanation and expose the still-unfrozen execution details. |
| `exclusion` | 0 | Rename `encoding_tag_exclusion` as requested; preserve the claimant's raw tag-9 veto. |
| `nested` | 0 | Rename `nested_delegate_exclusion`; tighten the predicate to the decoded-reference test actually evidenced in Trac. |
| `negative` | 0 | Rename `negative_inscription_number_exclusion`; preserve exact signed-number comparison. |
| `delegate` | 0 | Rename `delegate_exclusion`; preserve the claimant's raw tag-11 veto. |
| `prefix` | 0 | Keep the short ID and last position; add OPI evidence and correct the explanation of MIME matching. |

`text=1` stays directly after `order` and immediately before `content`. Its historical-impact comparison is still required before proposing a Standard change. No numeric bit positions, profile hashes, main-branch files or Parcel rules are changed.

No one of the six was deleted or merged with another: each has a concrete separating case. Conditional redundancy in one profile is not general equivalence. Descriptive filenames are retained so previously published relative links keep working; the active IDs themselves are single words.

## 1. Brotli: keep, but separate source from decoding

The original framing, "Bitcoin does not resolve Brotli but Ord does", combined data acquisition, content selection and decompression. A Bitcoin reader can decompress committed body bytes explicitly. Conversely, an Ord accessor can return the same stored compressed bytes without decoding them.

The [Ord 0.29.1 tag](https://github.com/ordinals/ord/tree/0.29.1) resolves to commit `d2ff0a789033e3d784048a23e856f15c54e88806`. Its [body accessors and wallet compressor](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/inscriptions/inscription.rs) return stored body bytes and produce Brotli only when compression makes the body smaller. Its [content response handler](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/subcommand/server/r.rs#L250-L357) can pass encoded bytes with a header, perform server-side Brotli decoding under a configured condition, or report not acceptable. Client-side decoding is another layer. Therefore a URL or a node brand does not define the byte interpretation used for a District claim.

The `content` page now explicitly pins **source selection**, not incidental HTTP decoding. Switching source must not silently switch compression policy. A claimant-specific metadata veto also remains about the claimant, even when a delegate supplies the body.

I retained the old additional-eligibility interpretation of `brotli`: disabled means decompression cannot rescue a nonmatching raw body, not "reject every encoding declaration". I did not quietly adopt a new trigger. The page proposes a tag-required, single-decode contract for review and lists the remaining stream/failure/version/bound requirements. With `schema=1` and `height=1`, a qualifying decoded claim can be at most `decimal_digits(reveal_height) + 7` bytes, which provides a principled output limit for that combination.

The [Trac-derived parser](https://github.com/Trac-Systems/ord-tap/blob/b8f6ea35cf6b9d405d4db7c58555e3c8ab33e8cd/src/index/updater/inscription_updater/tap/ops/bitmap.rs#L4-L42) has no Brotli decode in its District body path. The [inspected historical OPI parser](https://github.com/bestinslot-xyz/OPI/blob/4987c31eacb6d77a56124daaa98fe2f2595cfb5b/modules/bitmap_index/bitmap_index.py#L57-L71) decodes supplied body hex as UTF-8. Those findings do not certify every upstream export or deployment. `brotli` remains a useful proposed comparison route, not falsely labelled a verified 2023 policy.

### Gzip is separate, but not silently added

You were right to distinguish gzip from Brotli. The pinned Ord server can pass a `gzip`-labelled body to a client advertising gzip; its server-side `--decompress` fallback, however, is specifically Brotli-only. See its [encoding negotiation helper](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/subcommand/server/accept_encoding.rs) and the response handler above.

No active `gzip` bit was added. The inspected Bitmap paths did not establish a gzip-decoding comparison requirement, and transport support alone does not establish District validity. A gzip route should be separately proposed and specified, not hidden inside `brotli` or automatically activated by `content`.

## 2. Exclusion: tag presence, not decompression

The name is now `exclusion`, as requested. Its scope is explicitly limited to **raw tag 9 on the claimant**. Empty, unsupported and malformed values still count; property-encoding tag 19 and tag-looking bytes in a body do not.

This is not redundant with `brotli`. A raw canonical `123.bitmap` carrying tag 9 can pass raw evaluation with `brotli=0`, while `exclusion=1` rejects it solely for the declaration. Turning `exclusion` off does not grant permission to decompress anything.

The [Ord envelope parser](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/inscriptions/envelope.rs#L28-L91) and [accessors](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/inscriptions/inscription.rs) show why raw field presence and a successfully parsed/exported property are not identical.

Live OCI's broad encoding rejection remains a reported target, not an independently verified implementation match in this pass. The exact program and parser were not recovered. In particular, an exported-property truthiness test need not reject every empty or malformed raw declaration. I retained the current raw-presence draft definition and stated that evidence boundary explicitly.

## 3. Nested: real additional veto, not normal Ord behavior

`nested` remains separate from the `content` resolver. Ordinary one-hop resolution reads B's own body for A; it does not necessarily reject A because B references C. Trac's [pinned creation hook](https://github.com/Trac-Systems/ord-tap/blob/b8f6ea35cf6b9d405d4db7c58555e3c8ab33e8cd/src/index/updater/inscription_updater.rs#L1245-L1320) explicitly rejects that nested situation.

The definition is tightened in an important way: Trac tests **decodable** delegate references. A malformed raw tag on B is not sufficient if `B.delegate()` returns none. C need not itself resolve for the nested test to trigger. This precision correction is recorded as a definition change for review, not disguised as a name-only edit.

The old broken link to the deleted `delegate-content-resolution.md` page is removed. Normal resolution now points to `content`, and failed resolution to `fallback`.

The early September 2025 path placement and subsequent [25 September revision](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) remain historical evidence, not proof of original 2023 enforcement. Missing-target handling must also be distinguished from a local fetch failure before claiming reproducible historical results.

## 4. Negative: literal signed numbers, not every curse label

The ID is now `negative`, deliberately not `cursed`. The predicate remains `inscription_number < 0`. It does not independently reject a positive-numbered vindicated inscription, every reinscription or every unbound inscription.

The [Trac-derived creation path](https://github.com/Trac-Systems/ord-tap/blob/b8f6ea35cf6b9d405d4db7c58555e3c8ab33e8cd/src/index/updater/inscription_updater/tap/ops/bitmap.rs#L4-L42) and [OPI reader](https://github.com/bestinslot-xyz/OPI/blob/7933f5d05d978fc226df8126026ed92f8c45d03b/ord/db_reader/src/server.rs#L309-L325) both show this exclusion. The dated [Trac addition](https://github.com/Trac-Systems/ord-tap/commit/12ddc36ccfa7655a2bbec20d0245deecdec0ec55) is not a universal inception date.

`negative` is eligibility; `number` is winner ordering. I kept them separate and updated the `number` page's live reference. The number page retains the important caveat that the observed OPI procedure is block-first and number-ordered within each block, not an unconstrained global signed-number sort. No comparator or default was changed.

## 5. Delegate: keep the all-declarations veto distinct

The ID is now `delegate`, and the page explicitly says that enabling it **excludes**, rather than enables, delegate-tagged claimants. Its predicate remains exact raw tag 11 in the claimant's envelope, regardless of target validity or availability.

Selecting `body` does not itself reject such an inscription: its own bytes can be a valid claim despite having a delegate field. `delegate=1` adds that veto. Likewise, `delegate=0; nested=1` permits ordinary delegates but rejects the narrower Trac nesting case. This is why neither a merge with `body` nor a merge with `nested` is justified.

As with encoding, Live OCI's exact treatment of empty and malformed raw fields still needs primary implementation evidence. The page no longer allows the general reported behavior to stand in for that missing byte-level verification.

## 6. Prefix: keep last; stronger evidence, narrower claims

`prefix=0` remains at the bottom. I did not adopt loose prefix matching as the Standard or reopen the deferred parser-versus-regex decision.

The audit found related **OPI evidence from December 2023**, earlier than the Trac 2025 snapshot previously highlighted. The [historical query](https://github.com/bestinslot-xyz/OPI/blob/4987c31eacb6d77a56124daaa98fe2f2595cfb5b/modules/bitmap_index/bitmap_index.py#L99-L110) and [pinned current reader](https://github.com/bestinslot-xyz/OPI/blob/7933f5d05d978fc226df8126026ed92f8c45d03b/ord/db_reader/src/server.rs#L309-L325) compare the hex representation with the literal `text/plain` prefix. Lowercasing a hexadecimal spelling is not lowercasing the MIME text it encodes.

Three wording corrections matter. Valid `charset` parameters pass the literal prefix check, so earlier conversational wording suggesting otherwise was wrong. `text/plainish` need not be malformed MIME syntax; it is simply a different subtype. And a literal lowercase prefix can reject `TEXT/PLAIN` even though MIME type comparison is case-insensitive, so the comparison is not purely a widening operation. See [RFC 2045 section 5.1](https://www.rfc-editor.org/rfc/rfc2045.html#section-5.1).

There is also a remaining **raw-byte versus UTF-8 intake** difference: Trac's [content-type accessor](https://github.com/Trac-Systems/ord-tap/blob/b8f6ea35cf6b9d405d4db7c58555e3c8ab33e8cd/src/inscriptions/inscription.rs) requires a UTF-8 string, while OPI's shown reader compares hex. A non-UTF-8 suffix after the expected prefix is a synthetic separating input. I documented that gap rather than claiming a single comparator bit already reproduces every malformed-field path of both systems.

### Adjacent atomicity fix: JSON

The `json` detail page said "beginning with application/json", which secretly enabled prefix matching inside a supposedly independent MIME-label rule. I changed it to the `application/json` **label**, with literal prefix behavior only when `prefix=1`. No JSON-object claim grammar is introduced and `json` remains `0`. The obsolete suggestion that source selection had not yet been distinguished at all is replaced by links to the already separate `body` and `content` rules.

## Validation performed and not performed

The accompanying [synthetic check script](six-rule-checks.py) passed **32 checks, 0 failures** under Python 3.13 and Brotli 1.2.0. It demonstrates exact claim-byte checks, genuine Brotli and gzip round-trips, tag-presence counterexamples, decoded-reference nesting, signed-number boundaries and MIME comparator differences.

These are **small predicate/codec checks**, not native Ord/Trac/OPI integration tests, not a full MIME or inscription-envelope parser, and not proof of any real historical outlier. The script states those boundaries explicitly.

The registry remains at 16 unique single-word IDs with the same six `1` values and ten `0` values. This pass does not run Bitcoin history, produce winner-ID datasets, change deployed hashes, or establish the exact Live OCI program. No claim is made that the proposed Standard matches every major index in all edge cases.

## Review checkpoints left visible

The tagged single-decode Brotli proposal and its error/stream contract still need approval before an executable `brotli=1` profile is frozen. The precise Live OCI parser needs recovery before the raw tag vetoes can be declared exact replicas. Prefix matching remains last for the later focused review, including the OPI-versus-Trac malformed-field ingestion difference. Delegation comparisons also need a fixed replay snapshot rather than reliance on a live node's transient lookup results.

Finally, the planned `text=1` versus `text=0` historical comparison should compare **winning inscription IDs for every District at a specified block hash**, holding other choices constant. Equal counts are insufficient. Zero differences through that cutoff would support a simplification proposal, but would not prove that future inscriptions under the two policies can never diverge.

These open points are deliberately explicit. The consolidation shortens names and removes accidental coupling without silently turning a documentation clean-up into a new Standard policy.
