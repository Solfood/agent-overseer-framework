# Paired Usage with Engineering Scaffold Template

This repository defines oversight and controls. Pair it with:

- `engineering-scaffold-template` for execution structure and delivery mechanics.

## Responsibility split

- `agent-overseer-framework`:
- Governance policy, risk classification, security baseline, gate decisions.

- `engineering-scaffold-template`:
- Marker workflow, implementation sequencing, evidence capture, container/CI execution path.

## Recommended combined flow

1. Intake + risk classify (overseer template).
2. Execute through markerized engineering workflow.
3. Attach verification evidence from engineering outputs.
4. Run overseer gates (coherence/safety/security/fundamentals/verification/readiness).
5. Record final approval or block decision with rationale.

## Required artifacts from execution side

- Task/marker traceability
- Decision records and alternatives
- Test/log/metric evidence
- Rollback and operational readiness notes
