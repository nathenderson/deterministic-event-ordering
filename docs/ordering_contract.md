# Ordering Contract

## Ordering fields
Ordering depends only on:
1. `event_time`
2. `source_priority`
3. `event_id`

Payload is treated as opaque and does not affect ordering.

## Deterministic rule
Events are ordered using a stable tuple key:

`(event_time, source_priority, event_id)`

## Interpretation
This is a strict rule contract, not a best-effort estimator. If two events collide on all ordering fields,
the system must surface ambiguity rather than guessing.

## Non-Goals
- Clock skew correction
- Late arrival windowing
- Causality inference
