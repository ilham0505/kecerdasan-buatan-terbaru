#!/usr/bin/env python3
"""
Demo Test Script - Adaptive Math Learning System
Mendemonstrasikan cara kerja adaptive engine
"""

from adaptive_engine import AdaptiveEngine
from content_generator import ContentGenerator

def print_section(title):
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)

def demo_adaptive_engine():
    print_section("🧠 DEMO: ADAPTIVE ENGINE")
    
    engine = AdaptiveEngine()
    
    # Scenario 1: Pemula yang belajar cepat
    print("\n📘 Skenario 1: Siswa Pemula Belajar Cepat")
    print("-" * 70)
    
    knowledge = 0.2
    print(f"Knowledge Level Awal: {knowledge*100:.1f}%")
    
    for i in range(1, 6):
        # Simulasi jawaban benar dengan response time cepat
        is_correct = True
        response_time = 5.0
        difficulty = min(i, 5)
        
        new_knowledge = engine.update_knowledge_level(
            knowledge, is_correct, response_time, difficulty
        )
        
        print(f"\nSoal {i}:")
        print(f"  Difficulty: Level {difficulty}")
        print(f"  Jawaban: ✓ Benar (waktu: {response_time}s)")
        print(f"  Knowledge: {knowledge*100:.1f}% → {new_knowledge*100:.1f}%")
        print(f"  Kenaikan: +{(new_knowledge - knowledge)*100:.1f}%")
        
        knowledge = new_knowledge
    
    print(f"\n🎯 Knowledge Level Akhir: {knowledge*100:.1f}%")
    print("📊 Status: " + ("🏆 Mahir" if knowledge >= 0.8 else "👍 Baik" if knowledge >= 0.6 else "📈 Berkembang"))
    
    # Scenario 2: Siswa yang struggle
    print("\n\n📕 Skenario 2: Siswa yang Kesulitan")
    print("-" * 70)
    
    knowledge = 0.3
    print(f"Knowledge Level Awal: {knowledge*100:.1f}%")
    
    # Simulasi beberapa jawaban salah
    for i in range(1, 4):
        is_correct = False
        response_time = 25.0  # Lambat
        difficulty = 3
        
        new_knowledge = engine.update_knowledge_level(
            knowledge, is_correct, response_time, difficulty
        )
        
        print(f"\nSoal {i}:")
        print(f"  Difficulty: Level {difficulty}")
        print(f"  Jawaban: ✗ Salah (waktu: {response_time}s)")
        print(f"  Knowledge: {knowledge*100:.1f}% → {new_knowledge*100:.1f}%")
        print(f"  Penurunan: {(new_knowledge - knowledge)*100:.1f}%")
        
        knowledge = new_knowledge
    
    print(f"\n🎯 Knowledge Level Akhir: {knowledge*100:.1f}%")
    print("💡 Rekomendasi Sistem: Review materi & turunkan difficulty")
    
    # Scenario 3: Decision making berdasarkan emosi
    print("\n\n📗 Skenario 3: Adaptive Decision Making")
    print("-" * 70)
    
    scenarios = [
        ("Benar + Confident", True, "confident", 0.7, 8, 8),
        ("Salah + Frustrated", False, "frustrated", 0.4, 5, 2),
        ("Benar + Anxious", True, "anxious", 0.5, 3, 3),
        ("Salah + Confused", False, "confused", 0.3, 4, 1),
    ]
    
    for desc, is_correct, emotion, knowledge, attempted, correct in scenarios:
        decision = engine.determine_next_action(
            is_correct, emotion, knowledge, attempted, correct
        )
        
        print(f"\n{desc}:")
        print(f"  Knowledge: {knowledge*100:.0f}%")
        print(f"  Accuracy: {correct}/{attempted} = {correct/attempted*100:.0f}%")
        print(f"  → Action: {decision['action']}")
        print(f"  → Reason: {decision['reason']}")
        print(f"  → Recommendation: {decision['recommendation']}")

