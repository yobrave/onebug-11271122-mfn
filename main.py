"""r44 mfn entry shift: roast line mover with cap 200."""

import json
import os
from pathlib import Path

SLUG = "u-mfnakmal-roast-your-own-agent-2d221bda"
RANGE_END = 200


def load():
    return (Path(__file__).resolve().parent / "entry.txt").read_text(encoding="utf-8").strip()


def gate(text):
    return [tag for tag, bad in (("empty", not text), ("over", len(text) > RANGE_END)) if bad]


def shift():
    text = load()
    flags = gate(text)
    moved_to = ""
    if not flags:
        moved_to = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
        moved_to.mkdir(parents=True, exist_ok=True)
        (moved_to / "entry.txt").write_text(text + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({"flags": flags, "moved_to": str(moved_to), "chars_now": len(text), "slug": SLUG}))
    if flags:
        raise SystemExit(2)


shift()

STAMP = "r44-mfn"
print(json.dumps({"stamp": STAMP, "final": True}))
