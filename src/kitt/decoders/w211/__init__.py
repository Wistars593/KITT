"""W211-oriented decoder scaffolding.

These decoders are scaffolded, synthetic, and read-only. They exist to prove the
interface and registry architecture, not to claim production-ready vehicle decoding.
"""

from kitt.decoders.w211.can_b import CAN_B_DECODERS
from kitt.decoders.w211.can_c import CAN_C_DECODERS
from kitt.decoders.w211.can_d import CAN_D_DECODERS

W211_DECODERS = CAN_B_DECODERS + CAN_C_DECODERS + CAN_D_DECODERS

__all__ = ["CAN_B_DECODERS", "CAN_C_DECODERS", "CAN_D_DECODERS", "W211_DECODERS"]
