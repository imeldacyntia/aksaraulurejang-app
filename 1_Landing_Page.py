import streamlit as st

st.set_page_config(
    page_title="Deteksi Aksara Ulu Rejang",
    page_icon="📖",
    layout="wide"
)

st.markdown("<h1 style='text-align: center; color: #2E86C1;'>Deteksi Aksara Ulu Rejang</h1>", unsafe_allow_html=True)

st.markdown("""
Selamat datang di aplikasi **Deteksi Aksara Ulu Rejang** 👋  

Aplikasi ini dibuat untuk membantu mengenali dan mendeteksi aksara Ulu Rejang secara otomatis.  

### ✨ Fitur:
- 📷 Deteksi citra secara langsung menggunakan kamera
- 🖼️ Deteksi citra melalui unggahan gambar 
""")

# --- Tombol langsung ke halaman deteksi ---
st.markdown("---")
st.markdown("### 🔎 Siap mencoba?")
st.markdown("Mulailah mendeteksi aksara Ulu Rejang dari kamera atau gambar untuk mengenal lebih dekat warisan budaya kita. ✨")

if st.button("🚀 Mulai Deteksi"):
    st.switch_page("pages/1_Deteksi.py")  # sesuaikan dengan nama file halaman Deteksi

# --- Tentang Aksara Rejang ---
st.markdown("---")
st.markdown("## 📖 Tentang Aksara Ulu Rejang")

st.markdown("""
Aksara Ulu Rejang merupakan salah satu warisan budaya Nusantara yang tumbuh dan berkembang di Bengkulu.  
Aksara ini berbentuk silabis, di mana setiap huruf mewakili satu suku kata.  
Sejak dahulu, aksara ini digunakan dalam manuskrip untuk mencatat sejarah, silsilah, hingga tradisi masyarakat Rejang.  

Keberadaan aplikasi ini memiliki manfaat penting, yaitu:  
- 💡 Membantu masyarakat lebih mudah **mengenal dan mempelajari aksara Ulu Rejang** melalui teknologi modern.  
- 📝 Dapat digunakan untuk mendeteksi **tulisan tangan di atas kertas** maupun **manuskrip yang sudah didigitalisasi dalam bentuk font**.  
- 🌍 Berkontribusi pada **pelestarian kebudayaan** dengan memanfaatkan kecerdasan buatan untuk menjaga keberlanjutan aksara tradisional.  
- 📚 Memberi nilai edukatif bagi generasi muda agar semakin peduli dan tertarik terhadap warisan budaya lokal.  
""")

