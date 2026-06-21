from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Protocol, runtime_checkable

from kitt.can.frame import CanFrame
from kitt.core.events import DecodedEvent

DecodeResult = tuple[DecodedEvent, ...]
DecodeFn = Callable[[CanFrame], DecodeResult]


@runtime_checkable
class FrameDecoder(Protocol):
    """Pure, deterministic decoder contract."""

    name: str
    supported_buses: tuple[str, ...]

    def handles(self, frame: CanFrame) -> bool:
        """Return whether this decoder can interpret the frame."""

    def decode(self, frame: CanFrame) -> DecodeResult:
        """Decode a frame without side effects."""


@dataclass(frozen=True, slots=True)
class SimpleFrameDecoder:
    """Small immutable decoder wrapper for scaffolded decoders."""

    name: str
    supported_buses: tuple[str, ...]
    arbitration_ids: frozenset[int]
    decode_fn: DecodeFn

    def handles(self, frame: CanFrame) -> bool:
        return (
            frame.bus in self.supported_buses
            and frame.arbitration_id in self.arbitration_ids
        )

    def decode(self, frame: CanFrame) -> DecodeResult:
        if not self.handles(frame):
            return ()
        return self.decode_fn(frame)
