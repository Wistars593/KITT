from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class DecodedEvent:
    """Immutable decoded event container for future pure decoder output."""

    source: str
    name: str
    value: Any
    confidence: float
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isinstance(self.source, str) or not self.source.strip():
            raise ValueError("source must be a non-empty string")
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(self.confidence, (int, float)):
            raise TypeError("confidence must be numeric")
        if not 0.0 <= float(self.confidence) <= 1.0:
            raise ValueError("confidence must be between 0.0 and 1.0")
        if not isinstance(self.metadata, dict):
            raise TypeError("metadata must be a dictionary")

        object.__setattr__(self, "source", self.source.strip())
        object.__setattr__(self, "name", self.name.strip())
        object.__setattr__(self, "confidence", float(self.confidence))
        object.__setattr__(self, "metadata", dict(self.metadata))
