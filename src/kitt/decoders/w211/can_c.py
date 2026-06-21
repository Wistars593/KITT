from __future__ import annotations

from kitt.can.frame import CanFrame
from kitt.core.events import DecodedEvent
from kitt.decoders.base import DecodeResult, SimpleFrameDecoder


def _decode_synthetic_chassis_awake(frame: CanFrame) -> DecodeResult:
    if len(frame.data) < 1:
        return ()

    return (
        DecodedEvent(
            source="w211.can_c.synthetic_chassis_status",
            name="synthetic_chassis_awake",
            value=bool(frame.data[0] & 0x01),
            confidence=0.25,
            metadata={
                "bus": frame.bus,
                "arbitration_id": frame.arbitration_id_hex().lower(),
                "scaffolded": True,
                "source_note": "Synthetic Phase 2 decoder scaffold for CAN C routing only.",
            },
        ),
    )


CAN_C_DECODERS = (
    SimpleFrameDecoder(
        name="w211.can_c.synthetic_chassis_awake",
        supported_buses=("can-c-sim",),
        arbitration_ids=frozenset({0x0200}),
        decode_fn=_decode_synthetic_chassis_awake,
    ),
)
