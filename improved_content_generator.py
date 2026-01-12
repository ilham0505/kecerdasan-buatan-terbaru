import json
import random
from expanded_content_bank import ExpandedContentBank
from vark_learning_styles import VARKContentGenerator

class ImprovedContentGenerator:
    """
    Enhanced Content Generator dengan:
    - Expanded question bank
    - VARK learning styles integration
    - Better material generation
    - Adaptive hints system
    """
    
    def __init__(self):
        self.expanded_bank = ExpandedContentBank()
        self.vark_generator = VARKContentGenerator()
        
        # Default learning style (bisa dideteksi dari interaction history)
        self.default_learning_style = "visual"
        
    def generate_learning_content(self, topic_name, topic_description, 
                                  knowledge_level, attempts, learning_style=None):
        """
        Generate konten pembelajaran yang disesuaikan dengan:
        - Knowledge level (basic/intermediate/advanced)
        - Learning style (VARK)
        - Number of attempts (untuk determine approach)
        """
        # Determine content level
        if knowledge_level < 0.3:
            level = "basic"
        elif knowledge_level < 0.6:
            level = "intermediate"
        else:
            level = "advanced"
        
        # Use provided learning style or default
        style = learning_style or self.default_learning_style
        
        # Get base material from expanded bank
        base_material = self.expanded_bank.get_learning_material(topic_name, level)
        
        # Template konten
        content = {
            "title": f"Belajar {topic_name}",
            "level": level,
            "learning_style": style,
            "sections": []
        }
        
        # Section 1: Introduction
        if base_material.get("introduction"):
            content["sections"].append({
                "type": "introduction",
                "title": f"Apa itu {topic_name}?",
                "content": base_material["introduction"]
            })
        
        # Section 2: Core Concepts
        if base_material.get("concepts"):
            concepts_text = "\n• ".join([""] + base_material["concepts"])
            content["sections"].append({
                "type": "concept",
                "title": "Konsep Dasar",
                "content": f"Konsep-konsep penting:{concepts_text}"
            })
        
        # Section 3: Strategies
        if base_material.get("strategies"):
            strategies_text = "\n\n".join([f"**Strategi {i+1}**: {s}" 
                                          for i, s in enumerate(base_material.get("strategies", []))])
            content["sections"].append({
                "type": "strategy",
                "title": "Strategi Penyelesaian",
                "content": strategies_text
            })
        
        # Section 4: Examples
        if base_material.get("examples"):
            examples_text = "\n\n".join([f"**Contoh {i+1}**: {ex}" 
                                        for i, ex in enumerate(base_material.get("examples", []))])
            content["sections"].append({
                "type": "example",
                "title": "Contoh Soal",
                "content": examples_text
            })
        
        # Section 5: VARK-specific content
        vark_content = self.vark_generator.generate_multimodal_content(
            topic_name, 
            base_material, 
            int(knowledge_level * 5) + 1,
            style
        )
        
        # Add primary VARK section
        if vark_content["sections"]:
            primary_section = vark_content["sections"][0]
            content["sections"].append({
                "type": f"vark_{style}",
                "title": primary_section["title"],
                "content": self._format_vark_section(primary_section)
            })
        
        # Add tips based on struggles
        if attempts > 3 or knowledge_level < 0.4:
            content["sections"].append({
                "type": "tips",
                "title": "💡 Tips Khusus Untukmu",
                "content": self._get_personalized_tips(topic_name, knowledge_level, attempts)
            })
        
        return content
    
    def _format_vark_section(self, section):
        """Format VARK section untuk display"""
        formatted = []
        
        for element in section.get("elements", []):
            formatted.append(f"**{element.get('title', '')}**\n")
            
            if element.get("description"):
                formatted.append(element["description"] + "\n")
            
            if element.get("visual_aids"):
                formatted.append("\n".join(element["visual_aids"]) + "\n")
            
            if element.get("activities"):
                for activity in element["activities"]:
                    formatted.append(f"• {activity}")
            
            if element.get("tips"):
                for tip in element["tips"]:
                    formatted.append(f"• {tip}")
            
            formatted.append("\n")
        
        return "\n".join(formatted)
    
    def _get_personalized_tips(self, topic_name, knowledge_level, attempts):
        """Generate personalized tips based on performance"""
        tips = []
        
        if attempts > 5:
            tips.append("🌟 Jangan berkecil hati! Belajar membutuhkan waktu dan setiap orang punya kecepatannya sendiri.")
        
        if knowledge_level < 0.3:
            tips.append("📚 Fokus pada memahami konsep dasar dulu sebelum ke soal yang lebih rumit.")
            tips.append("🐢 Tidak perlu terburu-buru - pahami setiap langkah dengan baik.")
        
        if knowledge_level < 0.5:
            tips.append("✍️ Coba tulis ulang rumus dan contoh dengan kata-katamu sendiri.")
            tips.append("🎯 Latihan soal-soal mudah dulu sampai benar-benar paham.")
        
        # Topic-specific tips
        topic_tips = {
            "Penjumlahan Dasar": "Gunakan jari atau gambar untuk membantu visualisasi!",
            "Perkalian Dasar": "Hafalkan tabel perkalian sedikit demi sedikit, mulai dari yang mudah.",
            "Geometri Dasar": "Selalu gambar bangun datarnya dulu agar lebih jelas!",
            "Aljabar Sederhana": "Bayangkan variabel sebagai kotak misteri yang harus kita buka!",
        }
        
        if topic_name in topic_tips:
            tips.append(topic_tips[topic_name])
        
        return "\n\n".join(tips)
    
    def generate_question(self, topic_name, difficulty, knowledge_level, learning_style=None):
        """
        Generate soal dengan expanded question bank
        """
        # Get questions from expanded bank
        questions = self.expanded_bank.get_questions(topic_name, difficulty)
        
        if not questions:
            # Fallback to generated question
            return self._generate_fallback_question(topic_name, difficulty)
        
        # Pick random question
        q_data = random.choice(questions)
        
        # Enhance with learning style specific hints
        style = learning_style or self.default_learning_style
        hints = self._generate_vark_hints(q_data, style, difficulty)
        
        return {
            'question': q_data['q'],
            'answer': q_data['a'],
            'explanation': q_data['exp'],
            'difficulty': difficulty,
            'hints': hints,
            'learning_style': style
        }
    
    def _generate_vark_hints(self, question_data, style, difficulty):
        """Generate hints based on learning style"""
        hints = []
        question_text = question_data['q']
        answer = question_data['a']
        
        if style == "visual":
            hints.append("💡 Hint 1 (Visual): Coba gambarkan soal ini dengan diagram atau objek")
            hints.append(f"💡 Hint 2 (Visual): Gunakan garis bilangan atau array untuk visualisasi")
            hints.append(f"💡 Hint 3 (Visual): Jawabannya ada di range {max(0, int(answer)-3)} - {int(answer)+3}")
        
        elif style == "auditory":
            hints.append("💡 Hint 1 (Auditory): Baca soal dengan suara keras dan jelaskan apa yang ditanyakan")
            hints.append("💡 Hint 2 (Auditory): Verbalkan setiap langkah penyelesaian")
            hints.append(f"💡 Hint 3 (Auditory): Coba jelaskan ke diri sendiri mengapa jawabannya sekitar {answer}")
        
        elif style == "reading":
            hints.append("💡 Hint 1 (Reading): Baca soal dengan teliti, identifikasi operasi yang diminta")
            hints.append("💡 Hint 2 (Reading): Tulis langkah-langkah penyelesaian secara terstruktur")
            hints.append(f"💡 Hint 3 (Reading): Periksa kembali perhitungan, pastikan tidak ada kesalahan tulis")
        
        elif style == "kinesthetic":
            hints.append("💡 Hint 1 (Kinesthetic): Gunakan jari, benda nyata, atau gerakan untuk menghitung")
            hints.append("💡 Hint 2 (Kinesthetic): Praktikkan dengan objek di sekitarmu")
            hints.append("💡 Hint 3 (Kinesthetic): Lakukan perhitungan sambil bergerak atau menggunakan alat bantu")
        
        return hints
    
    def _generate_fallback_question(self, topic_name, difficulty):
        """Fallback question generator jika bank kosong"""
        if "Penjumlahan" in topic_name:
            if difficulty <= 2:
                a = random.randint(1, 10)
                b = random.randint(1, 10)
            else:
                a = random.randint(10, 100)
                b = random.randint(10, 100)
            
            result = a + b
            return {
                'question': f"{a} + {b} = ?",
                'answer': str(result),
                'explanation': f"{a} ditambah {b} sama dengan {result}",
                'difficulty': difficulty,
                'hints': [
                    f"💡 Mulai dari {a}, lalu tambah {b}",
                    f"💡 Hasilnya sekitar {(result//10)*10}",
                    f"💡 Jawaban pastinya adalah {result}"
                ]
            }
        
        # Default fallback
        return {
            'question': f"Soal {topic_name} (Level {difficulty})",
            'answer': "42",
            'explanation': "Contoh soal",
            'difficulty': difficulty,
            'hints': ["Coba baca soal dengan teliti"]
        }
    
    def generate_feedback(self, is_correct, question_data, user_answer, 
                         emotion, knowledge_level):
        """
        Generate personalized feedback dengan mempertimbangkan:
        - Correctness
        - Emotion
        - Knowledge level
        - Learning style
        """
        feedback = ""
        
        if is_correct:
            # Positive feedback dengan variasi
            positive_msgs = [
                "🎉 Sempurna! Jawabanmu tepat sekali!",
                "✨ Luar biasa! Kamu menguasainya!",
                "👏 Hebat! Pemahaman mu sangat baik!",
                "⭐ Bagus sekali! Teruskan!",
                "🌟 Bravo! Kamu pintar!",
                "💯 Perfect! Jawabanmu 100% benar!",
            ]
            feedback = random.choice(positive_msgs)
            
            # Emotional support
            if emotion in ['frustrated', 'confused', 'anxious']:
                feedback += "\n\n💪 Lihat, kamu BISA! Jangan ragu dengan kemampuanmu. Terus semangat!"
            elif emotion in ['confident', 'happy', 'motivated']:
                feedback += "\n\n🚀 Momentum mu sangat bagus! Pertahankan fokus dan semangat ini!"
            
            # Knowledge-based encouragement
            if knowledge_level > 0.7:
                feedback += "\n\n🏆 Level pemahamanmu sudah sangat tinggi! Kamu siap untuk tantangan lebih besar!"
        
        else:
            # Constructive feedback
            encouraging_msgs = [
                "Tidak apa-apa salah, itu bagian dari proses belajar! ",
                "Hampir benar! Sedikit lagi kamu akan menguasainya. ",
                "Bagus sudah berani mencoba! ",
                "Setiap kesalahan adalah kesempatan untuk belajar! ",
                "Terus semangat! Kamu sedang dalam proses belajar yang baik. ",
            ]
            feedback = random.choice(encouraging_msgs)
            
            # Add explanation
            feedback += f"\n\n📖 **Penjelasan**:\n"
            feedback += f"Jawaban yang benar adalah **{question_data['answer']}**.\n\n"
            feedback += question_data.get('explanation', '')
            
            # Emotional support berdasarkan kondisi
            if emotion in ['frustrated', 'anxious', 'stressed']:
                feedback += "\n\n🌈 **Tenang ya!** Semua orang pernah salah berkali-kali sebelum akhirnya berhasil."
                feedback += " Matematika butuh latihan, dan kamu sedang di jalur yang benar!"
                feedback += "\n\n💝 Sistem akan menyesuaikan pembelajaran agar lebih nyaman untukmu."
            
            elif emotion == 'confused':
                feedback += "\n\n🤔 **Mari kita coba jelaskan dengan cara berbeda**:"
                feedback += "\n• Baca soal sekali lagi dengan pelan"
                feedback += "\n• Identifikasi apa yang diketahui dan apa yang ditanyakan"
                feedback += "\n• Ikuti langkah-langkah yang sudah dipelajari"
            
            # Knowledge-based support
            if knowledge_level < 0.3:
                feedback += "\n\n📚 **Tip untuk pemula**: Tidak perlu terburu-buru. Pahami konsep dasarnya dulu, lalu coba latihan yang mudah-mudah. Sistem akan membantu mu step by step!"
        
        return feedback
    
    def generate_review_content(self, topic_name, knowledge_level, learning_style=None):
        """Generate review/summary content with VARK adaptation"""
        style = learning_style or self.default_learning_style
        
        # Get base material
        level = "basic" if knowledge_level < 0.5 else "intermediate"
        base_material = self.expanded_bank.get_learning_material(topic_name, level)
        
        content = {
            "title": f"Review: {topic_name}",
            "type": "review",
            "learning_style": style,
            "sections": []
        }
        
        # Key points section
        key_points = self._get_key_points(topic_name)
        content["sections"].append({
            "title": "📌 Poin-Poin Penting",
            "content": key_points
        })
        
        # Examples section
        if base_material.get("examples"):
            examples_text = "\n\n".join(base_material["examples"][:3])  # Top 3 examples
            content["sections"].append({
                "title": "📝 Contoh-Contoh Utama",
                "content": examples_text
            })
        
        # VARK-specific review
        if style == "visual":
            content["sections"].append({
                "title": "👁️ Visual Summary",
                "content": "Coba buat mind map atau diagram dari konsep-konsep yang sudah dipelajari!"
            })
        elif style == "auditory":
            content["sections"].append({
                "title": "👂 Audio Review",
                "content": "Coba jelaskan kembali materi ini dengan suara keras, seolah kamu mengajarkan ke teman!"
            })
        elif style == "reading":
            content["sections"].append({
                "title": "📖 Reading Summary",
                "content": "Buat catatan ringkasan dengan kata-katamu sendiri. Tulis poin-poin penting!"
            })
        elif style == "kinesthetic":
            content["sections"].append({
                "title": "🤸 Practice Review",
                "content": "Praktikkan konsep-konsep ini dengan benda nyata atau aktivitas hands-on!"
            })
        
        # Quick practice
        content["sections"].append({
            "title": "⚡ Latihan Singkat",
            "content": "Mari coba beberapa soal mudah untuk refresh ingatan!"
        })
        
        return content
    
    def _get_key_points(self, topic_name):
        """Get key points summary"""
        points = {
            "Penjumlahan Dasar": """
• Penjumlahan menggabungkan dua bilangan atau lebih
• Urutan tidak mempengaruhi hasil (sifat komutatif)
• Strategi: counting on, make ten, decomposition
• Selalu cek jawaban dengan cara berbeda
            """,
            "Pengurangan Dasar": """
• Pengurangan adalah kebalikan dari penjumlahan
• Selalu kurangi bilangan kecil dari bilangan besar
• Gunakan garis bilangan untuk membantu
• Cek dengan penjumlahan: hasil + pengurang = bilangan awal
            """,
            "Perkalian Dasar": """
• Perkalian = penjumlahan berulang
• Hafalkan tabel perkalian 1-10
• Sifat komutatif: a × b = b × a
• Gunakan strategi: doubling, skip counting, distributive
            """,
            "Pembagian Dasar": """
• Pembagian adalah kebalikan perkalian
• Format: dividend ÷ divisor = quotient
• Cek dengan perkalian: quotient × divisor = dividend
• Ingat: bilangan dibagi 1 = bilangan itu sendiri
            """,
            "Pecahan": """
• Pecahan terdiri dari pembilang dan penyebut
• Penjumlahan/pengurangan: samakan penyebut dulu
• Perkalian: kalikan pembilang dengan pembilang, penyebut dengan penyebut
• Sederhanakan hasil jika memungkinkan
            """,
            "Geometri Dasar": """
• Setiap bangun punya rumus keliling dan luas sendiri
• Keliling = jumlah semua sisi
• Luas = ukuran bidang yang tertutup
• Selalu beri label pada gambar (sisi, sudut, dll)
            """,
            "Aljabar Sederhana": """
• Variabel (x, y) mewakili bilangan yang belum diketahui
• Selesaikan dengan isolasi variabel
• Kedua ruas persamaan harus seimbang
• Selalu cek jawaban dengan substitusi kembali
            """
        }
        
        return points.get(topic_name, f"Konsep utama dari {topic_name}")
    
    def generate_session_insights(self, topic_name, attempted, correct, 
                                  knowledge_level, emotions):
        """Generate insights dari learning session dengan analisis lebih dalam"""
        accuracy = (correct / attempted * 100) if attempted > 0 else 0
        
        insights = []
        
        # Performance insight dengan kategori lebih detail
        if accuracy >= 90:
            insights.append("🏆 **Performa Luar Biasa!** Kamu menguasai materi ini dengan sangat baik. Ini adalah pencapaian yang membanggakan!")
        elif accuracy >= 80:
            insights.append("🎯 **Performa Excellent!** Pemahaman mu sudah sangat baik. Sedikit polish lagi akan sempurna!")
        elif accuracy >= 70:
            insights.append("👍 **Performa Bagus!** Kamu sudah memahami sebagian besar konsep. Terus berlatih untuk mengkonsolidasikan pengetahuan!")
        elif accuracy >= 60:
            insights.append("📈 **Performa Berkembang!** Ada progress yang baik. Fokus pada area yang masih challenging.")
        elif accuracy >= 40:
            insights.append("💪 **Tetap Semangat!** Kamu sedang dalam proses belajar. Setiap usaha adalah langkah maju!")
        else:
            insights.append("🌱 **Perjalanan Baru Dimulai!** Tidak apa-apa memulai dari nol. Yang penting adalah komitmen untuk terus belajar!")
        
        # Knowledge level insight
        if knowledge_level >= 0.9:
            insights.append("🌟 **Level Penguasaan: MASTER** - Kamu sudah benar-benar menguasai topik ini! Siap jadi mentor untuk yang lain!")
        elif knowledge_level >= 0.8:
            insights.append("⭐ **Level Penguasaan: MAHIR** - Excellent! Sudah siap untuk topik yang lebih menantang!")
        elif knowledge_level >= 0.7:
            insights.append("📊 **Level Penguasaan: KOMPETEN** - Bagus! Pemahaman mu sudah solid.")
        elif knowledge_level >= 0.6:
            insights.append("📈 **Level Penguasaan: BAIK** - Terus tingkatkan dengan lebih banyak latihan!")
        elif knowledge_level >= 0.4:
            insights.append("📚 **Level Penguasaan: BERKEMBANG** - Kamu sedang di jalur yang benar. Terus belajar!")
        elif knowledge_level >= 0.2:
            insights.append("🌱 **Level Penguasaan: PEMULA** - Setiap ahli pernah menjadi pemula. Bangun fondasi dengan kuat!")
        else:
            insights.append("🎯 **Level Penguasaan: BARU MULAI** - Welcome! Perjalanan seribu mil dimulai dari satu langkah!")
        
        # Emotion insight dengan analisis psikologis
        emotion_counts = {row['emotion_self_report']: row['count'] for row in emotions}
        if emotion_counts:
            dominant_emotion = max(emotion_counts.items(), key=lambda x: x[1])[0]
            
            positive_emotions = sum(emotion_counts.get(e, 0) for e in ['confident', 'happy', 'motivated'])
            negative_emotions = sum(emotion_counts.get(e, 0) for e in ['frustrated', 'anxious', 'stressed', 'confused'])
            neutral_emotions = emotion_counts.get('neutral', 0)
            
            total_emotions = positive_emotions + negative_emotions + neutral_emotions
            
            if total_emotions > 0:
                positive_ratio = positive_emotions / total_emotions
                
                if positive_ratio >= 0.7:
                    insights.append("😊 **Kondisi Emosi: SANGAT POSITIF** - Kamu benar-benar menikmati proses belajar! Ini adalah mindset yang sempurna untuk growth!")
                elif positive_ratio >= 0.5:
                    insights.append("🙂 **Kondisi Emosi: POSITIF** - Overall mood mu baik. Ada beberapa momen challenging tapi kamu handle dengan baik!")
                elif positive_ratio >= 0.3:
                    insights.append("😐 **Kondisi Emosi: MIXED** - Ada naik turun emosi. Normal kok! Yang penting kamu tidak menyerah!")
                else:
                    insights.append("🌈 **Kondisi Emosi: BUTUH SUPPORT** - Terdeteksi beberapa momen sulit. Sistem akan adjust untuk membuat belajar lebih nyaman!")
        
        # Learning style insight (placeholder - bisa dikembangkan)
        insights.append("🎨 **Gaya Belajar**: Sistem telah menyesuaikan konten dengan gaya belajarmu. Terus eksplorasi cara belajar yang paling cocok!")
        
        # Time management insight
        if attempted > 15:
            insights.append("⏱️ **Dedikasi Tinggi**: Kamu sudah menyelesaikan banyak soal dalam sesi ini. Great commitment!")
        elif attempted < 5:
            insights.append("⏱️ **Sesi Singkat**: Sesi kali ini singkat. Untuk hasil optimal, coba luangkan waktu lebih banyak next time!")
        
        # Specific recommendations
        if accuracy >= 70 and knowledge_level >= 0.6:
            insights.append("🎯 **Rekomendasi**: Kamu siap untuk:")
            insights.append("   • Topik berikutnya yang lebih menantang")
            insights.append("   • Soal-soal aplikasi real-world")
            insights.append("   • Membantu teman yang butuh bantuan!")
        elif accuracy < 50 or knowledge_level < 0.4:
            insights.append("📖 **Rekomendasi**: Untuk meningkatkan pemahaman:")
            insights.append("   • Review materi dasar dengan lebih teliti")
            insights.append("   • Fokus pada konsep fundamental dulu")
            insights.append("   • Jangan ragu minta bantuan atau penjelasan tambahan")
            insights.append("   • Coba pendekatan belajar yang berbeda (visual, hands-on, dll)")
        else:
            insights.append("🔄 **Rekomendasi**: Untuk progress lebih lanjut:")
            insights.append("   • Lanjutkan latihan dengan variasi soal")
            insights.append("   • Fokus pada area yang masih challenging")
            insights.append("   • Combine multiple learning strategies")
            insights.append("   • Set target pribadi untuk next session!")
        
        # Growth mindset encouragement
        insights.append("💡 **Remember**: Intelligence is not fixed. Setiap usaha melatih otakmu untuk tumbuh lebih kuat. Keep going!")
        
        return insights