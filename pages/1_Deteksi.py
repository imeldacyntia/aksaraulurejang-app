import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2

# ==========================
# KONFIGURASI HALAMAN
# ==========================
st.set_page_config(
    page_title="Deteksi Grafem Aksara Ulu Rejang",
    page_icon="📖",
    layout="wide"
)

# ==========================
# LOAD MODEL (CACHE)
# ==========================
@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

st.markdown(
    "<h2 style='color:#2E86C1; text-align:center;'>Mode Deteksi Grafem Aksara Ulu Rejang</h2>",
    unsafe_allow_html=True
)

# ==========================
# PARAMETER INFERENSI
# ==========================
IMG_SIZE = 640
CONF_THRESHOLD = 0.5
IOU_THRESHOLD = 0.45
DEVICE = "cpu"  # gunakan "cpu" untuk deployment

# ==========================
# FUNGSI DETEKSI
# ==========================
def detect_image(image):
    """
    Melakukan inferensi YOLO pada gambar
    """
    try:
        # Resize agar konsisten 640x640
        image_resized = image.resize((IMG_SIZE, IMG_SIZE))

        results = model.predict(
            image_resized,
            imgsz=IMG_SIZE,
            conf=CONF_THRESHOLD,
            iou=IOU_THRESHOLD,
            device=DEVICE,
            verbose=False
        )

        plotted = results[0].plot()
        plotted = cv2.cvtColor(plotted, cv2.COLOR_BGR2RGB)

        return image_resized, plotted

    except Exception as e:
        st.error(f"Terjadi kesalahan saat deteksi: {e}")
        return None, None


# ==========================
# MODE PILIHAN
# ==========================
mode = st.radio(
    "Pilih Mode Deteksi:",
    ["Ambil Foto Kamera", "Upload Gambar"],
    index=None
)

if mode is None:
    st.warning("Silakan pilih mode deteksi terlebih dahulu.")
    st.stop()

# ==========================
# MODE KAMERA
# ==========================
if mode == "Ambil Foto Kamera":

    st.info("Ambil foto menggunakan kamera kemudian sistem akan mendeteksi grafem pada gambar.")

    camera_file = st.camera_input("Aktifkan kamera dan ambil foto")

    if camera_file is not None:
        image = Image.open(camera_file).convert("RGB")

        original, detected = detect_image(image)

        if original is not None:
            col1, col2 = st.columns(2)

            with col1:
                st.image(original, caption="Foto Asli", use_column_width=True)

            with col2:
                st.image(detected, caption="Hasil Deteksi Grafem", use_column_width=True)


# ==========================
# MODE UPLOAD GAMBAR
# ==========================
elif mode == "Upload Gambar":

    st.info("Upload gambar berisi grafem Aksara Ulu Rejang untuk dilakukan deteksi.")

    uploaded_file = st.file_uploader(
        "Pilih gambar (JPG/JPEG/PNG)",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")

        original, detected = detect_image(image)

        if original is not None:
            col1, col2 = st.columns(2)

            with col1:
                st.image(original, caption="Gambar Asli (Resized 640x640)", use_column_width=True)

            with col2:
                st.image(detected, caption="Hasil Deteksi Grafem", use_column_width=True)