def demo_content_generator():
    print_section("📚 DEMO: CONTENT GENERATOR")
    
    generator = ContentGenerator()
    
    # Demo 1: Generate learning content
    print("\n📖 Demo: Generate Learning Content")
    print("-" * 70)
    
    content = generator.generate_learning_content(
        "Penjumlahan Dasar",
        "Operasi penjumlahan bilangan bulat",
        0.3,  # Low knowledge
        0
    )
    
    print(f"Title: {content['title']}")
    print(f"Level: {content['level']}")
    print(f"\nSections ({len(content['sections'])} sections):")
    for section in content['sections']:
        print(f"  • {section['title']} ({section['type']})")
    
    # Demo 2: Generate questions
    print("\n\n❓ Demo: Generate Questions")
    print("-" * 70)
    
    for difficulty in [1, 2, 3]:
        question = generator.generate_question(
            "Penjumlahan Dasar",
            difficulty,
            difficulty * 0.3
        )
        
        print(f"\nLevel {difficulty}:")
        print(f"  Q: {question['question']}")
        print(f"  A: {question['answer']}")
        print(f"  Explanation: {question['explanation']}")
    
    # Demo 3: Generate feedback
    print("\n\n💬 Demo: Generate Feedback")
    print("-" * 70)
    
    test_cases = [
        (True, "confident", 0.7, "Jawaban Benar + Confident"),
        (False, "frustrated", 0.3, "Jawaban Salah + Frustrated"),
        (True, "anxious", 0.5, "Jawaban Benar + Anxious"),
    ]
    
    question_data = {
        'question': "5 + 3 = ?",
        'answer': "8",
        'explanation': "5 ditambah 3 sama dengan 8"
    }
    
    for is_correct, emotion, knowledge, desc in test_cases:
        feedback = generator.generate_feedback(
            is_correct, question_data, "8", emotion, knowledge
        )
        
        print(f"\n{desc}:")
        print(f"  {feedback}")

def demo_5_step_cycle():
    print_section("🔄 DEMO: 5-STEP ADAPTIVE CYCLE")
    
    engine = AdaptiveEngine()
    generator = ContentGenerator()
    
    print("\nSimulasi satu cycle lengkap pembelajaran:")
    print("-" * 70)
    
    # State
    topic = "Penjumlahan Dasar"
    knowledge = 0.4
    attempts = 2
    correct = 1
    
    # Step 1: Siswa melihat materi
    print("\n📖 STEP 1: Siswa Melihat Materi")
    content = generator.generate_learning_content(topic, "", knowledge, attempts)
    print(f"  Content Level: {content['level']}")
    print(f"  Sections: {len(content['sections'])}")
    
    # Step 2: Mencari feedback
    print("\n❓ STEP 2: Mencari Feedback (Quiz)")
    difficulty = engine.get_next_difficulty(knowledge, 0.5, 10)
    question = generator.generate_question(topic, difficulty, knowledge)
    print(f"  Question (Difficulty {difficulty}): {question['question']}")
    
    # Simulasi jawaban siswa
    user_answer = "8"
    emotion = "confused"
    print(f"  Student Answer: {user_answer}")
    print(f"  Student Emotion: {emotion}")
    
    # Step 3: Identifikasi/klasifikasi feedback
    print("\n🔍 STEP 3: Identifikasi Feedback")
    is_correct = engine.check_answer(user_answer, question['answer'])
    print(f"  Answer Check: {'✓ Correct' if is_correct else '✗ Incorrect'}")
    print(f"  Emotion Classified: {emotion}")
    
    # Step 4: Update materi berdasarkan feedback
    print("\n🔄 STEP 4: Update Materi")
    
    # Update knowledge
    new_knowledge = engine.update_knowledge_level(
        knowledge, is_correct, 15.0, difficulty
    )
    print(f"  Knowledge: {knowledge*100:.1f}% → {new_knowledge*100:.1f}%")
    
    # Generate feedback
    feedback = generator.generate_feedback(
        is_correct, question, user_answer, emotion, new_knowledge
    )
    print(f"  Feedback: {feedback[:100]}...")
    
    # Determine next action
    decision = engine.determine_next_action(
        is_correct, emotion, new_knowledge, attempts+1, correct+(1 if is_correct else 0)
    )
    print(f"  Next Action: {decision['action']}")
    print(f"  Recommendation: {decision['recommendation']}")
    
    # Step 5: Iterasi
    print("\n🔁 STEP 5: Ulangi atau Selesai?")
    if decision['action'] == 'end_session':
        print("  → Session Complete! Student has mastered the topic.")
    else:
        print("  → Continue to next iteration with adapted content")
        print(f"     New Difficulty: {engine.get_next_difficulty(new_knowledge, 0.5, 10)}")

def main():
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║       🎓 ADAPTIVE MATH LEARNING SYSTEM - DEMO                       ║
║                                                                      ║
║       Demonstrasi Core Algorithm & Adaptive Engine                  ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    
    demo_adaptive_engine()
    input("\n\nPress Enter untuk lanjut ke Content Generator demo...")
    
    demo_content_generator()
    input("\n\nPress Enter untuk lanjut ke 5-Step Cycle demo...")
    
    demo_5_step_cycle()
    
    print_section("✅ DEMO SELESAI")
    print("\n📊 Summary:")
    print("  • Adaptive Engine: Menyesuaikan difficulty & knowledge level")
    print("  • Content Generator: Generate materi & soal adaptif")
    print("  • Decision Engine: Menentukan next action berdasarkan performa & emosi")
    print("  • 5-Step Cycle: Loop pembelajaran adaptif yang lengkap")
    print("\n🚀 Sistem siap digunakan untuk pembelajaran interaktif!")
    print("\nUntuk menjalankan full web app: python app.py")
    print()

if __name__ == "__main__":
    main()
