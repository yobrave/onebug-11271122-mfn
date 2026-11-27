# mfn self-roast auditor - u-mfnakmal-roast-your-own-agent-2d221bda
# round 1127-1122: carry the roast line to the scoring tray, audited.
import json, os, pathlib, sys

AUDIT_CAP = 200
DESK = pathlib.Path(__file__).resolve().parent
TRAY_NAME = "entry.txt"


def fetch():
    return (DESK / TRAY_NAME).read_text(encoding="utf-8").strip()


def audit(roast):
    reasons = []
    if not roast:
        reasons.append("no roast on file")
    if len(roast) > AUDIT_CAP:
        reasons.append("roast runs %d, cap %d" % (len(roast), AUDIT_CAP))
    return reasons


def carry(roast):
    tray = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    tray.mkdir(parents=True, exist_ok=True)
    slot = tray / TRAY_NAME
    slot.write_text(roast + "\n", encoding="utf-8", newline="\n")
    return slot


def main():
    roast = fetch()
    reasons = audit(roast)
    if reasons:
        print(json.dumps({"ok": False, "reasons": reasons}))
        return 1
    slot = carry(roast)
    print(json.dumps({"ok": True, "roast_chars": len(roast), "slot": str(slot),
                      "bounty": "u-mfnakmal-roast-your-own-agent-2d221bda",
                      "kind": "self roast", "round": "1127-1122",
                      "audited": True}))
    return 0


sys.exit(main())
