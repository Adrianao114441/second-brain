# Emotion Head

## Overview
A robot therapist project that detects a user's facial emotion via webcam and responds with empathetic, psychology-informed dialogue. Uses a colour-emotion mapping and a curated psychology knowledge base. An Arduino component controls the physical robot head hardware.

## Key Files
- `Emotion_Head.py` — main Python script; handles face capture, emotion detection, and response generation.
- `psychology_knowledge.txt` — curated empathetic responses covering anxiety, sadness, loneliness, anger, stress, mindfulness, and self-compassion.
- `Color_Emotion_Sentence.csv` — mapping of colours to emotions and corresponding sentences.
- `Emotion_Head.ino` — Arduino sketch for the physical robot head.
- `captured_image/` — folder of test images captured during sessions.

## Technologies
- Python (computer vision, emotion detection).
- Arduino (hardware control).
- Likely uses OpenCV or a similar library for face capture.

## Related Projects
- Whalerapy Aromatherapy Machine (also uses emotion detection).
- MonkeyBuddy (reuses Emotion_Head.py).

## Status
Active or completed prototype. Captured test images present from November–December 2025.
