# Valorant Analyzer

A multi-agent system for analyzing Valorant gameplay from VODs or live streams. Features an Overwolf-inspired frontend and extensible backend architecture.

## Features

### Frontend (Overwolf-inspired)
- 🎮 **Gaming-First Design**: Dark theme with bold gradients inspired by Overwolf
- 📤 **Drag & Drop Upload**: Easy VOD file upload interface
- 📊 **Interactive Results**: Visual display of analysis across multiple categories
- 📱 **Responsive**: Works on desktop, tablet, and mobile
- ⚡ **Real-time Updates**: Live analysis support (coming soon)

### Backend (Multi-Agent System)
- 👁️ **Vision Agent**: Frame-based object/ability detection and player positioning
- 🔊 **Audio Agent**: Voice/footsteps/ability sound extraction with timestamps
- 🎯 **Coach Agent**: Fuses vision+audio data for tactical coaching advice
- 🎨 **Frontend Agent**: UI/UX suggestions and component generation
- 🔧 **Backend Agent**: API design and data model recommendations
- 🚀 **Infra Agent**: Deployment and CI/CD configuration

## Quick Start

### 1. Install Backend Dependencies

```bash
# Create virtual environment (Python 3.10+)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install with Poetry (recommended)
poetry install

# Or with pip
pip install fastapi uvicorn python-multipart
```

### 2. Start the Backend Server

```bash
uvicorn app.main:app --reload --port 8002
```

The API will be available at `http://localhost:8002`

### 3. Launch the Frontend

```bash
cd frontend

# Option 1: Python HTTP server
python3 -m http.server 8000

# Option 2: Node.js http-server (if installed)
npx http-server -p 8000

# Option 3: Direct file access
open index.html  # macOS
start index.html  # Windows
```

Visit `http://localhost:8000` in your browser.

## Project Structure

```
valorant-analyzer/
├── app/
│   ├── main.py              # FastAPI application
│   └── agents/              # Multi-agent system
│       ├── vision.py        # Vision analysis
│       ├── audio.py         # Audio analysis
│       ├── coach.py         # Coaching insights
│       ├── frontend.py      # Frontend suggestions
│       ├── backend.py       # Backend design
│       └── infra.py         # Infrastructure config
├── frontend/
│   ├── index.html           # Main UI
│   ├── styles.css           # Overwolf-inspired styling
│   ├── app.js               # Frontend logic
│   └── README.md            # Frontend docs
├── tests/
│   └── test_agents.py       # Agent tests
├── pyproject.toml           # Dependencies
└── README.md                # This file
```

## API Endpoints

### POST /analyze/vod
Upload and analyze a VOD file.

**Request**: Multipart form data with video file
**Response**:
```json
{
  "vision": [...],      // Detected visual events
  "audio": [...],       // Audio events with timestamps
  "advice": {...}       // Coaching recommendations
}
```

### POST /analyze/live
Start live analysis session (currently stubbed).

**Request**: JSON with stream metadata
**Response**: Status and session info

## Usage

### Analyzing a VOD

1. Open the frontend in your browser
2. Drag and drop a video file or click to browse
3. Wait for analysis to complete
4. Review the results:
   - **Vision Events**: Ability casts, player positions
   - **Audio Events**: Footsteps, callouts
   - **Coaching Insights**: Tactical advice

### Current Limitations (Stubs)

The current implementation uses placeholder data. To extend:

- **Vision Agent**: Integrate ffmpeg + YOLO/Detectron2 for real detection
- **Audio Agent**: Add Whisper or VAD for audio processing
- **Live Analysis**: Implement WebSocket support for real-time streaming
- **Persistence**: Add database for match history
- **ML Models**: Train custom models on Valorant-specific data

## Testing

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_agents.py -v

# Run with coverage
pytest --cov=app tests/
```

## Development

### Adding New Agents

1. Create new agent class in `app/agents/`
2. Add initialization in `app/main.py`
3. Add tests in `tests/test_agents.py`
4. Update API endpoints as needed

### Frontend Customization

See [frontend/README.md](frontend/README.md) for:
- Color customization
- Component modification
- API integration details

## Roadmap

### Phase 1 (Current - Scaffold) ✅
- [x] Multi-agent backend structure
- [x] Overwolf-inspired frontend
- [x] Basic API integration
- [x] Stub implementations

### Phase 2 (ML Integration)
- [ ] Integrate ffmpeg for frame extraction
- [ ] Add YOLO/Detectron2 for vision detection
- [ ] Implement Whisper for audio analysis
- [ ] Custom Valorant ability detection models

### Phase 3 (Real-time)
- [ ] WebSocket support for live analysis
- [ ] Low-latency streaming pipeline
- [ ] Real-time coaching overlay

### Phase 4 (Production)
- [ ] Database integration (PostgreSQL)
- [ ] User authentication
- [ ] Match history and profiles
- [ ] Advanced statistics dashboard
- [ ] Deployment configuration

## Tech Stack

- **Backend**: FastAPI, Python 3.10+
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **Styling**: Custom CSS (Overwolf-inspired)
- **Future**: PyTorch, YOLO, Whisper, FFmpeg

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This is a starter scaffold for educational and development purposes.

## Credits

- Frontend design inspired by [Overwolf](https://www.overwolf.com/)
- Built with FastAPI and modern web technologies
