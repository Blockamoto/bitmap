# District rule code IDs and production review gates

**Status:** Provisional code identifiers, reviewed 22 October 2026. **Not numeric bit indices**, an executable ruleset, a frozen serialization contract, or authorization to commit production hashes.

## Naming convention

Short lowercase `snake_case` names identify **one current binary registry question** and are stable *within this draft review*. The [District registry](README.md) is the source of the currently included set. Code IDs are distinct from display titles, former compound aliases, dated evidence IDs, and future binary positions.

Earlier work had at least two naming systems:

- **Short rule IDs** in [`bitmap-old` District reference](https://github.com/Blockamoto/bitmap-old/blob/main/DISTRICT-RULESET.md): `content`, `text`, `regex`, `height`, `first` and `fiftxi`, with optional `fifin`, `brotli`, `delegate_exclusion`, `encoding_tag_exclusion`, and other exclusion bits.
- **Research/provenance IDs** such as `BMP-DISTRICT-001`, `BMP-CONTENT-003`, `BMP-ORD-001` and `BMP-ORDER-003` in [the older repository's `old` branch](https://github.com/Blockamoto/bitmap-old/blob/old/rules/README.md). These classify claims/evidence and **must not be misread as numeric bit allocations**.

## Exact or close carryovers

| Earlier identifier | Present code ID | Mapping |
| --- | --- | --- |
| `text` | `text` | Same independent `text/plain` media-type check; charset decoding is no longer hidden inside it. |
| `regex` | `regex` | Same canonical `<height>.bitmap` *whole-string* grammar; schema choice separate from claim source. |
| `height` | `height` | Same inclusive `target_height ≤ reveal_height` check. |
| `brotli` | `brotli` | Same default-off *additional Brotli-decompression eligibility*, not an encoding-tag veto. |
| `delegate_exclusion` | `delegate_exclusion` | Same default-off exclusion based on a declared Ord delegate tag. |
| `encoding_tag_exclusion` | `encoding_tag_exclusion` | Same default-off exclusion for Ord content-encoding tag 9 presence. |
| `decoder_mode=raw_utf8_strict` | `raw_utf8_strict` | Same strict UTF-8 decoder alternative; the new binary is independent of MIME filtering and source selection. |

## Related historical names that are **not exact aliases**

| Earlier name | Current related entry | Important difference |
| --- | --- | --- |
| `content=1` | `inscription_body=1` | Old `content` implied *own-body only*. The new body and served-content rules are separate independent bits. If both are enabled, no source-combination policy has yet been agreed. |
| `first=1` | `first=1` | The independent first-eligible-wins policy now has its own active row. It needs a separately declared comparator; `first=0` alone does not define an alternative winner policy. |
| `fiftxi=1` | `precedence_bitcoin_reveal=1` | Old `fiftxi` bundled first-wins + block/transaction/intra-transaction inscription-index ordering. Current row has an open **same-transaction tie**. Not a lossless alias. |
| `fifin=1` | `precedence_inscription_number=1` | Closest historical alternative by lowest signed global inscription number, but old mode also specified *replacement* of the Bitcoin comparator. Incompatible simultaneous precedence modes must be rejected or resolved by declared rules. |
| `raw_utf8_body=1` | `raw_utf8_strict=1` + selected source and independent MIME | The older compound `raw_utf8_body` implicitly bypassed MIME and selected the own body; strict UTF-8 **alone must not** do either. |
| `cursed_exclusion=1` | `negative_inscription_number_exclusion=1` | **Not equivalent:** the current candidate tests negative signed number, not every wider curse/vindication status. Default 0 imposes no negative-number veto; no new cursed-status veto is silently adopted. |
| `reinscription_exclusion=1` | **Not currently active** | Explicitly deferred by creator on 22 October 2026. Preserve [old evidence](https://github.com/Blockamoto/bitmap-old/blob/old/edge-cases/reinscriptions.md), but do not add a live toggle merely because older OPI filtered cursed inscriptions. |

## Current identifier inventory

The code IDs appearing on [README](README.md) are each unique within the active draft. The historical `first` ID is retained as its own standalone binary decision, separate from any precedence comparator. All other newer IDs name only their corresponding written questions: `schema_bmp101`, `inscription_content`, `delegate_content_resolution`, `text_mime_family`, `json_mime`, `mime_prefix_compatibility`, `strict_height`, `nested_delegate_exclusion`, `negative_inscription_number_exclusion`, `precedence_unix_timestamp`, `precedence_inscription_number`, and `precedence_bitcoin_reveal`. None is asserted to have existed as such in 2023.

## Production review gates, still open

1. **Foundational decision completeness:** executable District profiles must select a claim source, a schema, MIME/decoder semantics, an eligibility policy, `first` or a defined alternative winner policy, and exactly one fully deterministic comparator. Defaults are proposed values, not proof of a completed execution contract.
2. **Claim-source combinations:** define or reject `inscription_body=0; inscription_content=0` and `inscription_body=1; inscription_content=1`. Do not invent OR, AND, fallback, or precedence. Separately reconcile the overlap between `inscription_content` and the Trac-specific `delegate_content_resolution`.
3. **Multiple precedence settings:** `precedence_unix_timestamp`, `precedence_inscription_number`, and `precedence_bitcoin_reveal` are comparator choices currently shown as independent historical binaries. Their **combination and precedence constraints** remain to be settled. Unix timestamp ties and within-transaction reveal ties require explicit treatment. The independent [`first`](first-eligible-wins.md) selection predicate now has its own active registry row; profile semantics when it is off still require an explicit alternative.
4. **Data source, MIME, decoding:** pin exact envelope parser, MIME case/parameter handling, charset-label mapping, BOM and missing/malformed-charset behaviour; do not use `raw_utf8_strict` to imply an unstated MIME bypass.
5. **Transform and metadata:** an enabled `brotli` eligibility route needs trigger, decompression limits and failure policy. `encoding_tag_exclusion` is a separate tag-presence veto. No inference from an unverified Live OCI implementation.
6. **Evidence and reproducibility:** fixture inputs must include actual witness bytes, source policy, chain reveal coordinates, collisions, delegated content, encoding edge cases, effective MIME fields and declared profile. Verify version-specific indexer claims rather than declaring historical consensus from one modern source.
7. **No premature allocation:** blank `Index` values, provisional code names and defaults, no canonical serialized profile, no deployed hashes or final production validator.

## Deliberately excluded historical typo

The 3 June 2023 `#<height>.bitmap` tutorial typo was withdrawn/corrected by 14 June, and the 16 June verification guide rejected `#69.bitmap`. The creator has directed that it **not be an active District rule**. Preserve it as documentation history via the [earlier tutorial revision](https://gitbook.bitmap.land/~/revisions/AZO0a8slhI90dZCq0SNg/) and [archived verification guide](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/archive/_old/bitmap-theory-101/how-to-verify-blocks.md), not as a switch that recognizes `#<height>.bitmap`.

**Scope:** District-only. No Parcel or `main` updates.
