import streamlit as st
import cv2
from ultralytics import YOLO
import numpy as np

st.set_page_config(page_title="Deteksi Aksara", page_icon="🔍")

# Load model YOLO (cache biar gak reload terus)
@st.cache_resource
def load_model():
    return YOLO("C:/Users/ACER/OneDrive/Desktop/python/streamlit/best.pt")  # ganti path kalau beda

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
    ["📷 Kamera Real-time", "🖼️ Upload Gambar"]
)

# MODE KAMERA
if mode == "📷 Kamera Real-time":
    st.info("📹 Mode Kamera Real-time aktif. Klik checkbox untuk menyalakan kamera.")
    run = st.checkbox("▶️ Nyalakan Kamera", value=False)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        FRAME_WINDOW = st.image([])

    if run:
        cap = cv2.VideoCapture(0)
        while run:
            ret, frame = cap.read()
            if not ret:
                st.error("⚠️ Kamera tidak terdeteksi.")
                break

            results = model.predict(frame, imgsz=640, conf=0.5)
            annotated_frame = results[0].plot()

            FRAME_WINDOW.image(annotated_frame, channels="BGR")
        cap.release()

# MODE UPLOAD GAMBAR
elif mode == "🖼️ Upload Gambar":
    st.info("🖼️ Silakan upload gambar JPG/PNG untuk deteksi.")
    uploaded_file = st.file_uploader("📂 Pilih gambar", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)

        results = model.predict(img, imgsz=640, conf=0.5)
        annotated_img = results[0].plot()

        st.image(annotated_img, channels="BGR", caption="✅ Hasil Deteksi Aksara")