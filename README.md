# bitmap

Bitmap is a standard for claiming Bitcoin blocks as districts through Ordinals inscriptions

## standard district ruleset

**schema:** `<district>.bitmap` · regex = `^(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])`

**body:** claimant's own inscription envelope body bytes

**text:** parsed MIME type `text/plain` (case-insensitive, parameters permitted)

**ascii:** ASCII bytes (UTF-8 compatible), ignoring declared charset

**height:** `<district>` ≤ reveal block height

**order:** first qualifying inscription reveal per district

## standard parcel ruleset

**schema:** `<parcel>.<district>.bitmap` · regex = `^(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])`

**body:** claimant's own inscription envelope body bytes

**text:** parsed MIME type `text/plain` (case-insensitive, parameters permitted)

**ascii:** ASCII bytes (UTF-8 compatible), ignoring declared charset

**range:** `<parcel>` is a zero-based transaction index within Bitcoin block `<district>` (including index `0` for the coinbase transaction)

**district:** `<district>` has a valid winning District inscription under the standard district ruleset

**parent:** one of the claimant's declared Ordinals parents (tag 3) is that winning District inscription

**provenance:** the claimant's reveal transaction spends an input containing that District parent inscription

**order:** first qualifying inscription reveal per `<parcel>.<district>` in Bitcoin reveal order (block height, transaction index, inscription index)
