# mfn roast runner r47 — procedural steps
import json
import os
import zlib
from pathlib import Path

ROOF = 200


def load_stage():
    base = Path(__file__).resolve().parent
    return (base / "entry.txt").read_bytes()


def vet(raw):
    text = raw.decode("utf-8")
    if len(text) > ROOF:
        raise SystemExit("over the roof")
    if text.strip() != text:
        raise SystemExit("untidy roast edges")
    return text


def emit(text):
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "stage"
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "wb") as fh:
        fh.write(text.encode("utf-8"))
    return {"stamp": format(zlib.crc32(text.encode("utf-8")), "08x"), "wrote": folder, "chars": len(text)}


if __name__ == "__main__":
    print(json.dumps(emit(vet(load_stage())), ensure_ascii=True))
