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

> **Experimental / work in progress.** This is a draft commitment scheme, not a finalized specification or a new Bitmap validity requirement. Serialization, first-block initialization, and test vectors remain to be settled.

The Bitmap Chain is a reproducible SHA-256-linked record of applying the Bitmap Ruleset to Bitcoin. It commits to an indexer's declared source, applicable rules, and outcomes so that independent indexes can be compared. A matching commitment alone does **not** prove the rules were executed correctly.

**start:** the Bitcoin block containing the reveal of `0.bitmap`. Process subsequent Bitcoin blocks in height order.

**scope:** Districts and Parcels each have their own Ruleset Chain, Outcome Chain, and final Bitmap Chain, using the same structure. Both reference the Bitcoin source chain. Parcel indexing depends on District validity, but the Parcel chain never incorporates the District chain hash.

**per-block advancement:** advance all three Bitmap commitment chains **once for every Bitcoin block**, even when no rule changes and no valid inscriptions are found. Chain positions correspond to Bitcoin heights, not to individual transactions or only to ruleset changes.

**bitcoin source chain:** use the current Bitcoin Block Hash, which already commits to previous Bitcoin blocks through the block-header predecessor link. Verify the source block's relationship to the previous Bitcoin block; do not construct a second Bitcoin-source hash chain.

**registry:** rules have immutable canonical definitions and permanent positions in an append-only registry. Each rule has activation and retirement block-height arrays, allowing an on/off history. Changes take effect forward only; earlier blocks retain the rules that applied at their heights.

**ruleset registry hash:** at each height, take registry slots in canonical index order. A rule first contributes a slot at its first activation height. While active, its slot is the 32-byte SHA-256 hash of its exact immutable definition bytes; while inactive after introduction, its slot is 32 literal zero bytes. Concatenate the 32-byte slots and SHA-256 hash them. The activation/retirement heights select the slots' state; rule IDs, heights, and switches are not separately included in this hash.

**ruleset chain hash:** SHA-256 hash the previous Ruleset Chain Hash together with the current Ruleset Registry Hash. This preserves an independently comparable history of the *applied* ruleset at every block. If a rule is turned off and later on again, the current Ruleset Registry Hash may recur, but the Ruleset Chain Hash retains the intervening history.

**outcome hash:** SHA-256 hash the canonically encoded valid inscription IDs resolved for the current block.

**outcome chain hash:** SHA-256 hash the previous Outcome Chain Hash together with the current Outcome Hash. This preserves an independently comparable history of indexing results.

**subtotal hash:** SHA-256 hash the current Bitcoin Block Hash, Ruleset Chain Hash, and Outcome Chain Hash together. It binds the three constituent histories at the current height, without its own predecessor link.

**final bitmap chain hash:** SHA-256 hash the previous final Bitmap Chain Hash together with the current Subtotal Hash. This provides an explicitly linked history of the combined commitments.

**hash relationships (conceptual):**

```text
B[h] = Bitcoin Block Hash at height h (the Bitcoin source chain)
R[h] = SHA256(canonical ruleset registry slots at height h)
D[h] = SHA256(canonically encoded valid inscription IDs at height h)

Q[h] = SHA256(Q[h-1] || R[h])       Ruleset Chain Hash
O[h] = SHA256(O[h-1] || D[h])       Outcome Chain Hash
S[h] = SHA256(B[h] || Q[h] || O[h]) Subtotal Hash
F[h] = SHA256(F[h-1] || S[h])       Final Bitmap Chain Hash
```

Here `||` denotes concatenation. These formulas express the proposed hash dependencies and working input order, **not yet a finalized byte-level encoding**.

**rolling checkpoint:** advancing the commitments requires the previous Bitcoin Block Hash (to check source continuity), previous Ruleset Chain Hash, previous Outcome Chain Hash, and previous final Bitmap Chain Hash, plus the current block inputs. These four previous hashes are sufficient *rolling commitment heads*, not a replacement for the index state and evidence needed to determine valid Districts and Parcels.

**comparison:** matching Ruleset Chain Hashes indicate matching committed ruleset histories, and matching Outcome Chain Hashes indicate matching committed outcome histories. The Bitcoin Block Hash identifies the source history; the final Bitmap Chain Hash binds all three histories with its own predecessor. Compare commitments at the same height and from the same start and initialization. Retained intermediate heads (or data sufficient to recompute them) permit locating the earliest divergence; tip hashes alone do not reveal where it occurred. A disagreement reveals differing commitments, not which indexer is correct.

**still to specify:** exact inscription-ID serialization and ordering (including empty results), rule-definition byte encoding, hash digest serialization/byte order, first-block initialization for `Q`, `O`, and `F`, and reproducible test vectors.
