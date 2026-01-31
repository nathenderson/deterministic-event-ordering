# Assumptions

This document enumerates all assumptions relied upon by the Deterministic Event Ordering Engine.
If any assumption is violated, ordering correctness is not guaranteed.

No assumptions are implicit.

---

## Event Model Assumptions

- Events are **immutable** once created.
- All fields relevant to ordering are explicit and present at construction time.
- Event payloads are treated as **opaque data** and do not influence ordering.
- Each event has a stable, unique identifier (`event_id`) within a single ordering batch.

---

## Temporal Assumptions

- `event_time` represents the event’s intended logical time.
- No clock skew correction is performed in this milestone.
- All time values are assumed to be comparable without normalization.
- The engine does not infer time ordering beyond provided values.

---

## Source Assumptions

- `source_priority` is provided externally and reflects a trusted precedence ranking.
- Lower numeric priority values indicate higher precedence.
- Source priority is stable across the ordering batch.

---

## Input Scope Assumptions

- All events to be ordered are available as a complete batch.
- No events are added, removed, or modified during ordering.
- The engine does not handle streaming or incremental inputs.

---

## Determinism Assumptions

- Given identical input events, ordering output is identical across executions.
- No randomness, external state, or wall-clock time is used.

---

## Responsibility Boundaries

The engine assumes:
- Validation of input correctness occurs upstream.
- Consumers understand and accept documented limitations.

Violations of these assumptions constitute out-of-contract usage.
