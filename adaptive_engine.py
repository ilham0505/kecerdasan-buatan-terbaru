import math
import random

class AdaptiveEngine:
    """
    Engine untuk mengelola logika adaptive learning:
    - Menentukan difficulty level berikutnya
    - Update knowledge level
    - Menentukan next action berdasarkan performa dan emosi
    """
    
    def __init__(self):
        # Threshold untuk decision making
        self.MASTERY_THRESHOLD = 0.8
        self.STRUGGLE_THRESHOLD = 0.4
        self.HIGH_ANXIETY_EMOTIONS = ['frustrated', 'confused', 'anxious', 'stressed']
        self.POSITIVE_EMOTIONS = ['confident', 'happy', 'motivated', 'excited']
        
    def get_next_difficulty(self, knowledge_level, recent_accuracy, avg_response_time):
        """
        Menentukan difficulty level untuk soal berikutnya
        
        Args:
            knowledge_level: float (0-1) level penguasaan materi
            recent_accuracy: float (0-1) akurasi jawaban terakhir
            avg_response_time: float (seconds) rata-rata waktu respon
        
        Returns:
            int: difficulty level (1-5)
        """
        # Base difficulty dari knowledge level
        base_difficulty = int(knowledge_level * 5) + 1
        
        # Adjustment berdasarkan recent performance
        if recent_accuracy > 0.8:
            # Performing well, increase difficulty
            adjustment = 1
        elif recent_accuracy < 0.5:
            # Struggling, decrease difficulty
            adjustment = -1
        else:
            # Moderate performance, keep similar
            adjustment = 0
        
        # Adjustment berdasarkan response time
        if avg_response_time < 5:
            # Fast responses, might be too easy
            adjustment += 1
        elif avg_response_time > 20:
            # Slow responses, might be too hard
            adjustment -= 1
        
        # Calculate final difficulty
        difficulty = base_difficulty + adjustment
        
        # Clamp between 1-5
        return max(1, min(5, difficulty))
    
    def update_knowledge_level(self, current_level, is_correct, response_time, question_difficulty):
        """
        Update knowledge level berdasarkan performa
        Menggunakan modified Elo-like rating system
        
        Args:
            current_level: float (0-1) current knowledge level
            is_correct: bool apakah jawaban benar
            response_time: float waktu respon dalam detik
            question_difficulty: int (1-5) tingkat kesulitan soal
        
        Returns:
            float: updated knowledge level (0-1)
        """
        # K-factor (learning rate) - lebih tinggi = lebih cepat berubah
        K = 0.08
        
        # Expected performance based on current level and difficulty
        expected_level = (question_difficulty - 1) / 4.0  # Normalize to 0-1
        expected_prob = 1 / (1 + math.exp(-10 * (current_level - expected_level)))
        
        # Actual performance
        actual = 1.0 if is_correct else 0.0
        
        # Response time factor (faster = better mastery)
        time_factor = 1.0
        if is_correct:
            if response_time < 5:
                time_factor = 1.2  # Bonus for fast correct
            elif response_time > 20:
                time_factor = 0.9  # Penalty for slow correct
        
        # Update calculation
        delta = K * (actual - expected_prob) * time_factor
        new_level = current_level + delta
        
        # Clamp between 0 and 1
        return max(0.0, min(1.0, new_level))
    
    def check_answer(self, user_answer, correct_answer):
        """
        Check if answer is correct with some tolerance
        """
        if user_answer is None or user_answer == "":
            return False
        
        # Convert to string and normalize
        user_ans = str(user_answer).strip().lower()
        correct_ans = str(correct_answer).strip().lower()
        
        # Direct match
        if user_ans == correct_ans:
            return True
        
        # Try numeric comparison (for math answers)
        try:
            user_num = float(user_ans.replace(',', '.'))
            correct_num = float(correct_ans.replace(',', '.'))
            
            # Allow small tolerance for floating point
            return abs(user_num - correct_num) < 0.01
        except:
            pass
        
        # Check for common equivalent representations
        equivalents = {
            'ya': ['yes', 'benar', 'true', 'iya'],
            'tidak': ['no', 'salah', 'false'],
        }
        
        for key, values in equivalents.items():
            if user_ans in values and correct_ans == key:
                return True
            if correct_ans in values and user_ans == key:
                return True
        
        return False
    
    def determine_next_action(self, is_correct, emotion, knowledge_level, 
                              questions_attempted, questions_correct):
        """
        Menentukan action berikutnya berdasarkan:
        - Performa (benar/salah)
        - Emosi siswa
        - Knowledge level
        - Overall session performance
        
        Returns:
            dict: {
                'action': str,  # continue_practice, review_material, easier_content, end_session
                'reason': str,
                'recommendation': str
            }
        """
        accuracy = questions_correct / questions_attempted if questions_attempted > 0 else 0
        
        # HIGH ANXIETY atau NEGATIVE EMOTION - prioritas utama
        if emotion in self.HIGH_ANXIETY_EMOTIONS:
            if not is_correct:
                # Struggling + anxious = need break and review
                return {
                    'action': 'review_material',
                    'reason': 'anxiety_and_struggle',
                    'recommendation': 'Mari kita review materi dengan cara yang lebih mudah. Tidak apa-apa, belajar butuh proses! 😊'
                }
            else:
                # Correct but anxious = continue with encouragement
                return {
                    'action': 'continue_practice',
                    'reason': 'anxiety_but_correct',
                    'recommendation': 'Bagus! Kamu sebenarnya bisa kok. Yuk lanjut dengan soal serupa untuk menambah kepercayaan diri. 💪'
                }
        
        # STRUGGLING (accuracy < 40% atau knowledge < 0.4)
        if accuracy < 0.4 or knowledge_level < self.STRUGGLE_THRESHOLD:
            if questions_attempted >= 5:
                # Tried enough, need different approach
                return {
                    'action': 'easier_content',
                    'reason': 'persistent_struggle',
                    'recommendation': 'Mari kita coba pendekatan lain yang lebih mudah dipahami.'
                }
            else:
                # Give more chances with review
                return {
                    'action': 'review_material',
                    'reason': 'early_struggle',
                    'recommendation': 'Mari kita review dulu konsep dasarnya sebelum lanjut latihan.'
                }
        
        # MASTERY ACHIEVED (knowledge > 0.8 dan accuracy > 80%)
        if knowledge_level > self.MASTERY_THRESHOLD and accuracy > 0.8:
            if emotion in self.POSITIVE_EMOTIONS:
                # Great performance + positive emotion
                return {
                    'action': 'end_session',
                    'reason': 'mastery_achieved',
                    'recommendation': 'Hebat! Kamu sudah menguasai materi ini. Mau coba topik yang lebih menantang? 🎉'
                }
            else:
                # Good performance but not enthusiastic
                return {
                    'action': 'continue_practice',
                    'reason': 'consolidate_mastery',
                    'recommendation': 'Performamu bagus! Mari kita latihan beberapa soal lagi untuk memperkuat pemahaman.'
                }
        
        # MODERATE PERFORMANCE - terus berlatih
        if is_correct:
            if emotion in self.POSITIVE_EMOTIONS:
                # Positive momentum
                return {
                    'action': 'continue_practice',
                    'reason': 'positive_momentum',
                    'recommendation': 'Bagus! Kamu sedang dalam momentum yang baik. Yuk lanjut! ✨'
                }
            else:
                # Correct but neutral/negative emotion
                return {
                    'action': 'continue_practice',
                    'reason': 'build_confidence',
                    'recommendation': 'Jawabanmu benar! Yuk latihan lagi untuk menambah kepercayaan diri.'
                }
        else:
            # Wrong answer
            if emotion == 'confused':
                return {
                    'action': 'review_material',
                    'reason': 'confusion_detected',
                    'recommendation': 'Sepertinya ada yang masih membingungkan. Mari kita bahas ulang konsepnya. 🤔'
                }
            else:
                return {
                    'action': 'continue_practice',
                    'reason': 'learning_opportunity',
                    'recommendation': 'Tidak apa-apa salah, itu bagian dari belajar! Yuk coba lagi dengan soal serupa.'
                }
    
    def should_give_hint(self, attempts, response_time, emotion):
        """
        Menentukan apakah perlu memberikan hint
        """
        if attempts >= 2:
            return True
        if response_time > 30:
            return True
        if emotion in self.HIGH_ANXIETY_EMOTIONS:
            return True
        return False
    
    def calculate_session_score(self, questions_attempted, questions_correct, 
                                avg_response_time, final_knowledge_level):
        """
        Calculate overall session performance score
        """
        if questions_attempted == 0:
            return 0
        
        # Accuracy component (50%)
        accuracy_score = (questions_correct / questions_attempted) * 50
        
        # Knowledge gain component (30%)
        knowledge_score = final_knowledge_level * 30
        
        # Efficiency component (20%) - faster is better, but not too fast
        if avg_response_time < 3:
            efficiency_score = 10  # Too fast, might be guessing
        elif avg_response_time < 10:
            efficiency_score = 20  # Good pace
        elif avg_response_time < 20:
            efficiency_score = 15  # Acceptable
        else:
            efficiency_score = 10  # Too slow
        
        total_score = accuracy_score + knowledge_score + efficiency_score
        
        return round(total_score, 1)
