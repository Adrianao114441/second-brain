---
title: MonkeyBuddy
type: project
last-updated: 2026-06-21
---

# MonkeyBuddy

MonkeyBuddy is a conversational chatbot with a graphical user interface and emotion detection. It reuses the emotion detection module from [[Emotion Head]].

## Components

- **Chatbot:** `Chat_Bot.py` handles conversational logic.
- **Emotion detection:** `Emotion_Head.py` is imported directly from the [[Emotion Head]] project.
- **GUI:** `gui.py` provides the graphical interface (likely Tkinter or similar).
- **Testing:** `test_cases.py` contains a structured test suite.

## Key Files

- `Chat_Bot.py`, `main.py`, `new.py` — chatbot and entry-point variants.
- `Emotion_Head.py` — shared emotion detection module.
- `gui.py` — user interface.
- `test_cases.py` — test cases.

## Technologies

- Python.
- Emotion detection via OpenCV and Keras (shared with [[Emotion Head]]).

## Related Projects

- [[Emotion Head]] — provides the emotion detection module.

## Status

Unknown. Source code and tests present; no README found. Adrian to confirm status.
