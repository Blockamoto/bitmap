# District Rule Registry

The Index column is deliberately blank until rule positions are assigned. Rows follow the current historical ordering; after assignment, new rules are appended without renumbering.

| Index | Rule | Default | Introduced | Definition |
| --- | --- | :---: | --- | --- |
|  | [BMP101 District prototype schema](bmp101-district-prototype-schema.md) | 0 | 24 May 2023 | Accept a JSON District claim with `"p":"bmp101"`, `"op":"dis"`, and a `"dis<height>":"<name>"` entry; `"memo"` is optional. |
|  | [Canonical District schema](canonical-district-schema.md) | 1 | 1 June 2023 | Accept exact `<height>.bitmap` content, with height `0` or a decimal integer without leading zeros. |
|  | [Hash-prefixed District schema](hash-prefixed-district-schema.md) | 0 | 3 June 2023 | When enabled, accept exact `#<height>.bitmap` as an alternative District schema. |
|  | [Plain-text inscription (`text/plain`)](plain-text-inscription.md) | 1 | 3 June 2023 | Require MIME media type `text/plain`, allowing parameters such as `charset=utf-8`. |
|  | [Claimed block exists](claimed-block-exists.md) | 1 | 16 June 2023 | Require the claimed height to be no greater than the inscription's reveal-block height. |
|  | [Unix timestamp ordering](unix-timestamp-ordering.md) | 0 | — | Prefer the eligible claim whose reveal block has the lowest Unix timestamp; ties remain unresolved without an additional rule. |
|  | [Lowest inscription number](lowest-inscription-number.md) | 0 | 26–27 July 2023 | Prefer the eligible claim with the lowest signed Ordinals inscription number. |
|  | [Bitcoin transaction ordering](bitcoin-transaction-ordering.md) | 1 | 28 September 2023 | Prefer the eligible claim in the earliest reveal block, then at the earliest Bitcoin transaction index. |
|  | [JSON MIME exception for District claims](json-mime-exception.md) | 0 | 19 September 2025 | Also permit the `application/json` MIME prefix for otherwise exact canonical `<height>.bitmap` District content; does not accept JSON-object claims. |

History, evidence, and clarifications belong on each rule's page.
