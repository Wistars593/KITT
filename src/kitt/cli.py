from __future__ import annotations

import argparse
import sys
from pathlib import Path

from kitt.can.jsonl import CanLogFormatError, load_can_jsonl


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="kitt-can-validate")
    parser.add_argument("path", help="Path to a JSONL CAN log")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    path = Path(args.path)

    try:
        frames = load_can_jsonl(path)
    except (OSError, CanLogFormatError, TypeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    buses = sorted({frame.bus for frame in frames})
    first_timestamp = frames[0].timestamp.isoformat().replace("+00:00", "Z") if frames else "n/a"
    last_timestamp = frames[-1].timestamp.isoformat().replace("+00:00", "Z") if frames else "n/a"

    print(f"Validated CAN log: {path}")
    print(f"Frame count: {len(frames)}")
    print(f"Buses seen: {', '.join(buses) if buses else 'n/a'}")
    print(f"First timestamp: {first_timestamp}")
    print(f"Last timestamp: {last_timestamp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
