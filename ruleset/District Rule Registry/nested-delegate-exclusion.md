# Nested

**Code ID:** `nested`  
**Previous draft ID:** `nested_delegate_exclusion`  
**Standard:** `0`  
**Evidence:** Trac-derived public Rust implementation; first verified snapshot 19 September 2025, not proven original 2023 inception.

## Definition

When enabled, reject claimant A when A has a **decodable delegate reference** to B, B resolves to an inscription, and **B itself has a decodable delegate reference**.

In the audited Rust code the predicate is `payload.delegate()` followed by fetching B and testing `B.delegate().is_some()`. The destination C of B's reference need not be fetched or exist for that predicate to be true. This is a veto on a nested reference, not an instruction to follow it.

When disabled, this particular nested-reference condition does not veto A. It does not enable recursive resolution or override any other eligibility rule.

## Important boundary corrections

The earlier wording, "the delegate declares a delegate", was too broad to reproduce the evidenced code exactly. **A raw tag 11 with an undecodable value on B does not make `B.delegate().is_some()` true.** That differs from the raw-presence predicate in [`delegate`](delegate-tag-exclusion.md).

If A has no decodable reference, this predicate does not trigger. In the inspected Trac branch, a missing B or lookup error is treated as no detected nesting. That is an observed implementation behavior, not permission for a deterministic validator to mistake unavailable local data for proven on-chain absence. The replay snapshot, same-block availability and error policy must be pinned before claiming complete Trac reproduction.

The rule can veto A under either `body` or `content`: Trac checks nesting before passing the selected payload to its District parser. It is not dependent on which body's text eventually matches.

## Distinct from normal Ord resolution

[Ord 0.29.1's content handler](https://github.com/ordinals/ord/blob/d2ff0a789033e3d784048a23e856f15c54e88806/src/subcommand/server/r.rs#L250-L279) substitutes B once and does not inspect B's delegate to impose this veto. Thus A can resolve to B's own canonical body under one-hop content semantics while `nested=1` separately rejects A. Not following a second hop is not the same as rejecting a first-hop target that contains another reference.

[`delegate=1`](delegate-tag-exclusion.md) rejects all claimant tag-11 declarations and therefore already rejects every case caught by `nested`. That conditional redundancy does not justify merging the bits: with `delegate=0`, a profile can permit ordinary delegates while rejecting only nested ones. [`fallback`](fallback.md) concerns a failed content lookup, not this veto.

## History and implementation evidence

- [19 September 2025 snapshot](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater.rs): nested checking is in the post-TAP-start path; the earlier-height Bitmap path bypasses it.
- [25 September 2025 change](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea): moves delegate resolution and the nested check before both Bitmap paths.
- [Pinned inspected implementation `b8f6ea35`](https://github.com/Trac-Systems/ord-tap/blob/b8f6ea35cf6b9d405d4db7c58555e3c8ab33e8cd/src/index/updater/inscription_updater.rs#L1245-L1320): explicitly tests a decoded reference on B, returns on nesting, and separately selects an effective payload.

Those publication dates do not establish the original 2023 service's policy or deployment dates. Historical activation/coverage remains implementation evidence, not an additional hidden rule in this ID.

[Registry](README.md) · [Audit report](SIX-RULE-AUDIT.md).
