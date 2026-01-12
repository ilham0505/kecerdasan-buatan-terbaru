// ============================================
// TEXT-TO-SPEECH MODULE
// Untuk Auditory Learners - VARK Support
// ============================================

class TextToSpeech {
    constructor() {
        this.synth = window.speechSynthesis;
        this.isSpeaking = false;
        this.currentUtterance = null;
        
        // Check browser support
        if (!this.synth) {
            console.warn('Text-to-Speech not supported in this browser');
        }
        
        // Get Indonesian voice (if available)
        this.voices = [];
        this.loadVoices();
        
        // Load voices when they change (some browsers load async)
        if (speechSynthesis.onvoiceschanged !== undefined) {
            speechSynthesis.onvoiceschanged = () => this.loadVoices();
        }
    }
    
    loadVoices() {
        this.voices = this.synth.getVoices();
        
        // Try to find Indonesian voice
        this.indonesianVoice = this.voices.find(voice => 
            voice.lang === 'id-ID' || voice.lang.startsWith('id')
        );
        
        // Fallback to English if Indonesian not available
        if (!this.indonesianVoice) {
            this.indonesianVoice = this.voices.find(voice => 
                voice.lang === 'en-US' || voice.lang.startsWith('en')
            );
        }
        
        console.log('TTS voices loaded:', this.voices.length);
        if (this.indonesianVoice) {
            console.log('Using voice:', this.indonesianVoice.name);
        }
    }
    
    speak(text, options = {}) {
        // Stop current speech if any
        this.stop();
        
        if (!text || !this.synth) {
            console.warn('Cannot speak: no text or TTS not supported');
            return;
        }
        
        // Create utterance
        this.currentUtterance = new SpeechSynthesisUtterance(text);
        
        // Set voice
        if (this.indonesianVoice) {
            this.currentUtterance.voice = this.indonesianVoice;
        }
        
        // Set parameters
        this.currentUtterance.rate = options.rate || 0.9;  // Slightly slower for clarity
        this.currentUtterance.pitch = options.pitch || 1.0;
        this.currentUtterance.volume = options.volume || 1.0;
        
        // Set language
        this.currentUtterance.lang = options.lang || 'id-ID';
        
        // Event handlers
        this.currentUtterance.onstart = () => {
            this.isSpeaking = true;
            if (options.onStart) options.onStart();
            console.log('TTS started');
        };
        
        this.currentUtterance.onend = () => {
            this.isSpeaking = false;
            if (options.onEnd) options.onEnd();
            console.log('TTS ended');
        };
        
        this.currentUtterance.onerror = (event) => {
            console.error('TTS error:', event);
            this.isSpeaking = false;
            if (options.onError) options.onError(event);
        };
        
        // Speak!
        this.synth.speak(this.currentUtterance);
    }
    
    pause() {
        if (this.synth.speaking && !this.synth.paused) {
            this.synth.pause();
        }
    }
    
    resume() {
        if (this.synth.paused) {
            this.synth.resume();
        }
    }
    
    stop() {
        if (this.synth.speaking || this.synth.pending) {
            this.synth.cancel();
            this.isSpeaking = false;
        }
    }
    
    toggle(text, button) {
        if (this.isSpeaking) {
            this.stop();
            if (button) {
                button.innerHTML = '🔊 Dengarkan';
                button.classList.remove('speaking');
            }
        } else {
            this.speak(text, {
                onStart: () => {
                    if (button) {
                        button.innerHTML = '⏸️ Berhenti';
                        button.classList.add('speaking');
                    }
                },
                onEnd: () => {
                    if (button) {
                        button.innerHTML = '🔊 Dengarkan';
                        button.classList.remove('speaking');
                    }
                }
            });
        }
    }
}

// Create global TTS instance
const tts = new TextToSpeech();

// ============================================
// HELPER FUNCTIONS
// ============================================

/**
 * Add TTS button to element
 * @param {string} elementId - ID of element containing text
 * @param {string} buttonId - ID for the TTS button
 */
function addTTSButton(elementId, buttonId = null) {
    const element = document.getElementById(elementId);
    if (!element) return;
    
    const text = element.textContent || element.innerText;
    
    const button = document.createElement('button');
    button.className = 'tts-button';
    if (buttonId) button.id = buttonId;
    button.innerHTML = '🔊 Dengarkan';
    
    button.onclick = () => tts.toggle(text, button);
    
    // Insert button before the element
    element.parentNode.insertBefore(button, element);
}

