import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Konfigurasi Halaman
st.set_page_config(page_title="Media Pembelajaran JKW Dinamis", layout="wide")
st.title("🚀 Media Pembelajaran Matematika Dinamis: Jarak, Kecepatan, Waktu")

st.markdown("""
Halo, siswa-siswi! Selamat datang di media pembelajaran interaktif untuk memahami konsep **Jarak, Kecepatan, dan Waktu** dalam skenario sehari-hari.
Kita akan mengeksplorasi kapan dan di mana dua objek akan **susul menyusul** atau **bertemu di jalan**.
Siap untuk bereksperimen dan menemukan rumusnya sendiri? Mari kita mulai!
""")

# ========================
# 📘 Pengantar / Materi Awal
# ========================
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Bagian:", ["Pengantar", "Virtual Laboratory", "Kuis"])

if menu == "Pengantar":
    st.header("1. Pengantar: Konsep Jarak, Kecepatan, dan Waktu")
    st.markdown("""
    Dalam kehidupan sehari-hari, kita sering berinteraksi dengan konsep perjalanan. Untuk memahami perjalanan, ada tiga elemen utama yang perlu kita ketahui:

    * **Jarak (S)**: Seberapa jauh suatu benda telah bergerak dari titik awalnya. Satuan umumnya adalah kilometer (km) atau meter (m).
    * **Kecepatan (v)**: Seberapa cepat suatu benda bergerak. Ini adalah perbandingan antara jarak yang ditempuh dengan waktu yang dibutuhkan. Satuan umumnya adalah kilometer per jam (km/jam) atau meter per detik (m/s).
    * **Waktu (t)**: Durasi pergerakan suatu benda. Satuan umumnya adalah jam (jam) atau detik (s).

    

    **Skenario Khusus:**
    Dalam media ini, kita akan fokus pada dua skenario menarik:
    1.  **Susul Menyusul**: Kapan dan di mana satu objek (yang lebih cepat) akan menyusul objek lain yang bergerak dari titik yang sama (atau dengan jarak tempuh awal yang berbeda).
    2.  **Bertemu di Jalan**: Kapan dan di mana dua objek yang bergerak saling mendekat dari dua titik berbeda akan bertemu.

    Mari kita eksplorasi konsep ini lebih dalam di Virtual Laboratory!
    """)

