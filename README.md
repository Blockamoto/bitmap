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

# bitmap product

Bitmap inscriptions and the sats on which they are inscribed inherit Ordinals capabilities, including content, metadata, metaprotocols, delegates, properties (including galleries and attributes), and reinscriptions.

Beyond the Bitmap claim itself, Bitmap prescribes no specific content, use case, or product standard. Products may adopt existing standards, define their own, or support multiple standards.

Reinscriptions enable additional content to be associated with a Bitmap sat, while the Bitmap Interoperable Metadata Convention is recommended for interoperability of metadata and standards.

## reinscriptions

Multiple inscriptions may occupy the same sat. Each inscription remains independent, and products may interpret them individually or together.

## bitmap interoperable metadata convention

Recommended for interoperability of metadata and standards.

**structure:** a top-level CBOR map containing key-value pairs.

**key:** identifies an independent standard or metadata format.

**value:** any valid CBOR value, defined by its corresponding key.

**reading:** interpret recognised keys; ignore unrecognised keys.

**example:** illustrative JSON-style representation with placeholder identifiers and values.

```json
{
  "<standard-one>": "<value>",
  "<standard-two>": {
    // Custom metadata
  }
}
```

### platform preference

A Bitmap may declare a preferred platform through metadata reinscriptions. Preference does not restrict other platforms.

**key:** `platform`

**value:** CBOR map containing `id` and `block`.

**id:** inscription ID of the preferred platform.

**block:** Bitcoin block height containing the platform inscription's reveal transaction.

**example:** illustrative JSON-style representation of CBOR metadata.

```json
{
  "platform": {
    "id": "<inscription-id>",
    "block": 792435
  }
}
```
