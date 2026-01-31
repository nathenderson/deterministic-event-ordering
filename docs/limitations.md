# Limitations

This document defines intentional limitations of the Deterministic Event Ordering Engine.
These constraints are design decisions, not missing features.

---

## Temporal Limitations

- No clock skew correction
- No time synchronization modeling
- No late or out-of-order arrival handling
- No causal inference beyond explicit ordering fields

---

## Operational Limitations

- Batch processing only
- No real-time or streaming support
- No incremental updates
- No persistence layer

---

## Analytical Limitations

- No payload inspection or semantic interpretation
- No inference from partial data
- No probabilistic or heuristic ordering

---

## System Boundaries

- The engine is not flight software.
- The engine is not safety-certified.
- The engine is intended for deterministic analysis and tooling, not operations.

---

## Scaling Limitations

- Performance optimization is not a goal.
- Large-scale datasets have not been evaluated.
- Correctness and auditability are prioritized over throughput.

---

## Evolution Notes

These limitations may be revisited in future milestones.
Any relaxation must be explicitly documented and justified.
