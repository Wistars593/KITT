from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, Iterator, TextIO

from kitt.can.frame import CanFrame


class CanLogFormatError(ValueError):
    """Raised when a JSONL CAN log contains malformed content."""


def _open_text_reader(path: Path | str) -> TextIO:
    return Path(path).open("r", encoding="utf-8")


def _open_text_writer(path: Path | str) -> TextIO:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    return target.open("w", encoding="utf-8", newline="\n")


def read_can_jsonl(path: Path | str) -> Iterator[CanFrame]:
    with _open_text_reader(path) as handle:
        for line_number, raw_line in enumerate(handle, start=1):
            line = raw_line.strip()
            if not line:
                continue

            try:
                record = json.loads(line)
            except json.JSONDecodeError as exc:
                raise CanLogFormatError(
                    f"line {line_number}: invalid JSON: {exc.msg}"
                ) from exc

            try:
                yield CanFrame.from_record(record)
            except (TypeError, ValueError) as exc:
                raise CanLogFormatError(f"line {line_number}: {exc}") from exc


def load_can_jsonl(path: Path | str) -> list[CanFrame]:
    return list(read_can_jsonl(path))


def write_can_jsonl(path: Path | str, frames: Iterable[CanFrame]) -> None:
    with _open_text_writer(path) as handle:
        for frame in frames:
            if not isinstance(frame, CanFrame):
                raise TypeError("write_can_jsonl expects CanFrame instances")
            handle.write(json.dumps(frame.to_record(), separators=(",", ":")))
            handle.write("\n")
