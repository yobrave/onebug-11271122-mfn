# mfn roast pipeline r45 — datetime flavored style
import datetime as dt
import json
import os
from pathlib import Path

ROOT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
SOURCE = Path(__file__).resolve().parent / "entry.txt"


def stage() -> str:
    ROOT.mkdir(parents=True, exist_ok=True)
    material = SOURCE.read_text(encoding="utf-8")
    (ROOT / "entry.txt").write_text(material, encoding="utf-8")
    return material


if __name__ == "__main__":
    material = stage()
    tag = dt.datetime.now(dt.timezone.utc).strftime("mfn%jT%H%M%S")
    print(json.dumps({"stamp": tag, "chars": len(material), "root": str(ROOT)}))
