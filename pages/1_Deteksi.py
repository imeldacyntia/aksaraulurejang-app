# ==========================
# CEK HASIL DETEKSI
# ==========================
if len(results[0].boxes) == 0:

    st.toast(
        "⚠️ Grafem Aksara Ulu Rejang tidak terdeteksi.",
        icon="⚠️"
    )

    st.warning("""
### ⚠️ Grafem Aksara Ulu Rejang tidak terdeteksi

Sistem tidak menemukan grafem Aksara Ulu Rejang pada gambar yang diunggah.

**Kemungkinan penyebab:**
- Gambar bukan merupakan grafem Aksara Ulu Rejang.
- Posisi pengambilan gambar terlalu miring.
- Kamera belum berada pada posisi tegak lurus (90°) terhadap grafem.
- Pencahayaan kurang memadai.
- Grafem terlihat buram atau tidak utuh.

**Saran:**
Silakan gunakan gambar grafem Aksara Ulu Rejang dengan posisi kamera tegak lurus (90°), pencahayaan yang cukup, dan pastikan seluruh grafem terlihat jelas sebelum melakukan deteksi.
""")
