from __future__ import annotations

from typing import Iterable, List

from .model import Event


def order_events(events: Iterable[Event]) -> List[Event]:
    """
    Deterministic ordering contract.

    Sort order:
    1) event_time
    2) source_priority
    3) event_id
    """

    return sorted(
        events,
        key=lambda e: (e.event_time, e.source_priority, e.event_id),
    )
