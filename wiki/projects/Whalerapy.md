---
title: Whalerapy
type: project
last-updated: 2026-07-07
---

# Whalerapy

Whalerapy (深海鯨癒) is an aromatherapy machine that senses a user's emotional state from a webcam photo, profiles their scent preferences with a survey, and dispenses a personalised blend of five scent oils through Arduino-controlled pumps. It was developed for a Stanford proposal and as the [[WRO]] 2026 Macau entry. The live codebase is at `OneDrive\桌面\Whalerapy\Aromatherapy Machine` (uv-managed Python project, Python 3.13+); `raw/Whalerapy/` holds the archived materials.

## How a Session Works

1. The user picks a language: English or Traditional Chinese. The whole kiosk UI is bilingual.
2. **Camera scan ("Whale Vision"):** the user presses spacebar to snap a photo. MediaPipe's face detector (`detector.tflite`, BlazeFace) finds the face, and a Mini-XCEPTION model (trained on FER-2013) classifies the emotion.
3. The seven emotion classes are grouped into two states: **Energetic** (Happy, Surprise) and **Chill** (Angry, Disgust, Fear, Sad, Neutral). The machine prescribes the opposite of what it senses: an energetic user gets 1 drop of Chill oil, a chill user gets 1 drop of Energy oil.
4. **Deep Sea Survey:** ten bilingual lifestyle questions, each with a Wood, Flower, or Fruit answer. The three scores are split proportionally across 4 drops, rounded to 0.5-drop increments using a largest-remainder method.
5. **Results:** a pie chart drawn on a native canvas shows the final 5-drop blend (4 survey drops plus 1 prescribed drop) with a bilingual legend.
6. The five drop counts are sent over USB serial (COM3, 9600 baud) as a comma-separated line. Without an Arduino attached, the app runs in PC Test Mode and prints the command instead.

## Hardware

The Arduino sketch (`sketch_jun13a.ino`) drives five pumps on digital pins 9 to 13: Chill (9), Flower (10), Wood (11), Fruit (12), Energetic (13). It parses the five drop counts from serial and runs each pump for 5 seconds per drop, with a 0.5 second pause between pumps.

## Key Files

- `main.py`: the full kiosk application (CustomTkinter GUI, camera scan, survey, pie chart, serial output).
- `sketch_jun13a/sketch_jun13a.ino`: Arduino pump controller.
- `emotion_detectortest.py`: standalone webcam test of the MediaPipe plus Mini-XCEPTION Chill/Energetic pipeline.
- `backup.py`: an earlier revision of `main.py` (differs mainly in serial port, COM4).
- `surveyandui.py`: an earlier Raspberry Pi variant using gpiozero with three pumps on GPIO 17/27/22, English only.
- `detector.tflite`, `fer2013_mini_XCEPTION.102-0.66.hdf5`: face detection and emotion model weights.
- `pyproject.toml`, `uv.lock`: uv-managed environment (customtkinter, mediapipe, opencv-python, serial, tensorflow).

## Historical Note

The project README and earlier wiki versions describe a Colab-era pipeline using OpenCV Haar cascades for face detection plus a speech emotion branch (OpenAI Whisper, MFCC features, SVM). The current application (code last updated 2026-06-20) uses MediaPipe for face detection and contains no speech pipeline. The speech emotion work exists only in the older materials.

## Team

Two different team credits appear across the competition materials, likely reflecting different submission tracks:

- **Stanford track:** Adrian Ao, [[Gabriel Lo]], [[Yves Wong]] — Pui Ching Middle School (Coloane Campus).
- **WRO / brochure track:** Oscar Ao, Cabrina Wong, Abigail Choi — Pui Ching Middle School (Coloane Campus).

Adrian confirmed (2026-07-08) that the two team credits are correct: the Stanford and WRO/brochure submissions have different team compositions.

## Competition Materials

### Stanford Submission

A suite of Canva materials was prepared for a Stanford competition submission. The credited team is Adrian Ao, [[Gabriel Lo]], and [[Yves Wong]].

- 18-slide competition presentation (updated Jul 2026; was 17 slides as of Jun 2026).
- 17-page proposal document.
- 2-page poster (standard format).
- 3-page poster (60 × 160 cm large-format exhibition version, created Jul 2026).
- 2-page leaflet (expanded from 1 page in Jun 2026 to 2 pages by Jul 2026).

#### Business Case (from 60 × 160 cm Poster)

- **Positioning:** Smart Terminal for Personal Mental Wellness (not a conventional diffuser).
- **Target market:** Students and young professionals (16–35) under high stress.
- **Prototype BOM:** $28.50 USD; MSRP target $76–89 HKD (60%+ margin); $50 early-bird.
- **Business model:** Razor and Blades — hardware sale plus $11 USD monthly refill kit subscription; B2B channel for schools and corporate wellness programmes.
- **Go-to-market:** Digital campaigns (#WhaleRapyMe) and campus activations with live AI emotion-detection demos during exam periods.

#### SDG Alignment

- SDG 3: Good Health and Well-Being.
- SDG 4: Quality Education.
- SDG 9: Industry, Innovation and Infrastructure.

#### Five Scents

| Scent | Profile | Mental benefits |
|-------|---------|-----------------|
| Agarwood | Deep, woody | Relieves fatigue, calms restlessness, eases insomnia |
| Osmanthus | Warm, floral | Lessens anxiety, improves sleep, balances mood swings |
| Sandalwood | Mild, woody | Clears brain fog, fights inflammation |
| Pine | Heavy, woody | Relaxes tension, boosts focus, clears congestion |
| Bergamot | Fresh, citrus | Lifts low spirits, boosts energy |

Selection rationale: covers floral, wood, balsamic, and citrus tones, integrating traditional aromatherapy with Chinese herbal medicine.

### Brochure

Two Whalerapy product brochures (2 pages each) were created in July 2026, credited to Oscar Ao, Cabrina Wong, and Abigail Choi. Content includes testing results, product highlights, and target audience. Key testing findings:

- Improved emotional awareness through AI facial emotion analysis.
- Effective personalisation: scent preference surveys generated aroma formulas users found relevant.
- High user satisfaction: convenience, uniqueness, and relaxing effects rated highly.

### World Robot Olympiad (WRO) 2026 Macau

A separate set of materials was prepared for the [[WRO]] Macau submission:

- 24-slide Canva presentation (2026 Macau WRO Whalerapy Presentation).
- 16-page WRO proposal.
- 2-page WRO poster.

## Related Projects

- [[Emotion Head]]: shares the Mini-XCEPTION facial emotion model.
- [[WRO]]: the World Robot Olympiad competition for which Whalerapy is the 2026 Macau entry.

## Status

Working prototype: bilingual kiosk app with camera sensing, survey, blend calculation, and Arduino pump control. Stanford proposal submitted June 2026. WRO 2026 Macau materials submitted June 2026. See [[Whalerapy Improvements]] for the suggested backlog.
