from typing import Dict, List

class BackendAgent:
    """Provides API design, data model suggestions, and example endpoints."""
    def __init__(self):
        pass

    def suggest_endpoints(self) -> List[Dict]:
        return [
            {'path': '/api/v1/matches', 'method': 'GET', 'purpose': 'List analyzed matches'},
            {'path': '/api/v1/matches', 'method': 'POST', 'purpose': 'Upload and analyze a VOD'},
            {'path': '/api/v1/live', 'method': 'POST', 'purpose': 'Start live analysis session'},
        ]

    def example_model_schema(self) -> Dict:
        return {
            'Match': {
                'id': 'string',
                'started_at': 'datetime',
                'players': [{'id': 'string', 'name': 'string', 'team': 'string'}],
            }
        }

    def generate_express_route_stub(self, path: str) -> str:
        return f"app.post('{path}', async (req, res) => {{ res.json({{status: 'ok'}}) }})"
