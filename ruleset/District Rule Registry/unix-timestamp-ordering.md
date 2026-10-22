# Unix timestamp ordering

**Default:** `0`  
**Introduced:** —

## Definition

Prefer the eligible claim whose reveal block has the lowest Unix timestamp; ties remain unresolved without an additional rule.

## History

The introduction date remains unverified.

## Evidence

No dated published winner-selection rule has yet been verified. Source audit pending.

## Clarifications

- This uses the Bitcoin **block header timestamp**, not an inscription-specific timestamp.
- Header times need not increase with block height.
- Claims within the same reveal block share a timestamp; a separate tiebreaker is needed to identify a unique winner.
