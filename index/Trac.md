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
