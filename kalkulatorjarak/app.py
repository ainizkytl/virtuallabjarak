import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Kalkulator JKW Discovery - All in One", layout="wide")
st.title("📚 Kalkulator Jarak – Kecepatan – Waktu (Discovery Learning)")

st.markdown("""
Pelajari hubungan antara **jarak, kecepatan, dan waktu** dengan mencoba berbagai nilai dan melihat hasilnya secara bersamaan.  
Temukan sendiri rumus dan keterkaitannya!  
---
""")

with st.expander("📘 Penjelasan Konsep"):
    st.markdown("""
    - **Jarak**: seberapa jauh benda bergerak (km).
    - **Kecepatan**: seberapa cepat benda bergerak (km/jam).
    - **Waktu**: berapa lama benda bergerak (jam).
    
    🧠 Gunakan eksplorasi di bawah ini untuk menemukan sendiri rumus masing-masing.
    """)

# Layout 3 kolom untuk eksplorasi serentak
col1, col2, col3 = st.columns(3)

# ========================
# 🟦 KOLOM 1: JARAK
# ========================
with col1:
    st.subheader("📏 Temukan Jarak")
    kecepatan_j = st.slider("🚗 Kecepatan (km/jam)", 0, 200, 60, key="k_j")
    waktu_j = st.slider("⏱️ Waktu (jam)", 0, 10, 2, key="w_j")
    if kecepatan_j and waktu_j:
        jarak = int(kecepatan_j * waktu_j)
        st.success(f"Jarak = {jarak} km")
    with st.expander("💡 Refleksi Jarak"):
        st.markdown("- Apa yang terjadi jika kecepatan bertambah?\n- Bagaimana jika waktunya lebih lama?")

# ========================
# 🟩 KOLOM 2: KECEPATAN
# ========================
with col2:
    st.subheader("🚀 Temukan Kecepatan")
    jarak_k = st.slider("📏 Jarak (km)", 0, 500, 120, key="j_k")
    waktu_k = st.slider("⏱️ Waktu (jam)", 1, 10, 2, key="w_k")  # waktu tidak boleh 0
    if jarak_k and waktu_k:
        kecepatan = int(jarak_k / waktu_k)
        st.success(f"Kecepatan = {kecepatan} km/jam")
    with st.expander("💡 Refleksi Kecepatan"):
        st.markdown("- Apa yang terjadi jika jarak tetap tapi waktu makin lama?\n- Apakah kecepatannya bertambah atau berkurang?")

# ========================
# 🟥 KOLOM 3: WAKTU
# ========================
with col3:
    st.subheader("⏱️ Temukan Waktu")
    jarak_w = st.slider("📏 Jarak (km)", 0, 500, 100, key="j_w")
    kecepatan_w = st.slider("🚗 Kecepatan (km/jam)", 1, 200, 50, key="k_w")  # kecepatan tidak boleh 0
    if jarak_w and kecepatan_w:
        waktu = int(jarak_w / kecepatan_w)
        st.success(f"Waktu = {waktu} jam")
    with st.expander("💡 Refleksi Waktu"):
        st.markdown("- Bagaimana pengaruh kecepatan terhadap waktu tempuh?\n- Jika jaraknya tetap dan kecepatan naik, apa yang terjadi?")

# ========================
# 📈 GRAFIK SIMULASI
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

    fig, ax = plt.subplots()
    ax.plot(waktu_array, jarak_array, color="blue", linewidth=2)
    ax.set_xlabel("Waktu (jam)")
    ax.set_ylabel("Jarak (km)")
    ax.set_title("Grafik Gerak Lurus: Jarak vs Waktu")
    ax.grid(True)

    st.pyplot(fig)

st.caption("🔍 Gunakan semua kolom untuk eksplorasi mandiri. Media ini dirancang untuk pembelajaran aktif.")
