# KITT Roadmap

## Stage 1: Repository Memory

- establish canonical project context,
- record W211 network distinctions,
- define migration rules,
- define safety boundaries,
- add initial architecture decisions.

## Stage 2: Simulation

- define fixture formats,
- define replay interfaces,
- establish dry-run hardware abstractions,
- create sample offline decoder test flow.

## Stage 3: Read-Only CAN

- choose read-only capture approach,
- document candidate hardware access paths,
- design logging format and metadata,
- keep CAN C strictly observational,
- avoid CAN transmit entirely.

## Stage 4: CAN-B Decoder

- extract CAN-B donor knowledge,
- map CAN IDs, bit offsets, and formulas,
- build pure decoders with fixtures,
- represent cabin and body events cleanly,
- explicitly exclude window-control writes.

## Stage 5: CAN-D Diagnostics Notes

- document N93 Central Gateway and diagnostic assumptions,
- separate diagnostics knowledge from CAN-B observation,
- record what OBD can and cannot substitute for,
- avoid turning diagnostic notes into control features.

## Stage 6: Voice Layer

- define assistant interaction model,
- connect decoded events to a read-only event layer,
- design local memory and context model,
- keep vehicle actions out of voice scope until later review.

## Stage 7: Raspberry Pi Deployment

- choose packaging and service model,
- define local storage, logs, and data retention,
- support offline replay on target hardware,
- keep runtime safe in simulation mode by default.

## Stage 8: Later Gated Manual Actions

- only after prior stages are stable,
- only for isolated, explicitly reviewed commands,
- only with disabled-by-default transmit,
- only with simulation, dry-run, and manual operator intent.
