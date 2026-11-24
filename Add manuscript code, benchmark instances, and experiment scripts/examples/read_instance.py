"""Read a released input instance; no route optimization is performed."""
import argparse
import csv
import hashlib
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load_instance(name):
    with (ROOT / "data/instance_catalog.csv").open(encoding="utf-8-sig", newline="") as f:
        entries = list(csv.DictReader(f))
    matches = [r for r in entries if r["instance"] == name]
    if len(matches) != 1:
        raise ValueError("Choose one of: " + ", ".join(r["instance"] for r in entries))
    meta = matches[0]
    path = ROOT / meta["file"]
    if hashlib.sha256(path.read_bytes()).hexdigest() != meta["sha256"]:
        raise ValueError("Coordinate-file checksum does not match the catalogue")
    with path.open(encoding="utf-8-sig", newline="") as f:
        targets = [dict(target_id=int(r["target_id"]), x_km=float(r["x_km"]),
                        y_km=float(r["y_km"]), monitoring_minutes=float(r["monitoring_minutes"]))
                   for r in csv.DictReader(f)]
    if [r["target_id"] for r in targets] != list(range(1, int(meta["targets"]) + 1)):
        raise ValueError("Unexpected target identifiers or target count")
    if any(not math.isfinite(r[k]) for r in targets for k in ("x_km", "y_km", "monitoring_minutes")):
        raise ValueError("A coordinate or duration is not finite")
    if any(r["monitoring_minutes"] < 0 for r in targets):
        raise ValueError("Monitoring durations must be nonnegative")
    return meta, targets

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("instance", nargs="?", default="36_4_16")
    args = parser.parse_args()
    meta, targets = load_instance(args.instance)
    print("Instance:", meta["instance"])
    print("Targets:", len(targets))
    print("Available vessels:", meta["available_vessels"])
    print("Task groups:", meta["task_groups"])
    print("Port (km):", (float(meta["port_x_km"]), float(meta["port_y_km"])))
    print("Input format and checksum verified.")

if __name__ == "__main__":
    main()
