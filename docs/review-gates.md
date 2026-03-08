# Review Gates

## Gate 1: Coherence

- Requirement link present
- Scope clearly bounded
- Decision record updated (if design-impacting)

## Gate 2: Safety

- Failure modes identified
- Rollback plan documented
- Blast radius understood and acceptable

## Gate 3: Security

- Threat model completed for medium/high risk
- Secrets handling compliant
- Authn/authz controls reviewed for sensitive paths

## Gate 4: Engineering fundamentals

- Baseline engineering fundamentals checklist satisfied
- Design/correctness/maintainability expectations met
- Language/paradigm-specific implementation still adheres to language-agnostic principles

## Gate 5: Verification

- Tests pass
- Security checks pass
- Evidence artifacts attached
- Long-running infrastructure actions use a credential/session strategy that will survive the operation, or a documented recovery path exists (for example stale-lock, errored-state, or retry guidance)

## Gate 6: Release readiness

- Deployment plan documented
- Monitoring and alerting prepared
- On-call/owner identified
- Release package audited for local-only artifacts (state files, secret overrides, caches, generated build outputs)
- Infrastructure teardown plan distinguishes application resources from shared/bootstrap backend resources

## Block conditions

Any failed gate blocks approval until resolved or explicitly risk-accepted by authorized reviewer.
