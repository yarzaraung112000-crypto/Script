#!/bin/bash

echo "[*] Installing Termux Packages..."
pkg update && pkg upgrade -y
pkg install python clang cmake libjpeg-turbo libpng git -y

echo "[*] Upgrading pip and installing Python libraries..."
pip install --upgrade pip
pip install opencv-python ddddocr numpy aiohttp requests urllib3

echo "[✓] All packages installed successfully!"
