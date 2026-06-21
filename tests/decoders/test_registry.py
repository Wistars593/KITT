from __future__ import annotations

import ast
import json
from dataclasses import asdict
from pathlib import Path

from kitt.can.frame import CanFrame
from kitt.can.jsonl import load_can_jsonl
from kitt.core.events import DecodedEvent
from kitt.decoders.base import FrameDecoder, SimpleFrameDecoder
from kitt.decoders.registry import DecoderRegistry, build_default_registry
from kitt.decoders.w211 import W211_DECODERS


def test_decoder_interface_accepts_canframe_and_returns_events() -> None:
    registry = build_default_registry()
    frame = CanFrame.from_record(
        {
            "timestamp": "2026-06-21T12:10:00Z",
            "bus": "can-b-sim",
            "arbitration_id": "0x000",
            "data": "01",
            "is_extended_id": False,
        }
    )

    events = registry.decode_frame(frame)

    assert isinstance(W211_DECODERS[0], FrameDecoder)
    assert isinstance(events, tuple)
    assert all(isinstance(event, DecodedEvent) for event in events)


def test_registry_registration_and_lookup_are_immutable() -> None:
    dummy = SimpleFrameDecoder(
        name="test.dummy",
        supported_buses=("can-b-sim",),
        arbitration_ids=frozenset({0x123}),
        decode_fn=lambda frame: (),
    )

    original = DecoderRegistry()
    updated = original.with_decoder(dummy)

    assert original.decoders == ()
    assert updated.decoders_for_bus("can-b-sim") == (dummy,)
    assert updated.decoder_names_for_bus("can-b-sim") == ("test.dummy",)


def test_unknown_can_id_is_ignored_safely() -> None:
    registry = build_default_registry()
    frame = CanFrame.from_record(
        {
            "timestamp": "2026-06-21T12:10:02Z",
            "bus": "can-b-sim",
            "arbitration_id": "0x555",
            "data": "00",
            "is_extended_id": False,
        }
    )

    assert registry.decode_frame(frame) == ()


def test_registry_decoding_matches_sanitized_fixture() -> None:
    registry = build_default_registry()
    frames = load_can_jsonl("fixtures/can/synthetic/decoder-sample-log.jsonl")
    expected = json.loads(
        Path("fixtures/decoded/synthetic/decoder-sample-events.json").read_text(
            encoding="utf-8"
        )
    )

    actual = [
        asdict(event)
        for frame in frames
        for event in registry.decode_frame(frame)
    ]

    assert actual == expected


def test_registry_lookup_has_no_side_effects() -> None:
    registry = build_default_registry()
    before = registry.decoders

    left = registry.decoders_for_bus("can-b-sim")
    right = registry.decoders_for_bus("can-b-sim")

    assert left == right
    assert registry.decoders == before


def test_decoder_modules_do_not_import_hardware_dependencies() -> None:
    banned_roots = {"can", "pcan", "socketcan", "serial", "spidev", "RPi"}

    for path in Path("src/kitt/decoders").rglob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                roots = {name.name.split(".")[0] for name in node.names}
                assert roots.isdisjoint(banned_roots), path
            elif isinstance(node, ast.ImportFrom) and node.module:
                root = node.module.split(".")[0]
                assert root not in banned_roots, path
