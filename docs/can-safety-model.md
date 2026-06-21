# CAN Safety Model

KITT must keep all future CAN work separated into explicit layers so that read-only processing stays inspectable and write-capable behavior cannot be hidden.

## Required Layer Separation

1. Raw frame capture layer
2. Decoder layer
3. Event layer
4. Command planner layer
5. Safety gate layer
6. CAN transmit layer

## Layer Responsibilities

### Raw Frame Capture Layer

- reads frames from hardware or replay sources,
- records timing and metadata,
- performs no semantic interpretation beyond transport handling,
- must support simulation and offline fixtures.

### Decoder Layer

- turns raw frames into structured signal values,
- applies bit offsets and formulas,
- remains pure and read-only,
- must not emit writes, side effects, or hidden commands.

### Event Layer

- maps decoded signals into higher-level assistant events,
- remains read-only,
- must not contain transport writes or actuator logic.

### Command Planner Layer

- represents possible future actions as explicit intent objects,
- must be isolated from transport implementation,
- may exist before transmit is ever enabled.

### Safety Gate Layer

- decides whether a proposed action is blocked, simulated, or allowed,
- defaults to deny,
- requires explicit configuration and future policy review.

### CAN Transmit Layer

- contains all hardware write logic,
- must be isolated in dedicated modules,
- must default to disabled,
- must support simulation and dry-run modes,
- must never be reachable implicitly through decoder or event code.

## Non-Negotiable Rules

- Decoder modules must be pure and read-only.
- Transmit code must be isolated from decoders and parsing code.
- CAN transmit must default to disabled.
- Hardware-facing code must support simulation or dry-run operation.
- Hidden writes inside helpers, adapters, or decoders are forbidden.
- Replay and simulation must be available before real vehicle action support is considered.

## Review Checklist For Future CAN Work

- Is this layer read-only or write-capable?
- Can a reviewer locate all transmit logic in one place?
- Does the decoder remain pure?
- Does the hardware path support replay or dry-run?
- Is transmit disabled by default?
- Is the network assumption explicit: CAN B, CAN C, CAN D, or MOST?
