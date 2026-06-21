from __future__ import annotations

from kitt.can.frame import CanFrame
from kitt.core.events import DecodedEvent
from kitt.decoders.base import DecodeResult, SimpleFrameDecoder


def _decode_synthetic_diagnostic_service(frame: CanFrame) -> DecodeResult:
    if len(frame.data) < 3:
        return ()

    service = "tester_present" if frame.data[:3] == b"\x02\x3e\x02" else "unknown_service"
    return (
        DecodedEvent(
            source="w211.can_d.synthetic_kwp_request",
            name="synthetic_diagnostic_service",
            value=service,
            confidence=0.3,
            metadata={
                "bus": frame.bus,
                "arbitration_id": frame.arbitration_id_hex().lower(),
                "scaffolded": True,
                "source_note": "Synthetic Phase 2 decoder scaffold inspired by diagnostic request IDs.",
            },
        ),
    )


CAN_D_DECODERS = (
    SimpleFrameDecoder(
        name="w211.can_d.synthetic_diagnostic_service",
        supported_buses=("can-d-sim",),
        arbitration_ids=frozenset({0x001C}),
        decode_fn=_decode_synthetic_diagnostic_service,
    ),
)
