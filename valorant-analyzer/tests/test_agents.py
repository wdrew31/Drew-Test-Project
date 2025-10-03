from app.agents.vision import VisionAgent
from app.agents.audio import AudioAgent
from app.agents.coach import CoachAgent
from app.agents.frontend import FrontendAgent
from app.agents.backend import BackendAgent
from app.agents.infra import InfraAgent

vision = VisionAgent()
audio = AudioAgent()
coach = CoachAgent()
frontend = FrontendAgent()
backend = BackendAgent()
infra = InfraAgent()


def test_vision_extract_and_analyze():
    frames = vision.extract_frames_from_vod(b'dummy')
    assert len(frames) == 5
    events = vision.analyze_frames(frames)
    assert isinstance(events, list)


def test_audio_analysis():
    events = audio.analyze_audio_blob(b'dummy')
    assert any(e['type'] == 'footstep' for e in events)


def test_coach_fusion():
    vis_events = vision.analyze_frames(vision.extract_frames_from_vod(b'dummy'))
    aud_events = audio.analyze_audio_blob(b'dummy')
    advice = coach.generate_advice(vis_events, aud_events)
    assert 'tips' in advice


def test_frontend_agent():
    comps = frontend.suggest_components('dashboard')
    assert any(c['name'] == 'Timeline' for c in comps)
    css = frontend.generate_css_snippet('MetricsCard')
    assert 'metrics-card' in css


def test_backend_agent():
    eps = backend.suggest_endpoints()
    assert any(e['path'] == '/api/v1/matches' for e in eps)
    schema = backend.example_model_schema()
    assert 'Match' in schema


def test_infra_agent():
    rec = infra.recommend_deployment()
    assert 'db' in rec
    ci = infra.ci_yaml_snippet()
    assert 'name: CI' in ci
