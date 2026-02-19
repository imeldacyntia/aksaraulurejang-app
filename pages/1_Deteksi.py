import streamlit as st
from ultralytics import YOLO
from PIL import Image
import cv2

st.set_page_config(page_title="Deteksi Grafem Aksara Ulu Rejang", page_icon="📖")

@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

st.markdown(
    "<h2 style='color:#2E86C1; text-align:center;'>Mode Deteksi Grafem Aksara Ulu Rejang</h2>",
    unsafe_allow_html=True
)

# ==========================
# Inisialisasi session state
# ==========================
if "camera_key" not in st.session_state:
    st.session_state.camera_key = 0

if "upload_key" not in st.session_state:
    st.session_state.upload_key = 0

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

    camera_file = st.camera_input(
        "Aktifkan kamera dan ambil foto",
        key=f"camera_image_{st.session_state.camera_key}"
    )

    if camera_file is not None:
        image = Image.open(camera_file).convert("RGB")

        results = model.predict(image, imgsz=640, conf=0.5)
        plotted = results[0].plot()
        plotted = cv2.cvtColor(plotted, cv2.COLOR_BGR2RGB)

        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption="Foto Asli", use_column_width=True)
        with col2:
            st.image(plotted, caption="Hasil Deteksi Grafem", use_column_width=True)

        if st.button("Hapus Foto dan Hasil Deteksi", key="clear_camera"):
            st.session_state.camera_key += 1
            st.rerun()

# ==========================
# MODE UPLOAD GAMBAR
# ==========================
elif mode == "Upload Gambar":
    st.info("Upload gambar berisi grafem Aksara Ulu Rejang untuk dilakukan deteksi.")

    uploaded_file = st.file_uploader(
        "Pilih gambar (JPG/JPEG/PNG)",
        type=["jpg", "jpeg", "png"],
        key=f"upload_image_{st.session_state.upload_key}"
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")

        results = model.predict(image, imgsz=640, conf=0.5)
        plotted = results[0].plot()
        plotted = cv2.cvtColor(plotted, cv2.COLOR_BGR2RGB)

        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption="Gambar Asli", use_column_width=True)
        with col2:
            st.image(plotted, caption="Hasil Deteksi Grafem", use_column_width=True)

        if st.button("Hapus Gambar dan Hasil Deteksi", key="clear_upload"):
            st.session_state.upload_key += 1
            st.rerun()
