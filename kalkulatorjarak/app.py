import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Konfigurasi Halaman
st.set_page_config(page_title="Kalkulator JKW Discovery", layout="wide")
st.title("📚 Kalkulator Jarak – Kecepatan – Waktu (JKW)")

st.markdown("""
Pelajari hubungan antara **jarak (S)**, **kecepatan (v)**, dan **waktu (t)**  
dengan eksplorasi interaktif melalui simulasi!  
Coba ubah nilai dan **temukan sendiri rumusnya** 📐

---

🧭 **Cara Menggunakan Aplikasi Ini**:
1. Gunakan **slider** untuk memasukkan nilai kecepatan, waktu, atau jarak.
2. Lihat hasil perhitungan langsung di bawahnya.
3. Amati perubahan **grafik gerak** untuk memahami pola hubungan.
4. Gunakan bagian **refleksi dan interpretasi** untuk berpikir kritis.
""")

# ========================
# 📘 Penjelasan Konsep
# ========================
with st.expander("🔍 Penjelasan Konsep Dasar"):
    st.markdown("""
    - **Jarak (S)**: seberapa jauh benda bergerak (dalam kilometer - km)  
    - **Kecepatan (v)**: seberapa cepat benda bergerak (dalam km/jam)  
    - **Waktu (t)**: lamanya benda bergerak (dalam jam)
    """)

# ========================
# 🧪 Eksplorasi Interaktif
# ========================
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📏 Temukan Jarak")
    kecepatan_j = st.slider("🚗 Kecepatan (km/jam)", 0, 200, 60, key="k_j")
    waktu_j = st.slider("⏱️ Waktu (jam)", 0, 10, 2, key="w_j")
    jarak = kecepatan_j * waktu_j
    st.success(f"🔹 Jarak = {int(jarak)} km")

with col2:
    st.subheader("🚀 Temukan Kecepatan")
    jarak_k = st.slider("📏 Jarak (km)", 0, 500, 120, key="j_k")
    waktu_k = st.slider("⏱️ Waktu (jam)", 1, 10, 2, key="w_k")
    kecepatan = jarak_k / waktu_k
    st.success(f"🔹 Kecepatan = {int(kecepatan)} km/jam")

with col3:
    st.subheader("⏱️ Temukan Waktu")
    jarak_w = st.slider("📏 Jarak (km)", 0, 500, 100, key="j_w")
    kecepatan_w = st.slider("🚗 Kecepatan (km/jam)", 1, 200, 50, key="k_w")
    waktu = jarak_w / kecepatan_w
    st.success(f"🔹 Waktu = {round(waktu, 2)} jam")

# ========================
# 🧠 Discovery Learning Prompt
# ========================
with st.expander("🧠 Refleksi: Apa Hubungan Ketiganya?"):
    st.markdown("""
    - Jika **kecepatan dinaikkan**, tapi waktu tetap, apa yang terjadi pada jarak?  
    - Jika **jarak tetap** dan waktu lebih lama, bagaimana kecepatan berubah?  
    - Jika kecepatan tetap dan **jarak naik**, bagaimana waktu berubah?  

    💡 Dari eksplorasi ini, dapatkah kamu menyimpulkan **rumus matematis** yang menghubungkan ketiganya?
    """)

# ========================
# 📈 Simulasi Grafik Gerak
# ========================
st.markdown("---")
st.subheader("📈 Simulasi Grafik Gerak (Jarak vs Waktu)")

col_g1, col_g2 = st.columns([2, 1])
with col_g2:
    kecepatan_sim = st.slider("🚗 Kecepatan Simulasi (km/jam)", 10, 200, 60)
    waktu_maks = st.slider("⏱️ Lama Simulasi (jam)", 1, 10, 5)

with col_g1:
    waktu_array = np.linspace(0, waktu_maks, 100)
    jarak_array = kecepatan_sim * waktu_array

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(waktu_array, jarak_array, color="#FF6F61", linewidth=3, linestyle='--', marker='o', markersize=2)
    ax.set_xlabel("⏱️ Waktu (jam)", fontsize=12)
    ax.set_ylabel("📏 Jarak (km)", fontsize=12)
    ax.set_title(f"Simulasi Gerak Lurus: {kecepatan_sim} km/jam", fontsize=14)
    ax.grid(True)
    ax.set_facecolor("#f0f0f0")

    st.pyplot(fig)

with st.expander("📊 Interpretasi Grafik"):
    st.markdown(f"""
    - Grafik menunjukkan **garis lurus** karena gerak benda berkecepatan tetap.  
    - Setiap kenaikan 1 jam, jarak bertambah **{kecepatan_sim} km**.  
    - **Kemiringan garis (gradien)** mewakili kecepatan.  
    - Lebih curam = lebih cepat!

    ❓ Apa yang terjadi jika kamu meningkatkan kecepatan simulasi?
    """)

st.caption("🎯 Eksplorasi ini mendukung pembelajaran mandiri dan pemahaman konsep fungsional linear.")
