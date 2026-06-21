# Implementation Notes

## Phase 1 Skeleton

The current Python package is intentionally simulation-first and read-only:

- `src/kitt/can/frame.py` provides immutable classic CAN frame validation.
- `src/kitt/can/jsonl.py` provides JSONL import and export for synthetic or sanitized fixtures.
- `src/kitt/sim/replay.py` provides offline replay in timestamp order.
- `src/kitt/core/events.py` provides a generic decoded event container with no W211-specific decoder logic yet.
- `src/kitt/cli.py` provides `kitt-can-validate` for validating JSONL CAN logs.

## Phase 2 Decoder Scaffolding

Phase 2 adds pure read-only decoder architecture only:

- `src/kitt/decoders/base.py` defines immutable decoder contracts.
- `src/kitt/decoders/registry.py` provides pure registry lookup and frame decoding dispatch.
- `src/kitt/decoders/w211/` provides W211-oriented module boundaries for `CAN B`, `CAN C`, and `CAN D`.
- `fixtures/can/synthetic/decoder-sample-log.jsonl` and `fixtures/decoded/synthetic/decoder-sample-events.json` provide sanitized deterministic examples.

These decoders are scaffolded and synthetic. They prove interface shape, registry behavior, and deterministic testing. They do not claim validated real-vehicle decoding.

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
