# Nested delegate exclusion for District claims

**Default:** `0`  
**Introduced:** 19 September 2025

## Definition

When enabled, reject a District candidate whose inscription contains a delegation reference to another inscription that **itself** has a delegation reference. The referenced delegate is checked for nesting; a two-or-more-hop delegation chain is not followed as a District claim.

## History and evidence

- [Initial public `ord-tap` revision, 19 September 2025](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater.rs) checks `payload.delegate()`, obtains the referenced inscription, tests `insc.delegate().is_some()`, and returns on nested delegation **in the post-TAP-start path**. In that revision, the pre-TAP-start District path does not apply the nested guard.
- [25 September 2025 parity update](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) moves one-level delegate resolution and the nested guard before both District indexing paths.
- The introduced date here marks first verified public indexer code, **not** independently verified inception of this policy in the original 2023 Trac writer.

## Clarifications

- This veto is logically separate from [single-level delegate content resolution](delegate-content-resolution.md). An indexer may permit first-level delegates while rejecting nested ones.
- It **presupposes that delegate-tagged inscriptions are eligible in the first place**, which is not yet settled for the Bitmap Standard. See the [open District content and delegation question](DISTRICT-CONTENT-OPEN-QUESTION.md). “Undelegated content” as a body source is not, by itself, an all-delegates veto.
- The September 2025 early gate placement affects which reveal heights actually encountered the check.
- If a referenced inscription cannot be found, the code does not treat that absence as proof of nesting; unresolved delegation is a separate edge case.
- District claim recognition only. Parcel parent/child references and asset transfers are unrelated.
