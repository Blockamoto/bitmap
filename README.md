# bitmap

Bitmap is a standard for claiming Bitcoin blocks as districts through Ordinals inscriptions

## standard district ruleset

**schema:** `<district>.bitmap` · regex = `^(?:0|[1-9][0-9]*)\.bitmap(?![\s\S])`

**body:** claimant's own inscription envelope body bytes

**text:** parsed MIME type `text/plain` (case-insensitive, parameters permitted)

**ascii:** ASCII bytes (UTF-8 compatible), ignoring declared charset

**height:** `<district>` ≤ reveal block height

**order:** first qualifying inscription reveal per district
