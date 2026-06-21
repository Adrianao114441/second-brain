> claude-sessions: Adrian, Arduino L298N vacuum pump control. Wrote Arduino UNO code to control a DC 12V vacuum pump via an L298N motor driver.

---
source: claude-code
captured: 2026-06-21
session_id: 5b37726c-0b77-405a-86fe-73449e50727b
---

## Session Summary

**Topic:** Arduino motor control code for a wall-climbing robot component.

### What Was Built

- Arduino UNO sketch to control a DC 12V vacuum pump using an L298N motor controller.
- Code written in the `WallClimber` project directory.

### Key Decisions

- Used L298N H-bridge to switch the pump on and off (and potentially control speed via PWM).
- Arduino UNO as the microcontroller.

### Context

This session is part of the Robo Fest / WRO robotics work with teammates Bianca, Ashley, Oscar, Cabrina, and Peony. The wall-climbing robot uses a vacuum pump for suction-based adhesion.

### Open Questions

- Whether PWM speed control of the pump is needed or simple on/off is sufficient.
