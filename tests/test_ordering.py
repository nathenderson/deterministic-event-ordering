from datetime import datetime

from deterministic_event_ordering.model import Event
from deterministic_event_ordering.ordering import order_events


def test_deterministic_ordering_basic():
    events = [
        Event(datetime(2024, 1, 1, 0, 0, 1), 2, "B"),
        Event(datetime(2024, 1, 1, 0, 0, 1), 1, "A"),
        Event(datetime(2024, 1, 1, 0, 0, 0), 1, "C"),
    ]

    ordered = order_events(events)

    assert [e.event_id for e in ordered] == ["C", "A", "B"]
