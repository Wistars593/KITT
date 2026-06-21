# Project Context

KITT is the initial repository for a Mercedes-Benz W211 assistant project intended to evolve into a Raspberry Pi-based in-vehicle system. The long-term scope may include read-only CAN observation, W211 event decoding, voice interaction, local memory, UI, route/context memory, and only later carefully gated manual actions.

## Current State

- Phase 1 skeleton: documentation, migration structure, safety model, ADRs, and a simulation-first Python package scaffold.
- The codebase currently supports offline JSONL validation, replay, and generic event containers only.
- Default development posture is read-only.

## W211 Network Context

- W211 includes multiple distinct networks: CAN B, CAN C, CAN D, and MOST.
- CAN B is the body/interior network and is the likely primary source for cabin events.
- CAN C covers engine/chassis and must be treated more conservatively.
- CAN D is diagnostic/gateway access through N93 Central Gateway, typically via OBD paths.
- MOST is the audio/media network and is not CAN.
- OBD/CAN D must not be treated as equivalent to raw CAN B access.

## Known Access Notes To Preserve

- Known project access notes include `X30/5` for CAN C and `X30/4`, `X30/6`, `X30/7`, plus rear SAM `N10/2` for CAN B-related investigation.
- CAN B physical characteristics should not be assumed to match ordinary high-speed CAN without verification.

## Donor Project Position

`angelovAlex/w211-can-server` is treated as a donor of CAN-B knowledge only. Useful takeaways may include CAN IDs, bit offsets, decoding formulas, and specific observations such as window, lock/unlock, and temperature decoding behavior. It is not treated as production-ready architecture for KITT.

## Safety Model

- Read-only first.
- Decoders must be pure.
- CAN transmit must be isolated from decoders.
- Any future transmit feature must default to disabled and require explicit gates.
- Simulation and replay must exist before real vehicle actions are considered.

## Immediate Next Step

The next implementation task should expand sanitized fixtures and introduce pure read-only decoder scaffolding, still without real CAN transmit or hardware access.
