import re

class VARKContentGenerator:
    def __init__(self):
        self.vark_strategies = {
            "visual": {"name": "Visual Learner", "icon": "👁️"},
            "auditory": {"name": "Auditory Learner", "icon": "👂"},
            "reading": {"name": "Reading/Writing Learner", "icon": "📝"},
            "kinesthetic": {"name": "Kinesthetic Learner", "icon": "🤸"}
        }

    def _sanitize_for_audio(self, text):
        """
        Membersihkan teks dari tanda hubung kata ulang dan simbol matematika
        agar tidak salah dibaca oleh TTS browser.
        """
        if not text:
            return ""
        
        # 1. Ubah kata ulang (huruf-huruf) menjadi spasi: konsep-konsep -> konsep konsep
        text = re.sub(r'([a-zA-Z])-([a-zA-Z])', r'\1 \2', text)
        
        # 2. Ubah simbol matematika menjadi kata-kata
        replacements = {
            '+': ' tambah ',
            '*': ' kali ',
            '/': ' bagi ',
            ':': ' bagi ',
            '=': ' sama dengan '
        }
        for sym, word in replacements.items():
            text = text.replace(sym, word)
            
        # 3. Tangani minus/kurang (hanya jika di antara angka)
        text = re.sub(r'(\d)-(\d)', r'\1 kurang \2', text)
        
        return ' '.join(text.split())

    def generate_auditory_content(self, topic, concept, difficulty):
        # Narasi asli dengan tanda hubung
        raw_script = (
            f"Mari kita bahas konsep-konsep dari {topic}. "
            f"Misalnya jika ada soal 10-5, kita melakukannya dengan cara hitung mundur."
        )
        
        # Bersihkan narasi untuk auditory
        clean_script = self._sanitize_for_audio(raw_script)

        content = {
            "type": "auditory",
            "title": f"🗣️ Penjelasan Verbal: {topic}",
            "elements": [
                {
                    "type": "verbal_explanation",
                    "title": "Penjelasan Lisan",
                    "script": clean_script
                },
                {
                    "type": "self_talk",
                    "title": "Tips Bicara Sendiri",
                    "tips": [
                        self._sanitize_for_audio("Ucapkan soalnya: Berapa 5+5?"),
                        "Jelaskan langkah-langkahnya dengan suara keras"
                    ]
                }
            ]
        }
        return content

    # ... (generate_visual_content dan method lainnya tetap sama)

    def generate_multimodal_content(self, topic, concept, difficulty, preferred_style="visual"):
        content = {"topic": topic, "preferred_style": preferred_style, "sections": []}
        
        if preferred_style == "auditory":
            content["sections"].append(self.generate_auditory_content(topic, concept, difficulty))
            # Tambahkan style lain sebagai pendukung
        else:
            # Logika style lainnya
            pass
            
        return content