# Security Baseline

## Required controls

- Secret management: no plaintext secrets in repo
- Release/package hygiene: local secret overrides, state files, caches, and generated artifacts excluded from deliverables unless intentionally required
- Dependency hygiene: vulnerability scanning enabled
- Input validation: strict validation at trust boundaries
- Authz: explicit checks for privileged actions
- Logging: security-relevant events captured
- Least privilege: service accounts and tokens scoped minimally
- Temporary credentials: long-running cloud operations either use credentials with sufficient lifetime or document a safe recovery process for expired sessions

## Sensitive change categories

- Authentication/authorization logic
- Cryptography, key handling, token handling
- Data export/import, backups, migrations
- Network perimeter or firewall changes

## Mandatory security evidence for sensitive changes

- Threat model
- Test evidence for abuse cases
- Rollback/containment plan