elif menu == "Virtual Laboratory":
    st.header("2. Virtual Laboratory: Simulasi Jarak, Kecepatan, dan Waktu")
    st.markdown("""
    Gunakan simulasi di bawah ini untuk mengubah parameter dan mengamati bagaimana waktu dan jarak susul menyusul atau bertemu berubah.
    Ini adalah "laboratorium" virtualmu untuk menemukan pola dan rumus!
    """)

    scenario = st.radio("Pilih Skenario Simulasi:", ["Susul Menyusul", "Bertemu di Jalan"])

    if scenario == "Susul Menyusul":
        st.subheader("Scenario: Susul Menyusul 🚗💨")
        st.markdown("""
        Dua kendaraan berangkat dari titik yang sama (atau dengan titik awal yang sama secara efektif). Kendaraan A bergerak lebih dulu atau lebih lambat, dan Kendaraan B akan menyusulnya.
        """)

        col_input_sm, col_vis_sm = st.columns([1.5, 2])

        with col_input_sm:
            st.subheader("Input Parameter")
            v1_sm = st.slider("Kecepatan Kendaraan A (km/jam)", 10, 150, 60, key="v1_sm")
            v2_sm = st.slider("Kecepatan Kendaraan B (km/jam)", 10, 150, 80, key="v2_sm")
            
            if v2_sm <= v1_sm:
                st.warning("Kecepatan Kendaraan B harus lebih besar dari Kendaraan A agar terjadi susul menyusul.")
                st.stop()

            waktu_beda_sm = st.slider("Perbedaan Waktu Keberangkatan (jam) - B berangkat setelah A", 0.0, 5.0, 0.5, 0.1, key="w_beda_sm")
            st.info(f"Kendaraan B berangkat {waktu_beda_sm} jam setelah Kendaraan A.")

            st.subheader("Hasil Simulasi")
            # Jarak yang ditempuh A saat B mulai bergerak
            jarak_a_awal = v1_sm * waktu_beda_sm

            # Kecepatan relatif B terhadap A
            v_relatif_sm = v2_sm - v1_sm

            # Waktu B menyusul A (dihitung dari saat B berangkat)
            if v_relatif_sm > 0:
                t_susul_b = jarak_a_awal / v_relatif_sm
                jarak_susul = v2_sm * t_susul_b
                waktu_total_a = waktu_beda_sm + t_susul_b

                st.success(f"Kendaraan B akan menyusul Kendaraan A dalam **{t_susul_b:.2f} jam** setelah B berangkat.")
                st.success(f"Mereka akan menyusul pada jarak **{jarak_susul:.2f} km** dari titik awal.")
                st.info(f"Total waktu perjalanan Kendaraan A sampai disusul adalah {waktu_total_a:.2f} jam.")
            else:
                st.error("Kendaraan B tidak akan pernah menyusul Kendaraan A.")

        with col_vis_sm:
            st.subheader("Visualisasi Pergerakan")
            max_time_plot = waktu_total_a + 1 if 'waktu_total_a' in locals() else 5
            times = np.linspace(0, max_time_plot, 100)
            
            # Posisi Kendaraan A
            pos_a = np.where(times >= 0, v1_sm * times, 0)
            
            # Posisi Kendaraan B
            pos_b = np.where(times >= waktu_beda_sm, v2_sm * (times - waktu_beda_sm), 0)

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.plot(times, pos_a, label=f'Kendaraan A (v={v1_sm} km/jam)', color='blue', linewidth=2)
            ax.plot(times, pos_b, label=f'Kendaraan B (v={v2_sm} km/jam)', color='red', linestyle='--', linewidth=2)

            if 't_susul_b' in locals():
                ax.plot(waktu_total_a, jarak_susul, 'go', markersize=8, label=f'Titik Susul ({waktu_total_a:.2f} jam, {jarak_susul:.2f} km)')
                
            ax.set_xlabel("Waktu (jam)", fontsize=12)
            ax.set_ylabel("Jarak dari Titik Awal (km)", fontsize=12)
            ax.set_title("Grafik Jarak vs Waktu (Susul Menyusul)", fontsize=14)
            ax.legend()
            ax.grid(True)
            st.pyplot(fig)

    elif scenario == "Bertemu di Jalan":
        st.subheader("Scenario: Bertemu di Jalan 🤝🛣️")
        st.markdown("""
        Dua kendaraan bergerak dari dua lokasi berbeda, saling mendekati satu sama lain.
        """)

        col_input_b, col_vis_b = st.columns([1.5, 2])

        with col_input_b:
            st.subheader("Input Parameter")
            v1_b = st.slider("Kecepatan Kendaraan A (km/jam)", 10, 150, 70, key="v1_b")
            v2_b = st.slider("Kecepatan Kendaraan B (km/jam)", 10, 150, 50, key="v2_b")
            jarak_awal_b = st.slider("Jarak Awal Antar Kendaraan (km)", 50, 500, 300, key="j_awal_b")
            waktu_beda_b = st.slider("Perbedaan Waktu Keberangkatan (jam) - B berangkat setelah A", 0.0, 5.0, 0.0, 0.1, key="w_beda_b")
            st.info(f"Kendaraan B berangkat {waktu_beda_b} jam setelah Kendaraan A.")

            st.subheader("Hasil Simulasi")
            
            # Jarak yang ditempuh A sebelum B berangkat
            jarak_tempuh_a_awal_b = v1_b * waktu_beda_b
            
            # Sisa jarak yang harus ditempuh bersama
            sisa_jarak = jarak_awal_b - jarak_tempuh_a_awal_b

            # Kecepatan relatif (total kecepatan saat saling mendekat)
            v_relatif_b = v1_b + v2_b

            if sisa_jarak <= 0:
                st.error("Kendaraan A sudah melewati atau hampir mencapai titik keberangkatan B sebelum B berangkat. Sesuaikan jarak awal atau waktu beda.")
                st.stop()

            # Waktu bertemu (dihitung dari saat B berangkat)
            t_bertemu_b = sisa_jarak / v_relatif_b
            
            # Waktu total dari keberangkatan A
            waktu_total_a_bertemu = waktu_beda_b + t_bertemu_b

            # Jarak pertemuan dari titik awal A
            jarak_pertemuan_dari_a = v1_b * waktu_total_a_bertemu

            st.success(f"Mereka akan bertemu dalam **{t_bertemu_b:.2f} jam** setelah Kendaraan B berangkat.")
            st.success(f"Total waktu perjalanan Kendaraan A sampai bertemu adalah **{waktu_total_a_bertemu:.2f} jam**.")
            st.success(f"Mereka akan bertemu pada jarak **{jarak_pertemuan_dari_a:.2f} km** dari titik awal Kendaraan A.")
            st.info(f"Jarak pertemuan dari titik awal Kendaraan B adalah **{jarak_awal_b - jarak_pertemuan_dari_a:.2f} km**.")

        with col_vis_b:
            st.subheader("Visualisasi Pergerakan")
            max_time_plot_b = waktu_total_a_bertemu + 1 if 'waktu_total_a_bertemu' in locals() else 5
            times_b = np.linspace(0, max_time_plot_b, 100)
            
            # Posisi Kendaraan A dari titik awal A
            pos_a_b = np.where(times_b >= 0, v1_b * times_b, 0)
            
            # Posisi Kendaraan B dari titik awal A (jarak_awal - jarak tempuh B)
            pos_b_from_a = np.where(times_b >= waktu_beda_b, jarak_awal_b - v2_b * (times_b - waktu_beda_b), jarak_awal_b)

            fig_b, ax_b = plt.subplots(figsize=(10, 6))
            ax_b.plot(times_b, pos_a_b, label=f'Kendaraan A (v={v1_b} km/jam) dari Titik A', color='blue', linewidth=2)
            ax_b.plot(times_b, pos_b_from_a, label=f'Kendaraan B (v={v2_b} km/jam) dari Titik B', color='red', linestyle='--', linewidth=2)

            if 'waktu_total_a_bertemu' in locals():
                ax_b.plot(waktu_total_a_bertemu, jarak_pertemuan_dari_a, 'go', markersize=8, label=f'Titik Bertemu ({waktu_total_a_bertemu:.2f} jam, {jarak_pertemuan_dari_a:.2f} km dari A)')
                
            ax_b.set_xlabel("Waktu (jam)", fontsize=12)
            ax_b.set_ylabel("Jarak dari Titik Awal A (km)", fontsize=12)
            ax_b.set_title("Grafik Jarak vs Waktu (Bertemu di Jalan)", fontsize=14)
            ax_b.legend()
            ax_b.grid(True)
            ax_b.set_ylim(0, jarak_awal_b + 50) # Ensure full range is visible
            st.pyplot(fig_b)

    st.markdown("---")
    st.subheader("🧠 Refleksi: Apa yang Kamu Pelajari?")
    st.markdown("""
    Setelah mencoba simulasi di atas, coba jawab pertanyaan-pertanyaan berikut:

    * Bagaimana perbedaan kecepatan memengaruhi waktu yang dibutuhkan untuk susul menyusul?
    * Jika dua kendaraan bergerak saling mendekati, bagaimana total jarak awal memengaruhi waktu mereka bertemu?
    * Bisakah kamu merumuskan persamaan umum untuk waktu susul menyusul dan waktu bertemu berdasarkan parameter yang ada?
    """)

