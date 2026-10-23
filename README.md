# bitmap theory

Bitmap is a standard for claiming Bitcoin blocks as Districts through Ordinals inscriptions, and transactions within those blocks as Parcels through child inscriptions.

# bitmap ruleset

## district standard

**schema:** `<district>.bitmap` · regex = `^(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])`

**body:** claimant's own inscription envelope body bytes

**text:** parsed MIME type `text/plain` (case-insensitive, parameters permitted)

**ascii:** ASCII bytes (UTF-8 compatible), ignoring declared charset

**height:** `<district>` ≤ reveal block height

**order:** first qualifying inscription reveal per `<district>.bitmap`

## parcel standard

**schema:** `<parcel>.<district>.bitmap` · regex = `^(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])`

**body:** claimant's own inscription envelope body bytes

**text:** parsed MIME type `text/plain` (case-insensitive, parameters permitted)

**ascii:** ASCII bytes (UTF-8 compatible), ignoring declared charset

**index:** `<parcel>` ≤ (`TX count` at `block height` = `<district>`) − 1

**child:** claimant is a child inscription of the valid `<district>.bitmap` inscription (parent tag 3)

**order:** first qualifying inscription reveal per `<parcel>.<district>.bitmap`

# bitmap index

## bitmap chain

The Bitmap Chain is a reproducible SHA-256-linked record of applying the Bitmap Ruleset to Bitcoin blocks. It verifies indexing outcomes; it does not define Bitmap validity or require every indexer to produce a chain.

**start:** the Bitcoin block containing the reveal of `0.bitmap`

**chains:** Districts and Parcels use the same process but maintain separate chain hashes. Resolving Parcels depends on District validity, not on the District chain hash.

**registry:** an append-only, canonically ordered list of immutable rule definitions, with activation and retirement block heights. Rule changes apply forward only.

**ruleset hash:** for each block height, concatenate 32-byte slots in canonical registry order, including only rules that have reached their first activation. An active rule contributes `SHA256(definition bytes)`; an inactive, previously introduced rule contributes 32 literal zero bytes. Hash the concatenated slots with SHA-256.

**results hash:** SHA-256 commitment to the valid Bitmap claims resolved in the block.

**chain hash:** SHA-256 commitment to the Bitcoin block hash, ruleset hash, results hash, and (except for the first block) the previous chain hash. Each block produces a 32-byte chain hash.

The exact result serialization, chain-input byte ordering, and first-block initialization remain to be specified.
