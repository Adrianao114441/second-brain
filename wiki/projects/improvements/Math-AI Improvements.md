---
title: Math-AI Improvements
type: improvements
last-updated: 2026-07-06
---

# Math-AI Improvements

Suggested improvements for [[Math-AI]]. These are agent suggestions, not commitments; move an item into `priorities.md` when Adrian decides to act on it.

## Design

- Define the gesture-to-input mapping: which hand gestures produce which mathematical symbols or actions. This is the project page's first open question and blocks everything downstream.
- Decide whether the gesture interface runs standalone or inside a broader tutoring UI, and sketch that UI before writing more code.

## Knowledge Gaps

- Clarify whether Math-AI connects to the AI Tutoring Bias Study or is a separate learning tool, and update both pages accordingly.

## Technical

- Add a small evaluation script measuring gesture recognition accuracy and latency with MediaPipe on the target hardware, so design decisions rest on measured performance.
