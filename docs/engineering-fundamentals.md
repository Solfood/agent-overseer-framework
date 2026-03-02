# Engineering Fundamentals Baseline (Language-Agnostic)

This baseline applies across programming languages and paradigms (procedural, object-oriented, functional, event-driven, dataflow).

## 1) Problem framing

- Clear objective and success criteria
- Explicit scope and non-goals
- Known constraints and assumptions documented

## 2) Design quality

- Separation of concerns and bounded responsibilities
- Clear interfaces/contracts between components
- Simplicity first; avoid unnecessary abstraction
- Backward/forward compatibility considered when relevant

## 3) Correctness

- Deterministic behavior for core logic where possible
- Input validation at all trust boundaries
- Error handling paths implemented and tested
- Edge cases and failure modes explicitly covered

## 4) Readability and maintainability

- Names convey intent
- Control flow is easy to follow
- Comments explain non-obvious decisions
- Dead code and duplication minimized

## 5) Testing and verification

- Appropriate automated tests for risk level
- Regression protection for changed behavior
- Reproducible validation evidence attached
- Test gaps and residual risks documented

## 6) Performance and resource usage

- Basic complexity awareness (time/space)
- Resource-heavy paths identified
- Capacity/reliability tradeoffs made explicit

## 7) Security and safety

- Least privilege and secure defaults
- Sensitive data handling follows policy
- Abuse/failure scenarios considered and mitigated

## 8) Operability

- Logs/metrics sufficient for diagnosis
- Rollback/containment path exists for risky changes
- Ownership and runbook/checkpoint information present

## 9) Delivery discipline

- Small, reviewable change slices
- Decisions and tradeoffs recorded
- Release readiness gates satisfied before approval

## Enforcement

The Overseer should block or conditionally approve work when this baseline is materially violated.
