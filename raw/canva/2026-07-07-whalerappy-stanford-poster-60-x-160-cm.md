> canva: WhaleRapy Stanford Poster (60 x 160 cm). Large-format 3-page exhibition poster for the Stanford competition presenting the full Whalerapy product concept, scent science, hardware architecture, and business case.

---
source: canva
captured: 2026-07-07
---

## Design Details

- **Title:** WhaleRapy Stanford Poster (60 x 160 cm)
- **Design type:** Custom large-format poster (3 pages)
- **Last updated:** 2026-07-07
- **Team:** Adrian Ao, Gabriel Lo, Yves Wong — Pui Ching Middle School (Coloane Campus)

## Content

### Page 1 — Product Overview and Aromatherapy Science

**Problem statement:** In today's high-pressure world, chronic stress takes a heavy toll on focus, sleep, and overall health. WhaleRapy is a whale-shaped smart device combining AI, Traditional Chinese Medicine emotional theory, and aromatherapy to automatically craft personalised scent remedies.

**How it works:** 1. Webcam captures facial expression. 2. AI classifies mood as Energetic or Chill. 3. User completes an ocean-themed questionnaire for scent preference. 4. Python calculates a 5-drop formula. 5. USB serial sends the formula to Arduino. 6. Multi-channel pumps and atomizer release the blend.

**Five selected scents:**

| Scent | Profile | Mental benefits |
|-------|---------|-----------------|
| Agarwood | Deep, woody | Relieves fatigue, calms restlessness, eases insomnia |
| Osmanthus | Warm, floral | Lessens anxiety, improves sleep, balances mood swings |
| Sandalwood | Mild, woody | Clears brain fog, fights inflammation |
| Pine | Heavy, woody | Relaxes tension, boosts focus, clears congestion |
| Bergamot | Fresh, citrus | Lifts low spirits, boosts energy |

The five scents cover floral, wood, balsamic, and citrus tones, integrating traditional aromatherapy with Chinese herbal medicine.

### Page 2 — Hardware Architecture and System Flow

**Hardware components:**
- Webcam (facial capture)
- Arduino Uno (dispensing control)
- Relay modules (one per scent channel)
- Fragrance pumps and atomizer activators
- Ultrasonic atomizer (turns blend into inhalable mist)
- Whale-shaped, 3D-printed enclosure
- Power supply (Arduino, relays, dispensers)

**System flow (closed loop):**
1. AI emotion recognition classifies user as Energetic or Chill.
2. Python calculates personalised 5-drop formula from mood and preference data.
3. Arduino and relay modules coordinate precise, automated fragrance delivery.
4. Ultrasonic atomizer disperses the blend as a fine mist.

**SDG alignment:**
- SDG 3: Good Health and Well-Being — promotes emotional wellness through personalised aromatherapy.
- SDG 4: Quality Education — hands-on STEM learning project (AI, programming, electronics, engineering design).
- SDG 9: Industry, Innovation and Infrastructure — integrates AI, computer vision, software, and embedded systems.

### Page 3 — Results and Business Case

**Testing results:** System reliably generates a personalised formula from facial expressions and survey data and drives hardware accurately. AI effectively identifies core emotional states; questionnaire enhances personalisation. Users report boosted focus and improved relaxation.

**Business case:**

- **Positioning:** Smart Terminal for Personal Mental Wellness (not a conventional diffuser).
- **Target market:** Students (16–35) under academic pressure and young professionals.
- **Prototype BOM cost:** $28.50 USD.
- **MSRP target:** $76–89 HKD (60%+ margin); $50 early-bird price.
- **Business model:** Razor and Blades — hardware sale plus $11 USD monthly refill kit subscription; B2B channel targeting schools and corporate wellness (EAP) programmes.
- **Go-to-market:** Digital campaigns (#WhaleRapyMe) and campus activations with live AI emotion-detection demos at partner schools during exam periods.

**SWOT:**
- Strengths: Unique AI + TCM cross-over; 60%+ margin; low BOM cost.
- Weaknesses: New brand with low awareness; requires external PC and camera.
- Opportunities: Growing wellness market; B2B gap in schools and corporates.
- Threats: Easy for large brands to copy; scent-use regulations.

**References:** Ekman (1992), FER-2013 Dataset (Goodfellow et al.), Google MediaPipe, TensorFlow/Keras, Arduino, OECD (2022), WHO (2021).
