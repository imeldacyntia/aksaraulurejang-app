import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(page_title="Deteksi Aksara", page_icon="🔍")

# Load model YOLO (cache biar gak reload terus)
@st.cache_resource
def load_model():
    return YOLO("best.pt")  # pastikan file best.pt ada di repo

model = load_model()

st.markdown("<h2 style='color:#2E86C1; text-align:center;'>🔍 Mode Deteksi Aksara</h2>", unsafe_allow_html=True)

# Styling radio button
st.markdown("""
    <style>
    div.row-widget.stRadio > div {flex-direction: row;}
    label[data-baseweb="radio"] div[role="img"] {
        font-size: 22px;
        margin-right: 6px;
    }
    </style>
""", unsafe_allow_html=True)

mode = st.radio(
    "Pilih Mode Deteksi:",
    ["📷 Ambil Foto Kamera", "🖼️ Upload Gambar"]
)

# --- MODE KAMERA (streamlit camera_input, bukan cv2.VideoCapture) ---
if mode == "📷 Ambil Foto Kamera":
    st.info("📹 Ambil foto dengan kamera HP/laptop, lalu sistem akan mendeteksi aksara.")
    camera_file = st.camera_input("Aktifkan Kamera dan Ambil Foto")

    if camera_file is not None:
        image = Image.open(camera_file).convert("RGB")
        st.image(image, caption="📸 Foto dari kamera", use_column_width=True)

        # Prediksi YOLO
        results = model.predict(image, imgsz=640, conf=0.5)
        res_plotted = results[0].plot()
        st.image(res_plotted, caption="✅ Hasil Deteksi Aksara", use_column_width=True)

# --- MODE UPLOAD GAMBAR ---
elif mode == "🖼️ Upload Gambar":
    st.info("🖼️ Silakan upload gambar JPG/PNG untuk deteksi.")
    uploaded_file = st.file_uploader("📂 Pilih gambar", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="🖼️ Gambar yang diupload", use_column_width=True)

        # Prediksi YOLO
        results = model.predict(image, imgsz=640, conf=0.5)
        res_plotted = results[0].plot()
        st.image(res_plotted, caption="✅ Hasil Deteksi Aksara", use_column_width=True)
