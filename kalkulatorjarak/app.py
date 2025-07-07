
import streamlit as st

st.set_page_config(page_title="Kalkulator Jarak, Kecepatan, Waktu", layout="centered")

st.title("🧮 Kalkulator Jarak, Kecepatan, dan Waktu")

st.markdown("""
### Gunakan kalkulator ini untuk menghitung salah satu dari:
- **Jarak**: jika diketahui Kecepatan dan Waktu
- **Kecepatan**: jika diketahui Jarak dan Waktu
- **Waktu**: jika diketahui Jarak dan Kecepatan
""")

# Pilih jenis perhitungan
option = st.selectbox("Pilih yang ingin dihitung:", ["Jarak", "Kecepatan", "Waktu"])

if option == "Jarak":
    kecepatan = st.number_input("Masukkan Kecepatan (km/jam):", min_value=0.0, format="%.2f")
    waktu = st.number_input("Masukkan Waktu (jam):", min_value=0.0, format="%.2f")
    if st.button("Hitung Jarak"):
        jarak = kecepatan * waktu
        st.success(f"Jarak = {jarak:.2f} km")

elif option == "Kecepatan":
    jarak = st.number_input("Masukkan Jarak (km):", min_value=0.0, format="%.2f")
    waktu = st.number_input("Masukkan Waktu (jam):", min_value=0.01, format="%.2f")
    if st.button("Hitung Kecepatan"):
        kecepatan = jarak / waktu
        st.success(f"Kecepatan = {kecepatan:.2f} km/jam")

elif option == "Waktu":
    jarak = st.number_input("Masukkan Jarak (km):", min_value=0.0, format="%.2f")
    kecepatan = st.number_input("Masukkan Kecepatan (km/jam):", min_value=0.01, format="%.2f")
    if st.button("Hitung Waktu"):
        waktu = jarak / kecepatan
        st.success(f"Waktu = {waktu:.2f} jam")
