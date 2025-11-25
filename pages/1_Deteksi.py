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

st.markdown("<h2 style='color:#2E86C1; text-align:center;'>🔍 Mode Deteksi Aksara</h2>", unsafe_allow_html=True)

mode = st.radio(
    "Pilih Mode Deteksi:",
    ["📷 Ambil Foto Kamera", "🖼️ Upload Gambar"]
)

# MODE KAMERA
if mode == "📷 Ambil Foto Kamera":
    st.info("📹 Ambil foto dengan kamera HP/laptop, lalu sistem akan mendeteksi aksara.")
    camera_file = st.camera_input("Aktifkan Kamera dan Ambil Foto")

    if camera_file is not None:
        image = Image.open(camera_file).convert("RGB")
        st.image(image, caption="📸 Foto dari kamera", use_column_width=True)

        results = model.predict(image, imgsz=640, conf=0.5)
        plotted = results[0].plot()

        # convert BGR -> RGB
        plotted = cv2.cvtColor(plotted, cv2.COLOR_BGR2RGB)

        st.image(plotted, caption="✅ Hasil Deteksi Aksara", use_column_width=True)

# MODE UPLOAD
else:
    st.info("🖼️ Silakan upload gambar untuk deteksi.")
    uploaded_file = st.file_uploader("📂 Pilih gambar", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="🖼️ Gambar yang diupload", use_column_width=True)

        results = model.predict(image, imgsz=640, conf=0.5)
        plotted = results[0].plot()

        # convert BGR -> RGB
        plotted = cv2.cvtColor(plotted, cv2.COLOR_BGR2RGB)

        st.image(plotted, caption="✅ Hasil Deteksi Aksara", use_column_width=True)
