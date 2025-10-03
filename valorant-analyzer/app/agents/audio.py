from typing import List, Dict

class AudioAgent:
    def __init__(self):
        pass

    def analyze_audio_blob(self, vod_bytes: bytes) -> List[Dict]:
        """Stub: return fake audio events (footsteps, callouts). Replace with VAD/ASR."""
        return [{'time': 1.2, 'type': 'footstep', 'player': 'player2'}, {'time': 3.4, 'type': 'callout', 'text': 'rotating'}]
