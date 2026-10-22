# District Rule Registry

Draft for review. The **Index** column is intentionally blank. Rows follow the best-known historical introduction order for this initial pass. Once assigned, registry indexes remain fixed; later discoveries are appended.

| Index | Rule | Default | Introduction | Definition | Evidence / rationale |
| --- | --- | :---: | --- | --- | --- |
|  | Canonical District schema | 1 | June 2023 | An inscription's content matches `^(?:0\|[1-9][0-9]*)\\.bitmap$` exactly. | Original `<height>.bitmap` format; no leading zeros or extra characters. |
|  | Hash-prefixed District schema | 0 | 3 June 2023 | Accept exact `#<height>.bitmap` as an **alternative** schema. | A tutorial typo, corrected on 14 June and explicitly rejected in the verification guide on 16 June. Schema alternatives are OR choices. |
|  | Text MIME family | 0 | June 2023 | Require an inscription MIME type beginning with `text/`. | Retrospective executable interpretation of the early phrase “text inscription”; the published wording did not name a subtype. |
|  | Claimed block exists | 1 | By 16 June 2023 | Claimed height must be no greater than the inscription's reveal-block height. | Excludes claims on future blocks. |
|  | Unix timestamp ordering | 0 | Date unverified | Prefer the eligible claim with the lowest reveal-block header timestamp; an equal timestamp leaves a tie unless separately resolved. | Historical lead awaiting corroboration. Block timestamps are not guaranteed to increase with block height and cannot order claims within the same block. |
|  | Lowest inscription number | 0 | 26–27 July 2023 | Prefer the eligible claim with the lowest **signed** inscription number. | July “first is first” wording. Negative cursed numbers may give later inscriptions precedence. |
|  | Bitcoin transaction ordering | 1 | 28 September 2023 | Prefer the eligible claim in the earliest reveal block, then earliest Bitcoin transaction index. | Supersedes inscription-number ordering. Ordering multiple claims within one transaction remains to be specified. |

Only the three defaults marked `1` are provisionally enabled. This table records the District rules identified so far; indexer-specific additions are reserved for the later audit.

## Historical references

- [Early Bitmap verification guide](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/archive/_old/bitmap-theory-101/how-to-verify-blocks.md)
- [District Ruleset snapshot](https://github.com/Blockamoto/gitbook/blob/d541a50ee13da4637c38a77b9f8b69a541a741a1/areas/the-bitmap-standard/district-ruleset.md)

Dates and interpretations not yet supported by those snapshots remain subject to the historical audit.
