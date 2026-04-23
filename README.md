# 🎨 Raspberry Pi Colour Detection Bot

Real-time red colour detection robot using Raspberry Pi 4 and Pi Camera. Detects red objects and estimates their distance from the camera.

## 🤖 Hardware Used
- Raspberry Pi 4
- Raspberry Pi Camera Module
- 2x BO Motors

## 🧠 What It Does
- Captures live video from Pi Camera
- Detects red objects using HSV colour masking
- Estimates distance of detected object from camera
- Displays live feed with bounding contours and distance overlay

## ⚙️ Installation
sudo apt update && sudo apt upgrade -y
pip install opencv-python numpy
sudo raspi-config → Interface Options → Camera → Enable

## ▶️ How to Run
python colour_detection.py
Press Q to quit.

## 💡 Key Concepts
- HSV Colour Space Masking
- Morphological Operations
- Contour Detection
- Distance Estimation using Pinhole Camera Model
