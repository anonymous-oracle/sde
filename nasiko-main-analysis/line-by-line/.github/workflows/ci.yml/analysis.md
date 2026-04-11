# ci.yml — line-by-line analysis

## Lines 1-8
- Defines CI workflow triggers on main push and PRs.

## Lines 9-16
- Lint job uses checkout, setup-python 3.12, installs black/mypy.

## Lines 17-24
- Runs black check and starts typecheck job.

## Lines 25-33
- Typecheck job repeats setup and runs mypy with ignore-missing-imports.
