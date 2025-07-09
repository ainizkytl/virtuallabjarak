import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Kalkulator JKW Discovery - All in One", layout="wide")
st.title("📚 Kalkulator Jarak – Kecepatan – Waktu")

st.markdown("""
Pelajari hubungan antara **jarak, kecepatan, dan waktu** dengan mencoba berbagai nilai dan melihat hasilnya secara bersamaan.  
Temukan sendiri rumus dan keterkaitannya!  
---
""")

with st.expander("📘 Penjelasan Konsep Dasar"):
    st.markdown("""
    - **Jarak (S)**: seberapa jauh benda bergerak (km)  
    - **Kecepatan (v)**: seberapa cepat benda bergerak (km/jam)  
    - **Waktu (t)**: lamanya benda bergerak (jam)  
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
    st.success(f"Jarak = {int(jarak)} km")

with col2:
    st.subheader("🚀 Temukan Kecepatan")
    jarak_k = st.slider("📏 Jarak (km)", 0, 500, 120, key="j_k")
    waktu_k = st.slider("⏱️ Waktu (jam)", 1, 10, 2, key="w_k")
    kecepatan = jarak_k / waktu_k
    st.success(f"Kecepatan = {int(kecepatan)} km/jam")

with col3:
    st.subheader("⏱️ Temukan Waktu")
    jarak_w = st.slider("📏 Jarak (km)", 0, 500, 100, key="j_w")
    kecepatan_w = st.slider("🚗 Kecepatan (km/jam)", 1, 200, 50, key="k_w")
    waktu = jarak_w / kecepatan_w
    st.success(f"Waktu = {round(waktu, 2)} jam")

# ========================
# 🧠 Discovery Learning Prompt
# ========================
with st.expander("🧠 Refleksi: Apa Hubungan Ketiganya?"):
    st.markdown("""
    🔍 **Coba perhatikan!**  
    - Jika kecepatan dinaikkan tapi waktu tetap, apa yang terjadi pada jarak?  
    - Jika jarak tetap dan waktu lebih lama, bagaimana kecepatan berubah?  
    - Jika kecepatan tetap dan jarak naik, bagaimana waktu berubah?  

    👉 Dari eksplorasi di atas, dapatkah kamu menebak **rumus** yang menghubungkan ketiganya?
    """)

# ========================
# 📈 Grafik Simulasi Gerak
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
    ax.set_title(f"Grafik Gerak Lurus: Kecepatan {kecepatan_sim} km/jam")
    ax.grid(True)

    st.pyplot(fig)

with st.expander("📊 Interpretasi Grafik"):
    st.markdown(f"""
    - Grafik menunjukkan hubungan **linier** antara jarak dan waktu.  
    - Semakin besar waktu, semakin jauh jarak yang ditempuh.  
    - **Gradien (kemiringan garis)** menunjukkan kecepatan.  
    - Pada kecepatan {kecepatan_sim} km/jam, setiap jamnya bertambah {kecepatan_sim} km.

    💬 Apa yang akan terjadi jika kecepatan dinaikkan?
    """)

st.caption("🔍 Gunakan semua kolom untuk eksplorasi mandiri.