/**
 * Add TTS to all sections with class 'tts-enabled'
 */
function enableTTSForAll() {
    const elements = document.querySelectorAll('.tts-enabled');
    elements.forEach((element, index) => {
        const text = element.textContent || element.innerText;
        
        // Create button
        const button = document.createElement('button');
        button.className = 'tts-button';
        button.innerHTML = '🔊 Dengarkan';
        button.onclick = () => tts.toggle(text, button);
        
        // Add button before element
        element.parentNode.insertBefore(button, element);
    });
}

/**
 * Speak text immediately (for Auditory learners)
 * @param {string} text - Text to speak
 * @param {boolean} autoplay - Auto-play on page load
 */
function speakForAuditory(text, autoplay = false) {
    if (!text) return;
    
    const container = document.createElement('div');
    container.className = 'auditory-player';
    container.innerHTML = `
        <button class="tts-play-button" id="auditoryPlayBtn">
            🔊 Putar Penjelasan Audio
        </button>
        <div class="audio-controls" style="display: none;">
            <button class="tts-control-btn" id="pauseBtn">⏸️ Jeda</button>
            <button class="tts-control-btn" id="stopBtn">⏹️ Stop</button>
            <span class="audio-status">Sedang memutar...</span>
        </div>
    `;
    
    // Insert at top of content
    const contentArea = document.querySelector('.content-area') || document.body;
    contentArea.insertBefore(container, contentArea.firstChild);
    
    const playBtn = document.getElementById('auditoryPlayBtn');
    const controls = container.querySelector('.audio-controls');
    const pauseBtn = document.getElementById('pauseBtn');
    const stopBtn = document.getElementById('stopBtn');
    
    playBtn.onclick = () => {
        tts.speak(text, {
            onStart: () => {
                playBtn.style.display = 'none';
                controls.style.display = 'flex';
            },
            onEnd: () => {
                playBtn.style.display = 'block';
                controls.style.display = 'none';
            }
        });
    };
    
    pauseBtn.onclick = () => {
        if (tts.synth.paused) {
            tts.resume();
            pauseBtn.innerHTML = '⏸️ Jeda';
        } else {
            tts.pause();
            pauseBtn.innerHTML = '▶️ Lanjut';
        }
    };
    
    stopBtn.onclick = () => {
        tts.stop();
        playBtn.style.display = 'block';
        controls.style.display = 'none';
    };
    
    // Auto-play if requested (for Auditory learners)
    if (autoplay) {
        // Delay to ensure page is loaded
        setTimeout(() => playBtn.click(), 500);
    }
}

/**
 * Read question aloud (for practice page)
 * @param {string} question - Question text
 */
function readQuestion(question) {
    const button = document.getElementById('readQuestionBtn');
    if (button) {
        tts.toggle(question, button);
    } else {
        tts.speak(question);
    }
}

/**
 * Read feedback aloud
 * @param {string} feedback - Feedback text
 */
function readFeedback(feedback) {
    // Clean HTML tags if present
    const cleanText = feedback.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim();
    tts.speak(cleanText);
}

// ============================================
// AUTO-INITIALIZATION
// ============================================

// When page loads
document.addEventListener('DOMContentLoaded', () => {
    console.log('TTS module loaded');
    
    // Check if user is Auditory learner
    const isAuditoryLearner = document.body.dataset.learningStyle === 'auditory';
    
    if (isAuditoryLearner) {
        console.log('Auditory learner detected - enabling auto-features');
        
        // Enable TTS for all marked sections
        enableTTSForAll();
        
        // Add special auditory banner
        const banner = document.createElement('div');
        banner.className = 'auditory-banner';
        banner.innerHTML = `
            <span class="banner-icon">👂</span>
            <span class="banner-text">Mode Auditory: Klik 🔊 untuk mendengarkan penjelasan</span>
        `;
        document.body.insertBefore(banner, document.body.firstChild);
    }
});

// Export for use in other scripts
window.TextToSpeech = TextToSpeech;
window.tts = tts;
window.speakForAuditory = speakForAuditory;
window.readQuestion = readQuestion;
window.readFeedback = readFeedback;
window.addTTSButton = addTTSButton;