elif menu == "Kuis":
    st.header("3. Kuis: Uji Pemahamanmu!")
    st.markdown("Jawablah pertanyaan-pertanyaan berikut untuk menguji pemahamanmu tentang konsep jarak, kecepatan, dan waktu.")

    score = 0

    st.subheader("Soal Pilihan Ganda")
    st.write("1. Dua mobil berangkat dari kota yang sama. Mobil A melaju 60 km/jam, dan Mobil B melaju 80 km/jam. Jika keduanya berangkat pada waktu yang sama, berapa waktu yang dibutuhkan Mobil B untuk berada 40 km di depan Mobil A?")
    
    q1_options = {
        "A. 1 jam": False,
        "B. 1.5 jam": False,
        "C. 2 jam": True,
        "D. 2.5 jam": False
    }
    q1_answer = st.radio("Pilih jawabanmu:", list(q1_options.keys()), key="q1")

    if st.button("Cek Jawaban Soal 1", key="btn1"):
        if q1_options[q1_answer]:
            st.success("Jawabanmu benar! (Penjelasan: Jarak relatif = 40 km, Kecepatan relatif = 80-60 = 20 km/jam. Waktu = Jarak Relatif / Kecepatan Relatif = 40/20 = 2 jam)")
            score += 1
        else:
            st.error("Jawabanmu salah. Coba pikirkan kembali konsep kecepatan relatif.")

    st.subheader("Soal Isian Singkat")
    st.write("2. Kota A dan Kota B berjarak 300 km. Mobil P berangkat dari Kota A menuju Kota B dengan kecepatan 60 km/jam pada pukul 08.00. Mobil Q berangkat dari Kota B menuju Kota A dengan kecepatan 40 km/jam pada pukul 08.00. Pada pukul berapa kedua mobil akan bertemu?")
    
    q2_answer = st.text_input("Jawabanmu (contoh: 10.00):", key="q2").strip().replace('.', ':')

    if st.button("Cek Jawaban Soal 2", key="btn2"):
        # Hitung waktu bertemu
        # Kecepatan relatif = 60 + 40 = 100 km/jam
        # Waktu bertemu = Jarak / Kecepatan Relatif = 300 / 100 = 3 jam
        # Pukul bertemu = 08.00 + 3 jam = 11.00
        correct_answer_q2 = "11:00"

        if q2_answer == correct_answer_q2:
            st.success("Jawabanmu benar! (Penjelasan: Kecepatan relatif = 60+40=100 km/jam. Waktu bertemu = 300 km / 100 km/jam = 3 jam. Jadi, bertemu pada pukul 08.00 + 3 jam = 11.00)")
            score += 1
        else:
            st.error(f"Jawabanmu salah. Jawaban yang benar adalah {correct_answer_q2}. Pastikan format jawabanmu sesuai.")

    if st.button("Lihat Skor Akhir", key="score_btn"):
        st.subheader("Skor Akhir:")
        st.info(f"Kamu berhasil menjawab benar {score} dari 2 soal.")
        if score == 2:
            st.balloons()
            st.markdown("Hebat! Kamu telah memahami konsep Jarak, Kecepatan, Waktu dengan sangat baik!")
        elif score == 1:
            st.markdown("Bagus! Pertahankan belajarmu.")
        else:
            st.markdown("Jangan menyerah! Coba ulangi kembali virtual laboratory untuk pemahaman yang lebih baik.")
