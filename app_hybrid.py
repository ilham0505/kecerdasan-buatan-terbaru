import os
PORT = int(os.environ.get("PORT", 8000))

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
from datetime import datetime
import sqlite3
import os
from adaptive_engine import AdaptiveEngine
from content_generator import ContentGenerator

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this-in-production'

# Initialize components
adaptive_engine = AdaptiveEngine()
content_gen = ContentGenerator()

# Try to import enhanced modules (optional)
try:
    from improved_content_generator import ImprovedContentGenerator
    from expanded_content_bank import ExpandedContentBank
    from vark_learning_styles import VARKContentGenerator
    
    # Use enhanced version if available
    content_gen = ImprovedContentGenerator()
    expanded_bank = ExpandedContentBank()
    vark_gen = VARKContentGenerator()
    ENHANCED_MODE = True
    print("✅ Enhanced mode: VARK & Expanded Content ACTIVE")
    print("✅ Audio support: Text-to-Speech ENABLED")
except ImportError as e:
    # Fall back to original
    ENHANCED_MODE = False
    print("⚠️ Running in ORIGINAL mode (VARK modules not found)")
    print(f"   Error: {e}")
    print("   Tip: Rename 'Expanded content bank .py' to 'expanded_content_bank.py'")
    print("        Rename 'Vark learning styles.py' to 'vark_learning_styles.py'")

