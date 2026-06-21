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

## Related Projects

- [[Emotion Head]] — shares the Mini-XCEPTION facial emotion detection pipeline.
- [[Stanford Proposal]] — the proposal submitted in the context of Stanford.

## Status

Prototype built. Stanford proposal submitted. See `raw/Whalerapy/` for full source code.
