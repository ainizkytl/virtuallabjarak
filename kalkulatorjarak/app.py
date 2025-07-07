import streamlit as st

st.set_page_config(page_title="Kalkulator JKW - Discovery Learning", layout="centered")
st.title("📚 Kalkulator Jarak, Kecepatan, Waktu (Discovery Learning)")

st.markdown("""
### 🔍 **Pembelajaran Interaktif dengan Metode Discovery Learning**
Silakan eksplorasi hubungan antara **jarak**, **kecepatan**, dan **waktu** melalui simulasi berikut ini.
---
""")

with st.expander("📘 Teori Singkat"):
    st.markdown("""
    **Rumus dasar hubungan JKW**:
    - Jarak = Kecepatan × Waktu
    - Kecepatan = Jarak ÷ Waktu
    - Waktu = Jarak ÷ Kecepatan

    Cobalah berbagai nilai untuk melihat bagaimana satu variabel mempengaruhi yang lain.
    """)

# Pilihan eksplorasi
st.subheader("🧠 Eksplorasi Konsep")
option = st.radio("Apa yang ingin kamu temukan?", ["Jarak", "Kecepatan", "Waktu"], horizontal=True)

with st.form(key='form'):
    if option == "Jarak":
        kecepatan = st.slider("🔧 Kecepatan (km/jam)", 0.0, 200.0, 60.0, step=1.0)
        waktu = st.slider("⏱️ Waktu (jam)", 0.0, 10.0, 1.0, step=0.1)
        submit = st.form_submit_button("💡 Temukan Jarak")
        if submit:
            jarak = kecepatan * waktu
            st.success(f"📏 Jarak = {kecepatan} × {waktu} = **{jarak:.2f} km**")
            st.info("✅ Semakin besar kecepatan atau waktu, maka jarak akan semakin jauh.")

    elif option == "Kecepatan":
        jarak = st.slider("📏 Jarak (km)", 0.0, 500.0, 120.0, step=1.0)
        waktu = st.slider("⏱️ Waktu (jam)", 0.1, 10.0, 2.0, step=0.1)
        submit = st.form_submit_button("💡 Temukan Kecepatan")
        if submit:
            kecepatan = jarak / waktu
            st.success(f"🚗 Kecepatan = {jarak} ÷ {waktu} = **{kecepatan:.2f} km/jam**")
            st.info("✅ Jika jarak tetap, maka makin lama waktunya, makin kecil kecepatannya.")

    elif option == "Waktu":
        jarak = st.slider("📏 Jarak (km)", 0.0, 500.0, 100.0, step=1.0)
        kecepatan = st.slider("🚗 Kecepatan (km/jam)", 1.0, 200.0, 50.0, step=1.0)
        submit = st.form_submit_button("💡 Temukan Waktu")
        if submit:
            waktu = jarak / kecepatan
            st.success(f"⏱️ Waktu = {jarak} ÷ {kecepatan} = **{waktu:.2f} jam**")
            st.info("✅ Semakin cepat lajunya, semakin singkat waktu yang dibutuhkan.")

st.markdown("---")
st.caption("🧑‍🏫 Media ini dirancang untuk pembelajaran aktif dan eksploratif.")
