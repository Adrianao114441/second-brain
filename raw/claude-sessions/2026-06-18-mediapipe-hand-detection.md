> claude-sessions: Adrian, MediaPipe hand landmark detection. Wrote a Python script using MediaPipe to detect and display hand landmarks from a webcam or video source.

---
source: claude-code
captured: 2026-06-18
session_id: 6f1b01ab-c9d5-4810-aa6a-7cbd0c76155a
---

## Session Summary

**Topic:** Hand landmark detection using MediaPipe in the Math-AI project.

### What Was Built

- `hand_detection.py`: a Python script that uses MediaPipe's Hands solution to detect hand landmarks in real time.
- Written in the `Math-AI` project directory.

### Key Decisions

- Used MediaPipe (Google's framework) for hand landmark detection rather than training a custom model.
- Script likely reads from a webcam feed and overlays landmark visualisations.

### Context

This is part of the Math-AI project, suggesting hand gesture recognition may be used as an input modality for an AI-assisted mathematics learning tool.

### Open Questions

- How hand gestures map to mathematical input actions.
- Whether this integrates with a broader UI or runs standalone.
