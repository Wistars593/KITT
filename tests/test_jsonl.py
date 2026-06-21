from datetime import UTC, datetime

import pytest

from kitt.can.frame import CanFrame
from kitt.can.jsonl import CanLogFormatError, load_can_jsonl, write_can_jsonl


def test_jsonl_roundtrip(tmp_path) -> None:
    path = tmp_path / "roundtrip.jsonl"
    frames = [
        CanFrame(
            timestamp=datetime(2026, 6, 21, 12, 0, tzinfo=UTC),
            bus="can-b-sim",
            arbitration_id=0x123,
            data=b"\x01\x02",
        ),
        CanFrame(
            timestamp=datetime(2026, 6, 21, 12, 0, 1, tzinfo=UTC),
            bus="can-c-sim",
            arbitration_id=0x18FF50E5,
            data=b"\xAA\x55",
            is_extended_id=True,
        ),
    ]

    write_can_jsonl(path, frames)
    assert load_can_jsonl(path) == frames


def test_jsonl_reports_line_numbers_for_invalid_records(tmp_path) -> None:
    path = tmp_path / "invalid.jsonl"
    path.write_text(
        '{"timestamp":"2026-06-21T12:00:00Z","bus":"can-b-sim","arbitration_id":"0x123","data":"01","is_extended_id":false}\n'
        '{"timestamp":"2026-06-21T12:00:01Z","bus":"","arbitration_id":"0x124","data":"02","is_extended_id":false}\n',
        encoding="utf-8",
    )

    with pytest.raises(CanLogFormatError, match=r"line 2: .*bus must be a non-empty string"):
        load_can_jsonl(path)


def test_jsonl_reports_invalid_json(tmp_path) -> None:
    path = tmp_path / "broken.jsonl"
    path.write_text("{not-json}\n", encoding="utf-8")

    with pytest.raises(CanLogFormatError, match=r"line 1: invalid JSON"):
        load_can_jsonl(path)
