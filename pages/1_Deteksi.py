import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

st.set_page_config(page_title="Deteksi Aksara", page_icon="🔍")

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

st.markdown(
    "<h2 style='color:#2E86C1; text-align:center;'>🔍 Mode Deteksi Aksara</h2>",
    unsafe_allow_html=True
)

# ==========================
# MODE PILIHAN (tidak default)
# ==========================
mode = st.radio(
    "Pilih Mode Deteksi:",
    ["📷 Ambil Foto Kamera", "🖼️ Upload Gambar"],
    index=None
)

# Jika user belum memilih mode → tampilkan pesan
if mode is None:
    st.warning("Silakan pilih mode deteksi terlebih dahulu.")
    st.stop()

# ==========================
# MODE KAMERA
# ==========================
if mode == "📷 Ambil Foto Kamera":
    st.info("📹 Ambil foto dengan kamera HP/laptop, lalu sistem akan mendeteksi aksara.")
    camera_file = st.camera_input("Aktifkan Kamera dan Ambil Foto")

    if camera_file is not None:
        image = Image.open(camera_file).convert("RGB")

        # Prediksi YOLO
        results = model.predict(image, imgsz=640, conf=0.5)
        plotted = results[0].plot()

        plotted = cv2.cvtColor(plotted, cv2.COLOR_BGR2RGB)

        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption="📸 Foto Asli", use_column_width=True)
        with col2:
            st.image(plotted, caption="✅ Hasil Deteksi Aksara", use_column_width=True)

# ==========================
# MODE UPLOAD GAMBAR
# ==========================
else:
    st.info("🖼️ Silakan upload gambar untuk deteksi.")
    uploaded_file = st.file_uploader("📂 Pilih gambar", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")

        # Prediksi YOLO
        results = model.predict(image, imgsz=640, conf=0.5)
        plotted = results[0].plot()

        plotted = cv2.cvtColor(plotted, cv2.COLOR_BGR2RGB)

        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption="🖼️ Gambar Asli", use_column_width=True)
        with col2:
            st.image(plotted, caption="✅ Hasil Deteksi Aksara", use_column_width=True)
