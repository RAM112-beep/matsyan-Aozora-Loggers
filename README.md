# 🌊 AQUA PATROL — AOZORA LOGGERS

AI-Powered Illegal Fishing Detection System using Satellite Imagery and Deep Learning

---

## 📌 Problem Statement

Illegal, unreported, and unregulated (IUU) fishing poses a major threat to ocean ecosystems and maritime economies. Many vessels operate covertly within protected marine zones, escaping conventional detection. This project aims to automate the detection of illegal fishing vessels using satellite images and machine learning.

---

## 🚀 Project Description

AQUA PATROL is a web-based AI system that detects fishing vessels in satellite images and determines whether they are within designated illegal zones (e.g., marine protected areas). The application uses YOLOv5 for object detection and overlays detections on a map with marked zones. The goal is to assist authorities in real-time monitoring and enforcement.

---

## 🛠 Tech Stack Used

- Python 3.12
- Flask (Backend)
- YOLOv5 (Object Detection)
- OpenCV, NumPy, Pillow
- HTML/CSS (Frontend)
- GeoJSON (Illegal Zone Mapping)
- Git & GitHub

---

## 📁 Folder Structure
AI_Fishing_WebApp/
├── app.py
├── illegal_fishing_ai.py
├── requirements.txt
├── yolov5s.pt
├── illegal_zones.geojson
├── templates/
│   └── index.html
├── static/
│   ├── uploads/
│   └── results/
├── README.md
├── LICENSE
