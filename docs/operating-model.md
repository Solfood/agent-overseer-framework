# Operating Model

## Lifecycle

1. Intake
- Define objective, scope, constraints, owner, timeline

2. Risk classification
- Low / Medium / High

3. Design and threat review
- Required for medium/high

4. Implementation oversight
- Ensure adherence to approved design and controls

5. Verification
- Functional, regression, and security checks

6. Release readiness
- Gate review and approval decision

7. Post-release review
- Validate outcomes and capture learnings

## Decision classes

- Fast-path: low risk, reversible, no critical-asset impact
- Standard: medium risk or cross-service impact
- Escalated: high risk, regulated data, auth/crypto/infra boundary changes

## Escalation triggers

- Any unresolved critical or high vulnerability
- Data loss risk without tested backup/rollback
- Irreversible migration without staged validation
