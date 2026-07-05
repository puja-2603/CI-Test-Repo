# CI Test Repo — for the AI Diagnoser

This is a minimal repo whose only job is to give your AI CI/CD Diagnoser
something real to diagnose.

## First push (should PASS)
Push this exactly as-is. The `CI` workflow will run and pass — this
confirms your GitHub Actions setup and webhook registration are wired up
correctly before you break anything on purpose.

## Second push (trigger a real failure)
Edit `requirements.txt` and change:
```
pytest==8.3.3
requests==2.32.3
```
to:
```
pytest==8.3.3
requests==2.32.3
nonexistentpackage123==1.0.0
```

Commit and push. This workflow run will **fail** at the "Install
dependencies" step, since that package doesn't exist on PyPI — exactly
the kind of failure your AI Diagnoser is built to catch and explain.

## Other failure types to try later
- **Flaky/logic failure**: change `assert 1 + 1 == 2` to `assert 1 + 1 == 3`
  in `test_sample.py` — this tests how the AI handles an actual test
  failure vs. a dependency failure.
- **Lint/format failure**: add a `flake8` or `black --check` step to the
  workflow and commit badly-formatted code, to test the `lint_format`
  fix category.

## Webhook setup reminder
Settings → Webhooks → Add webhook:
- Payload URL: `https://<your-deployed-backend>/webhook`
- Content type: `application/json`
- Secret: same value as `GITHUB_WEBHOOK_SECRET` in your backend
- Events: select **only** "Workflow runs"
