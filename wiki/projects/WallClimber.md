---
title: WallClimber
type: project
last-updated: 2026-06-21
---

# WallClimber

WallClimber is a wall-climbing robot that uses a vacuum pump to adhere to surfaces. The pump is controlled via an Arduino sketch.

## Key Files

- `vacuum_pump_controller.ino` — Arduino sketch for vacuum pump control.

## 15-DOF Humanoid Robot

The project also includes a 15-degree-of-freedom humanoid robot, for which a full set of reference materials is available:

- **Installation manual:** `15自由度人形机器人安装说明书.pdf`.
- **Serial communication:** Protocol documentation and example code for 51 microcontroller (STC12C5A60S2, Keil) and STM32F103, at both 11.0592 MHz and 22.1184 MHz crystal frequencies.
- **Action groups:** Pre-defined motion sequence files.
- **Debugging software:** PC-based action debugging tool with user manual.
- **Mobile control:** Android app for wireless control.
- **Controller:** USB driver, user manual, and demo video.
- **Hardware:** Structural parts diagrams.

## Technologies

- Arduino (vacuum pump control).
- 51 microcontroller (STC12C5A60S2), Keil IDE.
- STM32F103.
- Serial (UART) communication.
- Android app control.
- Vacuum pump hardware.

## Status

Hardware prototype. Adrian to confirm competition context (likely Robo Fest or [[WRO]]).
