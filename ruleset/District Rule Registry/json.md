# JSON

**Code ID:** `json`  
**Standard:** `0`  
**Earliest verified related public snapshot:** 19 September 2025. This is not an independently verified original introduction date.

## Definition

When enabled, also permit the **`application/json` MIME label** for a candidate whose selected body still satisfies the exact canonical `<height>.bitmap` schema and all other enabled rules. This adds a MIME alternative, not a JSON-object or JSON-string claim format.

With [`prefix=0`](prefix.md), compare the parsed media type with `application/json`. With `prefix=1`, use the literal `application/json` prefix. **`json` does not itself enable prefix matching.** The earlier definition's phrase "beginning with" accidentally bundled those two separate questions and is removed in this consolidation.

When disabled, this additional label is not enabled. Existing plain-text eligibility is not removed. Under the agreed no-MIME-filter interpretation of `text=0`, this bit is unnecessary and does not impose a new restriction.

## History and evidence

- The [initial Trac-derived public Rust snapshot](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater.rs#L984-L989) accepts `text/` or `application/json` using literal prefixes before the District parser.
- Its [District parser](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater/tap/ops/bitmap.rs#L13-L23) still requires the raw canonical claim. A body `123.bitmap` labelled JSON is different from a body `{"height":123}` or `"123.bitmap"`.
- The [25 September 2025 revision](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) narrows the text branch to `text/plain` while retaining the JSON prefix. The [pinned inspected implementation](https://github.com/Trac-Systems/ord-tap/blob/b8f6ea35cf6b9d405d4db7c58555e3c8ab33e8cd/src/index/updater/inscription_updater.rs#L1305-L1316) retains both alternatives.

These are public Rust implementation findings, not proof of the original 2023 Trac writer or a particular marketplace deployment. [`body`](inscription-body-source.md) and [`content`](inscription-content-source.md) separately select the source; this MIME-label rule does not select it. Source metadata composition still needs the fixtures identified in the [source note](DISTRICT-CONTENT-OPEN-QUESTION.md).

[Registry](README.md) · [Prefix](prefix.md) · [Audit report](SIX-RULE-AUDIT.md).
