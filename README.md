# KITT W211

KITT is the start of an assistant-style system for the Mercedes-Benz W211. The intended long-term platform is Raspberry Pi, with staged support for read-only CAN observation, W211 event decoding, local memory, UI, voice interaction, route/context memory, and only much later carefully gated manual actions.

The repository now includes the initial Phase 1 Python simulation skeleton. It remains simulation-only: no vehicle-control code, CAN transmit code, Raspberry Pi services, hardware CAN integration, or voice agent implementation is included.

The ChatGPT project memory has been migrated into GitHub/Codex-facing repository docs and source archives. Future Codex work should use this repository, especially `AGENTS.md`, `docs/continuation.md`, and `docs/codex-last-report.md`, as the canonical handoff state.

## Current Status

- canonical repository memory created,
- W211 network context documented,
- safety model defined,
- migration rules defined,
- decision records started,
- Python package skeleton added for simulation, replay, validation, and tests,
- ChatGPT project exports migrated into `incoming/chatgpt-project/2026-06-21/`,
- Codex continuation/report files added.

## Important Documents

- [AGENTS.md](AGENTS.md)
- [SAFETY.md](SAFETY.md)
- [ROADMAP.md](ROADMAP.md)
- [MIGRATION.md](MIGRATION.md)
- [docs/PROJECT_CONTEXT.md](docs/PROJECT_CONTEXT.md)
- [docs/continuation.md](docs/continuation.md)
- [docs/codex-last-report.md](docs/codex-last-report.md)
- [docs/chatgpt-project-migration-2026-06-21.md](docs/chatgpt-project-migration-2026-06-21.md)
- [docs/w211-can-networks.md](docs/w211-can-networks.md)
- [docs/w211-can-server-analysis.md](docs/w211-can-server-analysis.md)
- [docs/can-safety-model.md](docs/can-safety-model.md)
- [docs/implementation-notes.md](docs/implementation-notes.md)
- [docs/FILE_MANIFEST.md](docs/FILE_MANIFEST.md)
- [docs/decisions/0001-read-only-first.md](docs/decisions/0001-read-only-first.md)
- [docs/decisions/0002-obd-is-diagnostic-not-raw-can-b.md](docs/decisions/0002-obd-is-diagnostic-not-raw-can-b.md)

## Repository Structure

```text
.
├── AGENTS.md
├── README.md
├── SAFETY.md
├── ROADMAP.md
├── MIGRATION.md
├── archive/
├── docs/
│   ├── PROJECT_CONTEXT.md
│   ├── continuation.md
│   ├── codex-last-report.md
│   ├── chatgpt-project-migration-2026-06-21.md
│   ├── FILE_MANIFEST.md
│   ├── can-safety-model.md
│   ├── w211-can-networks.md
│   ├── w211-can-server-analysis.md
│   └── decisions/
├── fixtures/
│   ├── can/
│   └── decoded/
├── incoming/
│   └── chatgpt-project/
├── pyproject.toml
├── src/
│   └── kitt/
└── tests/
```

`incoming/` is for raw migrated source material. `archive/` is for retained historical material. `docs/` is for cleaned, canonical project knowledge that future work should rely on.

## First Development Phases

1. Repository memory and safety rules.
2. Simulation and replay fixtures.
3. Read-only CAN logging.
4. Decoder development, starting with CAN B.
5. Higher-level assistant features such as voice, UI, and local memory.
6. Much later, explicitly gated manual actions.

## How To Use This Repo

- Read [AGENTS.md](AGENTS.md) before starting any Codex task.
- Read [docs/continuation.md](docs/continuation.md) for the current handoff.
- Read [docs/PROJECT_CONTEXT.md](docs/PROJECT_CONTEXT.md) before starting technical work.
- Use [SAFETY.md](SAFETY.md) and [docs/can-safety-model.md](docs/can-safety-model.md) as the guardrails for any CAN-related task.
- Place raw imported notes under `incoming/` or `archive/`.
- Promote only cleaned and reviewed knowledge into `docs/`.
- Update `docs/codex-last-report.md` and `docs/continuation.md` at the end of every Codex task.

## Local Development

Install the package in editable mode with test tooling:

```bash
python3 -m pip install -e '.[dev]'
```

Run the test suite:

```bash
pytest
```

Validate the synthetic CAN fixture log:

```bash
kitt-can-validate fixtures/can/synthetic/sample-log.jsonl
```

This skeleton is simulation-only. It supports JSONL frame validation, offline replay, and future pure decoder work. It does not include real CAN hardware access, transmit support, or vehicle-action behavior.

## Intentionally Not Implemented Yet

- real CAN transmit,
- SocketCAN or PCAN integration,
- automatic window or lock control,
- OBD/CAN D tooling,
- production CAN logging software,
- Raspberry Pi services,
- voice assistant runtime,
- route memory or UI code,
- external dependencies for runtime features.
