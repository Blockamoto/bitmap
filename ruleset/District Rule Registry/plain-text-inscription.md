# Plain-text inscription (`text/plain`)

**Code ID (provisional):** `text`  
**Standard:** `1`  
**Introduced:** 3 June 2023

## Definition

Require MIME media type `text/plain`, allowing parameters such as `charset=utf-8`.

## History

- **3 June 2023:** The GitBook instructions direct users to enter the claim in UniSat's text field; the search guide uses its TEXT category.

## Evidence

- [3 June GitBook revision](https://gitbook.bitmap.land/~/revisions/AZO0a8slhI90dZCq0SNg/)
- [UniSat inscription guide](https://github.com/unisat-wallet/unisat-dev-docs/blob/master/open-api/inscribe-guide.md) provides examples using `text/plain;charset=utf-8`.

## Clarifications

- The `text/plain` requirement is **inferred from the documented text-inscription workflow**; the early GitBook does not explicitly state that other MIME types are invalid.
- MIME parameters such as `charset=utf-8` do not change the `text/plain` media type.

- MIME eligibility is separate from the decoder: [`mime_charset`](mime-charset-decoding.md) respects a declared charset for `text/plain` and uses its MIME US-ASCII fallback when absent; [`raw_utf8_strict`](raw-utf8-strict-decoding.md) ignores the declared charset for decoding. Neither decoder mode turns this MIME rule on or off.
