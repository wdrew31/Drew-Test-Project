from typing import Dict, List

class FrontendAgent:
    """Provides UI/UX suggestions, component scaffolds and CSS snippets."""
    def __init__(self):
        pass

    def suggest_components(self, screen_purpose: str) -> List[Dict]:
        """Return a small list of suggested components for a given screen purpose."""
        if 'dashboard' in screen_purpose.lower():
            return [
                {'name': 'Header', 'purpose': 'Top navigation and branding'},
                {'name': 'MetricsCard', 'purpose': 'Show match KPIs (kills, accuracy, ADR)'},
                {'name': 'Timeline', 'purpose': 'Show events over time (abilities, kills)'}
            ]
        return [{'name': 'Container', 'purpose': 'Generic layout container'}]

    def generate_css_snippet(self, component_name: str) -> str:
        """Return a small CSS/Tailwind snippet for the named component."""
        if component_name == 'MetricsCard':
            return ".metrics-card { padding: 12px; border-radius: 8px; background: var(--card-bg); }"
        return f"/* styles for {component_name} */"

    def create_react_component_stub(self, component_name: str) -> str:
        """Return a tiny React functional component scaffold as string."""
        return f"function {component_name}() {{\n  return (<div className=\"{component_name.lower()}\">{component_name}</div>)\n}}\nexport default {component_name}\n"
