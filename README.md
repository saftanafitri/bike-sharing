**Dashboard Penyewaan Sepeda**

https://bikesharingsafta.streamlit.app/

**Deskripsi Proyek**

Proyek ini dibuat sebagai bagian dari submission kursus Belajar Analisis Data dengan Python dari Dicoding. Analisis ini berfokus pada data penyewaan sepeda untuk mengidentifikasi tren berdasarkan waktu, musim, dan kondisi lingkungan yang memengaruhi jumlah penyewaan.  


 **Sumber Data** 

Dataset yang digunakan dalam proyek ini berisi data penyewaan sepeda yang mencakup variabel seperti waktu, musim, cuaca, dan jumlah penyewaan dalam satuan jam

sumber: https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset 

**Insight Utama**  

Jumlah penyewaan sepeda cenderung lebih tinggi pada musim panas dan lebih rendah pada musim dingin.  
Penyewaan meningkat pada jam sibuk (pagi & sore) dibandingkan siang hari.  
Tren harian menunjukkan pola penggunaan lebih tinggi pada hari kerja dibandingkan akhir pekan.  

**Cara Menjalankan Dashboard**

nb: jalankan di cmd atau terminal

mkdir bike-sharing

cd bike-sharing

pipenv install

pipenv shell

pip install -r requirements.txt

cd dashboard 

streamlit run dashboard.py

