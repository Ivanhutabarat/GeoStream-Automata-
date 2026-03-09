#!/bin/bash

# GeoStream-Automata Utility Tools
# Author: Ivan Krisopras Hutabarat

function clean_results() {
    echo "[*] Cleaning results folder..."
    rm -rf results/*
    echo "[+] Done."
}

function backup_data() {
    echo "[*] Backing up data to storage..."
    timestamp=$(date +"%Y%m%d_%H%M%S")
    cp -r data/ "storage/backup_$timestamp"
    echo "[+] Backup completed."
}

# Menu Sederhana
echo "GeoStream Tools:"
echo "1. Clean Results"
echo "2. Backup Data"
read -p "Choose option: " opt

case $opt in
    1) clean_results ;;
    2) backup_data ;;
    *) echo "Invalid option" ;;
esac
