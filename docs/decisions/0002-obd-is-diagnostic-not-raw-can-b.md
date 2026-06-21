# ADR 0002: OBD Or CAN D Is Diagnostic, Not Raw CAN B

## Status

Accepted

## Context

The W211 includes multiple networks. CAN B is the primary body/interior network relevant to many assistant-style observations. CAN D is associated with diagnostic or gateway access through the N93 Central Gateway, commonly exposed through OBD-related paths.

There is a risk that future work could incorrectly assume OBD access is equivalent to direct CAN B visibility.

## Decision

KITT treats OBD or CAN D access as diagnostic and gateway-oriented access, not as raw CAN B access.

## Consequences

- CAN B observation requirements stay explicit,
- diagnostic tooling and body-network observation remain separate concerns,
- future capture design must verify which network is actually being observed,
- repository documentation and code review should reject any design that collapses the CAN D and CAN B distinction without evidence.
