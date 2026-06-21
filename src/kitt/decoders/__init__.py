"""Pure read-only decoder scaffolding for KITT."""

from kitt.decoders.base import DecodeResult, FrameDecoder, SimpleFrameDecoder
from kitt.decoders.registry import DecoderRegistry, build_default_registry

__all__ = [
    "DecodeResult",
    "DecoderRegistry",
    "FrameDecoder",
    "SimpleFrameDecoder",
    "build_default_registry",
]
