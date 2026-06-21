import pytest

from kitt.core.events import DecodedEvent


def test_decoded_event_accepts_valid_confidence() -> None:
    event = DecodedEvent(
        source="sim.replay",
        name="door_open",
        value=True,
        confidence=0.75,
        metadata={"bus": "can-b-sim"},
    )

    assert event.confidence == 0.75
    assert event.metadata == {"bus": "can-b-sim"}


def test_decoded_event_rejects_out_of_range_confidence() -> None:
    with pytest.raises(ValueError, match="between 0.0 and 1.0"):
        DecodedEvent(
            source="sim.replay",
            name="door_open",
            value=True,
            confidence=1.5,
        )
