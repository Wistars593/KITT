# KITT W211

KITT is the start of an assistant-style system for the Mercedes-Benz W211. The intended long-term platform is Raspberry Pi, with staged support for read-only CAN observation, W211 event decoding, local memory, UI, voice interaction, route/context memory, and only much later carefully gated manual actions.

The repository is currently in Phase 0: documentation and migration setup only. No vehicle-control code, CAN transmit code, Raspberry Pi services, or voice agent implementation is included yet.

## Current Status

- canonical repository memory created,
- W211 network context documented,
- safety model defined,
- migration rules defined,
- decision records started.

## Important Documents

- [SAFETY.md](SAFETY.md)
- [ROADMAP.md](ROADMAP.md)
- [MIGRATION.md](MIGRATION.md)
- [docs/PROJECT_CONTEXT.md](docs/PROJECT_CONTEXT.md)
- [docs/w211-can-networks.md](docs/w211-can-networks.md)
- [docs/w211-can-server-analysis.md](docs/w211-can-server-analysis.md)
- [docs/can-safety-model.md](docs/can-safety-model.md)
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
│   ├── FILE_MANIFEST.md
│   ├── can-safety-model.md
│   ├── w211-can-networks.md
│   ├── w211-can-server-analysis.md
│   └── decisions/
├── fixtures/
│   ├── can/
│   └── decoded/
└── incoming/
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

- Read [docs/PROJECT_CONTEXT.md](docs/PROJECT_CONTEXT.md) before starting technical work.
- Follow [AGENTS.md](AGENTS.md) for repository-level instructions.
- Use [SAFETY.md](SAFETY.md) and [docs/can-safety-model.md](docs/can-safety-model.md) as the guardrails for any CAN-related task.
- Place raw imported notes under `incoming/` or `archive/`.
- Promote only cleaned and reviewed knowledge into `docs/`.

## Intentionally Not Implemented Yet

- real CAN transmit,
- automatic window or lock control,
- OBD/CAN D tooling,
- production CAN logging software,
- Raspberry Pi services,
- voice assistant runtime,
- route memory or UI code,
- external dependencies for runtime features.
