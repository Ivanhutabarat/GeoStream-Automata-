# 🛰️ GeoStream-Automata v1.1
> **Advanced Geophysical Automation System for Mobile & Desktop**
> Developed with ❤️ by **Ivan Krisopras Hutabarat** (Teknik Geofisika ITERA)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Geophysics](https://img.shields.io/badge/Focus-Geophysics-green?style=for-the-badge)
![Termux](https://img.shields.io/badge/Environment-Termux-orange?style=for-the-badge&logo=termux)
![VSCode](https://img.shields.io/badge/IDE-VS_Code-blue?style=for-the-badge&logo=visual-studio-code)

---

## 🌟 Overview
GeoStream-Automata adalah asisten digital pintar yang dirancang khusus untuk mahasiswa dan praktisi Geofisika. Sistem ini memproses data lapangan (Gravity & Resistivity) secara instan, menghasilkan anomali, dan melakukan visualisasi data langsung ke dalam grafik profesional.

### 📊 Preview Output
![GeoStream Visualizer](https://drive.google.com/uc?export=view&id=1dJVK1PePrj3q2NfYGgo53c7GwcmAost-)
*Gambar 1: Contoh Grafik Profil Anomali Bouguer (SBA) hasil olahan GeoStream v1.1*

---

## 🚀 Fitur Utama (Core Engines)

* **[1] 🌏 Gravity Engine**: Menghitung Koreksi Udara Bebas (FAC), Koreksi Bouguer (BC), hingga **Simple Bouguer Anomaly (SBA)**.
* **[2] ⚡ Resistivity Engine**: Pengolahan data Geolistrik konfigurasi **Schlumberger** (Hitung Faktor Geometri K & Resistivitas Semu $\rho_a$).
* **[3] 📉 Data Visualizer**: Automasi pembuatan grafik profil anomali (.png) menggunakan Matplotlib & Seaborn.
* **[4] 🔄 Auto-Sync**: Backup data otomatis ke GitHub & Notifikasi update ke WhatsApp Bot.

---

## 💻 Panduan Instalasi & Penggunaan

### 📱 Di Termux (Android)
Jalankan perintah berikut secara berurutan:
```bash
# 1. Update sistem & Install compiler
pkg update && pkg upgrade
pkg install python clang make libjpeg-turbo freetype

# 2. Install library Geofisika
pip install numpy pandas matplotlib seaborn colorama

# 3. Clone & Jalankan
git clone [https://github.com/Ivanhutabarat/GeoStream-Automata-](https://github.com/Ivanhutabarat/GeoStream-Automata-)
cd GeoStream-Automata-
python main.py

🔵 Di VS Code (Laptop/PC)
​Clone Repository: git clone https://github.com/Ivanhutabarat/GeoStream-Automata-
​Buka Folder: Open folder di VS Code.
​Install Modul: Buka Terminal (Ctrl + ~) lalu ketik:
pip install numpy pandas matplotlib seaborn colorama
​Run: Buka main.py dan klik tombol Play atau ketik python main.py.
​📝 Catatan Teknis
​Input Desimal: Selalu gunakan tanda TITIK (.), bukan koma. Contoh: 150.5.
​Densitas: Jika densitas batuan tidak diketahui, tekan ENTER untuk menggunakan nilai standar 2.67 g/cm³.
​Lokasi Output: Grafik hasil visualisasi tersimpan di folder /results.
​🤝 Kontribusi
​Jika kamu mahasiswa Geofisika dan ingin menambahkan modul baru (Magnetik, Seismik, dll), silakan ajukan Pull Request atau hubungi Ivan!
​#GeophysicsITERA #CodeForScience #GeoStream #LampungGeophysics
