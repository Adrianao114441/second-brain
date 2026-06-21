---
title: Emotion Head
type: project
last-updated: 2026-06-21
---

# Emotion Head

Emotion Head is a robot therapist prototype that detects a user's facial emotion via webcam and responds with empathetic, psychology-informed dialogue. A physical robot head is controlled via Arduino.

## How It Works

1. The webcam captures the user's face.
2. Emotion is classified using a pre-trained Mini-XCEPTION model (trained on FER-2013), the same model used in the [[Whalerapy]] Aromatherapy Machine.
3. The system maps the detected emotion to a response using `Color_Emotion_Sentence.csv`.
4. An empathetic reply is drawn from `psychology_knowledge.txt`, covering topics such as anxiety, sadness, loneliness, anger, stress, and mindfulness.
5. The Arduino sketch (`Emotion_Head.ino`) controls the physical robot head hardware.

## Emotion Labels

Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral.

## Key Files

- `Emotion_Head.py` — main Python script.
- `psychology_knowledge.txt` — curated empathetic response library.
- `Color_Emotion_Sentence.csv` — colour-to-emotion-to-sentence mapping.
- `Emotion_Head.ino` — Arduino hardware control sketch.

## Technologies

- Python, OpenCV, Keras.
- Arduino.
- FER-2013 dataset (via pre-trained model).

## Related Projects

- [[Whalerapy]] — shares the same emotion detection pipeline.
- [[MonkeyBuddy]] — reuses `Emotion_Head.py`.
- [[表情機器人交互]] — related facial expression robot reference materials.

## Status

Prototype completed. Test images captured in November and December 2025.
