# 15自由度机器人资料 (15-DOF Humanoid Robot Materials)

Associated with the [[WallClimber]] project.

## Overview
Reference and development materials for a 15-degree-of-freedom humanoid robot. Includes installation documentation, serial communication protocols, action group files, debugging software, hardware schematics, and controller drivers.

## Contents

### Documentation
- `15自由度人形机器人安装说明书.pdf` — full installation manual for the 15-DOF humanoid robot.
- `控制器使用说明书/` — controller user manual.
- `动作调试软件使用说明/` — action debugging software user manual.
- `遥控手柄使用说明.doc` — remote control gamepad user manual.

### Software & Drivers
- `动作调试软件/` — action group debugging software.
- `手机控制安卓APP软件安装文件/` — Android app for mobile control.
- `控制器USB驱动/` — USB driver for the controller.
- `控制器简易演示视频/` — demo video for the controller.

### Hardware
- `结构零件图/` — structural parts diagrams.

### Serial Communication Protocol
- `二次开发串口通信协议/` — serial communication protocol for secondary development, containing:
  - `通信协议.doc` — communication protocol documentation.
  - `51单片机通信例程/` — 51 microcontroller (STC12C5A60S2) communication example (Keil project with `main.c`, `myfun.c/h`, `GamePad.uvproj`).
  - `STM32F103串口通信/` — STM32F103 serial communication example.
  - `串口调用动作组(晶振11.0592M)/` — action group serial call example at 11.0592 MHz crystal.
  - `串口调用动作组(晶振22.1184M)/` — action group serial call example at 22.1184 MHz crystal.

### Action Groups
- `动作组文件/` — pre-defined robot action group files.

## Technologies
- 51 microcontroller (STC12C5A60S2), Keil IDE.
- STM32F103.
- Serial (UART) communication.
- Android app control.
