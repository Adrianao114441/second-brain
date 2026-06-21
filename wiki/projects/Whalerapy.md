---
title: Whalerapy
type: project
last-updated: 2026-06-21
---

# Whalerapy



Whalerapy is an aromatherapy machine that detects a user's emotional state and responds with an appropriate aromatherapy treatment. It was developed as part of a Stanford proposal. The project combines facial emotion detection, speech-based emotion detection, and physical hardware control via Arduino.

## Emotion Detection Pipeline

### Facial Emotion Detection

- Uses OpenCV's Haar cascades for face detection.
- Classifies emotion using a pre-trained **Mini-XCEPTION** model trained on the **FER-2013** dataset.
- Seven emotion classes: Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral.
- Runs in Google Colab or locally.

### Speech-Based Emotion Detection

- Transcribes speech using **OpenAI Whisper**.
- Extracts **MFCC** and pitch features using Librosa.
- Classifies emotional tone with an SVM classifier (currently trained on synthetic data; can be replaced with RAVDESS or IEMOCAP datasets).
- Four speech emotion classes: Happy, Sad, Angry, Neutral.

## Hardware

- Arduino sketch (`sketch_jun13a.ino`) controls the physical aromatherapy dispenser.

## Key Files

- `main.py` — main application entry point.
- `emotion_detectortest.py` — emotion detection tests.
- `backup.py` — backup version.
- `surveyandui.py` — survey and user interface logic.
- `detector.tflite` — TensorFlow Lite model for on-device inference.
- `fer2013_mini_XCEPTION.102-0.66.hdf5` — pre-trained facial emotion model weights.
- `sketch_jun13a/sketch_jun13a.ino` — Arduino hardware sketch.

## Technologies

- Python, OpenCV, Keras, TensorFlow Lite.
- OpenAI Whisper, Librosa, scikit-learn.
- Arduino.

## Competition Materials

### Stanford Submission

A suite of Canva materials was prepared for a Stanford competition submission:

- 17-slide competition presentation.
- 17-page proposal document.
- 2-page poster.
- 1-page leaflet.

All four assets were last edited on 2026-06-19.

### World Robot Olympiad (WRO) 2026 Macau

A separate set of materials was prepared for the [[WRO]] Macau submission:

- 24-slide Canva presentation (2026 Macau WRO Whalerapy Presentation).
- 16-page WRO proposal.
- 2-page WRO poster.

## Related Projects

- [[Emotion Head]] — shares the Mini-XCEPTION facial emotion detection pipeline.
- [[WRO]] — the World Robot Olympiad competition for which Whalerapy is the 2026 Macau entry.

## Status

Prototype built. Stanford proposal submitted June 2026. WRO 2026 Macau materials submitted June 2026. See `raw/Whalerapy/` for full source code and `raw/canva/` for competition assets.
