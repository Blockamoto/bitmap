# Trac District Indexer Audit

**Audit date:** 22 October 2026  
**Status:** In progress; reviewed one rule at a time  
**Scope:** Bitmap **District** inscription eligibility and winner selection only. Excludes Parcel, ownership, transfers, tapping, and staking.  
**Purpose:** Document the District rules actually implemented by Trac-related indexers, the evidence for each rule, and how the implementation changed over time. Extract candidate rules for the separate District Rule Registry. **This page is evidence, not itself a canonical Bitmap ruleset or a change to the registry.**

## Source identity and historical limitations

Trac has more than one relevant historical public artifact. Do **not** treat the later Rust implementation as proof of what the original 2023 production service enforced.

1. [BennyTheDev/trac-bitmap-public-endpoint](https://github.com/BennyTheDev/trac-bitmap-public-endpoint), created 20 July 2023. Public repository history and its README document Bitmap API access. The repository's current tree contains **README.md only**; no District validation/writer implementation is published there. It is evidence that public lookup functionality was described in 2023, **not** code evidence for a MIME or eligibility rule.
2. [Trac-Systems/ord-tap](https://github.com/Trac-Systems/ord-tap), a later published Rust implementation. Its first public commit is [`3f3f851`, 19 September 2025](https://github.com/Trac-Systems/ord-tap/commit/3f3f851a00301b780e333fc9d8a3c3eaf29920e3), with no parent in that repository. Its later changes can establish **implementation history from that initial public snapshot onward**, but cannot by themselves establish when a rule first appeared in Trac's original service.
3. Prior investigation is preserved in [the District-only Trac audit](../ruleset/District%20Rule%20Registry/TRAC-DISTRICT-AUDIT.md). This indexer page draws on that investigation while keeping the ruleset registry separate.

**Evidence convention:** For every extracted rule, record (a) exact code behaviour, (b) earliest *verified* version, (c) subsequent changes with commit links, (d) any earlier history not established, and (e) whether the rule is proposed for the registry, already represented there, or still unresolved. Distinguish a source commit's date from the actual historical date of introduction.

## 2023 Trac public API README audit

**Evidence type:** Public API documentation, **not** the original District writer implementation. [Repository: `BennyTheDev/trac-bitmap-public-endpoint`](https://github.com/BennyTheDev/trac-bitmap-public-endpoint). The repository's published tree contains `README.md` only. Its README history has 14 commits between 20 July and 11 August 2023. Checked the first revisions and the commits adding the relevant District getters.

**Dated document evidence (do not backdate these statements to the launch of Bitmap):**
- **20 July 2023:** [`a16243a`, first getter documentation](https://github.com/BennyTheDev/trac-bitmap-public-endpoint/commit/a16243aecba6382063081465be85e0d1298b0ee9) adds `inscribedBitmaps`. The previously checked revision [`a62e71e`](https://github.com/BennyTheDev/trac-bitmap-public-endpoint/commit/a62e71e3951d19ad6e7e2e0fa2cc7e0d5e9ff140) does **not** contain that getter. [Contemporaneous README](https://github.com/BennyTheDev/trac-bitmap-public-endpoint/blob/a16243aecba6382063081465be85e0d1298b0ee9/README.md).
- **22 July 2023:** [`2eebb54`](https://github.com/BennyTheDev/trac-bitmap-public-endpoint/commit/2eebb54f0bc3bca77adf7e692e9bb8e4edf050b) documents the single-height `bitmap` lookup.
- **2 August 2023:** [`4ebc421`](https://github.com/BennyTheDev/trac-bitmap-public-endpoint/commit/4ebc421103c028f43c799eb911cb29d7260c8d94) documents `bitmapBlock`, which resolves an inscription ID **or number** to a claimed block if that inscription is considered valid.
- **11 August 2023:** [Latest README revision `b0130f1`](https://github.com/BennyTheDev/trac-bitmap-public-endpoint/commit/b0130f1d66178da7f3e89c6db1a0244be6ea4d3c); used to check the full getter descriptions.

**District-relevant statements and their limits:**

| Document statement | What it establishes | What it does **not** establish |
| --- | --- | --- |
| `inscribedBitmaps` is a **post-inscription** lookup. For a queried block height it returns an inscription ID and number if already inscribed, or `null` if the state is unknown. | The public interface distinguished a recorded claim from an *unknown* state by 20 July 2023. | Whether an unrecorded candidate was invalid, unconfirmed, missed by an indexer, or simply not yet inscribed. Do **not** equate `null` with definitive invalidity or future eligibility. |
| The same getter says **pre-inscription validations** can occur client-side and are outside this tracker's scope. | A stated product/API boundary between querying recorded District claims and assessing hypothetical future claims. | The original writer's exact block-exists, MIME, schema, activation, or candidate eligibility policy. It does **not** establish that the writer allowed future block claims. |
| The `bitmap` getter returns an inscription ID and number when the District exists and is valid; `bitmapBlock` maps a valid inscription ID or number back to its block. | The API exposes an accepted District mapping and identifies a single returned claim per block through these getter descriptions. | **How** the winner is selected between multiple qualifying inscriptions. In particular, exposing inscription numbers does not prove lowest-inscription-number ordering. |
| The `ordinal` getter advertises base64 content, MIME type, block and timestamp fields; `latestBlock` reports the last known block. | Information exposed to consumers. | No MIME acceptance rule or timestamp-based priority rule can be inferred from the mere presence of those fields. |
| Getter rejects a nonnumeric input block value. | Request argument validation at the API boundary. | A District claim-body syntax rule; do not promote API error handling to an inscription-validity rule. |

**Proposed District registry extraction from this document:** **No new binary validity or winner-selection rule is established by the README alone.** Record the post-inscription/unknown-state distinction as evidence about the API, not a candidate ruleset switch. The single-result mapping suggests a useful *question* about winner-selection behaviour, but its precedence is undocumented. The source includes Parcel, ownership and staking getters; those remain **out of scope** for this District audit.

**Outstanding historical checks:** Seek the original 2023 writer code or dated snapshots and concrete competing District inscriptions whose Trac results can be verified. That evidence is required to decide whether the 2023 winner ordering, exact syntax, MIME, delegation, or other District eligibility decisions differ from the 2025–26 Rust port.

## Rule-by-rule audit

### TRAC-D01 — Text MIME family exception

**Implementation behaviour:**
- At the initial public Rust snapshot (19 September 2025), the intake guard accepted a declared content type if the byte/string representation began with `text/` **or** `application/json`. This is a string-prefix test, not a parsed MIME family test. District candidates still had to pass the separate body and block-height checks.
- The [25 September 2025 commit `acf6b7b`](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) narrowed the text branch to `starts_with("text/plain")` while keeping `application/json` as an alternative prefix. A malformed value such as `text/plainbogus` could match the latter text prefix; this is not the same as a standards-compliant media-type parser.

**Dated evidence:**
- **19 Sep 2025, earliest verified public code:** [initial Rust commit `3f3f851`](https://github.com/Trac-Systems/ord-tap/commit/3f3f851a00301b780e333fc9d8a3c3eaf29920e3) and [the intake source at that commit](https://github.com/Trac-Systems/ord-tap/blob/3f3f851a00301b780e333fc9d8a3c3eaf29920e3/src/index/updater/inscription_updater.rs#L984-L989) show `ct.starts_with("text/") || ct.starts_with("application/json")`.
- **25 Sep 2025, verified narrowing:** [commit `acf6b7b`](https://github.com/Trac-Systems/ord-tap/commit/acf6b7bbc7862e50999edd42c02ae170dfe23eea) explicitly replaces the `text/` test with `text/plain`. This commit also changed delegated-content resolution; that is a **separate rule** to audit later.
- **Before 19 Sep 2025:** The 2023 public API repository does not expose the original District writer or its MIME check. **Earliest public code observed is not proof of first introduction or 2023 production behaviour.**

**Extracted candidate registry rule:** *Text MIME Family Exception*, proposed default `0` (off). When enabled, allow otherwise valid canonical District claims with MIME labels beginning `text/`, rather than requiring only `text/plain`; exact prefix-matching versus parsed MIME semantics is an additional audit distinction. This is an alternative to the narrower baseline text MIME rule, not permission for arbitrary non-District bodies.

**Registry status:** Candidate already documented as [Text MIME family exception](../ruleset/District%20Rule%20Registry/text-mime-family-exception.md); **no registry edits or numbering made by this page**.

**Open history checks:** Find independently dated pre-September-2025 Trac writer, archived source, deployment evidence, or test fixtures that establish whether `text/*` was accepted earlier. In their absence, keep the historical introduction **unknown**. Also isolate malformed MIME-prefix behaviour as a possible separate compatibility switch if indexer outcomes demonstrably differ.

## Next checkpoint

Continue with the next **District** rule from the Trac code, verify its commit history, and append findings here. Do not move to another indexer or to Parcel rules until Trac District is complete.
