# `angelovAlex/w211-can-server` Analysis

## Position In KITT

The `angelovAlex/w211-can-server` project is useful as a donor of CAN-B knowledge, not as production-ready server architecture for KITT.

## Practical Assessment

The donor appears to be an older or experimental C++ and serial-style project rather than a modern, safety-structured platform for an automotive assistant. KITT should not inherit its architecture blindly.

## Potentially Valuable Knowledge

Useful donor knowledge may include:

- CAN IDs,
- bit offsets,
- decoding formulas,
- lock and unlock detection,
- temperature extraction,
- window-related state knowledge,
- frame-to-event observations for CAN B.

This makes the donor valuable as a reference corpus for reverse-engineering and decoder design.

## What Must Not Be Copied Forward

- write behavior,
- automatic window-control logic,
- any hidden coupling between parsing and command output,
- assumptions that donor hardware behavior is safe for a real vehicle.

If the donor contains CAN write behavior, it must not be copied into KITT without a future dedicated safety review, an isolated transmit layer, and explicit disabled-by-default gates.
