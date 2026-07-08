---
title: Emotion Head Improvements
type: improvements
last-updated: 2026-07-06
---

# Emotion Head Improvements

Suggested improvements for [[Emotion Head]]. These are agent suggestions, not commitments; move an item into `priorities.md` when Adrian decides to act on it.

## Technical

- Evaluate the Mini-XCEPTION model against the test images captured in November and December 2025, and record the accuracy per emotion class.
- Consider a newer emotion model: FER-2013 era models are dated, and the same upgrade would benefit [[Whalerapy]] and [[MonkeyBuddy]] since they share the pipeline.
- Expand `psychology_knowledge.txt` with sourced content, and note where each response comes from, since the replies are presented as psychology informed.
- Extract the emotion detection code into a small shared module: three projects currently copy `Emotion_Head.py` around.

## Next Steps

- Decide whether this prototype has a future (demo, competition, or component library for other projects) or should be marked completed on the project page.
