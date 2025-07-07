import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Kalkulator JKW - Discovery Learning", layout="centered")
st.title("📚 Kalkulator Jarak, Kecepatan, Waktu (Discovery Learning)")

st.markdown("""
### 🔍 Eksplorasi Interaktif
Eksplorasilah masing-masing konsep secara terpisah dan temukan sendiri rumus hubungan antar variabel!
""")

with st.expander("📘 Apa itu Jarak, Kecepatan, dan Waktu?"):
    st.markdown("""
    - **Jarak**: Panjang lintasan yang ditempuh suatu benda (satuan: km).
    - **Kecepatan**: Seberapa cepat benda bergerak (satuan: km/jam).
    - **Waktu**: Lama waktu benda bergerak (satuan: jam).

    Yuk kita cari tahu sendiri rumus-rumus hubungan ketiganya! 🚀
    """)

menu = st.sidebar.selectbox("Pilih topik eksplorasi:", ["Temukan Jarak", "Temukan Kecepatan", "Temukan Waktu", "Simulasi Gerak"])

# ================================
# 🔢 CARI JARAK
# ================================
if menu == "Temukan Jarak":
    st.subheader("📏 Temukan Jarak")
    st.markdown("Masukkan kecepatan dan waktu, lalu coba amati bagaimana jarak berubah!")

    kecepatan = st.slider("🚗 Kecepatan (km/jam)", 0, 200, 60, step=1)
    waktu = st.slider("⏱️ Waktu (jam)", 0, 10, 1, step=1)

    if st.button("🔍 Hitung Jarak"):
        jarak = int(kecepatan * waktu)
        st.success(f"Jarak yang ditempuh: **{jarak} km**")
        st.info("🧠 Apa yang terjadi jika kecepatan atau waktu ditambah?")
    
    with st.expander("💡 Coba renungkan..."):
        st.markdown("""
        - Bagaimana hubungan antara jarak, kecepatan, dan waktu?
        - Apa rumus yang kamu temukan dari percobaan ini?
        """)

# ================================
# 🔢 CARI KECEPATAN
# ================================
elif menu == "Temukan Kecepatan":
    st.subheader("🚀 Temukan Kecepatan")
    st.markdown("Masukkan jarak dan waktu, lalu amati bagaimana hasil kecepatan berubah.")

    jarak = st.slider("📏 Jarak (km)", 0, 500, 120, step=1)
    waktu = st.slider("⏱️ Waktu (jam)", 1, 10, 2, step=1)

    if st.button("🔍 Hitung Kecepatan"):
        kecepatan = int(jarak / waktu)
        st.success(f"Kecepatan: **{kecepatan} km/jam**")
        st.info("🧠 Coba kurangi waktu. Apa yang terjadi pada kecepatan?")

    with st.expander("💡 Pertanyaan Pemandu"):
        st.markdown("""
        - Bagaimana caramu mendapatkan kecepatan dari jarak dan waktu?
        - Apa rumus yang kamu simpulkan?
        """)

# ================================
# 🔢 CARI WAKTU
# ================================
elif menu == "Temukan Waktu":
    st.subheader("⏱️ Temukan Waktu")
    st.markdown("Masukkan jarak dan kecepatan, lalu lihat bagaimana waktu berubah.")

    jarak = st.slider("📏 Jarak (km)", 0, 500, 100, step=1)
    kecepatan = st.slider("🚗 Kecepatan (km/jam)", 1, 200, 50, step=1)

    if st.button("🔍 Hitung Waktu"):
        waktu = int(jarak / kecepatan)
        st.success(f"Waktu tempuh: **{waktu} jam**")
        st.info("🧠 Semakin cepat lajunya, semakin singkat waktu yang dibutuhkan.")

    with st.expander("💡 Refleksi Konsep"):
        st.markdown("""
        - Dari mana kamu tahu waktu bisa dihitung dengan rumus tertentu?
        - Bandingkan hasilnya dengan perhitungan manualmu.
        """)

# ================================
# 📈 SIMULASI GRAFIK
# ================================
elif menu == "Simulasi Gerak":
    st.subheader("📈 Simulasi Grafik Gerak (Jarak vs Waktu)")

    with st.expander("🎮 Atur Kecepatan dan Lama Waktu untuk Simulasi:"):
        kecepatan_sim = st.slider("🚗 Kecepatan benda (km/jam)", 10, 200, 60, step=1)
        waktu_maks = st.slider("⏱️ Durasi pengamatan (jam)", 1, 10, 5, step=1)

    # Data grafik
    waktu_array = np.linspace(0, waktu_maks, 100)
    jarak_array = kecepatan_sim * waktu_array

    fig, ax = plt.subplots()
    ax.plot(waktu_array, jarak_array, color="blue", linewidth=2)
    ax.set_xlabel("Waktu (jam)")
    ax.set_ylabel("Jarak (km)")
    ax.set_title("Simulasi Gerak Lurus (Jarak vs Waktu)")
    ax.grid(True)

    st.pyplot(fig)
    st.info(f"📌 Kecepatan tetap: {kecepatan_sim} km/jam → garis lurus menunjukkan pertambahan jarak konstan terhadap waktu.")

st.markdown("---")
st.caption("📘 Media ini dirancang untuk pembelajaran aktif dan eksploratif.")
