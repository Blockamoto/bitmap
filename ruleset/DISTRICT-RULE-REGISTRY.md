# District Rule Registry

Initial District draft. The **Index** column is intentionally blank. Rows are arranged by their best-known historical introduction order; indexes become permanent once assigned.

| Index | Rule | Default | Introduced | Definition |
| --- | --- | :---: | --- | --- |
|  | BMP101 District prototype schema | 0 | 24 May 2023 (public release) | Accept a JSON District claim with `"p":"bmp101"`, `"op":"dis"`, and a `"dis<height>":"<name>"` entry; `"memo"` is optional. |
|  | Canonical District schema | 1 | 1 June 2023 (`0.bitmap` inscribed as `text/plain`) | Accept exact `<height>.bitmap` content, with height `0` or a decimal integer without leading zeros. |
|  | Hash-prefixed District schema | 0 | 3 June 2023 | Retracted documentation typo. When enabled, accept exact `#<height>.bitmap` as an alternative District schema. |
|  | Text inscription | 0 | June 2023 | Assumed to mean MIME type `text/`; subtype unspecified in the original wording. |
|  | Claimed block exists | 1 | By 16 June 2023 | Require the claimed height to be no greater than the inscription's reveal-block height. |
|  | Unix timestamp ordering | 0 | Date unverified | Prefer the eligible claim whose reveal block has the lowest Unix timestamp; an equal timestamp remains a tie unless separately resolved. |
|  | Lowest inscription number | 0 | 26–27 July 2023 | Prefer the eligible claim with the lowest signed Ordinals inscription number. |
|  | Bitcoin transaction ordering | 1 | 28 September 2023 | Prefer the eligible claim in the earliest reveal block, then at the earliest Bitcoin transaction index. |

Evidence, rationale, and indexer-specific rules will be examined separately. Nothing in this draft assigns permanent rule indexes.
