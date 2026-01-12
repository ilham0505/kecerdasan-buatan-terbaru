import json
import random

class ContentGenerator:
    """
    Generator untuk membuat konten pembelajaran adaptif
    Menggunakan AI untuk personalisasi dan bank soal untuk fallback
    """
    
    def __init__(self):
        # Bank soal sederhana sebagai fallback
        self.question_bank = {
            "Penjumlahan Dasar": {
                1: [
                    {"q": "2 + 3 = ?", "a": "5", "exp": "2 ditambah 3 sama dengan 5"},
                    {"q": "5 + 4 = ?", "a": "9", "exp": "5 ditambah 4 sama dengan 9"},
                    {"q": "1 + 7 = ?", "a": "8", "exp": "1 ditambah 7 sama dengan 8"},
                ],
                2: [
                    {"q": "12 + 8 = ?", "a": "20", "exp": "12 + 8 = 20"},
                    {"q": "15 + 17 = ?", "a": "32", "exp": "15 + 17 = 32"},
                ],
                3: [
                    {"q": "45 + 67 = ?", "a": "112", "exp": "45 + 67 = 112"},
                    {"q": "89 + 34 = ?", "a": "123", "exp": "89 + 34 = 123"},
                ],
            },
            "Perkalian Dasar": {
                1: [
                    {"q": "3 × 2 = ?", "a": "6", "exp": "3 dikali 2 sama dengan 6"},
                    {"q": "4 × 5 = ?", "a": "20", "exp": "4 dikali 5 sama dengan 20"},
                ],
                2: [
                    {"q": "12 × 3 = ?", "a": "36", "exp": "12 × 3 = 36"},
                    {"q": "7 × 8 = ?", "a": "56", "exp": "7 × 8 = 56"},
                ],
                3: [
                    {"q": "15 × 12 = ?", "a": "180", "exp": "15 × 12 = 180"},
                    {"q": "25 × 4 = ?", "a": "100", "exp": "25 × 4 = 100"},
                ],
            },
            "Geometri Dasar": {
                1: [
                    {"q": "Persegi dengan sisi 4 cm, berapakah kelilingnya?", "a": "16", "exp": "Keliling = 4 × sisi = 4 × 4 = 16 cm"},
                    {"q": "Persegi panjang panjang 6 cm dan lebar 3 cm, berapakah luasnya?", "a": "18", "exp": "Luas = panjang × lebar = 6 × 3 = 18 cm²"},
                ],
                2: [
                    {"q": "Segitiga dengan alas 8 cm dan tinggi 5 cm, berapakah luasnya?", "a": "20", "exp": "Luas segitiga = ½ × alas × tinggi = ½ × 8 × 5 = 20 cm²"},
                ],
            },
            "Aljabar Sederhana": {
                1: [
                    {"q": "x + 5 = 12, maka x = ?", "a": "7", "exp": "x = 12 - 5 = 7"},
                    {"q": "2x = 10, maka x = ?", "a": "5", "exp": "x = 10 ÷ 2 = 5"},
                ],
                2: [
                    {"q": "3x + 2 = 17, maka x = ?", "a": "5", "exp": "3x = 17 - 2 = 15, maka x = 15 ÷ 3 = 5"},
                ],
            }
        }
    
    def generate_learning_content(self, topic_name, topic_description, knowledge_level, attempts):
        """
        Generate konten pembelajaran yang disesuaikan dengan level siswa
        
        Args:
            topic_name: str nama topik
            topic_description: str deskripsi topik
            knowledge_level: float (0-1) tingkat penguasaan
            attempts: int jumlah percobaan sebelumnya
        
        Returns:
            dict: konten pembelajaran dengan sections
        """
        # Determine content level
        if knowledge_level < 0.3:
            level = "basic"
            approach = "sangat sederhana dengan banyak contoh"
        elif knowledge_level < 0.6:
            level = "intermediate"
            approach = "dengan contoh dan latihan"
        else:
            level = "advanced"
            approach = "dengan aplikasi dan problem solving"
        
        # Template konten berdasarkan level
        content = {
            "title": f"Belajar {topic_name}",
            "level": level,
            "sections": []
        }
        
        # Section 1: Pengenalan
        if level == "basic":
            content["sections"].append({
                "type": "introduction",
                "title": "Apa itu " + topic_name + "?",
                "content": self._get_introduction(topic_name, "basic")
            })
        
        # Section 2: Konsep Utama
        content["sections"].append({
            "type": "concept",
            "title": "Konsep Dasar",
            "content": self._get_concept_explanation(topic_name, level)
        })
        
        # Section 3: Contoh
        content["sections"].append({
            "type": "example",
            "title": "Contoh Soal",
            "content": self._get_examples(topic_name, level)
        })
        
        # Section 4: Tips
        if knowledge_level < 0.5:
            content["sections"].append({
                "type": "tips",
                "title": "Tips Mudah",
                "content": self._get_tips(topic_name)
            })
        
        return content
    
    def _get_introduction(self, topic_name, level):
        """Generate introduction text"""
        intros = {
            "Penjumlahan Dasar": "Penjumlahan adalah operasi menggabungkan dua bilangan atau lebih menjadi satu bilangan yang lebih besar. Misalnya, jika kamu punya 2 apel dan temanmu memberi 3 apel lagi, sekarang kamu punya 5 apel. Itulah penjumlahan!",
            "Perkalian Dasar": "Perkalian adalah penjumlahan berulang. Misalnya, 3 × 4 artinya 3 ditambahkan sebanyak 4 kali: 3 + 3 + 3 + 3 = 12. Perkalian membuat hitungan lebih cepat!",
            "Geometri Dasar": "Geometri adalah ilmu tentang bentuk dan ukuran. Kita akan belajar tentang bangun datar seperti persegi, segitiga, dan lingkaran, serta cara menghitung luas dan kelilingnya.",
            "Aljabar Sederhana": "Aljabar menggunakan huruf (seperti x, y) untuk mewakili angka yang belum kita ketahui. Ini seperti teka-teki matematika yang seru!"
        }
        return intros.get(topic_name, f"Mari kita pelajari {topic_name} dengan cara yang menyenangkan!")
    
    def _get_concept_explanation(self, topic_name, level):
        """Generate concept explanation"""
        concepts = {
            "Penjumlahan Dasar": {
                "basic": "Untuk menjumlahkan, mulai dari angka pertama, lalu hitung maju sebanyak angka kedua. Contoh: 5 + 3 = ?, mulai dari 5, lalu hitung 3 langkah: 6, 7, 8. Jadi jawabannya 8!",
                "intermediate": "Tips menjumlah cepat: 1) Cari pasangan yang jumlahnya 10, 2) Bulatkan ke angka 10-an terdekat, 3) Gunakan sifat komutatif (5+3 = 3+5)",
                "advanced": "Strategi menjumlah bilangan besar: decompose, regrouping, dan estimasi untuk mengecek jawaban."
            },
            "Perkalian Dasar": {
                "basic": "Perkalian adalah penjumlahan berulang. 4 × 3 = 4 + 4 + 4 = 12. Atau bisa dibayangkan: 4 kotak, masing-masing berisi 3 permen.",
                "intermediate": "Hafalkan tabel perkalian 1-10. Gunakan trik: untuk × 9, turunkan 1 dari angka yang dikali, lalu pasangkan dengan angka yang jumlahnya 9.",
                "advanced": "Gunakan distributive property: 7 × 12 = 7 × (10 + 2) = (7 × 10) + (7 × 2) = 70 + 14 = 84"
            },
            "Geometri Dasar": {
                "basic": "Persegi: semua sisi sama panjang. Keliling = 4 × sisi. Luas = sisi × sisi.",
                "intermediate": "Persegi panjang: Keliling = 2 × (panjang + lebar). Luas = panjang × lebar. Segitiga: Luas = ½ × alas × tinggi.",
                "advanced": "Gunakan rumus luas untuk berbagai bangun datar dan aplikasikan dalam masalah kontekstual."
            }
        }
        
        topic_concepts = concepts.get(topic_name, {})
        return topic_concepts.get(level, f"Penjelasan konsep {topic_name}")
    
    def _get_examples(self, topic_name, level):
        """Generate example problems"""
        examples = {
            "Penjumlahan Dasar": {
                "basic": [
                    "Contoh 1: 3 + 4 = 7 (mulai dari 3, hitung 4 langkah: 4, 5, 6, 7)",
                    "Contoh 2: 7 + 2 = 9 (mulai dari 7, hitung 2 langkah: 8, 9)"
                ],
                "intermediate": [
                    "Contoh 1: 25 + 37 = (20+30) + (5+7) = 50 + 12 = 62",
                    "Contoh 2: 48 + 35 = (48 + 2) + (35 - 2) = 50 + 33 = 83"
                ]
            },
            "Perkalian Dasar": {
                "basic": [
                    "Contoh 1: 5 × 3 = 5 + 5 + 5 = 15",
                    "Contoh 2: 4 × 2 = 4 + 4 = 8"
                ],
                "intermediate": [
                    "Contoh 1: 7 × 8 = (7 × 4) + (7 × 4) = 28 + 28 = 56",
                    "Contoh 2: 9 × 6 = (10 × 6) - (1 × 6) = 60 - 6 = 54"
                ]
            }
        }
        
        topic_examples = examples.get(topic_name, {})
        example_list = topic_examples.get(level, ["Contoh akan ditampilkan di sini"])
        
        return "\n\n".join(example_list)
    
    def _get_tips(self, topic_name):
        """Generate helpful tips"""
        tips = {
            "Penjumlahan Dasar": "💡 Tips: Gunakan jari atau gambar untuk membantu menghitung. Latih dengan benda di sekitarmu!",
            "Perkalian Dasar": "💡 Tips: Hafalkan tabel perkalian sedikit demi sedikit. Mulai dari yang mudah: 1, 2, 5, 10.",
            "Geometri Dasar": "💡 Tips: Gambar bangun datarnya dulu, lalu beri label pada setiap sisi. Ini membantu visualisasi!",
            "Aljabar Sederhana": "💡 Tips: Bayangkan x sebagai kotak misteri. Kita harus mencari tahu isi kotaknya!"
        }
        return tips.get(topic_name, "💡 Terus berlatih dan jangan takut salah!")
    
    def generate_question(self, topic_name, difficulty, knowledge_level):
        """
        Generate soal berdasarkan topik dan difficulty
        
        Returns:
            dict: {
                'question': str,
                'answer': str,
                'explanation': str,
                'difficulty': int,
                'hints': list
            }
        """
        # Try to get from question bank
        if topic_name in self.question_bank:
            topic_questions = self.question_bank[topic_name]
            difficulty_questions = topic_questions.get(difficulty, topic_questions.get(1, []))
            
            if difficulty_questions:
                q_data = random.choice(difficulty_questions)
                return {
                    'question': q_data['q'],
                    'answer': q_data['a'],
                    'explanation': q_data['exp'],
                    'difficulty': difficulty,
                    'hints': self._generate_hints(q_data['q'], q_data['a'])
                }
        
        # Fallback: generate simple question
        return self._generate_fallback_question(topic_name, difficulty)
    
    def _generate_hints(self, question, answer):
        """Generate progressive hints"""
        # Simple hint generation (could be improved with AI)
        return [
            "💡 Hint 1: Baca soal dengan teliti. Apa yang ditanyakan?",
            "💡 Hint 2: Coba pecah soal menjadi bagian-bagian kecil.",
            f"💡 Hint 3: Jawabannya adalah angka antara {max(0, int(answer)-5)} dan {int(answer)+5}"
        ]
    
    def _generate_fallback_question(self, topic_name, difficulty):
        """Generate a simple fallback question"""
        if difficulty <= 2:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            result = a + b
            return {
                'question': f"{a} + {b} = ?",
                'answer': str(result),
                'explanation': f"{a} ditambah {b} sama dengan {result}",
                'difficulty': difficulty,
                'hints': [
                    f"💡 Mulai dari {a}, lalu hitung {b} langkah ke depan",
                    f"💡 {a} + {b} = {result}"
                ]
            }
        else:
            a = random.randint(10, 50)
            b = random.randint(10, 50)
            result = a + b
            return {
                'question': f"{a} + {b} = ?",
                'answer': str(result),
                'explanation': f"Cara cepat: bulatkan {a} menjadi {(a//10+1)*10}, sesuaikan hasilnya",
                'difficulty': difficulty,
                'hints': [
                    "💡 Coba bulatkan salah satu angka untuk mempermudah",
                    f"💡 Jawabannya sekitar {(result//10)*10}"
                ]
            }
    
    def generate_feedback(self, is_correct, question_data, user_answer, emotion, knowledge_level):
        """
        Generate personalized feedback based on performance and emotion
        """
        feedback = ""
        
        if is_correct:
            # Positive feedback dengan variasi
            positive_msgs = [
                "🎉 Benar! Kamu hebat!",
                "✨ Bagus sekali! Jawabanmu tepat!",
                "👏 Mantap! Kamu sudah memahami konsepnya!",
                "⭐ Sempurna! Teruskan!",
                "🌟 Luar biasa! Kamu pintar!"
            ]
            feedback = random.choice(positive_msgs)
            
            # Additional encouragement based on emotion
            if emotion in ['frustrated', 'confused']:
                feedback += " Lihat, kamu bisa kok! Terus semangat ya! 💪"
            elif emotion in ['confident', 'happy']:
                feedback += " Kamu sedang dalam performa terbaik! 🚀"
            
        else:
            # Constructive feedback
            encouraging_msgs = [
                "Tidak apa-apa, belajar itu proses! ",
                "Hampir benar! ",
                "Bagus sudah mencoba! ",
                "Terus semangat! ",
            ]
            feedback = random.choice(encouraging_msgs)
            
            # Add explanation
            feedback += f"Jawaban yang benar adalah {question_data['answer']}. "
            feedback += question_data.get('explanation', '')
            
            # Emotional support
            if emotion in ['frustrated', 'anxious', 'stressed']:
                feedback += "\n\n🌈 Tenang, semua orang pernah salah. Yuk kita coba lagi dengan cara yang lebih mudah!"
            elif emotion == 'confused':
                feedback += "\n\n🤔 Mari saya jelaskan dengan cara yang berbeda agar lebih jelas."
        
        return feedback
    
    def generate_review_content(self, topic_name, knowledge_level):
        """Generate review/summary content"""
        return {
            "title": f"Review: {topic_name}",
            "type": "review",
            "sections": [
                {
                    "title": "Poin-Poin Penting",
                    "content": self._get_key_points(topic_name)
                },
                {
                    "title": "Contoh Sederhana",
                    "content": self._get_examples(topic_name, "basic")
                },
                {
                    "title": "Latihan Singkat",
                    "content": "Mari coba beberapa soal mudah untuk mengingat kembali."
                }
            ]
        }
    
    def _get_key_points(self, topic_name):
        """Get key points summary"""
        points = {
            "Penjumlahan Dasar": "• Penjumlahan menggabungkan dua bilangan\n• Urutan tidak penting (3+5 = 5+3)\n• Gunakan strategi counting on atau decomposition",
            "Perkalian Dasar": "• Perkalian = penjumlahan berulang\n• Hafalkan tabel perkalian\n• Gunakan strategi doubling atau skip counting",
            "Geometri Dasar": "• Setiap bangun punya rumus sendiri\n• Keliling = jumlah semua sisi\n• Luas = ukuran bidang yang tertutup",
            "Aljabar Sederhana": "• Variabel (x, y) mewakili nilai yang belum diketahui\n• Selesaikan dengan isolasi variabel\n• Cek jawaban dengan substitusi"
        }
        return points.get(topic_name, f"Konsep utama dari {topic_name}")
    
    def generate_session_insights(self, topic_name, attempted, correct, knowledge_level, emotions):
        """Generate insights from learning session"""
        accuracy = (correct / attempted * 100) if attempted > 0 else 0
        
        insights = []
        
        # Performance insight
        if accuracy >= 80:
            insights.append("🎯 Performa luar biasa! Kamu sudah menguasai materi ini dengan baik.")
        elif accuracy >= 60:
            insights.append("👍 Performa bagus! Sedikit lagi untuk menguasai materi ini sepenuhnya.")
        elif accuracy >= 40:
            insights.append("📚 Terus berlatih! Kamu sedang dalam proses belajar yang baik.")
        else:
            insights.append("💪 Jangan menyerah! Mari kita coba pendekatan yang berbeda.")
        
        # Knowledge level insight
        if knowledge_level >= 0.8:
            insights.append("⭐ Level penguasaan: MAHIR - Siap untuk topik yang lebih menantang!")
        elif knowledge_level >= 0.6:
            insights.append("📈 Level penguasaan: BAIK - Terus tingkatkan dengan lebih banyak latihan.")
        elif knowledge_level >= 0.4:
            insights.append("📊 Level penguasaan: BERKEMBANG - Kamu sedang berkembang dengan baik!")
        else:
            insights.append("🌱 Level penguasaan: PEMULA - Mari bangun fondasi yang kuat.")
        
        # Emotion insight
        emotion_counts = {row['emotion_self_report']: row['count'] for row in emotions}
        dominant_emotion = max(emotion_counts.items(), key=lambda x: x[1])[0] if emotion_counts else 'neutral'
        
        if dominant_emotion in ['confident', 'happy', 'motivated']:
            insights.append("😊 Kondisi emosi: POSITIF - Kamu menikmati proses belajar!")
        elif dominant_emotion in ['frustrated', 'anxious', 'stressed']:
            insights.append("🌈 Kondisi emosi: BUTUH DUKUNGAN - Mari kita buat belajar lebih menyenangkan di sesi berikutnya.")
        else:
            insights.append("😐 Kondisi emosi: NETRAL - Pertahankan fokus dan semangat belajarmu.")
        
        # Recommendation
        if accuracy >= 70 and knowledge_level >= 0.6:
            insights.append("🎯 Rekomendasi: Kamu siap untuk topik berikutnya atau soal yang lebih menantang!")
        elif accuracy < 50:
            insights.append("📖 Rekomendasi: Review materi dasar dan coba dengan pendekatan yang berbeda.")
        else:
            insights.append("🔄 Rekomendasi: Lanjutkan latihan dengan variasi soal untuk memperkuat pemahaman.")
        
        return insights
