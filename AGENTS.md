# AGENTS.md

## Project Identity

KITT is the repository for an assistant-style system intended for the Mercedes-Benz W211 platform, with an eventual deployment target of Raspberry Pi hardware. The long-term system may include:

- read-only CAN observation,
- W211 event decoding,
- voice interaction,
- local memory,
- UI,
- route and context memory,
- later, carefully gated manual vehicle actions.

This repository is in migration/bootstrap mode. Do not implement production application logic unless the task explicitly advances an approved phase.

## Operating Rule

Default mode is read-only.

Until project safety rules are explicitly revised, all work must assume:

- capture is allowed before control,
- decoding is allowed before control,
- simulation is required before control,
- real vehicle actions are forbidden by default.

## CAN Safety Boundaries

- Treat CAN B, CAN C, CAN D, and MOST as distinct networks with different risk profiles and access assumptions.
- Do not treat OBD or CAN D diagnostic access as equivalent to raw CAN B observation.
- CAN C is higher-risk drivetrain/chassis data and must stay read-only first.
- CAN B is the main target for body/interior observation, but its physical layer must not be assumed to match ordinary high-speed CAN without verification.
- MOST is an audio/media network and should not be treated as CAN.
- Any future real transmit feature must be isolated from decoders, disabled by default, and protected by explicit safety gates.

## Forbidden Behavior

- Do not implement real CAN transmit code in early phases.
- Do not hide CAN transmit behavior inside decoder, parser, event, or helper code.
- Do not implement automatic window control, lock control, or other vehicle actions in this repository phase.
- Do not assume donor code is safe for production use.
- Do not commit VINs, credentials, routes, raw personal location data, private recordings, or private vehicle data.
- Do not add live hardware behavior without a simulation or replay path.

## Required Architecture Rules

- Decoder modules must be pure and read-only.
- Frame capture, decoding, event mapping, planning, safety gating, and transmit must remain separate layers.
- Any future transmit code must live in a dedicated module boundary that is easy to inspect and disable.
- Hardware-facing code must support simulation or dry-run mode.
- Simulation and replay must be built before any real vehicle action support.
- The donor project `angelovAlex/w211-can-server` may be mined for CAN-B knowledge only; it must not be copied in as production server architecture.

## Codex Repository Memory Contract

GitHub is the canonical Codex-facing project memory for KITT.

Every future Codex task must update:

- `docs/codex-last-report.md` with the latest task report,
- `docs/continuation.md` with the next-step handoff,
- `docs/PROJECT_CONTEXT.md` when project context changes,
- `docs/FILE_MANIFEST.md` whenever files are added, moved, or reclassified.

Completion reports must include:

- summary,
- files changed,
- validation commands and results,
- safety confirmations,
- commit hash or PR reference,
- push/merge status,
- exact next recommended task.

Do not rely on a chat transcript as the only project memory after a task is complete. The repository must be left readable by a fresh Codex session.

## Testing Requirements

- Documentation changes must keep all Markdown internally consistent.
- Future parser and decoder changes must include fixture-driven tests.
- Future hardware-facing code must be testable in replay or dry-run mode.
- Any future transmit proposal must include explicit negative tests proving transmit stays disabled by default.
- If linting or Markdown tooling is present, run it. If not present, perform manual consistency checks and note that in the completion report.

## Review Guidelines

Review all future CAN-related changes with a safety-first lens:

- identify whether the change is read-only or write-capable,
- verify decoder purity,
- verify transmit isolation,
- verify disabled-by-default gates,
- verify simulation coverage,
- verify the network assumption is correct for CAN B, CAN C, CAN D, or MOST,
- verify no personal or sensitive data is introduced.

When in doubt, prefer documenting an assumption over implementing behavior.
