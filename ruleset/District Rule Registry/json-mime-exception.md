# JSON MIME exception for District claims

**Code ID (provisional):** `json_mime`  
**Standard:** `0`  
**Introduced:** 19 September 2025

## Definition

When enabled, permit an inscription with a declared content type beginning with `application/json` to qualify as a District claim **if the District claim body chosen by the profile's content-source rule still satisfies the exact canonical `<height>.bitmap` schema and the other enabled validity rules**. This adds an accepted MIME label, **not** a JSON-object District schema.

## History and evidence

- [Trac-Systems/ord-tap initial public commit, 19 September 2025](https://github.com/Trac-Systems/ord-tap/commit/3f3f851a00301b780e333fc9d8a3c3eaf29920e3) implements a shared content-type gate accepting `text/` or `application/json` (via `starts_with`) before its Bitmap District indexing call.
- [Bitmap claim parser in the same initial commit](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater/tap/ops/bitmap.rs) then examines the raw body for the exact decimal `<height>.bitmap` form. Thus an inscription *labelled* JSON can qualify, but a JSON object containing fields for a claim does not qualify through this exception.
- The date above is **the earliest verified public implementation snapshot of this behaviour**, not independently verified evidence that Trac first introduced it on that date. The original 2023 Trac Bitmap writer/production validation logic has not been established from this source.
- The later Trac-derived implementation retains `application/json` as an accepted MIME prefix while narrowing `text/` to `text/plain`.

## Clarifications

- A deliberately separate, default-off historical alternative to the [plain-text inscription](plain-text-inscription.md) requirement. Activating this exception must not silently disable the latter for ordinary plain-text claims.
- Source code uses a **string-prefix** test, not MIME parameter parsing; the independent historical compatibility option is recorded in [Literal MIME string-prefix compatibility](mime-string-prefix-compatibility.md).
- What “content” means for a District candidate carrying a delegate is **not yet agreed**. See [District content semantics decision](DISTRICT-CONTENT-OPEN-QUESTION.md). This MIME label exception does not choose own versus delegated content.
- This does **not** introduce an alternative JSON-object claim grammar: the body must still match the canonical plain District claim syntax.
- No Parcel, ownership, transfer, or staking semantics are implied.
