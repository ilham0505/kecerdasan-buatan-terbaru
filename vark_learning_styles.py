"""
VARK Learning Styles Implementation
Mendukung 4 gaya belajar: Visual, Auditory, Reading/Writing, Kinesthetic
"""

class VARKContentGenerator:
    """
    Generator konten berdasarkan gaya belajar VARK
    V - Visual (gambar, diagram, warna)
    A - Auditory (penjelasan verbal, instruksi lisan)
    R - Reading/Writing (teks, catatan)
    K - Kinesthetic (aktivitas, hands-on)
    """
    
    def __init__(self):
        self.vark_strategies = {
            "visual": {
                "name": "Visual Learner",
                "icon": "👁️",
                "description": "Belajar terbaik melalui gambar, diagram, dan representasi visual",
                "characteristics": [
                    "Lebih suka melihat informasi",
                    "Mengingat dengan gambar dan diagram",
                    "Suka menggunakan warna dan highlighter",
                    "Berpikir dalam gambar",
                ]
            },
            "auditory": {
                "name": "Auditory Learner",
                "icon": "👂",
                "description": "Belajar terbaik melalui mendengar dan diskusi verbal",
                "characteristics": [
                    "Lebih suka mendengar penjelasan",
                    "Mengingat apa yang didengar",
                    "Suka diskusi dan menjelaskan ke orang lain",
                    "Belajar dari mendengarkan",
                ]
            },
            "reading": {
                "name": "Reading/Writing Learner",
                "icon": "📝",
                "description": "Belajar terbaik melalui membaca dan menulis",
                "characteristics": [
                    "Lebih suka membaca teks",
                    "Suka membuat catatan",
                    "Mengingat dengan menulis",
                    "Suka list dan poin-poin",
                ]
            },
            "kinesthetic": {
                "name": "Kinesthetic Learner",
                "icon": "🤸",
                "description": "Belajar terbaik melalui praktek dan aktivitas",
                "characteristics": [
                    "Lebih suka belajar dengan melakukan",
                    "Suka gerakan dan aktivitas fisik",
                    "Mengingat dengan praktek",
                    "Hands-on learning",
                ]
            }
        }
    
    def generate_visual_content(self, topic, concept, difficulty):
        """Generate konten untuk Visual learner"""
        content = {
            "type": "visual",
            "title": f"📊 Visualisasi: {topic}",
            "elements": []
        }
        
        if topic == "Penjumlahan Dasar":
            if difficulty <= 2:
                content["elements"] = [
                    {
                        "type": "diagram",
                        "title": "Diagram Penjumlahan",
                        "description": "Gunakan gambar untuk memvisualisasikan penjumlahan:",
                        "visual_aids": [
                            "🟦🟦 + 🟦🟦🟦 = 🟦🟦🟦🟦🟦 (2 + 3 = 5)",
                            "⭐⭐⭐⭐ + ⭐⭐ = ⭐⭐⭐⭐⭐⭐ (4 + 2 = 6)",
                            "🔵🔵🔵 + 🔵🔵🔵 = 🔵🔵🔵🔵🔵🔵 (3 + 3 = 6)",
                        ]
                    },
                    {
                        "type": "number_line",
                        "title": "Garis Bilangan",
                        "description": "Untuk 5 + 3, mulai dari 5 lalu lompat 3 langkah:",
                        "representation": "←─┼─┼─┼─┼─★─┼─┼─┼─→\n  0 1 2 3 4 5 6 7 8 9"
                    },
                    {
                        "type": "color_code",
                        "title": "Penggunaan Warna",
                        "tips": [
                            "🔴 Gunakan warna merah untuk bilangan pertama",
                            "🔵 Gunakan warna biru untuk bilangan kedua",
                            "🟢 Gunakan warna hijau untuk hasil",
                        ]
                    }
                ]
            else:
                content["elements"] = [
                    {
                        "type": "place_value_chart",
                        "title": "Tabel Nilai Tempat",
                        "description": "Visualisasikan dengan tabel:\n\n  Ratusan | Puluhan | Satuan\n  --------|---------|--------\n     2    |    5    |   6\n  +  1    |    7    |   8\n  --------|---------|--------\n     4    |    3    |   4\n\nHasil: 434"
                    },
                    {
                        "type": "mind_map",
                        "title": "Peta Konsep Penjumlahan",
                        "description": "Buat mind map untuk strategi penjumlahan"
                    }
                ]
        
        elif topic == "Perkalian Dasar":
            content["elements"] = [
                {
                    "type": "array",
                    "title": "Array Model",
                    "description": "3 × 4 dapat divisualisasikan sebagai 3 baris, 4 kolom:",
                    "visual": "⭐⭐⭐⭐\n⭐⭐⭐⭐\n⭐⭐⭐⭐\n\nTotal: 12 bintang"
                },
                {
                    "type": "group",
                    "title": "Model Grup",
                    "description": "4 × 3 = 4 grup berisi 3 item:\n(⭐⭐⭐) (⭐⭐⭐) (⭐⭐⭐) (⭐⭐⭐)"
                },
                {
                    "type": "table",
                    "title": "Tabel Perkalian Visual",
                    "description": "Gunakan tabel perkalian dengan warna berbeda untuk setiap angka"
                }
            ]
        
        elif topic == "Geometri Dasar":
            content["elements"] = [
                {
                    "type": "shapes",
                    "title": "Gambar Bangun Datar",
                    "description": "Visualisasi bangun datar:\n\n□ PERSEGI\n└─ Semua sisi sama panjang\n\n▭ PERSEGI PANJANG  \n└─ 2 pasang sisi sama panjang\n\n△ SEGITIGA\n└─ 3 sisi, 3 sudut\n\n○ LINGKARAN\n└─ Bulat sempurna"
                },
                {
                    "type": "labeled_diagram",
                    "title": "Diagram Berlabel",
                    "description": "Gambar bangun dengan label pada setiap bagian (sisi, sudut, tinggi, alas)"
                }
            ]
        
        return content
    
    def generate_auditory_content(self, topic, concept, difficulty):
        """Generate konten untuk Auditory learner"""
        content = {
            "type": "auditory",
            "title": f"🗣️ Penjelasan Verbal: {topic}",
            "elements": []
        }
        
        if topic == "Penjumlahan Dasar":
            content["elements"] = [
                {
                    "type": "verbal_explanation",
                    "title": "Penjelasan Lisan",
                    "script": "Mari kita bicara tentang penjumlahan. Bayangkan aku bercerita: Kamu punya 3 kelereng di kantong kiri, dan 5 kelereng di kantong kanan. Kalau kamu gabungkan semua kelereng, berapa totalnya? Iya benar, 8 kelereng! Itu adalah penjumlahan: tiga tambah lima sama dengan delapan."
                },
                {
                    "type": "rhyme",
                    "title": "Lagu/Sajak Memori",
                    "content": [
                        "♪ Dua tambah dua menjadi empat ♪",
                        "♪ Tiga tambah tiga jadi enam ternyata ♪",
                        "♪ Lima tambah lima sepuluh hasilnya ♪",
                    ]
                },
                {
                    "type": "self_talk",
                    "title": "Bicara pada Diri Sendiri",
                    "tips": [
                        "Ucapkan soal dengan keras: 'Berapa lima tambah tiga?'",
                        "Verbalkan proses: 'Lima, lalu tambah satu jadi enam, tambah satu lagi jadi tujuh, tambah satu lagi jadi delapan'",
                        "Jelaskan ke diri sendiri kenapa jawabannya benar",
                    ]
                },
                {
                    "type": "discussion_prompt",
                    "title": "Diskusi",
                    "prompts": [
                        "Coba jelaskan cara menyelesaikan soal ini dengan kata-katamu sendiri",
                        "Ceritakan strategi yang kamu gunakan",
                        "Diskusikan dengan teman mengapa cara ini berhasil",
                    ]
                }
            ]
        
        return content
    
    def generate_reading_content(self, topic, concept, difficulty):
        """Generate konten untuk Reading/Writing learner"""
        content = {
            "type": "reading",
            "title": f"📖 Materi Tertulis: {topic}",
            "elements": []
        }
        
        if topic == "Penjumlahan Dasar":
            content["elements"] = [
                {
                    "type": "text_explanation",
                    "title": "Penjelasan Tertulis Lengkap",
                    "content": """
PENJUMLAHAN DASAR

Definisi:
Penjumlahan adalah operasi matematika yang menggabungkan dua bilangan atau lebih 
menjadi satu bilangan yang disebut jumlah.

Notasi:
• Simbol: + (baca: tambah atau plus)
• Format: a + b = c
• a dan b disebut addend
• c disebut sum (jumlah)

Sifat-sifat Penjumlahan:
1. Komutatif: a + b = b + a
   Contoh: 3 + 5 = 5 + 3 = 8
   
2. Asosiatif: (a + b) + c = a + (b + c)
   Contoh: (2 + 3) + 4 = 2 + (3 + 4) = 9
   
3. Identitas: a + 0 = a
   Contoh: 7 + 0 = 7

Langkah-langkah Menyelesaikan:
1. Identifikasi bilangan-bilangan yang akan dijumlahkan
2. Pilih strategi (counting on, decomposition, atau lainnya)
3. Lakukan operasi penjumlahan
4. Tuliskan hasil
5. Cek kembali jawaban
                    """
                },
                {
                    "type": "note_taking",
                    "title": "Panduan Membuat Catatan",
                    "tips": [
                        "Buat ringkasan dengan poin-poin penting",
                        "Tuliskan rumus dan contoh di buku catatan",
                        "Buat kartu flash dengan soal di depan, jawaban di belakang",
                        "Tulis ulang materi dengan kata-katamu sendiri",
                    ]
                },
                {
                    "type": "lists",
                    "title": "Daftar Strategi",
                    "content": """
Strategi Penjumlahan:
• Counting On - Hitung maju dari bilangan pertama
• Make Ten - Buat pasangan yang jumlahnya 10
• Decomposition - Pecah bilangan menjadi puluhan dan satuan
• Number Line - Gunakan garis bilangan
• Doubles - Gandakan bilangan yang sama (3+3, 4+4)
• Near Doubles - Gunakan doubles yang sudah diketahui (3+4 = 3+3+1)
                    """
                },
                {
                    "type": "practice_worksheet",
                    "title": "Lembar Kerja",
                    "description": "Tulis 10 soal penjumlahan dan selesaikan dengan menuliskan langkah-langkahnya"
                }
            ]
        
        return content
    
    def generate_kinesthetic_content(self, topic, concept, difficulty):
        """Generate konten untuk Kinesthetic learner"""
        content = {
            "type": "kinesthetic",
            "title": f"🤸 Aktivitas Praktis: {topic}",
            "elements": []
        }
        
        if topic == "Penjumlahan Dasar":
            content["elements"] = [
                {
                    "type": "hands_on_activity",
                    "title": "Aktivitas dengan Benda Nyata",
                    "activities": [
                        "🧮 Gunakan manik-manik atau kelereng: Ambil 3 kelereng, lalu tambah 5 lagi. Hitung totalnya.",
                        "✋ Gunakan jari: Angkat 4 jari tangan kiri, 3 jari tangan kanan. Hitung total jari yang diangkat.",
                        "📦 Kotak dan benda: Masukkan benda ke dalam kotak sambil menghitung",
                        "🎲 Dadu: Lempar 2 dadu, jumlahkan angka yang muncul",
                    ]
                },
                {
                    "type": "movement",
                    "title": "Aktivitas Gerakan",
                    "activities": [
                        "🚶 Penjumlahan dengan langkah: Untuk 5+3, ambil 5 langkah, lalu 3 langkah lagi",
                        "👏 Tepuk tangan: Tepuk 4 kali, lalu 5 kali. Berapa total tepukan?",
                        "🏃 Lompat: Lompat sambil menghitung penjumlahan",
                        "🎯 Lempar bola: Lempar bola ke target sambil berhitung",
                    ]
                },
                {
                    "type": "interactive_game",
                    "title": "Permainan Interaktif",
                    "games": [
                        "🎮 Math Hopscotch: Buat engklek dengan angka, lompat untuk menjumlahkan",
                        "🃏 Kartu angka: Ambil 2 kartu, jumlahkan nilainya",
                        "🎲 Board game matematika: Main permainan papan dengan penjumlahan",
                        "🏆 Relay matematika: Lomba estafet dengan soal penjumlahan di setiap pos",
                    ]
                },
                {
                    "type": "physical_manipulation",
                    "title": "Manipulasi Fisik",
                    "tools": [
                        "Gunakan balok Lego untuk merepresentasikan bilangan",
                        "Susun stick es krim untuk menghitung",
                        "Gunakan puzzle matematika",
                        "Mainkan dengan tangram atau pattern blocks",
                    ]
                }
            ]
        
        elif topic == "Perkalian Dasar":
            content["elements"] = [
                {
                    "type": "hands_on_activity",
                    "title": "Aktivitas Perkalian",
                    "activities": [
                        "Buat grup fisik: 3 × 4 = buat 3 grup, masing-masing 4 benda",
                        "Array dengan benda: Susun 4 baris 5 kolom dengan koin",
                        "Skip counting dengan gerakan: Loncat 2, 4, 6, 8, 10 (untuk × 2)",
                    ]
                }
            ]
        
        elif topic == "Geometri Dasar":
            content["elements"] = [
                {
                    "type": "hands_on_activity",
                    "title": "Aktivitas Geometri",
                    "activities": [
                        "Buat bangun datar dengan kertas atau kardus",
                        "Ukur benda di sekitar dengan penggaris",
                        "Gambar bangun di pasir atau tanah",
                        "Bentuk bangun dengan tali atau benang",
                        "Jalan mengelilingi bangun untuk merasakan keliling",
                    ]
                }
            ]
        
        return content
    
    def generate_multimodal_content(self, topic, concept, difficulty, preferred_style="visual"):
        """
        Generate konten yang mengintegrasikan berbagai gaya belajar
        dengan penekanan pada gaya belajar yang disukai
        """
        content = {
            "topic": topic,
            "preferred_style": preferred_style,
            "sections": []
        }
        
        # Generate konten untuk semua style tapi prioritaskan yang disukai
        if preferred_style == "visual":
            content["sections"].append(self.generate_visual_content(topic, concept, difficulty))
            content["sections"].append(self.generate_kinesthetic_content(topic, concept, difficulty))
            content["sections"].append(self.generate_reading_content(topic, concept, difficulty))
        
        elif preferred_style == "auditory":
            content["sections"].append(self.generate_auditory_content(topic, concept, difficulty))
            content["sections"].append(self.generate_kinesthetic_content(topic, concept, difficulty))
            content["sections"].append(self.generate_visual_content(topic, concept, difficulty))
        
        elif preferred_style == "reading":
            content["sections"].append(self.generate_reading_content(topic, concept, difficulty))
            content["sections"].append(self.generate_visual_content(topic, concept, difficulty))
            content["sections"].append(self.generate_auditory_content(topic, concept, difficulty))
        
        elif preferred_style == "kinesthetic":
            content["sections"].append(self.generate_kinesthetic_content(topic, concept, difficulty))
            content["sections"].append(self.generate_visual_content(topic, concept, difficulty))
            content["sections"].append(self.generate_auditory_content(topic, concept, difficulty))
        
        return content
    
    def detect_learning_style(self, interaction_history):
        """
        Deteksi gaya belajar berdasarkan interaksi siswa
        Analisis pola: response time, accuracy dengan berbagai jenis konten
        """
        style_scores = {
            "visual": 0,
            "auditory": 0,
            "reading": 0,
            "kinesthetic": 0
        }
        
        # Placeholder - bisa dikembangkan dengan ML
        # Untuk sekarang, return default
        return "visual"
    
    def get_vark_recommendations(self, learning_style):
        """Berikan rekomendasi berdasarkan gaya belajar"""
        recommendations = {
            "visual": [
                "Gunakan diagram dan gambar untuk memahami konsep",
                "Buat mind map atau flowchart",
                "Gunakan warna berbeda untuk highlightAspek penting",
                "Tonton video pembelajaran",
                "Gambar konsep dengan cara mu sendiri",
            ],
            "auditory": [
                "Bacakan soal dengan keras",
                "Diskusikan dengan teman atau guru",
                "Rekam penjelasan dan dengarkan ulang",
                "Jelaskan konsep dengan kata-kata mu sendiri",
                "Gunakan musik atau ritme untuk mengingat",
            ],
            "reading": [
                "Baca materi dengan teliti",
                "Buat catatan detail",
                "Tulis ringkasan dengan kata-kata sendiri",
                "Buat daftar dan checklist",
                "Kerjakan latihan tertulis",
            ],
            "kinesthetic": [
                "Praktikkan dengan benda nyata",
                "Gunakan gerakan untuk membantu mengingat",
                "Buat model atau bangun sesuatu",
                "Ambil break dan bergerak saat belajar",
                "Gunakan hands-on activities",
            ]
        }
        
        return recommendations.get(learning_style, recommendations["visual"])


# Fungsi utilitas
def format_vark_content_for_display(vark_content):
    """Format konten VARK untuk ditampilkan di UI"""
    html_output = []
    
    for section in vark_content["sections"]:
        html_output.append(f"<h3>{section['title']}</h3>")
        
        for element in section["elements"]:
            html_output.append(f"<h4>{element['title']}</h4>")
            
            if element["type"] == "diagram" or element["type"] == "visual_aids":
                for aid in element.get("visual_aids", []):
                    html_output.append(f"<p>{aid}</p>")
            
            elif element["type"] == "verbal_explanation":
                html_output.append(f"<p>{element['script']}</p>")
            
            elif element["type"] == "text_explanation":
                html_output.append(f"<pre>{element['content']}</pre>")
            
            elif element["type"] == "hands_on_activity":
                html_output.append("<ul>")
                for activity in element["activities"]:
                    html_output.append(f"<li>{activity}</li>")
                html_output.append("</ul>")
    
    return "\n".join(html_output)