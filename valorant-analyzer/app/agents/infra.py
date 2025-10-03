from typing import Dict

class InfraAgent:
    """Suggests infrastructure, deployment templates and CI snippets."""
    def __init__(self):
        pass

    def recommend_deployment(self) -> Dict:
        return {
            'platforms': ['Vercel (frontend)', 'Render/Heroku (backend)', 'S3 + CloudFront (static)'],
            'db': 'Postgres for match metadata, Redis for caching',
        }

    def ci_yaml_snippet(self) -> str:
        return (
            "name: CI\n\non: [push]\n\njobs:\n  test:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v3\n      - name: Set up Python\n        uses: actions/setup-python@v4\n        with:\n          python-version: '3.10'\n      - name: Install deps\n        run: pip install -r requirements.txt\n      - name: Run tests\n        run: pytest --maxfail=1 -q\n"
        )
