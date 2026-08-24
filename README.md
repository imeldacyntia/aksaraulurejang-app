# Sistem Deteksi Grafem Aksara Ulu Rejang

Aplikasi *Computer Vision* berbasis web untuk mendeteksi dan mengenali grafem Aksara Ulu Rejang (aksara tradisional Provinsi Bengkulu) secara *real-time* menggunakan model **YOLOv11** dan framework **Streamlit**.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://aksaraulurejang-app.streamlit.app/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![YOLOv11](https://img.shields.io/badge/YOLO-v11-orange.svg)](https://docs.ultralytics.com/)

---

## Tentang Proyek
Aksara Ulu Rejang merupakan warisan budaya penting dari masyarakat Rejang di Provinsi Bengkulu yang digunakan untuk mendokumentasikan adat, silsilah, dan tradisi. Sistem ini dirancang untuk mendukung digitalisasi dan media pembelajaran aksara lokal dengan mendeteksi **253 kelas grafem dan sandangan** dari citra fon digital maupun tulisan tangan.

### Fitur Utama
- **Deteksi Real-Time:** Deteksi langsung menggunakan webcam / kamera perangkat.
- **Unggah Gambar:** Mendukung inferensi citra dalam format JPG, JPEG, dan PNG.
- **Robust Terhadap Kemiringan:** Mampu mendeteksi grafem pada berbagai orientasi sudut ($45^\circ$ dan $90^\circ$).
- **Zero False-Positive:** Sistem tidak mendeteksi karakter non-target (seperti huruf Latin atau aksara Nusantara lainnya).

---

## Performa Model & Eksperimen
Model dibangun melalui eksperimen **Hyperparameter Tuning (Grid Search)** dengan 8 skenario berbeda selama 100 *epoch*. Konfigurasi terbaik diperoleh menggunakan:

* **Optimizer:** AdamW
* **Learning Rate (lr):** 0.01
* **Weight Decay:** 0.00005

### Hasil Evaluasi Model:
| Metrik Evaluasi | Nilai |
| :--- | :---: |
| **Precision** | **98.8%** (0.988) |
| **Recall** | **99.3%** (0.993) |
| **mAP@50** | **99.3%** (0.993) |
| **mAP@50-95** | **82.3%** (0.823) |
| **F1-Score** | **0.99** |

---

## Tech Stack
- **Bahasa:** Python
- **Model Object Detection:** YOLOv11 (`ultralytics`)
- **Computer Vision:** OpenCV, Pillow (PIL)
- **Data Processing:** NumPy, Pandas, Matplotlib
- **Web Interface / Deployment:** Streamlit, Streamlit Community Cloud
