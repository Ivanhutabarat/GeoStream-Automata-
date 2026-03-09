#!/bin/bash

# --- GeoStream-Automata Installer ---
# Author: Ivan Krisopras Hutabarat

echo "------------------------------------------"
echo "Initializing GeoStream-Automata System..."
echo "------------------------------------------"

# 1. Membuat Struktur Folder agar rapi seperti di gambar
mkdir -p data lib matlab n8n node_modules notebooks session storage core results utils

# 2. Menginstal Dependency System
echo "[*] Installing system dependencies..."
if [ -f /data/data/com.termux/files/usr/bin/pkg ]; then
    pkg update && pkg upgrade -y
    pkg install python git shc openssl -y
else
    sudo apt-get update
    sudo apt-get install python3 python3-pip git shc openssl -y
fi

# 3. Menginstal Python Libraries
echo "[*] Installing Python requirements..."
pip install -r requirements.txt

# 4. Pesan Berhasil
echo "------------------------------------------"
echo "Setup Complete, Van!"
echo "Folders are organized and system is ready."
echo "------------------------------------------"
