# W211 CAN Networks

This document is the clean engineering summary of the W211 network context currently preserved in KITT.

## CAN B

CAN B is the body and interior network. It is the main candidate for cabin and user-interaction events such as:

- doors,
- windows,
- SAM-related body events,
- climate,
- seats,
- OCP/UCP controls,
- Parktronic,
- TPMS-related body-side visibility,
- AGW-linked interior context,
- lighting,
- button and cabin state events.

KITT will likely rely on CAN B for assistant-relevant body/interior observations. CAN B should still be approached carefully because Mercedes physical characteristics must not be assumed to match ordinary high-speed CAN without verification.

## CAN C

CAN C is the engine and chassis network. Relevant modules may include:

- ME-SFI,
- ESP,
- EGS/ETC,
- selector state,
- suspension,
- Distronic,
- drivetrain and chassis signals.

CAN C is higher-risk and should be treated read-only first.

## CAN D

CAN D is associated with diagnostic and gateway access, including OBD-facing diagnostics through the N93 Central Gateway. It is not the same thing as direct raw CAN B observation.

## MOST

MOST is the audio and media network. It should be treated separately from CAN-based work.

## N93 Central Gateway

N93 Central Gateway is the key distinction point for diagnostic/gateway access. Any future OBD-related work must keep the gateway/diagnostic nature of CAN D explicit and must not collapse that distinction into assumptions about raw CAN B visibility.

## OBD Versus CAN B

- OBD or CAN D access is diagnostic/gateway access.
- CAN B is the body/interior network needed for many assistant-relevant cabin events.
- OBD/CAN D must not be treated as a substitute for direct CAN B access without evidence.

## Known Physical Access Points

Known project notes mention these access points:

- `X30/5` for CAN C,
- `X30/4` for CAN B,
- `X30/6` for CAN B,
- `X30/7` for CAN B,
- rear SAM `N10/2`.

These references are preserved as project notes, not as verified wiring instructions.

## Read-Only-First Approach

- start with documentation,
- move to read-only logging,
- build replay and simulation,
- implement pure decoders,
- consider any hardware action only much later and behind explicit safety gates.
