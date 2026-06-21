# CLAUDE.md — Second Brain Instructions

## Project Structure

This vault is Adrian's AI second brain, hosted in Obsidian.

- `raw/` — Source material: dropped-in PDFs, notes, clippings, and drafts. Claude reads this but does not edit it.
- `wiki/` — Claude-maintained knowledge base of cross-linked pages organised by topic. Sub-folders: `concepts/`, `people/`, `projects/`. The running log lives at `wiki/log.md`.

## Page Conventions

Every wiki page must include YAML frontmatter at the top:

```yaml
---
title: Page Title In Title Case
type: concept | person | project | index
last-updated: YYYY-MM-DD
---
```

- Titles use Title Case.
- Internal links use `[[Wiki Links]]` with the page name matching the file name.
- Every bullet point ends with a full stop.
- Tag related pages using `[[link]]` inline in the body text.

## Style Guide

- Write in second person ("you are working on…") where addressing Adrian directly; otherwise use third person for factual entries.
- Use plain English. Prefer short, common words over jargon unless the term is a defined concept.
- One idea per sentence.
- No em dashes. Use a comma, a colon, or a new sentence instead.
- Use **bold** for emphasis. Use it sparingly so it retains weight.

## Domain Context

Adrian Ao Pak Lon is a university student based in Macau, previously at Pui Ching Middle School (Coloane Campus).

### Field

Computer science and AI, with a focus on machine learning research and educational technology. Also active in UX/UI design and product management.

### Technical Interests

- **Machine Learning and Deep Learning:** CNNs, VAEs, RNNs, Transformers.
- **Reinforcement Learning:** Q-learning, Soft Actor-Critic (SAC).
- **Vision-Language-Action (VLA) models:** LeRobot framework, SO-101 robotic arm, Makermods hardware.
- **Competitive ML:** Currently competing in the Kaggle Pokemon TCG AI Battle Challenge (strategy track).

### Active Projects

- **AI Tutoring Bias Study** (co-authored with Benjamin Tam at Pui Ching): Investigates whether eight major LLM platforms (ChatGPT, Gemini, Claude, Grok, DeepSeek, Qwen, Doubao, Yiyan) produce significantly different tutoring quality across Cantonese-dominant, Mandarin-dominant, and English-dominant Secondary 2 students in Macau. Uses a within-subject repeated-measures ANOVA design with a 100-point blinded rubric. Analysis implemented in Python (scipy, pingouin, pandas).
- **Robo Fest** and **WRO (World Robot Olympiad):** Robotics competition proposals (details to be ingested from raw PDFs).
- **WhaleRapy Stanford Proposal:** A proposal submitted in the context of Stanford (details to be ingested from raw PDF).
- **Kaggle Pokemon TCG AI Battle Challenge:** Strategy-track competition requiring AI game-play agents.

### Organisation

**Pui Ching Middle School (Coloane Campus), Macau** — the institution where the AI tutoring bias study is conducted and where several project proposals originate.

### Key People

| Name             | Role / Relationship                                  |
| ---------------- | ---------------------------------------------------- |
| **Benjamin Tam** | Co-author on the AI tutoring bias research proposal. |
| **Bianca**       | Robotics teammate.                                   |
| **Ashley**       | Robotics teammate.                                   |
| **Oscar**        | Robotics teammate.                                   |
| **Cabrina**      | Robotics teammate.                                   |
| **Peony**        | Robotics teammate.                                   |

### What Claude Helps With

- Researching academic literature and summarising findings.
- Drafting proposals, reports, leaflets, and presentations.
- Processing raw notes into structured wiki pages.
- Answering questions by searching across the wiki and raw material.
