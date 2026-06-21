# ADR 0001: KITT Starts Read-Only

## Status

Accepted

## Context

KITT is an automotive assistant project targeting the Mercedes-Benz W211. The system may eventually observe CAN traffic, decode events, provide UI and voice features, and later support carefully gated manual actions. Because the project touches vehicle networks, early architecture must prevent accidental writes and keep review simple.

## Decision

KITT starts in a read-only-first mode.

That means:

- initial repository work is documentation only,
- early code phases focus on capture, replay, and decoding,
- decoders remain pure,
- real CAN transmit is not implemented in the initial phases.

## Consequences

- review is simpler because write-capable behavior is absent,
- simulation and replay become mandatory foundation work,
- any future transmit support must be proposed explicitly and isolated architecturally,
- early roadmap work prioritizes understanding CAN B, CAN C, CAN D, and MOST correctly before action features are considered.