# ------------------------------
# DATABASE SETUP
# ------------------------------
def init_db():
    conn = sqlite3.connect('learning_data.db')
    c = conn.cursor()
    
    # Tabel siswa - with optional learning_style for enhanced mode
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  learning_style TEXT DEFAULT 'visual',
                  created_at TIMESTAMP)''')
    
    # Tabel topik matematika
    c.execute('''CREATE TABLE IF NOT EXISTS topics
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT,
                  description TEXT,
                  difficulty INTEGER)''')
    
    # Tabel progress siswa per topik
    c.execute('''CREATE TABLE IF NOT EXISTS progress
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  student_id INTEGER,
                  topic_id INTEGER,
                  knowledge_level REAL,
                  attempts INTEGER,
                  last_accessed TIMESTAMP,
                  FOREIGN KEY (student_id) REFERENCES students (id),
                  FOREIGN KEY (topic_id) REFERENCES topics (id))''')
    
    # Tabel interaksi (untuk behavioral analysis)
    c.execute('''CREATE TABLE IF NOT EXISTS interactions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  student_id INTEGER,
                  topic_id INTEGER,
                  question TEXT,
                  answer TEXT,
                  is_correct INTEGER,
                  response_time REAL,
                  difficulty_level INTEGER,
                  emotion_self_report TEXT,
                  timestamp TIMESTAMP,
                  FOREIGN KEY (student_id) REFERENCES students (id),
                  FOREIGN KEY (topic_id) REFERENCES topics (id))''')
    
    # Tabel session belajar
    c.execute('''CREATE TABLE IF NOT EXISTS learning_sessions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  student_id INTEGER,
                  topic_id INTEGER,
                  start_time TIMESTAMP,
                  end_time TIMESTAMP,
                  questions_attempted INTEGER,
                  questions_correct INTEGER,
                  avg_difficulty REAL,
                  final_emotion TEXT,
                  FOREIGN KEY (student_id) REFERENCES students (id),
                  FOREIGN KEY (topic_id) REFERENCES topics (id))''')
    
    conn.commit()
    conn.close()

# Load emotion model jika ada
try:
    emotion_model = tf.keras.models.load_model('emotion_model.h5')
    EMOTIONS = ['Marah', 'Jijik', 'Takut', 'Senang', 'Sedih', 'Terkejut', 'Biasa']
    EMOTION_MODEL_LOADED = True
    print("✅ Emotion model loaded successfully")
except Exception as e:
    print(f"⚠️ Could not load emotion model: {e}")
    print("⚠️ Emotion detection will not work")
    EMOTION_MODEL_LOADED = False
    emotion_model = None
    EMOTIONS = []

# Seed initial topics
def seed_topics():
    conn = sqlite3.connect('learning_data.db')
    c = conn.cursor()
    
    c.execute("SELECT COUNT(*) FROM topics")
    if c.fetchone()[0] == 0:
        topics = [
            ("Penjumlahan Dasar", "Operasi penjumlahan bilangan bulat", 1),
            ("Pengurangan Dasar", "Operasi pengurangan bilangan bulat", 1),
            ("Perkalian Dasar", "Operasi perkalian bilangan bulat", 2),
            ("Pembagian Dasar", "Operasi pembagian bilangan bulat", 2),
            ("Pecahan", "Operasi dengan bilangan pecahan", 3),
            ("Geometri Dasar", "Bangun datar dan rumus sederhana", 3),
            ("Aljabar Sederhana", "Persamaan linear satu variabel", 4),
        ]
        c.executemany("INSERT INTO topics (name, description, difficulty) VALUES (?, ?, ?)", topics)
        conn.commit()
    
    conn.close()

# Initialize database
init_db()
seed_topics()

# ------------------------------
# HELPER FUNCTIONS
# ------------------------------
def get_db():
    conn = sqlite3.connect('learning_data.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_student_id():
    if 'student_id' not in session:
        return None
    return session['student_id']

def get_student_learning_style():
    """Get student's preferred learning style (if enhanced mode)"""
    if not ENHANCED_MODE:
        return 'visual'
    
    if 'learning_style' in session:
        return session['learning_style']
    
    student_id = get_student_id()
    if student_id:
        conn = get_db()
        c = conn.cursor()
        c.execute("SELECT learning_style FROM students WHERE id = ?", (student_id,))
        result = c.fetchone()
        conn.close()
        if result:
            session['learning_style'] = result['learning_style']
            return result['learning_style']
    
    return 'visual'  # Default

# ------------------------------
# ROUTES
# ------------------------------

@app.route("/")
def index():
    return redirect(url_for("register"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        learning_style = request.form.get("learning_style", "visual") if ENHANCED_MODE else "visual"
        
        if name:
            conn = get_db()
            c = conn.cursor()
            c.execute("""
                INSERT INTO students (name, learning_style, created_at)
                VALUES (?, ?, ?)
            """, (name, learning_style, datetime.now()))
            conn.commit()

            student_id = c.lastrowid
            conn.close()
            
            session["student_id"] = student_id
            session["student_name"] = name
            session["learning_style"] = learning_style
            
            return redirect(url_for("dashboard"))

    return render_template("register.html", enhanced_mode=ENHANCED_MODE)


@app.route("/dashboard")
def dashboard():
    student_id = get_student_id()
    if not student_id:
        return redirect(url_for('register'))
    
    conn = get_db()
    c = conn.cursor()
    
    # Get all topics with student progress
    c.execute("""
        SELECT t.id, t.name, t.description, t.difficulty,
               COALESCE(p.knowledge_level, 0) as knowledge_level,
               COALESCE(p.attempts, 0) as attempts
        FROM topics t
        LEFT JOIN progress p ON t.id = p.topic_id AND p.student_id = ?
        ORDER BY t.difficulty, t.id
    """, (student_id,))
    
    topics = c.fetchall()
    conn.close()
    
    return render_template("dashboard.html", 
                         topics=topics,
                         student_name=session.get('student_name'),
                         enhanced_mode=ENHANCED_MODE)

@app.route("/learn/<int:topic_id>")
def learn(topic_id):
    student_id = get_student_id()
    if not student_id:
        return redirect(url_for('register'))
    
    conn = get_db()
    c = conn.cursor()
    
    # Get topic info
    c.execute("SELECT * FROM topics WHERE id = ?", (topic_id,))
    topic = c.fetchone()
    
    if not topic:
        return "Topic not found", 404
    
    # Get student's current knowledge level for this topic
    c.execute("""
        SELECT knowledge_level, attempts 
        FROM progress 
        WHERE student_id = ? AND topic_id = ?
    """, (student_id, topic_id))
    
    progress = c.fetchone()
    knowledge_level = progress['knowledge_level'] if progress else 0
    attempts = progress['attempts'] if progress else 0
    
    conn.close()
    
    # Initialize learning session
    session['current_topic_id'] = topic_id
    session['session_start'] = datetime.now().isoformat()
    session['questions_attempted'] = 0
    session['questions_correct'] = 0
    
    # Get learning style for this session
    learning_style = get_student_learning_style()
    
    # Generate content (enhanced or original)
    if ENHANCED_MODE:
        content = content_gen.generate_learning_content(
            topic['name'],
            topic['description'],
            knowledge_level,
            attempts,
            learning_style
        )
    else:
        content = content_gen.generate_learning_content(
            topic['name'],
            topic['description'],
            knowledge_level,
            attempts
        )
    
    # 🔊 CHANGED: Use learn.html (audio-enabled version)
    # Make sure you've renamed learn_with_audio.html to learn.html
    # OR keep both and use learn_with_audio.html here
    return render_template("learn.html",  # ← Audio-enabled template
                         topic=topic,
                         content=content,
                         knowledge_level=knowledge_level,
                         learning_style=learning_style)  # ← Pass learning_style!

@app.route("/check_status")
def check_status():
    """Endpoint untuk cek status sesi (untuk dashboard)"""
    student_id = get_student_id()
    if not student_id:
        return jsonify({"error": "not_logged_in"}), 401
    
    return jsonify({
        "session_active": bool(session.get('current_topic_id')),
        "current_question": session.get('questions_attempted', 0),
        "remaining": 10 - session.get('questions_attempted', 0) if session.get('questions_attempted', 0) < 10 else 0,
        "last_emotion": session.get('last_emotion', 'Belum terdeteksi')
    })

@app.route("/detect_emotion", methods=["POST"])
def detect_emotion():
    if "student_id" not in session:
        return jsonify({"error": "not_logged_in"}), 401

    # Jika model tidak di-load, return dummy data
    if not EMOTION_MODEL_LOADED:
        return jsonify({
            "emotion": "Senang",
            "confidence": 0.85
        })
    
    data = request.json
    image_base64 = data.get("image")

    if not image_base64:
        return jsonify({"error": "no_image"}), 400

    try:
        # Decode base64 → image
        image_bytes = base64.b64decode(image_base64.split(",")[1])
        img = Image.open(BytesIO(image_bytes)).convert("L")
        img = img.resize((48, 48))

        img_array = np.array(img) / 255.0
        img_array = img_array.reshape(1, 48, 48, 1)

        prediction = emotion_model.predict(img_array, verbose=0)
        emotion_index = np.argmax(prediction)
        emotion = EMOTIONS[emotion_index] if emotion_index < len(EMOTIONS) else "Biasa"

        # SIMPAN KE SESSION
        session["last_emotion"] = emotion

        return jsonify({
            "emotion": emotion,
            "confidence": float(np.max(prediction))
        })
    except Exception as e:
        print(f"Error in emotion detection: {e}")
        return jsonify({
            "emotion": "Error",
            "confidence": 0.0
        })

@app.route("/practice/<int:topic_id>")
def practice(topic_id):
    student_id = get_student_id()
    if not student_id:
        return redirect(url_for('register'))
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute("SELECT * FROM topics WHERE id = ?", (topic_id,))
    topic = c.fetchone()
    
    # Get current knowledge level
    c.execute("""
        SELECT knowledge_level 
        FROM progress 
        WHERE student_id = ? AND topic_id = ?
    """, (student_id, topic_id))
    
    progress = c.fetchone()
    knowledge_level = progress['knowledge_level'] if progress else 0
    
    # Get recent performance for adaptive difficulty
    c.execute("""
        SELECT AVG(is_correct) as accuracy, AVG(response_time) as avg_time
        FROM (
            SELECT is_correct, response_time 
            FROM interactions 
            WHERE student_id = ? AND topic_id = ?
            ORDER BY timestamp DESC 
            LIMIT 5
        )
    """, (student_id, topic_id))
    
    recent_perf = c.fetchone()
    conn.close()
    
    # Determine difficulty level using adaptive engine
    difficulty = adaptive_engine.get_next_difficulty(
        knowledge_level,
        recent_perf['accuracy'] if recent_perf['accuracy'] else 0.5,
        recent_perf['avg_time'] if recent_perf['avg_time'] else 10
    )
    
    # Get learning style for this session
    learning_style = get_student_learning_style()
    
    # Generate question (enhanced or original)
    if ENHANCED_MODE:
        question_data = content_gen.generate_question(
            topic['name'],
            difficulty,
            knowledge_level,
            learning_style
        )
    else:
        question_data = content_gen.generate_question(
            topic['name'],
            difficulty,
            knowledge_level
        )
    
    session['current_topic_id'] = topic_id
    session['current_question'] = question_data
    session['question_start_time'] = datetime.now().isoformat()
    
    # 🔊 CHANGED: Use practice.html (audio-enabled version)
    # Make sure you've renamed practice_with_audio.html to practice.html
    # OR keep both and use practice_with_audio.html here
    return render_template("practice.html",  # ← Audio-enabled template
                         topic=topic,
                         question=question_data['question'],
                         difficulty=difficulty,
                         learning_style=learning_style)  # ← Pass learning_style!

@app.route("/submit_answer", methods=["POST"])
def submit_answer():
    student_id = get_student_id()
    if not student_id:
        return jsonify({"error": "Not logged in"}), 401
    
    data = request.json
    answer = data.get('answer')
    emotion = data.get('emotion', 'neutral')
    
    topic_id = session.get('current_topic_id')
    question_data = session.get('current_question')
    
    if not topic_id or not question_data:
        return jsonify({"error": "No active question"}), 400
    
    # Calculate response time
    start_time = datetime.fromisoformat(session.get('question_start_time'))
    response_time = (datetime.now() - start_time).total_seconds()
    
    # Check answer
    is_correct = adaptive_engine.check_answer(answer, question_data['answer'])
    
    # Save interaction
    conn = get_db()
    c = conn.cursor()
    
    c.execute("""
        INSERT INTO interactions 
        (student_id, topic_id, question, answer, is_correct, 
         response_time, difficulty_level, emotion_self_report, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (student_id, topic_id, question_data['question'], answer,
          1 if is_correct else 0, response_time, question_data['difficulty'],
          emotion, datetime.now()))
    
    conn.commit()
    
    # Update session stats
    session['questions_attempted'] = session.get('questions_attempted', 0) + 1
    if is_correct:
        session['questions_correct'] = session.get('questions_correct', 0) + 1
    
    # Update knowledge level
    c.execute("""
        SELECT knowledge_level, attempts 
        FROM progress 
        WHERE student_id = ? AND topic_id = ?
    """, (student_id, topic_id))
    
    progress = c.fetchone()
    
    if progress:
        new_knowledge = adaptive_engine.update_knowledge_level(
            progress['knowledge_level'],
            is_correct,
            response_time,
            question_data['difficulty']
        )
        
        c.execute("""
            UPDATE progress 
            SET knowledge_level = ?, attempts = ?, last_accessed = ?
            WHERE student_id = ? AND topic_id = ?
        """, (new_knowledge, progress['attempts'] + 1, datetime.now(),
              student_id, topic_id))
    else:
        initial_knowledge = 0.5 if is_correct else 0.3
        c.execute("""
            INSERT INTO progress 
            (student_id, topic_id, knowledge_level, attempts, last_accessed)
            VALUES (?, ?, ?, 1, ?)
        """, (student_id, topic_id, initial_knowledge, datetime.now()))
    
    conn.commit()
    
    # Get updated knowledge level
    c.execute("""
        SELECT knowledge_level FROM progress 
        WHERE student_id = ? AND topic_id = ?
    """, (student_id, topic_id))
    
    new_progress = c.fetchone()
    new_knowledge_level = new_progress['knowledge_level']
    
    conn.close()
    
    # Generate feedback
    feedback = content_gen.generate_feedback(
        is_correct,
        question_data,
        answer,
        emotion,
        new_knowledge_level
    )
    
    # Determine next step based on emotion and performance
    next_action = adaptive_engine.determine_next_action(
        is_correct,
        emotion,
        new_knowledge_level,
        session.get('questions_attempted', 0),
        session.get('questions_correct', 0)
    )
    
    return jsonify({
        "is_correct": is_correct,
        "correct_answer": question_data['answer'],
        "explanation": question_data.get('explanation', ''),
        "feedback": feedback,
        "next_action": next_action,
        "knowledge_level": new_knowledge_level,
        "emotion_detected": emotion
    })

@app.route("/get_next_content", methods=["POST"])
def get_next_content():
    student_id = get_student_id()
    if not student_id:
        return jsonify({"error": "Not logged in"}), 401
    
    data = request.json
    action = data.get('action')
    topic_id = session.get('current_topic_id')
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute("SELECT * FROM topics WHERE id = ?", (topic_id,))
    topic = c.fetchone()
    
    c.execute("""
        SELECT knowledge_level FROM progress 
        WHERE student_id = ? AND topic_id = ?
    """, (student_id, topic_id))
    
    progress = c.fetchone()
    knowledge_level = progress['knowledge_level'] if progress else 0.5
    
    conn.close()
    
    if action == "review_material":
        # Generate review content
        if ENHANCED_MODE:
            learning_style = get_student_learning_style()
            content = content_gen.generate_review_content(
                topic['name'],
                knowledge_level,
                learning_style
            )
        else:
            content = content_gen.generate_review_content(
                topic['name'],
                knowledge_level
            )
        return jsonify({"content_type": "review", "content": content})
    
    elif action == "continue_practice":
        # Continue with next question
        return jsonify({"content_type": "redirect", "url": f"/practice/{topic_id}"})
    
    elif action == "easier_content":
        # Generate easier explanation
        if ENHANCED_MODE:
            learning_style = get_student_learning_style()
            content = content_gen.generate_learning_content(
                topic['name'],
                topic['description'],
                max(0, knowledge_level - 0.2),
                0,
                learning_style
            )
        else:
            content = content_gen.generate_learning_content(
                topic['name'],
                topic['description'],
                max(0, knowledge_level - 0.2),
                0
            )
        return jsonify({"content_type": "learn", "content": content})
    
    elif action == "end_session":
        # Save session summary
        return jsonify({"content_type": "redirect", "url": f"/session_summary/{topic_id}"})
    
    else:
        return jsonify({"error": "Unknown action"}), 400

@app.route("/session_summary/<int:topic_id>")
def session_summary(topic_id):
    student_id = get_student_id()
    if not student_id:
        return redirect(url_for('register'))
    
    attempted = session.get('questions_attempted', 0)
    correct = session.get('questions_correct', 0)
    
    conn = get_db()
    c = conn.cursor()
    
    c.execute("SELECT * FROM topics WHERE id = ?", (topic_id,))
    topic = c.fetchone()
    
    c.execute("""
        SELECT knowledge_level FROM progress 
        WHERE student_id = ? AND topic_id = ?
    """, (student_id, topic_id))
    
    progress = c.fetchone()
    knowledge_level = progress['knowledge_level'] if progress else 0
    
    # Get emotion trends from this session
    c.execute("""
        SELECT emotion_self_report, COUNT(*) as count
        FROM interactions
        WHERE student_id = ? AND topic_id = ? 
        AND timestamp >= ?
        GROUP BY emotion_self_report
    """, (student_id, topic_id, session.get('session_start', datetime.now().isoformat())))
    
    emotions = c.fetchall()
    
    conn.close()
    
    # Calculate accuracy
    accuracy = (correct / attempted * 100) if attempted > 0 else 0
    
    # Generate insights
    if ENHANCED_MODE:
        insights = content_gen.generate_session_insights(
            topic['name'],
            attempted,
            correct,
            knowledge_level,
            emotions
        )
    else:
        insights = content_gen.generate_session_insights(
            topic['name'],
            attempted,
            correct,
            knowledge_level,
            emotions
        )
    
    return render_template("session_summary.html",
                         topic=topic,
                         attempted=attempted,
                         correct=correct,
                         accuracy=accuracy,
                         knowledge_level=knowledge_level,
                         insights=insights)

@app.route("/analytics")
def analytics():
    student_id = get_student_id()
    if not student_id:
        return redirect(url_for('register'))
    
    conn = get_db()
    c = conn.cursor()
    
    # Overall progress
    c.execute("""
        SELECT t.name, p.knowledge_level, p.attempts
        FROM progress p
        JOIN topics t ON p.topic_id = t.id
        WHERE p.student_id = ?
        ORDER BY t.difficulty
    """, (student_id,))
    
    progress_data = c.fetchall()
    
    # Recent performance
    c.execute("""
        SELECT 
            DATE(timestamp) as date,
            COUNT(*) as total,
            SUM(is_correct) as correct
        FROM interactions
        WHERE student_id = ?
        GROUP BY DATE(timestamp)
        ORDER BY date DESC
        LIMIT 7
    """, (student_id,))
    
    daily_perf = c.fetchall()
    
    # Emotion patterns
    c.execute("""
        SELECT emotion_self_report, COUNT(*) as count
        FROM interactions
        WHERE student_id = ?
        GROUP BY emotion_self_report
    """, (student_id,))
    
    emotions = c.fetchall()
    
    conn.close()
    
    return render_template("analytics.html",
                         progress=progress_data,
                         daily_performance=daily_perf,
                         emotions=emotions)

if __name__ == "__main__":
    print("\n" + "="*70)
    print("  🎓 ADAPTIVE MATH LEARNING SYSTEM")
    print("="*70)
    if ENHANCED_MODE:
        print("  ✅ Mode: ENHANCED (VARK + Expanded Content)")
        print("  📚 Features: 150+ questions, VARK learning styles")
        print("  🔊 Audio: Text-to-Speech for Auditory learners")
    else:
        print("  ⚠️  Mode: ORIGINAL (Basic version)")
        print("  💡 Tip: Rename files to enable enhanced mode:")
        print("      'Expanded content bank .py' → 'expanded_content_bank.py'")
        print("      'Vark learning styles.py' → 'vark_learning_styles.py'")
    print("="*70)
    print("  🌐 Starting server at http://localhost:5000")
    print("="*70 + "\n")
    
    app.run(host="0.0.0.0", port=PORT)
