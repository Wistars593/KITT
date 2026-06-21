# Migration Rules

## Raw Versus Canonical Material

- Raw imported source files belong under `incoming/` or `archive/`.
- Cleaned, reviewed, canonical knowledge belongs under `docs/`.
- Future tasks should treat `docs/` as the main engineering reference, not raw chat exports.

## Sensitive Data Handling

- Do not commit secrets, credentials, tokens, keys, `.env` files, or personal notes.
- Do not commit VINs, routes, precise location history, private voice recordings, or personally identifying logs.
- Real CAN logs must be anonymized before they become reusable fixtures.

## Source Material Handling

- Chat exports, scratch notes, and donor references may be preserved as raw history under `incoming/` or `archive/`.
- PDFs, workshop manuals, and schematics should usually be represented by summarized notes in `docs/`.
- Commit raw manuals or large PDFs only if explicitly permitted and legally appropriate.

## Canonicalization Process

1. Preserve the original raw source file when it is useful.
2. Extract durable technical facts into a focused document under `docs/`.
3. Separate observation from assumption.
4. Mark anything safety-critical or uncertain.
5. Avoid copying donor-project code directly into KITT during migration.

## Current Migration Note

The prompt referenced the following source files, but they were not present in this workspace during the initial migration task:

- `incoming/chatgpt-project/2026-06-21/Изучение W211 CAN-сетей.txt`
- `incoming/chatgpt-project/2026-06-21/Обзор проекта W211 CAN.txt`

The current canonical documents were created from the project context preserved in the task prompt and should be updated if those raw notes are later added.
