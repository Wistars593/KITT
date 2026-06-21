# Project Context

KITT is the initial repository for a Mercedes-Benz W211 assistant project intended to evolve into a Raspberry Pi-based in-vehicle system. The long-term scope may include read-only CAN observation, W211 event decoding, voice interaction, local memory, UI, route/context memory, and only later carefully gated manual actions.

## Current State

- Repository `Wistars593/KITT` is public and uses `main` as the canonical branch.
- Phase 1 skeleton is merged into `main`: documentation, migration structure, safety model, ADRs, and a simulation-first Python package scaffold.
- The codebase currently supports offline JSONL validation, replay, and generic event containers only.
- ChatGPT project migration into GitHub/Codex-facing docs/source archive was completed on 2026-06-21.
- Default development posture is read-only.

## Canonical Memory Locations

- `AGENTS.md` contains repository-level instructions for Codex and future agents.
- `docs/continuation.md` contains the current handoff and next task.
- `docs/codex-last-report.md` contains the latest completion report.
- `docs/chatgpt-project-migration-2026-06-21.md` records the ChatGPT-to-GitHub migration boundary.
- `docs/FILE_MANIFEST.md` classifies canonical docs, code, fixtures, raw source material, and private material that must not be committed.

## W211 Network Context

- W211 includes multiple distinct networks: CAN B, CAN C, CAN D, and MOST.
- CAN B is the body/interior network and is the likely primary source for cabin events.
- CAN C covers engine/chassis and must be treated more conservatively.
- CAN D is diagnostic/gateway access through N93 Central Gateway, typically via OBD paths.
- MOST is the audio/media network and is not CAN.
- OBD/CAN D must not be treated as equivalent to raw CAN B access.

## Known Access Notes To Preserve

- Known project access notes include `X30/5` for CAN C and `X30/4`, `X30/6`, `X30/7`, plus rear SAM `N10/2` for CAN B-related investigation.
- CAN B physical characteristics should not be assumed to match ordinary high-speed CAN without verification.

## Donor Project Position

`angelovAlex/w211-can-server` is treated as a donor of CAN-B knowledge only. Useful takeaways may include CAN IDs, bit offsets, decoding formulas, and specific observations such as window, lock/unlock, and temperature decoding behavior. It is not treated as production-ready architecture for KITT.

The donor project includes CAN write behavior and automation ideas, but KITT must not import that behavior into early phases. KITT should extract knowledge only after documentation, sanitization, fixture design, and read-only decoder boundaries are in place.

## Safety Model

- Read-only first.
- Decoders must be pure.
- CAN transmit must be isolated from decoders.
- Any future transmit feature must default to disabled and require explicit gates.
- Simulation and replay must exist before real vehicle actions are considered.
- Public repository contents must not include real CAN logs, VIN/GPS/route/voice data, credentials, local runtime auth, or secrets.

## Immediate Next Step

The next implementation task should be Phase 2: expand sanitized fixtures and introduce pure read-only decoder scaffolding, still without real CAN transmit or hardware access.
