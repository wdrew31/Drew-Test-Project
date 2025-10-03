// API Configuration
const API_BASE_URL = 'http://localhost:8002';

// DOM Elements
const uploadArea = document.getElementById('uploadArea');
const vodUpload = document.getElementById('vodUpload');
const uploadSection = document.getElementById('upload-section');
const resultsSection = document.getElementById('results-section');
const loadingOverlay = document.getElementById('loadingOverlay');
const newAnalysisBtn = document.getElementById('newAnalysisBtn');
const liveAnalysisBtn = document.getElementById('liveAnalysisBtn');

// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    initializeEventListeners();
});

function initializeEventListeners() {
    // Upload area click
    uploadArea.addEventListener('click', () => {
        vodUpload.click();
    });

    // File input change
    vodUpload.addEventListener('change', (e) => {
        handleFileSelect(e.target.files[0]);
    });

    // Drag and drop
    uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadArea.classList.add('dragover');
    });

    uploadArea.addEventListener('dragleave', () => {
        uploadArea.classList.remove('dragover');
    });

    uploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadArea.classList.remove('dragover');
        const file = e.dataTransfer.files[0];
        handleFileSelect(file);
    });

    // New analysis button
    newAnalysisBtn.addEventListener('click', () => {
        resetToUploadView();
    });

    // Live analysis button
    liveAnalysisBtn.addEventListener('click', () => {
        handleLiveAnalysis();
    });

    // Header buttons
    const headerUploadBtn = document.querySelector('.header-actions .btn-primary');
    const headerLiveBtn = document.querySelector('.header-actions .btn-secondary');
    
    if (headerUploadBtn) {
        headerUploadBtn.addEventListener('click', () => {
            vodUpload.click();
        });
    }
    
    if (headerLiveBtn) {
        headerLiveBtn.addEventListener('click', () => {
            handleLiveAnalysis();
        });
    }
}

async function handleFileSelect(file) {
    if (!file) return;

    // Validate file type
    const validTypes = ['video/mp4', 'video/avi', 'video/quicktime', 'video/x-matroska'];
    if (!validTypes.includes(file.type)) {
        showNotification('Please select a valid video file (MP4, AVI, MOV)', 'error');
        return;
    }

    // Validate file size (max 2GB)
    const maxSize = 2 * 1024 * 1024 * 1024;
    if (file.size > maxSize) {
        showNotification('File size must be less than 2GB', 'error');
        return;
    }

    // Upload and analyze
    await uploadAndAnalyze(file);
}

