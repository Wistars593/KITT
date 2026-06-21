# Continuation — KITT W211

## Current State

- Repository: `Wistars593/KITT`.
- Visibility: public.
- Default branch: `main`.
- Phase 2 read-only decoder scaffolding is complete on branch `phase-2-read-only-decoder-scaffolding`.
- Phase 1 remains the merged baseline in `main`.
- ChatGPT project migration into GitHub docs/source archive remains complete.

## What Exists Now

- Repository-level project rules in `AGENTS.md`.
- Safety rules in `SAFETY.md` and `docs/can-safety-model.md`.
- Project memory in `docs/PROJECT_CONTEXT.md`.
- File classification in `docs/FILE_MANIFEST.md`.
- W211 network notes in `docs/w211-can-networks.md`.
- W211 donor project analysis in `docs/w211-can-server-analysis.md`.
- Phase 1 simulation package under `src/kitt/`.
- Phase 2 pure read-only decoder scaffolding under `src/kitt/decoders/`.
- Synthetic CAN fixtures under `fixtures/can/synthetic/`.
- Synthetic decoded expectations under `fixtures/decoded/synthetic/`.
- Tests under `tests/` including decoder tests.

## Safety Posture

Default mode remains read-only and simulation-first.

Still absent by design:

- CAN transmit code,
- SocketCAN integration,
- PCAN integration,
- `python-can` hardware integration,
- hardware access layer,
- actuator logic,
- automatic vehicle behavior,
- Raspberry Pi service files,
- voice assistant runtime,
- real CAN logs,
- VIN/GPS/route/voice data,
- credentials or secrets.

## Next Approved Task

Stay within Phase 2 and expand donor-informed decoder coverage carefully.

Recommended next scope:

- add more sanitized synthetic fixtures,
- introduce donor-informed `CAN B` decoder candidates with explicit scaffolded labeling,
- add fixture-driven tests for field extraction and unknown-frame handling,
- keep decoder modules pure and side-effect-free,
- continue avoiding hardware access and transmit.

## Mandatory Codex Behavior

For every future task, Codex must update:

- `docs/codex-last-report.md`,
- `docs/continuation.md`,
- `docs/PROJECT_CONTEXT.md` if project state changes,
- `docs/FILE_MANIFEST.md` if files are added, moved, or reclassified.

Codex must report:

- files changed,
- validation commands and results,
- safety confirmations,
- commit hash,
- push/PR/merge status,
- exact next task.

## Do Not Do Next

Do not start hardware integration.
Do not add CAN transmit.
Do not connect to a real car.
Do not add PCAN/SocketCAN/python-can code.
Do not import real CAN captures.
Do not copy donor project code as runtime architecture.
Do not add voice/UI/Raspberry Pi services before decoder coverage and fixture discipline are stronger.
