# Milestones

## Milestone 1 — Deterministic Ordering Baseline (Complete)

### Deliverable
A deterministic, rule-based event ordering function with explicit assumptions and test-backed guarantees.

### Guarantees
- Deterministic ordering based on an explicit contract.
- Stable tie-breaking for identical event_time using explicit secondary/tertiary keys.
- Reproducible outputs for identical inputs across environments.

### Evidence
- Unit tests that fail if the ordering contract breaks.
- CI validation (format + lint + tests).

### Non-Goals
- Clock skew estimation/correction
- Late arrival handling
- Heuristic inference
- Real-time performance constraints

## Milestone 2 — Ambiguity Handling + Unresolved States (Planned)
(Defined in planning before implementation.)
