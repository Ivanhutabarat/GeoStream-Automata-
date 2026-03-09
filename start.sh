#!/bin/bash

# GeoStream-Automata Quick Start
# Author: Ivan Krisopras Hutabarat

# Pastikan folder results bersih sebelum mulai
if [ -d "results" ]; then
    rm -rf results/*
fi

echo "🚀 Launching GeoStream-Automata..."
python main.py

# Setelah main.py selesai, tawarkan untuk sync
echo "------------------------------------------"
read -p "Do you want to sync results to GitHub? (y/n): " sync_choice
if [ "$sync_choice" == "y" ]; then
    python -c "from core.sync_manager import SyncManager; SyncManager().push_to_git('Update field results')"
fi
