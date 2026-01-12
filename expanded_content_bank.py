"""
Expanded Content Bank - Bank Soal dan Materi yang Diperluas
Menyediakan lebih banyak soal, materi, dan konten pembelajaran
"""

class ExpandedContentBank:
    """
    Bank konten yang diperluas dengan lebih banyak soal dan materi
    """
    
    def __init__(self):
        self.question_bank = {
            "Penjumlahan Dasar": {
                1: [  # Level 1 - Sangat Mudah
                    {"q": "1 + 1 = ?", "a": "2", "exp": "1 ditambah 1 sama dengan 2"},
                    {"q": "2 + 2 = ?", "a": "4", "exp": "2 ditambah 2 sama dengan 4"},
                    {"q": "3 + 2 = ?", "a": "5", "exp": "3 ditambah 2 sama dengan 5"},
                    {"q": "4 + 3 = ?", "a": "7", "exp": "4 ditambah 3 sama dengan 7"},
                    {"q": "5 + 4 = ?", "a": "9", "exp": "5 ditambah 4 sama dengan 9"},
                    {"q": "1 + 7 = ?", "a": "8", "exp": "1 ditambah 7 sama dengan 8"},
                    {"q": "6 + 2 = ?", "a": "8", "exp": "6 ditambah 2 sama dengan 8"},
                    {"q": "3 + 3 = ?", "a": "6", "exp": "3 ditambah 3 sama dengan 6"},
                    {"q": "7 + 1 = ?", "a": "8", "exp": "7 ditambah 1 sama dengan 8"},
                    {"q": "4 + 5 = ?", "a": "9", "exp": "4 ditambah 5 sama dengan 9"},
                ],
                2: [  # Level 2 - Mudah
                    {"q": "12 + 8 = ?", "a": "20", "exp": "12 + 8 = 20"},
                    {"q": "15 + 17 = ?", "a": "32", "exp": "15 + 17 = 32"},
                    {"q": "23 + 14 = ?", "a": "37", "exp": "23 + 14 = 37"},
                    {"q": "18 + 16 = ?", "a": "34", "exp": "18 + 16 = 34"},
                    {"q": "25 + 13 = ?", "a": "38", "exp": "25 + 13 = 38"},
                    {"q": "19 + 21 = ?", "a": "40", "exp": "19 + 21 = 40"},
                    {"q": "27 + 15 = ?", "a": "42", "exp": "27 + 15 = 42"},
                    {"q": "33 + 18 = ?", "a": "51", "exp": "33 + 18 = 51"},
                    {"q": "28 + 24 = ?", "a": "52", "exp": "28 + 24 = 52"},
                    {"q": "36 + 19 = ?", "a": "55", "exp": "36 + 19 = 55"},
                ],
                3: [  # Level 3 - Menengah
                    {"q": "45 + 67 = ?", "a": "112", "exp": "45 + 67 = 112. Tip: 45 + 60 = 105, lalu 105 + 7 = 112"},
                    {"q": "89 + 34 = ?", "a": "123", "exp": "89 + 34 = 123. Tip: 89 + 30 = 119, lalu 119 + 4 = 123"},
                    {"q": "58 + 76 = ?", "a": "134", "exp": "58 + 76 = 134"},
                    {"q": "93 + 48 = ?", "a": "141", "exp": "93 + 48 = 141"},
                    {"q": "67 + 85 = ?", "a": "152", "exp": "67 + 85 = 152"},
                    {"q": "72 + 59 = ?", "a": "131", "exp": "72 + 59 = 131"},
                    {"q": "84 + 77 = ?", "a": "161", "exp": "84 + 77 = 161"},
                    {"q": "96 + 68 = ?", "a": "164", "exp": "96 + 68 = 164"},
                    {"q": "53 + 89 = ?", "a": "142", "exp": "53 + 89 = 142"},
                    {"q": "78 + 94 = ?", "a": "172", "exp": "78 + 94 = 172"},
                ],
                4: [  # Level 4 - Sulit
                    {"q": "156 + 237 = ?", "a": "393", "exp": "156 + 237 = 393"},
                    {"q": "284 + 365 = ?", "a": "649", "exp": "284 + 365 = 649"},
                    {"q": "412 + 298 = ?", "a": "710", "exp": "412 + 298 = 710"},
                    {"q": "567 + 384 = ?", "a": "951", "exp": "567 + 384 = 951"},
                    {"q": "629 + 473 = ?", "a": "1102", "exp": "629 + 473 = 1102"},
                    {"q": "745 + 586 = ?", "a": "1331", "exp": "745 + 586 = 1331"},
                    {"q": "893 + 647 = ?", "a": "1540", "exp": "893 + 647 = 1540"},
                    {"q": "512 + 799 = ?", "a": "1311", "exp": "512 + 799 = 1311"},
                    {"q": "678 + 854 = ?", "a": "1532", "exp": "678 + 854 = 1532"},
                    {"q": "926 + 738 = ?", "a": "1664", "exp": "926 + 738 = 1664"},
                ],
                5: [  # Level 5 - Sangat Sulit
                    {"q": "1234 + 5678 = ?", "a": "6912", "exp": "1234 + 5678 = 6912"},
                    {"q": "2847 + 6193 = ?", "a": "9040", "exp": "2847 + 6193 = 9040"},
                    {"q": "3956 + 7284 = ?", "a": "11240", "exp": "3956 + 7284 = 11240"},
                    {"q": "4729 + 8365 = ?", "a": "13094", "exp": "4729 + 8365 = 13094"},
                    {"q": "5618 + 9473 = ?", "a": "15091", "exp": "5618 + 9473 = 15091"},
                ],
            },
            "Pengurangan Dasar": {
                1: [
                    {"q": "5 - 2 = ?", "a": "3", "exp": "5 dikurangi 2 sama dengan 3"},
                    {"q": "8 - 3 = ?", "a": "5", "exp": "8 dikurangi 3 sama dengan 5"},
                    {"q": "9 - 4 = ?", "a": "5", "exp": "9 dikurangi 4 sama dengan 5"},
                    {"q": "7 - 2 = ?", "a": "5", "exp": "7 dikurangi 2 sama dengan 5"},
                    {"q": "10 - 6 = ?", "a": "4", "exp": "10 dikurangi 6 sama dengan 4"},
                    {"q": "6 - 1 = ?", "a": "5", "exp": "6 dikurangi 1 sama dengan 5"},
                    {"q": "8 - 5 = ?", "a": "3", "exp": "8 dikurangi 5 sama dengan 3"},
                    {"q": "9 - 7 = ?", "a": "2", "exp": "9 dikurangi 7 sama dengan 2"},
                    {"q": "10 - 3 = ?", "a": "7", "exp": "10 dikurangi 3 sama dengan 7"},
                    {"q": "7 - 4 = ?", "a": "3", "exp": "7 dikurangi 4 sama dengan 3"},
                ],
                2: [
                    {"q": "25 - 12 = ?", "a": "13", "exp": "25 - 12 = 13"},
                    {"q": "34 - 18 = ?", "a": "16", "exp": "34 - 18 = 16"},
                    {"q": "42 - 27 = ?", "a": "15", "exp": "42 - 27 = 15"},
                    {"q": "51 - 29 = ?", "a": "22", "exp": "51 - 29 = 22"},
                    {"q": "63 - 35 = ?", "a": "28", "exp": "63 - 35 = 28"},
                    {"q": "47 - 19 = ?", "a": "28", "exp": "47 - 19 = 28"},
                    {"q": "56 - 28 = ?", "a": "28", "exp": "56 - 28 = 28"},
                    {"q": "68 - 39 = ?", "a": "29", "exp": "68 - 39 = 29"},
                    {"q": "75 - 46 = ?", "a": "29", "exp": "75 - 46 = 29"},
                    {"q": "82 - 54 = ?", "a": "28", "exp": "82 - 54 = 28"},
                ],
                3: [
                    {"q": "112 - 67 = ?", "a": "45", "exp": "112 - 67 = 45"},
                    {"q": "145 - 89 = ?", "a": "56", "exp": "145 - 89 = 56"},
                    {"q": "178 - 93 = ?", "a": "85", "exp": "178 - 93 = 85"},
                    {"q": "203 - 128 = ?", "a": "75", "exp": "203 - 128 = 75"},
                    {"q": "256 - 179 = ?", "a": "77", "exp": "256 - 179 = 77"},
                ],
            },
            "Perkalian Dasar": {
                1: [
                    {"q": "2 × 2 = ?", "a": "4", "exp": "2 dikali 2 sama dengan 4"},
                    {"q": "3 × 2 = ?", "a": "6", "exp": "3 dikali 2 sama dengan 6"},
                    {"q": "4 × 2 = ?", "a": "8", "exp": "4 dikali 2 sama dengan 8"},
                    {"q": "5 × 2 = ?", "a": "10", "exp": "5 dikali 2 sama dengan 10"},
                    {"q": "3 × 3 = ?", "a": "9", "exp": "3 dikali 3 sama dengan 9"},
                    {"q": "4 × 3 = ?", "a": "12", "exp": "4 dikali 3 sama dengan 12"},
                    {"q": "5 × 3 = ?", "a": "15", "exp": "5 dikali 3 sama dengan 15"},
                    {"q": "2 × 5 = ?", "a": "10", "exp": "2 dikali 5 sama dengan 10"},
                    {"q": "6 × 2 = ?", "a": "12", "exp": "6 dikali 2 sama dengan 12"},
                    {"q": "7 × 2 = ?", "a": "14", "exp": "7 dikali 2 sama dengan 14"},
                ],
                2: [
                    {"q": "6 × 7 = ?", "a": "42", "exp": "6 × 7 = 42"},
                    {"q": "8 × 5 = ?", "a": "40", "exp": "8 × 5 = 40"},
                    {"q": "9 × 4 = ?", "a": "36", "exp": "9 × 4 = 36"},
                    {"q": "7 × 8 = ?", "a": "56", "exp": "7 × 8 = 56"},
                    {"q": "6 × 9 = ?", "a": "54", "exp": "6 × 9 = 54"},
                    {"q": "8 × 8 = ?", "a": "64", "exp": "8 × 8 = 64"},
                    {"q": "9 × 7 = ?", "a": "63", "exp": "9 × 7 = 63"},
                    {"q": "12 × 5 = ?", "a": "60", "exp": "12 × 5 = 60"},
                    {"q": "11 × 6 = ?", "a": "66", "exp": "11 × 6 = 66"},
                    {"q": "9 × 9 = ?", "a": "81", "exp": "9 × 9 = 81"},
                ],
                3: [
                    {"q": "15 × 12 = ?", "a": "180", "exp": "15 × 12 = 180"},
                    {"q": "18 × 14 = ?", "a": "252", "exp": "18 × 14 = 252"},
                    {"q": "23 × 11 = ?", "a": "253", "exp": "23 × 11 = 253"},
                    {"q": "25 × 16 = ?", "a": "400", "exp": "25 × 16 = 400"},
                    {"q": "27 × 13 = ?", "a": "351", "exp": "27 × 13 = 351"},
                ],
            },
            "Pembagian Dasar": {
                1: [
                    {"q": "6 ÷ 2 = ?", "a": "3", "exp": "6 dibagi 2 sama dengan 3"},
                    {"q": "8 ÷ 2 = ?", "a": "4", "exp": "8 dibagi 2 sama dengan 4"},
                    {"q": "10 ÷ 2 = ?", "a": "5", "exp": "10 dibagi 2 sama dengan 5"},
                    {"q": "12 ÷ 3 = ?", "a": "4", "exp": "12 dibagi 3 sama dengan 4"},
                    {"q": "15 ÷ 3 = ?", "a": "5", "exp": "15 dibagi 3 sama dengan 5"},
                    {"q": "20 ÷ 4 = ?", "a": "5", "exp": "20 dibagi 4 sama dengan 5"},
                    {"q": "18 ÷ 3 = ?", "a": "6", "exp": "18 dibagi 3 sama dengan 6"},
                    {"q": "16 ÷ 4 = ?", "a": "4", "exp": "16 dibagi 4 sama dengan 4"},
                    {"q": "25 ÷ 5 = ?", "a": "5", "exp": "25 dibagi 5 sama dengan 5"},
                    {"q": "30 ÷ 5 = ?", "a": "6", "exp": "30 dibagi 5 sama dengan 6"},
                ],
                2: [
                    {"q": "42 ÷ 6 = ?", "a": "7", "exp": "42 ÷ 6 = 7"},
                    {"q": "56 ÷ 8 = ?", "a": "7", "exp": "56 ÷ 8 = 7"},
                    {"q": "63 ÷ 9 = ?", "a": "7", "exp": "63 ÷ 9 = 7"},
                    {"q": "72 ÷ 8 = ?", "a": "9", "exp": "72 ÷ 8 = 9"},
                    {"q": "81 ÷ 9 = ?", "a": "9", "exp": "81 ÷ 9 = 9"},
                ],
            },
            "Pecahan": {
                1: [
                    {"q": "1/2 + 1/2 = ?", "a": "1", "exp": "Setengah + setengah = satu utuh"},
                    {"q": "1/4 + 1/4 = ?", "a": "1/2", "exp": "Seperempat + seperempat = setengah"},
                    {"q": "2/3 + 1/3 = ?", "a": "1", "exp": "Dua pertiga + satu pertiga = satu utuh"},
                    {"q": "1/5 + 2/5 = ?", "a": "3/5", "exp": "Satu perlima + dua perlima = tiga perlima"},
                    {"q": "3/4 - 1/4 = ?", "a": "1/2", "exp": "Tiga perempat - satu perempat = setengah"},
                ],
                2: [
                    {"q": "1/2 + 1/4 = ?", "a": "3/4", "exp": "1/2 = 2/4, maka 2/4 + 1/4 = 3/4"},
                    {"q": "2/3 + 1/6 = ?", "a": "5/6", "exp": "2/3 = 4/6, maka 4/6 + 1/6 = 5/6"},
                    {"q": "3/4 - 1/2 = ?", "a": "1/4", "exp": "3/4 - 2/4 = 1/4"},
                    {"q": "1/2 × 2 = ?", "a": "1", "exp": "Setengah dikali dua sama dengan satu utuh"},
                    {"q": "1/3 × 3 = ?", "a": "1", "exp": "Sepertiga dikali tiga sama dengan satu utuh"},
                ],
            },
            "Geometri Dasar": {
                1: [
                    {"q": "Persegi dengan sisi 3 cm, berapa kelilingnya?", "a": "12", "exp": "Keliling persegi = 4 × sisi = 4 × 3 = 12 cm"},
                    {"q": "Persegi dengan sisi 5 cm, berapa kelilingnya?", "a": "20", "exp": "Keliling = 4 × 5 = 20 cm"},
                    {"q": "Persegi dengan sisi 4 cm, berapa luasnya?", "a": "16", "exp": "Luas = sisi × sisi = 4 × 4 = 16 cm²"},
                    {"q": "Persegi panjang panjang 5 cm dan lebar 3 cm, berapa luasnya?", "a": "15", "exp": "Luas = panjang × lebar = 5 × 3 = 15 cm²"},
                    {"q": "Persegi panjang panjang 6 cm dan lebar 4 cm, berapa kelilingnya?", "a": "20", "exp": "Keliling = 2 × (panjang + lebar) = 2 × (6 + 4) = 20 cm"},
                ],
                2: [
                    {"q": "Segitiga dengan alas 6 cm dan tinggi 4 cm, berapa luasnya?", "a": "12", "exp": "Luas segitiga = ½ × alas × tinggi = ½ × 6 × 4 = 12 cm²"},
                    {"q": "Segitiga dengan alas 10 cm dan tinggi 5 cm, berapa luasnya?", "a": "25", "exp": "Luas = ½ × 10 × 5 = 25 cm²"},
                    {"q": "Lingkaran dengan jari-jari 7 cm, berapa kelilingnya? (π = 22/7)", "a": "44", "exp": "Keliling = 2 × π × r = 2 × 22/7 × 7 = 44 cm"},
                    {"q": "Persegi panjang panjang 8 cm dan lebar 5 cm, berapa luasnya?", "a": "40", "exp": "Luas = 8 × 5 = 40 cm²"},
                    {"q": "Persegi dengan sisi 6 cm, berapa luasnya?", "a": "36", "exp": "Luas = 6 × 6 = 36 cm²"},
                ],
            },
            "Aljabar Sederhana": {
                1: [
                    {"q": "x + 3 = 8, maka x = ?", "a": "5", "exp": "x = 8 - 3 = 5"},
                    {"q": "x + 5 = 12, maka x = ?", "a": "7", "exp": "x = 12 - 5 = 7"},
                    {"q": "x - 4 = 6, maka x = ?", "a": "10", "exp": "x = 6 + 4 = 10"},
                    {"q": "2x = 10, maka x = ?", "a": "5", "exp": "x = 10 ÷ 2 = 5"},
                    {"q": "3x = 15, maka x = ?", "a": "5", "exp": "x = 15 ÷ 3 = 5"},
                ],
                2: [
                    {"q": "2x + 3 = 11, maka x = ?", "a": "4", "exp": "2x = 11 - 3 = 8, maka x = 8 ÷ 2 = 4"},
                    {"q": "3x - 5 = 10, maka x = ?", "a": "5", "exp": "3x = 10 + 5 = 15, maka x = 15 ÷ 3 = 5"},
                    {"q": "4x + 2 = 18, maka x = ?", "a": "4", "exp": "4x = 18 - 2 = 16, maka x = 16 ÷ 4 = 4"},
                    {"q": "5x - 7 = 13, maka x = ?", "a": "4", "exp": "5x = 13 + 7 = 20, maka x = 20 ÷ 5 = 4"},
                    {"q": "2x + 6 = 16, maka x = ?", "a": "5", "exp": "2x = 16 - 6 = 10, maka x = 10 ÷ 2 = 5"},
                ],
            },
        }
        
        # Materi pembelajaran yang lebih lengkap
        self.learning_materials = {
            "Penjumlahan Dasar": {
                "basic": {
                    "introduction": "Penjumlahan adalah operasi matematika dasar yang menggabungkan dua bilangan atau lebih menjadi satu bilangan yang lebih besar. Bayangkan kamu punya 2 kelereng, lalu temanmu memberi 3 kelereng lagi. Sekarang kamu punya 5 kelereng! Itulah penjumlahan: 2 + 3 = 5.",
                    "concepts": [
                        "Penjumlahan menggunakan simbol '+' (baca: tambah atau plus)",
                        "Hasil penjumlahan disebut 'jumlah'",
                        "Urutan bilangan tidak mempengaruhi hasil (3+5 sama dengan 5+3)",
                        "Menambah 0 tidak mengubah bilangan (5+0 = 5)",
                    ],
                    "strategies": [
                        "Counting On: Mulai dari bilangan pertama, hitung maju sebanyak bilangan kedua",
                        "Gunakan jari untuk membantu menghitung",
                        "Visualisasikan dengan benda konkret (kelereng, pensil, dll)",
                        "Buat garis bilangan untuk membantu",
                    ],
                    "examples": [
                        "3 + 2: Mulai dari 3, hitung 2 langkah → 4, 5. Jadi hasilnya 5",
                        "5 + 4: Mulai dari 5, hitung 4 langkah → 6, 7, 8, 9. Jadi hasilnya 9",
                        "7 + 3: Mulai dari 7, hitung 3 langkah → 8, 9, 10. Jadi hasilnya 10",
                    ]
                },
                "intermediate": {
                    "introduction": "Sekarang kita akan belajar penjumlahan bilangan yang lebih besar. Tidak perlu khawatir, ada trik-trik yang bisa membuat penjumlahan lebih mudah!",
                    "concepts": [
                        "Decomposition: Pecah bilangan menjadi puluhan dan satuan",
                        "Make Ten: Cari cara membuat 10 terlebih dahulu",
                        "Rounding: Bulatkan ke 10-an terdekat, lalu sesuaikan",
                        "Sifat komutatif: a + b = b + a",
                        "Sifat asosiatif: (a + b) + c = a + (b + c)",
                    ],
                    "strategies": [
                        "Untuk 25 + 37: Pisahkan (20+30) + (5+7) = 50 + 12 = 62",
                        "Untuk 48 + 35: Bulatkan 48 ke 50, jadi (50+35) - 2 = 85 - 2 = 83",
                        "Cari pasangan yang menghasilkan 10 untuk mempermudah",
                    ],
                    "examples": [
                        "23 + 45 = (20+40) + (3+5) = 60 + 8 = 68",
                        "37 + 28 = (37 + 3) + (28 - 3) = 40 + 25 = 65",
                        "56 + 44 = 100 (karena 56 + 40 = 96, lalu + 4 = 100)",
                    ]
                },
                "advanced": {
                    "introduction": "Pada level mahir, kita akan menguasai penjumlahan bilangan besar dan strategi mental math yang efisien.",
                    "concepts": [
                        "Left-to-right addition: Tambahkan dari kiri ke kanan",
                        "Compensating: Sesuaikan salah satu bilangan untuk mempermudah",
                        "Breaking apart: Pecah bilangan dengan cara yang paling efisien",
                        "Estimation: Perkirakan hasil untuk mengecek jawaban",
                    ],
                    "strategies": [
                        "256 + 378 = (200+300) + (50+70) + (6+8) = 500 + 120 + 14 = 634",
                        "Untuk cek: 256 ≈ 260, 378 ≈ 380, jadi sekitar 640 ✓",
                        "Gunakan sifat-sifat penjumlahan untuk mempercepat",
                    ]
                }
            },
            "Perkalian Dasar": {
                "basic": {
                    "introduction": "Perkalian adalah penjumlahan berulang. Jadi 3 × 4 artinya 3 ditambahkan sebanyak 4 kali: 3 + 3 + 3 + 3 = 12. Perkalian membuat hitungan lebih cepat dan efisien!",
                    "concepts": [
                        "Perkalian menggunakan simbol '×' atau '*'",
                        "Hasil perkalian disebut 'hasil kali'",
                        "Perkalian adalah penjumlahan berulang",
                        "Mengalikan dengan 1 tidak mengubah bilangan",
                        "Mengalikan dengan 0 hasilnya selalu 0",
                    ],
                    "strategies": [
                        "Visualisasikan sebagai grup: 4 × 3 = 4 grup berisi 3 item",
                        "Gunakan array (susunan baris dan kolom)",
                        "Mulai hafalkan tabel perkalian 1-5 dulu",
                        "Skip counting: untuk 3×4, hitung 3, 6, 9, 12",
                    ]
                },
                "intermediate": {
                    "introduction": "Sekarang kita akan menguasai tabel perkalian dan strategi perkalian yang lebih efisien.",
                    "concepts": [
                        "Tabel perkalian 1-10 sangat penting untuk dihafal",
                        "Sifat komutatif: a × b = b × a",
                        "Sifat distributif: a × (b + c) = (a × b) + (a × c)",
                        "Trik perkalian 9: Turunkan 1, pasangkan dengan yang jumlahnya 9",
                    ],
                    "strategies": [
                        "Untuk × 9: 7 × 9 = (7-1) dan (9-6) = 63",
                        "Untuk × 5: Kalikan 10, lalu bagi 2",
                        "Doubling: 7 × 8 = 7 × 4 × 2 = 28 × 2 = 56",
                    ]
                }
            },
            "Geometri Dasar": {
                "basic": {
                    "introduction": "Geometri adalah cabang matematika yang mempelajari bentuk, ukuran, dan posisi benda. Mari kita mulai dengan bangun datar sederhana!",
                    "concepts": [
                        "Persegi: 4 sisi sama panjang, 4 sudut siku-siku",
                        "Persegi panjang: 2 pasang sisi sejajar sama panjang",
                        "Segitiga: 3 sisi dan 3 sudut",
                        "Lingkaran: Bentuk bulat sempurna",
                        "Keliling: Panjang semua sisi yang mengelilingi bangun",
                        "Luas: Ukuran bidang yang tertutup bangun",
                    ],
                    "formulas": {
                        "Persegi": {
                            "keliling": "4 × sisi",
                            "luas": "sisi × sisi"
                        },
                        "Persegi Panjang": {
                            "keliling": "2 × (panjang + lebar)",
                            "luas": "panjang × lebar"
                        }
                    }
                },
                "intermediate": {
                    "concepts": [
                        "Segitiga: Luas = ½ × alas × tinggi",
                        "Lingkaran: Keliling = 2 × π × jari-jari, Luas = π × r²",
                        "Jajar genjang: Luas = alas × tinggi",
                        "Trapesium: Luas = ½ × (a + b) × tinggi",
                    ]
                }
            },
            "Aljabar Sederhana": {
                "basic": {
                    "introduction": "Aljabar menggunakan huruf (variabel) untuk mewakili angka yang belum kita ketahui. Ini seperti teka-teki matematika yang seru! Huruf x, y, atau yang lain bisa mewakili bilangan apa saja.",
                    "concepts": [
                        "Variabel adalah simbol (huruf) yang mewakili bilangan",
                        "Persamaan adalah kalimat matematika dengan tanda '='",
                        "Kedua ruas persamaan harus seimbang",
                        "Untuk menyelesaikan, isolasi variabel di satu ruas",
                    ],
                    "strategies": [
                        "x + 5 = 12 → Kurangi 5 dari kedua ruas → x = 7",
                        "2x = 10 → Bagi kedua ruas dengan 2 → x = 5",
                        "x - 3 = 7 → Tambah 3 ke kedua ruas → x = 10",
                        "Selalu cek jawaban dengan mensubstitusi kembali",
                    ]
                }
            }
        }
        
    def get_questions(self, topic_name, difficulty):
        """Ambil soal berdasarkan topik dan tingkat kesulitan"""
        if topic_name in self.question_bank:
            questions = self.question_bank[topic_name].get(difficulty, [])
            return questions
        return []
    
    def get_learning_material(self, topic_name, level="basic"):
        """Ambil materi pembelajaran"""
        if topic_name in self.learning_materials:
            return self.learning_materials[topic_name].get(level, {})
        return {}