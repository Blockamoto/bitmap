# Unix timestamp ordering

**Code ID (provisional):** `precedence_unix_timestamp`  
**Default:** `0`  
**Introduced:** —

## Definition

Prefer the eligible claim whose reveal block has the lowest Unix timestamp; ties remain unresolved without an additional rule.

## History

The introduction date remains unverified. The creator recalls an early Unix-time precedence interpretation that preceded the July 2023 published lowest-inscription-number rule, but the current audit has not located a **dated publication or implementation** of it. Its placement immediately before the 14 July entry is **tentative historical ordering**, not proof of the chronology or the clock source used in a deployed 2023 writer.

## Evidence

No dated published winner-selection rule has yet been verified. Source audit pending.

## Clarifications

- This uses the Bitcoin **block header timestamp**, not an inscription-specific timestamp.
- Header times need not increase with block height.
- Claims within the same reveal block share a timestamp; a separate tiebreaker is needed to identify a unique winner, **or the profile must explicitly permit a tied winner set / no unique winner**. A single-winner registry profile must reject an incomplete time-only precedence configuration.
- The header `nTime` field is miner-chosen within Bitcoin's consensus constraints, not a guaranteed monotonic real-world clock. A timestamp option must specify this field explicitly and must not silently use a site's inscription display time.
