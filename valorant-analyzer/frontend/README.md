# Valorant Analyzer Frontend

An Overwolf-inspired frontend application for analyzing Valorant gameplay footage.

## Features

- **Dark Gaming Theme**: Sleek, modern UI inspired by Overwolf's design language
- **Drag & Drop Upload**: Easy VOD file upload with drag and drop support
- **Real-time Analysis**: Integration with backend API for video analysis
- **Interactive Results**: Visual display of vision events, audio events, and coaching insights
- **Responsive Design**: Works on desktop and mobile devices
- **Live Analysis**: Support for real-time gameplay analysis (coming soon)

## Design Principles

The frontend follows Overwolf's design philosophy:
- Dark background (#0A0B0F) for reduced eye strain during gaming sessions
- Bold gradient accents (Red to Purple: #FF4655 → #8B5CF6)
- Clear typography with Inter font family
- Smooth animations and transitions
- Gaming-centric UI patterns

## Color Palette

- **Primary**: #FF4655 (Red)
- **Secondary**: #8B5CF6 (Purple)
- **Background**: #0A0B0F (Dark Navy)
- **Surface**: #13141A / #1A1B23 (Dark Gray)
- **Text**: #FFFFFF / #B4B5BD / #6B6C7A

## File Structure

```
frontend/
├── index.html      # Main HTML structure
├── styles.css      # Overwolf-inspired styling
├── app.js          # JavaScript functionality & API integration
└── README.md       # This file
```

## Getting Started

### Prerequisites

- Backend server running on `http://localhost:8002`
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Running the Frontend

1. **Start the Backend Server**:
   ```bash
   cd ../
   uvicorn app.main:app --reload --port 8002
   ```

2. **Open the Frontend**:
   ```bash
   # Simple HTTP server with Python
   python3 -m http.server 8000
   
   # Or use any local server
   # Then visit: http://localhost:8000
   ```

3. **Alternative - Direct File Access**:
   ```bash
   # Open directly in browser (may have CORS limitations)
   open index.html
   ```

## Usage

### Upload and Analyze a VOD

1. Click the upload area or drag and drop a video file
2. Supported formats: MP4, AVI, MOV (max 2GB)
3. Wait for analysis to complete
4. View results in three categories:
   - Vision Analysis (ability casts, player positions)
   - Audio Analysis (footsteps, callouts)
   - Coaching Insights (actionable advice)

### Live Analysis

1. Click "Live Analysis" button
2. Feature is currently in development
3. Will support real-time gameplay analysis

## API Integration

The frontend communicates with the FastAPI backend:

- `POST /analyze/vod` - Upload and analyze VOD files
- `POST /analyze/live` - Start live analysis session

## Customization

### Changing Colors

Edit the CSS variables in `styles.css`:

```css
:root {
    --primary: #FF4655;
    --secondary: #8B5CF6;
    --background: #0A0B0F;
    /* ... */
}
```

### Changing API URL

Edit the API configuration in `app.js`:

```javascript
const API_BASE_URL = 'http://localhost:8002';
```

## Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Responsive Breakpoints

- Desktop: 1400px+
- Tablet: 768px - 1399px
- Mobile: < 768px

## Performance

- Minimal JavaScript dependencies (vanilla JS)
- Optimized CSS animations
- Lazy loading for analysis results
- Efficient DOM manipulation

## Future Enhancements

- [ ] Match history page
- [ ] Detailed statistics dashboard
- [ ] Player profile system
- [ ] Comparison tools
- [ ] Video playback with overlay
- [ ] Real-time coaching during gameplay
- [ ] Export analysis reports

## Credits

Design inspired by [Overwolf](https://www.overwolf.com/) - The guild of in-game creators.
