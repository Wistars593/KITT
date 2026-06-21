from __future__ import annotations

from kitt.can.frame import CanFrame
from kitt.core.events import DecodedEvent
from kitt.decoders.base import DecodeResult, SimpleFrameDecoder


def _synthetic_metadata(frame: CanFrame, signal_name: str) -> dict[str, object]:
    return {
        "bus": frame.bus,
        "arbitration_id": frame.arbitration_id_hex().lower(),
        "scaffolded": True,
        "signal_name": signal_name,
        "source_note": "Synthetic Phase 2 decoder scaffold inspired by donor research.",
    }


def _decode_synthetic_lock_state(frame: CanFrame) -> DecodeResult:
    if len(frame.data) < 1:
        return ()

    locked = bool(frame.data[0] & 0x01)
    return (
        DecodedEvent(
            source="w211.can_b.synthetic_ezs_a1",
            name="synthetic_lock_state",
            value="locked" if locked else "unlocked",
            confidence=0.5,
            metadata=_synthetic_metadata(frame, "synthetic_lock_state"),
        ),
    )


def _decode_synthetic_cabin_temperature(frame: CanFrame) -> DecodeResult:
    if len(frame.data) < 1:
        return ()

    celsius = round(frame.data[0] / 4.0, 2)
    return (
        DecodedEvent(
            source="w211.can_b.synthetic_dbe_a1",
            name="synthetic_cabin_temperature_c",
            value=celsius,
            confidence=0.4,
            metadata=_synthetic_metadata(frame, "synthetic_cabin_temperature_c"),
        ),
    )


CAN_B_DECODERS = (
    SimpleFrameDecoder(
        name="w211.can_b.synthetic_lock_state",
        supported_buses=("can-b-sim",),
        arbitration_ids=frozenset({0x0000}),
        decode_fn=_decode_synthetic_lock_state,
    ),
    SimpleFrameDecoder(
        name="w211.can_b.synthetic_cabin_temperature",
        supported_buses=("can-b-sim",),
        arbitration_ids=frozenset({0x0014}),
        decode_fn=_decode_synthetic_cabin_temperature,
    ),
)
