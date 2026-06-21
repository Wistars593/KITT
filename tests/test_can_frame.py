from datetime import UTC, datetime

import pytest

from kitt.can.frame import CanFrame


def test_can_frame_accepts_standard_frame() -> None:
    frame = CanFrame(
        timestamp=datetime(2026, 6, 21, 12, 0, tzinfo=UTC),
        bus="can-b-sim",
        arbitration_id=0x123,
        data=b"\x01\x02",
    )

    assert frame.data_hex() == "0102"
    assert frame.arbitration_id_hex() == "0x123"


def test_can_frame_rejects_standard_id_out_of_range() -> None:
    with pytest.raises(ValueError, match="standard CAN arbitration_id"):
        CanFrame(
            timestamp=datetime(2026, 6, 21, 12, 0, tzinfo=UTC),
            bus="can-b-sim",
            arbitration_id=0x800,
            data=b"\x00",
        )


def test_can_frame_rejects_too_much_data() -> None:
    with pytest.raises(ValueError, match="8 bytes or fewer"):
        CanFrame(
            timestamp=datetime(2026, 6, 21, 12, 0, tzinfo=UTC),
            bus="can-b-sim",
            arbitration_id=0x123,
            data=b"\x00" * 9,
        )


def test_can_frame_rejects_non_bytes_like_data() -> None:
    with pytest.raises(TypeError, match="bytes-like"):
        CanFrame(
            timestamp=datetime(2026, 6, 21, 12, 0, tzinfo=UTC),
            bus="can-b-sim",
            arbitration_id=0x123,
            data="0102",  # type: ignore[arg-type]
        )


def test_can_frame_from_record_supports_extended_ids() -> None:
    frame = CanFrame.from_record(
        {
            "timestamp": "2026-06-21T12:00:00Z",
            "bus": "can-c-sim",
            "arbitration_id": "0x18FF50E5",
            "data": "01020304",
            "is_extended_id": True,
        }
    )

    assert frame.is_extended_id is True
    assert frame.arbitration_id == 0x18FF50E5
