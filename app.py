import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Peta UMKM Polewali Mandar",
    page_icon="🗺️",
    layout="wide"
)

# =========================
#       CUSTOM CSS
# =========================
st.markdown("""
<style>
.title { font-size:42px; font-weight:800; color:#0A5EB0; text-align:center; }
.subtitle { font-size:18px; text-align:center; color:#444; margin-bottom:20px; }
.footer { text-align:center; font-size:13px; color:#777; margin-top:40px; }
</style>
""", unsafe_allow_html=True)

# =========================
#  DATA UMKM DENGAN KOORDINAT FIX
# =========================
data_umkm = pd.DataFrame({
    "Nama UMKM": [
        "Kue Mandar Sari", 
        "Kopi Lapeo", 
        "Kerajinan Anyaman",
        "Abon Ikan Polewali",
        "Dodol Mandar", 
        "Sambal Mandar",
        "Pecel Mandar", 
        "Kain Tenun Mandar"
    ],
    "Kategori": [
        "Kuliner", 
        "Minuman", 
        "Kerajinan",
        "Kuliner", 
        "Kuliner", 
        "Kuliner",
        "Kuliner", 
        "Kerajinan"
    ],
    "Kecamatan": [
        "Polewali", 
        "Binuang", 
        "Wonomulyo",
        "Mapilli", 
        "Tapango", 
        "Polewali",
        "Wonomulyo", 
        "Campalagian"
    ],
    # Koordinat kecamatan yang sudah diperbaiki
    "latitude": [
        -3.4326,   # Polewali
        -3.4885,   # Binuang
        -3.4569,   # Wonomulyo
        -3.4820,   # Mapilli
        -3.5353,   # Tapango
        -3.4310,   # Polewali (titik kedua)
        -3.4575,   # Wonomulyo (titik kedua)
        -3.4675    # Campalagian
    ],
    "longitude": [
        119.3435,  # Polewali
        119.3547,  # Binuang
        119.3824,  # Wonomulyo
        119.3098,  # Mapilli
        119.3993,  # Tapango
        119.3501,  # Polewali (titik kedua)
        119.3850,  # Wonomulyo (titik kedua)
        119.3187   # Campalagian
    ]
})

# =========================
#        UI TITLE
# =========================
st.markdown('<p class="title">🗺️ Peta Digital UMKM Polewali Mandar</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Lokasi UMKM berdasarkan kecamatan di Kabupaten Polewali Mandar</p>', unsafe_allow_html=True)

# =========================
#         SIDEBAR FILTER
# =========================
st.sidebar.header("🔎 Filter Data UMKM")

kecamatan_list = ["Semua"] + sorted(data_umkm["Kecamatan"].unique())
pilih_kecamatan = st.sidebar.selectbox("Pilih Kecamatan", kecamatan_list)

kategori_list = ["Semua"] + sorted(data_umkm["Kategori"].unique())
pilih_kategori = st.sidebar.selectbox("Pilih Kategori", kategori_list)

# Filter
data_tampil = data_umkm.copy()

if pilih_kecamatan != "Semua":
    data_tampil = data_tampil[data_tampil["Kecamatan"] == pilih_kecamatan]

if pilih_kategori != "Semua":
    data_tampil = data_tampil[data_tampil["Kategori"] == pilih_kategori]

# =========================
#        TABEL DATA
# =========================
st.subheader("📋 Daftar UMKM")
st.dataframe(data_tampil, use_container_width=True)

# =========================
#         PETA STREAMLIT
# =========================
st.subheader("📍 Peta Lokasi UMKM Polewali Mandar")
st.map(data_tampil[["latitude", "longitude"]], zoom=11)

# =========================
#        FOOTER
# =========================
st.markdown('<p class="footer">© 2025 • Peta UMKM Polewali Mandar • dibuat dengan Streamlit</p>', unsafe_allow_html=True)
