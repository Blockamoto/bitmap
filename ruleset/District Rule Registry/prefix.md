# Prefix

**Code ID:** `prefix`  
**Standard:** `0`  
**Review position:** Last in the registry, as requested. No default or placement change in this audit.

## Definition

When enabled, replace parsed MIME media-type matching with **literal, case-sensitive prefix matching** for the MIME labels allowed by the profile:

- the plain-text branch uses `starts_with("text/plain")`;
- the JSON branch uses `starts_with("application/json")` only when [`json=1`](json.md).

Do not trim, case-fold, require a semicolon boundary, or validate trailing parameters in this prefix comparator. When disabled, the selected MIME branches use parsed media types instead. The precise production MIME parser and malformed-field ingestion still need to be pinned.

`prefix` changes **how a label is matched**, not which MIME labels are enabled, how a body is decoded, or the District body grammar. Under the agreed no-MIME-filter interpretation of `text=0`, `json` and `prefix` do not reintroduce a MIME restriction.

## Examples and corrections

| Declared type | Parsed `text/plain` branch | Literal `text/plain` prefix |
| --- | --- | --- |
| `text/plain` | Pass | Pass |
| `text/plain;charset=utf-8` | Pass | Pass |
| `text/plain;charset=banana` | Pass syntactic media-type check; no charset decoder selected | Pass |
| `text/plainish` | Fail: different subtype | Pass |
| `TEXT/PLAIN` | Pass under case-insensitive MIME type comparison | Fail |

An unknown charset name is not permission to transcode; [`ascii`](ascii-byte-matching.md) independently requires the actual claim bytes. Earlier conversational wording suggesting that Trac's prefix check rejects charset parameters was incorrect.

`text/plainish` and `application/jsonbogus` need not be syntactically malformed MIME types. They are **different subtype tokens** from `plain` and `json`. Literal prefix matching can admit them anyway. Conversely, a case-sensitive prefix can reject uppercase spellings accepted by MIME type comparison, so this option is not simply a superset of strict matching. See [RFC 2045 section 5.1](https://www.rfc-editor.org/rfc/rfc2045.html#section-5.1).

## Implementation evidence

- [OPI, 5 December 2023](https://github.com/bestinslot-xyz/OPI/blob/4987c31eacb6d77a56124daaa98fe2f2595cfb5b/modules/bitmap_index/bitmap_index.py#L99-L110) filters the hex-encoded content-type field with a `LIKE '746578742f706c61696e%'` prefix. This is earlier verified related evidence than the Trac 2025 snapshot; it is not proof of first-ever use.
- [OPI reader at `7933f5d0`](https://github.com/bestinslot-xyz/OPI/blob/7933f5d05d978fc226df8126026ed92f8c45d03b/ord/db_reader/src/server.rs#L309-L325) still tests that hex prefix. Lowercasing the **hexadecimal spelling** does not lowercase the encoded MIME text.
- [Trac initial 19 September 2025 snapshot](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater.rs#L984-L989) accepts `text/` or `application/json` prefixes. The [25 September change](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) narrows the first branch to `text/plain`. Broader `text/*` remains history under [`text`](plain-text-inscription.md), not a restored bit.
- The [pinned Trac implementation](https://github.com/Trac-Systems/ord-tap/blob/b8f6ea35cf6b9d405d4db7c58555e3c8ab33e8cd/src/index/updater/inscription_updater.rs#L1305-L1316) applies the two literal prefixes to the effective payload's content type.

## Remaining comparison boundary

Trac first obtains a valid UTF-8 string through its [`content_type()` accessor](https://github.com/Trac-Systems/ord-tap/blob/b8f6ea35cf6b9d405d4db7c58555e3c8ab33e8cd/src/inscriptions/inscription.rs). OPI's shown reader compares hex/raw-byte prefixes instead. A content-type field containing `text/plain` followed by a non-UTF-8 byte can distinguish those intake paths even though the literal prefix is identical.

This audit records that **unresolved ingestion distinction** instead of claiming `prefix=1` alone perfectly reproduces both entire indexers. Establish a fixture from the actual upstream exports before deciding whether another comparison policy is needed. No new bit is allocated on that basis here.

This rule is retained for comparison, not turned on in Bitmap Standard. It remains last for the later focused review.

[Registry](README.md) · [Audit report](SIX-RULE-AUDIT.md).
