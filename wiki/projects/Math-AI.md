---
title: Math-AI
type: project
last-updated: 2026-06-21
---

# Math-AI

Math-AI is a project exploring AI-assisted mathematics learning. The current focus is on hand gesture recognition as an input modality, implemented using [[MediaPipe]].

## Hand Gesture Recognition

- `hand_detection.py` — a Python script using MediaPipe's Hands solution to detect hand landmarks in real time from a webcam feed and overlay landmark visualisations.
- Uses MediaPipe rather than a custom-trained model.
- Intended to allow students to input mathematical expressions or answers through hand gestures.

## Technologies

- Python.
- MediaPipe (Google's hand landmark detection framework).
- OpenCV (for video capture and display).

## Open Questions

- How hand gestures map to specific mathematical input actions.
- Whether the gesture interface integrates with a broader UI or runs standalone.
- Whether this connects to the [[AI Tutoring Bias Study]] or is a separate learning tool.

## Status

Prototype `hand_detection.py` built. Integration with broader UI pending.
