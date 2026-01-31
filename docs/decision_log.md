# Decision Log

## D1 — Immutable Event model
**Decision:** Represent events as immutable objects.

**Why:** Eliminates hidden mutation and enables deterministic replay.

**Alternatives considered:** Mutable class, dict-based events.

**Risk:** Future pipelines requiring mutation must create new events rather than modifying existing ones.

---

## D2 — Explicit deterministic ordering contract
**Decision:** Define ordering via an explicit, stable tuple-key contract.

**Why:** Reviewable determinism with no heuristics or randomness.

**Alternatives considered:** Heuristic timestamp ordering, inference-based tie-breaking.

**Risk:** True ties remain possible; higher layers must represent ambiguity explicitly rather than guessing.

---

## D3 — Treat payload as opaque
**Decision:** Payload content does not participate in ordering.

**Why:** Prevents hidden coupling and preserves separation between ordering and semantic interpretation.

**Risk:** Some domains may want payload-derived ordering later; that will be a new contract and milestone.
