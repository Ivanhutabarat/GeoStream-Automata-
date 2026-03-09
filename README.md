
# 🌐 GeoStream-Automata v1.0
> **Integrated Geophysics Data Toolkit for Termux & VS Code**

[![Author](https://img.shields.io/badge/Author-Ivan%20Krisopras%20Hutabarat-black?style=flat-square)](https://github.com/Ivanhutabarat)
[![Major](https://img.shields.io/badge/Major-Geophysical%20Engineering-green?style=flat-square)](https://itera.ac.id)
[![Environment](https://img.shields.io/badge/Env-Termux%20%7C%20VS%20Code-orange?style=flat-square)](https://github.com)

---

## 📖 Deskripsi
**GeoStream-Automata** adalah toolkit otomasi untuk pengolahan data geofisika (Gaya Berat, Geolistrik, dan Seismik) yang dirancang agar sinkron antara perangkat mobile (Termux) dan desktop (VS Code). Proyek ini dikembangkan oleh **Ivan Hutabarat** untuk mendukung efisiensi pengolahan data lapangan secara real-time.

## 🛡️ Keamanan & Lisensi
> [!CAUTION]
> **PROTECTED SOURCE CODE**
> Seluruh script eksekusi (`.sh`) dalam repository ini telah dienkripsi menggunakan **SHC (Shell Script Compiler)** dengan fitur *Anti-Debug* dan *Environment Hardening*. Upaya pembongkaran kode secara ilegal akan memicu *Self-Destruct* (SIGKILL).

## 🚀 Fitur Utama
- **Gravity Engine:** Kalkulator Koreksi Udara Bebas (FAC) dan Koreksi Bouguer (BC).
- **Resistivity Tools:** Pengolahan data geolistrik (Hukum Archie & Konfigurasi Schlumberger).
- **Auto-Sync:** Sinkronisasi otomatis data lapangan ke GitHub/PC TITANCORE.
- **WhatsApp Integration:** Notifikasi hasil olah data via n8n Bot.

## 🛠️ Instalasi (Termux)
```bash
pkg update && pkg upgrade
pkg install python git shc
git clone [https://github.com/Ivanhutabarat/GeoStream-Automata](https://github.com/Ivanhutabarat/GeoStream-Automata)
cd GeoStream-Automata
pip install -r requirements.txt
chmod +x geostream
./geostream
