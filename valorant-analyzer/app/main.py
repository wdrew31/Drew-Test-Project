from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from app.agents.vision import VisionAgent
from app.agents.audio import AudioAgent
from app.agents.coach import CoachAgent

app = FastAPI(title="Valorant Analyzer")

# Add CORS middleware to allow frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
vision = VisionAgent()
audio = AudioAgent()
coach = CoachAgent()

@app.post('/analyze/vod')
async def analyze_vod(file: UploadFile = File(...)):
    # stub: read file (not saving in scaffold)
    contents = await file.read()
    frames = vision.extract_frames_from_vod(contents)
    vis_events = vision.analyze_frames(frames)
    audio_events = audio.analyze_audio_blob(contents)
    advice = coach.generate_advice(vis_events, audio_events)
    return {
        'vision': vis_events,
        'audio': audio_events,
        'advice': advice,
    }

@app.post('/analyze/live')
async def analyze_live(payload: dict):
    # Stub for live analysis: accepts metadata and returns a placeholder
    return {'status': 'live analysis not yet implemented', 'payload': payload}
