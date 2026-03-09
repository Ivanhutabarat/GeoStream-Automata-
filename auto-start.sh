#!/bin/bash

# GeoStream-Automata Launcher
# Protect this file with SHC later for self-destruct feature

clear
if [ -f "main.py" ]; then
    python main.py
else
    echo "Error: Core engine (main.py) not found!"
    exit 1
fi
