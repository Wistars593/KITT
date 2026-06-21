# ChatGPT Project Migration — 2026-06-21

## Purpose

This document records the final migration of the KITT W211 project memory from the ChatGPT project context into the public GitHub repository `Wistars593/KITT`.

The migration goal is to make GitHub the canonical working memory for Codex and future repository work, while keeping unsafe or private material out of the public repository.

## Migration Status

- GitHub repository: `Wistars593/KITT`.
- Repository visibility: public.
- Default branch: `main`.
- Phase 1 PR merged into `main`: PR `#2`, `Add Phase 1 Python simulation skeleton`.
- Phase 1 merge commit: `5f0be94523fb55b142359a36fca079662d4c450d`.
- Current canonical state: Phase 1 simulation-first Python skeleton is present in `main`.

## Source Material Migrated

The following ChatGPT project exports were added under `incoming/chatgpt-project/2026-06-21/` as retained source material:

- `Изучение W211 CAN-сетей.txt`
- `Обзор проекта W211 CAN.txt`

These files are not the primary implementation source. They are retained as migrated project memory. Cleaned and actionable project knowledge should live in canonical docs under `docs/`.

## Canonical Knowledge Already Promoted

The cleaned repository memory already includes:

- W211 network separation: CAN B, CAN C, CAN D, MOST.
- OBD/CAN D warning: OBD diagnostic access must not be treated as raw CAN B.
- Known investigation points: X30/5, X30/4, X30/6, X30/7, rear SAM N10/2.
- Donor project position: `angelovAlex/w211-can-server` is a source of CAN-B knowledge, not production architecture.
- Safety-first rule: read-only first; simulation before hardware; no transmit in early phases.
- Phase 1 Python skeleton: immutable CAN frame/event models, JSONL handling, replay, CLI validation, synthetic fixture, and tests.

## Material Intentionally Not Migrated

The public repository must not contain:

- Mercedes proprietary PDFs or large manuals unless explicitly approved and legally safe.
- Real CAN captures.
- VINs.
- GPS or route history.
- Voice recordings.
- Credentials, tokens, `.env` files, or local auth files.
- Private notes unrelated to KITT implementation.
- Hardware-control code hidden inside parser, decoder, event, or helper layers.

## Codex Working Memory Contract

Every future Codex task for this repository must update:

- `docs/codex-last-report.md` — the latest task report.
- `docs/continuation.md` — the next-step handoff and current state.
- `docs/PROJECT_CONTEXT.md` — only when project context changes.
- `docs/FILE_MANIFEST.md` — whenever files are added, moved, or reclassified.

Completion reports should include:

- summary,
- files changed,
- validation performed,
- safety confirmations,
- commit hash or PR reference,
- push/merge status,
- next recommended task.

## Current Next Task

Phase 2 should introduce pure read-only decoder scaffolding around sanitized synthetic fixtures only.

Phase 2 must not add:

- CAN transmit,
- SocketCAN integration,
- PCAN integration,
- `python-can` hardware integration,
- hardware access layer,
- actuator logic,
- automatic vehicle behavior,
- Raspberry Pi service files,
- real vehicle logs.

## Obsidian Note

This repository is now the canonical Codex-facing memory. If an Obsidian vault is used later, it should be a filtered safe sync of repository docs and reports only. Do not sync secrets, raw logs, credentials, voice recordings, VIN/GPS data, or local runtime files into Obsidian.
