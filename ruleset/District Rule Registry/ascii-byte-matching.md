# ASCII District claim bytes

**Code ID (provisional):** `ascii`  
**Standard:** `1`  
**Scope:** District claims only. This is a byte-interpretation rule, not a MIME-label filter or a claim-source selector.

## Definition

When `ascii=1`, interpret the selected inscription bytes as **US-ASCII**, compatible with UTF-8 and other ASCII-compatible character sets for these characters, **ignoring any declared charset**. Reject bytes outside the US-ASCII range (0x00–0x7F); do not transcode, guess encodings, trim, strip BOMs, replace invalid bytes, normalise, or extract strings from other formats.

Pass the resulting characters unchanged to the separate [canonical District schema](canonical-district-schema.md), which only accepts the entire `<height>.bitmap` claim in exact ASCII bytes. An ASCII control character, space or newline is not allowed by that schema even though it is representable in ASCII.

This does not bypass the separate [`text` MIME rule](plain-text-inscription.md), [source rules](inscription-body-source.md), decompression policy or metadata exclusions. A `text/plain;charset=utf-16` declaration alone does not authorise UTF-16-encoded claim bytes.

When `ascii=0`, this rule supplies no byte interpretation. No alternative compatibility decoder is presently defined, so disabling the sole interpretation rule leaves the candidate profile incomplete.

## Why this matches previous strict UTF-8 outcomes

The canonical District grammar uses only US-ASCII characters. UTF-8 encodes them as the exact same single bytes, so strict UTF-8 decoding followed by exact canonical matching and direct ASCII matching accept the **same claims**, provided the selected bytes and any upstream transforms are unchanged. This statement concerns recognised District claims, not arbitrary non-ASCII text.

## Historical context

- [Best in Slot OPI's 5 December 2023 Bitmap module](https://github.com/bestinslot-xyz/OPI/blob/4987c31eacb6d77a56124daaa98fe2f2595cfb5b/modules/bitmap_index/bitmap_index.py#L57-L71) decodes claim bytes with strict UTF-8. The current ASCII-only schema makes that outcome-equivalent here, not identical implementation code.
- The active draft previously called this policy `strict`. On 23 October 2026, its ID was changed to `ascii` with explicit byte-level semantics. Prior draft wording remains in Git history.
- Charset-aware parsing remains [research only](TEXT-ENCODING-COMPARISON.md), not an active compatibility mode.

[Registry](README.md) · [Code ID and review gates](CODE-IDS-AND-REVIEW-GATES.md).
