from typing import List, Dict

class CoachAgent:
    def __init__(self):
        pass

    def generate_advice(self, vision_events: List[Dict], audio_events: List[Dict]) -> Dict:
        """Simple fusion logic: produce generic advice based on detected events."""
        advice = {'summary': 'No critical issues detected', 'tips': []}
        # If many ability casts of type 'smoke' by same player, suggest economy changes
        smoke_count = sum(1 for v in vision_events for e in v.get('events', []) if e.get('ability') == 'smoke')
        if smoke_count > 2:
            advice['tips'].append('Consider swapping some smoke usage for aggressive plays')
        # If audio shows footsteps near time of ability, suggest better spacing
        if any(a.get('type') == 'footstep' for a in audio_events):
            advice['tips'].append('Work on clearing angles and spacing when approaching sites')
        return advice
