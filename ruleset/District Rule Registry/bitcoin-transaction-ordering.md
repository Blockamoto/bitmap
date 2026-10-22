# Bitcoin transaction ordering

**Default:** `1`  
**Introduced:** 28 September 2023

## Definition

Prefer the eligible claim in the earliest reveal block, then at the earliest Bitcoin transaction index.

## History

- **28 September 2023:** The District claim winner was specified by Bitcoin block and transaction order instead of Ordinals inscription number.

## Evidence

Primary source and precise wording to be attached during the historical audit.

## Clarifications

- Bitcoin block height and transaction index establish a chain-based order.
- Multiple inscriptions revealed in the same transaction still require a specified intra-transaction ordering rule.
