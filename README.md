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

The Bitmap Chain is a reproducible SHA-256-linked record of applying the Bitmap Ruleset to Bitcoin. It commits to an indexer's source blocks, applicable rules, and outcomes; it does not determine Bitmap validity or require every indexer to produce a chain.

**start:** the Bitcoin block containing the reveal of `0.bitmap`. Process subsequent Bitcoin blocks in height order.

**scope:** Districts and Parcels each have their own Bitmap Chain and Outcome Chain, using the same algorithm. Parcel indexing depends on District validity, but the Parcel chain never incorporates the District chain hash.

**registry:** rules have immutable canonical definitions and permanent positions in an append-only registry. Each rule has activation and retirement block-height arrays, allowing an on/off history. Changes take effect forward only; earlier blocks retain the rules that applied at their heights.

**ruleset registry hash:** at each height, take the registry slots in canonical index order. A rule first contributes a slot at its first activation height. While active, its slot is the 32-byte SHA-256 hash of its exact immutable definition bytes; while inactive after introduction, its slot is 32 literal zero bytes. Concatenate the 32-byte slots and SHA-256 hash them. The activation/retirement heights select the slots' state; rule IDs, heights, and switches are not separately included in this hash.

**outcome hash:** SHA-256 hash the canonically encoded valid inscription IDs resolved for the current block.

**outcome chain hash:** SHA-256 hash the previous Outcome Chain Hash concatenated with the current Outcome Hash. This preserves a separately comparable history of indexing results.

**bitmap chain hash:** SHA-256 hash the previous final Bitmap Chain Hash together with the current Bitcoin Block Hash, Ruleset Registry Hash, and Outcome Chain Hash. This commits to the complete history, including rule or source divergence even when outcomes agree or later converge.

**comparison:** matching Outcome Chain Hashes indicate matching committed outcome histories; matching final Bitmap Chain Hashes indicate matching complete committed histories (assuming the same chain specification). The Ruleset Registry Hash may recur if the same active rules recur, without erasing their intervening history from the final chain.

**still to specify:** exact inscription-ID serialization and ordering (including empty results), rule-definition byte encoding, exact final-hash input byte order, and initialization of previous hashes at the first block. A separate rolling ruleset chain remains under consideration; it is not part of this draft.
