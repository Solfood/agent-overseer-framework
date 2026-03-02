# Agent Overseer Framework

A reusable framework for an AI agent that oversees project execution for coherence, safety, and security.

## Purpose

This framework defines how an Overseer Agent governs work so teams can move fast without compromising:

- Cohesion: architecture, requirements, and implementation stay aligned
- Safety: risky operations are identified and controlled
- Security: threat exposure is continuously reduced
- Traceability: decisions, risks, and evidence are auditable

## What this repository provides

- Overseer system prompt and operating protocol
- Governance policies and gate criteria
- Security/risk baselines and threat modeling templates
- Work-intake and release-checklist templates
- Validation script to ensure framework integrity
- CI workflow that enforces scaffold validity

## Quick Start

1. Copy or clone into your project as `.overseer/` or `governance/`.
2. Fill in project-specific values in `policies/overseer-policy.yaml`.
3. Use templates for every significant work item.
4. Run:
   - `python3 tools/validate_overseer_framework.py`
5. Wire your execution agent to `prompts/overseer-system-prompt.md`.

## Core Principle

No high-impact change should ship without explicit evidence of:

- Requirement alignment
- Security review
- Risk treatment
- Verification results
