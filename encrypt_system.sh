#!/bin/bash

# GeoStream-Automata Security Suite
# Mengubah script .sh menjadi biner yang tidak bisa dibaca

if ! command -v shc &> /dev/null; then
    echo "Error: SHC tidak ditemukan. Jalankan setup.sh dulu."
    exit 1
fi

echo "[*] Encrypting Shell Scripts..."

# Daftar file yang akan dienkripsi
files=("auto-start.sh" "tools.sh" "setup.sh")

for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "  -> Securing $file..."
        # -r: Redistributable, -f: File, -S: Secure/Self-destruct if debugged
        shc -rvf "$file"
        # Menghapus file asli (.sh) dan menyisakan binernya (.x)
        rm "$file" "$file.x.c"
        mv "$file.x" "${file%.sh}"
        echo "  [OK] $file is now encrypted as '${file%.sh}'"
    fi
done

echo "------------------------------------------"
echo "Security Hardening Complete, Ivan."
