// ============================================
// TEXT-TO-SPEECH MODULE (FINAL INTEGRATION)
// ============================================

class TextToSpeech {
    constructor() {
        this.synth = window.speechSynthesis;
        this.isSpeaking = false;
        this.currentUtterance = null;
        this.voices = [];
        this.loadVoices();

        if (speechSynthesis.onvoiceschanged !== undefined) {
            speechSynthesis.onvoiceschanged = () => this.loadVoices();
        }
    }

    sanitizeText(text) {
        if (!text) return "";

        let cleaned = text.toString();

        cleaned = cleaned.replace(/([a-zA-Z])(-)([a-zA-Z])/g, "$1 $3");
        cleaned = cleaned.replace(/\+/g, " tambah ")
                         .replace(/\*/g, " kali ")
                         .replace(/x/g, " kali ")
                         .replace(/\//g, " bagi ")
                         .replace(/:/g, " bagi ")
                         .replace(/=/g, " sama dengan ")
                         .replace(/\^/g, " pangkat ");

        cleaned = cleaned.replace(/(\d)-(\d)/g, "$1 kurang $2");
        cleaned = cleaned.replace(/\s-\s/g, " kurang ");

        cleaned = cleaned.replace(/<[^>]*>/g, ' ');
        return cleaned.replace(/\s+/g, ' ').trim();
    }

    loadVoices() {
        this.voices = this.synth.getVoices();
        this.indonesianVoice = this.voices.find(v => 
            v.lang === 'id-ID' || v.lang.startsWith('id')
        );

        if (!this.indonesianVoice) {
            this.indonesianVoice = this.voices.find(v =>
                v.lang === 'en-US' || v.lang.startsWith('en')
            );
        }
    }

    speak(text, options = {}) {
        this.stop(); // prevent double speak

        if (!text || !this.synth) return;

        const cleanText = this.sanitizeText(text);
        console.log("TTS Reading:", cleanText);

        this.currentUtterance = new SpeechSynthesisUtterance(cleanText);

        if (this.indonesianVoice) {
            this.currentUtterance.voice = this.indonesianVoice;
        }

        this.currentUtterance.rate = options.rate || 0.85;
        this.currentUtterance.pitch = options.pitch || 1.0;
        this.currentUtterance.lang = options.lang || 'id-ID';

        this.currentUtterance.onstart = () => {
            this.isSpeaking = true;
            if (options.onStart) options.onStart();
        };

        this.currentUtterance.onend = () => {
            this.isSpeaking = false;
            if (options.onEnd) options.onEnd();
        };

        this.synth.speak(this.currentUtterance);
    }

    // stop biasa
    stop() {
        if (this.synth.speaking || this.synth.pending) {
            this.synth.cancel();
            this.isSpeaking = false;
        }
    }

    // dipanggil dari module lain → ex: emotion.js
    forceStop() {
        this.stop();
    }

    // toggle button system
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
                        button.innerHTML = '⏸ Berhenti';
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

// GLOBAL ACCESS
const tts = new TextToSpeech();
window.tts = tts;
