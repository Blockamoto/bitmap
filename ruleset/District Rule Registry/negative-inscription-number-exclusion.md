# Negative

**Code ID:** `negative`  
**Previous draft ID:** `negative_inscription_number_exclusion`  
**Standard:** `0`  
**Predicate:** The claimant's signed Ordinals inscription number is less than zero.

## Definition

When enabled, reject a claimant if `inscription_number < 0`. When disabled, a negative number is not itself an additional veto. Neither setting bypasses the other District rules.

The number must be derived under the recorded Ord/indexer version. A missing number is unknown, not zero or an implicit non-negative value.

## Why the name is not `cursed`

The evidenced check is signed-number comparison, not a general test of every historical curse cause, reinscription flag, unbound status or vindication status. Keep the name aligned with the actual predicate. A positive-numbered vindicated inscription is not rejected by this bit solely because its envelope has a property that formerly caused a curse.

A body `-1.bitmap` is a separate matter: it already fails canonical District syntax. This rule tests the inscription's assigned number, not its claimed Bitcoin height.

## Independent of `number`

[`number`](number.md) ranks eligible claims. `negative` determines whether a class of claims reaches that ranking at all. Enabling one must not silently enable the other. The same negative-number veto can be combined with Bitcoin reveal [`order`](order.md).

## Evidence

- [Trac-derived change `12ddc36`, 19 May 2026](https://github.com/Trac-Systems/ord-tap/commit/12ddc36ccfa7655a2bbec20d0245deecdec0ec55) adds the negative-inscription-number guard to the District creation path. The [inspected implementation](https://github.com/Trac-Systems/ord-tap/blob/b8f6ea35cf6b9d405d4db7c58555e3c8ab33e8cd/src/index/updater/inscription_updater/tap/ops/bitmap.rs#L4-L42) begins with that guard before reading the body.
- [OPI reader at `7933f5d0`](https://github.com/bestinslot-xyz/OPI/blob/7933f5d05d978fc226df8126026ed92f8c45d03b/ord/db_reader/src/server.rs#L309-L325) also rejects negative inscription numbers in `is_valid_bitmap`.
- The Trac code-change date is **not** a universal first-introduction date, and neither public snapshot proves a particular marketplace's deployed version.

The current default remains `0`. Keeping this comparison bit does not settle a new Standard exclusion, nor add a blanket reinscription or unbound-inscription ban.

[Registry](README.md) · [Audit report](SIX-RULE-AUDIT.md).
