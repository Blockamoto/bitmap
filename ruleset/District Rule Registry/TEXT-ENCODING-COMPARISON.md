# District text decoding and content-encoding comparison

**Research status:** 22 October 2026. Gathered for the District Registry from `Blockamoto/bitmap-old`, public Trac-derived `ord-tap` and OPI Bitmap source. **Live OCI/Boppleton is not yet independently code-verified.**  
**Scope:** District claim-body eligibility only. Do not import Parcel rules, ownership or asset transfers.

## Distinct operations

1. **Source:** Choose *Inscription Body* (claimant's undelegated bytes) or *Inscription Content* (bytes served for claimant ID; may come from a direct delegate). These are independent binaries in this registry. Neither chooses a text decoder.
2. **MIME filter:** Independently check a `text/plain` media type and any optional MIME-label exceptions. MIME `charset` is **metadata**; honoring the declared charset is a separate decision from MIME eligibility.
3. **Content-encoding tag:** Ord inscription field **9** declares body content encoding such as `br`. A policy can reject **presence of the field** without attempting decompression.
4. **Transform:** A profile can separately permit **Brotli decompression**, whose precise trigger, failure behavior and bounds still require definition. A declared tag does not mean decompression occurred.
5. **Text decoder:** Convert the selected/transformed byte sequence to text, e.g. **strict UTF-8**, **lossy UTF-8**, or **strict declared-charset decoding**, then apply the exact District grammar. The decoder is not the body source and does not itself confer MIME eligibility.

## Historical public code and current evidence

| Implementation/evidence | Earliest verified source | What code establishes | What is not yet established |
| --- | --- | --- | --- |
| **OPI (Best in Slot Bitmap module)** | [5 December 2023 Bitmap indexer](https://github.com/bestinslot-xyz/OPI/blob/4987c31eacb6d77a56124daaa98fe2f2595cfb5b/modules/bitmap_index/bitmap_index.py#L57-L71) | `codecs.decode(content_hex, "hex").decode('utf-8')`: raw body hex → bytes → **strict UTF-8** text; decoding errors cause no District parse. The separate query filters `text/plain` by content-type prefix, not declared charset. | The upstream Ord data/export pipeline's full semantics, whether a content-encoding tag caused an earlier transformation, every historical deployment date, and the treatment of all candidate envelope edge cases. |
| **Trac-derived `ord-tap`** | [19 September 2025 Rust snapshot](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater/tap/ops/bitmap.rs#L13-L23) | `String::from_utf8_lossy(body)` decodes using UTF-8 with replacement for invalid input. MIME eligibility is a different preceding check. No declared charset is used in this District parser. | Whether the original **2023** Trac service used this decoder or accepted a special case; no 2023 writer source was recovered. A literal ASCII schema means replacement behaviour need not change recognized winners. |
| **Live OCI (Boppleton)** | Rules reported during prior Live OCI discussions (16–20 October 2026) are **not independently source-verified here**; the Trac audit should not be cited as evidence of Boppleton’s code. | **Reported**: exact UTF-8 body-content matching; any `contentEncoding` declaration excluded; compressed content not accepted. | The exact source code, treatment of malformed UTF-8 versus raw-byte equality, whether MIME `charset` is interpreted, deployment/activation date, and whether the stated public rules are fully reflected in the implementation. Do **not** assert these are verified from a source artifact. |
| **Bitmap working Standard (design, not an indexer)** | [15 October 2026 working District draft](https://github.com/Blockamoto/bitmap-old/blob/1751e0d37073ab920cbd8b5548c61b74c37716d1/DISTRICT-RULESET.md) and [21 October atomic-options revision](https://github.com/Blockamoto/bitmap-old/blob/63e77aa6f5cd95248e3abad55e168fa2215e0e32/COMPARISON-OPTIONS.md) | Intended baseline named `decoder_mode=declared_charset_strict`, independent `text=1`, `body_transform=none`, `encoding_tag_exclusion=0`; alternative `raw_utf8_strict` and Brotli route separately described. | Charset-label mapping, BOM and absent/malformed-charset fallback, exact transform pipeline, shared test fixtures and whether this conceptual configuration reproduces any external historical indexer. |

## Explicit 2026 interpretation fork

Two distinct **proposed binary registry choices** now record the ambiguity left by the early phrase "text inscription":

1. **[`mime_charset`](mime-charset-decoding.md), Standard `1`:** for `text/plain`, interpret source bytes according to an explicitly declared MIME `charset`; absent a `charset`, RFC 6657 §4 retains the **US-ASCII** MIME default. This is a standards-grounded *working interpretation*, not a recovered 2023 Bitmap decoder mandate. The exact supported charset repertoire, label aliases, malformed parameters, BOM policy and error behaviour must be pinned to reproduce results.
2. **[`raw_utf8_strict`](raw-utf8-strict-decoding.md), Standard `0`:** decode selected bytes using **strict UTF-8** regardless of a declared charset. For the canonical exact ASCII District string, this recognises precisely the same bytes as a direct ASCII-byte full-match, including rejection of extra BOM bytes, newlines or other characters. That equivalence does **not** apply to all possible schemas.

These are **alternatives**, not two compulsory filters. Neither bit silently changes `text`, body-versus-served source, Brotli transform, or encoding-tag exclusion. Both-on and both-off decoder combinations require a declared policy and are not executable by default. Critically, **MIME's US-ASCII fallback is not equivalent to ignoring a declared UTF-16 charset**.

Standards: [RFC 2046 §4.1.2](https://www.rfc-editor.org/rfc/rfc2046.html#section-4.1.2), [RFC 6657 §4](https://www.rfc-editor.org/rfc/rfc6657.html#section-4), [RFC 3629 §3](https://www.rfc-editor.org/rfc/rfc3629.html#section-3), [IANA character sets](https://www.iana.org/assignments/character-sets). The [WHATWG Encoding Standard](https://encoding.spec.whatwg.org/) is **not** interchangeable with the complete IANA registry and does not make every decoder available in every environment.

## Registry entries and proposed Standard values

- [MIME Charset Decoding](mime-charset-decoding.md): `1` (proposed Standard). Honor declared `text/plain` charset or US-ASCII absent one, with implementation details still to be frozen.
- [Raw Strict UTF-8 Decoding](raw-utf8-strict-decoding.md): `0`. Enabling selects strict UTF-8 regardless of declared charset, **without bypassing MIME**.
- [Brotli Decompression Eligibility](brotli-decompression-eligibility.md): `0`. Enabling permits a separately specified decompression route; it is not an encoding-tag veto.
- [Content-Encoding Tag Exclusion](content-encoding-tag-exclusion.md): `0`. Enabling rejects candidates solely for the presence of an Ord tag 9 field, independent of byte transformation.
- The previously registered [Text MIME rule](plain-text-inscription.md) is `1`; this concerns type eligibility only, **not** the decoder or transform.
- [Inscription Body](inscription-body-source.md) `1`, [Inscription Content](inscription-content-source.md) `0`: independent claim-byte sources, not decoder switches.

**Historical note:** OPI strict-UTF8 code is verifiable in its December 2023 public module. Trac-derived lossy UTF-8 appears in its September 2025 public Rust port. Boppleton/Live OCI behaviour is a reported claim pending its own source audit, not a false equivalence with either implementation.

## Pending focused examples

- A correctly declared UTF-16 `text/plain` body encoding `840000.bitmap` compared against a charset-aware decoder and raw UTF-8 decoder. A MIME check passing `text/plain` does **not** guarantee a raw UTF-8 decoder recognizes the body.
- A candidate with invalid UTF-8 bytes but otherwise similar material: OPI's strict decoder rejects malformed bytes, while lossy UTF-8 replacement cannot ordinarily recreate a fully canonical ASCII District string.
- A canonical uncompressed ASCII body with Ord `content_encoding` tag 9 present. Distinguishes a **tag-based veto** from a **transform path**.
- A genuine Brotli-compressed `840000.bitmap` body with/without a `br` tag. Requires deterministic decompression pipeline and declared output bound.
- A delegate-tagged inscription whose own body differs from the delegate-served body. Independent from text-decoder choices.

These are **test recommendations**, not claims that Live OCI has already been QA'd or that particular contested winners are proven.
