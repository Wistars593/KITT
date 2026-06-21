from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass

from kitt.can.frame import CanFrame
from kitt.decoders.base import DecodeResult, FrameDecoder


@dataclass(frozen=True, slots=True)
class DecoderRegistry:
    """Immutable registry for pure frame decoders."""

    decoders: tuple[FrameDecoder, ...] = ()

    def with_decoder(self, decoder: FrameDecoder) -> "DecoderRegistry":
        if not isinstance(decoder, FrameDecoder):
            raise TypeError("decoder must implement the FrameDecoder protocol")
        return DecoderRegistry(self.decoders + (decoder,))

    def with_decoders(self, decoders: Iterable[FrameDecoder]) -> "DecoderRegistry":
        registry = self
        for decoder in decoders:
            registry = registry.with_decoder(decoder)
        return registry

    def decoders_for_bus(self, bus: str) -> tuple[FrameDecoder, ...]:
        return tuple(decoder for decoder in self.decoders if bus in decoder.supported_buses)

    def decoder_names_for_bus(self, bus: str) -> tuple[str, ...]:
        return tuple(decoder.name for decoder in self.decoders_for_bus(bus))

    def decode_frame(self, frame: CanFrame) -> DecodeResult:
        events = []
        for decoder in self.decoders_for_bus(frame.bus):
            if decoder.handles(frame):
                events.extend(decoder.decode(frame))
        return tuple(events)


def build_default_registry() -> DecoderRegistry:
    from kitt.decoders.w211 import W211_DECODERS

    return DecoderRegistry().with_decoders(W211_DECODERS)
