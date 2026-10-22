# Bitcoin transaction ordering

**Code ID (provisional):** `precedence_bitcoin_reveal`  
**Standard:** `1`  
**Introduced:** 22 September 2023 (earliest verified public wording)

## Definition

Prefer the eligible claim in the earliest reveal block, then at the earliest Bitcoin transaction index.

## History

- **22 September 2023:** [Blockamoto Labs README commit `754d4d7`](https://github.com/blockamotolabs/ruleset/commit/754d4d7eda182de76ad543844e530c53426c855c) replaces “lowest inscription number of valid claims” with **“first valid inscription transaction on block”**. A [same-day update to the District file `b94efb8`](https://github.com/blockamotolabs/ruleset/commit/b94efb8f0982d7561a4582cfdb1937c2597cb63c) repeats the change.
- **28 September 2023:** Previously used as the documentary date in this registry. It is **superseded as earliest verified evidence** by the 22 September Git commit, not necessarily disproved as a later documentation milestone.
- **19 September 2025 public Rust snapshot:** [`ord-tap` Bitmap creator](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater/tap/ops/bitmap.rs#L24-L41) retains the first accepted `bm/<height>` record, but does not prove the unseen 2023 Trac writer used precisely the same iteration ordering.

## Evidence

- [22 September 2023 published source change](https://github.com/blockamotolabs/ruleset/commit/754d4d7eda182de76ad543844e530c53426c855c).
- This documents an **authored winner policy**; the 2023 Trac writer and actual competing-claim outcomes remain unverified.

## Clarifications

- This registry's **earliest reveal block, then earliest Bitcoin transaction index** is an explicit deterministic interpretation of the historical wording, not a verbatim quoted algorithm from the September 2023 document.
- Multiple inscriptions revealed in the same transaction still require a specified intra-transaction ordering rule; do not infer a unique winner from only the two fields.
- This historical alternative is distinct from lowest signed Ordinals inscription-number ordering and from Unix timestamp ordering.
