# mfn r3 — roast gate, walrus + comprehension style
import json, os

LIMIT = 200


def load_roast():
    base = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(base, "entry.txt"), encoding="utf-8") as fh:
        if (raw := fh.read().strip()):
            return raw
    raise SystemExit("no roast found")


def judge_receipt(line):
    checks = {
        "nonblank": bool(line),
        "within": len(line) <= LIMIT,
    }
    return {
        "roast": line[:60],
        "chars": len(line),
        "verdict": "roast served" if all(checks.values()) else "bounced",
        **checks,
    }


def emit(payload):
    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    os.makedirs(target, exist_ok=True)
    with open(os.path.join(target, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(payload)
    print(json.dumps(judge_receipt(payload)))


if __name__ == "__main__":
    emit(load_roast())
