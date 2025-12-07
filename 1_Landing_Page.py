import streamlit as st

st.set_page_config(
    page_title="Deteksi Aksara Ulu Rejang",
    page_icon="📖",
    layout="wide"
)

# === Judul Halaman ===
st.markdown(
    "<h1 style='text-align: center; color: #2E86C1;'>Deteksi Aksara Ulu Rejang</h1>",
    unsafe_allow_html=True
)

# === Penjelasan Tentang Aksara (Diletakkan di Awal) ===
st.markdown("""
## Tentang Aksara Ulu Rejang

Aksara Ulu Rejang adalah salah satu aksara tradisional penting di Provinsi Bengkulu 
yang digunakan untuk mendokumentasikan adat, silsilah, dan tradisi masyarakat Rejang. 
Termasuk dalam rumpun aksara Sumatera Selatan, aksara ini memiliki struktur grafem dan kaidah penulisan yang khas, 
sebagaimana tampak pada manuskrip kuno yang ditulis pada kulit kayu, bambu, dan kertas.

Saat ini, tingkat literasi Aksara Ulu Rejang menurun, penggunaannya hanya bertahan di kalangan terbatas 
dan tidak lagi menjadi bagian dari pembelajaran generasi muda. 
Aplikasi deteksi Aksara Ulu Rejang ini dikembangkan untuk membantu pengenalan dan pembacaan aksara secara otomatis, 
sehingga dapat mendukung pelestarian dan pemanfaatan aksara tradisional ini di era digital.
""")

st.markdown("---")

# === Penjelasan Singkat Aplikasi ===
st.markdown("""
## Tentang Aplikasi

Aplikasi ini dapat digunakan untuk mendeteksi grafem aksara Ulu Rejang melalui:
- Deteksi citra menggunakan kamera
- Deteksi citra melalui unggahan gambar

Model yang digunakan dirancang untuk mengenali pola grafem baik dari tulisan tangan maupun hasil digitalisasi font.
""")

st.markdown("---")

# === Tombol Mulai Deteksi ===
st.markdown("## Siap Mencoba?")
st.markdown("Mulai proses deteksi aksara Ulu Rejang melalui kamera atau gambar.")

if st.button("Mulai Deteksi"):
    st.switch_page("pages/1_Deteksi.py")
