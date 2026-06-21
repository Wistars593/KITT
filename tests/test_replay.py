from pathlib import Path

import pytest

from kitt.sim.replay import replay_can_log


def test_replay_preserves_order_without_sleep() -> None:
    fixture = Path("fixtures/can/synthetic/sample-log.jsonl")
    observed_sleeps: list[float] = []

    frames = list(
        replay_can_log(
            fixture,
            deterministic=False,
            speed_multiplier=2.0,
            sleep_fn=observed_sleeps.append,
        )
    )

    assert [frame.arbitration_id for frame in frames] == [0x123, 0x1A4, 0x18FF50E5]
    assert observed_sleeps == [0.75, 0.75]


def test_replay_rejects_out_of_order_input(tmp_path) -> None:
    fixture = tmp_path / "out-of-order.jsonl"
    fixture.write_text(
        '{"timestamp":"2026-06-21T12:00:01Z","bus":"can-b-sim","arbitration_id":"0x124","data":"01","is_extended_id":false}\n'
        '{"timestamp":"2026-06-21T12:00:00Z","bus":"can-b-sim","arbitration_id":"0x123","data":"02","is_extended_id":false}\n',
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="non-decreasing timestamp order"):
        list(replay_can_log(fixture, deterministic=True))
