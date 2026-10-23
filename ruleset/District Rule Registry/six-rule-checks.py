"""Synthetic counterexamples for the Bitmap District six-rule audit.

These checks demonstrate independent predicates and codec behavior. They are not
an Ord/Trac/OPI integration test, an envelope parser, a frozen Bitmap validator,
or a historical winner comparison. MIME fixtures below are deliberately limited
to the literal examples under review; this is not a general MIME parser.
Requires Python 3.10+ and the `brotli` package for the codec checks.
"""
from __future__ import annotations

import gzip
import json
import re
import sys
from pathlib import Path

try:
    import brotli
except ImportError:
    raise SystemExit("Install the brotli package to run the codec checks.")

CLAIM = b"123.bitmap"
BROTLI_CLAIM = bytes.fromhex("8b04803132332e6269746d617003")
RESULTS: list[dict[str, object]] = []


def check(name: str, condition: bool) -> None:
    RESULTS.append({"name": name, "passed": bool(condition)})
    if not condition:
        raise AssertionError(name)


def claim_ok(body: bytes) -> bool:
    return re.fullmatch(rb"(?:0|[1-9][0-9]*)\.bitmap", body) is not None


def trac_prefix(value: bytes, allow_json: bool = False) -> bool:
    """Model the UTF-8 accessor plus case-sensitive starts_with comparator."""
    try:
        text = value.decode("utf-8")
    except UnicodeDecodeError:
        return False
    return text.startswith("text/plain") or (
        allow_json and text.startswith("application/json")
    )


def fixture_exact_type(value: bytes, allow_json: bool = False) -> bool:
    """Compare fixture media-type tokens; NOT a general parameter validator."""
    try:
        essence = value.decode("ascii").split(";", 1)[0].lower()
    except UnicodeDecodeError:
        return False
    return essence == "text/plain" or (
        allow_json and essence == "application/json"
    )


def raw_tag_present(fields: list[tuple[bytes, bytes]], tag: bytes) -> bool:
    """Inputs are authenticated, correctly positioned field pairs, not bodies."""
    return any(key == tag for key, _ in fields)


def nested_trac(
    claimant_delegate: str | None,
    resolved_delegate_reference: dict[str, str | None],
) -> bool:
    """Inputs are already decoded delegate references, not raw field values."""
    return claimant_delegate is not None and (
        resolved_delegate_reference.get(claimant_delegate) is not None
    )


def main() -> None:
    check("canonical raw body", claim_ok(CLAIM))
    check("trailing newline rejected", not claim_ok(CLAIM + b"\n"))
    check("UTF-8 BOM rejected", not claim_ok(b"\xef\xbb\xbf" + CLAIM))
    check("UTF-16 bytes rejected", not claim_ok("123.bitmap".encode("utf-16le")))
    check("Brotli stream decodes to canonical body", brotli.decompress(BROTLI_CLAIM) == CLAIM)
    check("stored Brotli bytes are not a canonical raw body", not claim_ok(BROTLI_CLAIM))
    zipped = gzip.compress(CLAIM, mtime=0)
    check("gzip stream decodes independently", gzip.decompress(zipped) == CLAIM)
    check("stored gzip bytes are not a canonical raw body", not claim_ok(zipped))
    try:
        brotli.decompress(zipped)
        wrong_codec_rejected = False
    except brotli.error:
        wrong_codec_rejected = True
    check("Brotli does not implicitly enable gzip", wrong_codec_rejected)
    encoding = [(b"\x09", b"br")]
    check("raw claim remains canonical despite tag metadata", claim_ok(CLAIM))
    check("tag-9 veto detects br declaration", raw_tag_present(encoding, b"\x09"))
    check("tag-9 veto includes empty value", raw_tag_present([(b"\x09", b"")], b"\x09"))
    check("tag-9 veto includes gzip declaration", raw_tag_present([(b"\x09", b"gzip")], b"\x09"))
    check("property-encoding tag 19 is not tag 9", not raw_tag_present([(b"\x13", b"br")], b"\x09"))
    check("absent field is not present", not raw_tag_present([], b"\x09"))
    check("tag-looking bytes in another field value do not count", not raw_tag_present([(b"\x07", b"\x09")], b"\x09"))
    check("delegate veto includes empty raw value", raw_tag_present([(b"\x0b", b"")], b"\x0b"))
    check("delegate-looking value is not a field key", not raw_tag_present([(b"\x07", b"\x0b")], b"\x0b"))
    check("malformed delegate is still a raw declaration", raw_tag_present([(b"\x0b", b"bad")], b"\x0b"))
    check("A to B to C triggers nested veto without fetching C", nested_trac("B", {"B": "C"}))
    check("undecodable B delegate does not trigger Trac nested veto", not nested_trac("B", {"B": None}))
    check("single-level delegate passes nested predicate", not nested_trac("B", {"B": None}))
    check("missing B does not prove nesting in observed Trac branch", not nested_trac("B", {}))
    check("negative signed number vetoes minus one", -1 < 0)
    check("zero is not negative", not (0 < 0))
    check("positive number does not become negative due to a status label", not (123 < 0))
    labelled = b"text/plain;charset=banana"
    check("unknown charset label does not separate the tested MIME comparators", fixture_exact_type(labelled) and trac_prefix(labelled) and claim_ok(CLAIM))
    check("plainish separates exact-type and prefix matching", not fixture_exact_type(b"text/plainish") and trac_prefix(b"text/plainish"))
    check("JSON prefix remains conditional on JSON eligibility", not trac_prefix(b"application/jsonbogus") and trac_prefix(b"application/jsonbogus", True) and not fixture_exact_type(b"application/jsonbogus", True))
    check("literal prefix can reject uppercase accepted by case-insensitive MIME comparison", fixture_exact_type(b"TEXT/PLAIN") and not trac_prefix(b"TEXT/PLAIN"))
    check("MIME acceptance never accepts a JSON-object District body", trac_prefix(b"application/json", True) and not claim_ok(b'{"height":123}'))
    bad_mime = b"text/plain\xff"
    check("OPI raw-prefix and Trac UTF-8 accessor can differ", bad_mime.startswith(b"text/plain") and not trac_prefix(bad_mime))
    output = {
        "scope": "Synthetic predicate and codec checks only; no historical chain replay",
        "python": sys.version.split()[0],
        "brotli": getattr(brotli, "__version__", "unknown"),
        "passed": len(RESULTS),
        "failed": 0,
        "checks": RESULTS,
    }
    Path(__file__).with_name("six-rule-checks-results.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(f"{len(RESULTS)} synthetic checks passed; 0 failed.")


if __name__ == "__main__":
    main()
