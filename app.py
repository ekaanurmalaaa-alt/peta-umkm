import streamlit as st
import pandas as pd

st.set_page_config(page_title="Peta UMKM Sulawesi Barat", layout="wide")
st.title("🗺️ Peta UMKM Sulawesi Barat (Tanpa Library Tambahan)")

st.markdown("""
Aplikasi ini menampilkan lokasi UMKM di Sulawesi Barat menggunakan **peta bawaan Streamlit**.
Tidak membutuhkan instalasi library tambahan seperti Folium atau Plotly.
""")

# ======================
# DATA UMKM
# ======================
data = {
    "nama_umkm": [
        "Warung Makan Sederhana", "Toko Kue Manis", "Butik Muslimah Cantik",
        "Toko Sembako Murah", "Kedai Kopi Santai", "Toko Oleh-Oleh Sulbar",
        "Bengkel Motor Jaya", "Laundry Bersih Selalu", "Rumah Makan Laut Segar",
        "Toko Elektronik Maju Tech"
    ],
    "kategori": [
        "Kuliner", "Kuliner", "Fashion",
        "Sembako", "Kuliner", "Kerajinan",
        "Otomotif", "Jasa", "Kuliner", "Elektronik"
    ],
    "kabupaten": [
        "Polewali Mandar", "Polewali Mandar", "Mamuju",
        "Mamuju", "Majene", "Majene",
        "Polewali Mandar", "Mamuju Tengah", "Mamuju", "Pasangkayu"
    ],
    "lat": [-3.4321, -3.4455, -2.6744, -2.6901, -3.5378, -3.5222, -3.4655, -2.7166, -2.6749, -1.1902],
    "lon": [119.3432, 119.3655, 118.8877, 118.9012, 118.9734, 118.9659, 119.3111, 119.0134, 118.8966, 119.3621]
}

df = pd.DataFrame(data)

# ======================
# SIDEBAR FILTER
# ======================
st.sidebar.header("Filter")

kab_opts = ["Semua"] + sorted(df["kabupaten"].unique())
kat_opts = ["Semua"] + sorted(df["kategori"].unique())

pilih_kab = st.sidebar.selectbox("Pilih Kabupaten", kab_opts)
pilih_kat = st.sidebar.selectbox("Pilih Kategori", kat_opts)

filtered = df.copy()

if pilih_kab != "Semua":
    filtered = filtered[filtered["kabupaten"] == pilih_kab]

if pilih_kat != "Semua":
    filtered = filtered[filtered["kategori"] == pilih_kat]

st.write(f"### Jumlah UMKM ditemukan: {len(filtered)}")

# ======================
# PETA STREAMLIT
# ======================
st.subheader("🗺️ Peta Lokasi UMKM")
st.map(filtered.rename(columns={"lat": "latitude", "lon": "longitude"}))

# ======================
# TABEL DATA
# ======================
st.subheader("📋 Tabel UMKM")
st.dataframe(filtered)
