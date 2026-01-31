# Milestone 1 — Deterministic Ordering Contract

## Purpose
Establish a minimal, correctness-first deterministic ordering baseline that is reproducible across environments.

## Guarantees
- Event objects are immutable after creation.
- Ordering depends only on explicit ordering fields, not payload contents.
- Identical input produces identical output.

## Evidence
- Unit tests assert ordering behavior and deterministic replay.
- CI runs formatting, linting, and tests.

## Non-Goals
- Clock skew correction
- Late-arrival windowing
- Causality inference
- Real-time streaming or ingestion
