from __future__ import annotations

import time
from collections.abc import Callable, Iterator
from pathlib import Path

from kitt.can.frame import CanFrame
from kitt.can.jsonl import read_can_jsonl


def replay_can_log(
    path: Path | str,
    *,
    deterministic: bool = False,
    speed_multiplier: float = 1.0,
    sleep_fn: Callable[[float], None] = time.sleep,
) -> Iterator[CanFrame]:
    """Replay a JSONL CAN log in timestamp order.

    When ``deterministic`` is true, no sleeping is performed. Otherwise
    inter-frame delays are scaled by ``speed_multiplier``.
    """

    if speed_multiplier <= 0:
        raise ValueError("speed_multiplier must be greater than zero")

    previous = None
    for frame in read_can_jsonl(path):
        if previous is not None:
            if frame.timestamp < previous.timestamp:
                raise ValueError("frames must be in non-decreasing timestamp order")

            if not deterministic:
                delay = (frame.timestamp - previous.timestamp).total_seconds()
                sleep_fn(delay / speed_multiplier)

        yield frame
        previous = frame
