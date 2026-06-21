from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Any


def _coerce_timestamp(value: datetime | str) -> datetime:
    if isinstance(value, datetime):
        timestamp = value
    elif isinstance(value, str):
        normalized = value.replace("Z", "+00:00")
        try:
            timestamp = datetime.fromisoformat(normalized)
        except ValueError as exc:
            raise ValueError(f"invalid timestamp: {value!r}") from exc
    else:
        raise TypeError("timestamp must be a datetime or ISO-8601 string")

    if timestamp.tzinfo is None:
        raise ValueError("timestamp must be timezone-aware")

    return timestamp.astimezone(UTC)


def _coerce_data(value: bytes | bytearray | memoryview) -> bytes:
    if not isinstance(value, (bytes, bytearray, memoryview)):
        raise TypeError("data must be bytes-like")

    payload = bytes(value)
    if len(payload) > 8:
        raise ValueError("classic CAN data length must be 8 bytes or fewer")
    return payload


@dataclass(frozen=True, slots=True)
class CanFrame:
    """Immutable classic CAN frame used for simulation and replay only."""

    timestamp: datetime
    bus: str
    arbitration_id: int
    data: bytes
    is_extended_id: bool = False

    def __post_init__(self) -> None:
        timestamp = _coerce_timestamp(self.timestamp)
        payload = _coerce_data(self.data)

        if not isinstance(self.bus, str) or not self.bus.strip():
            raise ValueError("bus must be a non-empty string")

        if not isinstance(self.arbitration_id, int):
            raise TypeError("arbitration_id must be an integer")
        if self.arbitration_id < 0:
            raise ValueError("arbitration_id must be non-negative")

        max_id = 0x1FFFFFFF if self.is_extended_id else 0x7FF
        id_kind = "extended" if self.is_extended_id else "standard"
        if self.arbitration_id > max_id:
            raise ValueError(
                f"{id_kind} CAN arbitration_id must be within 0x000 and 0x{max_id:X}"
            )

        object.__setattr__(self, "timestamp", timestamp)
        object.__setattr__(self, "bus", self.bus.strip())
        object.__setattr__(self, "data", payload)

    def data_hex(self) -> str:
        return self.data.hex()

    def arbitration_id_hex(self) -> str:
        width = 8 if self.is_extended_id else 3
        return f"0x{self.arbitration_id:0{width}X}"

    def to_record(self) -> dict[str, Any]:
        return {
            "timestamp": self.timestamp.isoformat().replace("+00:00", "Z"),
            "bus": self.bus,
            "arbitration_id": self.arbitration_id_hex().lower(),
            "data": self.data_hex(),
            "is_extended_id": self.is_extended_id,
        }

    @classmethod
    def from_record(cls, record: dict[str, Any]) -> "CanFrame":
        if not isinstance(record, dict):
            raise TypeError("record must be a mapping")

        missing = {
            "timestamp",
            "bus",
            "arbitration_id",
            "data",
            "is_extended_id",
        } - set(record)
        if missing:
            missing_names = ", ".join(sorted(missing))
            raise ValueError(f"missing required field(s): {missing_names}")

        arbitration_id_raw = record["arbitration_id"]
        if isinstance(arbitration_id_raw, int):
            arbitration_id = arbitration_id_raw
        elif isinstance(arbitration_id_raw, str):
            try:
                arbitration_id = int(arbitration_id_raw, 16)
            except ValueError as exc:
                raise ValueError(
                    f"invalid arbitration_id hex string: {arbitration_id_raw!r}"
                ) from exc
        else:
            raise TypeError("arbitration_id must be an int or hex string")

        data_raw = record["data"]
        if not isinstance(data_raw, str):
            raise TypeError("data must be a hex string")
        try:
            payload = bytes.fromhex(data_raw)
        except ValueError as exc:
            raise ValueError(f"invalid data hex string: {data_raw!r}") from exc

        is_extended_id = record["is_extended_id"]
        if not isinstance(is_extended_id, bool):
            raise TypeError("is_extended_id must be a boolean")

        return cls(
            timestamp=record["timestamp"],
            bus=record["bus"],
            arbitration_id=arbitration_id,
            data=payload,
            is_extended_id=is_extended_id,
        )
