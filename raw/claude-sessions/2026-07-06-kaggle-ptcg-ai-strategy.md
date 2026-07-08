> claude-sessions: Adrian, Kaggle Pokemon TCG AI strategy. Adrian joined the Kaggle Pokemon TCG AI Battle Challenge and discussed strategy with Claude, who recommended a rule-based heuristic approach before advanced RL.

---
source: claude-code
captured: 2026-07-06
session_id: 26c0c535-471c-4af9-9981-89c07b6e4f2b
---

## Session Summary

Adrian asked for help with the **Kaggle Pokemon TCG AI Battle Challenge**, sharing advice he had received from Gemini (which recommended AlphaZero/ISMCTS or PPO with self-play).

Claude's assessment:

- Gemini's advice is technically sound but over-ambitious for a 3-month solo competition.
- AlphaZero/ISMCTS is a research project scope, not a hackathon approach.
- **Recommendation: start with a rule-based heuristic agent** before attempting PPO or self-play.

The project directory is `C:\Users\user\OneDrive\PTCG-Hackathon`. At the start of the session, the directory was empty.

## Key Decisions

- Strategy track chosen (not speed track).
- Start with rule-based heuristics as the baseline, then layer in learned policy if time permits.
- Claude provided a realistic 3-month timeline and assessment of the competition constraints (hidden information, severe action-space constraints).

## Open Questions

- Which specific heuristics were implemented, if any, is not captured in the header alone.
- Whether a competition SDK was downloaded or a project structure set up is unknown (session is 8 MB, suggesting significant work).

## Related Projects

- [[Kaggle Pokemon TCG AI Battle Challenge]] wiki page.
