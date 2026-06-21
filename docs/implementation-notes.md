# Implementation Notes

## Phase 1 Skeleton

The current Python package is intentionally simulation-first and read-only:

- `src/kitt/can/frame.py` provides immutable classic CAN frame validation.
- `src/kitt/can/jsonl.py` provides JSONL import and export for synthetic or sanitized fixtures.
- `src/kitt/sim/replay.py` provides offline replay in timestamp order.
- `src/kitt/core/events.py` provides a generic decoded event container with no W211-specific decoder logic yet.
- `src/kitt/cli.py` provides `kitt-can-validate` for validating JSONL CAN logs.

## Explicitly Excluded

- real CAN hardware access,
- SocketCAN,
- PCAN,
- `python-can`,
- CAN transmit,
- actuator commands,
- automatic vehicle behavior,
- Raspberry Pi service wiring,
- real W211 decoder implementations.
