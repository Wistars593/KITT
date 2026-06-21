# Continuation — KITT W211

## Current State

- Repository: `Wistars593/KITT`.
- Visibility: public.
- Default branch: `main`.
- Phase 1 Python simulation skeleton is merged into `main`.
- Phase 1 merge commit: `5f0be94523fb55b142359a36fca079662d4c450d`.
- ChatGPT project migration into GitHub docs/source archive completed on 2026-06-21.

## What Exists Now

- Repository-level project rules in `AGENTS.md`.
- Safety rules in `SAFETY.md` and `docs/can-safety-model.md`.
- Project memory in `docs/PROJECT_CONTEXT.md`.
- File classification in `docs/FILE_MANIFEST.md`.
- W211 network notes in `docs/w211-can-networks.md`.
- W211 donor project analysis in `docs/w211-can-server-analysis.md`.
- Phase 1 implementation notes in `docs/implementation-notes.md`.
- ChatGPT migration record in `docs/chatgpt-project-migration-2026-06-21.md`.
- Raw migrated ChatGPT project exports under `incoming/chatgpt-project/2026-06-21/`.
- Python package skeleton under `src/kitt/`.
- Synthetic CAN fixture under `fixtures/can/synthetic/sample-log.jsonl`.
- Tests under `tests/`.

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

Start Phase 2: pure read-only decoder scaffolding.

Phase 2 scope:

- Define decoder interfaces.
- Add decoder registry.
- Add W211-oriented decoder module structure.
- Use sanitized synthetic fixtures only.
- Add tests for deterministic decoder behavior.
- Keep unknown CAN IDs safely ignored.
- Keep decoder modules pure and side-effect-free.
- Keep all hardware and transmit code out of scope.

Suggested structure:

```text
src/kitt/decoders/
src/kitt/decoders/base.py
src/kitt/decoders/registry.py
src/kitt/decoders/w211/
src/kitt/decoders/w211/can_b.py
src/kitt/decoders/w211/can_c.py
src/kitt/decoders/w211/can_d.py
tests/decoders/
fixtures/can/synthetic/
```

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
Do not add voice/UI/Raspberry Pi services before decoder scaffolding is stable.
