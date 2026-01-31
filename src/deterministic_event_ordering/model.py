from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True, slots=True)
class Event:
    """
    Immutable event record.

    Ordering contract:
    1) event_time
    2) source_priority (lower wins)
    3) event_id (lexicographic final tie-break)
    """

    event_time: datetime
    source_priority: int
    event_id: str
    payload: Any = None
