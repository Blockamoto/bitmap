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
