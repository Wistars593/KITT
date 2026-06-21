# Safety Model By Phase

KITT is an automotive project. Safety constraints are part of the architecture, not an optional review step.

## Phase 0: Documentation Only

- Allowed: project memory, migration notes, architecture notes, safety rules, ADRs.
- Forbidden: hardware access, CAN logging code, CAN transmit code, automation against a real vehicle.

## Phase 1: Read-Only CAN Logging

- Allowed: read-only frame capture, offline storage design, interface notes, fixture collection rules.
- Forbidden: any CAN transmit, hidden writes, actuator logic, automatic control behavior.

## Phase 2: Simulation And Replay

- Allowed: offline replay tools, deterministic fixtures, decoder test harnesses, dry-run hardware interfaces.
- Required: simulation and replay paths before real-world actions are considered.
- Forbidden: real CAN transmit in normal development flow.

## Phase 3: Decoders

- Allowed: pure decoding logic, event extraction, formulas, bit offsets, normalization layers.
- Required: decoder purity and fixture-driven tests.
- Forbidden: write behavior inside decoders, planners, or event mappers.

## Phase 4: Voice, UI, And Memory

- Allowed: assistant UX, local memory, route/context models, display logic, voice interaction, replay-backed demos.
- Required: separation from hardware action paths.
- Forbidden: implicit control actions triggered only by conversational output.

## Phase 5: Gated Manual Actions Only

- Allowed only after explicit safety review: isolated transmit modules, manual-action workflows, strong safety gates, disabled-by-default configuration, dry-run mode, explicit user/operator intent.
- Still forbidden: automatic control loops, hidden writes, uncontrolled startup behavior, default-on transmit.

## Non-Negotiable Rules

- Real CAN transmit is forbidden in early phases.
- CAN transmit must not be implemented in decoders or helpers.
- Simulation and replay must exist before any real vehicle action path.
- OBD/CAN D diagnostic access must not be treated as raw CAN B access.
- CAN C must be handled with extra caution and remain read-only first.
