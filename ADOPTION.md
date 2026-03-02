# Adoption Guide

## Integration options

1. Subdirectory mode:
- Copy this repo into your project under `.overseer/`

2. Independent governance repo:
- Keep this as a separate repo and reference it in your project docs/automation

## Required first-day setup

1. Edit `policies/overseer-policy.yaml`:
- project_name
- critical_assets
- compliance_requirements
- risk_tolerance
- required_reviewers

2. Configure your agent with:
- `prompts/overseer-system-prompt.md`
- `docs/operating-model.md`

3. Start using templates:
- `templates/task-intake.md`
- `templates/decision-record.md`
- `templates/threat-model.md`
- `templates/release-readiness.md`

4. Run validation:
```bash
python3 tools/validate_overseer_framework.py
```

## Recommended operating cadence

- Every task: intake + risk classification
- Every design decision: decision record + alternatives
- Every release: security and readiness gates
- Every incident: postmortem using the same evidence model
