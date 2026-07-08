---
title: Whalerapy Improvements
type: improvements
last-updated: 2026-07-06
---

# Whalerapy Improvements

Suggested improvements for [[Whalerapy]], based on a code review of `OneDrive\桌面\Whalerapy\Aromatherapy Machine` on 2026-07-06. These are agent suggestions, not commitments; move an item into `priorities.md` when Adrian decides to act on it.

## Code Cleanup

- Rewrite `README.md`: it still describes the old Colab pipeline (Haar cascades, Whisper speech emotion) and does not mention the actual kiosk app, the survey, or the Arduino protocol.
- Delete `backup.py`: it is an earlier revision of `main.py`. The project has a `.gitignore`, so use git history for old versions instead of backup files.
- Decide the fate of `surveyandui.py` (the Raspberry Pi gpiozero variant with three pumps): delete it if the Windows plus Arduino design is final, or fold its Pi support into the main app if a Pi build is still planned.
- Move the hardcoded serial port (`COM3` in `main.py`, `COM4` in `backup.py`) into a config value or auto-detect the Arduino, so the app works when the USB port changes.

## Design Review

- Reconsider the emotion grouping: Angry, Disgust, and Fear currently count as "Chill", so an angry user is prescribed Energy oil. Grouping negative arousal emotions with calm ones deserves a deliberate decision, and the rationale should be documented for competition judging.
- Handle the no-face case visibly: if detection fails, the session silently continues with no prescribed drop (4 drops instead of 5). Offer a retake instead.

## Technical

- The GUI freezes while pumps run: the Arduino sketch blocks up to 5 seconds per drop and `main.py` writes to serial on the UI thread. Send the command from a background thread and show a "dispensing" screen.
- Add an acknowledgement byte from the Arduino after dispensing, so the app knows the blend finished rather than assuming.
- Evaluate the Mini-XCEPTION model's Chill/Energetic accuracy on real user photos and record the numbers; proposals currently cite the model without local evidence.
- Document the physical build: which oil reservoir feeds which pump on pins 9 to 13, power supply, and tubing layout, so teammates can rebuild the machine.

## Knowledge Gaps

- Record the Stanford proposal outcome when announced, then update the project page and `priorities.md` Archive.
- Record the WRO 2026 Macau result and judge feedback when available.
- Decide whether the speech emotion branch from the old materials is permanently dropped or planned for a future version.
