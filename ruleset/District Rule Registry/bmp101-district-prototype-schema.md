# BMP101 District prototype schema

**Default:** `0`  
**Introduced:** 24 May 2023

## Definition

Accept a JSON District claim with `"p":"bmp101"`, `"op":"dis"`, and a `"dis<height>":"<name>"` entry; `"memo"` is optional.

## History

- **24 May 2023:** Public-launch date attributed to BMP101 by its creator, associated with the creation of the Blockamoto X account.
- **30 May 2023:** The preserved BMP101 GitBook space and revision were created. This dates the surviving GitBook record, not necessarily the earliest publication.
- The later canonical District schema replaced this prototype in ordinary Bitmap use.

## Evidence

The [BMP101 GitBook protocol example](https://bitmap.gitbook.io/bitcoin-metaverse-protocol-bmp101/3.-the-bmp101-protocol-explained) defines a District claim as:

```json
{
  "p": "bmp101",
  "op": "dis",
  "dis4": "LOCKE",
  "memo": "Optional"
}
```

The `dis4` entry refers to block 4, names the District `LOCKE`, and `memo` is optional.

## Clarifications

- Historical alternative schema, disabled by default.
- This rule concerns recognition of the JSON District claim format; other BMP101 mechanics are not implicitly adopted.