async function uploadAndAnalyze(file) {
    try {
        // Show loading overlay
        loadingOverlay.classList.add('active');

        // Create FormData
        const formData = new FormData();
        formData.append('file', file);

        // Send to backend
        const response = await fetch(`${API_BASE_URL}/analyze/vod`, {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Analysis failed');
        }

        const data = await response.json();

        // Hide loading and show results
        loadingOverlay.classList.remove('active');
        displayResults(data);

    } catch (error) {
        console.error('Analysis error:', error);
        loadingOverlay.classList.remove('active');
        showNotification('Failed to analyze VOD. Please try again.', 'error');
    }
}

function displayResults(data) {
    // Hide upload section, show results
    uploadSection.style.display = 'none';
    resultsSection.style.display = 'block';

    // Populate vision events
    const visionContainer = document.getElementById('visionEvents');
    visionContainer.innerHTML = '';
    
    if (data.vision && data.vision.length > 0) {
        data.vision.forEach(event => {
            const eventHTML = createVisionEventHTML(event);
            visionContainer.innerHTML += eventHTML;
        });
    } else {
        visionContainer.innerHTML = '<p style="color: var(--text-muted);">No vision events detected</p>';
    }

    // Populate audio events
    const audioContainer = document.getElementById('audioEvents');
    audioContainer.innerHTML = '';
    
    if (data.audio && data.audio.length > 0) {
        data.audio.forEach(event => {
            const eventHTML = createAudioEventHTML(event);
            audioContainer.innerHTML += eventHTML;
        });
    } else {
        audioContainer.innerHTML = '<p style="color: var(--text-muted);">No audio events detected</p>';
    }

    // Populate coaching advice
    const coachingContainer = document.getElementById('coachingAdvice');
    coachingContainer.innerHTML = '';
    
    if (data.advice) {
        const adviceHTML = createCoachingAdviceHTML(data.advice);
        coachingContainer.innerHTML = adviceHTML;
    } else {
        coachingContainer.innerHTML = '<p style="color: var(--text-muted);">No coaching insights available</p>';
    }

    // Scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function createVisionEventHTML(event) {
    if (!event.events || event.events.length === 0) return '';
    
    return event.events.map(e => `
        <div class="event-item">
            <div class="event-header">
                <span class="event-type">${formatEventType(e.type)}</span>
                <span class="event-time">Frame ${event.frame}</span>
            </div>
            <div class="event-details">
                ${e.ability ? `Ability: ${formatAbilityName(e.ability)}` : ''}
                ${e.player ? ` | Player: ${e.player}` : ''}
            </div>
        </div>
    `).join('');
}

function createAudioEventHTML(event) {
    return `
        <div class="event-item">
            <div class="event-header">
                <span class="event-type">${formatEventType(event.type)}</span>
                <span class="event-time">${event.time}s</span>
            </div>
            <div class="event-details">
                ${event.player ? `Player: ${event.player}` : ''}
                ${event.text ? `Message: "${event.text}"` : ''}
            </div>
        </div>
    `;
}

function createCoachingAdviceHTML(advice) {
    let html = '';
    
    if (advice.summary) {
        html += `
            <div class="advice-item">
                <span class="advice-icon">📊</span>
                <strong>Summary:</strong> ${advice.summary}
            </div>
        `;
    }
    
    if (advice.tips && advice.tips.length > 0) {
        advice.tips.forEach(tip => {
            html += `
                <div class="advice-item">
                    <span class="advice-icon">💡</span>
                    ${tip}
                </div>
            `;
        });
    }
    
    return html || '<p style="color: var(--text-muted);">No specific advice available</p>';
}

function formatEventType(type) {
    return type
        .split('_')
        .map(word => word.charAt(0).toUpperCase() + word.slice(1))
        .join(' ');
}

function formatAbilityName(ability) {
    return ability.charAt(0).toUpperCase() + ability.slice(1);
}

function resetToUploadView() {
    uploadSection.style.display = 'block';
    resultsSection.style.display = 'none';
    vodUpload.value = '';
}

async function handleLiveAnalysis() {
    try {
        loadingOverlay.classList.add('active');

        const response = await fetch(`${API_BASE_URL}/analyze/live`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                stream_url: 'placeholder',
                timestamp: new Date().toISOString()
            })
        });

        const data = await response.json();
        loadingOverlay.classList.remove('active');

        if (data.status === 'live analysis not yet implemented') {
            showNotification('Live analysis feature coming soon!', 'info');
        } else {
            showNotification('Live analysis started successfully', 'success');
        }

    } catch (error) {
        console.error('Live analysis error:', error);
        loadingOverlay.classList.remove('active');
        showNotification('Failed to start live analysis', 'error');
    }
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    
    // Add styles
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        padding: 1rem 1.5rem;
        background: ${type === 'error' ? 'var(--error)' : type === 'success' ? 'var(--success)' : 'var(--secondary)'};
        color: white;
        border-radius: var(--radius-sm);
        box-shadow: var(--shadow-lg);
        z-index: 10000;
        animation: slideIn 0.3s ease;
        max-width: 400px;
        font-weight: 500;
    `;

    // Add to document
    document.body.appendChild(notification);

    // Remove after 4 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 4000);
}

// Add notification animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(400px);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

// Handle navigation
document.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        
        // Remove active class from all links
        document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
        
        // Add active class to clicked link
        link.classList.add('active');
        
        // Handle navigation based on href
        const href = link.getAttribute('href');
        if (href === '#dashboard') {
            resetToUploadView();
        } else if (href === '#analyze') {
            resetToUploadView();
            setTimeout(() => {
                uploadArea.scrollIntoView({ behavior: 'smooth' });
            }, 100);
        }
    });
});

// Add smooth scroll behavior
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        }
    });
});

console.log('Valorant Analyzer Frontend Loaded');
console.log('API Base URL:', API_BASE_URL);
