# File Manifest

## Canonical Docs

- `AGENTS.md`
- `README.md`
- `SAFETY.md`
- `ROADMAP.md`
- `MIGRATION.md`
- `docs/PROJECT_CONTEXT.md`
- `docs/continuation.md`
- `docs/codex-last-report.md`
- `docs/chatgpt-project-migration-2026-06-21.md`
- `docs/w211-can-networks.md`
- `docs/w211-can-server-analysis.md`
- `docs/can-safety-model.md`
- `docs/implementation-notes.md`
- `docs/decisions/0001-read-only-first.md`
- `docs/decisions/0002-obd-is-diagnostic-not-raw-can-b.md`

## Code And Test Files

- `pyproject.toml`
- `src/kitt/`
- `src/kitt/decoders/`
- `tests/`
- `fixtures/can/synthetic/sample-log.jsonl`
- `fixtures/can/synthetic/decoder-sample-log.jsonl`
- `fixtures/decoded/synthetic/decoder-sample-events.json`

## Archived Or Raw Source Material

Raw migrated ChatGPT project exports are stored under:

- `incoming/chatgpt-project/2026-06-21/Изучение W211 CAN-сетей.txt`
- `incoming/chatgpt-project/2026-06-21/Обзор проекта W211 CAN.txt`

These files are retained as source memory only. Cleaned, actionable knowledge should be promoted to canonical docs before implementation work depends on it.

Place future raw chat exports under `incoming/`.
Place retained historical material under `archive/`.

## Private Files That Must Not Be Committed

- `.env`
- secret keys and credentials
- private notes
- personally identifying route/location history
- raw voice recordings
- unanonymized CAN captures
- VINs
- local runtime/auth files
- real vehicle logs

## Future Fixture Locations

- `fixtures/can/` for anonymized replay fixtures
- `fixtures/decoded/` for expected decoder outputs
- `tests/data/` for small sanitized test assets if needed

## Ignored Data Categories

- raw CAN captures
- GPS and route logs
- voice recordings
- private reference PDFs
- large manuals and schematics unless explicitly approved and legally safe
- build artifacts and caches
