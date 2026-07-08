---
title: Kaggle Pokemon TCG AI Battle Challenge
type: project
last-updated: 2026-07-07
---

# Kaggle Pokemon TCG AI Battle Challenge

The Kaggle Pokémon TCG AI Battle Challenge is a Kaggle competition in which agents play the Pokémon Trading Card Game. Adrian joined in July 2026 and chose the strategy track (as opposed to the speed track).

## Project Directory

`C:\Users\user\OneDrive\PTCG-Hackathon`

## Strategy and Approach

Claude assessed Gemini's initial advice (which recommended AlphaZero / ISMCTS or PPO with self-play) as technically sound but over-ambitious for a solo competition. The agreed approach:

1. Start with a **rule-based heuristic agent** as the baseline.
2. Layer in a learned policy (PPO or similar) only if time allows within the ~3-month window.

Key constraints the agent must handle: hidden information (opponent's hand is not visible), severe action-space constraints, and the large branching factor of the TCG game tree.

## Timeline

- July 2026: project started, directory set up, strategy decided.
- ~October 2026: approximate competition window close (3-month estimate).

## Technologies

- Python (uv-managed environment in `C:\Users\user\OneDrive\PTCG-Hackathon`).
- Potential libraries: PyTorch (for RL policy), competition SDK (Kaggle-provided).

## Status

Early stage: heuristic baseline in development. Competition SDK setup and initial agent structure being established as of 2026-07-06.

## Related Projects

- [[Whalerapy]]: separate concurrent project.
- Machine learning work including PyTorch models and YOLOv8 from prior projects informs this work.
