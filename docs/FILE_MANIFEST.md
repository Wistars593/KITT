# File Manifest

## Canonical Docs

- `AGENTS.md`
- `README.md`
- `SAFETY.md`
- `ROADMAP.md`
- `MIGRATION.md`
- `docs/PROJECT_CONTEXT.md`
- `docs/w211-can-networks.md`
- `docs/w211-can-server-analysis.md`
- `docs/can-safety-model.md`
- `docs/implementation-notes.md`
- `docs/decisions/0001-read-only-first.md`
- `docs/decisions/0002-obd-is-diagnostic-not-raw-can-b.md`

## Archived Or Raw Source Material

- place raw chat exports under `incoming/`
- place retained historical material under `archive/`
- expected source paths from the first migration task were not present at creation time:
  - `incoming/chatgpt-project/2026-06-21/Изучение W211 CAN-сетей.txt`
  - `incoming/chatgpt-project/2026-06-21/Обзор проекта W211 CAN.txt`

## Private Files That Must Not Be Committed

- `.env`
- secret keys and credentials
- private notes
- personally identifying route/location history
- raw voice recordings
- unanonymized CAN captures

## Future Fixture Locations

- `fixtures/can/` for anonymized replay fixtures
- `fixtures/decoded/` for expected decoder outputs
- `tests/data/` for small sanitized test assets if needed

## Ignored Data Categories

- raw CAN captures
- GPS and route logs
- voice recordings
- private reference PDFs
- large manuals and schematics unless explicitly approved
- build artifacts and caches
