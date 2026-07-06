# Lint/Format Failure Test

This adds a `black --check .` step to your CI workflow, plus a deliberately
badly-formatted file (`badly_formatted.py`) that will fail it.

## Why this test matters
Unlike the "nonexistent package" failure (which needs human judgment to fix),
a `black` formatting failure has exactly one correct, unambiguous fix:
run `black` on the file. This is the category of failure your AI Diagnoser
should mark as `safe_to_auto_fix=True`, since there's no ambiguity in what
the "fix" should look like.

## How to use
1. Copy `.github/workflows/ci.yml`, `requirements.txt`, and
   `badly_formatted.py` into your existing `ci-test-repo` (overwriting the
   first two, adding the third).
2. Commit and push.
3. The `pytest` step will pass, but the new `black --check .` step will
   fail — this triggers your AI Diagnoser.
4. Check the AI comment on the commit — you should now see
   `fix_category: lint_format` and (if your diagnosis prompt/logic is
   tuned correctly) `safe_to_auto_fix: True`.

## To fix it manually and get back to green
```
pip install black
black .
git add .
git commit -m "fix: apply black formatting"
git push
```
