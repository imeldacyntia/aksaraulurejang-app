import streamlit as st

st.set_page_config(
    page_title="Deteksi Aksara Ulu Rejang",
    page_icon="📖",
    layout="wide"
)

# === Custom CSS (Responsive + Justify) ===
st.markdown("""
<style>

/* Container teks utama */
.content-container {
    max-width: 900px;
    margin: auto;
}

/* Paragraf justify */
.justify-text {
    text-align: justify;
    line-height: 1.8;
    font-size: 16px;
}

/* Responsive mobile */
@media (max-width: 768px) {
    .justify-text {
        font-size: 15px;
        line-height: 1.7;
        padding-left: 10px;
        padding-right: 10px;
    }
}

</style>
""", unsafe_allow_html=True)


# === Judul Halaman ===
st.markdown(
    "<h1 style='text-align: center; color: #2E86C1;'>Sistem Deteksi Grafem Aksara Ulu Rejang</h1>",
    unsafe_allow_html=True
)

st.markdown("<div class='content-container'>", unsafe_allow_html=True)

# === Penjelasan Tentang Aksara ===
st.markdown("""
## Tentang Aksara Ulu Rejang

<div class='justify-text'>
Aksara Ulu Rejang adalah salah satu aksara tradisional penting di Provinsi Bengkulu 
yang digunakan untuk mendokumentasikan adat, silsilah, dan tradisi masyarakat Rejang. 
Termasuk dalam rumpun aksara Sumatera Selatan, aksara ini memiliki struktur grafem dan kaidah penulisan yang khas, 
sebagaimana tampak pada manuskrip kuno yang ditulis pada kulit kayu, bambu, dan kertas.
<br><br>
Saat ini, tingkat literasi Aksara Ulu Rejang menurun, penggunaannya hanya bertahan di kalangan terbatas 
dan tidak lagi menjadi bagian dari pembelajaran generasi muda. 
Aplikasi deteksi Aksara Ulu Rejang ini dikembangkan untuk membantu pengenalan dan pembacaan aksara secara otomatis, 
sehingga dapat mendukung pelestarian dan pemanfaatan aksara tradisional ini di era digital.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# === Penjelasan Singkat Aplikasi ===
st.markdown("""
## Tentang Aplikasi

<div class='justify-text'>
Aplikasi ini dapat digunakan untuk mendeteksi grafem aksara Ulu Rejang melalui:
<ul>
<li>Deteksi citra menggunakan kamera</li>
<li>Deteksi citra melalui unggahan gambar</li>
</ul>

Model yang digunakan dirancang untuk mengenali pola grafem baik dari tulisan tangan maupun hasil digitalisasi font.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# === Tombol Mulai Deteksi ===
st.markdown("## Siap Mencoba?")
st.markdown("<div class='justify-text'>Mulai proses deteksi aksara Ulu Rejang melalui kamera atau gambar.</div>", unsafe_allow_html=True)

if st.button("Mulai Deteksi"):
    st.switch_page("pages/1_Deteksi.py")

st.markdown("</div>", unsafe_allow_html=True)
