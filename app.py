import streamlit as st
import pandas as pd

# =========================
#      CONFIG PAGE
# =========================
st.set_page_config(
    page_title="Peta UMKM Polewali Mandar",
    page_icon="🗺️",
    layout="wide"
)

# =========================
#      CUSTOM CSS
# =========================
st.markdown("""
    <style>
    .title {
        font-size: 42px;
        font-weight: 800;
        color: #0A5EB0;
        text-align: center;
        margin-bottom: -5px;
    }
    .subtitle {
        font-size: 18px;
        color: #444;
        text-align: center;
        margin-bottom: 25px;
    }
    .footer {
        text-align: center;
        color: #777;
        margin-top: 45px;
        font-size: 13px;
    }
    .block-container {
        padding-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# =========================
#        DATA UMKM
# =========================
data_umkm = pd.DataFrame({
    "Nama UMKM": [
        "Kue Mandar Sari", "Kopi Lapeo", "Kerajinan Anyaman",
        "Abon Ikan Polewali", "Dodol Mandar", "Sambal Mandar",
        "Pecel Mandar", "Kain Tenun Mandar"
    ],
    "Kategori": [
        "Kuliner", "Minuman", "Kerajinan",
        "Kuliner", "Kuliner", "Kuliner",
        "Kuliner", "Kerajinan"
    ],
    "Kecamatan": [
        "Polewali", "Binuang", "Wonomulyo",
        "Mapilli", "Tapango", "Polewali",
        "Wonomulyo", "Campalagian"
    ],
    "Latitude": [
        -3.4321, -3.5001, -3.4567,
        -3.4801, -3.5222, -3.4404,
        -3.4600, -3.4705
    ],
    "Longitude": [
        119.3433, 119.3550, 119.3888,
        119.3102, 119.4001, 119.3500,
        119.3990, 119.3201
    ]
})

# =========================
#           UI
# =========================
st.markdown('<p class="title">🗺️ Peta Digital UMKM Polewali Mandar</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Menampilkan lokasi UMKM terbaik dari berbagai kecamatan di Polewali Mandar</p>', unsafe_allow_html=True)

# =========================
#      SIDEBAR FILTER
# =========================
st.sidebar.header("🔎 Filter Data")

# Kecamatan
kecamatan_list = ["Semua"] + sorted(data_umkm["Kecamatan"].unique())
pilih_kecamatan = st.sidebar.selectbox("Pilih Kecamatan", kecamatan_list)

# Kategori
kategori_list = ["Semua"] + sorted(data_umkm["Kategori"].unique())
pilih_kategori = st.sidebar.selectbox("Pilih Kategori UMKM", kategori_list)

# Filter data
data_tampil = data_umkm.copy()

if pilih_kecamatan != "Semua":
    data_tampil = data_tampil[data_tampil["Kecamatan"] == pilih_kecamatan]

if pilih_kategori != "Semua":
    data_tampil = data_tampil[data_tampil["Kategori"] == pilih_kategori]

# =========================
#       TABEL DATA
# =========================
st.subheader("📋 Daftar UMKM")
st.dataframe(
    data_tampil,
    column_config={
        "Nama UMKM": "Nama UMKM",
        "Kategori": "Kategori",
        "Kecamatan": "Kecamatan"
    },
    use_container_width=True
)

# =========================
#          PETA
# =========================
st.subheader("📍 Peta Lokasi UMKM")
st.map(data_tampil[["Latitude", "Longitude"]])

# =========================
#        FOOTER
# =========================
st.markdown('<p class="footer">© 2025 • Peta UMKM Polewali Mandar • Dibuat dengan Streamlit</p>', unsafe_allow_html=True)
