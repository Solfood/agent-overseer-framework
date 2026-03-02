#!/usr/bin/env python3

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    'README.md',
    'ADOPTION.md',
    'prompts/overseer-system-prompt.md',
    'docs/charter.md',
    'docs/operating-model.md',
    'docs/review-gates.md',
    'docs/engineering-fundamentals.md',
    'docs/security-baseline.md',
    'docs/risk-model.md',
    'docs/handoff-protocol.md',
    'templates/task-intake.md',
    'templates/decision-record.md',
    'templates/threat-model.md',
    'templates/release-readiness.md',
    'policies/overseer-policy.yaml',
    '.github/workflows/validate.yml',
]

REQUIRED_POLICY_KEYS = [
    'project_name:',
    'marker_prefix:',
    'risk_tolerance:',
    'critical_assets:',
    'mandatory_gates:',
]


def must_exist(rel: str) -> None:
    p = ROOT / rel
    if not p.exists():
        raise FileNotFoundError(f'missing required file: {rel}')


def must_contain(path: Path, needle: str) -> None:
    text = path.read_text(encoding='utf-8')
    if needle not in text:
        raise AssertionError(f'{path} missing expected text: {needle}')


def main() -> None:
    for f in REQUIRED_FILES:
        must_exist(f)

    policy = ROOT / 'policies/overseer-policy.yaml'
    for key in REQUIRED_POLICY_KEYS:
        must_contain(policy, key)

    prompt = ROOT / 'prompts/overseer-system-prompt.md'
    must_contain(prompt, 'Block unsafe releases')
    must_contain(prompt, 'language-agnostic engineering fundamentals')
    must_contain(prompt, 'Require evidence, not assertion')

    fundamentals = ROOT / 'docs/engineering-fundamentals.md'
    must_contain(fundamentals, 'languages and paradigms')
    must_contain(fundamentals, 'Correctness')
    print('OK: overseer framework validation passed')


if __name__ == '__main__':
    main()
