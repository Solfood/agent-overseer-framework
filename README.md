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
- Language-agnostic engineering fundamentals baseline
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

## Companion Framework

Use this together with `engineering-scaffold-template` so governance controls are applied to a concrete execution workflow.

- Companion repo: https://github.com/Solfood/engineering-scaffold-template
- Integration guide: `docs/paired-with-engineering-scaffold.md`


## Start New Project (Human Bootstrap)

```bash
mkdir -p <new-project> && cd <new-project>
git init

# Pull execution scaffold
git clone https://github.com/Solfood/engineering-scaffold-template.git .tmp-engineering
rsync -a .tmp-engineering/ ./
rm -rf .tmp-engineering

# Pull overseer framework
git clone https://github.com/Solfood/agent-overseer-framework.git .overseer
```

Then run:

```bash
python3 tools/validate_template_scaffold.py
python3 .overseer/tools/validate_overseer_framework.py
```

## Continuation Prompt

- Use `docs/new-chat-continuation-prompt.md` for governance-aware continuity in new chats.
